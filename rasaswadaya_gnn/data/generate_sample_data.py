"""
Sample Dataset Generator for Rasaswadaya.lk
===========================================
Generates realistic synthetic data for Sri Lankan cultural platform.
"""

import random
import json
import pickle
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple
import numpy as np

from .cultural_constants import (
    SRI_LANKAN_CULTURAL_TAXONOMY,
    get_art_forms,
    get_styles,
    get_sub_genres,
    get_regions,
    get_moods,
    get_languages,
    get_cities
)


def get_regions_dict():
    """Get regions dictionary with cities."""
    return SRI_LANKAN_CULTURAL_TAXONOMY.get("regions", {})


# Name databases for realistic Sri Lankan names
SINHALA_FIRST_NAMES = [
    "Kasun", "Nuwan", "Chaminda", "Mahela", "Dilshan", "Lasith", "Angelo",
    "Sanduni", "Dilini", "Chathurika", "Nadeeka", "Thilini", "Buddhika",
    "Ravi", "Priya", "Amila", "Danushka", "Saman", "Lakshman", "Nalaka",
    "Nimesh", "Sachini", "Tharindu", "Madhavi", "Isuru", "Nadeesha", "Kavinda",
    "Yashodha", "Damith", "Ayesha", "Ruwan", "Hiruni", "Shehan", "Hashini",
    "Chathura", "Anusha", "Gayan", "Sandani", "Thisara", "Vindya", "Roshan",
    "Chandima", "Dinesh", "Malsha", "Ajith", "Samanthi", "Lahiru", "Nishani"
]

TAMIL_FIRST_NAMES = [
    "Kumar", "Rajan", "Vel", "Shan", "Thiru", "Muthu", "Nirmala",
    "Priya", "Deepa", "Mala", "Kamala", "Ragavan", "Karthik", "Vijay",
    "Arun", "Shanthi", "Ravi", "Lakshmi", "Suresh", "Durga", "Ganesh",
    "Vasanthi", "Mohan", "Kavitha", "Senthil", "Meena", "Siva", "Vani"
]

LAST_NAMES = [
    "Fernando", "Silva", "Perera", "Jayasuriya", "Wijesinghe", "Mendis",
    "Rajapaksa", "Wickremasinghe", "Gunasekara", "Dissanayake",
    "Kumar", "Sivarajah", "Nadarajah", "Thiyagarajah", "Selvam",
    "De Silva", "Gunawardena", "Amarasinghe", "Bandara", "Jayawardena",
    "Senanayake", "Ranasinghe", "Herath", "Liyanage", "Ekanayake",
    "Weerasinghe", "Pathirana", "Rathnayake", "Samaraweera", "Kumara"
]

# Artist stage names (Real Sri Lankan artists & performers)
ARTIST_STAGE_NAMES = [
    "Chitrasena", "Vajira", "Upeka", "Navarasa", "Rithma", "Sandanari",
    "Sunil Edirisinghe", "W.D. Amaradeva", "Nanda Malini", "Victor Ratnayake",
    "Rookantha Gunathilaka", "Bathiya & Santhush", "Yohani", "Sanuka Wickramasinghe",
    "Ashanthi De Alwis", "Dinupa Kodagoda", "Ravibandu Vidyapathi", "Iraj Weeraratne",
    "Randhir", "Umaria", "Sashika Nisansala", "Chandani Hettiarachchi",
    "Annesley Malewana", "Clarence Wijewardena", "H.R. Jothipala", "Sunil Perera",
    "Desmond de Silva", "Milton Mallawarachchi", "Neela Wickremasinghe",
    "Edward Jayakody", "Angeline Gunathilaka", "Gunadasa Kapuge", "Malini Bulathsinghala",
    "Amarasiri Peiris", "Karunarathna Divulgane", "Pandith Amaradeva",
    "Mohideen Baig", "Premasiri Khemadasa", "Sunil Ariyaratne", "Dharmadasa Walpola",
    "Chitral Somapala", "Sangeeth Wijesuriya", "Uresha Ravihari", "Shanika Madumali",
    "Umara Sinhawansa", "Dilki Uresha", "Thushara Joshep", "Damith Asanka"
]

