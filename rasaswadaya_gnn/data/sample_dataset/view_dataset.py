#!/usr/bin/env python3
"""
Dataset Viewer - Explore Rasaswadaya Dataset
============================================
Beautiful visualization of the dataset structure and contents.
"""

import pickle
import pandas as pd
from collections import Counter

# Load dataset
print("Loading dataset...")
with open("rasaswadaya_dataset.pkl", "rb") as f:
    dataset = pickle.load(f)

print("\n" + "="*80)
print(" " * 25 + "RASASWADAYA DATASET VIEWER")
print("="*80)

# Convert to DataFrames
df_users = pd.DataFrame(dataset['users'])
df_artists = pd.DataFrame(dataset['artists'])
df_events = pd.DataFrame(dataset['events'])
df_follows = pd.DataFrame(dataset['interactions']['follows'])
df_attends = pd.DataFrame(dataset['interactions']['attends'])

# ============================================================================
# OVERVIEW
# ============================================================================
print("\n📊 DATASET OVERVIEW")
print("-" * 80)
print(f"{'Entity Type':<20} {'Count':<15} {'Columns':<50}")
print("-" * 80)
print(f"{'Users':<20} {len(df_users):<15} {len(df_users.columns):<50}")
print(f"{'Artists':<20} {len(df_artists):<15} {len(df_artists.columns):<50}")
print(f"{'Events':<20} {len(df_events):<15} {len(df_events.columns):<50}")
print(f"{'Follow Relations':<20} {len(df_follows):<15} {len(df_follows.columns):<50}")
print(f"{'Event Attendance':<20} {len(df_attends):<15} {len(df_attends.columns):<50}")
print("-" * 80)
print(f"{'TOTAL ROWS':<20} {len(df_users) + len(df_artists) + len(df_events) + len(df_follows) + len(df_attends):<15}")
print("="*80)

# ============================================================================
# USERS
# ============================================================================
print("\n\n👥 USERS TABLE (Sample)")
print("-" * 80)
display_cols = ['user_id', 'name', 'ethnicity', 'language_preferences', 'art_interests', 'region_preference', 'activity_level']
print(df_users[display_cols].head(10).to_string(index=False))

print("\n📈 User Statistics:")
print(f"  • Activity Levels: {df_users['activity_level'].value_counts().to_dict()}")
print(f"  • Ethnicity Distribution: {df_users['ethnicity'].value_counts().to_dict()}")
print(f"  • Top Art Interests: {Counter([item for sublist in df_users['art_interests'] for item in sublist]).most_common(5)}")

# ============================================================================
# ARTISTS
# ============================================================================
print("\n\n🎨 ARTISTS TABLE (Sample)")
print("-" * 80)
display_cols = ['artist_id', 'name', 'art_forms', 'genres', 'region', 'language', 'popularity', 'follower_count']
print(df_artists[display_cols].head(10).to_string(index=False))

print("\n📈 Artist Statistics:")
print(f"  • Popularity Distribution: {df_artists['popularity'].value_counts().to_dict()}")
print(f"  • Top Genres: {Counter([item for sublist in df_artists['genres'] for item in sublist]).most_common(8)}")
print(f"  • Regional Distribution: {df_artists['region'].value_counts().head(5).to_dict()}")

# ============================================================================
# EVENTS
# ============================================================================
print("\n\n🎪 EVENTS TABLE (Sample)")
print("-" * 80)
display_cols = ['event_id', 'name', 'genres', 'region', 'venue', 'date', 'ticket_price', 'capacity']
print(df_events[display_cols].head(10).to_string(index=False))

print("\n📈 Event Statistics:")
print(f"  • Event Types: {df_events['event_type'].value_counts().to_dict()}")
print(f"  • Free Events: {(df_events['ticket_price'] == 0).sum()} ({(df_events['ticket_price'] == 0).sum() / len(df_events) * 100:.1f}%)")
print(f"  • Average Ticket Price: LKR {df_events[df_events['ticket_price'] > 0]['ticket_price'].mean():.0f}")
print(f"  • Top Venues: {df_events['venue'].value_counts().head(5).to_dict()}")

