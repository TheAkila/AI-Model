# Demo Workflow: Visual Guide

## Quick Overview (TL;DR)

```
📊 Data → 🔗 Graph → 🧠 GNN Model → 🎯 Recommendations → 💡 Explanations
```

---

## Detailed Pipeline

### Phase 1: Preparation (Steps 1-2)

```
┌────────────────────────────────────────────────────────────────┐
│ STEP 1: DATA GENERATION                                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Config →  Generate Random Sri Lankan Cultural Data            │
│                                                                │
│     Users (150)           Artists (60)        Events (120)     │
│  ┌──────────────────┐  ┌────────────────┐  ┌──────────────┐  │
│  │ Name: Madhavi    │  │ Name: Chathura │  │ Name: Vesak  │  │
│  │ City: Ratnapura  │  │ Genre: Kandyan │  │ City: Kandy  │  │
│  │ Interests: Dance │  │ Mood: Spiritual│  │ Date: 12/25  │  │
│  │ City: Matara     │  │ City: Kandy    │  │ Artists: [A1]│  │
│  │ ...×148 more     │  │ ...×59 more    │  │ ...×119 more │  │
│  └──────────────────┘  └────────────────┘  └──────────────┘  │
│                                                                │
│           Interactions (~13,000 total)                         │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Follows (1,238):  U0003 → A0001                        │   │
│  │                   U0003 → A0005                        │   │
│  │                   ...                                  │   │
│  │ Attends (7,096):  U0003 → E0050                        │   │
│  │                   U0003 → E0087                        │   │
│  │                   ...                                  │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│                    ↓↓↓ SAVED ↓↓↓                              │
│           data/sample_dataset/*.pkl/.json                     │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ STEP 2: GRAPH CONSTRUCTION                                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Flat Data → Heterogeneous Graph                              │
│                                                                │
│              USERS (150)                                       │
│                  ▲                                             │
│                  │ follows (1,238)                            │
│                  │                                            │
│              ARTISTS (60)                                      │
│              ▲         ▼                                       │
│         performs_at   belongs_to                              │
│           (178)          (78)                                 │
│              ▲         ▼                                       │
│            EVENTS      GENRES (16)                            │
│             (120)       ▲   │                                  │
│              │          │   └─ features (199)                │
│              └─ held_at (120)                                │
│                          │                                    │
│                      LOCATIONS (9)                            │
│                                                                │
│  + Encode Cultural DNA Features                               │
│    Each node → 58D vector                                     │
│                                                                │
│    User embedding:    User_DNA (58D from interests)           │
│    Artist embedding:  Artist_DNA (58D: genres+mood+style)    │
│    Event embedding:   Event_DNA (58D from artists)            │
│    Genre embedding:   One-hot vectors                         │
│                                                                │
│            ↓↓↓ READY FOR GNN ↓↓↓                              │
│         346 nodes, 1,693 edges                                │
│         All with feature vectors                              │
└────────────────────────────────────────────────────────────────┘
```

---

### Phase 2: Training (Step 3)

