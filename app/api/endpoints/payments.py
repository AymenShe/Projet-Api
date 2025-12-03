from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.payment import PaymentCreate, PaymentOut
from app.services.payment_service import process_payment, get_payment_details
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=PaymentOut)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return process_payment(db, payment)

@router.get("/{payment_id}", response_model=PaymentOut)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = get_payment_details(db, payment_id)
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
