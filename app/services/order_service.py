from sqlalchemy.orm import Session
from app.db import crud
from app.models.order import OrderCreate, OrderUpdate

def create_new_order(db: Session, order: OrderCreate, user_id: int):
    return crud.create_order(db, order, user_id)

def get_order_by_id(db: Session, order_id: int):
    return crud.get_order(db, order_id)

def get_user_orders(db: Session, user_id: int):
    return crud.get_orders_by_user(db, user_id)

def update_order_status_service(db: Session, order_id: int, status: str):
    return crud.update_order_status(db, order_id, status)
