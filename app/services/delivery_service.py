from sqlalchemy.orm import Session
from app.db import crud
from app.models.delivery import DeliveryCreate, DeliveryUpdate
from datetime import datetime, timedelta

def create_delivery_record(db: Session, delivery: DeliveryCreate):
    # Mock delivery logic
    # Set estimated delivery to 3 days from now
    delivery_data = delivery.model_dump()
    delivery_data['estimated_delivery'] = datetime.utcnow() + timedelta(days=3)
    delivery_data['tracking_number'] = "TRK_MOCK_98765"
    
    # We need to pass a DeliveryCreate object or similar to crud, but crud expects DeliveryCreate
    # Let's just pass the original delivery object and let crud handle it, 
    # but we might need to modify the object or create a new one if we want to add fields.
    # Actually, crud uses **delivery.model_dump(). 
    # So we should probably update the delivery object before passing it, or modify crud.
    # For simplicity, let's just create it as is, and then update it.
    
    db_delivery = crud.create_delivery(db, delivery)
    
    # Update with mock details
    update_data = DeliveryUpdate(
        tracking_number="TRK_MOCK_98765",
        estimated_delivery=datetime.utcnow() + timedelta(days=3),
        status="shipped"
    )
    return crud.update_delivery_status(db, db_delivery.id, update_data)

def get_delivery_status(db: Session, delivery_id: int):
    return crud.get_delivery(db, delivery_id)

def update_delivery(db: Session, delivery_id: int, delivery_update: DeliveryUpdate):
    return crud.update_delivery_status(db, delivery_id, delivery_update)
