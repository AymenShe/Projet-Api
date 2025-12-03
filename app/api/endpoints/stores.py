from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.store import StoreCreate, StoreOut
from app.services.store_service import create_new_store, get_all_stores_service, get_nearby_stores
from app.services.geolocation_service import get_coordinates
from app.db.base import get_db
router = APIRouter()

@router.post("/", response_model=StoreOut)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    return create_new_store(db, store)

@router.get("/", response_model=list[StoreOut])
def list_stores(db: Session = Depends(get_db)):
    return get_all_stores_service(db)

@router.get("/nearby", response_model=list[StoreOut])
def find_nearby_stores(
    lat: float = Query(None, description="Latitude of the user"),
    lon: float = Query(None, description="Longitude of the user"),
    q: str = Query(None, description="Address or city to search"),
    radius: float = Query(10.0, description="Search radius in km"),
    db: Session = Depends(get_db)
):
    if q:
        coords = get_coordinates(q)
        if coords:
            lat, lon = coords
        else:
            raise HTTPException(status_code=404, detail="Address not found")
    
    if lat is None or lon is None:
        raise HTTPException(status_code=400, detail="Either lat/lon or q must be provided")

    return get_nearby_stores(db, lat, lon, radius)
