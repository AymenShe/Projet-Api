from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any
from app.models.payment import PaymentDetails

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemOut(OrderItemBase):
    id: int
    price: float

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    pass

class OrderCreate(OrderBase):
    items: List[OrderItemBase]
    delivery_type: str
    pickup_point: Dict[str, Any] | None = None
    payment: PaymentDetails

class OrderUpdate(BaseModel):
    status: str | None = None

class OrderOut(OrderBase):
    id: int
    user_id: int
    status: str
    total_price: float
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True
