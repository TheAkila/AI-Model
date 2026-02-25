"""
Graph Neural Network Visualization
Visualizes the heterogeneous graph structure for the recommendation system
"""

import plotly.graph_objects as go
import numpy as np
from typing import Dict, List, Tuple


def create_gnn_visualization(user_data: Dict, recommendations: Dict) -> go.Figure:
    """
    Create an interactive GNN graph visualization showing:
    - User node at center
    - Similar users (collaborative filtering)
    - Connected artists (from recommendations)
    - Connected events
    - Edge types showing relationships
    
    Args:
        user_data: Selected user information
        recommendations: Recommendations dict with artists and events
    
    Returns:
        Plotly figure object
    """
    
    # Define positions using optimized layout
    positions = {}
    
    # User at center
    user_x, user_y = 0, 0
    positions['user'] = (user_x, user_y)
    
    # Similar users in inner circle (for collaborative filtering visualization)
    similar_users = recommendations.get('similar_users', [])
    num_similar = min(len(similar_users), 4)
    similar_radius = 2.5
    for i in range(num_similar):
        angle = (2 * np.pi * i) / num_similar
        x = similar_radius * np.cos(angle)
        y = similar_radius * np.sin(angle)
        positions[f'similar_{i}'] = (x, y)
    
    # Artists in middle circle
    num_artists = min(len(recommendations.get('artists', [])), 6)
    artist_radius = 5
    for i in range(num_artists):
        angle = (2 * np.pi * i) / num_artists + np.pi / num_artists
        x = artist_radius * np.cos(angle)
        y = artist_radius * np.sin(angle)
        positions[f'artist_{i}'] = (x, y)
    
    # Events in outer circle
    num_events = min(len(recommendations.get('events', [])), 6)
    event_radius = 8
    for i in range(num_events):
        angle = (2 * np.pi * i) / num_events
        x = event_radius * np.cos(angle)
        y = event_radius * np.sin(angle)
        positions[f'event_{i}'] = (x, y)
    
    # Create edges
    user_similar_edges_x = []
    user_similar_edges_y = []
    user_artist_edges_x = []
    user_artist_edges_y = []
    artist_event_edges_x = []
    artist_event_edges_y = []
    
    # User to Similar Users (collaborative filtering connections)
    for i in range(num_similar):
        similar_pos = positions[f'similar_{i}']
        user_similar_edges_x.extend([user_x, similar_pos[0], None])
        user_similar_edges_y.extend([user_y, similar_pos[1], None])
    
    # User to Artists (direct recommendations)
    for i in range(num_artists):
        artist_pos = positions[f'artist_{i}']
        user_artist_edges_x.extend([user_x, artist_pos[0], None])
        user_artist_edges_y.extend([user_y, artist_pos[1], None])
    
    # Artists to Events (performs_at relationship)
    for i in range(min(num_artists, num_events)):
        artist_pos = positions[f'artist_{i}']
        event_pos = positions[f'event_{i}']
        artist_event_edges_x.extend([artist_pos[0], event_pos[0], None])
        artist_event_edges_y.extend([artist_pos[1], event_pos[1], None])
    
    # Create edge traces separately for each relationship type
    user_similar_edge_trace = go.Scatter(
        x=user_similar_edges_x, y=user_similar_edges_y,
        mode='lines',
        line=dict(width=3, color='rgba(156, 39, 176, 0.5)', dash='dash'),
        hoverinfo='none',
        showlegend=True,
        name='User Similarity',
        legendgroup='edges'
    )
    
    user_artist_edge_trace = go.Scatter(
        x=user_artist_edges_x, y=user_artist_edges_y,
        mode='lines',
        line=dict(width=2.5, color='rgba(208, 0, 0, 0.5)'),
        hoverinfo='none',
        showlegend=True,
        name='Recommendations',
        legendgroup='edges'
    )
    
    artist_event_edge_trace = go.Scatter(
        x=artist_event_edges_x, y=artist_event_edges_y,
        mode='lines',
        line=dict(width=1.5, color='rgba(100, 150, 200, 0.3)', dash='dot'),
        hoverinfo='none',
        showlegend=True,
        name='Artist → Event',
        legendgroup='edges'
    )
    
    # Create node traces for different node types
    # User node (center)
    user_trace = go.Scatter(
        x=[user_x], y=[user_y],
        mode='markers+text',
        marker=dict(
            size=45,
            color='#D00000',
            symbol='star',
            line=dict(width=3, color='#ffffff')
        ),
        text=[user_data['name'].split()[0]],
        textposition='bottom center',
        textfont=dict(size=14, color='#1a1a1a', family='Outfit', weight=700),
        hovertext=f"<b>👤 {user_data['name']}</b><br>📍 {user_data['city']}<br>Type: Current User",
        hoverinfo='text',
        showlegend=True,
        name='🔴 You',
        legendgroup='user'
    )
    
    # Similar user nodes
    if num_similar > 0:
        similar_x = [positions[f'similar_{i}'][0] for i in range(num_similar)]
        similar_y = [positions[f'similar_{i}'][1] for i in range(num_similar)]
        similar_names = [similar_users[i]['name'].split()[0] for i in range(num_similar)]
        similar_hover = [
            f"<b>👥 {similar_users[i]['name']}</b><br>" +
            f"Similarity: {int(similar_users[i]['similarity'] * 100)}%<br>" +
            f"Type: Similar User"
            for i in range(num_similar)
        ]
        
        similar_trace = go.Scatter(
            x=similar_x, y=similar_y,
            mode='markers+text',
            marker=dict(
                size=30,
                color='#9C27B0',
                symbol='hexagon',
                line=dict(width=3, color='#ffffff')
            ),
            text=similar_names,
            textposition='top center',
            textfont=dict(size=10, color='#1a1a1a', family='Outfit', weight=600),
            hovertext=similar_hover,
            hoverinfo='text',
            showlegend=True,
            name='🟣 Similar Users',
            legendgroup='similar'
        )
    else:
        similar_trace = go.Scatter(x=[], y=[], mode='markers', showlegend=False)
    
    # Artist nodes
    artists = recommendations.get('artists', [])
    artist_x = [positions[f'artist_{i}'][0] for i in range(num_artists)]
    artist_y = [positions[f'artist_{i}'][1] for i in range(num_artists)]
    artist_names = [artists[i]['name'].split()[0] if len(artists[i]['name'].split()[0]) <= 10 else artists[i]['name'].split()[0][:8] + "..." for i in range(num_artists)]
    artist_hover = [
        f"<b>🎭 {artists[i]['name']}</b><br>" +
        f"🎨 {', '.join(artists[i].get('art_forms', ['N/A']))}<br>" +
        f"🎵 {artists[i].get('genre', 'N/A')}<br>" +
        f"Type: Artist"
        for i in range(num_artists)
    ]
    
    artist_trace = go.Scatter(
        x=artist_x, y=artist_y,
        mode='markers+text',
        marker=dict(
            size=28,
            color='#4A90E2',
            symbol='circle',
            line=dict(width=3, color='#ffffff')
        ),
        text=artist_names,
        textposition='top center',
        textfont=dict(size=11, color='#1a1a1a', family='Outfit', weight=600),
        hovertext=artist_hover,
        hoverinfo='text',
        showlegend=True,
        name='🔵 Artists',
        legendgroup='artist'
    )
    
    # Event nodes
    events = recommendations.get('events', [])
    event_x = [positions[f'event_{i}'][0] for i in range(num_events)]
    event_y = [positions[f'event_{i}'][1] for i in range(num_events)]
    event_names = [events[i]['name'].split()[0] if len(events[i]['name'].split()[0]) <= 10 else events[i]['name'].split()[0][:8] + "..." for i in range(num_events)]
    event_hover = [
        f"<b>🎪 {events[i]['name']}</b><br>" +
        f"📍 {events[i]['city']}<br>" +
        f"🎵 {events[i].get('genre', 'N/A')}<br>" +
        f"Type: Event"
        for i in range(num_events)
    ]
    
    event_trace = go.Scatter(
        x=event_x, y=event_y,
        mode='markers+text',
        marker=dict(
            size=26,
            color='#00C9A7',
            symbol='diamond',
            line=dict(width=3, color='#ffffff')
        ),
        text=event_names,
        textposition='bottom center',
        textfont=dict(size=11, color='#1a1a1a', family='Outfit', weight=600),
        hovertext=event_hover,
        hoverinfo='text',
        showlegend=True,
        name='💎 Events',
        legendgroup='event'
    )
    
    # Create figure
    fig = go.Figure(
        data=[user_similar_edge_trace, user_artist_edge_trace, artist_event_edge_trace, 
              user_trace, similar_trace, artist_trace, event_trace],
        layout=go.Layout(
            title={
                'text': f'<b>Collaborative Filtering Graph Network</b><br><sub>User: {user_data["name"]} | Personalized + Community-Driven Recommendations</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18, 'color': '#1a1a1a', 'family': 'Outfit'}
            },
            titlefont_size=18,
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="top",
                y=0.98,
                xanchor="left",
                x=0.02,
                bgcolor="rgba(255, 255, 255, 0.95)",
                bordercolor="#cccccc",
                borderwidth=2,
                font=dict(size=11, family='Outfit')
            ),
            hovermode='closest',
            margin=dict(b=40, l=40, r=40, t=80),
            annotations=[
                dict(
                    text="<b>💡 Collaborative Filtering:</b> Purple hexagons = Users with similar tastes | Their preferences influence your recommendations",
                    xref="paper", yref="paper",
                    x=0.5, y=-0.02,
                    xanchor="center", yanchor="top",
                    showarrow=False,
                    font=dict(size=11, color="#555", family='Outfit')
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-9, 9]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-9, 9]),
            plot_bgcolor='#fafafa',
            paper_bgcolor='#ffffff',
            width=1000,
            height=750
        )
    )
    
    return fig


