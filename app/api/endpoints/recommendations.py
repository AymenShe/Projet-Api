from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.models.product import ProductOut
from app.services.recommendation_service import get_recommendations
from app.db.base import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=list[ProductOut])
def get_user_recommendations(
    user_id: int, 
    lat: float = Query(None, description="User latitude"), 
    lon: float = Query(None, description="User longitude"),
    db: Session = Depends(get_db)
):
    return get_recommendations(db, user_id, lat, lon)
