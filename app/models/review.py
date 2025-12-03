from pydantic import BaseModel
from datetime import datetime

class ReviewBase(BaseModel):
    rating: int
    comment: str | None = None

class ReviewCreate(ReviewBase):
    product_id: int

class ReviewUpdate(BaseModel):
    rating: int | None = None
    comment: str | None = None

class ReviewOut(ReviewBase):
    id: int
    user_id: int
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True