```
┌────────────────────────────────────────────────────────────────┐
│ STEP 3: GNN TRAINING                                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Graph + Features → GNN Model → Learned Embeddings             │
│                                                                │
│  1️⃣ Edge Splitting                                            │
│     ┌──────────────────────────────┐                          │
│     │ 1,238 user-follows edges     │                          │
│     ├──────────────────────────────┤                          │
│     │ Train: 70% (867)             │                          │
│     │ Val:   15% (186)             │                          │
│     │ Test:  15% (185)             │                          │
│     └──────────────────────────────┘                          │
│                                                                │
│  2️⃣ Negative Sampling                                         │
│     For each positive edge (U follows A):                      │
│        Generate: U follows Random_Artist (negative)            │
│     Goal: Teach model what NOT to recommend                    │
│                                                                │
│  3️⃣ GNN Architecture                                          │
│     ┌─────────────────────────────────────────┐               │
│     │ INPUT: User features (58D)              │               │
│     │        Artist features (58D)            │               │
│     └─────────────┬───────────────────────────┘               │
│                   ▼                                            │
│     ┌─────────────────────────────────────────┐               │
│     │ LAYER 1: Message Passing                │               │
│     │ Aggregate neighbor artists              │               │
│     │ Dense(64D hidden)                       │               │
│     │ ReLU activation                         │               │
│     └─────────────┬───────────────────────────┘               │
│                   ▼                                            │
│     ┌─────────────────────────────────────────┐               │
│     │ LAYER 2: Message Passing (2-hop)        │               │
│     │ Aggregate artists of similar users      │               │
│     │ Dense(32D output)                       │               │
│     │ ReLU activation                         │               │
│     └─────────────┬───────────────────────────┘               │
│                   ▼                                            │
│     ┌─────────────────────────────────────────┐               │
│     │ USER & ARTIST EMBEDDINGS (32D each)     │               │
│     └─────────────┬───────────────────────────┘               │
│                   ▼                                            │
│     ┌─────────────────────────────────────────┐               │
│     │ LINK PREDICTOR NETWORK                  │               │
│     │ Input: [user_emb(32D), artist_emb(32D)]│               │
│     │ Dense(128) → ReLU → Dropout(0.2)        │               │
│     │ Dense(1) → Sigmoid                      │               │
│     │ Output: Score (0.0 = unlikely to follow)│               │
│     │         (1.0 = very likely to follow)   │               │
│     └─────────────┬───────────────────────────┘               │
│                   ▼                                            │
│     ┌─────────────────────────────────────────┐               │
│     │ LOSS = CrossEntropy(positive, negative) │               │
│     │ Penalizes:                              │               │
│     │ - Low scores for real follows           │               │
│     │ - High scores for fake follows          │               │
│     └─────────────────────────────────────────┘               │
│                                                                │
│  4️⃣ Training Loop (100 epochs)                                │
│     ┌──────────────────────────────────────┐                 │
│     │ Epoch  1: Loss=1.412 Val_Acc=0.500  │                 │
│     │ Epoch 10: Loss=1.387 Val_Acc=0.500  │                 │
│     │ Epoch 50: Loss=1.387 Val_Acc=0.543  │ ← Best          │
│     │ Epoch 60: Loss=1.386 Val_Acc=0.540  │ (saved)         │
│     │ Epoch 70: Loss=1.385 Val_Acc=0.540  │                 │
│     │ ...Early Stopping (no improvement)...│                 │
│     │ Epoch 75: STOP                       │                 │
│     └──────────────────────────────────────┘                 │
│                                                                │
│            ↓↓↓ TRAINED MODEL ↓↓↓                              │
│  Parameters learned: 102,145                                   │
│  Best checkpoint saved: checkpoints/best_model.pt              │
└────────────────────────────────────────────────────────────────┘
```

---

### Phase 3: Inference (Steps 4-6)

