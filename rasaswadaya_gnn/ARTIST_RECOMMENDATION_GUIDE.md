# How Artist Recommendations Work

## Overview

The system recommends artists to users using a **Graph Neural Network (GNN)** combined with **embeddings** and **link prediction**.

---

## Step-by-Step Process

### Step 1: Get User's Current Follow List

```python
user_follows = [f['artist_id'] for f in interactions['follows'] 
                if f['user_id'] == user_id]
```

- Extract all artists that the user is already following
- These are filtered OUT from recommendations (no duplicates)

**Example:**
- User "U0003" follows: [A0001, A0005, A0012]
- We only recommend from other 57 artists (60 - 3)

---

### Step 2: Get All Candidate Artists

```python
all_artist_ids = list(graph_builder.artists.keys())
candidate_artist_ids = [aid for aid in all_artist_ids if aid not in user_follows]
```

- Create a list of all unfollowed artists
- These are the candidates for recommendation

**Example:**
- Total artists: 60
- Already follows: 3
- Candidates: 57 artists

---

### Step 3: Generate GNN Embeddings

```python
with torch.no_grad():
    embeddings = model(x_dict, edge_index_dict)
```

The GNN processes the heterogeneous graph and creates **32-dimensional embeddings** for:
- All 150 users
- All 60 artists
- All 120 events
- All 16 genres

**What the embedding represents:**
- Encodes the artist's features (genres, style, mood, art forms, cultural attributes)
- Encodes the relationship patterns (which users follow similar artists)
- Encodes similarity to other nodes in the graph

---

### Step 4: Score Candidates Using Link Prediction

```python
user_emb = embeddings['user'][user_idx]                    # 32-D embedding
candidate_emb = embeddings['artist'][candidate_indices]   # Nx32 embeddings

scores = link_predictor(user_emb, candidate_emb)          # N scores
```

**Link Predictor (Neural Network):**
```
Input:  (user_embedding, candidate_embedding)  → [64-D, 64-D]
Hidden: Dense(128) → ReLU → Dropout(0.2)       → [128-D]
Output: Dense(1) → Sigmoid                      → [0.0-1.0 score]
```

**Scoring logic:**
- Higher score = higher compatibility between user and artist
- Score based on embedding similarity + learned patterns
- Trained on existing user-artist follow relationships

---

### Step 5: Select Top-K Recommendations

```python
top_scores, top_idx = torch.topk(scores, k=5)
top_indices = candidate_indices[top_idx]
```

- Sort all candidates by score (descending)
- Pick top-5 highest scoring artists
- Return their IDs and scores

---

## Complete Artist Recommendation Flow

```
┌─────────────────────────────────────┐
│ User requests recommendations       │
│ (e.g., User "U0003")                │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Step 1: Get user's follow history   │
│ User follows: [A0001, A0005, A0012] │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Step 2: Get candidate artists       │
│ Candidates: 57 artists (60 - 3)     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Step 3: Generate GNN embeddings     │
│ • User embedding: 32-D              │
│ • Artist embeddings: 57 x 32-D      │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Step 4: Score each candidate        │
│ Using link predictor neural network │
│ Score = link_predictor(user, artist)│
│ Range: 0.0 (bad) to 1.0 (perfect)  │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Step 5: Select top-5 artists        │
│ 1. Artist A (score: 0.895)         │
│ 2. Artist B (score: 0.875)         │
│ 3. Artist C (score: 0.850)         │
│ 4. Artist D (score: 0.825)         │
│ 5. Artist E (score: 0.800)         │
└─────────────────────────────────────┘
```

---

## What Influences Artist Scores?

### 1. **Graph Structure** (Main Factor)
The GNN learns patterns from the graph:
- Users with similar follows get similar embeddings
- Artists that attract similar users get grouped together
- If many users who follow Artist A also follow Artist B → Artist B gets high score

**Example:**
- You follow: [Kandyan dancers, Traditional music]
- System recommends other artists followed by similar users
- High score for artists in these genres

### 2. **Cultural DNA Features**
Each artist has features extracted from:
- Art forms (dance, drama, music, etc.)
- Genres (traditional, contemporary, fusion, etc.)
- Mood tags (celebratory, spiritual, etc.)
- Languages
- Style (classical, modern, etc.)

These are encoded in the artist's embedding.

### 3. **Collaborative Filtering**
The model learns:
> "Users who follow Artist A also tend to follow Artist X"

So if you follow Artist A (and many others like you), Artist X gets boosted.

---

## Example: Real Recommendation

**User:** Madhavi Rajapaksa (U0003)
- Interests: literature, kandyan arts
- City: Ratnapura
- Currently follows: 3 artists

**Recommendation Output:**
```
Top Artist Recommendations:
1. Chathura Rajapaksa (score: 0.500)
2. H.R. Jothipala (score: 0.500)
3. Sachini Dissanayake (score: 0.499)
4. Gayan Senanayake (score: 0.498)
5. Nalaka Nadarajah (score: 0.497)
```

