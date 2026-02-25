#!/usr/bin/env python3
import pandas as pd
import json

# Load the CSV
df = pd.read_csv('data/sample_dataset/csv_export_updated_real/artists.csv')

print("=" * 80)
print("ALL 28 REAL SRI LANKAN ARTISTS")
print("=" * 80)
print()

# Display all artists
for idx, row in df.iterrows():
    followers = row['follower_count']
    name = row['name']
    art_form = row['art_form']
    popularity = row['popularity']
    verified = '✓' if row['verified'] else '○'
    print(f"{idx+1:2}. {verified} {name:35} {art_form:8} {followers:>10,} followers | {popularity}")

print()
print("=" * 80)
print(f"TOTAL REAL ARTISTS: {len(df)}")
print("=" * 80)

# Distribution
print("\n📊 DISTRIBUTION BY ART FORM:")
print(df['art_form'].value_counts().sort_index().to_string())

# Load JSON for details
print("\n\n🌟 SAMPLE ARTISTS WITH DETAILS:")
with open('data/sample_dataset/rasaswadaya_dataset_real_artists.json') as f:
    data = json.load(f)

for artist in data['artists'][:8]:
    print(f"\n   {artist['name']}")
    print(f"      Art Form: {artist['art_form']}")
    print(f"      Era: {artist['era']}")
    print(f"      Followers: {artist['follower_count']:,}")
    print(f"      Bio: {artist['bio']}")
