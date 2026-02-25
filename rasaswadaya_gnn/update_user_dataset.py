#!/usr/bin/env python3
"""Analyze artists dataset and update user dataset with diverse interests"""
import pandas as pd
import ast
import random
from pathlib import Path

# Load artists
csv_dir = Path('data/sample_dataset/csv_export_updated_real')
artists = pd.read_csv(csv_dir / 'artists.csv')
users = pd.read_csv(csv_dir / 'users.csv')

print("=" * 70)
print("ARTISTS DATASET ANALYSIS")
print("=" * 70)

# Extract all unique genres
all_genres = set()
for genres_str in artists['genres']:
    try:
        genres_list = ast.literal_eval(genres_str) if isinstance(genres_str, str) else genres_str
        all_genres.update(genres_list)
    except:
        pass

print(f"\n📚 Available Genres: {len(all_genres)}")
genres_list = sorted(list(all_genres))
for i, genre in enumerate(genres_list, 1):
    print(f"   {i:2d}. {genre}")

# Extract all unique moods
all_moods = set()
for moods_str in artists['mood_tags']:
    try:
        moods_list = ast.literal_eval(moods_str) if isinstance(moods_str, str) else moods_str
        all_moods.update(moods_list)
    except:
        pass

print(f"\n🎭 Available Moods: {len(all_moods)}")
moods_list = sorted(list(all_moods))
for i, mood in enumerate(moods_list, 1):
    print(f"   {i:2d}. {mood}")

# Extract all unique art forms
art_forms = sorted(list(artists['art_form'].unique()))
print(f"\n🎨 Available Art Forms: {len(art_forms)}")
for i, form in enumerate(art_forms, 1):
    print(f"   {i}. {form}")

print("\n" + "=" * 70)
print("CURRENT USER DATASET STRUCTURE")
print("=" * 70)
print(f"\nTotal Users: {len(users)}")
print("\nSample Users:")
print(users[['user_id', 'name', 'city', 'interests', 'moods']].head(10).to_string())

print("\n" + "=" * 70)
print("UPDATING USER DATASET WITH MULTIPLE INTERESTS & GENRES")
print("=" * 70)

# Update users to have multiple interests and genres
random.seed(42)

def update_user_interests(user, genres_list, moods_list, art_forms):
    """Update user with multiple interests and genres"""
    # Each user gets 1-3 art form interests
    num_interests = random.randint(1, 3)
    user_art_interests = random.sample(art_forms, min(num_interests, len(art_forms)))
    
    # Each user gets 2-4 mood preferences
    num_moods = random.randint(2, 4)
    user_moods = random.sample(moods_list, min(num_moods, len(moods_list)))
    
    # Each user gets 2-5 genre preferences (filtered by their art form interests)
    num_genres = random.randint(2, 5)
    user_genres = random.sample(genres_list, min(num_genres, len(genres_list)))
    
    return {
        'art_interests': user_art_interests,
        'genres': user_genres,
        'moods': user_moods
    }

# Create updated users dataframe
users_data = []
for idx, row in users.iterrows():
    user_dict = row.to_dict()
    
    # Parse existing interests and moods
    try:
        current_interests = ast.literal_eval(row['interests']) if isinstance(row['interests'], str) else row['interests']
    except:
        current_interests = ['music']
    
    try:
        current_moods = ast.literal_eval(row['moods']) if isinstance(row['moods'], str) else row['moods']
    except:
        current_moods = ['energetic']
    
    # Generate multiple interests and genres
    updates = update_user_interests(user_dict, genres_list, moods_list, art_forms)
    
    user_dict['art_interests'] = str(updates['art_interests'])
    user_dict['genres'] = str(updates['genres'])
    user_dict['moods'] = str(updates['moods'])
    
    # Keep original interests for backward compatibility
    user_dict['interests'] = str(updates['art_interests'])
    
    users_data.append(user_dict)

# Create new dataframe with updated users
users_updated = pd.DataFrame(users_data)

# Save updated users
users_updated.to_csv(csv_dir / 'users.csv', index=False)

print("\n✅ Users dataset updated!")
print("\nUpdated Sample Users:")
print(users_updated[['user_id', 'name', 'city', 'art_interests', 'genres', 'moods']].head(10).to_string())

print("\n" + "=" * 70)
print("✅ USER DATASET SUCCESSFULLY UPDATED")
print("=" * 70)
