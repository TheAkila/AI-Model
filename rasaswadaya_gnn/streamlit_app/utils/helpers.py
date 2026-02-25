"""
Helper functions for data formatting and processing
"""
import pandas as pd


def format_artist(artist_data):
    """Format artist data for display"""
    return {
        'id': artist_data.get('id', ''),
        'name': artist_data.get('name', 'Unknown Artist'),
        'art_forms': artist_data.get('art_forms', []),
        'genre': artist_data.get('genre', 'Miscellaneous'),
        'mood': artist_data.get('mood', 'Diverse'),
        'score': float(artist_data.get('score', 0.5)),
        'city': artist_data.get('city', 'Unknown')
    }


def format_event(event_data):
    """Format event data for display"""
    return {
        'id': event_data.get('id', ''),
        'name': event_data.get('name', 'Unknown Event'),
        'date': event_data.get('date', 'TBD'),
        'city': event_data.get('city', 'Unknown'),
        'genre': event_data.get('genre', 'Miscellaneous'),
        'distance': float(event_data.get('distance', 0)),
        'num_artists': int(event_data.get('num_artists', 0)),
        'score': float(event_data.get('score', 0.5))
    }


def format_trending_artist(artist_data):
    """Format trending artist data"""
    return {
        'id': artist_data.get('id', ''),
        'name': artist_data.get('name', 'Unknown Artist'),
        'follows': int(artist_data.get('follows', 0)),
        'genre': artist_data.get('genre', 'Miscellaneous')
    }


def format_trending_event(event_data):
    """Format trending event data"""
    return {
        'id': event_data.get('id', ''),
        'name': event_data.get('name', 'Unknown Event'),
        'attendees': int(event_data.get('attendees', 0)),
        'date': event_data.get('date', 'TBD')
    }


def get_star_rating(score):
    """Convert score to star rating (0-5)"""
    rating = int(score * 5)
    return '⭐' * rating + '☆' * (5 - rating)


def format_distance(km):
    """Format distance for display"""
    if km < 1:
        return "Same City"
    elif km < 50:
        return f"{km:.1f} km (Nearby)"
    elif km < 150:
        return f"{km:.1f} km (Moderate)"
    else:
        return f"{km:.1f} km (Far)"


def convert_dataframe_to_list(df, columns=None):
    """Convert pandas DataFrame to list of dicts"""
    if columns:
        df = df[columns]
    return df.to_dict('records')


def filter_dataframe(df, column, value):
    """Filter DataFrame by column value"""
    return df[df[column] == value]


def sort_dataframe(df, column, ascending=False):
    """Sort DataFrame by column"""
    return df.sort_values(by=column, ascending=ascending)


def truncate_text(text, max_length=50):
    """Truncate text to max length"""
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text
