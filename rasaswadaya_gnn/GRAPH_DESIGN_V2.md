# Rasaswadaya GNN - Graph Design V2 (Updated)

## Overview

This document describes the updated heterogeneous graph structure after removing unrealistic edges and implementing proper event recommendation logic.

---

## Graph Architecture

### Node Types (5)

```
├── Users (N_users)           - Platform users with region preferences
├── Artists (N_artists)       - Cultural performers
├── Events (N_events)         - Cultural gatherings with venue info
├── Genres (N_genres)         - Cultural classifications
└── Locations (N_locations)   - Geographic regions (9 in Sri Lanka)
```

### Edge Types (4) - UPDATED

**Important Principle:** Event attributes are DERIVED from performing artists.
Event genres are the UNION of all performing artists' genres.

```
✅ User --follows--> Artist
   • Direct user preference
   • Trainable via link prediction
   • Basis for artist recommendations

✅ Artist --performs_at--> Event  
   • Semantic connection
   • Enables 2-hop event discovery
   • No edge weight needed

✅ Artist --belongs_to--> Genre
   • Multi-hot (artist can have multiple genres)
   • Semantic grouping
   • Enables genre-based recommendations

✅ Event --features--> Genre
   • Multi-hot (event features multiple genres)
   • Semantic grouping
   • Shared with artists for cross-domain similarity

✅ Event --held_at--> Location
   • Venue information
   • Only location edges (not artist-based)
   • Enables location-aware filtering

❌ REMOVED: User --attends--> Event
   • Reason: No attendance data in graph (prevents data leakage)
   • Events recommended via 2-hop path instead
   • Attendance data kept in dataset for evaluation only

❌ REMOVED: Artist --based_in--> Location
   • Reason: Artists don't publicly reveal their region
   • Only venues (events) have public location info
```

---

## Data Relationships

### What's In the Graph
```
User Profile:
  - user_id, name, languages, art_interests, region_preference

Artist Profile (partial):
  - artist_id, name, art_forms, genres, language, style, moods
  - NO region (kept in metadata but not used for edges)

Event Profile (DERIVED from artists):
  - event_id, name, date, venue, region
  - artist_ids: list of performers
  - genres: UNION of all performing artists' genres
  - art_forms: UNION of all performing artists' art_forms
  - languages: UNION of all performing artists' languages
  - style: UNION of all performing artists' styles
  - mood_tags: UNION of all performing artists' moods

Example:
  Event "Kandyan + Baila Night"
    - Artist 1: Kandyan dancer → genres: [Kandyan]
    - Artist 2: Baila musician → genres: [Baila]
    - Result: Event genres: [Kandyan, Baila]

Genre Node:
  - genre_id, name

Location Node:
  - location_id (e.g., "L_Western"), name (region)
```

### What's NOT in the Graph
```
- User attendance history (not in edges)
- Artist location/region (not exposed as edges)
- Direct user-event relationships
```

---

## Message Passing Flow

### Example: Recommend Events to User "Kasun"

```
Step 1: Find Artists user follows
  Kasun --follows--> [Chitrasena, Nanda Malini, ...]

Step 2: Find Events those artists perform at
  Chitrasena --performs_at--> [Kandy Perahera, Colombo Festival, ...]
  Nanda Malini --performs_at--> [Temple Vesak, New Year Concert, ...]

Step 3: Find Genres those events feature
  Kandy Perahera --features--> [Kandyan, Classical, ...]
  Temple Vesak --features--> [Spiritual, Kandyan, ...]

Step 4: GNN learns embeddings
  - Kasun embedding captures: loves Kandyan + Spiritual
  - Kandy Perahera embedding captures: Kandyan + Spiritual
  - Similarity score: High → Recommend!

Step 5: Apply Location Filter (Optional)
  - Kasun region_preference: "Western"
  - Kandy Perahera region: "Central"
  - Distance score: Applied during ranking
```

---

## Recommendation Algorithms

### Algorithm 1: Artist Recommendations

**Task:** Predict which new artists user will follow

**Method:** Link prediction on User→Artist edges

