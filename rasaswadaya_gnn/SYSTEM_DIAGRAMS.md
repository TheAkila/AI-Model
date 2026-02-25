# SYSTEM ARCHITECTURE & DATA MODEL DIAGRAMS

## 📊 DATA MODEL

### Entity Relationship Diagram

```
┌─────────────┐         ┌──────────────┐
│    USER     │◄───────►│    ARTIST    │
│             │  follows │              │
├─────────────┤         ├──────────────┤
│ user_id(PK) │         │artist_id(PK) │
│ name        │         │ name         │
│ city        │         │ art_form     │
│ interests[] │         │ genres[]     │
│ genres[]    │         │ moods[]      │
│ moods[]     │         │ followers    │
│             │         │ city         │
└─────────────┘         └──────────────┘
       │                      │
       │                      │
       │                      │ featured_in
       │                      │
       │                      ▼
       │         ┌──────────────────┐
       │         │      EVENT       │
       │         ├──────────────────┤
       │         │ event_id (PK)    │
       └────────►│ name             │
        attends  │ artist_id (FK)   │
                 │ city             │
                 │ date             │
                 │ venue            │
                 │ ticket_price     │
                 │ capacity         │
                 └──────────────────┘
```

### User Data Model (NEW)

```
USER RECORD (CSV Row)
┌──────────────────────────────────────────────────┐
│ user_id: "U0000"                                 │
│ name: "User_0"                                   │
│ city: "colombo"                                  │
├──────────────────────────────────────────────────┤
│ art_interests: ['dance', 'music', 'drama'] ✅NEW │
│ genres: ['political_theatre', 'rock']      ✅NEW │
│ moods: ['energetic', 'engaging']           ✅NEW │
├──────────────────────────────────────────────────┤
│ language: "english"                              │
│ follows: ['A0000', 'A0003', 'A0005']            │
│ attends: ['E0001', 'E0005']                     │
└──────────────────────────────────────────────────┘
```

### Artist Data Model

```
ARTIST RECORD (CSV Row)
┌──────────────────────────────────────────────────┐
│ artist_id: "A0000"                               │
│ name: "W.D. Amaradeva"                          │
│ art_form: "music"                               │
├──────────────────────────────────────────────────┤
│ genres: ['classical_semi_classical',            │
│          'devotional_religious']                 │
│ mood_tags: ['energetic', 'engaging']            │
│ styles: ['classical_semi_classical',            │
│          'devotional_religious']                 │
├──────────────────────────────────────────────────┤
│ languages: ['sinhala']                          │
│ city: "colombo"                                 │
│ follower_count: 1500000                         │
│ verified: true                                  │
│ era: "legend"                                   │
│ popularity: "superstar"                         │
└──────────────────────────────────────────────────┘
```

### Event Data Model

```
EVENT RECORD (CSV Row)
┌──────────────────────────────────────────────────┐
│ event_id: "E0000"                                │
│ name: "Concert of W.D. Amaradeva"               │
│ artist_ids: ['A0000']  (can be multiple)        │
│ art_form: "music"                               │
├──────────────────────────────────────────────────┤
│ city: "colombo"                                 │
│ date: "2026-01-01"                              │
│ time: "18:00"                                   │
│ venue: "Concert Hall"                           │
│ ticket_price: 500                               │
│ capacity: 100                                   │
└──────────────────────────────────────────────────┘
```

---

## 🔄 RECOMMENDATION ENGINE FLOW

### Complete Recommendation Pipeline

```
┌─────────────────────────────────────────────────────┐
│        USER OPENS STREAMLIT APP                    │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  LOAD DATASET                                       │
│  ├─ users.csv (100 users)                          │
│  ├─ artists.csv (28 artists)                       │
│  ├─ events.csv (80 events)                         │
│  ├─ follows.csv (595 relationships)                │
│  └─ attends.csv (350 attendances)                  │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  DISPLAY USER DROPDOWN                             │
│  └─ User selects: "User_0"                        │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  LOAD USER PROFILE                                  │
│  ├─ Parse art_interests: ['dance', 'music', ...] │
│  ├─ Parse genres: ['political_theatre', ...]     │
│  ├─ Parse moods: ['energetic', 'engaging']      │
│  └─ Get follows: ['A0001', 'A0005', ...]        │
└──────────────┬──────────────────────────────────────┘
               │
       ┌───────┴───────────────┐
       │                       │
       ▼                       ▼
  ┌──────────────┐         ┌──────────────┐
  │  ARTISTS OR  │         │   EVENTS     │
  │  TRENDING    │         │  OR TRENDING │
  │  BUTTON?     │         │  BUTTON?     │
  └──────────────┘         └──────────────┘
       │                       │
       ▼                       ▼
  [ARTIST FLOW]           [EVENT FLOW]
```

