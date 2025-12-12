import strawberry
from typing import List, Optional
from app.db import models

@strawberry.type
class ProductType:
    id: int
    name: str
    description: Optional[str]
    category: Optional[str]
    price: float
    quantity: int
    rating: float
    image_url: Optional[str]

    @classmethod
    def from_model(cls, model: models.Product):
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            category=model.category,
            price=model.price,
            quantity=model.quantity if model.quantity is not None else 0,
            rating=model.rating,
            image_url=model.image_url
        )

@strawberry.type
class StoreType:
    id: int
    name: str
    address: str
    latitude: float
    longitude: float

    @classmethod
    def from_model(cls, model: models.Store):
        return cls(
            id=model.id,
            name=model.name,
            address=model.address,
            latitude=model.latitude,
            longitude=model.longitude
        )
