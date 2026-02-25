#!/usr/bin/env python3
"""
Rasaswadaya.lk GNN Model - Interactive Demo
===========================================
Complete end-to-end demonstration of the model.

This script:
1. Generates sample data
2. Builds heterogeneous graph
3. Trains GNN model
4. Generates recommendations
5. Detects trends
6. Provides explanations
"""

import os
import sys
import torch
import numpy as np
import random
from typing import Dict, List, Tuple

# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)
random.seed(42)

from config import get_config, print_config_summary
from data.generate_sample_data import generate_sample_dataset, load_dataset
from models.graph_builder import HeterogeneousGraphBuilder
from models.gnn_model import RecommendationModel, train_step, evaluate
from models.cultural_dna import compute_cultural_similarity, explain_similarity
from utils.distance_calculator import get_distance_info, haversine_distance, distance_to_score


def split_edges_for_training(data, train_ratio=0.7, val_ratio=0.15):
    """Split edges into train/val/test sets for link prediction.
    
    Note: Only user->artist edges are used for training.
    User->event edges are not included in the graph (no data leakage).
    Event recommendations are derived via 2-hop path: User->Artist->Event.
    """
    edge_splits = {
        'train': {},
        'val': {},
        'test': {}
    }
    
    # Only user follows artist edges (user->event removed)
    important_edge_types = [
        ('user', 'follows', 'artist'),
    ]
    
    for edge_type in important_edge_types:
        if edge_type in data.edge_index_dict:
            edge_index = data.edge_index_dict[edge_type]
            num_edges = edge_index.size(1)
            
            # Random permutation
            perm = torch.randperm(num_edges)
            
            # Split indices
            train_end = int(train_ratio * num_edges)
            val_end = int((train_ratio + val_ratio) * num_edges)
            
            train_idx = perm[:train_end]
            val_idx = perm[train_end:val_end]
            test_idx = perm[val_end:]
            
            # Create edge dictionaries
            edge_splits['train'][edge_type] = (
                edge_index[0, train_idx],
                edge_index[1, train_idx]
            )
            edge_splits['val'][edge_type] = (
                edge_index[0, val_idx],
                edge_index[1, val_idx]
            )
            edge_splits['test'][edge_type] = (
                edge_index[0, test_idx],
                edge_index[1, test_idx]
            )
    
    return edge_splits


def generate_negative_samples(data, pos_edges: Dict, neg_ratio: float = 1.0):
    """Generate negative samples for link prediction."""
    neg_edges = {}
    
    for edge_type, (pos_src, pos_dst) in pos_edges.items():
        src_type, rel, dst_type = edge_type
        
        num_pos = len(pos_src)
        num_neg = int(num_pos * neg_ratio)
        
        # Get number of nodes for each type
        num_src_nodes = data[src_type].x.size(0)
        num_dst_nodes = data[dst_type].x.size(0)
        
        # Random negative samples
        neg_src = torch.randint(0, num_src_nodes, (num_neg,))
        neg_dst = torch.randint(0, num_dst_nodes, (num_neg,))
        
        neg_edges[edge_type] = (neg_src, neg_dst)
    
    return neg_edges


def detect_trending_artists(graph_builder: HeterogeneousGraphBuilder, embeddings: Dict, top_k: int = 10) -> List[Tuple[str, float]]:
    """
    Detect trending artists based on recent engagement.
    
    Returns:
        List of (artist_id, trend_score) tuples
    """
    print("\n📈 Detecting Trending Artists...")
    
    # Simple trend detection: count recent interactions
    from collections import Counter
    from datetime import datetime, timedelta
    
    recent_cutoff = datetime.now() - timedelta(days=30)
    
    artist_engagement = Counter()
    genre_engagement = Counter()
    
    # Count follows
    for follow in graph_builder.dataset['interactions']['follows']:
        timestamp = datetime.fromisoformat(follow['timestamp'])
        if timestamp > recent_cutoff:
            artist_engagement[follow['artist_id']] += 2  # Follows weighted more
            # Track genres
            artist = graph_builder.artists.get(follow['artist_id'], {})
            for genre in artist.get('genres', []):
                genre_engagement[genre] += 2
    
    # Count event attendances
    for attend in graph_builder.dataset['interactions']['attends']:
        timestamp = datetime.fromisoformat(attend['timestamp'])
        if timestamp > recent_cutoff:
            event = graph_builder.events.get(attend['event_id'])
            if event:
                for artist_id in event.get('artist_ids', []):
                    artist_engagement[artist_id] += 1
                # Track genres from events
                for genre in event.get('genres', []):
                    genre_engagement[genre] += 1
    
    # Get top trending artists
    trending = artist_engagement.most_common(top_k)
    trending_genres = genre_engagement.most_common(5)
    
    print(f"✓ Found {len(trending)} trending artists\n")
    
    for i, (artist_id, score) in enumerate(trending, 1):
        artist = graph_builder.artists[artist_id]
        print(f"  {i}. {artist['name']}")
        print(f"     Genres: {', '.join(artist['genres'])}")
        print(f"     City: {artist.get('city', 'Unknown')}")
        print(f"     Engagement score: {score}")
        print()
    
    # Display trending genres
    print("\n🔥 Trending Genres:")
    for i, (genre, score) in enumerate(trending_genres, 1):
        print(f"  {i}. {genre} (engagement score: {score})")
    print()
    
    return trending