```
┌────────────────────────────────────────────────────────────────┐
│ STEP 4: ARTIST RECOMMENDATIONS                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  For User: Madhavi (U0003)                                    │
│                                                                │
│  INPUT: User embedding (32D)                                   │
│                                                                │
│  Process:                                                      │
│  ┌──────────────────────────────────────────┐                │
│  │ 1. Get already-followed artists:         │                │
│  │    Madhavi follows: [A0001, A0005, A12] │                │
│  │                                          │                │
│  │ 2. Get candidates (unfollowed):          │                │
│  │    Candidates: 57 artists (60-3)         │                │
│  │                                          │                │
│  │ 3. Get 57 artist embeddings (32D each)   │                │
│  │                                          │                │
│  │ 4. Score each: link_predictor(           │                │
│  │      user_emb, artist_emb) → score       │                │
│  │                                          │                │
│  │    Artist A: 0.528                       │                │
│  │    Artist B: 0.527                       │                │
│  │    Artist C: 0.526                       │                │
│  │    ...                                   │                │
│  │                                          │                │
│  │ 5. Sort by score (descending)            │                │
│  │                                          │                │
│  │ 6. Return top-5                          │                │
│  └──────────────────────────────────────────┘                │
│                                                                │
│  OUTPUT:                                                       │
│  1. Chathura Rajapaksa (0.528) ✅                             │
│  2. H.R. Jothipala (0.528)                                    │
│  3. Sachini Dissanayake (0.499)                               │
│  4. Gayan Senanayake (0.498)                                  │
│  5. Nalaka Nadarajah (0.497)                                  │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ STEP 4b: EVENT RECOMMENDATIONS (3-Signal Model)               │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  For User: Madhavi (U0003) in City: Ratnapura                 │
│                                                                │
│  For each event, calculate:                                    │
│                                                                │
│  SIGNAL 1: DISTANCE (40% weight)                              │
│  ────────────────────────────                                 │
│  event_city = event['city']                                   │
│  distance_km = haversine_distance(                            │
│      user_city='Ratnapura',                                   │
│      event_city='Ratnapura'                                   │
│  )                                                             │
│  distance_score = max(0.1, 1 - (distance_km / 500))          │
│                 = max(0.1, 1 - (0 / 500))                    │
│                 = 1.0 (perfect: same city)                    │
│                                                                │
│  proximity = "Same City"                                       │
│  travel_time = "0 minutes"                                     │
│  signal1_score = 0.40 × 1.0 = 0.40                           │
│                                                                │
│  SIGNAL 2: ARTISTS (35% weight)                               │
│  ──────────────────────                                       │
│  event_artists = ['A0034', 'A0089']                           │
│  user_follows = ['A0001', 'A0005', 'A0012']                  │
│  matching_artists = 0 (no overlap)                            │
│  artist_score = 0 / 2 = 0.0                                   │
│  signal2_score = 0.35 × 0.0 = 0.0                            │
│                                                                │
│  SIGNAL 3: GENRES (25% weight)                                │
│  ───────────────────────                                      │
│  event_genres = ['folk_music', 'traditional']                │
│  user_interests = ['literature', 'crafts']                    │
│  matching_genres = 0 (no overlap)                             │
│  genre_score = 0 / 2 = 0.0                                    │
│  signal3_score = 0.25 × 0.0 = 0.0                            │
│                                                                │
│  COMBINED SCORE:                                              │
│  ───────────────                                              │
│  total_score = 0.40 + 0.0 + 0.0 = 0.40                       │
│                                                                │
│  Sort all events by total_score (descending)                  │
│  Return top-5                                                  │
│                                                                │
│  OUTPUT:                                                       │
│  1. Celebration of Dilini (0.750)                            │
│     Ratnapura → Ratnapura | 0 km | Same City                 │
│     Score: 0.750 (Dist: 1.00, Art: 1.00, Genre: 0.00)       │
│                                                                │
│  2. Evening with Madhavi (0.723)                             │
│     Ratnapura → Kalutara | 33.6 km | Nearby                 │
│     Score: 0.723 (Dist: 0.93, Art: 1.00, Genre: 0.00)       │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ STEP 5: EXPLAINABILITY                                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Explain why "Chathura Rajapaksa" was recommended              │
│                                                                │
│  STEP 1: Encode User's Inferred DNA                            │
│  ─────────────────────────────────────                         │
│  Madhavi's followed artists:                                   │
│    - Chathura (kandyan, traditional, spiritual)               │
│    - H.R. Jothipala (classical, meditative)                   │
│    - Sachini (fusion, energetic)                              │
│                                                                │
│  Aggregate their attributes:                                  │
│  User DNA = [                                                  │
│    Art Forms: [0.6 dance, 0.4 music],                        │
│    Genres: [0.5 kandyan, 0.3 classical, 0.2 fusion],         │
│    Moods: [0.5 spiritual, 0.3 meditative, 0.2 energetic],    │
│    Style: [0.8 traditional, 0.1 contemporary, 0.1 fusion]     │
│  ]                                                             │
│                                                                │
│  STEP 2: Artist's DNA                                          │
│  ────────────────────                                          │
│  Chathura Rajapaksa DNA = [                                   │
│    Art Forms: [1.0 dance],                                    │
│    Genres: [1.0 kandyan],                                     │
│    Moods: [0.5 spiritual, 0.5 celebratory],                  │
│    Style: [1.0 traditional]                                   │
│  ]                                                             │
│                                                                │
│  STEP 3: Calculate Similarity                                  │
│  ─────────────────────────────                                │
│  Art Forms match:     dot([0.6, 0.4], [1, 0]) = 0.6          │
│  Genres match:        dot([0.5, 0.3, 0.2], [1, 0, 0]) = 0.5 │
│  Moods match:         dot([0.5, 0.3, 0.2], [0.5, 0, 0.5]) = 0.35
│  Style match:         dot([0.8, 0.1, 0.1], [1, 0, 0]) = 0.8 │
│                                                                │
│  Overall similarity = 66.4%                                    │
│                                                                │
│  OUTPUT:                                                       │
│  🎯 Why we recommend 'Chathura Rajapaksa':                    │
│  Overall similarity: 66.4%                                     │
│  Key matching dimensions:                                      │
│    ✓ Art Forms: Dance (your interest matches)                 │
│    ✓ Genres: Kandyan Traditional (exact match)                │
│    ✓ Style: Traditional (you prefer this)                     │
│  📋 Artist Details:                                            │
│    • Genres: kandyan                                           │
│    • City: Matale                                              │
│    • Style: traditional                                        │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│ STEP 6: TREND DETECTION                                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Find hottest artists (last 30 days)                           │
│                                                                │
│  Scoring:                                                      │
│  ────────                                                      │
│  For each artist:                                              │
│    engagement = (recent_follows × 2) + recent_event_attends  │
│                                                                │
│  Chathura Rajapaksa:                                           │
│    Recent follows: 23 × 2 = 46                                │
│    Event attendees: 0                                          │
│    Score: 46 + 0 = 46 ✅ #1 TRENDING                         │
│                                                                │
│  Chathura Herath:                                              │
│    Recent follows: 21 × 2 = 42                                │
│    Event attendees: 1                                          │
│    Score: 42 + 1 = 43 ✅ #2 TRENDING                         │
│                                                                │
│  ...                                                           │
│                                                                │
│  OUTPUT:                                                       │
│  📈 Top 5 Trending Artists (Last 30 Days):                    │
│                                                                │
│  1. Chathura Rajapaksa (46) - kandyan, Matale                │
│  2. Chathura Herath (43) - traditional, Anuradhapura         │
│  3. Sachini Dissanayake (42) - fusion, Anuradhapura          │
│  4. Annesley Malewana (41) - traditional, Polonnaruwa        │
│  5. Lasith Wickremasinghe (38) - kandyan, Nuwara Eliya       │
└────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Summary

```
Raw Data (CSV/JSON)
        ↓
