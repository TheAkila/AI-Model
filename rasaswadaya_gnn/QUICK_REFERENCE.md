# QUICK REFERENCE: Updated System Usage
## Rasaswadaya GNN - New Cultural Database

---

## 🎯 WHAT CHANGED

### Quick Summary
- **Art Forms**: 6-8 → **4** (music, dance, film, drama)
- **Languages**: 6 → **3** (sinhala, tamil, english)
- **Moods**: 8 → **71** (categorized)
- **Styles**: Basic → **34 major + 100+ sub-genres**
- **Real Data**: 20 → **50+ artists, 30+ events, 25+ venues**

---

## 🚀 HOW TO USE

### 1. Import the New Taxonomy

```python
from data.cultural_constants import (
    get_art_forms,      # Returns: ['music', 'dance', 'film', 'drama']
    get_styles,         # Get styles for an art form
    get_sub_genres,     # Get sub-genres for a style
    get_languages,      # Returns: ['sinhala', 'tamil', 'english']
    get_moods,          # Get moods (all or by category)
    get_cities,         # Get all cities or by region
    get_city_coordinates  # Get GPS coordinates
)
```

### 2. Get Styles for an Art Form

```python
# Music styles (10 major categories)
music_styles = get_styles('music')
# ['traditional_indigenous', 'classical_semi_classical', 'baila',
#  'sinhala_commercial', 'tamil_commercial', 'hip_hop_rap',
#  'rock_alternative', 'devotional_religious', 'fusion', 'film_music']

# Dance styles (9 major categories)
dance_styles = get_styles('dance')
# ['kandyan_dance', 'low_country_dance', 'sabaragamuwa_dance',
#  'tamil_classical', 'muslim_cultural_dance', 'folk_dance',
#  'contemporary_modern', 'urban_street', 'ballroom_western']

# Film styles (10 categories)
film_styles = get_styles('film')
# ['commercial_cinema', 'art_parallel_cinema', 'political_cinema', ...]

# Drama styles (5 categories)
drama_styles = get_styles('drama')
# ['traditional_theatre', 'modern_stage_drama', 'teledrama',
#  'musical_drama', 'experimental_avant_garde']
```

### 3. Get Sub-genres for a Style

```python
# Get sub-genres for Baila music
baila_subgenres = get_sub_genres('music', 'baila')
# ['traditional_baila', 'modern_baila', 'party_baila']

# Get sub-genres for Kandyan dance
kandyan_subgenres = get_sub_genres('dance', 'kandyan_dance')
# ['ves_dance', 'naiyandi', 'pantheru', 'uddekki', 'vannam_dance']

# Get sub-genres for Commercial Cinema
commercial_film_subgenres = get_sub_genres('film', 'commercial_cinema')
# ['mass_action', 'romantic_commercial', 'comedy_commercial', 'family_drama']
```

### 4. Work with Moods (71 Total)

```python
# Get all moods
all_moods = get_moods()  # Returns all 71 moods

# Get moods by category
core_moods = get_moods('core')  # 27 universal emotional moods
# ['celebratory', 'spiritual', 'devotional', 'romantic', 'energetic', ...]

cultural_moods = get_moods('cultural')  # 15 Sri Lankan cultural moods
# ['ritualistic', 'ceremonial', 'heroic', 'mythological', ...]

music_moods = get_moods('music')  # 11 music-specific moods
# ['party', 'danceable', 'chill', 'acoustic_warm', 'heartbreak', ...]

dance_moods = get_moods('dance')  # 7 dance-specific moods
# ['rhythmic', 'theatrical', 'expressive', 'graceful', 'fierce', ...]

film_drama_moods = get_moods('film_drama')  # 11 cinematic moods
# ['suspense', 'thriller_tension', 'romantic_longing', 'satirical', ...]
```

### 5. Work with Cities and GPS Coordinates

```python
# Get all cities
all_cities = get_cities()  # 27 cities
# ['colombo', 'gampaha', 'kalutara', 'kandy', 'galle', ...]

# Get cities by region
western_cities = get_cities('western')
# ['colombo', 'gampaha', 'kalutara', 'negombo', 'panadura']

# Get GPS coordinates
lat, lon = get_city_coordinates('colombo')
# (6.9271, 79.8612)

lat, lon = get_city_coordinates('kandy')
# (7.2906, 80.6337)
```

---