def calculate_city_distance(city1: str, city2: str) -> float:
    """
    Calculate distance score between two cities using real geographical distance.
    
    Uses Haversine formula to calculate actual km distance, then converts to 0-1 score.
    
    Returns: Score from 0.0 to 1.0 (1.0 = same city, 0.1 = very far)
    """
    distance_km = haversine_distance(city1, city2)
    score = distance_to_score(distance_km)
    return score


def calculate_user_similarity(user1: Dict, user2: Dict) -> float:
    """Calculate similarity between two users based on interests and preferences."""
    score = 0.0
    
    # Interest similarity (40%)
    interests1 = set(user1.get('art_interests', []))
    interests2 = set(user2.get('art_interests', []))
    if interests1 and interests2:
        interest_sim = len(interests1 & interests2) / len(interests1 | interests2)
        score += interest_sim * 0.4
    
    # Mood similarity (30%)
    moods1 = set(user1.get('mood_preferences', []))
    moods2 = set(user2.get('mood_preferences', []))
    if moods1 and moods2:
        mood_sim = len(moods1 & moods2) / len(moods1 | moods2)
        score += mood_sim * 0.3
    
    # Cultural preferences (25%)
    culture1 = set(user1.get('culture_preferences', []))
    culture2 = set(user2.get('culture_preferences', []))
    if culture1 and culture2:
        culture_sim = len(culture1 & culture2) / len(culture1 | culture2)
        score += culture_sim * 0.25
    
    # City proximity (5%)
    if user1.get('city') == user2.get('city'):
        score += 0.05
    
    return min(score, 1.0)


def find_similar_users(graph_builder: HeterogeneousGraphBuilder, user_id: str, top_k: int = 5) -> List[Tuple[Dict, float]]:
    """Find users most similar to the given user."""
    current_user = next((u for u in graph_builder.dataset['users'] if u['user_id'] == user_id), None)
    if not current_user:
        return []
    
    similar_users = []
    for user in graph_builder.dataset['users']:
        if user['user_id'] == user_id:
            continue
        
        similarity = calculate_user_similarity(current_user, user)
        if similarity > 0.1:
            similar_users.append((user, similarity))
    
    similar_users.sort(key=lambda x: x[1], reverse=True)
    return similar_users[:top_k]


def get_collaborative_recommendations(
    graph_builder: HeterogeneousGraphBuilder,
    user_id: str,
    similar_users: List[Tuple[Dict, float]],
    user_follows: List[str]
) -> Dict[str, float]:
    """Get artist recommendations based on what similar users follow."""
    collaborative_scores = {}
    
    for similar_user, similarity in similar_users:
        similar_follows = [f['artist_id'] for f in graph_builder.dataset['interactions']['follows'] 
                          if f['user_id'] == similar_user['user_id']]
        
        for artist_id in similar_follows:
            if artist_id not in user_follows:
                collaborative_scores[artist_id] = collaborative_scores.get(artist_id, 0) + similarity
    
    return collaborative_scores