### Artist Recommendation Flow (Detailed)

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: CONTENT-BASED (50% weight)                    │
│  For each artist NOT in user.follows:                  │
│  ├─ Art Form Match:                                   │
│  │  if artist.form in user.art_interests              │
│  │  → score += 0.4                                    │
│  │  else if any genre matches                         │
│  │  → score += 0.2                                    │
│  ├─ Genre Match:                                      │
│  │  shared = user.genres ∩ artist.genres              │
│  │  score += 0.3 × (shared / len(user.genres))       │
│  ├─ Mood Match:                                       │
│  │  shared = user.moods ∩ artist.moods                │
│  │  score += 0.2 × (shared / len(user.moods))        │
│  ├─ Location + Popularity:                            │
│  │  score += 0.1 × min(followers / 500K, 1.0)       │
│  └─ Result: content_scores = dict(artist_id → score)│
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 2: COLLABORATIVE (30% weight)                    │
│  Find similar users:                                   │
│  For each other_user:                                 │
│  ├─ Jaccard(interests) × 0.40                        │
│  ├─ Jaccard(genres) × 0.15                           │
│  ├─ Jaccard(moods) × 0.15                            │
│  ├─ Jaccard(follows) × 0.25                          │
│  └─ City match × 0.05                                │
│  Similar_users = [users with score > 0.3]           │
│                                                      │
│  For each similar_user:                              │
│  ├─ For each artist in similar_user.follows:         │
│  │  if NOT in current_user.follows:                 │
│  │  collab_score[artist] += similarity_score         │
│  └─ Result: collab_scores = dict(artist_id → score) │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 3: DISCOVERY (20% weight)                        │
│  Get trending artists:                                 │
│  ├─ Sort by follower_count (descending)              │
│  ├─ Filter: NOT in user.follows                      │
│  └─ Result: discovery_scores = normalized ranking     │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 4: HYBRID SCORING                                │
│  For each artist:                                      │
│  hybrid_score = (content × 0.5) +                     │
│                 (collab × 0.3) +                       │
│                 (discovery × 0.2)                      │
│                                                        │
│  Sort by hybrid_score (descending)                    │
│  Return top 10 with reason                            │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  DISPLAY RESULTS                                       │
│  For each recommended artist:                          │
│  ├─ ⭐ Score: 0.85                                    │
│  ├─ 🎤 Name: W.D. Amaradeva                           │
│  ├─ 🎵 Art Form: music                                │
│  ├─ 💡 Reason: Content match (music interest + moods)│
│  └─ [Follow] button                                   │
└─────────────────────────────────────────────────────────┘
```

### Event Recommendation Flow

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: DISTANCE FILTERING                           │
│  For each event:                                       │
│  ├─ distance = haversine(user.city, event.city)       │
│  ├─ if distance > 500km → skip                        │
│  └─ else → score = max(0, 1 - distance/500)          │
│     (40% of final score)                              │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 2: ARTIST MATCHING (35% of score)               │
│  For each nearby event:                                │
│  ├─ event_artists = set(event.artist_ids)             │
│  ├─ user_follows = set(user.follows)                  │
│  ├─ match_count = |event_artists ∩ user_follows|     │
│  └─ artist_score = match_count / len(event_artists)   │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 3: INTEREST MATCHING (25% of score)              │
│  For each event:                                       │
│  ├─ if event.art_form in user.art_interests          │
│  │  → interest_score = 1.0                           │
│  ├─ elif match via genres                            │
│  │  → interest_score = 0.5                           │
│  └─ else (discovery)                                  │
│     → interest_score = 0.1                            │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 4: FINAL SCORING                                │
│  For each event:                                       │
│  event_score = (distance × 0.4) +                     │
│                (artist_match × 0.35) +                │
│                (interest_match × 0.25)                │
│                                                        │
│  Sort by event_score (descending)                     │
│  Return top 10 with details                           │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  DISPLAY RESULTS                                       │
│  For each recommended event:                           │
│  ├─ 🎪 Name: Concert of Yohani                       │
│  ├─ 📍 Location: Colombo (0km away)                  │
│  ├─ 🎤 Artists: Yohani                                │
│  ├─ 📅 Date/Time: 2026-05-15 18:00                   │
│  ├─ 🎫 Ticket: Rs 503 | Capacity: 120                │
│  └─ [Attend] button                                   │
└─────────────────────────────────────────────────────────┘
```

