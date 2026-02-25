"""
Data loader - loads CSV files and dataset
"""
import pandas as pd
import pickle
import json
from pathlib import Path
import sys

# Get parent directory
parent_dir = Path(__file__).parent.parent.parent

def load_dataset():
    """Load dataset from CSV files (NEW REAL ARTISTS)"""
    try:
        # Try to load from new real artists CSV files first
        csv_dir = Path(__file__).parent.parent.parent / 'data' / 'sample_dataset' / 'csv_export_updated_real'
        
        # Load CSVs
        users_df = pd.read_csv(csv_dir / 'users.csv')
        artists_df = pd.read_csv(csv_dir / 'artists.csv')
        events_df = pd.read_csv(csv_dir / 'events.csv')
        follows_df = pd.read_csv(csv_dir / 'follows.csv')
        attends_df = pd.read_csv(csv_dir / 'attends.csv')
        
        # Convert to list of dicts
        users = users_df.to_dict('records')
        artists = artists_df.to_dict('records')
        events = events_df.to_dict('records')
        follows = follows_df.to_dict('records')
        attends = attends_df.to_dict('records')
        
        return users, artists, events, follows, attends
    except Exception as e:
        print(f"Error loading CSV dataset: {e}")
        # Fallback to pickle file if CSV fails
        dataset_path = Path(__file__).parent.parent.parent / 'data' / 'sample_dataset' / 'rasaswadaya_dataset.pkl'
        try:
            with open(dataset_path, 'rb') as f:
                dataset = pickle.load(f)
            return (dataset.get('users', []), 
                    dataset.get('artists', []), 
                    dataset.get('events', []),
                    dataset.get('follows', []),
                    dataset.get('attends', []))
        except Exception as e2:
            print(f"Error loading pickle dataset: {e2}")
            return [], [], [], [], []


def load_users_list():
    """Load and format users list for dropdown (with real artists data - ENHANCED)"""
    import ast
    users, artists, _, follows, _ = load_dataset()
    
    users_list = []
    for user in users:
        # Get followed artists for this user
        user_id = user.get('user_id')
        
        # Handle both dict/dataframe formats
        if isinstance(follows, pd.DataFrame):
            followed = follows[follows['user_id'] == user_id]['artist_id'].tolist()
        else:
            followed = [f.get('artist_id') for f in follows if f.get('user_id') == user_id]
        
        # Get artist names for followed artists
        followed_artist_names = []
        for artist_id in followed:
            for artist in artists:
                if artist.get('artist_id') == artist_id:
                    followed_artist_names.append(artist.get('name', artist_id))
                    break
        
        # Parse multiple interests and genres (NEW)
        def parse_list_field(field_value):
            """Parse string representation of list to actual list"""
            if isinstance(field_value, list):
                return field_value
            if isinstance(field_value, str):
                try:
                    return ast.literal_eval(field_value)
                except:
                    return [field_value]
            return []
        
        # Extract multi-valued fields
        art_interests = parse_list_field(user.get('art_interests', user.get('interests', [])))
        genres = parse_list_field(user.get('genres', []))
        moods = parse_list_field(user.get('moods', []))
        
        language = user.get('language', 'sinhala')
        
        users_list.append({
            'name': user['name'],
            'city': user['city'],
            'art_interests': art_interests,  # NEW: Multiple art form interests
            'genres': genres,                 # NEW: Multiple genre preferences
            'interests': art_interests,       # Keep for backward compatibility
            'moods': moods,
            'follows': followed_artist_names,
            'language': language,
            'user_id': user_id
        })
    
    return sorted(users_list, key=lambda x: x['name'])


def load_artists_df():
    """Load artists as DataFrame (REAL ARTISTS)"""
    _, artists, _, _, _ = load_dataset()
    
    if isinstance(artists, pd.DataFrame):
        return artists
    
    artists_list = []
    for artist in artists:
        artists_list.append({
            'artist_id': artist.get('artist_id'),
            'name': artist.get('name'),
            'art_form': artist.get('art_form', 'music'),
            'city': artist.get('city'),
            'follower_count': artist.get('follower_count', 0),
            'verified': artist.get('verified', False),
            'era': artist.get('era', 'contemporary'),
            'popularity': artist.get('popularity', 'mid_tier')
        })
    
    return pd.DataFrame(artists_list)


def load_events_df():
    """Load events as DataFrame (REAL EVENTS)"""
    _, _, events, _, _ = load_dataset()
    
    if isinstance(events, pd.DataFrame):
        return events
    
    events_list = []
    for event in events:
        events_list.append({
            'event_id': event.get('event_id'),
            'name': event.get('name'),
            'date': event.get('date', ''),
            'time': event.get('time', ''),
            'city': event.get('city'),
            'venue': event.get('venue', 'TBA'),
            'ticket_price': event.get('ticket_price', 0),
            'capacity': event.get('capacity', 0)
        })
    
    return pd.DataFrame(events_list)


def load_follows_df():
    """Load follows relationships as DataFrame"""
    _, _, _, follows, _ = load_dataset()
    return pd.DataFrame(follows)


def load_attends_df():
    """Load event attendance as DataFrame"""
    _, _, _, _, attends = load_dataset()
    return pd.DataFrame(attends)


def get_user_by_name(name):
    """Get user object by name"""
    users_list = load_users_list()
    for user in users_list:
        if user['name'] == name:
            return user
    return None


def get_artist_by_id(artist_id):
    """Get artist object by ID (REAL ARTISTS)"""
    _, artists, _, _, _ = load_dataset()
    for artist in artists:
        artist_id_val = artist.get('artist_id') if isinstance(artist, dict) else artist['artist_id']
        if str(artist_id_val) == str(artist_id):
            return artist
    return None


def get_event_by_id(event_id):
    """Get event object by ID (REAL EVENTS)"""
    _, _, events, _, _ = load_dataset()
    for event in events:
        event_id_val = event.get('event_id') if isinstance(event, dict) else event['event_id']
        if str(event_id_val) == str(event_id):
            return event
    return None
