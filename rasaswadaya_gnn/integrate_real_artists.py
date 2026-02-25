#!/usr/bin/env python3
"""
Real Artist Integration Script
===============================
Integrates real Sri Lankan artists from COMPLETE_CULTURAL_DATABASE_2026.md
into the dataset.
"""

# Real Sri Lankan Artists Database
REAL_ARTISTS = [
    # MUSIC - LEGENDS
    {
        "artist_id": "RA001",
        "name": "W.D. Amaradeva",
        "art_forms": ["music"],
        "styles": ["classical_semi_classical", "devotional_religious"],
        "genres": ["sinhala_classical", "light_classical", "buddhist_devotional"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["traditional"],
        "mood_tags": ["spiritual", "devotional", "reflective", "peaceful"],
        "festivals": ["vesak", "poson"],
        "popularity": "established",
        "follower_count": 1500000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Sasara Wasana Thuru", "Budu Sadu", "Giligili Mese"],
        "awards": ["Kala Keerthi", "Deshamanya", "Padma Sri India"]
    },
    {
        "artist_id": "RA002",
        "name": "Nanda Malini",
        "art_forms": ["music"],
        "styles": ["classical_semi_classical", "devotional_religious"],
        "genres": ["sinhala_classical", "devotional", "patriotic_songs"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["traditional"],
        "mood_tags": ["devotional", "spiritual", "patriotic", "emotional"],
        "festivals": ["vesak", "independence_day"],
        "popularity": "established",
        "follower_count": 850000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Pipena Kusuma", "Punchi Suranganavi", "Dase Dasi Kula"],
        "awards": ["Kala Keerthi", "Deshamanya"]
    },
    
    # MUSIC - CONTEMPORARY POP
    {
        "artist_id": "RA003",
        "name": "Yohani",
        "art_forms": ["music"],
        "styles": ["sinhala_commercial"],
        "genres": ["sinhala_pop", "acoustic_pop"],
        "language": ["sinhala", "english"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["romantic", "chill", "acoustic_warm", "heartbreak"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 5200000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Manike Mage Hithe", "Sathuta", "Aaye"],
        "youtube_subscribers": 2800000,
        "viral_hit": True
    },
    {
        "artist_id": "RA004",
        "name": "Bathiya & Santhush",
        "art_forms": ["music"],
        "styles": ["sinhala_commercial"],
        "genres": ["sinhala_pop", "dance_pop", "ballads"],
        "language": ["sinhala", "english"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["energetic", "romantic", "celebratory", "party"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 1200000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Yaalpanamen", "Athdakawe Hitha Watila"],
        "grammy_nominated": True
    },
    {
        "artist_id": "RA005",
        "name": "Rookantha Gunathilaka",
        "art_forms": ["music"],
        "styles": ["sinhala_commercial"],
        "genres": ["sinhala_pop", "ballads", "love_songs"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["romantic", "emotional", "dramatic_ballad"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 900000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Dileepa Podi Puthu", "Sanda Eliye"]
    },
    
    # MUSIC - HIP HOP/RAP
    {
        "artist_id": "RA006",
        "name": "Costa",
        "art_forms": ["music"],
        "styles": ["hip_hop_rap"],
        "genres": ["sinhala_rap", "trap"],
        "language": ["sinhala", "english"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["energetic", "rebel", "urban_street", "powerful"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 380000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Salli", "Chooty Malli Polla"],
        "genre_pioneer": "Sinhala Rap"
    },
    
    # MUSIC - BAILA
    {
        "artist_id": "RA007",
        "name": "Sunil Perera",
        "art_forms": ["music"],
        "styles": ["baila"],
        "genres": ["modern_baila", "party_baila"],
        "language": ["sinhala", "english"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["celebratory", "party", "energetic", "danceable"],
        "festivals": ["sinhala_tamil_new_year"],
        "popularity": "established",
        "follower_count": 800000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Kurumitto", "Signore", "Hotel Polanda"],
        "band": "Gypsies"
    },
    
    # DANCE - TRADITIONAL
    {
        "artist_id": "RA008",
        "name": "Chitrasena",
        "art_forms": ["dance"],
        "styles": ["kandyan_dance", "contemporary_modern"],
        "genres": ["ves_dance", "vannam_dance", "interpretative"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["traditional", "fusion"],
        "mood_tags": ["graceful", "spiritual", "theatrical", "expressive"],
        "festivals": ["esala_perahera"],
        "popularity": "established",
        "follower_count": 450000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Gajaga Vannama", "Developed modern Lankan dance"],
        "title": "Father of Modern Sri Lankan Dance"
    },
    {
        "artist_id": "RA009",
        "name": "Vajira Chitrasena",
        "art_forms": ["dance"],
        "styles": ["kandyan_dance", "contemporary_modern"],
        "genres": ["classical_kandyan", "modern_interpretative"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["traditional", "contemporary"],
        "mood_tags": ["graceful", "expressive", "theatrical", "empowerment"],
        "festivals": ["esala_perahera"],
        "popularity": "established",
        "follower_count": 380000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Revolutionized Lankan dance"],
        "title": "Dance Legend"
    },
    
    # FILM - DIRECTORS & ACTORS
    {
        "artist_id": "RA010",
        "name": "Lester James Peries",
        "art_forms": ["film"],
        "styles": ["art_parallel_cinema"],
        "genres": ["realism", "social_realism", "festival_cinema"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["traditional"],
        "mood_tags": ["reflective", "social_awareness", "intellectual", "serious"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 520000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Rekava", "Gamperaliya", "Nidhanaya", "Kaliyugaya"],
        "title": "Father of Sri Lankan Cinema",
        "awards": ["Ramon Magsaysay Award"]
    },
    {
        "artist_id": "RA011",
        "name": "Jackson Anthony",
        "art_forms": ["film", "drama"],
        "styles": ["commercial_cinema", "teledrama"],
        "genres": ["family_drama", "romantic_commercial"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["emotional", "dramatic", "romantic"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 900000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Aba", "Adaraniya Poornima", "Sulaga Sandi"]
    },
    
    # DRAMA/THEATRE
    {
        "artist_id": "RA012",
        "name": "Ediriweera Sarachchandra",
        "art_forms": ["drama"],
        "styles": ["modern_stage_drama", "traditional_theatre"],
        "genres": ["nadagam", "modern_adaptations"],
        "language": ["sinhala"],
        "city": "peradeniya",
        "style": ["traditional", "contemporary"],
        "mood_tags": ["intellectual", "cultural_pride", "theatrical", "dramatic"],
        "festivals": [],
        "popularity": "established",
        "follower_count": 280000,
        "verified": True,
        "era": "legend",
        "notable_works": ["Maname", "Sinhabahu"],
        "title": "Revived Sinhala Theatre"
    },
    
    # Additional Contemporary Artists
    {
        "artist_id": "RA013",
        "name": "Sanuka Wickramasinghe",
        "art_forms": ["music"],
        "styles": ["sinhala_commercial"],
        "genres": ["ballads", "emotional_pop"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["romantic", "emotional", "heartbreak", "sad"],
        "festivals": [],
        "popularity": "mid_tier",
        "follower_count": 450000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Numba Mage", "Sanda Tharu"]
    },
    {
        "artist_id": "RA014",
        "name": "Iraj Weeraratne",
        "art_forms": ["music"],
        "styles": ["hip_hop_rap", "fusion"],
        "genres": ["sinhala_rap", "traditional_hip_hop_fusion"],
        "language": ["sinhala", "english"],
        "city": "colombo",
        "style": ["fusion"],
        "mood_tags": ["energetic", "fusion_energy", "urban_street"],
        "festivals": [],
        "popularity": "mid_tier",
        "follower_count": 320000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Mal Malak", "Working Man"]
    },
    {
        "artist_id": "RA015",
        "name": "Umaria Sinhawansa",
        "art_forms": ["music"],
        "styles": ["sinhala_commercial"],
        "genres": ["sinhala_pop", "acoustic_pop"],
        "language": ["sinhala"],
        "city": "colombo",
        "style": ["contemporary"],
        "mood_tags": ["romantic", "chill", "acoustic_warm"],
        "festivals": [],
        "popularity": "emerging",
        "follower_count": 280000,
        "verified": True,
        "era": "contemporary",
        "notable_works": ["Obage Namayen", "Pawela"]
    }
]

def integrate_real_artists(dataset):
    """Add real artists to the dataset."""
    
    print("=" * 70)
    print(" INTEGRATING REAL ARTISTS")
    print("=" * 70)
    
    print(f"\n📊 Current dataset:")
    print(f"   Artists: {len(dataset['artists'])}")
    
    print(f"\n➕ Adding {len(REAL_ARTISTS)} real Sri Lankan artists...")
    
    # Add real artists to the dataset
    dataset['artists'].extend(REAL_ARTISTS)
    
    print(f"\n✅ Updated dataset:")
    print(f"   Total artists: {len(dataset['artists'])}")
    print(f"   Real artists: {len(REAL_ARTISTS)}")
    print(f"   Generated artists: {len(dataset['artists']) - len(REAL_ARTISTS)}")
    
    # Print sample real artists
    print(f"\n🎨 Sample Real Artists:")
    print("-" * 70)
    for artist in REAL_ARTISTS[:5]:
        print(f"\n   {artist['name']}")
        print(f"      Art Form: {artist['art_forms'][0]}")
        print(f"      Styles: {artist['styles']}")
        print(f"      Era: {artist.get('era', 'N/A')}")
        print(f"      Followers: {artist['follower_count']:,}")
        if 'notable_works' in artist:
            print(f"      Notable Works: {', '.join(artist['notable_works'][:2])}")
    
    print("\n" + "=" * 70)
    print(" ✅ REAL ARTISTS INTEGRATED!")
    print("=" * 70)
    
    return dataset


def main():
    """Load dataset, add real artists, and save."""
    import json
    from pathlib import Path
    
    # Load generated dataset
    dataset_file = Path('data/sample_dataset/rasaswadaya_dataset_updated.json')
    
    if not dataset_file.exists():
        print(f"❌ Dataset not found: {dataset_file}")
        print("   Please run generate_new_data.py first!")
        return
    
    print(f"📂 Loading dataset...")
    with open(dataset_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    # Integrate real artists
    dataset = integrate_real_artists(dataset)
    
    # Save updated dataset
    output_file = Path('data/sample_dataset/rasaswadaya_dataset_with_real_artists.json')
    print(f"\n💾 Saving updated dataset to {output_file.name}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"   ✓ Saved!")
    
    print(f"\n🎉 Complete! Dataset now includes:")
    print(f"   • {len(REAL_ARTISTS)} real artists (W.D. Amaradeva, Yohani, Chitrasena, etc.)")
    print(f"   • {len(dataset['artists']) - len(REAL_ARTISTS)} generated artists")
    print(f"   • {len(dataset['users'])} users")
    print(f"   • {len(dataset['events'])} events")


if __name__ == "__main__":
    main()
