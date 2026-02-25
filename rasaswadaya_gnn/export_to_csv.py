#!/usr/bin/env python3
"""
CSV Export Script for Updated Dataset
=====================================
Exports the generated dataset to CSV files.
"""

import json
import csv
from pathlib import Path

def export_to_csv(dataset_file='data/sample_dataset/rasaswadaya_dataset_updated.json'):
    """Export dataset to CSV files."""
    
    print("=" * 70)
    print(" CSV EXPORT - UPDATED DATASET")
    print("=" * 70)
    
    # Load dataset
    dataset_path = Path(dataset_file)
    if not dataset_path.exists():
        print(f"\n❌ Dataset file not found: {dataset_file}")
        print("   Please run generate_new_data.py first!")
        return
    
    print(f"\n📂 Loading dataset from {dataset_path.name}...")
    with open(dataset_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    print(f"   ✓ Loaded {len(dataset['users'])} users")
    print(f"   ✓ Loaded {len(dataset['artists'])} artists")
    print(f"   ✓ Loaded {len(dataset['events'])} events")
    
    # Create output directory
    csv_dir = Path('data/sample_dataset/csv_export_updated')
    csv_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Exporting to {csv_dir}/")
    
    # Export Users
    print(f"\n   Exporting users...")
    users_file = csv_dir / 'users.csv'
    with open(users_file, 'w', newline='', encoding='utf-8') as f:
        if dataset['users']:
            writer = csv.DictWriter(f, fieldnames=dataset['users'][0].keys())
            writer.writeheader()
            writer.writerows(dataset['users'])
    print(f"   ✓ users.csv ({len(dataset['users'])} rows)")
    
    # Export Artists
    print(f"   Exporting artists...")
    artists_file = csv_dir / 'artists.csv'
    with open(artists_file, 'w', newline='', encoding='utf-8') as f:
        if dataset['artists']:
            writer = csv.DictWriter(f, fieldnames=dataset['artists'][0].keys())
            writer.writeheader()
            writer.writerows(dataset['artists'])
    print(f"   ✓ artists.csv ({len(dataset['artists'])} rows)")
    
    # Export Events
    print(f"   Exporting events...")
    events_file = csv_dir / 'events.csv'
    with open(events_file, 'w', newline='', encoding='utf-8') as f:
        if dataset['events']:
            writer = csv.DictWriter(f, fieldnames=dataset['events'][0].keys())
            writer.writeheader()
            writer.writerows(dataset['events'])
    print(f"   ✓ events.csv ({len(dataset['events'])} rows)")
    
    # Export Follows
    print(f"   Exporting follows...")
    follows_file = csv_dir / 'follows.csv'
    with open(follows_file, 'w', newline='', encoding='utf-8') as f:
        if dataset['interactions']['follows']:
            writer = csv.DictWriter(f, fieldnames=dataset['interactions']['follows'][0].keys())
            writer.writeheader()
            writer.writerows(dataset['interactions']['follows'])
    print(f"   ✓ follows.csv ({len(dataset['interactions']['follows'])} rows)")
    
    # Export Attends
    print(f"   Exporting attends...")
    attends_file = csv_dir / 'attends.csv'
    with open(attends_file, 'w', newline='', encoding='utf-8') as f:
        if dataset['interactions']['attends']:
            writer = csv.DictWriter(f, fieldnames=dataset['interactions']['attends'][0].keys())
            writer.writeheader()
            writer.writerows(dataset['interactions']['attends'])
    print(f"   ✓ attends.csv ({len(dataset['interactions']['attends'])} rows)")
    
    print("\n" + "=" * 70)
    print(" ✅ CSV EXPORT COMPLETE!")
    print("=" * 70)
    print(f"\nFiles created in {csv_dir}:")
    print(f"   1. users.csv")
    print(f"   2. artists.csv")
    print(f"   3. events.csv")
    print(f"   4. follows.csv")
    print(f"   5. attends.csv")
    print("=" * 70)


if __name__ == "__main__":
    export_to_csv()
