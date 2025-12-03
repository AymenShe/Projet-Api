import requests
from math import radians, cos, sin, asin, sqrt

def get_coordinates(address: str):
    """
    Get latitude and longitude for an address using OpenStreetMap Nominatim API.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "EcommerceApp/1.0"
    }
    try:
        print(f"Fetching coordinates for: {address}")
        response = requests.get(url, params=params, headers=headers)
        print(f"Response Status: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        print(f"Response Data: {data}")
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        return None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) using Haversine formula.
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r