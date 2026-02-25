# Recommendation Workflows Documentation

## Overview

The Streamlit app implements a **Hybrid Recommendation System** combining three approaches:
- **Content-Based (50%)**: Match user interests with artist/event attributes
- **Collaborative Filtering (30%)**: Find similar users and recommend their preferences
- **Discovery/Trending (20%)**: Explore new content based on popularity

---

## 1. RECOMMENDED ARTISTS WORKFLOW

### Data Flow Diagram
```
User Profile
    ├─ art_interests [dance, music, drama]
    ├─ genres [pop, classical, devotional]
    ├─ moods [energetic, engaging]
    └─ follows [A0001, A0005]
         │
         ├─→ [1] CONTENT-BASED FILTERING (50%)
         │        ├─ Match art forms
         │        ├─ Match genres
         │        ├─ Match moods
         │        └─ Score: 0-1.0
         │
         ├─→ [2] COLLABORATIVE FILTERING (30%)
         │        ├─ Find similar users
         │        ├─ Get their followed artists
         │        ├─ Recommend unfollowed artists
         │        └─ Score: 0-1.0
         │
         └─→ [3] DISCOVERY/TRENDING (20%)
                  ├─ Popular artists
                  ├─ New artists
                  ├─ Trending in user's region
                  └─ Score: 0-1.0
             │
             └─→ HYBRID SCORE = (C×0.5) + (Co×0.3) + (D×0.2)
                                    │
                                    └─→ RANKED RECOMMENDATIONS
```

### Step 1: Content-Based Filtering

**Function**: `get_content_based_artist_recommendations(user_data, dataset)`

**Algorithm**:
```
For each artist not followed by user:
    score = 0.3  (base score)
    
    # Art Form Matching (40%)
    if artist.art_form in user.art_interests:
        score += 0.4
    
    # Genre Matching (30%)
    shared_genres = user.genres ∩ artist.genres
    score += 0.3 × (|shared_genres| / max(len(user.genres), 1))
    
    # Mood Matching (20%)
    shared_moods = user.moods ∩ artist.moods
    score += 0.2 × (|shared_moods| / max(len(user.moods), 1))
    
    # Popularity Boost (10%)
    followers = artist.follower_count
    score += 0.1 × min(followers / 500000, 1.0)

Final Score = min(score, 1.0)
```

**Example**:
```
User Profile:
  art_interests: [music, dance]
  genres: [classical, pop, devotional]
  moods: [energetic, engaging]

Artist: Yohani
  art_form: music ✅ (matches music in art_interests)
  genres: [pop, sinhala_commercial] ✅ (pop matches)
  moods: [energetic, engaging] ✅ (both match)
  followers: 5.2M ✅ (popular)

Content Score = 0.4 + (0.3 × 1/3) + (0.2 × 2/2) + 0.1 = 0.8
```

### Step 2: Collaborative Filtering

**Function**: `get_collaborative_artist_recommendations(user_data, dataset)`

**Algorithm**:
```
1. Find similar users
   For each other_user:
       similarity = calculate_user_similarity(user, other_user)
       if similarity > 0.3:
           add to similar_users
   
2. Get artists followed by similar users
   for similar_user in similar_users:
       for artist in similar_user.follows:
           if user doesn't follow artist:
               collaborative_score += similarity × (1/len(similar_users))

3. Weight by artist popularity
   final_score = collaborative_score × 0.3 × popularity_factor
```

**User Similarity Calculation**:
```
similarity_score = 0.0

# Interest Similarity (40%)
shared_interests = user1.art_interests ∩ user2.art_interests
interest_sim = |shared_interests| / |user1.art_interests ∪ user2.art_interests|
similarity_score += interest_sim × 0.4

# Mood Similarity (30%)
shared_moods = user1.moods ∩ user2.moods
mood_sim = |shared_moods| / |user1.moods ∪ user2.moods|
similarity_score += mood_sim × 0.3

# Followed Artists Overlap (25%)
shared_follows = user1.follows ∩ user2.follows
follow_sim = |shared_follows| / |user1.follows ∪ user2.follows|
similarity_score += follow_sim × 0.25

# City Proximity (5%)
if user1.city == user2.city:
    similarity_score += 0.05

Final similarity = min(similarity_score, 1.0)
```

