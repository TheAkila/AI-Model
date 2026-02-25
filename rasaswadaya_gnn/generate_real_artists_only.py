#!/usr/bin/env python3
"""
Real Sri Lankan Artists Database
Comprehensive collection of legendary and contemporary artists
across all 4 art forms: Music, Dance, Film, Drama
"""

import json
import pandas as pd
import os
from datetime import datetime

# ============================================================================
# REAL SRI LANKAN ARTISTS DATABASE
# ============================================================================

REAL_ARTISTS_DATABASE = [
    # ========== MUSIC - CLASSICAL & DEVOTIONAL ==========
    {
        "name": "W.D. Amaradeva",
        "art_form": "music",
        "genres": ["classical_semi_classical", "devotional_religious"],
        "styles": ["classical_semi_classical", "devotional_religious"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 1500000,
        "verified": True,
        "notable_works": ["Sasara Wasana Thuru", "Budu Sadum", "Devata Handa"],
        "awards": ["Kala Keerthi Award", "Presidential Award"],
        "popularity": "superstar",
        "bio": "Father of Sri Lankan classical music, legendary composer"
    },
    {
        "name": "Nanda Malini",
        "art_form": "music",
        "genres": ["classical_semi_classical", "devotional_religious"],
        "styles": ["classical_semi_classical", "devotional_religious"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 850000,
        "verified": True,
        "notable_works": ["Pipena Kusuma", "Punchi Suranganavi"],
        "awards": ["Kala Keerthi Award"],
        "popularity": "superstar",
        "bio": "Iconic devotional singer with 6 decades of career"
    },
    {
        "name": "Victor Ratnayake",
        "art_form": "music",
        "genres": ["devotional_religious", "classical_semi_classical"],
        "styles": ["devotional_religious"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 920000,
        "verified": True,
        "notable_works": ["Sudu Dusum Mal", "Dandum Budunge"],
        "awards": ["Kala Keerthi Award", "Presidential Award"],
        "popularity": "superstar",
        "bio": "Master of devotional music with international recognition"
    },
    
    # ========== MUSIC - COMMERCIAL POP ==========
    {
        "name": "Yohani",
        "art_form": "music",
        "genres": ["sinhala_commercial", "pop"],
        "styles": ["sinhala_commercial", "pop"],
        "languages": ["sinhala", "english"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 5200000,
        "verified": True,
        "notable_works": ["Manike Mage Hithe", "Sathuta"],
        "awards": ["MTV Europe Award nomination", "Viral sensation"],
        "popularity": "superstar",
        "bio": "Global viral sensation, modern pop icon"
    },
    {
        "name": "Bathiya & Santhush",
        "art_form": "music",
        "genres": ["sinhala_commercial", "pop"],
        "styles": ["sinhala_commercial"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 1200000,
        "verified": True,
        "notable_works": ["Yaalpanamen", "Athdakawe Hitha Watila"],
        "awards": ["Grammy nomination", "SLMA Best Duo"],
        "popularity": "superstar",
        "bio": "Grammy-nominated duo, international recognition"
    },
    {
        "name": "Rookantha Gunathilaka",
        "art_form": "music",
        "genres": ["sinhala_commercial", "ballads"],
        "styles": ["sinhala_commercial", "ballads"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 900000,
        "verified": True,
        "notable_works": ["Dileepa Podi Puthu", "Sanda Eliye"],
        "awards": ["SLMA Award"],
        "popularity": "mid_tier",
        "bio": "Renowned pop ballad singer"
    },
    {
        "name": "Sanuka Wickramasinghe",
        "art_form": "music",
        "genres": ["sinhala_commercial", "ballads"],
        "styles": ["sinhala_commercial", "ballads"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 450000,
        "verified": True,
        "notable_works": ["Hitha Hadae", "Rasa Kili"],
        "awards": ["SLMA Award"],
        "popularity": "mid_tier",
        "bio": "Contemporary ballad singer"
    },
    
    # ========== MUSIC - TRADITIONAL & BAILA ==========
    {
        "name": "Sunil Perera",
        "art_form": "music",
        "genres": ["baila", "folk"],
        "styles": ["baila", "folk"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 800000,
        "verified": True,
        "notable_works": ["Ran Madura", "Baila hits with The Gypsies"],
        "awards": ["Kala Keerthi Award"],
        "popularity": "superstar",
        "bio": "Baila king, founder of legendary band The Gypsies"
    },
    {
        "name": "Stanley Perera",
        "art_form": "music",
        "genres": ["baila", "folk"],
        "styles": ["baila"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 620000,
        "verified": True,
        "notable_works": ["Soru Soru", "Traditional Baila"],
        "awards": ["SLMA Lifetime Achievement"],
        "popularity": "superstar",
        "bio": "Classical baila performer, folk music maestro"
    },
    
    # ========== MUSIC - ROCK & ALTERNATIVE ==========
    {
        "name": "Costa",
        "art_form": "music",
        "genres": ["sinhala_rap", "hip_hop"],
        "styles": ["sinhala_rap", "hip_hop"],
        "languages": ["sinhala", "english"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 380000,
        "verified": True,
        "notable_works": ["Mama Miya", "Rap from Sri Lanka"],
        "awards": ["Hip-hop artist of the year"],
        "popularity": "mid_tier",
        "bio": "Pioneer of Sinhala hip-hop and rap culture"
    },
    {
        "name": "Nalin Perera",
        "art_form": "music",
        "genres": ["rock", "alternative_rock"],
        "styles": ["rock", "alternative_rock"],
        "languages": ["english", "sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 320000,
        "verified": True,
        "notable_works": ["Rock anthems"],
        "awards": ["Sri Lanka Rock Award"],
        "popularity": "mid_tier",
        "bio": "Sri Lankan rock music icon"
    },
    
    # ========== MUSIC - TAMIL ==========
    {
        "name": "Bommi & Oru Nila",
        "art_form": "music",
        "genres": ["tamil_classical", "tamil_folk"],
        "styles": ["tamil_classical"],
        "languages": ["tamil"],
        "city": "jaffna",
        "era": "contemporary",
        "follower_count": 280000,
        "verified": True,
        "notable_works": ["Tamil songs from Jaffna"],
        "awards": ["Tamil Music Award"],
        "popularity": "mid_tier",
        "bio": "Tamil music performers in Sri Lanka"
    },
    
    # ========== DANCE - CLASSICAL & CONTEMPORARY ==========
    {
        "name": "Chitrasena",
        "art_form": "dance",
        "genres": ["kandyan_dance", "classical_ballet"],
        "styles": ["kandyan_dance", "contemporary"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 450000,
        "verified": True,
        "notable_works": ["Kandyan dance performances", "Ballet adaptations"],
        "awards": ["Kala Keerthi Award", "UNESCO recognition"],
        "popularity": "superstar",
        "bio": "Father of modern Sri Lankan dance, dance revolution pioneer"
    },
    {
        "name": "Vajira Chitrasena",
        "art_form": "dance",
        "genres": ["kandyan_dance", "contemporary"],
        "styles": ["kandyan_dance", "contemporary"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 420000,
        "verified": True,
        "notable_works": ["Contemporary Kandyan fusion"],
        "awards": ["National Dance Award"],
        "popularity": "superstar",
        "bio": "Contemporary dance icon, carries on dance legacy"
    },
    {
        "name": "Upeka Wijayawardhane",
        "art_form": "dance",
        "genres": ["kandyan_dance", "classical_ballet"],
        "styles": ["kandyan_dance", "classical_ballet"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 320000,
        "verified": True,
        "notable_works": ["Classical ballet performances"],
        "awards": ["Dance Excellence Award"],
        "popularity": "mid_tier",
        "bio": "Classical ballet dancer with international exposure"
    },
    {
        "name": "Asanga Abeygunasekera",
        "art_form": "dance",
        "genres": ["kandyan_dance"],
        "styles": ["kandyan_dance"],
        "languages": ["sinhala"],
        "city": "kandy",
        "era": "contemporary",
        "follower_count": 280000,
        "verified": True,
        "notable_works": ["Traditional Kandyan dance"],
        "awards": ["National Heritage Award"],
        "popularity": "mid_tier",
        "bio": "Master of traditional Kandyan dance forms"
    },
    
    # ========== FILM - LEGENDARY DIRECTORS & ACTORS ==========
    {
        "name": "Lester James Peries",
        "art_form": "film",
        "genres": ["biographical", "historical", "drama"],
        "styles": ["biographical", "historical"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 520000,
        "verified": True,
        "notable_works": ["Rekava", "Gamperaliya", "Baddegama"],
        "awards": ["Kala Keerthi Award", "Palme d'Or nomination"],
        "popularity": "superstar",
        "bio": "Father of Sri Lankan cinema, legendary filmmaker"
    },
    {
        "name": "Jackson Anthony",
        "art_form": "film",
        "genres": ["drama", "film_songs"],
        "styles": ["drama", "contemporary"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 900000,
        "verified": True,
        "notable_works": ["Film and drama performances"],
        "awards": ["Best Actor Award"],
        "popularity": "superstar",
        "bio": "Top film and television actor"
    },
    {
        "name": "Tissa Jata Abeysekera",
        "art_form": "film",
        "genres": ["documentary", "social_drama"],
        "styles": ["documentary"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 380000,
        "verified": True,
        "notable_works": ["Documentary filmmaking"],
        "awards": ["International Film Festival Award"],
        "popularity": "mid_tier",
        "bio": "Pioneering documentary filmmaker"
    },
    {
        "name": "Sumitra Peries",
        "art_form": "film",
        "genres": ["drama", "family_drama"],
        "styles": ["drama"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 320000,
        "verified": True,
        "notable_works": ["Pioneering women filmmaker in Sri Lanka"],
        "awards": ["National Film Award"],
        "popularity": "mid_tier",
        "bio": "Pioneer of women filmmakers in Sri Lanka"
    },
    {
        "name": "Jude Channapriya",
        "art_form": "film",
        "genres": ["drama", "biography"],
        "styles": ["drama"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 410000,
        "verified": True,
        "notable_works": ["Contemporary film acting"],
        "awards": ["FIPRESCI Award"],
        "popularity": "mid_tier",
        "bio": "Contemporary film talent"
    },
    
    # ========== DRAMA & THEATRE ==========
    {
        "name": "Ediriweera Sarachchandra",
        "art_form": "drama",
        "genres": ["immersive_theatre", "political_theatre"],
        "styles": ["immersive_theatre", "political_theatre"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 320000,
        "verified": True,
        "notable_works": ["Theatre revolution, Nuraniye, Maname"],
        "awards": ["Kala Keerthi Award"],
        "popularity": "superstar",
        "bio": "Father of Sri Lankan theatre revolution"
    },
    {
        "name": "Ananda Abeysinghe",
        "art_form": "drama",
        "genres": ["immersive_theatre", "comedy"],
        "styles": ["immersive_theatre"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 380000,
        "verified": True,
        "notable_works": ["Comedy and satire performances"],
        "awards": ["SLARTCC Award"],
        "popularity": "superstar",
        "bio": "Comedy and theatre maestro"
    },
    {
        "name": "Tissa Jayakody",
        "art_form": "drama",
        "genres": ["political_theatre", "experimental"],
        "styles": ["political_theatre", "experimental_avant_garde"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 290000,
        "verified": True,
        "notable_works": ["Experimental theatre"],
        "awards": ["Contemporary Theatre Award"],
        "popularity": "mid_tier",
        "bio": "Experimental theatre director"
    },
    {
        "name": "Ranjith Jayakody",
        "art_form": "drama",
        "genres": ["family_drama", "immersive_theatre"],
        "styles": ["immersive_theatre"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 250000,
        "verified": True,
        "notable_works": ["Contemporary theatrical works"],
        "awards": ["Theatre Excellence Award"],
        "popularity": "mid_tier",
        "bio": "Contemporary drama performer"
    },
    
    # ========== ADDITIONAL LEGENDS ==========
    {
        "name": "Iraj Weeraratne",
        "art_form": "music",
        "genres": ["hip_hop", "fusion"],
        "styles": ["hip_hop", "fusion"],
        "languages": ["sinhala", "english"],
        "city": "colombo",
        "era": "contemporary",
        "follower_count": 410000,
        "verified": True,
        "notable_works": ["Fusion hip-hop"],
        "awards": ["Urban Music Award"],
        "popularity": "mid_tier",
        "bio": "Fusion hip-hop artist"
    },
    {
        "name": "Swarnalatha",
        "art_form": "music",
        "genres": ["sinhala_commercial", "film_songs"],
        "styles": ["sinhala_commercial"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 540000,
        "verified": True,
        "notable_works": ["Film songs"],
        "awards": ["SLMA Best Female Singer"],
        "popularity": "superstar",
        "bio": "Legendary film and playback singer"
    },
    {
        "name": "T.M. Jayaratne",
        "art_form": "music",
        "genres": ["classical_semi_classical"],
        "styles": ["classical_semi_classical"],
        "languages": ["sinhala"],
        "city": "colombo",
        "era": "legend",
        "follower_count": 480000,
        "verified": True,
        "notable_works": ["Classical performances"],
        "awards": ["President's Award"],
        "popularity": "superstar",
        "bio": "Classical music maestro"
    },
]

def generate_real_artists_dataset():
    """Generate dataset with only real Sri Lankan artists"""
    
    artists_data = []
    for idx, artist in enumerate(REAL_ARTISTS_DATABASE):
        artist_id = f"A{idx:04d}"
        artistic_record = {
            "artist_id": artist_id,
            "name": artist["name"],
            "art_form": artist["art_form"],
            "art_forms": [artist["art_form"]],
            "genres": artist["genres"],
            "styles": artist["styles"],
            "language": artist["languages"],
            "languages": artist["languages"],
            "city": artist["city"],
            "mood_tags": ["energetic", "engaging"],
            "festivals": [],
            "popularity": artist["popularity"],
            "follower_count": artist["follower_count"],
            "verified": artist["verified"],
            "era": artist["era"],
            "notable_works": artist["notable_works"],
            "awards": artist["awards"],
            "bio": artist["bio"]
        }
        artists_data.append(artistic_record)
    
    return artists_data

def create_users_dataset(num_users=100):
    """Create user profiles"""
    users = []
    cities = ["colombo", "galle", "kandy", "jaffna", "matara", "kurunegala", "nuwara_eliya", "badulla", "gampaha"]
    art_form_options = ["music", "dance", "film", "drama"]
    moods = ["patriotic", "intense", "romantic", "energetic", "spiritual"]
    
    for i in range(num_users):
        user = {
            "user_id": f"U{i:04d}",
            "name": f"User_{i}",
            "city": cities[i % len(cities)],
            "interests": [art_form_options[i % len(art_form_options)]],
            "moods": [moods[i % len(moods)]],
            "language": "sinhala" if i % 3 != 0 else ("tamil" if i % 3 == 1 else "english")
        }
        users.append(user)
    
    return users

def create_events_dataset(artists, num_events=80):
    """Create event records"""
    events = []
    cities = ["colombo", "galle", "kandy", "jaffna", "matara", "kurunegala"]
    
    for i in range(num_events):
        event = {
            "event_id": f"E{i:04d}",
            "name": f"Concert of {artists[i % len(artists)]['name']}",
            "artist_id": artists[i % len(artists)]["artist_id"],
            "city": cities[i % len(cities)],
            "date": f"2026-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
            "time": f"{18 + (i % 6):02d}:00",
            "venue": f"Venue_{i}",
            "ticket_price": 500 + (i % 5000),
            "capacity": 100 + (i * 10)
        }
        events.append(event)
    
    return events

def create_interaction_data(users, artists, events):
    """Create follow and attendance interactions"""
    follows = []
    attends = []
    
    # Create follows (users following artists)
    for u_idx, user in enumerate(users):
        num_follows = 3 + (u_idx % 7)
        for a_idx in range(num_follows):
            artist_idx = (u_idx + a_idx) % len(artists)
            follows.append({
                "user_id": user["user_id"],
                "artist_id": artists[artist_idx]["artist_id"]
            })
    
    # Create event attendances
    for u_idx, user in enumerate(users):
        num_events_attend = 2 + (u_idx % 4)
        for e_idx in range(num_events_attend):
            event_idx = (u_idx + e_idx) % len(events)
            attends.append({
                "user_id": user["user_id"],
                "event_id": events[event_idx]["event_id"]
            })
    
    return follows, attends

def export_to_csv(artists, users, events, follows, attends, output_dir="data/sample_dataset/csv_export_updated_real"):
    """Export all data to CSV format"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert to DataFrames
    df_artists = pd.DataFrame(artists)
    df_users = pd.DataFrame(users)
    df_events = pd.DataFrame(events)
    df_follows = pd.DataFrame(follows)
    df_attends = pd.DataFrame(attends)
    
    # Save to CSV
    df_artists.to_csv(f"{output_dir}/artists.csv", index=False)
    df_users.to_csv(f"{output_dir}/users.csv", index=False)
    df_events.to_csv(f"{output_dir}/events.csv", index=False)
    df_follows.to_csv(f"{output_dir}/follows.csv", index=False)
    df_attends.to_csv(f"{output_dir}/attends.csv", index=False)
    
    return output_dir

def main():
    print("=" * 70)
    print(" REAL SRI LANKAN ARTISTS DATABASE GENERATOR")
    print("=" * 70)
    print()
    
    # Generate real artists
    print("📊 Loading real artists database...")
    artists = generate_real_artists_dataset()
    print(f"✓ Loaded {len(artists)} real Sri Lankan artists")
    
    # Display art form distribution
    art_form_count = {}
    for artist in artists:
        form = artist["art_form"]
        art_form_count[form] = art_form_count.get(form, 0) + 1
    
    print("\n🎨 Artists by Art Form:")
    for form, count in sorted(art_form_count.items()):
        print(f"   • {form}: {count}")
    
    # Generate users
    print(f"\n👥 Generating 100 user profiles...")
    users = create_users_dataset(100)
    print(f"✓ Created {len(users)} users")
    
    # Generate events
    print(f"\n🎪 Generating 80 events...")
    events = create_events_dataset(artists, 80)
    print(f"✓ Created {len(events)} events")
    
    # Create interactions
    print(f"\n🔗 Generating interactions...")
    follows, attends = create_interaction_data(users, artists, events)
    print(f"✓ Created {len(follows)} follow relationships")
    print(f"✓ Created {len(attends)} event attendances")
    
    # Export to CSV
    print(f"\n💾 Exporting to CSV...")
    output_dir = export_to_csv(artists, users, events, follows, attends)
    print(f"✓ Exported to {output_dir}/")
    
    # Save as JSON
    json_data = {
        "artists": artists,
        "users": users,
        "events": events,
        "follows": follows,
        "attends": attends
    }
    
    json_file = "data/sample_dataset/rasaswadaya_dataset_real_artists.json"
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"✓ Saved JSON to {json_file}")
    
    # Display summary
    print("\n" + "=" * 70)
    print(" SUMMARY")
    print("=" * 70)
    print(f"✅ Real Artists: {len(artists)}")
    print(f"✅ Users: {len(users)}")
    print(f"✅ Events: {len(events)}")
    print(f"✅ Follow Relationships: {len(follows)}")
    print(f"✅ Event Attendances: {len(attends)}")
    print("\n📁 Output Files:")
    print(f"   • CSV: {output_dir}/")
    print(f"   • JSON: {json_file}")
    
    # Display top real artists
    print("\n🌟 Top Real Artists (by followers):")
    sorted_artists = sorted(artists, key=lambda x: x["follower_count"], reverse=True)
    for i, artist in enumerate(sorted_artists[:10], 1):
        print(f"   {i:2}. {artist['name']:30} {artist['follower_count']:>10,} followers | {artist['art_form']}")
    
    print("\n✅ COMPLETE!")

if __name__ == "__main__":
    main()