def create_gnn_architecture_diagram() -> go.Figure:
    """
    Create a diagram showing the GNN architecture with collaborative filtering
    """
    
    fig = go.Figure()
    
    # Layer information
    layers = [
        {
            'title': 'Input Layer',
            'desc': 'User Features\n+ Interests',
            'x': 1,
            'y': 2,
            'color': '#E8E8E8'
        },
        {
            'title': 'User Similarity',
            'desc': 'Find Similar\nUsers',
            'x': 2,
            'y': 2.5,
            'color': '#9C27B0'
        },
        {
            'title': 'GraphSAGE Conv',
            'desc': 'Message\nPassing',
            'x': 3,
            'y': 2,
            'color': '#4A90E2'
        },
        {
            'title': 'Collaborative Filter',
            'desc': 'Aggregate\nNeighbors',
            'x': 4,
            'y': 2.5,
            'color': '#00BCD4'
        },
        {
            'title': 'Output',
            'desc': 'Hybrid\nRecommendations',
            'x': 5,
            'y': 2,
            'color': '#D00000'
        }
    ]
    
    # Add layer boxes
    for layer in layers:
        fig.add_trace(go.Scatter(
            x=[layer['x']], y=[layer['y']],
            mode='markers+text',
            marker=dict(size=90, color=layer['color'], 
                       line=dict(width=3, color='#333')),
            text=layer['desc'],
            textposition='middle center',
            textfont=dict(size=9, color='#1a1a1a', family='Outfit', weight=600),
            hovertext=f"<b>{layer['title']}</b><br>{layer['desc'].replace(chr(10), '<br>')}",
            hoverinfo='text',
            showlegend=False
        ))
    
    # Add arrows between layers
    for i in range(len(layers) - 1):
        fig.add_annotation(
            x=layers[i]['x'] + 0.35, y=layers[i]['y'],
            ax=layers[i+1]['x'] - 0.35, ay=layers[i+1]['y'],
            xref='x', yref='y',
            axref='x', ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=3,
            arrowcolor='#666',
        )
    
    # Add data flow information boxes
    data_flows = [
        {'text': '👤 Content-Based\n(Your Interests)', 'x': 3, 'y': 1, 'color': '#4CAF50'},
        {'text': '👥 Collaborative\n(Similar Users)', 'x': 4, 'y': 1, 'color': '#9C27B0'},
        {'text': '🔥 Discovery\n(Trending)', 'x': 5, 'y': 1, 'color': '#FF9800'},
    ]
    
    for flow in data_flows:
        fig.add_trace(go.Scatter(
            x=[flow['x']], y=[flow['y']],
            mode='markers+text',
            marker=dict(size=70, color=flow['color'], opacity=0.7,
                       line=dict(width=2, color='#fff')),
            text=flow['text'],
            textposition='middle center',
            textfont=dict(size=8, color='#fff', family='Outfit', weight=700),
            showlegend=False
        ))
    
    # Add relationship type information
    relationships = [
        'User ↔ User (Similarity)',
        'User → Artist (Follows)',
        'Artist → Event (Performs)',
        'Artist ↔ Genre (Belongs)'
    ]
    
    for i, rel in enumerate(relationships):
        fig.add_annotation(
            x=0.15, y=0.75 - (i * 0.12),
            text=f"<b>•</b> {rel}",
            xref='paper', yref='paper',
            showarrow=False,
            font=dict(size=11, color='#555', family='Outfit'),
            xanchor='left',
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#ddd',
            borderwidth=1,
            borderpad=4
        )
    
    fig.update_layout(
        title={
            'text': '<b>Collaborative Filtering GNN Architecture</b><br><sub>Hybrid: Content-Based + Collaborative + Discovery</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#1a1a1a', 'family': 'Outfit'}
        },
        showlegend=False,
        hovermode='closest',
        margin=dict(b=50, l=50, r=50, t=100),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 6]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.5, 3]),
        plot_bgcolor='#fafafa',
        paper_bgcolor='#ffffff',
        width=1000,
        height=550
    )
    
    return fig
