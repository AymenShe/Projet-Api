from sqlalchemy.orm import Session
from app.db import crud

def get_recommendations(db: Session, user_id: int, lat: float = None, lon: float = None):
    # Mock AI recommendation logic
    # Simple logic: Recommend products the user hasn't bought yet, or popular products
    # If location is provided, we could filter by availability in nearby stores (if we had that link)
    # For now, just return all products as a simple "recommendation"
    all_products = crud.get_all_products(db)
    return all_products[:5] # Return top 5 products