### Trending Now Flow

```
┌─────────────────────────────────────────────────────────┐
│  OPTION A: NOT PERSONALIZED                           │
│  (or User_0 not selected)                             │
└──────────────┬──────────────────────────────────────────┘
               │
      ┌────────┴────────┬──────────────┬─────────────┐
      │                 │              │             │
      ▼                 ▼              ▼             ▼
  TRENDING         TRENDING        TRENDING      TRENDING
  ARTISTS BY       EVENTS BY       GENRES BY     ARTISTS BY
  FOLLOWERS        ATTENDANCE      ENGAGEMENT    DIVERSITY
  
  1. Yohani        1. Concert of   1. Music      1. Music
  2. W.D. A        2. Festival     2. Dance      2. Dance
  3. Bathiya    3. Competition   3. Pop         3. Film
  
└──────────────┬──────────────────────────────────────────┘
               │
┌──────────────────────────────────────────────────────────┐
│  OPTION B: PERSONALIZED                                │
│  (User_0 selected)                                     │
└──────────────┬──────────────────────────────────────────┘
               │
      ┌────────┴────────┬──────────────┬─────────────┐
      │                 │              │             │
      ▼                 ▼              ▼             ▼
  PERSONALIZED  PERSONALIZED   PERSONALIZED  PERSONALIZED
  ARTISTS       EVENTS         GENRES        BY CITY
  
  Boost:        Boost:         Boost:        Filter to
  artist.form   event.city     user.genres   user.city
  in user.art   in user.city   +30%          events
  interests     +40%
  +30%
  
  1. W.D. A     1. Concert of  1. Music      1. Concert
  2. Bathiya    2. Dance Comp  2. Dance    2. Festival
  3. Music      3. Festival    3. Pop      3. Music Fest
  
└─────────────────────────────────────────────────────────┘
```

---

## 📈 SCORING MATRICES

### User Similarity Calculation Matrix

```
        User_A      User_B      Similarity Weight  Contribution
        ───────     ───────     ─────────           ────────────
art_int  [M, D]     [M, F]      1/3 = 0.33    ×0.40 = 0.132
genres   [Pop, R]   [Pop, C]    1/3 = 0.33    ×0.15 = 0.050
moods    [E, En]    [E, En]     2/2 = 1.00    ×0.15 = 0.150
follows  [A1,A2]    [A1,A3]     1/3 = 0.33    ×0.25 = 0.083
city     Colombo    Colombo     Yes           ×0.05 = 0.050
                                                     ────────
                                    Total Similarity = 0.465
```

### Artist Scoring Matrix (User_0 recommending artists)

```
Artist          Art Form  Match  Genre  Mood  Score
─────────────   ────────  ─────  ─────  ────  ─────
W.D. Amaradeva  Music ✅   0.4    0.1    0.2   → 0.87
Yohani          Music ✅   0.4    0.15   0.2   → 0.85
Chitrasena      Dance ✅   0.4    0.2    0.15  → 0.78
Jackson Anthony Film ❌    0.2    0.1    0.2   → 0.62
Victor Ratnayake Music ✅   0.4    0.15   0.15  → 0.80
```

### Event Scoring Matrix

```
Event                Location Distance Artist Match Interest Score
─────────────────── ─────── ──────── ────── ─────────────────────
Concert of Yohani   Colombo 0km      ✅✅   Music   → 0.95
Festival of Music   Colombo 0km      ✅     Music   → 0.82
Dance Competition   Kandy   120km    ✅     Dance   → 0.68
Cultural Show       Galle   180km    ❌     Drama   → 0.55
```

---

## 🔀 DATA FLOW DIAGRAM