```
1. Get user embedding (learned from follow patterns)
2. Get candidate artist embeddings
3. Score: sim(user_emb, artist_emb)
4. Rank by score
5. Return top-K
```

**Training Signal:** User→Artist follows (70% train, 15% val, 15% test)

---

### Algorithm 2: Event Recommendations (Combined - Option D)

**Task:** Predict which events user will be interested in

**Method:** Combined scoring (multiple signals)

```
Signal 1: Path-based (User -> Artist -> Event)
  For each artist user follows:
    For each event that artist performs in:
      score += path_strength(user -> artist -> event)

Signal 2: Genre-based (User -> Genre -> Event)
  For each genre user's artists belong to:
    For each event featuring that genre:
      score += genre_strength(user_pref -> genre -> event)

Signal 3: Embedding-based
  event_score = cosine_similarity(user_embedding, event_embedding)
  
Signal 4: Location-based
  location_score = proximity(event_region, user_region_preference)

Combined Score:
  final_score = 0.4 * embedding_score
              + 0.2 * path_score
              + 0.2 * genre_score
              + 0.2 * location_score
```

**Training Signal:** Attendance data used for evaluation only (not in graph edges)

---

## Why This Design?

### Realistic Data Modeling
- ✅ Artists don't expose their location publicly
- ✅ Venues (events) are public information
- ✅ Attendance not assumed in advance

### Prevents Data Leakage
- ✅ User→Event edges removed from graph
- ✅ Attendance used only for evaluation metrics
- ✅ Simulates real deployment scenario

### Explainability
- ✅ Event recs traceable to followed artists
- ✅ Genre connections explicit in graph
- ✅ Location filtering transparent

### Scalability
- ✅ Fewer edge types = simpler message passing
- ✅ 2-hop paths efficiently computed
- ✅ Embeddings capture complex patterns

---

## Graph Statistics (Sample)

```
Nodes:
  - Users: 150
  - Artists: 60
  - Events: 120
  - Genres: ~20
  - Locations: 9 (Sri Lankan regions)
  
Edges:
  - User→Artist: ~500 (follows)
  - Artist→Event: ~200 (performs_at)
  - Artist→Genre: ~150 (belongs_to)
  - Event→Genre: ~250 (features)
  - Event→Location: ~120 (held_at)
  
Total: ~1,220 edges (much sparser than with User→Event edges)
```

---

## Training & Inference

### Training Phase
```
1. Create graph with 4 edge types
2. Split User→Artist edges: 70% train, 15% val, 15% test
3. Generate negative samples for all splits
4. Train GNN with link prediction loss
5. Evaluate on validation set (link prediction accuracy)
6. Save best model
```

### Inference Phase - Artist Recommendations
```
1. Load trained model
2. Get user embedding
3. Get all candidate artist embeddings
4. Compute cosine similarities
5. Rank and return top-K
```

### Inference Phase - Event Recommendations
```
1. Load trained model
2. Get user embedding
3. Get all candidate event embeddings
4. Compute multiple signals (path, genre, embedding, location)
5. Combine scores with weights
6. Rank and return top-K
```

---

## Implementation Files

| File | Changes |
|------|---------|
| `models/graph_builder.py` | Removed User→Event edges, updated metadata |
| `models/gnn_model.py` | Added `recommend_events()` with combined scoring |
| `demo.py` | Updated event recommendation logic, edge splitting |
| `data/generate_sample_data.py` | No changes needed (keeps attendance data for evaluation) |

---

## Next Steps

1. **Test the updated model** - Run demo.py and verify recommendations
2. **Tune weights** - Adjust 0.4/0.2/0.2/0.2 scoring weights
3. **Add path computation** - Implement actual 2-hop path scoring
4. **Location filtering** - Add user region preference matching
5. **Visualize graph** - Show recommendation paths to users

---

## Backward Compatibility

- ✅ Attendance data still generated and stored
- ✅ Can be used for offline evaluation metrics
- ✅ Doesn't affect model training (not in graph)
- ✅ Easy to add back if needed for different task