**Why these artists?**
1. **Collaborative Filtering**: Users similar to Madhavi also follow these artists
2. **Cultural Match**: These artists perform kandyan and traditional arts
3. **Embedding Similarity**: Their embeddings are closest to Madhavi's user embedding

---

## Why Use GNN for Artist Recommendation?

### Traditional Approach ❌
```python
# Simple content-based: Match genres only
if user_genres == artist_genres:
    score = 1.0
```
**Problem:** All artists with same genres get equal score (not personalized)

### GNN Approach ✅
```python
# Graph-based: Learn from entire network
embedding_distance = distance(user_embedding, artist_embedding)
score = learned_function(embedding_distance)
```
**Benefits:**
- Captures indirect patterns (users follow similar users)
- Handles new artists (cold-start through embeddings)
- Learns what combinations work well together
- Personalized based on follow patterns

---

## Model Architecture

```
Graph Neural Network (GNN):
═════════════════════════════════════════════════════════════

Input Node Features:
  User: [Cultural DNA (67D) + user attributes]
  Artist: [Cultural DNA (67D) + genres, style, etc.]
  Event: [Cultural DNA (67D) + date, venue, etc.]
  Genre: [One-hot encoded (16D)]

Message Passing (Layer 1):
  ┌─────────────────┐
  │ User embeddings │ ─→ Aggregate artist follows
  └─────────────────┘
  ┌─────────────────┐
  │ Artist embeddings │ ─→ Aggregate user followers
  └─────────────────┘
  ┌─────────────────┐
  │ Event embeddings │ ─→ Aggregate artist performers
  └─────────────────┘

Message Passing (Layer 2):
  Second level aggregation (neighbors of neighbors)

Output Embeddings (32D each):
  User: 32-D embedding
  Artist: 32-D embedding
  Event: 32-D embedding
  Genre: 32-D embedding

Link Predictor (Neural Network):
  Input: (user_32D, artist_32D)
  Hidden: 128 neurons
  Output: Score (0.0-1.0)
```

---

## Parameters Used

| Parameter | Value | Reason |
|-----------|-------|--------|
| Embedding Dim | 32 | Captures 32 dimensions of artist-user compatibility |
| Hidden Channels | 64 | Intermediate representation |
| GNN Layers | 2 | Captures 2-hop neighborhood patterns |
| Link Predictor Hidden | 128 | Non-linear transformation |
| Top-K | 5 | Return 5 recommendations |
| Score Range | 0.0-1.0 | Normalized probability |

---

## Improving Artist Recommendations

### 1. **Better Cold-Start**
For new artists with no followers:
```python
# Use genre-based boosting
genre_sim = compute_genre_similarity(user, artist)
score = 0.6 * gnn_score + 0.4 * genre_sim
```

### 2. **Recency Weighting**
Prioritize recent follows:
```python
recency_weight = exponential_decay(days_since_follow)
score = gnn_score * recency_weight
```

### 3. **Diversity**
Avoid recommending too similar artists:
```python
# Add diversity penalty
if embedding_sim(artist1, artist2) > 0.8:
    score[artist2] *= 0.5  # Lower score if too similar to already recommended
```

### 4. **Hybrid Scoring**
Combine multiple signals:
```python
final_score = (0.5 * gnn_score 
             + 0.3 * genre_match 
             + 0.2 * location_match)
```

---

## Integration Points

### In Demo (`demo.py`):
```python
def generate_recommendations_for_user(model, data, graph_builder, user_id, top_k=5):
    # Lines 175-235
    # 1. Get user follows (line 207-208)
    # 2. Get candidates (line 211-212)
    # 3. Generate embeddings (line 190-192)
    # 4. Call model.recommend() (line 219-223)
    # 5. Parse results (line 225-230)
```

### In Model (`gnn_model.py`):
```python
def recommend(self, embeddings, user_idx, candidate_type, candidate_indices, top_k=10):
    # Line 202-223
    # 1. Get user embedding
    # 2. Get candidate embeddings
    # 3. Score using link predictor
    # 4. Return top-K
```

---

## Running Custom Artist Recommendations

```python
from data.generate_sample_data import load_dataset
from models.graph_builder import HeterogeneousGraphBuilder
from models.gnn_model import RecommendationModel

# Load data
dataset = load_dataset()

# Build graph
graph_builder = HeterogeneousGraphBuilder(dataset)
data = graph_builder.build()

# Create model
model = RecommendationModel(input_channels=67, hidden_channels=64, 
                            output_channels=32, num_layers=2)

# Get recommendations for specific user
recommendations = generate_recommendations_for_user(
    model, data, graph_builder, 
    user_id='U0003',  # Your target user
    top_k=10          # Get top 10
)

for artist_id, score, name in recommendations['artists']:
    print(f"{name}: {score:.3f}")
```

---

## Key Takeaways

1. **GNN-based approach** learns from the entire user-artist follow network
2. **Embeddings** capture multi-dimensional compatibility
3. **Link predictor** scores how likely a user-artist connection should exist
4. **Collaborative filtering** provides personalization
5. **Top-K selection** returns the best recommendations
6. **Avoids duplicates** by filtering already-followed artists
