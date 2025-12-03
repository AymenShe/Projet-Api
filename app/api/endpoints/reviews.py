from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.review import ReviewCreate, ReviewOut
from app.services.review_service import add_review, get_product_reviews
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=ReviewOut)
def create_review(review: ReviewCreate, user_id: int, db: Session = Depends(get_db)):
    # In a real app, user_id would come from the authenticated user
    return add_review(db, review, user_id)

@router.get("/product/{product_id}", response_model=list[ReviewOut])
def read_product_reviews(product_id: int, db: Session = Depends(get_db)):
    return get_product_reviews(db, product_id)
