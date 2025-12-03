from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.product import ProductCreate, ProductUpdate, ProductOut
from app.services.product_service import (
    create_new_product,
    get_product_by_id,
    get_all_products_service,
    update_product_service,
    delete_product_service,
)
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_new_product(db, product)

@router.get("/", response_model=list[ProductOut])
def list_products(
    skip: int = 0,
    limit: int = 100,
    search: str = Query(None, description="Search query for product name"),
    category: str = Query(None, description="Category filter"),
    db: Session = Depends(get_db)
):
    products = get_all_products_service(db)
    
    if search:
        products = [p for p in products if search.lower() in p.name.lower()]
    if category:
        products = [p for p in products if p.category == category]
        
    return products[skip : skip + limit]

@router.get("/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = update_product_service(db, product_id, product_update)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = delete_product_service(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
