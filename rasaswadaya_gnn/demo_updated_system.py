#!/usr/bin/env python3
"""
Final System Demonstration
==========================
Shows the updated system generating sample data with the new taxonomy.
"""

print('=' * 70)
print(' FINAL SYSTEM DEMONSTRATION')
print('=' * 70)

from data.generate_sample_data import generate_sample_dataset
from data.cultural_constants import get_city_coordinates

print('\n📊 Generating sample dataset...')
dataset = generate_sample_dataset(
    num_users=20,
    num_artists=15,
    num_events=10
)

print(f'\n✅ Dataset generated successfully!')
print(f'   Users: {len(dataset["users"])}')
print(f'   Artists: {len(dataset["artists"])}')
print(f'   Events: {len(dataset["events"])}')
print(f'   Follow interactions: {len(dataset["interactions"]["follows"])}')

print(f'\n🎨 Sample Artist Profiles (First 3):')
print('-' * 70)
for i, artist in enumerate(dataset['artists'][:3], 1):
    print(f'\n{i}. {artist["name"]}')
    print(f'   Art Form: {artist["art_forms"][0]}')
    print(f'   Styles: {artist.get("styles", ["N/A"])}')
    print(f'   Sub-genres: {artist["genres"][:2]}...')
    print(f'   Language: {artist["language"]}')
    print(f'   City: {artist["city"]}')
    print(f'   Moods: {artist["mood_tags"][:3]}')
    print(f'   Followers: {artist["follower_count"]:,}')

print(f'\n📍 Sample Cities with GPS:')
print('-' * 70)
sample_cities = ['colombo', 'kandy', 'galle', 'jaffna']
for city in sample_cities:
    lat, lon = get_city_coordinates(city)
    print(f'   {city.title():15s} → {lat:.4f}°N, {lon:.4f}°E')

print('\n' + '=' * 70)
print(' ✅ SYSTEM FULLY OPERATIONAL!')
print('=' * 70)
print('\nNext steps:')
print('  1. Review QUICK_REFERENCE.md for usage examples')
print('  2. Review SYSTEM_UPDATE_SUMMARY.md for complete changes')
print('  3. Run: python demo.py (to train GNN model)')
print('  4. Add real artists from COMPLETE_CULTURAL_DATABASE_2026.md')
print('=' * 70)
