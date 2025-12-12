from sqlalchemy.orm import Session
from app.db.models import Product, User, Order, OrderItem, Payment, Review, Delivery, Store
from app.models.product import ProductCreate, ProductUpdate
from app.models.user import UserCreate, UserUpdate
from app.models.order import OrderCreate, OrderUpdate
from app.models.payment import PaymentCreate, PaymentUpdate
from app.models.review import ReviewCreate, ReviewUpdate
from app.models.delivery import DeliveryCreate, DeliveryUpdate
from app.models.store import StoreCreate, StoreUpdate
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    """Authenticate user by email and password"""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        address=user.address,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    update_data = user_update.model_dump(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data["password"])
        del update_data["password"]
    
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Order CRUD
def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()

def create_order(db: Session, order: OrderCreate, user_id: int):
    # Create order
    db_order = Order(
        user_id=user_id, 
        status="pending", 
        total_price=0.0
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Process items
    total_price = 0.0
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product and product.quantity >= item.quantity:
            price = product.price
            total_price += price * item.quantity
            db_item = OrderItem(
                order_id=db_order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=price
            )
            db.add(db_item)
            # Update stock
            product.quantity -= item.quantity
        else:
            # Rollback if stock insufficient
            db.delete(db_order)
            db.commit()
            raise ValueError(f"Insufficient stock for product {item.product_id}")
            
    db_order.total_price = total_price
    db.commit() # Commit order and items before payment
    
    # Process Payment using Service
    from app.services import payment_service
    payment_create = PaymentCreate(
        amount=total_price,
        order_id=db_order.id
    )
    # process_payment calls create_payment which updates order status to 'paid' if successful
    payment_service.process_payment(db, payment_create, order.payment)
    
    # Handle Delivery (if needed, we can store it or just acknowledge it)
    if order.delivery_type == "shipping":
        db_delivery = Delivery(
            order_id=db_order.id,
            status="pending",
            estimated_delivery=datetime.utcnow() + timedelta(days=3)
        )
        db.add(db_delivery)
        db.commit()
    elif order.delivery_type == "pickup":
        # Logic for pickup could go here
        pass
        
    db.refresh(db_order)
    return db_order

def update_order_status(db: Session, order_id: int, status: str):
    db_order = get_order(db, order_id)
    if db_order:
        db_order.status = status
        db.commit()
        db.refresh(db_order)
    return db_order

# Payment CRUD
def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    # Update order status
    order = get_order(db, payment.order_id)
    if order:
        order.status = "paid"
        db.commit()
    return db_payment

# Review CRUD
def get_reviews_by_product(db: Session, product_id: int):
    return db.query(Review).filter(Review.product_id == product_id).all()

def create_review(db: Session, review: ReviewCreate, user_id: int):
    db_review = Review(**review.model_dump(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# Delivery CRUD
def get_delivery(db: Session, delivery_id: int):
    return db.query(Delivery).filter(Delivery.id == delivery_id).first()

def get_delivery_by_order_id(db: Session, order_id: int):
    return db.query(Delivery).filter(Delivery.order_id == order_id).first()

def create_delivery(db: Session, delivery: DeliveryCreate):
    db_delivery = Delivery(**delivery.model_dump())
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def update_delivery_status(db: Session, delivery_id: int, delivery_update: DeliveryUpdate):
    db_delivery = get_delivery(db, delivery_id)
    if not db_delivery:
        return None
    update_data = delivery_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_delivery, key, value)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

# Store CRUD
def get_store(db: Session, store_id: int):
    return db.query(Store).filter(Store.id == store_id).first()

def get_all_stores(db: Session):
    return db.query(Store).all()

def create_store(db: Session, store: StoreCreate):
    db_store = Store(**store.model_dump())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump()) #product.dict()
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    update_data = product_update.model_dump(exclude_unset=True) #product_update.dict()
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
