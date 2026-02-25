import pandas as pd
import random

# Read current events data
events_df = pd.read_csv('data/sample_dataset/csv_export_updated_real/events.csv')

# Read artists to get their info
artists_df = pd.read_csv('data/sample_dataset/csv_export_updated_real/artists.csv')

# Create list of all artist IDs
all_artist_ids = artists_df['artist_id'].tolist()

# Update events to have multiple artists
# Keep about 50% with single artist, 35% with 2 artists, 15% with 3+ artists
new_artist_ids = []

for idx, event in events_df.iterrows():
    original_artist = event['artist_id']
    
    # Decide number of artists
    rand = random.random()
    if rand < 0.50:
        # Single artist (keep original)
        artists = [original_artist]
    elif rand < 0.85:
        # 2 artists
        other_artists = [a for a in all_artist_ids if a != original_artist]
        artists = [original_artist, random.choice(other_artists)]
    else:
        # 3 artists
        other_artists = [a for a in all_artist_ids if a != original_artist]
        artists = [original_artist] + random.sample(other_artists, min(2, len(other_artists)))
    
    new_artist_ids.append(str(artists))

# Create new dataframe with artist_ids instead of artist_id
events_updated = events_df.copy()
events_updated['artist_ids'] = new_artist_ids
events_updated = events_updated.drop('artist_id', axis=1)

# Reorder columns to put artist_ids after event_id
cols = events_updated.columns.tolist()
cols.insert(1, cols.pop(cols.index('artist_ids')))
events_updated = events_updated[cols]

# Show first few rows
print("Updated Events Dataset (with multiple artists):")
print("=" * 100)
print(events_updated.head(20).to_string())
print(f"\nTotal events: {len(events_updated)}")

# Count distribution
single_artist = sum(1 for artists_str in events_updated['artist_ids'] if artists_str.count("['") == 1)
dual_artist = sum(1 for artists_str in events_updated['artist_ids'] if artists_str.count(',') == 1)
multi_artist = sum(1 for artists_str in events_updated['artist_ids'] if artists_str.count(',') > 1)

print(f"\nArtist Distribution:")
print(f"  Single artist events: {single_artist} ({100*single_artist/len(events_updated):.1f}%)")
print(f"  Dual artist events: {dual_artist} ({100*dual_artist/len(events_updated):.1f}%)")
print(f"  Multi-artist events (3+): {multi_artist} ({100*multi_artist/len(events_updated):.1f}%)")

# Save to CSV
output_path = 'data/sample_dataset/csv_export_updated_real/events.csv'
events_updated.to_csv(output_path, index=False)
print(f"\n✓ Events dataset updated successfully!")
