from sqlalchemy.orm import Session
from app.db import crud
from app.models.user import UserCreate, UserUpdate

def create_new_user(db: Session, user: UserCreate):
    return crud.create_user(db, user)

def get_user_by_id(db: Session, user_id: int):
    return crud.get_user(db, user_id)

def get_user_by_email_service(db: Session, email: str):
    return crud.get_user_by_email(db, email)

def update_user_service(db: Session, user_id: int, user_update: UserUpdate):
    return crud.update_user(db, user_id, user_update)

def delete_user_service(db: Session, user_id: int):
    return crud.delete_user(db, user_id)

def authenticate_user_service(db: Session, email: str, password: str):
    return crud.authenticate_user(db, email, password)
