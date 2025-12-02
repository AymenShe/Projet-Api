from app.db.base import Base, engine

# Import all models so they are registered with Base
from app.db.models import Product

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
