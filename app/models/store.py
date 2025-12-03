from pydantic import BaseModel

class StoreBase(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float

class StoreCreate(StoreBase):
    pass

class StoreUpdate(BaseModel):
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None

class StoreOut(StoreBase):
    id: int

    class Config:
        from_attributes = True
