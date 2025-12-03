from app.db.base import SessionLocal
from app.models.store import StoreCreate
from app.services.store_service import create_new_store

stores = [
    {
        "name": "MotoShop Paris Central",
        "address": "10 Rue de Rivoli, 75001 Paris",
        "latitude": 48.8556,
        "longitude": 2.3470
    },
    {
        "name": "MotoShop Bastille",
        "address": "Place de la Bastille, 75011 Paris",
        "latitude": 48.8531,
        "longitude": 2.3691
    },
    {
        "name": "MotoShop Champs-Élysées",
        "address": "Av. des Champs-Élysées, 75008 Paris",
        "latitude": 48.8698,
        "longitude": 2.3075
    }
]

def seed_stores():
    db = SessionLocal()
    try:
        for s_data in stores:
            store_in = StoreCreate(**s_data)
            create_new_store(db, store_in)
            print(f"Added store: {s_data['name']}")
        print("Store seeding completed successfully.")
    except Exception as e:
        print(f"Error seeding stores: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_stores()
