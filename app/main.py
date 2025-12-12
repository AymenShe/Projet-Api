from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from app.api.endpoints import products, users, orders, payments, reviews, recommendations, deliveries, stores
from app.db.base import engine, Base
from app.core.rate_limit import limiter

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4000", "http://localhost:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(deliveries.router, prefix="/deliveries", tags=["deliveries"])
app.include_router(stores.router, prefix="/stores", tags=["stores"])

from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