# Venue names (Real Sri Lankan cultural venues)
VENUES = [
    "Bishop's College Auditorium", "Lionel Wendt Theatre", "Nelum Pokuna Theatre",
    "BMICH (Bandaranaike Memorial International Conference Hall)",
    "Colombo Hilton Grand Ballroom", "Gangaramaya Temple Grounds",
    "Galle Face Green", "Independence Square", "Viharamahadevi Park Open Air Theatre",
    "University of Peradeniya Open Air Theatre", "Kandy Lake Club",
    "Jaffna Public Library Hall", "Galle Fort Gateway", "Anuradhapura Cultural Centre",
    "Elphinstone Theatre", "Tower Hall Theatre", "Punchi Theatre (Borella)",
    "Lumbini Theatre (Havelock Town)", "Regal Theatre (Colombo)",
    "Navarangahala (Borella)", "Royal College Main Hall", "Ladies' College Auditorium",
    "Sugathadasa Indoor Stadium", "Maharagama Youth Centre",
    "Temple Trees Grounds", "Cinnamon Grand Ballroom", "Galadari Hotel Ballroom",
    "National Museum Auditorium", "Sapumal Foundation", "Colombo University Arts Theatre",
    "Kelaniya Raja Maha Vihara", "Dalada Maligawa (Temple of the Tooth)",
    "Diyatha Uyana", "Waters Edge", "Colombo Racecourse",
    "Galle International Cricket Stadium", "Bentota Beach Resort",
    "Mount Lavinia Hotel Ballroom", "Cinnamon Lakeside Ballroom",
    "Sri Lanka Foundation Institute", "Harold Peiris Gallery", "Paradise Road Gallery"
]


