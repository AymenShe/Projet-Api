import strawberry
from typing import List, Optional
from app.graphql.types import ProductType, StoreType
from app.db.base import get_db
from app.db import crud
from app.db import models
from sqlalchemy.orm import Session

@strawberry.type
class Query:
    @strawberry.field
    def products(self, limit: int = 10, offset: int = 0) -> List[ProductType]:
        db: Session = next(get_db())
        products = db.query(models.Product).offset(offset).limit(limit).all()
        return [ProductType.from_model(p) for p in products]

    @strawberry.field
    def product(self, id: int) -> Optional[ProductType]:
        db: Session = next(get_db())
        product = crud.get_product(db, id)
        if product:
            return ProductType.from_model(product)
        return None

    @strawberry.field
    def stores(self) -> List[StoreType]:
        db: Session = next(get_db())
        stores = crud.get_all_stores(db)
        return [StoreType.from_model(s) for s in stores]

schema = strawberry.Schema(query=Query)