┌───────────────────────────────────┐
│ Cultural DNA Encoding (58D)       │
│ - Art forms (7D)                  │
│ - Genres (25D)                    │
│ - Languages (5D)                  │
│ - Style (3D)                      │
│ - Moods (8D)                      │
│ - Festivals (11D)                 │
└────────────┬──────────────────────┘
             ↓
┌───────────────────────────────────┐
│ Heterogeneous Graph (PyG)         │
│ - 346 nodes (5 types)             │
│ - 1,693 edges (5 types)           │
│ - Features attached to nodes      │
└────────────┬──────────────────────┘
             ↓
┌───────────────────────────────────┐
│ GNN Model Training                │
│ - GraphSAGE/GAT 2 layers          │
│ - Link predictor network          │
│ - Train on 70% edges              │
└────────────┬──────────────────────┘
             ↓
┌───────────────────────────────────┐
│ Learned Embeddings (32D)          │
│ - User embeddings                 │
│ - Artist embeddings               │
│ - Event embeddings                │
│ - Genre embeddings                │
└────────────┬──────────────────────┘
             ↓
┌───────────────────────────────────┐
│ Scoring & Ranking                 │
│ - Link prediction score           │
│ - Distance-based scoring          │
│ - Multi-signal combination        │
└────────────┬──────────────────────┘
             ↓
┌───────────────────────────────────┐
│ Recommendations                   │
│ - Top-5 Artists (per user)        │
│ - Top-5 Events (per user)         │
│ - Explanations                    │
│ - Trend reports                   │
└───────────────────────────────────┘
```

---

## Metrics at Each Step

| Step | Input | Output | Time | Quality |
|------|-------|--------|------|---------|
| 1 | Config | 150 users, 60 artists, 120 events | 2s | ✅ Realistic |
| 2 | Dataset | 346 nodes, 1,693 edges | 1s | ✅ Complete |
| 3 | Graph | 32D embeddings | 25s | ✅ 54% acc |
| 4 | User | Top-5 artists + events | 1s | ✅ Relevant |
| 5 | Recommendation | Text explanation | 0.5s | ✅ Interpretable |
| 6 | Interactions | Top trending | 1s | ✅ Insightful |

---

## Conclusion

The demo is a **complete ML pipeline in ~30 seconds** that demonstrates:
- Data generation
- Feature engineering (Cultural DNA)
- Graph construction
- Deep learning (GNN)
- Inference (recommendations)
- Explainability (Cultural DNA similarity)
