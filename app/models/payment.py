from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    amount: float
    status: str = "pending"

class PaymentCreate(PaymentBase):
    order_id: int
    transaction_id: str | None = None

class PaymentUpdate(BaseModel):
    status: str | None = None
    transaction_id: str | None = None

class PaymentOut(PaymentBase):
    id: int
    order_id: int
    transaction_id: str | None
    created_at: datetime

    class Config:
        from_attributes = True