**Example**:
```
User_A (Colombo):
  art_interests: [music, dance]
  moods: [energetic, engaging]
  follows: [A0000, A0001, A0005]

User_B (Colombo):
  art_interests: [music, film]
  moods: [engaging, energetic]
  follows: [A0000, A0003, A0010]

Similarity Calculation:
  - art_interests overlap: 1/3 = 0.33 → 0.33 × 0.4 = 0.132
  - moods overlap: 2/2 = 1.0 → 1.0 × 0.3 = 0.300
  - follows overlap: 1/5 = 0.20 → 0.20 × 0.25 = 0.050
  - city match: Colombo = Colombo → 0.05
  
  Total Similarity = 0.532

Collaborative Recommendation:
  User_B follows [A0000, A0003, A0010]
  User_A doesn't follow: [A0003, A0010]
  
  Recommendation Score = 0.532 × 1.0 × popularity_factor
```

### Step 3: Discovery/Trending

**Function**: `get_discovery_recommendations(user_data, dataset)`

**Algorithm**:
```
1. Get trending artists (by follow count)
   trending_artists = sort(artists, by=follower_count)[:top_k]
   trending_artists = remove(trending_artists, user.follows)

2. Score based on:
   - Artist popularity (relative to others)
   - Match to user's interests (soft match)
   - Geographic proximity (if available)
   - Era preferences (if available)

3. Diversity boost
   Ensure user sees different art forms, not just their primary interest
```

**Example**:
```
Trending Artists (sorted by followers):
1. Yohani (5.2M, music)
2. W.D. Amaradeva (1.5M, music)
3. Jackson Anthony (900K, film)
4. Victor Ratnayake (920K, music)
...

User_A follows: [A0000]
Discovery Recommendations (already filtered):
- A0003 (Yohani)
- A0001 (Jackson Anthony)
- A0002 (Victor Ratnayake)

Discovery Boost = 0.2 × (trending_score × diversity_factor)
```

### Final Hybrid Score

```
For each candidate artist:
    content_score = get_content_based_score(user, artist)
    collab_score = get_collaborative_score(user, artist, similar_users)
    discovery_score = get_discovery_score(artist, trending)
    
    FINAL_SCORE = (content_score × 0.5) + (collab_score × 0.3) + (discovery_score × 0.2)

Sort by FINAL_SCORE (descending)
Return top_k artists
```

---

## 2. RECOMMENDED EVENTS WORKFLOW

### Data Flow Diagram
```
User Profile           Event Data
    ├─ city             ├─ city
    ├─ art_interests    ├─ artist_ids
    ├─ genres           ├─ venue
    └─ follows          ├─ ticket_price
                        └─ capacity
         │
         ├─→ [1] LOCATION FILTERING
         │        ├─ Calculate distance
         │        ├─ Filter nearby events (500km)
         │        └─ Score by proximity
         │
         ├─→ [2] ARTIST MATCHING
         │        ├─ Events by followed artists (high boost)
         │        ├─ Events by similar artists
         │        └─ Score: 0-1.0
         │
         ├─→ [3] INTEREST MATCHING
         │        ├─ Match event art form with user interests
         │        └─ Score: 0-1.0
         │
         ├─→ [4] POPULARITY
         │        ├─ Based on attendance
         │        └─ Score: 0-1.0
         │
         └─→ [5] COLLABORATIVE EVENT
                  ├─ Events attended by similar users
                  └─ Score: 0-1.0
             │
             └─→ COMPUTE FINAL EVENT SCORE
                    │
                    └─→ RANKED EVENT RECOMMENDATIONS
```

### Algorithm

**Function**: `get_event_recommendations(user_data, dataset)`

**Scoring**:
```
For each event:
    score = 0.5  (base score)
    
    # [1] DISTANCE SCORING (40%)
    distance = calculate_distance(user.city, event.city)
    if distance > 500km:
        skip event  # Filter out far events
    distance_score = max(0, 1 - (distance / 500))
    score += distance_score × 0.4
    
    # [2] ARTIST SCORING (35%)
    user_follows = set(user.follows)
    event_artists = set(event.artist_ids)
    artist_match = |user_follows ∩ event_artists| / max(|event_artists|, 1)
    score += artist_match × 0.35
    
    # [3] ART FORM SCORING (25%)
    if event.art_form in user.art_interests:
        score += 0.25
    elif event.art_form in user.interests:
        score += 0.15  # Soft match
    else:
        score += 0.05  # Discovery
    
    # Additional factors:
    # - Ticket price accessibility (if user_preference available)
    # - Time proximity (upcoming events > future)
    # - Venue popularity

Final event_score = min(score, 1.0)
```

**Example**:
```
User_A (Colombo):
  city: colombo
  follows: [A0000, A0003]
  art_interests: [music, dance]

Event E0001:
  name: "Concert of Yohani"
  city: colombo
  artist_ids: [A0003]
  art_form: music
  date: 2026-05-15
  ticket_price: 503

Event Scoring:
  Distance: 0km → distance_score = 1.0 × 0.4 = 0.4
  Artists: follows A0003 → 1/1 = 1.0 × 0.35 = 0.35
  Art Form: music in interests → 0.25
  Popularity: high attendance → bonus
  
  Final Score = 0.4 + 0.35 + 0.25 + 0.5_base = 1.5 (capped at 1.0)
```

