"""
Distance Calculator for Sri Lankan Cities
==========================================
Provides multiple ways to calculate distance between cities:
1. City proximity scoring (simple)
2. Haversine distance (real geographical distance in km)
3. Travel time estimation
"""

import math
from typing import Dict, Tuple

# Geographic coordinates (latitude, longitude) for Sri Lankan cities
CITY_COORDINATES: Dict[str, Tuple[float, float]] = {
    # Western Province
    'Colombo': (6.9271, 80.7789),
    'Gampaha': (7.0889, 80.2114),
    'Kalutara': (6.5869, 80.1130),
    
    # Central Province
    'Kandy': (7.2906, 80.6337),
    'Matale': (7.7674, 80.7294),
    'Nuwara Eliya': (6.9497, 80.7891),
    
    # Southern Province
    'Galle': (6.0535, 80.2170),
    'Matara': (5.7490, 80.5371),
    'Hambantota': (6.1256, 81.1242),
    
    # Northern Province
    'Jaffna': (9.6615, 80.7740),
    'Kilinochchi': (9.3834, 80.4050),
    'Mannar': (8.9833, 79.9167),
    
    # Eastern Province
    'Trincomalee': (8.5874, 81.2346),
    'Batticaloa': (7.7132, 81.7687),
    'Ampara': (7.3000, 81.6833),
    
    # North Central Province
    'Anuradhapura': (8.3163, 80.4167),
    'Polonnaruwa': (7.9408, 81.0033),
    
    # Sabaragamuwa Province
    'Ratnapura': (6.6828, 80.4017),
    'Kegalle': (7.2544, 80.6457),
    
    # Uva Province
    'Badulla': (6.9497, 81.2692),
    'Monaragala': (6.8167, 81.3500),
}


def haversine_distance(city1: str, city2: str) -> float:
    """
    Calculate real geographical distance between two cities using Haversine formula.
    
    Formula: 
    a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2(√a, √(1−a))
    d = R ⋅ c (where R is earth's radius ≈ 6371 km)
    
    Args:
        city1: First city name
        city2: Second city name
    
    Returns:
        Distance in kilometers
    """
    if city1 == city2:
        return 0.0
    
    coords1 = CITY_COORDINATES.get(city1)
    coords2 = CITY_COORDINATES.get(city2)
    
    if not coords1 or not coords2:
        return float('inf')  # Unknown city
    
    lat1, lon1 = coords1
    lat2, lon2 = coords2
    
    # Convert to radians
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    # Haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Earth radius in kilometers
    earth_radius_km = 6371
    distance = earth_radius_km * c
    
    return distance


def distance_to_score(distance_km: float, max_distance: float = 500) -> float:
    """
    Convert distance in kilometers to a recommendation score (0.0 to 1.0).
    
    Scoring logic:
    - 0 km (same city) → 1.0
    - 50 km (nearby) → 0.8
    - 100 km (regional) → 0.6
    - 200 km (far) → 0.4
    - 500+ km (very far) → 0.1
    
    Args:
        distance_km: Distance in kilometers
        max_distance: Maximum distance considered (default 500 km)
    
    Returns:
        Score between 0.0 and 1.0
    """
    if distance_km == 0:
        return 1.0
    
    # Decay function: score decreases with distance
    score = max(0.1, 1.0 - (distance_km / max_distance))
    return round(score, 3)


def estimate_travel_time(distance_km: float) -> str:
    """
    Estimate travel time by road in Sri Lanka.
    
    Assumptions:
    - Average speed: 60 km/h
    - Add 10% for traffic and road conditions
    
    Args:
        distance_km: Distance in kilometers
    
    Returns:
        Travel time as formatted string (e.g., "2.5 hours")
    """
    average_speed = 60  # km/h
    hours = distance_km / average_speed * 1.1  # Add 10% overhead
    
    if hours < 1:
        minutes = hours * 60
        return f"{minutes:.0f} minutes"
    elif hours < 2:
        return f"{hours:.1f} hours"
    else:
        return f"{hours:.1f} hours"


