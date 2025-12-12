from sqlalchemy.orm import Session
from app.db import crud
from app.models.payment import PaymentCreate, PaymentDetails
from app.core.config import settings
import stripe

def process_payment(db: Session, payment: PaymentCreate, card_details: PaymentDetails | None = None):
    if settings.stripe_api_key and card_details:
        try:
            stripe.api_key = settings.stripe_api_key
            
            try:
                exp_month, exp_year = card_details.exp.split('/')
                exp_year = "20" + exp_year if len(exp_year) == 2 else exp_year
            except ValueError:
                exp_month = 12
                exp_year = 2025

            payment_method = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": card_details.cardNumber,
                    "exp_month": int(exp_month),
                    "exp_year": int(exp_year),
                    "cvc": card_details.cvc,
                },
            )

            intent = stripe.PaymentIntent.create(
                amount=int(payment.amount * 100),
                currency="usd",
                payment_method=payment_method.id,
                confirm=True,
                automatic_payment_methods={
                    'enabled': True,
                    'allow_redirects': 'never'
                }
            )
            
            payment.transaction_id = intent.id
            payment.status = "completed" if intent.status == "succeeded" else intent.status

        except Exception as e:
            print(f"Stripe Error: {e}")
            payment.status = "failed"
            payment.transaction_id = f"failed_{e}"
            
    else:
        payment.status = "completed"
        payment.transaction_id = "txn_mock_12345"

    return crud.create_payment(db, payment)

def get_payment_details(db: Session, payment_id: int):
    return crud.get_payment(db, payment_id)