### Event Recommendation Types

1. **Must-Attend** (Artist Follow Match)
   - User follows an artist performing at the event
   - High priority recommendation

2. **Interest-Matched** (Location + Art Form)
   - Event matches user's art form interests
   - Close proximity
   - Good for discovery

3. **Collaborative** (Similar Users)
   - Similar users attended or plan to attend
   - Signals quality event

---

## 3. TRENDING NOW WORKFLOW

### Data Flow Diagram
```
Dataset
    ├─ Artists: [artist, followers, moods, genres]
    ├─ Events: [event, attendees, art_form, city]
    ├─ Users: [interests, moods, follows, attends]
    └─ Interactions: [follows, attends]
         │
         ├─→ [1] TRENDING ARTISTS
         │        ├─ Count follows per artist
         │        ├─ Sort by follower_count
         │        ├─ Filter by art form diversity
         │        └─ Return top_k
         │
         ├─→ [2] TRENDING EVENTS
         │        ├─ Count attendees per event
         │        ├─ Apply time decay (recent > old)
         │        ├─ Filter location-relevant
         │        └─ Return top_k
         │
         ├─→ [3] TRENDING ART FORMS
         │        ├─ Aggregate follows per art_form
         │        ├─ Count event attendances
         │        ├─ Weight by user engagement
         │        └─ Return top_k
         │
         └─→ [4] PERSONALIZED TRENDING (if user selected)
                  ├─ Boost artists in user's interests
                  ├─ Boost events in user's city
                  ├─ Favor artists user might like
                  └─ Return personalized top_k
```

### Algorithm

**Function**: `get_trending_data(user=None, days=30, personalized=True)`

#### Trending Artists

```
1. Count followers per artist (global adoption)
   for follow in dataset.follows:
       artist_follows[artist_id] += 1

2. Get engagement metrics
   popularity = artist.follower_count
   trend_score = popularity × (1 + engagement_bonus)

3. Sort and return
   trending_artists = sort(artists, by=trend_score)[:10]
```

**Example**:
```
Top Trending Artists:
1. Yohani (5.2M followers) - Score: 5,200,000
2. W.D. Amaradeva (1.5M followers) - Score: 1,500,000
3. Bathiya & Santhush (1.2M followers) - Score: 1,200,000
4. Jackson Anthony (900K followers) - Score: 900,000
5. Victor Ratnayake (920K followers) - Score: 920,000
```

#### Trending Events

```
1. Count attendees per event
   for attend in dataset.attends:
       event_attendees[event_id] += 1

2. Apply time decay (recent events score higher)
   days_old = (today - event.date).days
   time_decay = e^(-days_old / 30)  # Half-life: 30 days
   
3. Boost by user engagement
   engagement = event_attendees[event_id]
   engagement_score = min(engagement / 100, 1.0)
   
4. Final trending score
   trend_score = engagement_score × time_decay × proximity_factor

5. Sort and return
   trending_events = sort(events, by=trend_score)[:10]
```

**Example**:
```
Top Trending Events (within 500km of user):
1. "Concert of Yohani" - 45 attendees, 10 days old, Colombo
2. "Festival of Music" - 38 attendees, 5 days old, Kandy
3. "Dance Competition" - 28 attendees, 2 days old, Colombo
```

#### Trending Art Forms/Genres

```
1. Aggregate engagement by category
   for follow in dataset.follows:
       artist = get_artist(follow.artist_id)
       genre_engagement[artist.genres] += weight_follow
   
   for attend in dataset.attends:
       event = get_event(attend.event_id)
       genre_engagement[event.art_form] += weight_attend

2. Normalize and rank
   trending_genres = sort(genre_engagement, descending=True)[:8]

3. Return with engagement scores
   return [
       {name: "pop", engagement: 250},
       {name: "classical", engagement: 198},
       ...
   ]
```

#### Personalized Trending (if user_id provided)

```
If user is selected:
    1. Apply user preference soft matching
       for trend_item in trending_list:
           if trend_item.art_form in user.art_interests:
               boost_score(trend_item, 0.3)  # +30% boost
           elif trend_item.genre in user.genres:
               boost_score(trend_item, 0.2)  # +20% boost
    
    2. Prioritize user's region
       for event in trending_events:
           if event.city in user.nearby_cities:
               boost_score(event, 0.4)  # +40% boost
    
    3. Highlight artists similar to user's follows
       for artist in trending_artists:
           similarity = calculate_artist_similarity(
               artist, 
               user_followed_artists
           )
           if similarity > 0.6:
               boost_score(artist, 0.2)
    
    4. Re-sort by boosted scores
       personalized_trending = sort(trending_list, by=boosted_score)

Output: Trending content relevant to the selected user
```

