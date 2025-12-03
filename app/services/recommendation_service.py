from sqlalchemy.orm import Session
from app.db import crud
from app.models.order import Order
from app.models.product import Product
from collections import Counter

def get_recommendations(db: Session, user_id: int, lat: float = None, lon: float = None):
    user_orders = crud.get_orders_by_user(db, user_id)
    
    purchased_product_ids = set()
    category_counts = Counter()
    
    for order in user_orders:
        for item in order.items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if product:
                purchased_product_ids.add(product.id)
                if product.category:
                    category_counts[product.category] += item.quantity

    preferred_categories = [cat for cat, count in category_counts.most_common(3)]
    
    all_products = crud.get_all_products(db)
    
    recommendations = []
    
    for product in all_products:
        if product.id in purchased_product_ids:
            continue
            
        score = 0
        if product.category in preferred_categories:
            score += 10
        
        score += product.rating
        
        if score > 0:
            recommendations.append((score, product))
            
    recommendations.sort(key=lambda x: x[0], reverse=True)
    
    final_recommendations = [r[1] for r in recommendations]
    
    if len(final_recommendations) < 5:
        top_rated = sorted([p for p in all_products if p.id not in purchased_product_ids], 
                           key=lambda x: x.rating, reverse=True)
        for p in top_rated:
            if p not in final_recommendations:
                final_recommendations.append(p)
                if len(final_recommendations) >= 5:
                    break
                    
    return final_recommendations[:5]
