from pydantic import BaseModel
from datetime import datetime

class DeliveryBase(BaseModel):
    tracking_number: str | None = None
    estimated_delivery: datetime | None = None

class DeliveryCreate(DeliveryBase):
    order_id: int

class DeliveryUpdate(BaseModel):
    status: str | None = None
    tracking_number: str | None = None
    estimated_delivery: datetime | None = None

class DeliveryOut(DeliveryBase):
    id: int
    order_id: int
    status: str
    updated_at: datetime

    class Config:
        from_attributes = True
