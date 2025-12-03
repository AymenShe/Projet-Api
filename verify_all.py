import requests
import json

BASE_URL = "http://localhost:8001"

def test_flow():
    # 1. Create User
    print("Creating User...")
    user_data = {
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User"
    }
    try:
        response = requests.post(f"{BASE_URL}/users/", json=user_data)
        if response.status_code == 200:
            user = response.json()
            print(f"User created: {user['id']}")
        elif response.status_code == 400 and "Email already registered" in response.text:
            print("User already exists, fetching...")
            # Assuming we can't easily fetch by email without auth in this simple setup, 
            # let's just try to login or assume ID 1 for simplicity if we just started fresh.
            # Or better, let's just use a random email
            import random
            user_data["email"] = f"test{random.randint(1, 10000)}@example.com"
            response = requests.post(f"{BASE_URL}/users/", json=user_data)
            user = response.json()
            print(f"User created: {user['id']}")
        else:
            print(f"Failed to create user: {response.text}")
            return
    except Exception as e:
        print(f"Error creating user: {e}")
        return

    user_id = user['id']
    print(user_id)
    # 2. Create Product (if not exists)
    print("Creating Product...")
    product_data = {
        "name": "Test Product",
        "description": "A test product",
        "price": 10.0,
        "quantity": 100
    }
    response = requests.post(f"{BASE_URL}/products/", json=product_data)
    if response.status_code == 200:
        product = response.json()
        print(f"Product created: {product['id']}")
    else:
        print(f"Failed to create product: {response.text}")
        return

    product_id = product['id']

    # 3. Create Order
    print("Creating Order...")
    order_data = {
        "items": [
            {"product_id": product_id, "quantity": 2}
        ]
    }
    response = requests.post(f"{BASE_URL}/orders/", params={"user_id": user_id}, json=order_data)
    if response.status_code == 200:
        order = response.json()
        print(f"Order created: {order['id']}, Total: {order['total_price']}")
    else:
        print(f"Failed to create order: {response.text}")
        return

    order_id = order['id']

    # 4. Create Payment
    print("Processing Payment...")
    payment_data = {
        "amount": order['total_price'],
        "order_id": order_id
    }
    response = requests.post(f"{BASE_URL}/payments/", json=payment_data)
    if response.status_code == 200:
        payment = response.json()
        print(f"Payment processed: {payment['id']}, Status: {payment['status']}")
    else:
        print(f"Failed to process payment: {response.text}")

    # 5. Create Delivery
    print("Creating Delivery...")
    delivery_data = {
        "order_id": order_id
    }
    response = requests.post(f"{BASE_URL}/deliveries/", json=delivery_data)
    if response.status_code == 200:
        delivery = response.json()
        print(f"Delivery created: {delivery['id']}, Tracking: {delivery['tracking_number']}")
    else:
        print(f"Failed to create delivery: {response.text}")

    # 6. Create Review
    print("Creating Review...")
    review_data = {
        "product_id": product_id,
        "rating": 5,
        "comment": "Great product!"
    }
    response = requests.post(f"{BASE_URL}/reviews/", params={"user_id": user_id}, json=review_data)
    if response.status_code == 200:
        review = response.json()
        print(f"Review created: {review['id']}")
    else:
        print(f"Failed to create review: {response.text}")

    # 7. Get Recommendations
    print("Getting Recommendations...")
    response = requests.get(f"{BASE_URL}/recommendations/{user_id}")
    if response.status_code == 200:
        recs = response.json()
        print(f"Recommendations: {len(recs)} items")
    else:
        print(f"Failed to get recommendations: {response.text}")

if __name__ == "__main__":
    test_flow()
