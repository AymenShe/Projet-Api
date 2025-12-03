from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.order import OrderCreate, OrderUpdate, OrderOut
from app.services.order_service import (
    create_new_order,
    get_order_by_id,
    update_order_status_service,
)
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, user_id: int, db: Session = Depends(get_db)):
    # In a real app, user_id would come from the authenticated user
    try:
        return create_new_order(db, order, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", response_model=OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order_by_id(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}/cancel", response_model=OrderOut)
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    db_order = update_order_status_service(db, order_id, "cancelled")
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