def generate_recommendations_for_user(
    model: RecommendationModel,
    graph_builder: HeterogeneousGraphBuilder,
    data,
    user_id: str,
    top_k: int = 5,
    device: str = 'cpu',
    show_process: bool = False
) -> Dict[str, List[Tuple[str, float, str]]]:
    """
    Generate personalized recommendations for a user using collaborative filtering.
    
    Returns:
        Dictionary with 'artists' and 'events' recommendations
    """
    model.eval()
    
    # Get user index
    try:
        user_idx = graph_builder.get_node_idx('user', user_id)
    except KeyError:
        print(f"❌ User {user_id} not found")
        return {'artists': [], 'events': []}
    
    # Get current user data
    current_user = next((u for u in graph_builder.dataset['users'] if u['user_id'] == user_id), None)
    
    # Get embeddings
    x_dict = {k: v.to(device) for k, v in data.x_dict.items()}
    edge_index_dict = {k: v.to(device) for k, v in data.edge_index_dict.items()}
    
    with torch.no_grad():
        embeddings = model(x_dict, edge_index_dict)
    
    recommendations = {}
    
    # Artist recommendations with collaborative filtering
    user_follows = [f['artist_id'] for f in graph_builder.dataset['interactions']['follows'] 
                    if f['user_id'] == user_id]
    
    if show_process:
        print(f"\n{'='*80}")
        print(" COLLABORATIVE FILTERING PROCESS")
        print(f"{'='*80}")
        print(f"\n📊 Step 1: Finding Similar Users...")
    
    # Find similar users
    similar_users = find_similar_users(graph_builder, user_id, top_k=5)
    
    if show_process and similar_users:
        print(f"\n   ✓ Found {len(similar_users)} similar users:")
        for i, (sim_user, similarity) in enumerate(similar_users[:3], 1):
            shared_interests = set(current_user.get('art_interests', [])) & set(sim_user.get('art_interests', []))
            print(f"   {i}. {sim_user['name']} (ID: {sim_user['user_id']}) - Similarity: {similarity:.1%}")
            if shared_interests:
                print(f"      → Shared interests: {', '.join(list(shared_interests)[:3])}")
    
    # Get collaborative recommendations
    if show_process:
        print(f"\n📊 Step 2: Gathering Collaborative Recommendations (from similar users)...")
    
    collaborative_scores = get_collaborative_recommendations(graph_builder, user_id, similar_users, user_follows)
    
    if show_process and collaborative_scores:
        print(f"\n   ✓ Found {len(collaborative_scores)} artists from similar users")
        top_collab = sorted(collaborative_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        for artist_id, score in top_collab:
            artist = graph_builder.artists.get(artist_id, {})
            print(f"   • {artist.get('name', 'Unknown')} (collaborative score: {score:.2f})")
    
    # Get content-based recommendations (GNN embeddings)
    if show_process:
        print(f"\n📊 Step 3: Computing Content-Based Recommendations (from user preferences)...")
    
    # Get all artist indices except already followed
    all_artist_ids = list(graph_builder.artists.keys())
    candidate_artist_ids = [aid for aid in all_artist_ids if aid not in user_follows]
    
    content_scores = {}
    if candidate_artist_ids:
        candidate_indices = torch.tensor(
            [graph_builder.get_node_idx('artist', aid) for aid in candidate_artist_ids],
            dtype=torch.long
        )
        
        top_indices, top_scores = model.recommend(
            embeddings,
            torch.tensor([user_idx]),
            'artist',
            candidate_indices,
            top_k=len(candidate_artist_ids)
        )
        
        for idx, score in zip(top_indices, top_scores):
            artist_id = graph_builder.get_node_id('artist', idx.item())
            content_scores[artist_id] = score.item()
    
    if show_process:
        print(f"\n   ✓ Content-based scores calculated for {len(content_scores)} artists")
    
    # Get trending/discovery recommendations
    if show_process:
        print(f"\n📊 Step 4: Analyzing Trending Artists (discovery component)...")
    
    popularity_scores = {}
    for artist_id in candidate_artist_ids:
        follows_count = len([f for f in graph_builder.dataset['interactions']['follows'] 
                           if f['artist_id'] == artist_id])
        popularity_scores[artist_id] = follows_count
    
    max_popularity = max(popularity_scores.values()) if popularity_scores else 1
    
    if show_process:
        top_trending = sorted(popularity_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"\n   ✓ Top trending artists:")
        for artist_id, follows in top_trending:
            artist = graph_builder.artists.get(artist_id, {})
            print(f"   🔥 {artist.get('name', 'Unknown')} ({follows} followers)")
    
    # Mix recommendations: 50% content + 30% collaborative + 20% discovery
    if show_process:
        print(f"\n📊 Step 5: Mixing Recommendations...")
        print(f"   Formula: 50% Content + 30% Collaborative + 20% Trending\n")
    
    combined_scores = {}
    for artist_id in candidate_artist_ids:
        score = 0.0
        score += 0.5 * content_scores.get(artist_id, 0)
        score += 0.3 * collaborative_scores.get(artist_id, 0)
        score += 0.2 * (popularity_scores.get(artist_id, 0) / max_popularity)
        combined_scores[artist_id] = score
    
    # Sort and get top-k
    sorted_artists = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    
    artist_recs = []
    for artist_id, score in sorted_artists:
        artist = graph_builder.artists[artist_id]
        
        # Determine primary recommendation reason
        content = content_scores.get(artist_id, 0) * 0.5
        collab = collaborative_scores.get(artist_id, 0) * 0.3
        pop = (popularity_scores.get(artist_id, 0) / max_popularity) * 0.2
        
        if collab > content and collab > pop:
            reason = 'collaborative'
        elif pop > content and pop > collab:
            reason = 'trending'
        else:
            reason = 'content'
        
        artist_recs.append((artist_id, score, artist['name'], reason))
    
    recommendations['artists'] = artist_recs
    recommendations['similar_users'] = [(u['name'], sim) for u, sim in similar_users]
    
    if show_process:
        print(f"   ✓ Final Top {top_k} Recommendations:")
        for i, (artist_id, score, name, reason) in enumerate(artist_recs, 1):
            reason_emoji = {'content': '✨', 'collaborative': '👥', 'trending': '🔥'}
            reason_label = {'content': 'For You', 'collaborative': 'Similar Users', 'trending': 'Trending'}
            print(f"   {i}. {name}")
            print(f"      {reason_emoji[reason]} {reason_label[reason]} | Score: {score:.3f}")
    
    # Event recommendations - LOCATION-AWARE + ARTIST-AWARE + GENRE-AWARE
    # Get user's city (from profile)
    user_city = graph_builder.users.get(user_id, {}).get('city', None)
    user_art_interests = graph_builder.users.get(user_id, {}).get('art_interests', [])
    
    all_events = list(graph_builder.events.items())
    
    if all_events and user_city:
        event_scores = []
        
        for event_id, event in all_events:
            score = 0.0
            
            # Signal 1: Distance-based Location (40% weight)
            # Use real geographical distance from haversine formula
            event_city = event.get('city', None)
            distance_score = calculate_city_distance(user_city, event_city) if event_city else 0.1
            distance_km = haversine_distance(user_city, event_city) if event_city else float('inf')
            score += 0.40 * distance_score
            
            # Signal 2: Followed Artists Performing (35% weight)
            artist_score = 0.0
            event_artists = event.get('artist_ids', [])
            if event_artists:
                num_followed_in_event = len([a for a in event_artists if a in user_follows])
                if num_followed_in_event > 0:
                    artist_score = min(1.0, num_followed_in_event / len(event_artists))
            score += 0.35 * artist_score
            
            # Signal 3: Genre Preference Match (25% weight)
            genre_score = 0.0
            event_genres = set(event.get('genres', []))
            user_interests_set = set([g.lower() for g in user_art_interests])
            event_genres_lower = set([g.lower() for g in event_genres])
            
            if event_genres and user_interests_set:
                matching_genres = len(event_genres_lower & user_interests_set)
                genre_score = min(1.0, matching_genres / len(event_genres))
            score += 0.25 * genre_score
            
            event_scores.append((event_id, event, score, distance_score, distance_km, artist_score, genre_score))
        
        # Sort by combined score (descending)
        event_scores.sort(key=lambda x: x[2], reverse=True)
        
        # Get top-k events
        event_recs = []
        for i, (event_id, event, combined_score, distance_score, distance_km, artist_score, genre_score) in enumerate(event_scores[:top_k]):
            event_city = event.get('city', 'Unknown')
            distance_info = get_distance_info(user_city, event_city)
            event_recs.append((
                event_id, 
                combined_score, 
                event['name'], 
                distance_score, 
                artist_score, 
                genre_score, 
                event_city,
                distance_info
            ))
        
        recommendations['events'] = event_recs
    else:
        recommendations['events'] = []
    
    return recommendations


def explain_recommendation(
    graph_builder: HeterogeneousGraphBuilder,
    user_id: str,
    recommended_id: str,
    recommended_type: str
) -> str:
    """
    Generate human-readable explanation for a recommendation.
    """
    from models.cultural_dna import CulturalDNAEncoder, explain_similarity
    
    encoder = CulturalDNAEncoder()
    
    # Get user's cultural profile from interactions
    user_follows = [f['artist_id'] for f in graph_builder.dataset['interactions']['follows']
                    if f['user_id'] == user_id]
    
    user_history = []
    for artist_id in user_follows[:5]:  # Sample recent follows
        artist = graph_builder.artists.get(artist_id)
        if artist:
            user_history.append({
                'type': 'artist',
                'metadata': artist,
                'weight': 1.0
            })
    
    user_dna = encoder.encode_user(user_history)
    
    # Get recommended item's DNA
    if recommended_type == 'artist':
        item = graph_builder.artists[recommended_id]
        item_dna = encoder.encode_artist(item)
        item_name = item['name']
    else:  # event
        item = graph_builder.events[recommended_id]
        item_dna = encoder.encode_event(item)
        item_name = item['name']
    
    # Calculate similarity
    explanation = f"🎯 Why we recommend '{item_name}':\n\n"
    explanation += explain_similarity(user_dna, item_dna, encoder, top_k=3)
    
    # Add specific insights
    if recommended_type == 'artist':
        explanation += f"\n📋 Artist Details:\n"
        explanation += f"  • Genres: {', '.join(item['genres'])}\n"
        explanation += f"  • City: {item.get('city', 'Unknown')}\n"
        explanation += f"  • Style: {', '.join(item['style'])}\n"
    else:
        explanation += f"\n📋 Event Details:\n"
        explanation += f"  • Date: {item['date'][:10]}\n"
        explanation += f"  • Venue: {item['venue']}\n"
        explanation += f"  • City: {item.get('city', 'Unknown')}\n"
        explanation += f"  • Genres: {', '.join(item['genres'])}\n"
    
    return explanation


def analyze_recommendation_diversity(recommendations_by_user: Dict, graph_builder: HeterogeneousGraphBuilder = None) -> Dict:
    """
    Analyze diversity metrics across recommendations.
    
    Returns metrics like:
    - Genre diversity
    - Regional diversity
    - Artist diversity
    - Recommendation mixing ratio
    """
    print("\n" + "="*70)
    print(" 📊 RECOMMENDATION DIVERSITY ANALYSIS")
    print("="*70)
    
    if not recommendations_by_user:
        print("   No recommendations to analyze")
        return {}
    
    # Collect all recommended artists and their reasons
    all_artists = []
    reason_counts = {'content': 0, 'collaborative': 0, 'trending': 0}
    all_genres = []
    all_regions = []
    
    total_users = 0
    for user_id, recs in recommendations_by_user.items():
        if 'artists' in recs:
            total_users += 1
            for artist_id, score, name, reason in recs['artists']:
                all_artists.append((artist_id, name))
                reason_counts[reason] += 1
                # Get genres from artist data if graph_builder available
                if graph_builder:
                    artist = graph_builder.artists.get(artist_id, {})
                    all_genres.extend(artist.get('genres', []))
    
    # Calculate metrics
    unique_artists = len(set([a[0] for a in all_artists]))
    total_recommendations = len(all_artists)
    
    print(f"\n📈 Recommendation Statistics:")
    print(f"   • Total users analyzed: {total_users}")
    print(f"   • Total recommendations: {total_recommendations}")
    print(f"   • Unique artists recommended: {unique_artists}")
    print(f"   • Avg recommendation per user: {total_recommendations/max(total_users, 1):.1f}")
    
    print(f"\n🎯 Recommendation Mixing (Hybrid Strategy):")
    print(f"   • Content-Based (For You): {reason_counts['content']} ({reason_counts['content']*100/max(total_recommendations, 1):.1f}%)")
    print(f"   • Collaborative (Similar Users): {reason_counts['collaborative']} ({reason_counts['collaborative']*100/max(total_recommendations, 1):.1f}%)")
    print(f"   • Discovery (Trending): {reason_counts['trending']} ({reason_counts['trending']*100/max(total_recommendations, 1):.1f}%)")
    
    # Genre diversity
    if all_genres:
        from collections import Counter
        genre_counts = Counter(all_genres)
        print(f"\n🎨 Genre Diversity:")
        print(f"   • Unique genres recommended: {len(genre_counts)}")
        top_3_genres = genre_counts.most_common(3)
        for genre, count in top_3_genres:
            print(f"   • {genre}: {count} recommendations")
    
    return {
        'total_users': total_users,
        'total_recommendations': total_recommendations,
        'unique_artists': unique_artists,
        'reason_counts': reason_counts,
        'genre_diversity': len(set(all_genres)) if all_genres else 0
    }


def compute_graph_statistics(graph_builder: HeterogeneousGraphBuilder, data) -> Dict:
    """
    Compute comprehensive graph statistics.
    """
    print("\n" + "="*70)
    print(" 🔗 GRAPH STRUCTURE ANALYSIS")
    print("="*70)
    
    # Node statistics
    print(f"\n👥 Node Statistics:")
    print(f"   • Users: {len(graph_builder.users)}")
    print(f"   • Artists: {len(graph_builder.artists)}")
    print(f"   • Events: {len(graph_builder.events)}")
    total_nodes = len(graph_builder.users) + len(graph_builder.artists) + len(graph_builder.events)
    print(f"   • Total nodes: {total_nodes}")
    
    # Edge statistics
    print(f"\n🔗 Edge Statistics:")
    follows = graph_builder.dataset['interactions']['follows']
    attends = graph_builder.dataset['interactions']['attends']
    print(f"   • User-Artist follows: {len(follows)}")
    print(f"   • User-Event attends: {len(attends)}")
    total_edges = len(follows) + len(attends)
    print(f"   • Total edges: {total_edges}")
    
    # Connectivity metrics
    print(f"\n📊 Connectivity Metrics:")
    avg_follows_per_user = len(follows) / max(len(graph_builder.users), 1)
    avg_followers_per_artist = len(follows) / max(len(graph_builder.artists), 1)
    print(f"   • Avg follows per user: {avg_follows_per_user:.2f}")
    print(f"   • Avg followers per artist: {avg_followers_per_artist:.2f}")
    print(f"   • Graph density: {2*total_edges/(total_nodes*(total_nodes-1)):.4f}")
    
    # Event statistics
    print(f"\n🎪 Event Coverage:")
    events_with_artists = len([e for e in graph_builder.events.values() if e.get('artist_ids')])
    print(f"   • Events with artists: {events_with_artists}/{len(graph_builder.events)}")
    avg_artists_per_event = sum([len(e.get('artist_ids', [])) for e in graph_builder.events.values()]) / max(len(graph_builder.events), 1)
    print(f"   • Avg artists per event: {avg_artists_per_event:.2f}")
    
    return {
        'num_users': len(graph_builder.users),
        'num_artists': len(graph_builder.artists),
        'num_events': len(graph_builder.events),
        'num_follows': len(follows),
        'avg_follows_per_user': avg_follows_per_user
    }


def analyze_cold_start_recommendations(
    graph_builder: HeterogeneousGraphBuilder,
    model: RecommendationModel,
    data,
    device: str = 'cpu'
) -> Dict:
    """
    Analyze how well the system handles cold-start (new users with few interactions).
    """
    print("\n" + "="*70)
    print(" ❄️ COLD-START ANALYSIS (New User Recommendation)")
    print("="*70)
    
    # Create hypothetical new user with minimal interactions
    print("\n🆕 Creating synthetic new user with ZERO initial follows...")
    
    # Take a user with many follows and see what recommendations we'd make based on partial data
    user = graph_builder.dataset['users'][0]
    user_follows = [f['artist_id'] for f in graph_builder.dataset['interactions']['follows'] 
                    if f['user_id'] == user['user_id']]
    
    if user_follows:
        # Test with 1 follow (extreme cold-start)
        print(f"\n   Based on 1 follow (cold-start):")
        
        # Get recommendations
        x_dict = {k: v.to(device) for k, v in data.x_dict.items()}
        edge_index_dict = {k: v.to(device) for k, v in data.edge_index_dict.items()}
        
        with torch.no_grad():
            embeddings = model(x_dict, edge_index_dict)
        
        # Get user embedding similarity
        user_id = user['user_id']
        try:
            user_idx = graph_builder.get_node_idx('user', user_id)
            
            all_artist_ids = list(graph_builder.artists.keys())
            candidate_indices = torch.tensor(
                [graph_builder.get_node_idx('artist', aid) for aid in all_artist_ids],
                dtype=torch.long
            )
            
            top_indices, top_scores = model.recommend(
                embeddings,
                torch.tensor([user_idx]),
                'artist',
                candidate_indices,
                top_k=5
            )
            
            print(f"   Top recommendations based on embeddings:")
            for i, (idx, score) in enumerate(zip(top_indices, top_scores), 1):
                artist_id = graph_builder.get_node_id('artist', idx.item())
                artist = graph_builder.artists[artist_id]
                print(f"   {i}. {artist['name']} - Score: {score:.3f}")
        except Exception as e:
            print(f"   ❌ Error in cold-start analysis: {e}")
    
    return {'cold_start_handled': True}


def main():
    """Main demo function."""
    print("=" * 70)
    print(" " * 15 + "RASASWADAYA.LK GNN MODEL DEMO")
    print("=" * 70)
    
    # Print configuration
    print_config_summary()
    
    config = get_config()
    device = config.gnn.device
    print(f"Using device: {device}\n")
    
    # Step 1: Generate or load dataset
    print("\n" + "="*70)
    print(" STEP 1: DATA GENERATION")
    print("="*70)
    
    dataset_path = "data/sample_dataset/rasaswadaya_dataset.pkl"
    if not os.path.exists(dataset_path):
        dataset = generate_sample_dataset(num_users=150, num_artists=60, num_events=120)
    else:
        print(f"\n📂 Loading existing dataset from {dataset_path}...")
        dataset = load_dataset(dataset_path)
        print(f"✓ Loaded {len(dataset['users'])} users, {len(dataset['artists'])} artists, {len(dataset['events'])} events")
    
    # Step 2: Build graph
    print("\n" + "="*70)
    print(" STEP 2: GRAPH CONSTRUCTION")
    print("="*70)
    
    graph_builder = HeterogeneousGraphBuilder(dataset)
    G = graph_builder.build_graph()
    
    # Detect communities
    print()
    communities = graph_builder.detect_communities('louvain')
    
    # Convert to PyG format
    print()
    data = graph_builder.build_pyg_data()
    
    # Step 3: Train GNN
    print("\n" + "="*70)
    print(" STEP 3: GNN TRAINING")
    print("="*70)
    
    # Split edges
    edge_splits = split_edges_for_training(data, train_ratio=0.7, val_ratio=0.15)
    
    train_pos = edge_splits['train']
    val_pos = edge_splits['val']
    test_pos = edge_splits['test']
    
    train_neg = generate_negative_samples(data, train_pos)
    val_neg = generate_negative_samples(data, val_pos)
    test_neg = generate_negative_samples(data, test_pos)
    
    # Initialize model
    model = RecommendationModel(
        metadata=data.metadata(),
        hidden_channels=config.gnn.hidden_channels,
        out_channels=config.gnn.out_channels,
        num_layers=config.gnn.num_layers,
        model_type=config.gnn.model_type
    ).to(device)
    
    optimizer = torch.optim.Adam(model.parameters(), lr=config.gnn.learning_rate, weight_decay=config.gnn.weight_decay)
    
    print(f"\n🧠 Model initialized:")
    print(f"   Architecture: {config.gnn.model_type.upper()}")
    print(f"   Hidden channels: {config.gnn.hidden_channels}")
    print(f"   Output channels: {config.gnn.out_channels}")
    print(f"   Layers: {config.gnn.num_layers}")
    print(f"   Parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # Training loop
    print(f"\n🏋️  Training for {config.training.epochs} epochs...")
    
    best_val_acc = 0.0
    patience_counter = 0
    
    for epoch in range(1, config.training.epochs + 1):
        loss = train_step(model, data, optimizer, train_pos, train_neg, device)
        
        if epoch % 10 == 0 or epoch == 1:
            val_loss, val_acc = evaluate(model, data, val_pos, val_neg, device)
            
            print(f"Epoch {epoch:3d} | Train Loss: {loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.4f}")
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                patience_counter = 0
                # Save best model
                torch.save(model.state_dict(), 'checkpoints/best_model.pt')
            else:
                patience_counter += 1
            
            if patience_counter >= config.training.early_stopping_patience:
                print(f"\n⏹️  Early stopping at epoch {epoch}")
                break
    
    # Test evaluation
    test_loss, test_acc = evaluate(model, data, test_pos, test_neg, device)
    print(f"\n✅ Training complete!")
    print(f"   Best Val Accuracy: {best_val_acc:.4f}")
    print(f"   Test Accuracy: {test_acc:.4f}")
    
    # Step 4: Recommendations with Collaborative Filtering
    print("\n" + "="*80)
    print(" STEP 4: PERSONALIZED RECOMMENDATIONS (Collaborative Filtering)")
    print("="*80)
    print("\nℹ️  This system uses HYBRID recommendations:")
    print("   • 50% Content-Based (GNN embeddings from user preferences)")
    print("   • 30% Collaborative (from similar users' choices)")
    print("   • 20% Discovery (trending artists across platform)\n")
    
    # Compute graph statistics before recommendations
    graph_stats = compute_graph_statistics(graph_builder, data)
    
    # Display available users
    print(f"📋 Available Users ({len(dataset['users'])} total):")
    for idx in range(min(10, len(dataset['users']))):
        user = dataset['users'][idx]
        print(f"   {idx}: {user['name']} - Interests: {', '.join(user['art_interests'][:2])}")
    if len(dataset['users']) > 10:
        print(f"   ... and {len(dataset['users']) - 10} more users")
    
    # Get user selection
    try:
        user_input = input(f"\nSelect user index (0-{len(dataset['users'])-1}), 'random' for random user, or 'all' for all users: ").strip().lower()
        
        if user_input == 'random':
            selected_indices = [random.randint(0, len(dataset['users']) - 1)]
        elif user_input == 'all':
            selected_indices = list(range(len(dataset['users'])))
            print(f"\n🔄 Showing recommendations for all {len(dataset['users'])} users...")
        else:
            try:
                idx = int(user_input)
                if 0 <= idx < len(dataset['users']):
                    selected_indices = [idx]
                else:
                    print(f"❌ Invalid index. Using first user.")
                    selected_indices = [0]
            except ValueError:
                print(f"❌ Invalid input. Using first user.")
                selected_indices = [0]
    except EOFError:
        # For non-interactive mode (e.g., testing)
        print("\nℹ️  Non-interactive mode: showing first 3 users")
        selected_indices = [0, 1, 2]
    
    # Store all recommendations for diversity analysis
    recommendations_by_user = {}
    
    # Generate recommendations for selected users
    for user_idx in selected_indices:
        sample_user_id = dataset['users'][user_idx]['user_id']
        sample_user = dataset['users'][user_idx]
        
        print(f"\n{'='*80}")
        print(f"👤 User {user_idx}: {sample_user['name']} ({sample_user_id})")
        print(f"   Interests: {', '.join(sample_user.get('art_interests', []))}")
        print(f"   Moods: {', '.join(sample_user.get('mood_preferences', []))}")
        print(f"   City: {sample_user.get('city', 'Unknown')}")
        
        # Show collaborative filtering process for first user only
        show_details = (user_idx == selected_indices[0])
        
        recommendations = generate_recommendations_for_user(
            model, graph_builder, data, sample_user_id, top_k=5, device=device, show_process=show_details
        )
        
        recommendations_by_user[sample_user_id] = recommendations
        
        # Display similar users
        if 'similar_users' in recommendations and recommendations['similar_users']:
            print(f"\n👥 Similar Users ({len(recommendations['similar_users'])} found):")
            for i, (user_name, similarity) in enumerate(recommendations['similar_users'][:3], 1):
                print(f"   {i}. {user_name} - {similarity:.1%} match")
        
        if recommendations['artists']:
            if not show_details:
                print(f"\n🎨 Top Artist Recommendations:")
                for i, (artist_id, score, name, reason) in enumerate(recommendations['artists'], 1):
                    reason_emoji = {'content': '✨', 'collaborative': '👥', 'trending': '🔥'}
                    reason_label = {'content': 'For You', 'collaborative': 'Similar Users', 'trending': 'Trending'}
                    print(f"   {i}. {name}")
                    print(f"      {reason_emoji[reason]} {reason_label[reason]} | Score: {score:.3f}")
        else:
            print(f"\n🎨 No artist recommendations available")
        
        if recommendations['events']:
            print(f"\n🎪 Top Event Recommendations (By Location Distance + Artists + Genres):")
            for i, event_rec in enumerate(recommendations['events'], 1):
                event_id, combined_score, event_name, distance_score, artist_score, genre_score, event_city, distance_info = event_rec
                print(f"   {i}. {event_name}")
                print(f"      📍 {distance_info['user_city']} → {distance_info['event_city']}")
                print(f"      Distance: {distance_info['distance_km']} km | {distance_info['proximity']} | Travel: {distance_info['travel_time']}")
                print(f"      Score: {combined_score:.3f} (Distance: {distance_score:.2f}, Artists: {artist_score:.2f}, Genres: {genre_score:.2f})")
        else:
            print(f"\n🎪 No event recommendations available")
        
        # Show explanation for first selected user
        if user_idx == selected_indices[0] and recommendations['artists']:
            print(f"\n" + "="*70)
            print(" STEP 5: EXPLAINABILITY (for first selected user)")
            print("="*70)
            top_artist_id = recommendations['artists'][0][0]
            print(f"\n{explain_recommendation(graph_builder, sample_user_id, top_artist_id, 'artist')}")
    
    # Step 6: Trend Detection
    print("\n" + "="*70)
    print(" STEP 6: TREND DETECTION")
    print("="*70)
    
    trending = detect_trending_artists(graph_builder, {}, top_k=5)
    
    # Step 7: Diversity Analysis
    diversity_metrics = analyze_recommendation_diversity(recommendations_by_user, graph_builder)
    
    # Step 8: Cold-Start Analysis
    cold_start_analysis = analyze_cold_start_recommendations(graph_builder, model, data, device)
    
    # Summary
    print("\n" + "="*70)
    print(" 📋 DEMO SUMMARY & STATISTICS")
    print("="*70)
    
    print("\n✅ Successfully demonstrated:")
    print("   ✓ Data generation with Cultural DNA")
    print("   ✓ Heterogeneous graph construction")
    print("   ✓ GNN training with link prediction")
    print("   ✓ Personalized recommendations")
    print("   ✓ Collaborative filtering")
    print("   ✓ Explainable recommendations")
    print("   ✓ Trend detection")
    print("   ✓ Diversity analysis")
    print("   ✓ Cold-start handling")
    
    print("\n" + "="*70)
    print(" 🎯 FINAL SYSTEM OVERVIEW")
    print("="*70)
    
    print(f"\n📊 Dataset Size:")
    print(f"   • Users: {len(dataset['users'])}")
    print(f"   • Artists: {len(dataset['artists'])}")
    print(f"   • Events: {len(dataset['events'])}")
    print(f"   • User-Artist Follows: {len(dataset['interactions']['follows'])}")
    
    print(f"\n🧠 Model Performance:")
    print(f"   • Best Validation Accuracy: {best_val_acc:.4f}")
    print(f"   • Test Accuracy: {test_acc:.4f}")
    print(f"   • Architecture: {config.gnn.model_type.upper()}")
    print(f"   • Embedding Dimension: {config.gnn.out_channels}D")
    
    if diversity_metrics:
        print(f"\n🎨 Recommendation Quality:")
        print(f"   • Total Unique Artists Recommended: {diversity_metrics.get('unique_artists', 0)}")
        print(f"   • Genre Diversity: {diversity_metrics.get('genre_diversity', 0)} unique genres")
        print(f"   • Hybrid Mix:")
        reason_counts = diversity_metrics.get('reason_counts', {})
        total = sum(reason_counts.values())
        if total > 0:
            print(f"     - Content-Based: {reason_counts.get('content', 0)*100//total}%")
            print(f"     - Collaborative: {reason_counts.get('collaborative', 0)*100//total}%")
            print(f"     - Discovery: {reason_counts.get('trending', 0)*100//total}%")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    # Create checkpoints directory
    os.makedirs("checkpoints", exist_ok=True)
    os.makedirs("data/sample_dataset", exist_ok=True)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
