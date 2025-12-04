import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base, get_db
from app.core.auth import create_access_token

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_security.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_sql_injection_login():
    """
    Test that SQL injection attempts fail.
    We attempt to log in with a classic SQL injection payload.
    """
    client.post("/users/", json={
        "email": "victim@example.com",
        "password": "securepassword",
        "full_name": "Victim User",
        "address": "123 Street"
    })

    payload = {
        "email": "victim@example.com' OR '1'='1",
        "password": "wrongpassword"
    }
    
    response = client.post("/users/login", json=payload)
    
    assert response.status_code in [401, 422]

def test_rate_limiting():
    """
    Test that rate limiting is enforced.
    We send many requests rapidly to the login endpoint.
    """
    responses = []
    for _ in range(20):
        responses.append(client.post("/users/login", json={
            "email": "spammer@example.com",
            "password": "password"
        }))
    
    has_429 = any(r.status_code == 429 for r in responses)
    
    assert has_429, "Rate limiting not active! Vulnerability confirmed."

def test_idor_vulnerability():
    """
    Test for Insecure Direct Object Reference (IDOR).
    User A should not be able to update User B's profile.
    """
    res_a = client.post("/users/", json={
        "email": "usera@example.com",
        "password": "passwordA",
        "full_name": "User A",
        "address": "Address A"
    })
    user_a_id = res_a.json()["id"]
    token_a = create_access_token(user_a_id, "usera@example.com")

    res_b = client.post("/users/", json={
        "email": "userb@example.com",
        "password": "passwordB",
        "full_name": "User B",
        "address": "Address B"
    })
    user_b_id = res_b.json()["id"]

    headers = {"Authorization": f"Bearer {token_a}"}
    update_payload = {"full_name": "Hacked by A"}
    
    response = client.put(f"/users/{user_b_id}", json=update_payload, headers=headers)
    
    assert response.status_code in [403, 404], f"IDOR Vulnerability confirmed! User A updated User B. Status: {response.status_code}"
