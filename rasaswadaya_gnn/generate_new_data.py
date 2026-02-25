#!/usr/bin/env python3
"""
Generate Updated Dataset - Simple Version
========================================
Creates dataset using new taxonomy and exports to JSON.
"""

import json
import pickle
from pathlib import Path
from data.generate_sample_data import generate_sample_dataset

print("=" * 70)
print(" GENERATING UPDATED DATASET")
print("=" * 70)

print("\n📊 Generating sample dataset...")
dataset = generate_sample_dataset(
    num_users=200,
    num_artists=100,
    num_events=150
)

print(f"\n✅ Generated:")
print(f"   Users: {len(dataset['users'])}")
print(f"   Artists: {len(dataset['artists'])}")
print(f"   Events: {len(dataset['events'])}")
print(f"   Follows: {len(dataset['interactions']['follows'])}")

# Save to JSON
output_dir = Path('data/sample_dataset')
output_dir.mkdir(parents=True, exist_ok=True)

json_file = output_dir / 'rasaswadaya_dataset_updated.json'
print(f"\n💾 Saving JSON...")
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)
print(f"   ✓ Saved: {json_file}")

# Save to Pickle
pkl_file = output_dir / 'rasaswadaya_dataset_updated.pkl'
print(f"\n💾 Saving Pickle...")
with open(pkl_file, 'wb') as f:
    pickle.dump(dataset, f)
print(f"   ✓ Saved: {pkl_file}")

print("\n✅ COMPLETE!")
