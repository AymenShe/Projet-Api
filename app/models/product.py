from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    category: str | None = None
    price: float
    quantity: int = 0
    rating: float = 0.0
    image_url: str | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True