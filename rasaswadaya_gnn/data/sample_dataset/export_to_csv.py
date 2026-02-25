#!/usr/bin/env python3
"""
Export Rasaswadaya Dataset to CSV Files
Converts the pickle dataset into separate CSV files for each entity type.
"""

import pickle
import pandas as pd
from pathlib import Path

def export_to_csv():
    """Export all dataset components to CSV files."""
    
    # Load the dataset
    dataset_path = Path(__file__).parent / 'rasaswadaya_dataset.pkl'
    print(f"Loading dataset from {dataset_path}...")
    
    with open(dataset_path, 'rb') as f:
        data = pickle.load(f)
    
    # Create output directory
    output_dir = Path(__file__).parent / 'csv_export'
    output_dir.mkdir(exist_ok=True)
    
    print(f"\nExporting to {output_dir}/")
    
    # Export Users
    users_df = pd.DataFrame(data['users'])
    users_file = output_dir / 'users.csv'
    users_df.to_csv(users_file, index=False, encoding='utf-8')
    print(f"✓ Exported {len(users_df):,} users to users.csv")
    
    # Export Artists
    artists_df = pd.DataFrame(data['artists'])
    artists_file = output_dir / 'artists.csv'
    artists_df.to_csv(artists_file, index=False, encoding='utf-8')
    print(f"✓ Exported {len(artists_df):,} artists to artists.csv")
    
    # Export Events
    events_df = pd.DataFrame(data['events'])
    events_file = output_dir / 'events.csv'
    events_df.to_csv(events_file, index=False, encoding='utf-8')
    print(f"✓ Exported {len(events_df):,} events to events.csv")
    
    # Export Follows
    follows_df = pd.DataFrame(data['interactions']['follows'])
    follows_file = output_dir / 'follows.csv'
    follows_df.to_csv(follows_file, index=False, encoding='utf-8')
    print(f"✓ Exported {len(follows_df):,} follow relationships to follows.csv")
    
    # Export Event Attendances
    attends_df = pd.DataFrame(data['interactions']['attends'])
    attends_file = output_dir / 'attends.csv'
    attends_df.to_csv(attends_file, index=False, encoding='utf-8')
    print(f"✓ Exported {len(attends_df):,} event attendances to attends.csv")
    
    # Summary
    total_rows = len(users_df) + len(artists_df) + len(events_df) + len(follows_df) + len(attends_df)
    print(f"\n{'='*60}")
    print(f"Export Complete! Total: {total_rows:,} rows")
    print(f"{'='*60}")
    print(f"\nFiles created in: {output_dir}/")
    print(f"  • users.csv      - {len(users_df):,} rows")
    print(f"  • artists.csv    - {len(artists_df):,} rows")
    print(f"  • events.csv     - {len(events_df):,} rows")
    print(f"  • follows.csv    - {len(follows_df):,} rows")
    print(f"  • attends.csv    - {len(attends_df):,} rows")
    
    # Calculate file sizes
    total_size = sum(f.stat().st_size for f in output_dir.glob('*.csv'))
    print(f"\nTotal CSV size: {total_size / (1024*1024):.1f} MB")

if __name__ == '__main__':
    export_to_csv()
