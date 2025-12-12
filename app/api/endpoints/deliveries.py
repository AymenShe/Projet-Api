from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.delivery import DeliveryCreate, DeliveryUpdate, DeliveryOut
from app.services.delivery_service import create_delivery_record, get_delivery_status, update_delivery
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=DeliveryOut)
def create_delivery(delivery: DeliveryCreate, db: Session = Depends(get_db)):
    return create_delivery_record(db, delivery)

@router.get("/{delivery_id}", response_model=DeliveryOut)
def read_delivery(delivery_id: int, db: Session = Depends(get_db)):
    db_delivery = get_delivery_status(db, delivery_id)
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return db_delivery

@router.get("/order/{order_id}", response_model=DeliveryOut)
def read_delivery_by_order(order_id: int, db: Session = Depends(get_db)):
    from app.db import crud
    db_delivery = crud.get_delivery_by_order_id(db, order_id)
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found for this order")
    return db_delivery

@router.put("/{delivery_id}", response_model=DeliveryOut)
def update_delivery_info(delivery_id: int, delivery_update: DeliveryUpdate, db: Session = Depends(get_db)):
    db_delivery = update_delivery(db, delivery_id, delivery_update)
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return db_delivery
