from sqlalchemy.orm import Session
from app.db import crud
from app.models.payment import PaymentCreate

def process_payment(db: Session, payment: PaymentCreate):
    # Mock payment processing logic here
    # In a real app, we would integrate with Stripe/PayPal
    payment.status = "completed"
    payment.transaction_id = "txn_mock_12345"
    return crud.create_payment(db, payment)

def get_payment_details(db: Session, payment_id: int):
    return crud.get_payment(db, payment_id)
