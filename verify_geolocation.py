import requests
import json

BASE_URL = "http://localhost:8001"

def test_geolocation():
    print("Testing Geolocation Features...")

    # 1. Create a Store with Address (should auto-fetch coords)
    print("Creating Store with Address...")
    store_data = {
        "name": "Paris Store",
        "address": "Eiffel Tower, Paris, France",
        "latitude": 0.0,
        "longitude": 0.0
    }
    try:
        response = requests.post(f"{BASE_URL}/stores/", json=store_data)
        if response.status_code == 200:
            store = response.json()
            print(f"Store created: {store['name']} at ({store['latitude']}, {store['longitude']})")
        else:
            print(f"Failed to create store: {response.text}")
    except Exception as e:
        print(f"Error creating store: {e}")

    # 2. Create another store manually
    print("Creating Store manually...")
    store_data_2 = {
        "name": "London Store",
        "address": "London, UK",
        "latitude": 51.5074,
        "longitude": -0.1278
    }
    requests.post(f"{BASE_URL}/stores/", json=store_data_2)

    # 3. Find Nearby Stores (from a point near Paris)
    print("Finding Nearby Stores...")
    # Coordinates near Eiffel Tower
    lat = 48.85
    lon = 2.30
    response = requests.get(f"{BASE_URL}/stores/nearby", params={"lat": lat, "lon": lon, "radius": 20})
    if response.status_code == 200:
        stores = response.json()
        print(f"Found {len(stores)} stores near ({lat}, {lon})")
        for s in stores:
            print(f" - {s['name']}")
    else:
        print(f"Failed to find nearby stores: {response.text}")

    # 4. Get Recommendations with Location
    print("Getting Recommendations with Location...")
    response = requests.get(f"{BASE_URL}/recommendations/1", params={"lat": lat, "lon": lon})
    if response.status_code == 200:
        recs = response.json()
        print(f"Recommendations received: {len(recs)}")
    else:
        print(f"Failed to get recommendations: {response.text}")

if __name__ == "__main__":
    test_geolocation()