## 🏗️ CREATE AN ARTIST PROFILE

### Example 1: Contemporary Sinhala Pop Artist

```python
yohani = {
    'artist_id': 'A0001',
    'name': 'Yohani',
    'art_forms': ['music'],
    'styles': ['sinhala_commercial'],           # Major style
    'genres': ['sinhala_pop', 'acoustic_pop'],  # Sub-genres
    'language': ['sinhala', 'english'],
    'city': 'colombo',
    'style': ['contemporary'],                   # Cultural style
    'mood_tags': ['romantic', 'chill', 'acoustic_warm'],
    'follower_count': 5200000,
    'verified': True
}
```

### Example 2: Traditional Kandyan Dancer

```python
chitrasena = {
    'artist_id': 'A0002',
    'name': 'Chitrasena',
    'art_forms': ['dance'],
    'styles': ['kandyan_dance'],
    'genres': ['ves_dance', 'vannam_dance'],
    'language': ['sinhala'],
    'city': 'kandy',
    'style': ['traditional'],
    'mood_tags': ['spiritual', 'ceremonial', 'graceful'],
    'follower_count': 450000,
    'verified': True
}
```

### Example 3: Film Director (Art Cinema)

```python
lester_james = {
    'artist_id': 'A0003',
    'name': 'Lester James Peries',
    'art_forms': ['film'],
    'styles': ['art_parallel_cinema'],
    'genres': ['realism', 'social_realism'],
    'language': ['sinhala'],
    'city': 'colombo',
    'style': ['traditional'],
    'mood_tags': ['reflective', 'social_awareness', 'intellectual'],
    'title': 'Father of Sri Lankan Cinema'
}
```

### Example 4: Modern Stage Drama Artist

```python
stage_director = {
    'artist_id': 'A0004',
    'name': 'Ranjith Dharmakeerthi',
    'art_forms': ['drama'],
    'styles': ['modern_stage_drama'],
    'genres': ['social_drama', 'political_theatre'],
    'language': ['sinhala'],
    'city': 'colombo',
    'style': ['contemporary'],
    'mood_tags': ['political_awareness', 'social_critique', 'intense']
}
```

---

## 🎭 GENERATE SAMPLE DATA

### Quick Start

```python
from data.generate_sample_data import (
    generate_artists,
    generate_users,
    generate_events,
    generate_interactions,
    generate_sample_dataset
)

# Generate complete dataset
dataset = generate_sample_dataset(
    num_users=100,
    num_artists=60,
    num_events=120
)

# Or generate components separately
artists = generate_artists(num_artists=50)
users = generate_users(num_users=100)
events = generate_events(artists, num_events=100)
interactions = generate_interactions(users, artists, events)
```

### Verify Generated Data

```python
# Check generated artists
for artist in artists[:3]:
    print(f"Name: {artist['name']}")
    print(f"  Art Form: {artist['art_forms']}")
    print(f"  Styles: {artist['styles']}")
    print(f"  Genres: {artist['genres']}")
    print(f"  Language: {artist['language']}")
    print(f"  City: {artist['city']}")
    print(f"  Moods: {artist['mood_tags']}")
    print()
```

---

## 🧪 TEST THE SYSTEM

### Run All Tests

```bash
cd rasaswadaya_gnn
python test_updated_system.py
```

Expected output:
```
✅ Test 1: Cultural Constants - PASSED
✅ Test 2: Configuration - PASSED
✅ Test 3: Cultural DNA Encoder - PASSED
✅ Test 4: Data Generator - PASSED
✅ Test 5: Graph Builder - PASSED
✅ Test 6: Demo Script - PASSED

🎉 ALL TESTS PASSED (6/6)
System is ready to use.
```

### Quick Validation

```python
# Test imports
from data.cultural_constants import *
from config import get_config
from models.cultural_dna import CulturalDNAEncoder

# Verify taxonomy
print("Art Forms:", get_art_forms())
# ['music', 'dance', 'film', 'drama']

print("Languages:", get_languages())
# ['sinhala', 'tamil', 'english']

print("Total Moods:", len(get_moods()))
# 71

# Test Cultural DNA encoder
encoder = CulturalDNAEncoder()
print("Cultural DNA Dimensions:", encoder.total_dims)
# 138
```

---

## 📊 MIGRATION FROM OLD SYSTEM

### Update Your Code

