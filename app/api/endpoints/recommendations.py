from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.models.product import ProductOut
from app.services.recommendation_service import get_recommendations
from app.db.base import get_db
from app.core.auth import get_current_user
from app.models.user import UserOut

router = APIRouter()

@router.get("/", response_model=list[ProductOut])
def get_user_recommendations(
    current_user: UserOut = Depends(get_current_user),
    lat: float = Query(None, description="User latitude"), 
    lon: float = Query(None, description="User longitude"),
    db: Session = Depends(get_db)
):
    return get_recommendations(db, current_user.id, lat, lon)
