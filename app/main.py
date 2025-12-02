from fastapi import FastAPI
from app.api.endpoints import products

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
