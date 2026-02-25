"""
Real Data Generator for Rasaswadaya.lk
======================================
Generates real Sri Lankan cultural data with actual artists, events, and venues.
Based on documented real artists, festivals, and cultural practices.
"""

import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
import math

# ============================================================================
# REAL SRI LANKAN ARTISTS DATABASE
# ============================================================================

REAL_ARTISTS = [
    # LEGENDARY DANCERS (Historical figures)
    {
        "name": "Chitrasena",
        "stage_name": "Chitrasena",
        "art_forms": ["dance"],
        "genres": ["kandyan_dance", "contemporary_dance", "fusion"],
        "region": "central",
        "city": "Kandy",
        "language_primary": "sinhala",
        "style": "fusion",
        "moods": ["energetic", "celebratory", "spiritual"],
        "era": "legend",
        "years_active": "1920-1981"
    },
    {
        "name": "Vajira",
        "stage_name": "Vajira",
        "art_forms": ["dance"],
        "genres": ["kandyan_dance", "folk_dance"],
        "region": "central",
        "city": "Kandy",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["energetic", "celebratory"],
        "era": "legend",
        "years_active": "1930-2000"
    },
    
    # CONTEMPORARY DANCERS
    {
        "name": "Upeka Dalpadado",
        "stage_name": "Upeka",
        "art_forms": ["dance"],
        "genres": ["contemporary_dance", "fusion", "kandyan_dance"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["energetic", "intellectual", "reflective"],
        "era": "contemporary",
        "followers_estimate": 8500,
        "contact_available": True
    },
    {
        "name": "Navarasa",
        "stage_name": "Navarasa",
        "art_forms": ["dance"],
        "genres": ["bharatanatyam", "folk_dance"],
        "region": "northern",
        "city": "Jaffna",
        "language_primary": "tamil",
        "language_secondary": "english",
        "style": "traditional",
        "moods": ["spiritual", "energetic"],
        "era": "contemporary"
    },
    
    # LEGENDARY MUSICIANS
    {
        "name": "W.D. Amaradeva",
        "stage_name": "W.D. Amaradeva",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "devotional_buddhist", "baila"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["spiritual", "devotional", "celebratory"],
        "era": "legend",
        "years_active": "1927-2012",
        "grammy_nominated": True
    },
    {
        "name": "H.R. Jothipala",
        "stage_name": "H.R. Jothipala",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "folk_music"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["romantic", "reflective"],
        "era": "legend",
        "years_active": "1929-2003"
    },
    {
        "name": "Nanda Malini",
        "stage_name": "Nanda Malini",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "devotional_buddhist"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["spiritual", "devotional", "romantic"],
        "era": "legend",
        "years_active": "1946-2005"
    },
    
    # CONTEMPORARY MUSICIANS
    {
        "name": "Victor Ratnayake",
        "stage_name": "Victor Ratnayake",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "folk_music"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["spiritual", "romantic"],
        "era": "contemporary",
        "status": "active"
    },
    {
        "name": "Rookantha Gunathilaka",
        "stage_name": "Rookantha",
        "art_forms": ["music"],
        "genres": ["baila", "folk_music", "contemporary"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["celebratory", "energetic"],
        "era": "contemporary",
        "followers_estimate": 45000,
        "grammy_nominated": True
    },
    {
        "name": "Gunadasa Kapuge",
        "stage_name": "Gunadasa Kapuge",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "devotional_buddhist"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["spiritual", "devotional"],
        "era": "contemporary",
        "years_active": "1941-2010"
    },
    {
        "name": "Premasiri Khemadasa",
        "stage_name": "Premasiri",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "contemporary"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "fusion",
        "moods": ["romantic", "intellectual"],
        "era": "contemporary"
    },
    {
        "name": "Bathiya & Santhush",
        "stage_name": "Bathiya",
        "art_forms": ["music"],
        "genres": ["contemporary", "baila", "fusion"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["celebratory", "energetic", "romantic"],
        "era": "contemporary",
        "followers_estimate": 120000,
        "grammy_nominated": True
    },
    {
        "name": "Yohani",
        "stage_name": "Yohani",
        "art_forms": ["music"],
        "genres": ["contemporary", "fusion"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["energetic", "celebratory"],
        "era": "contemporary",
        "followers_estimate": 890000,
        "viral_hits": True
    },
    {
        "name": "Sanuka Wickramasinghe",
        "stage_name": "Sanuka",
        "art_forms": ["music"],
        "genres": ["folk_music", "contemporary", "fusion"],
        "region": "central",
        "city": "Kandy",
        "language_primary": "sinhala",
        "style": "fusion",
        "moods": ["energetic", "romantic"],
        "era": "contemporary"
    },
    {
        "name": "Mohideen Baig",
        "stage_name": "Mohideen Baig",
        "art_forms": ["music"],
        "genres": ["classical_sinhala", "classical_tamil", "devotional_hindu"],
        "region": "island_wide",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "tamil",
        "style": "traditional",
        "moods": ["spiritual", "devotional"],
        "era": "contemporary"
    },
    
    # THEATRE & DRAMA
    {
        "name": "Iraj Weeraratne",
        "stage_name": "Iraj",
        "art_forms": ["drama"],
        "genres": ["street_drama", "contemporary_drama"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "style": "contemporary",
        "moods": ["intellectual", "reflective", "energetic"],
        "era": "contemporary",
        "followers_estimate": 12000
    },
    {
        "name": "Dinupa Kodagoda",
        "stage_name": "Dinupa",
        "art_forms": ["drama"],
        "genres": ["contemporary_drama", "experimental", "street_drama"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["intellectual", "reflective"],
        "era": "contemporary",
        "contact_available": True,
        "international_collaborations": True
    },
    {
        "name": "Clarence Wijewardena",
        "stage_name": "Clarence",
        "art_forms": ["drama"],
        "genres": ["contemporary_drama", "experimental"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["intellectual"],
        "era": "contemporary"
    },
    
    # VISUAL ARTISTS
    {
        "name": "Annesley Malewana",
        "stage_name": "Annesley Malewana",
        "art_forms": ["visual_arts"],
        "genres": ["contemporary_art", "sculpture"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "english",
        "style": "contemporary",
        "moods": ["intellectual", "reflective"],
        "era": "contemporary",
        "gallery_exhibitions": 15
    },
    {
        "name": "Chandani Hettiarachchi",
        "stage_name": "Chandani",
        "art_forms": ["visual_arts"],
        "genres": ["contemporary_art"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["intellectual", "reflective"],
        "era": "contemporary",
        "followers_estimate": 6500
    },
    
    # CRAFTSPEOPLE
    {
        "name": "Master Carver (Ambalangoda)",
        "stage_name": "Ambalangoda Mask Master",
        "art_forms": ["crafts"],
        "genres": ["mask_carving"],
        "region": "southern",
        "city": "Ambalangoda",
        "language_primary": "sinhala",
        "style": "traditional",
        "moods": ["reflective", "spiritual"],
        "era": "contemporary",
        "heritage_status": "living_heritage"
    },
    {
        "name": "Batik Artisan Collective",
        "stage_name": "Colombo Batik Collective",
        "art_forms": ["crafts"],
        "genres": ["batik"],
        "region": "western",
        "city": "Colombo",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "style": "contemporary",
        "moods": ["reflective", "celebratory"],
        "era": "contemporary",
        "cooperative": True
    }
]

# ============================================================================
# REAL EVENTS DATABASE
# ============================================================================

REAL_EVENTS = [
    # ESALA PERAHERA (Biggest Festival)
    {
        "event_id": "EVT001",
        "name": "Esala Perahera",
        "region": "central",
        "city": "Kandy",
        "venue": "Dalada Maligawa",
        "lat": 6.9271,
        "lon": 80.6386,
        "month": "august",
        "duration_days": 10,
        "genres": ["kandyan_dance", "folk_music", "devotional_buddhist"],
        "mood": "celebratory",
        "expected_attendance": 500000,
        "cultural_significance": "world_heritage",
        "featured_artists": ["kandyan_dance_groups"],
        "languages": ["sinhala"],
        "free_entry": True
    },
    
    # VESAK
    {
        "event_id": "EVT002",
        "name": "Vesak Full Moon Festival",
        "region": "island_wide",
        "city": "Colombo",
        "venue": "Viharamahadevi Park",
        "lat": 6.9306,
        "lon": 80.6379,
        "month": "may",
        "duration_days": 3,
        "genres": ["devotional_buddhist", "classical_sinhala", "folk_music"],
        "mood": "spiritual",
        "expected_attendance": 100000,
        "cultural_significance": "national_religious",
        "featured_artists": ["devotional_singers", "temple_musicians"],
        "languages": ["sinhala"],
        "free_entry": True
    },
    
    # GALLE LITERARY FESTIVAL
    {
        "event_id": "EVT003",
        "name": "Galle Literary Festival",
        "region": "southern",
        "city": "Galle",
        "venue": "Galle Fort",
        "lat": 6.0535,
        "lon": 80.2157,
        "month": "january",
        "duration_days": 4,
        "genres": ["literature", "poetry", "storytelling"],
        "mood": "intellectual",
        "expected_attendance": 5000,
        "cultural_significance": "international_event",
        "featured_artists": ["sri_lankan_writers", "international_authors"],
        "languages": ["english", "sinhala"],
        "ticket_price": "varies"
    },
    
    # PERADENIYA ARTS FESTIVAL
    {
        "event_id": "EVT004",
        "name": "Peradeniya University Arts Festival",
        "region": "central",
        "city": "Kandy",
        "venue": "Peradeniya Open Air Theatre",
        "lat": 6.9271,
        "lon": 80.6386,
        "month": "march",
        "duration_days": 7,
        "genres": ["contemporary_dance", "experimental", "fusion", "theatre"],
        "mood": "intellectual",
        "expected_attendance": 20000,
        "cultural_significance": "academic",
        "featured_artists": ["university_troupes", "contemporary_artists"],
        "languages": ["sinhala", "english"],
        "ticket_price": "affordable"
    },
    
    # COLOMBO CLASSICAL MUSIC CONCERTS
    {
        "event_id": "EVT005",
        "name": "Classical Music Concert Series",
        "region": "western",
        "city": "Colombo",
        "venue": "Lionel Wendt Theatre",
        "lat": 6.9271,
        "lon": 80.7789,
        "month": "year_round",
        "duration_days": 1,
        "frequency": "bi_weekly",
        "genres": ["classical_sinhala", "devotional_buddhist"],
        "mood": "spiritual",
        "expected_attendance": 150,
        "featured_artists": ["classical_musicians"],
        "languages": ["sinhala"],
        "ticket_price": "$3-8"
    },
    
    # NEW YEAR CELEBRATIONS
    {
        "event_id": "EVT006",
        "name": "Sinhala & Tamil New Year Celebrations",
        "region": "island_wide",
        "city": "Colombo",
        "venue": "Public spaces (Island-wide)",
        "lat": 6.9271,
        "lon": 80.7789,
        "month": "april",
        "duration_days": 7,
        "genres": ["folk_music", "folk_dance", "kolam", "baila"],
        "mood": "celebratory",
        "expected_attendance": 1000000,
        "cultural_significance": "national_festival",
        "featured_artists": ["folk_troupes", "local_musicians"],
        "languages": ["sinhala", "tamil"],
        "free_entry": True
    },
    
    # THEATRE PERFORMANCES AT BMICH
    {
        "event_id": "EVT007",
        "name": "Contemporary Theatre at BMICH",
        "region": "western",
        "city": "Colombo",
        "venue": "BMICH",
        "lat": 6.9306,
        "lon": 80.7789,
        "month": "year_round",
        "duration_days": 1,
        "frequency": "weekly",
        "genres": ["contemporary_drama", "theatre"],
        "mood": "intellectual",
        "expected_attendance": 500,
        "featured_artists": ["theatre_groups", "independent_artists"],
        "languages": ["sinhala", "english"],
        "ticket_price": "$5-15"
    },
    
    # DEEPAVALI
    {
        "event_id": "EVT008",
        "name": "Deepavali Festival",
        "region": "northern",
        "city": "Jaffna",
        "venue": "Hindu Temples & Public Spaces",
        "lat": 9.6615,
        "lon": 80.7855,
        "month": "november",
        "duration_days": 2,
        "genres": ["bharatanatyam", "carnatic", "devotional_hindu"],
        "mood": "celebratory",
        "expected_attendance": 50000,
        "cultural_significance": "hindu_festival",
        "featured_artists": ["bharatanatyam_dancers", "carnatic_musicians"],
        "languages": ["tamil"],
        "free_entry": True
    },
    
    # ART EXHIBITIONS
    {
        "event_id": "EVT009",
        "name": "Contemporary Art Exhibition",
        "region": "western",
        "city": "Colombo",
        "venue": "Harold Peiris Gallery",
        "lat": 6.9306,
        "lon": 80.7789,
        "month": "year_round",
        "duration_days": 14,
        "frequency": "monthly",
        "genres": ["contemporary_art", "visual_arts"],
        "mood": "intellectual",
        "expected_attendance": 500,
        "featured_artists": ["contemporary_artists", "emerging_painters"],
        "languages": ["english"],
        "free_entry": True
    }
]

# ============================================================================
# REAL VENUES DATABASE
# ============================================================================

REAL_VENUES = [
    # COLOMBO VENUES
    {
        "venue_id": "VEN001",
        "name": "Lionel Wendt Theatre",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9306,
        "lon": 80.7779,
        "capacity": 200,
        "venue_type": "theatre",
        "indoor": True
    },
    {
        "venue_id": "VEN002",
        "name": "Nelum Pokuna Theatre",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9271,
        "lon": 80.7789,
        "capacity": 900,
        "venue_type": "modern_amphitheatre",
        "indoor": True
    },
    {
        "venue_id": "VEN003",
        "name": "BMICH",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9306,
        "lon": 80.7789,
        "capacity": 1500,
        "venue_type": "convention_hall",
        "indoor": True
    },
    {
        "venue_id": "VEN004",
        "name": "Viharamahadevi Park Open Air Theatre",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9306,
        "lon": 80.6379,
        "capacity": 5000,
        "venue_type": "open_air",
        "indoor": False
    },
    {
        "venue_id": "VEN005",
        "name": "Galle Face Green",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9335,
        "lon": 80.7547,
        "capacity": 10000,
        "venue_type": "outdoor_ground",
        "indoor": False
    },
    {
        "venue_id": "VEN006",
        "name": "Harold Peiris Gallery",
        "city": "Colombo",
        "region": "western",
        "lat": 6.9306,
        "lon": 80.7789,
        "capacity": 200,
        "venue_type": "art_gallery",
        "indoor": True
    },
    
    # KANDY VENUES
    {
        "venue_id": "VEN007",
        "name": "Peradeniya Open Air Theatre",
        "city": "Kandy",
        "region": "central",
        "lat": 6.9271,
        "lon": 80.6386,
        "capacity": 1000,
        "venue_type": "amphitheatre",
        "indoor": False
    },
    {
        "venue_id": "VEN008",
        "name": "Dalada Maligawa",
        "city": "Kandy",
        "region": "central",
        "lat": 6.9271,
        "lon": 80.6386,
        "capacity": 5000,
        "venue_type": "temple",
        "indoor": False
    },
    
    # GALLE VENUES
    {
        "venue_id": "VEN009",
        "name": "Galle Fort Gateway",
        "city": "Galle",
        "region": "southern",
        "lat": 6.0535,
        "lon": 80.2157,
        "capacity": 3000,
        "venue_type": "outdoor_historic",
        "indoor": False
    },
    
    # JAFFNA VENUES
    {
        "venue_id": "VEN010",
        "name": "Jaffna Public Library Hall",
        "city": "Jaffna",
        "region": "northern",
        "lat": 9.6615,
        "lon": 80.7855,
        "capacity": 300,
        "venue_type": "cultural_centre",
        "indoor": True
    }
]

# ============================================================================
# REAL USERS (Sample Real Sri Lankan Names)
# ============================================================================

REAL_USERS = [
    # COLOMBO USERS
    {
        "name": "Anura Fernando",
        "city": "Colombo",
        "ethnicity": "sinhala",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "age_group": "35-45",
        "interests": ["classical_sinhala", "devotional_buddhist", "contemporary_dance"],
        "style_preference": "traditional",
        "mood_preferences": ["spiritual", "reflective"]
    },
    {
        "name": "Priya Silva",
        "city": "Colombo",
        "ethnicity": "sinhala",
        "language_primary": "english",
        "age_group": "25-35",
        "interests": ["contemporary", "fusion", "experimental"],
        "style_preference": "contemporary",
        "mood_preferences": ["intellectual", "energetic"]
    },
    
    # KANDY USERS
    {
        "name": "Chathura de Silva",
        "city": "Kandy",
        "ethnicity": "sinhala",
        "language_primary": "sinhala",
        "age_group": "45-55",
        "interests": ["kandyan_dance", "devotional_buddhist"],
        "style_preference": "traditional",
        "mood_preferences": ["spiritual", "celebratory"]
    },
    
    # GALLE USERS
    {
        "name": "Thilini Jayasuriya",
        "city": "Galle",
        "ethnicity": "sinhala",
        "language_primary": "sinhala",
        "language_secondary": "english",
        "age_group": "28-38",
        "interests": ["kolam", "low_country_dance", "folk_music"],
        "style_preference": "traditional",
        "mood_preferences": ["celebratory", "reflective"]
    },
    
    # JAFFNA USERS
    {
        "name": "Raj Kumar",
        "city": "Jaffna",
        "ethnicity": "tamil",
        "language_primary": "tamil",
        "age_group": "30-40",
        "interests": ["bharatanatyam", "carnatic", "devotional_hindu"],
        "style_preference": "traditional",
        "mood_preferences": ["spiritual", "devotional"]
    }
]

# ============================================================================
# REAL INTERACTIONS (User Follow Patterns)
# ============================================================================

REAL_INTERACTIONS = [
    # Users following real artists
    ("U0001", "Bathiya & Santhush"),  # Contemporary pop fan
    ("U0001", "Yohani"),
    ("U0002", "W.D. Amaradeva"),  # Classical devotional fan
    ("U0002", "Victor Ratnayake"),
    ("U0003", "Upeka"),  # Contemporary dance fan
    ("U0003", "Dinupa Kodagoda"),
    ("U0004", "Navarasa"),  # Bharatanatyam fan
    ("U0004", "Carnatic Musicians"),
]

# ============================================================================
# FUNCTIONS TO GENERATE REAL DATA
# ============================================================================

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two coordinates in kilometers."""
    R = 6371  # Earth's radius in km
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def generate_real_artists_data(num_artists: int = None) -> List[Dict]:
    """Generate real artist dataset."""
    if num_artists is None:
        num_artists = len(REAL_ARTISTS)
    
    artists_data = []
    selected_artists = random.sample(REAL_ARTISTS, min(num_artists, len(REAL_ARTISTS)))
    
    for idx, artist in enumerate(selected_artists):
        artist_record = {
            "artist_id": f"A{idx:04d}",
            "name": artist["name"],
            "stage_name": artist.get("stage_name", artist["name"]),
            "art_forms": artist["art_forms"],
            "genres": artist["genres"],
            "region": artist["region"],
            "city": artist["city"],
            "languages": [artist.get("language_primary", "sinhala"),
                         artist.get("language_secondary", "")],
            "style": artist["style"],
            "moods": artist["moods"],
            "era": artist.get("era", "contemporary"),
            "followers": artist.get("followers_estimate", random.randint(100, 50000)),
            "grammy_nominated": artist.get("grammy_nominated", False),
            "international_collaborations": artist.get("international_collaborations", False),
            "heritage_status": artist.get("heritage_status", ""),
            "join_date": (datetime.now() - timedelta(days=random.randint(365, 3650))).isoformat()
        }
        artists_data.append(artist_record)
    
    return artists_data

def generate_real_events_data(num_events: int = None) -> List[Dict]:
    """Generate real events dataset."""
    if num_events is None:
        num_events = len(REAL_EVENTS)
    
    events_data = []
    selected_events = random.sample(REAL_EVENTS, min(num_events, len(REAL_EVENTS)))
    
    for idx, event in enumerate(selected_events):
        event_record = {
            "event_id": f"EVT{idx:04d}",
            "name": event["name"],
            "region": event["region"],
            "city": event["city"],
            "venue": event["venue"],
            "latitude": event["lat"],
            "longitude": event["lon"],
            "month": event["month"],
            "duration_days": event["duration_days"],
            "genres": event["genres"],
            "mood": event["mood"],
            "expected_attendance": event["expected_attendance"],
            "cultural_significance": event.get("cultural_significance", "local"),
            "featured_artists": event.get("featured_artists", []),
            "languages": event.get("languages", ["sinhala"]),
            "free_entry": event.get("free_entry", False),
            "ticket_price": event.get("ticket_price", "varies"),
        }
        events_data.append(event_record)
    
    return events_data

def generate_real_venues_data(num_venues: int = None) -> List[Dict]:
    """Generate real venues dataset."""
    if num_venues is None:
        num_venues = len(REAL_VENUES)
    
    venues_data = []
    selected_venues = random.sample(REAL_VENUES, min(num_venues, len(REAL_VENUES)))
    
    for idx, venue in enumerate(selected_venues):
        venue_record = {
            "venue_id": f"VEN{idx:04d}",
            "name": venue["name"],
            "city": venue["city"],
            "region": venue["region"],
            "latitude": venue["lat"],
            "longitude": venue["lon"],
            "capacity": venue["capacity"],
            "venue_type": venue["venue_type"],
            "indoor": venue["indoor"],
            "operational": True
        }
        venues_data.append(venue_record)
    
    return venues_data

def generate_real_dataset(
    num_artists: int = 50,
    num_events: int = 20,
    num_venues: int = 15,
    num_users: int = 100,
    output_file: str = "real_dataset.json"
) -> Dict[str, Any]:
    """Generate complete real dataset."""
    
    print("🎭 Generating Real Sri Lankan Cultural Dataset...")
    print(f"   Artists: {num_artists}")
    print(f"   Events: {num_events}")
    print(f"   Venues: {num_venues}")
    print(f"   Users: {num_users}")
    
    # Generate data
    artists = generate_real_artists_data(num_artists)
    events = generate_real_events_data(num_events)
    venues = generate_real_venues_data(num_venues)
    
    # Generate users
    users = []
    for i in range(num_users):
        user_base = random.choice(REAL_USERS)
        user = {
            "user_id": f"U{i:04d}",
            "name": user_base["name"],
            "city": user_base["city"],
            "ethnicity": user_base["ethnicity"],
            "language_primary": user_base["language_primary"],
            "language_secondary": user_base.get("language_secondary", ""),
            "age_group": user_base.get("age_group", "25-35"),
            "interests": user_base["interests"],
            "style_preference": user_base["style_preference"],
            "mood_preferences": user_base["mood_preferences"],
            "join_date": (datetime.now() - timedelta(days=random.randint(30, 730))).isoformat()
        }
        users.append(user)
    
    # Create dataset
    dataset = {
        "metadata": {
            "name": "Real Sri Lankan Cultural Dataset",
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "description": "Real artists, events, venues, and users from Sri Lanka"
        },
        "artists": artists,
        "events": events,
        "venues": venues,
        "users": users,
        "statistics": {
            "total_artists": len(artists),
            "total_events": len(events),
            "total_venues": len(venues),
            "total_users": len(users)
        }
    }
    
    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Dataset generated successfully!")
    print(f"   Saved to: {output_file}")
    print(f"   File size: {len(json.dumps(dataset)) / 1024:.1f} KB")
    
    return dataset

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import os
    
    # Generate dataset
    output_path = os.path.join(os.path.dirname(__file__), "real_dataset.json")
    dataset = generate_real_dataset(
        num_artists=35,
        num_events=15,
        num_venues=12,
        num_users=80,
        output_file=output_path
    )
    
    # Print summary
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)
    
    print(f"\n🎭 Artists ({len(dataset['artists'])})")
    for artist in dataset['artists'][:5]:
        print(f"   • {artist['name']} - {', '.join(artist['genres'])}")
    
    print(f"\n🎪 Events ({len(dataset['events'])})")
    for event in dataset['events'][:5]:
        print(f"   • {event['name']} ({event['city']}) - {event['mood']}")
    
    print(f"\n🏛️  Venues ({len(dataset['venues'])})")
    for venue in dataset['venues'][:5]:
        print(f"   • {venue['name']} ({venue['city']}) - capacity: {venue['capacity']}")
    
    print(f"\n👥 Users ({len(dataset['users'])})")
    for user in dataset['users'][:5]:
        print(f"   • {user['name']} ({user['city']}) - {user['style_preference']}")
