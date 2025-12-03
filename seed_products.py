from app.db.base import SessionLocal
from app.db.models import Product

products = [
  {
    "name": "Casque Arai RX-7V",
    "description": "Casque intégral haut de gamme ventilation optimisée.",
    "category": "Casque",
    "price": 799.9,
    "quantity": 12,
    "rating": 4.8,
    "image_url": "/images/arai.jpg"
  },
  {
    "name": "Gants chauffants RiderHeat",
    "description": "Chauffage intégré, waterproof, batteries amovibles.",
    "category": "Gant",
    "price": 189.0,
    "quantity": 25,
    "rating": 4.4,
    "image_url": "/images/Gant.jpg"
  },
  {
    "name": "Veste Airbag X3",
    "description": "Airbag intégré, certification CE, doublure hiver.",
    "category": "Veste",
    "price": 499.99,
    "quantity": 8,
    "rating": 4.7,
    "image_url": "/images/vesteairbagx3.jpg"
  },
  {
    "name": "Chaussures StormRide",
    "description": "Imperméables, renfort malléole, semelle anti-dérapante.",
    "category": "Protection",
    "price": 159.0,
    "quantity": 30,
    "rating": 4.2,
    "image_url": "/images/pas_image.png"
  },
  {
    "name": "Pantalon RoadGuard",
    "description": "Textile Cordura, protections genoux/hanche.",
    "category": "Protection",
    "price": 229.0,
    "quantity": 15,
    "rating": 4.3,
    "image_url": "/images/pas_image.png"
  },
  {
    "name": "Blouson Mesh SummerFlow",
    "description": "Ultra aéré pour l’été, coques CE.",
    "category": "Veste",
    "price": 179.0,
    "quantity": 20,
    "rating": 4.1,
    "image_url": "/images/pas_image.png"
  }
]

def seed_products():
    db = SessionLocal()
    try:
        # Check if products already exist to avoid duplicates if run multiple times
        # For this task, we can just clear and re-seed or append. 
        # Given the instruction to "implement the structure... and the exact values",
        # and the plan to reset DB, we just add them.
        
        for p_data in products:
            # Check if product exists by name
            existing = db.query(Product).filter(Product.name == p_data["name"]).first()
            if not existing:
                product = Product(**p_data)
                db.add(product)
                print(f"Adding product: {p_data['name']}")
            else:
                print(f"Product already exists: {p_data['name']}")
        
        db.commit()
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"Error seeding products: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_products()
