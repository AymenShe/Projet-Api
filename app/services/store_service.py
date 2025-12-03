from sqlalchemy.orm import Session
from app.db import crud
from app.models.store import StoreCreate
from app.services.geolocation_service import get_coordinates, calculate_distance

def create_new_store(db: Session, store: StoreCreate):
    # If lat/lon are not provided (0.0), try to fetch them from address
    if store.latitude == 0.0 and store.longitude == 0.0:
        coords = get_coordinates(store.address)
        if coords:
            store.latitude, store.longitude = coords
    return crud.create_store(db, store)

def get_all_stores_service(db: Session):
    return crud.get_all_stores(db)

def get_nearby_stores(db: Session, lat: float, lon: float, radius_km: float = 10.0):
    all_stores = crud.get_all_stores(db)
    nearby_stores = []
    for store in all_stores:
        distance = calculate_distance(lat, lon, store.latitude, store.longitude)
        if distance <= radius_km:
            # Add distance to store object for response if needed, 
            # but for now just return the store
            nearby_stores.append(store)
    return nearby_stores