def get_distance_info(user_city: str, event_city: str) -> Dict[str, any]:
    """
    Get comprehensive distance information between user and event.
    
    Returns:
        Dictionary with:
        - distance_km: Actual distance in km
        - distance_score: Score for recommendations (0-1)
        - travel_time: Estimated travel time
        - proximity: Human-readable proximity (Same City, Nearby, etc.)
    """
    distance_km = haversine_distance(user_city, event_city)
    distance_score = distance_to_score(distance_km)
    travel_time = estimate_travel_time(distance_km)
    
    # Proximity classification
    if distance_km == 0:
        proximity = "Same City"
    elif distance_km <= 30:
        proximity = "Very Close"
    elif distance_km <= 80:
        proximity = "Nearby"
    elif distance_km <= 150:
        proximity = "Regional"
    elif distance_km <= 300:
        proximity = "Far"
    else:
        proximity = "Very Far"
    
    return {
        'distance_km': round(distance_km, 1),
        'distance_score': distance_score,
        'travel_time': travel_time,
        'proximity': proximity,
        'user_city': user_city,
        'event_city': event_city
    }


def compare_events_by_distance(user_city: str, events: list) -> list:
    """
    Sort events by distance from user's city.
    
    Args:
        user_city: User's city
        events: List of events with 'city' field
    
    Returns:
        Events sorted by distance (closest first)
    """
    events_with_distance = []
    
    for event in events:
        event_city = event.get('city', 'Unknown')
        distance_info = get_distance_info(user_city, event_city)
        events_with_distance.append({
            'event': event,
            'distance_info': distance_info
        })
    
    # Sort by distance
    events_with_distance.sort(key=lambda x: x['distance_info']['distance_km'])
    
    return events_with_distance


if __name__ == "__main__":
    # Test examples
    print("=" * 70)
    print(" DISTANCE CALCULATOR - TEST EXAMPLES")
    print("=" * 70)
    
    # Example 1: Same city
    print("\n📍 Example 1: Colombo to Colombo")
    info = get_distance_info("Colombo", "Colombo")
    print(f"  Distance: {info['distance_km']} km")
    print(f"  Score: {info['distance_score']}")
    print(f"  Proximity: {info['proximity']}")
    
    # Example 2: Nearby cities
    print("\n📍 Example 2: Colombo to Kandy")
    info = get_distance_info("Colombo", "Kandy")
    print(f"  Distance: {info['distance_km']} km")
    print(f"  Score: {info['distance_score']}")
    print(f"  Travel Time: {info['travel_time']}")
    print(f"  Proximity: {info['proximity']}")
    
    # Example 3: Far cities
    print("\n📍 Example 3: Colombo to Jaffna")
    info = get_distance_info("Colombo", "Jaffna")
    print(f"  Distance: {info['distance_km']} km")
    print(f"  Score: {info['distance_score']}")
    print(f"  Travel Time: {info['travel_time']}")
    print(f"  Proximity: {info['proximity']}")
    
    # Example 4: Regional
    print("\n📍 Example 4: Kandy to Galle")
    info = get_distance_info("Kandy", "Galle")
    print(f"  Distance: {info['distance_km']} km")
    print(f"  Score: {info['distance_score']}")
    print(f"  Travel Time: {info['travel_time']}")
    print(f"  Proximity: {info['proximity']}")
    
    # Example 5: All cities from Colombo
    print("\n📍 Example 5: Distances from Colombo")
    print("-" * 70)
    colombo_distances = {}
    for city in CITY_COORDINATES.keys():
        if city != "Colombo":
            dist = haversine_distance("Colombo", city)
            colombo_distances[city] = dist
    
    # Sort by distance
    sorted_cities = sorted(colombo_distances.items(), key=lambda x: x[1])
    for city, distance in sorted_cities:
        score = distance_to_score(distance)
        travel = estimate_travel_time(distance)
        print(f"  {city:20} | {distance:6.1f} km | Score: {score:.2f} | {travel}")
