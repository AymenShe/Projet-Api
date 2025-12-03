from sqlalchemy.orm import Session
from app.db import crud
from app.models.review import ReviewCreate

def add_review(db: Session, review: ReviewCreate, user_id: int):
    return crud.create_review(db, review, user_id)

def get_product_reviews(db: Session, product_id: int):
    return crud.get_reviews_by_product(db, product_id)
