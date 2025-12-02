from sqlalchemy.orm import Session
from app.db import crud
from app.models.product import ProductCreate, ProductUpdate

def create_new_product(db: Session, product: ProductCreate):
    return crud.create_product(db, product)

def get_product_by_id(db: Session, product_id: int):
    return crud.get_product(db, product_id)

def get_all_products_service(db: Session):
    return crud.get_all_products(db)

def update_product_service(db: Session, product_id: int, product_update: ProductUpdate):
    return crud.update_product(db, product_id, product_update)

def delete_product_service(db: Session, product_id: int):
    return crud.delete_product(db, product_id)
