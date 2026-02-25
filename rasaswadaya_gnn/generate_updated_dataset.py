#!/usr/bin/env python3
"""
Generate Updated Dataset with New Taxonomy
==========================================
Creates a fresh dataset using the new 4 art form taxonomy.
"""

import json
import pickle
import pandas as pd
from pathlib import Path
from datetime import datetime
from data.generate_sample_data import generate_sample_dataset

def generate_and_export_dataset():
    """Generate new dataset and export to multiple formats."""
    
    print("=" * 70)
    print(" GENERATING UPDATED DATASET")
    print(" Using New Taxonomy: 4 Art Forms, 3 Languages, 71 Moods")
    print("=" * 70)
    
    # Generate dataset with updated taxonomy
    print("\n📊 Generating sample dataset...")
    print("   Users: 200")
    print("   Artists: 100")
    print("   Events: 150")
    
    dataset = generate_sample_dataset(
        num_users=200,
        num_artists=100,
        num_events=150
    )
    
    print(f"\n✅ Dataset generated successfully!")
    print(f"   Users: {len(dataset['users'])}")
    print(f"   Artists: {len(dataset['artists'])}")
    print(f"   Events: {len(dataset['events'])}")
    print(f"   Follows: {len(dataset['interactions']['follows'])}")
    print(f"   Attends: {len(dataset['interactions']['attends'])}")
    
    # Save to JSON
    output_dir = Path(__file__).parent / 'data' / 'sample_dataset'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    json_file = output_dir / 'rasaswadaya_dataset_updated.json'
    print(f"\n💾 Saving to JSON: {json_file.name}")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"   ✓ JSON saved ({json_file.stat().st_size / 1024:.1f} KB)")
    
    # Save to Pickle
    pkl_file = output_dir / 'rasaswadaya_dataset_updated.pkl'
    print(f"\n💾 Saving to Pickle: {pkl_file.name}")
    with open(pkl_file, 'wb') as f:
        pickle.dump(dataset, f)
    print(f"   ✓ Pickle saved ({pkl_file.stat().st_size / 1024:.1f} KB)")
    
    # Export to CSV
    csv_dir = output_dir / 'csv_export_updated'
    csv_dir.mkdir(exist_ok=True)
    
    print(f"\n📁 Exporting to CSV: {csv_dir.name}/")
    
    # Export Users
    users_df = pd.DataFrame(dataset['users'])
    users_file = csv_dir / 'users.csv'
    users_df.to_csv(users_file, index=False, encoding='utf-8')
    print(f"   ✓ users.csv ({len(users_df):,} rows)")
    
    # Export Artists
    artists_df = pd.DataFrame(dataset['artists'])
    artists_file = csv_dir / 'artists.csv'
    artists_df.to_csv(artists_file, index=False, encoding='utf-8')
    print(f"   ✓ artists.csv ({len(artists_df):,} rows)")
    
    # Export Events
    events_df = pd.DataFrame(dataset['events'])
    events_file = csv_dir / 'events.csv'
    events_df.to_csv(events_file, index=False, encoding='utf-8')
    print(f"   ✓ events.csv ({len(events_df):,} rows)")
    
    # Export Follows
    follows_df = pd.DataFrame(dataset['interactions']['follows'])
    follows_file = csv_dir / 'follows.csv'
    follows_df.to_csv(follows_file, index=False, encoding='utf-8')
    print(f"   ✓ follows.csv ({len(follows_df):,} rows)")
    
    # Export Attends
    attends_df = pd.DataFrame(dataset['interactions']['attends'])
    attends_file = csv_dir / 'attends.csv'
    attends_df.to_csv(attends_file, index=False, encoding='utf-8')
    print(f"   ✓ attends.csv ({len(attends_df):,} rows)")
    
    # Print sample statistics
    print(f"\n📊 Dataset Statistics:")
    print(f"   Art Forms Distribution:")
    art_forms_count = {}
    for artist in dataset['artists']:
        af = artist['art_forms'][0]
        art_forms_count[af] = art_forms_count.get(af, 0) + 1
    for af, count in sorted(art_forms_count.items()):
        print(f"      {af:15s}: {count:3d} artists ({count/len(dataset['artists'])*100:.1f}%)")
    
    print(f"\n   Language Distribution:")
    lang_count = {}
    for artist in dataset['artists']:
        for lang in artist['language']:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    for lang, count in sorted(lang_count.items()):
        print(f"      {lang:15s}: {count:3d} artists")
    
    print(f"\n   Top 5 Cities by Artist Count:")
    city_count = {}
    for artist in dataset['artists']:
        city = artist['city']
        city_count[city] = city_count.get(city, 0) + 1
    for city, count in sorted(city_count.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"      {city.title():15s}: {count:3d} artists")
    
    print("\n" + "=" * 70)
    print(" ✅ DATASET GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\nFiles created:")
    print(f"   1. {json_file.name}")
    print(f"   2. {pkl_file.name}")
    print(f"   3. csv_export_updated/users.csv")
    print(f"   4. csv_export_updated/artists.csv")
    print(f"   5. csv_export_updated/events.csv")
    print(f"   6. csv_export_updated/follows.csv")
    print(f"   7. csv_export_updated/attends.csv")
    print("=" * 70)
    
    return dataset


if __name__ == "__main__":
    dataset = generate_and_export_dataset()