#### OLD WAY (6-8 Art Forms)
```python
# ❌ Old - Hardcoded
art_forms = ['dance', 'music', 'drama', 'visual_arts', 'literature', 'crafts']
genres = ['kandyan', 'baila', 'kolam', ...]  # Flat list
```

#### NEW WAY (4 Art Forms)
```python
# ✅ New - Dynamic
art_forms = get_art_forms()  # ['music', 'dance', 'film', 'drama']

# Hierarchical: Art Form → Style → Sub-genres
music_styles = get_styles('music')  # 10 major styles
baila_subgenres = get_sub_genres('music', 'baila')  # 3 sub-genres
```

### Update Language Handling

#### OLD WAY (6 Options)
```python
# ❌ Old
languages = ['sinhala', 'tamil', 'english',
             'mixed_sinhala_english',  # Removed
             'mixed_tamil_english',    # Removed
             'trilingual']             # Removed
```

#### NEW WAY (3 Primary)
```python
# ✅ New - Use multiple tags
languages = ['sinhala', 'tamil', 'english']

# For bilingual artists, use array:
artist['language'] = ['sinhala', 'english']  # Bilingual
```

### Update Mood Handling

#### OLD WAY (8 Basic)
```python
# ❌ Old
moods = ['celebratory', 'spiritual', 'romantic', ...]
```

#### NEW WAY (71 Categorized)
```python
# ✅ New - Get by category
core_moods = get_moods('core')  # 27 universal moods
music_moods = get_moods('music')  # 11 music-specific moods
all_moods = get_moods()  # All 71 moods
```

---

## 🎯 COMMON USE CASES

### 1. Find Artists by Art Form and Style

```python
artists = generate_artists(num_artists=100)

# Filter by art form
music_artists = [a for a in artists if 'music' in a['art_forms']]

# Filter by style
baila_artists = [a for a in artists if 'baila' in a['styles']]

# Filter by mood
romantic_artists = [a for a in artists if 'romantic' in a['mood_tags']]
```

### 2. Calculate Distance Between Cities

```python
from utils.distance_calculator import haversine_distance
from data.cultural_constants import get_city_coordinates

# Get coordinates
colombo_lat, colombo_lon = get_city_coordinates('colombo')
kandy_lat, kandy_lon = get_city_coordinates('kandy')

# Calculate distance
distance = haversine_distance(colombo_lat, colombo_lon, kandy_lat, kandy_lon)
print(f"Colombo to Kandy: {distance:.1f} km")
# Output: Colombo to Kandy: 115.4 km
```

### 3. Encode Artist Cultural DNA

```python
from models.cultural_dna import CulturalDNAEncoder

encoder = CulturalDNAEncoder()

artist_metadata = {
    'art_forms': ['music'],
    'genres': ['sinhala_pop', 'ballads'],
    'language': ['sinhala', 'english'],
    'style': ['contemporary'],
    'mood_tags': ['romantic', 'emotional']
}

dna = encoder.encode_artist(artist_metadata)
print(f"Cultural DNA Vector: {dna.vector.shape}")
# Output: Cultural DNA Vector: (138,)
```

### 4. Generate Dataset for Training

```python
from data.generate_sample_data import generate_sample_dataset

# Generate complete dataset
dataset = generate_sample_dataset(
    num_users=200,
    num_artists=100,
    num_events=150
)

# Save to JSON
import json
with open('my_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)
```

---

## 📚 REFERENCE DOCUMENTS

1. **COMPLETE_CULTURAL_DATABASE_2026.md** - Master reference with all real artists
2. **IMPLEMENTATION_GUIDE.md** - Detailed usage examples
3. **SYSTEM_UPDATE_SUMMARY.md** - Complete change log
4. **SYSTEM_OVERVIEW.md** - GNN architecture documentation

---

## ✅ VALIDATION

Run this to verify your system is updated correctly:

```python
from data.cultural_constants import *

assert len(get_art_forms()) == 4, "Should have 4 art forms"
assert len(get_languages()) == 3, "Should have 3 languages"
assert len(get_moods()) >= 70, "Should have 70+ moods"
assert len(get_cities()) >= 27, "Should have 27+ cities"

print("✅ System validated successfully!")
```

---

**Status**: ✅ SYSTEM READY  
**Version**: 2.0 (Updated Cultural Database)  
**Last Updated**: February 25, 2026
