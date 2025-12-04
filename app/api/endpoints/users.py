from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.models.user import UserCreate, UserUpdate, UserOut, UserLogin, LoginResponse
from app.models.order import OrderOut
from app.services.user_service import (
    create_new_user,
    get_user_by_id,
    get_user_by_email_service,
    update_user_service,
    delete_user_service,
    authenticate_user_service,
)
from app.services.order_service import get_user_orders
from app.core.auth import create_access_token, get_current_user
from app.db.base import get_db
from app.core.rate_limit import limiter

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email_service(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_new_user(db, user)

@router.post("/login", response_model=LoginResponse)
@limiter.limit("5/minute")
def login(request: Request, credentials: UserLogin, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token"""
    user = authenticate_user_service(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token(user.id, user.email)
    return LoginResponse(token=token, user=user)

@router.get("/me/orders", response_model=list[OrderOut])
def read_current_user_orders(current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_user_orders(db, current_user.id)

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this user")
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user")
    db_user = update_user_service(db, user_id, user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")
    db_user = delete_user_service(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/{user_id}/orders", response_model=list[OrderOut])
def read_user_orders(user_id: int, current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access these orders")
    return get_user_orders(db, user_id)