```
CSV FILES (Input)
├─ users.csv
│  ├─ user_id
│  ├─ art_interests[] ← NEW (Multiple values)
│  ├─ genres[]        ← NEW (Multiple values)
│  └─ moods[]         ← NEW (Multiple values)
│
├─ artists.csv
│  ├─ artist_id
│  ├─ art_form
│  ├─ genres[]
│  ├─ mood_tags[]
│  └─ follower_count
│
├─ events.csv
│  ├─ event_id
│  ├─ artist_id
│  ├─ city
│  └─ date
│
├─ follows.csv
│  ├─ user_id
│  └─ artist_id
│
└─ attends.csv
   ├─ user_id
   └─ event_id
       │
       ▼
    ┌──────────────────────────────┐
    │   DATA LOADER (Updated)      │
    │ ├─ load_dataset()            │
    │ ├─ load_users_list()    ✅   │
    │ ├─ load_artists_df()         │
    │ └─ load_events_df()          │
    │                              │
    │ Parses:                      │
    │ ├─ ast.literal_eval()        │
    │ └─ Multi-valued fields  ✅   │
    └──────────────────────────────┘
       │
       ▼
    ┌──────────────────────────────┐
    │  RECOMMENDER (Updated)       │
    │ ├─ calculate_user_sim()  ✅  │
    │ ├─ calculate_artist_score()✅│
    │ ├─ get_content_based()       │
    │ ├─ get_collaborative()       │
    │ ├─ get_discovery()           │
    │ └─ get_trending_data()       │
    └──────────────────────────────┘
       │
       ▼
    ┌──────────────────────────────┐
    │   STREAMLIT APP              │
    │ ├─ User Dropdown             │
    │ ├─ Profile Display           │
    │ ├─ Recommendations           │
    │ ├─ Events                    │
    │ ├─ Trending Now              │
    │ └─ Buttons (Follow/Attend)   │
    └──────────────────────────────┘
       │
       ▼
    ┌──────────────────────────────┐
    │   UI DISPLAY (Browser)       │
    │ http://localhost:8501        │
    └──────────────────────────────┘
```

---

## 🎯 SCORING SCHEMA SUMMARY

### Content-Based Scoring Formula

```
SCORE = BASE_SCORE + 
        (art_form_match × 0.4) +
        (genre_overlap × 0.3) +
        (mood_overlap × 0.2) +
        (popularity_factor × 0.1)

Where:
- base_score = 0.3
- art_form_match = 1.0 or 0.2 (soft)
- genre_overlap = (shared_genres / max_genres)
- mood_overlap = (shared_moods / max_moods)
- popularity_factor = min(followers / 500K, 1.0)

Result: Capped at 1.0
```

### Collaborative Scoring Formula

```
SIMILARITY = (interest_jac × 0.40) +
             (genre_jac × 0.15) +
             (mood_jac × 0.15) +
             (follow_jac × 0.25) +
             (city_match × 0.05)

Where:
- Jac(A, B) = |A ∩ B| / |A ∪ B|

Then:
COLLAB_SCORE = Σ(similar_user_similarity × 
               artist_in_similar_follows)
```

### Event Scoring Formula

```
EVENT_SCORE = (distance_score × 0.4) +
              (artist_match × 0.35) +
              (interest_match × 0.25)

Where:
- distance_score = max(0, 1 - distance_km/500)
- artist_match = matched_artists / total_artists
- interest_match = 1.0 (match), 0.5 (soft), 0.1 (discovery)
```

### Hybrid Recommendation Formula

```
HYBRID_SCORE = (content_score × 0.5) +
               (collaborative_score × 0.3) +
               (discovery_score × 0.2)
```

---

## 📊 STATISTICS DASHBOARD

### Current System Metrics

```
USER DATASET:
  Total Users: 100
  Avg interests per user: 1.85 (was: 1.0)
  Avg genres per user: 3.2 (was: 0)
  Avg moods per user: 3.1 (was: 1.0)
  Avg follows per user: 5.95
  
ARTIST DATASET:
  Total Artists: 28 (All Real Sri Lankan)
  Music: 15 | Dance: 4 | Film: 5 | Drama: 4
  Total followers: 21.3M
  Verified: 100%
  
EVENT DATASET:
  Total Events: 80
  Cities covered: 6 (Colombo, Galle, Kandy, Jaffna, Matara, Anuradhapura)
  Avg attendance: 43.75 per event
  
RELATIONSHIPS:
  Follows: 595
  Attends: 350
  Follow-to-user ratio: 5.95
  Attend-to-user ratio: 3.5
  
COVERAGE:
  Artists reachable per user (old): 25
  Artists reachable per user (new): 65
  Improvement: +160%
```

---

*Last Updated: February 25, 2026*