def generate_users(num_users: int = 150) -> List[Dict[str, Any]]:
    """Generate synthetic user profiles with city-based locations."""
    users = []
    
    # Extract all cities from cultural constants
    all_cities = get_cities()  # Use the helper function from cultural_constants
    
    for i in range(num_users):
        # Randomly pick ethnicity to influence language preference
        ethnicity = random.choices(['sinhala', 'tamil', 'other'], weights=[0.75, 0.15, 0.10])[0]
        
        if ethnicity == 'sinhala':
            first_name = random.choice(SINHALA_FIRST_NAMES)
            language_prefs = random.choice([
                ['sinhala'],
                ['sinhala', 'english']
            ])
        elif ethnicity == 'tamil':
            first_name = random.choice(TAMIL_FIRST_NAMES)
            language_prefs = random.choice([
                ['tamil'],
                ['tamil', 'english']
            ])
        else:
            first_name = random.choice(SINHALA_FIRST_NAMES + TAMIL_FIRST_NAMES)
            language_prefs = ['english']
        
        last_name = random.choice(LAST_NAMES)
        
        # City-based location (updated from region to city)
        # User's city determines their location
        user_city = random.choice(all_cities)
        
        # Art form interests (1-3 forms)
        num_interests = random.choices([1, 2, 3], weights=[0.5, 0.35, 0.15])[0]
        art_interests = random.sample(get_art_forms(), num_interests)
        
        # Cultural category preferences
        culture_prefs = random.choices(
            ['traditional', 'contemporary', 'fusion'],
            weights=[0.3, 0.5, 0.2],
            k=random.randint(1, 2)
        )
        
        # Mood preferences
        mood_prefs = random.sample(get_moods(), random.randint(2, 4))
        
        # Activity level
        activity_level = random.choices(
            ['high', 'medium', 'low'],
            weights=[0.2, 0.5, 0.3]
        )[0]
        
        users.append({
            'user_id': f"U{i:04d}",
            'name': f"{first_name} {last_name}",
            'ethnicity': ethnicity,
            'language_preferences': language_prefs,
            'city': user_city,  # Changed from region_preference to city
            'art_interests': art_interests,
            'culture_preferences': culture_prefs,
            'mood_preferences': mood_prefs,
            'activity_level': activity_level,
            'join_date': (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat()
        })
    
    return users


def generate_artists(num_artists: int = 60) -> List[Dict[str, Any]]:
    """Generate synthetic artist profiles with new taxonomy."""
    artists = []
    art_forms = get_art_forms()  # ['music', 'dance', 'film', 'drama']
    
    for i in range(num_artists):
        # Pick primary art form
        primary_art = random.choice(art_forms)
        
        # Get styles for this art form using the new taxonomy
        available_styles = get_styles(primary_art)
        
        if not available_styles:
            # Fallback for any art form without styles
            available_styles = ['traditional', 'contemporary']
        
        # Pick 1-2 styles
        num_styles = random.choices([1, 2], weights=[0.7, 0.3])[0]
        styles_chosen = random.sample(available_styles, min(num_styles, len(available_styles)))
        
        # Get sub-genres for the chosen styles
        genres = []
        for style in styles_chosen:
            sub_genres = get_sub_genres(primary_art, style)
            if sub_genres:
                # Pick 1-2 sub-genres from this style
                num_subgenres = random.randint(1, min(2, len(sub_genres)))
                genres.extend(random.sample(sub_genres, num_subgenres))
        
        # If no genres found, use the styles themselves
        if not genres:
            genres = styles_chosen
        
        # Determine if traditional/contemporary/fusion based on styles
        if any('traditional' in s or 'classical' in s or 'kandyan' in s or 'devotional' in s for s in styles_chosen):
            style = ['traditional']
        elif any('fusion' in s or 'experimental' in s for s in styles_chosen):
            style = ['fusion', 'contemporary']
        else:
            style = ['contemporary']
        
        # Language based on art form and style
        if any('tamil' in s or 'bharatanatyam' in s or 'carnatic' in s for s in ' '.join(styles_chosen + genres)):
            language = ['tamil']
        elif 'contemporary' in style:
            language = random.choice([['sinhala'], ['sinhala', 'english'], ['tamil'], ['english']])
        else:
            language = ['sinhala']
        
        # Region-based city selection
        if any('kandyan' in s for s in styles_chosen + genres):
            city = random.choice(['kandy', 'matale', 'nuwara_eliya'])
        elif any('low_country' in s for s in styles_chosen + genres):
            city = random.choice(['galle', 'matara', 'hambantota'])
        elif 'tamil' in language:
            city = random.choice(['jaffna', 'kilinochchi', 'trincomalee', 'batticaloa'])
        else:
            # Spread across all cities
            city = random.choice(get_cities())
        
        # Mood tags based on genres
        if any('devotional' in g or 'religious' in g for g in genres):
            moods = ['spiritual', 'devotional']
        elif any('baila' in g for g in genres):
            moods = ['celebratory', 'energetic', 'party']
        elif any('hip_hop' in g or 'rap' in g for g in genres):
            moods = ['energetic', 'rebel', 'urban_street']
        elif any('romantic' in g for g in genres):
            moods = ['romantic', 'emotional']
        else:
            moods = random.sample(get_moods(), random.randint(1, 3))
        
        # Festival associations (simplified - use generic festivals)
        festivals = []
        if 'devotional' in ' '.join(genres) or 'traditional' in style:
            # Traditional/devotional artists associated with cultural festivals
            festivals = random.sample(['vesak', 'esala_perahera', 'poson'], 
                                      random.randint(0, 2))
        elif 'tamil' in language:
            festivals = random.sample(['deepavali', 'thai_pongal'], random.randint(0, 1))
        
        # Use stage name or real name
        if random.random() < 0.4 and len(ARTIST_STAGE_NAMES) > i:
            name = ARTIST_STAGE_NAMES[i % len(ARTIST_STAGE_NAMES)]
        else:
            first = random.choice(SINHALA_FIRST_NAMES if 'tamil' not in language else TAMIL_FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            name = f"{first} {last}"
        
        # Popularity score
        popularity = random.choices(
            ['emerging', 'mid_tier', 'established'],
            weights=[0.5, 0.35, 0.15]
        )[0]
        
        artists.append({
            'artist_id': f"A{i:04d}",
            'name': name,
            'art_forms': [primary_art],
            'genres': genres,  # Sub-genres
            'styles': styles_chosen,  # Major styles
            'language': language,
            'city': city,
            'style': style,  # Cultural style: traditional/contemporary/fusion
            'mood_tags': moods,
            'festivals': festivals,
            'popularity': popularity,
            'follower_count': random.randint(50, 5000),
            'verified': random.random() < 0.3
        })
    
    return artists


def generate_events(artists: List[Dict], num_events: int = 120) -> List[Dict[str, Any]]:
    """
    Generate synthetic events with realistic cultural metadata.
    
    IMPORTANT: Event genres are DERIVED from performing artists' genres.
    Event is the union of all performing artists' genres/art_forms/languages.
    This ensures semantic consistency in the graph.
    """
    events = []
    
    event_types = ['concert', 'performance', 'exhibition', 'workshop', 
                   'festival', 'competition', 'ritual_ceremony']
    
    for i in range(num_events):
        # Pick 1-3 performing artists
        num_artists = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
        event_artists = random.sample(artists, num_artists)
        
        # Event cultural properties are DERIVED from performing artists
        primary_artist = event_artists[0]
        
        # Union of all artists' art forms
        art_forms = list(set([af for artist in event_artists for af in artist['art_forms']]))
        
        # Union of all artists' genres - THIS IS KEY
        # Event genres = combination of all performing artists' genres
        genres = list(set([g for artist in event_artists for g in artist['genres']]))
        
        # Union of all artists' languages
        languages = list(set([lang for artist in event_artists for lang in artist['language']]))
        
        # City from primary artist (event held in artist's city)
        city = primary_artist['city']
        venue = random.choice(VENUES)
        
        # Union of all artists' styles
        styles = list(set([s for artist in event_artists for s in artist['style']]))
        
        # Union of all artists' moods (limit to 3)
        moods = list(set([m for artist in event_artists for m in artist['mood_tags']]))[:3]
        
        # Event type
        event_type = random.choice(event_types)
        
        # Festival alignment - from artists' festival associations
        festival = None
        festivals_list = list(set([f for artist in event_artists for f in artist.get('festivals', [])]))
        if festivals_list and random.random() < 0.3:
            festival = random.choice(festivals_list)
        
        # Date (upcoming events)
        days_ahead = random.randint(7, 180)
        event_date = (datetime.now() + timedelta(days=days_ahead)).isoformat()
        
        # Capacity and ticket price
        capacity = random.choice([50, 100, 200, 500, 1000, 2000])
        
        if 'festival' in event_type or festival:
            ticket_price = random.choice([0, 500, 1000])  # Often free or cheap
        else:
            ticket_price = random.choice([0, 500, 1000, 1500, 2000, 3000])
        
        # Generate event name
        if festival:
            event_name = f"{festival.replace('_', ' ').title()} - {primary_artist['name']}"
        else:
            action = random.choice(['Live', 'Night of', 'Celebration of', 'Evening with'])
            event_name = f"{action} {primary_artist['name']}"
        
        events.append({
            'event_id': f"E{i:04d}",
            'name': event_name,
            'artist_ids': [artist['artist_id'] for artist in event_artists],
            'art_forms': art_forms,
            'genres': genres,
            'language': languages,
            'city': city,  # Changed from region to city
            'venue': venue,
            'style': styles,
            'mood_tags': moods,
            'festival': festival,
            'festivals': [festival] if festival else [],
            'event_type': event_type,
            'date': event_date,
            'capacity': capacity,
            'ticket_price': ticket_price,
            'status': 'upcoming'
        })
    
    return events


def generate_interactions(
    users: List[Dict],
    artists: List[Dict],
    events: List[Dict]
) -> Dict[str, List[Dict]]:
    """Generate user interactions (follows, attends, likes)."""
    
    interactions = {
        'follows': [],  # user -> artist
        'attends': [],  # user -> event
        'likes_genre': [],  # user -> genre (implicit)
        'rates': []  # user -> event/artist
    }
    
    for user in users:
        user_id = user['user_id']
        activity_level = user['activity_level']
        
        # Number of follows based on activity
        if activity_level == 'high':
            num_follows = random.randint(10, 30)
        elif activity_level == 'medium':
            num_follows = random.randint(3, 12)
        else:
            num_follows = random.randint(1, 5)
        
        # Filter artists by user preferences
        compatible_artists = []
        for artist in artists:
            score = 0
            # Language match
            if any(lang in artist['language'] for lang in user['language_preferences']):
                score += 2
            # Art form match
            if any(af in artist['art_forms'] for af in user['art_interests']):
                score += 3
            # City match
            if user['city'] and artist['city'] == user['city']:
                score += 1
            # Culture preference match
            if any(style in artist['style'] for style in user['culture_preferences']):
                score += 2
            # Mood match
            if any(mood in artist['mood_tags'] for mood in user['mood_preferences']):
                score += 1
            
            if score > 0:
                compatible_artists.append((artist, score))
        
        # Sort by compatibility and add some randomness
        compatible_artists.sort(key=lambda x: x[1] * random.uniform(0.8, 1.2), reverse=True)
        
        # Follow top compatible artists
        for artist, score in compatible_artists[:num_follows]:
            interactions['follows'].append({
                'user_id': user_id,
                'artist_id': artist['artist_id'],
                'timestamp': (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat(),
                'compatibility_score': score
            })
        
        # Attend events (fewer than follows)
        if activity_level == 'high':
            num_attends = random.randint(5, 15)
        elif activity_level == 'medium':
            num_attends = random.randint(2, 7)
        else:
            num_attends = random.randint(0, 3)
        
        # User more likely to attend events by followed artists
        followed_artist_ids = [f['artist_id'] for f in interactions['follows'] if f['user_id'] == user_id]
        
        compatible_events = []
        for event in events:
            score = 0
            # Event by followed artist
            if any(aid in followed_artist_ids for aid in event['artist_ids']):
                score += 5
            # Art form match
            if any(af in event['art_forms'] for af in user['art_interests']):
                score += 2
            # City match
            if user['city'] and event['city'] == user['city']:
                score += 1
            # Free event bonus
            if event['ticket_price'] == 0:
                score += 1
            
            if score > 0:
                compatible_events.append((event, score))
        
        compatible_events.sort(key=lambda x: x[1] * random.uniform(0.7, 1.3), reverse=True)
        
        for event, score in compatible_events[:num_attends]:
            interactions['attends'].append({
                'user_id': user_id,
                'event_id': event['event_id'],
                'timestamp': (datetime.now() - timedelta(days=random.randint(1, 60))).isoformat(),
                'rsvp_status': random.choice(['going', 'interested', 'going']),
                'compatibility_score': score
            })
    
    return interactions


def generate_sample_dataset(
    num_users: int = 150,
    num_artists: int = 60,
    num_events: int = 120,
    output_dir: str = "data/sample_dataset"
) -> Dict[str, Any]:
    """
    Generate complete sample dataset.
    
    Returns:
        Dictionary with users, artists, events, interactions
    """
    print("🎭 Generating Rasaswadaya.lk Sample Dataset...")
    print("=" * 60)
    
    random.seed(42)
    np.random.seed(42)
    
    print(f"\n📊 Generating {num_users} users...")
    users = generate_users(num_users)
    print(f"✓ Created {len(users)} user profiles")
    
    print(f"\n🎨 Generating {num_artists} artists...")
    artists = generate_artists(num_artists)
    print(f"✓ Created {len(artists)} artist profiles")
    
    print(f"\n🎪 Generating {num_events} events...")
    events = generate_events(artists, num_events)
    print(f"✓ Created {len(events)} events")
    
    print(f"\n🔗 Generating user interactions...")
    interactions = generate_interactions(users, artists, events)
    print(f"✓ Created {len(interactions['follows'])} follows")
    print(f"✓ Created {len(interactions['attends'])} event attendances")
    
    dataset = {
        'users': users,
        'artists': artists,
        'events': events,
        'interactions': interactions,
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'num_users': len(users),
            'num_artists': len(artists),
            'num_events': len(events),
            'num_follows': len(interactions['follows']),
            'num_attends': len(interactions['attends'])
        }
    }
    
    # Save to files
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as JSON
    json_path = os.path.join(output_dir, "rasaswadaya_dataset.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Saved to: {json_path}")
    
    # Save as pickle for faster loading
    pickle_path = os.path.join(output_dir, "rasaswadaya_dataset.pkl")
    with open(pickle_path, 'wb') as f:
        pickle.dump(dataset, f)
    print(f"💾 Saved to: {pickle_path}")
    
    print("\n" + "=" * 60)
    print("✅ Dataset generation complete!")
    print("=" * 60)
    
    return dataset


def load_dataset(dataset_path: str = "data/sample_dataset/rasaswadaya_dataset.pkl") -> Dict[str, Any]:
    """Load pre-generated dataset."""
    if dataset_path.endswith('.pkl'):
        with open(dataset_path, 'rb') as f:
            return pickle.load(f)
    else:
        with open(dataset_path, 'r', encoding='utf-8') as f:
            return json.load(f)


if __name__ == "__main__":
    dataset = generate_sample_dataset(
        num_users=1500,      # 10x more users
        num_artists=500,     # 8x more artists  
        num_events=1000      # 8x more events
        # This generates ~13,000-15,000 total interaction rows
    )
    
    print("\n📈 Dataset Statistics:")
    print(f"  Total Users: {len(dataset['users'])}")
    print(f"  Total Artists: {len(dataset['artists'])}")
    print(f"  Total Events: {len(dataset['events'])}")
    print(f"  Total Follows: {len(dataset['interactions']['follows'])}")
    print(f"  Total Event RSVPs: {len(dataset['interactions']['attends'])}")
    print(f"\n  Average follows per user: {len(dataset['interactions']['follows']) / len(dataset['users']):.1f}")
    print(f"  Average events per user: {len(dataset['interactions']['attends']) / len(dataset['users']):.1f}")