---

## 4. DATA STRUCTURES

### User Profile
```json
{
  "user_id": "U0000",
  "name": "User_0",
  "city": "colombo",
  "art_interests": ["music", "dance", "drama"],
  "genres": ["pop", "classical", "devotional"],
  "moods": ["energetic", "engaging"],
  "language": "english",
  "follows": ["A0000", "A0003", "A0005"],
  "attends": ["E0001", "E0005"]
}
```

### Artist Profile
```json
{
  "artist_id": "A0000",
  "name": "W.D. Amaradeva",
  "art_form": "music",
  "genres": ["classical_semi_classical", "devotional_religious"],
  "moods": ["energetic", "engaging"],
  "languages": ["sinhala"],
  "city": "colombo",
  "follower_count": 1500000,
  "verified": true,
  "era": "legend",
  "popularity": "superstar"
}
```

### Event Profile
```json
{
  "event_id": "E0000",
  "name": "Concert of W.D. Amaradeva",
  "artist_ids": ["A0000"],
  "art_form": "music",
  "city": "colombo",
  "date": "2026-01-01",
  "time": "18:00",
  "venue": "Concert Hall",
  "ticket_price": 500,
  "capacity": 100
}
```

---

## 5. SCORING SUMMARY

### Content-Based Scoring (Artist)
| Component | Weight | Calculation |
|-----------|--------|-------------|
| Art Form Match | 40% | 1.0 if match, else 0 |
| Genre Match | 30% | overlapping genres / max genres |
| Mood Match | 20% | overlapping moods / max moods |
| Popularity | 10% | min(followers / 500K, 1.0) |

### Collaborative Filtering (Artist)
| Component | Calculation |
|-----------|-------------|
| Similar Users | Jaccard similarity on interests + moods + follows |
| Artist From Similar User | similarity_score × normalization |
| Final Weight | 30% of hybrid score |

### Event Scoring
| Component | Weight | Formula |
|-----------|--------|---------|
| Distance | 40% | max(0, 1 - distance/500km) |
| Artist Match | 35% | matched_artists / total_artists |
| Art Form | 25% | 1.0 if match, 0.5 if soft, 0.1 if discovery |

---

## 6. WORKFLOW EXECUTION FLOW

```
USER OPENS STREAMLIT APP
    │
    ├─→ SELECT USER FROM DROPDOWN
    │      └─→ Load user profile from CSV
    │
    ├─→ CLICK "GET RECOMMENDATIONS"
    │      ├─ get_artist_recommendations()
    │      │   ├─ Content-based: 50%
    │      │   ├─ Collaborative: 30%
    │      │   ├─ Discovery: 20%
    │      │   └─ Return top 10 artists
    │      │
    │      ├─ get_event_recommendations()
    │      │   ├─ Distance filter (500km)
    │      │   ├─ Artist match scoring
    │      │   ├─ Interest matching
    │      │   └─ Return top 10 events
    │      │
    │      └─ Display cards with:
    │         - Artist/Event name
    │         - Recommendation reason
    │         - Follow/Attend button
    │
    ├─→ CLICK "TRENDING NOW"
    │      ├─ get_trending_data(user, personalized=true)
    │      │   ├─ Count follows → trending artists
    │      │   ├─ Count attendees → trending events
    │      │   ├─ Aggregate genre/form engagement
    │      │   ├─ Apply user preferences
    │      │   └─ Return trending lists
    │      │
    │      └─ Display:
    │         - Top 3 trending artists
    │         - Top 3 trending events
    │         - Top 3 trending genres
    │
    ├─→ CLICK "FOLLOW ARTIST"
    │      └─ Update user.follows → Streamlit state
    │
    └─→ CLOSE APP
           └─→ (Note: Changes not persisted in current demo)
```

---

## 7. IMPLEMENTATION STATUS

✅ **Completed**:
- Content-based artist recommendations
- Collaborative user similarity
- Event scoring with location
- Trending data aggregation
- Personalized trending boost

⚠️ **In Progress**:
- GraphQL API integration
- Real-time follow/attend updates
- Persistence layer

❌ **Future Enhancements**:
- Matrix factorization for collaborative filtering
- Deep learning embeddings
- Real-time interaction tracking
- A/B testing framework

---

*Last Updated: February 25, 2026*