# ============================================================================
# INTERACTIONS - FOLLOWS
# ============================================================================
print("\n\n🔗 FOLLOW INTERACTIONS (Sample)")
print("-" * 80)
# Merge with names for readability
follows_display = df_follows.head(10).copy()
follows_display['user_name'] = follows_display['user_id'].map(df_users.set_index('user_id')['name'])
follows_display['artist_name'] = follows_display['artist_id'].map(df_artists.set_index('artist_id')['name'])
print(follows_display[['user_id', 'user_name', 'artist_id', 'artist_name', 'timestamp']].to_string(index=False))

print("\n📈 Follow Statistics:")
print(f"  • Total Follows: {len(df_follows):,}")
print(f"  • Average Follows per User: {len(df_follows) / len(df_users):.1f}")
print(f"  • Most Followed Artists:")
follows_count = df_follows['artist_id'].value_counts().head(5)
for artist_id, count in follows_count.items():
    artist_name = df_artists[df_artists['artist_id'] == artist_id]['name'].values[0]
    print(f"      • {artist_name}: {count} followers")

# ============================================================================
# INTERACTIONS - ATTENDS
# ============================================================================
print("\n\n🎟️  EVENT ATTENDANCE (Sample)")
print("-" * 80)
attends_display = df_attends.head(10).copy()
attends_display['user_name'] = attends_display['user_id'].map(df_users.set_index('user_id')['name'])
attends_display['event_name'] = attends_display['event_id'].map(df_events.set_index('event_id')['name'])
print(attends_display[['user_id', 'user_name', 'event_id', 'event_name', 'rsvp_status']].to_string(index=False))

print("\n📈 Attendance Statistics:")
print(f"  • Total RSVPs: {len(df_attends):,}")
print(f"  • Average RSVPs per User: {len(df_attends) / len(df_users):.1f}")
print(f"  • RSVP Status Distribution: {df_attends['rsvp_status'].value_counts().to_dict()}")
print(f"  • Most Popular Events:")
attends_count = df_attends['event_id'].value_counts().head(5)
for event_id, count in attends_count.items():
    event_name = df_events[df_events['event_id'] == event_id]['name'].values[0]
    print(f"      • {event_name}: {count} RSVPs")

# ============================================================================
# CULTURAL DNA BREAKDOWN
# ============================================================================
print("\n\n🧬 CULTURAL DNA FEATURES")
print("-" * 80)
print("Art Forms:", sorted(set([item for sublist in df_artists['art_forms'] for item in sublist])))
print("\nAll Genres:", sorted(set([item for sublist in df_artists['genres'] for item in sublist])))
print("\nLanguages:", sorted(set([item for sublist in df_artists['language'] for item in sublist])))
print("\nRegions:", sorted(df_artists['region'].unique()))
print("\nMoods:", sorted(set([item for sublist in df_artists['mood_tags'] for item in sublist])))
all_festivals = [item for sublist in df_artists['festivals'] for item in sublist if sublist]
print("\nFestivals:", sorted(set(all_festivals)) if all_festivals else "None")

# ============================================================================
# GRAPH STATISTICS
# ============================================================================
print("\n\n📊 GRAPH STRUCTURE")
print("-" * 80)
print(f"Total Nodes: {len(df_users) + len(df_artists) + len(df_events):,}")
print(f"  • User Nodes: {len(df_users):,}")
print(f"  • Artist Nodes: {len(df_artists):,}")
print(f"  • Event Nodes: {len(df_events):,}")
print(f"\nTotal Edges: {len(df_follows) + len(df_attends):,}")
print(f"  • User → Artist (follows): {len(df_follows):,}")
print(f"  • User → Event (attends): {len(df_attends):,}")

# Calculate some artist -> event edges
artist_event_edges = df_events['artist_ids'].apply(len).sum()
print(f"  • Artist → Event (performs_at): ~{artist_event_edges:,}")

print(f"\nGraph Density:")
print(f"  • Average degree: {(len(df_follows) + len(df_attends)) / (len(df_users) + len(df_artists) + len(df_events)):.2f}")

print("\n" + "="*80)
print(" " * 30 + "END OF REPORT")
print("="*80)

# ============================================================================
# SAVE TO CSV (OPTIONAL)
# ============================================================================
print("\n💾 Export Options:")
print("  To export to CSV files, run:")
print("    df_users.to_csv('users.csv', index=False)")
print("    df_artists.to_csv('artists.csv', index=False)")
print("    df_events.to_csv('events.csv', index=False)")
print("    df_follows.to_csv('follows.csv', index=False)")
print("    df_attends.to_csv('attends.csv', index=False)")
