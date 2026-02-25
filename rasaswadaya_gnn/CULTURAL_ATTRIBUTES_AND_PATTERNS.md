# Cultural Attributes & Relationship Patterns

## Overview

The system encodes two layers of information:

1. **Cultural Attributes** - What makes an artist or user "who they are" (58D for artists, 67D for users/events)
2. **Relationship Patterns** - How users and artists connect in the graph network

Together, these are embedded into **32D embeddings** that capture compatibility.

**Note:** Artist location (region/city) is NOT encoded in cultural DNA for artist recommendations,
because recommendations should be based on artistic style, genres, and mood—not geography.
Location filtering happens at the event level instead.

---

## Part 1: Cultural Attributes (Cultural DNA)

### For Artists: 6 Dimensions (58D total)

Artists are encoded WITHOUT geographic location:
- Art Forms (7D)
- Sub-Genres (25D)
- Languages (5D)
- Cultural Category/Style (3D)
- Mood/Vibe (8D)
- Festival Alignment (11D)

**Why no region for artists?** Artist location is irrelevant for recommending them to users.
Recommendations are based on artistic style, genres, and mood. Geographic filtering happens
at the event level (where events are held) instead.

### For Users/Events: 7 Dimensions (67D total)

Users and events include geographic location because it affects event attendance decisions.

---

### The 6 Cultural Dimensions (Artist View)

#### 1. **Art Forms** (7 dimensions)
What type of art the artist performs or user enjoys:
- Dance
- Music
- Drama
- Literature
- Visual Arts
- Crafts
- Martial Arts

**Example:**
- Artist "Chitrasena": [1, 0, 0, 0, 0, 0, 0] → Dance specialist
- User "Madhavi": [0.5, 0, 0, 0.5, 0, 0, 0] → Likes dance & literature

**Encoding:** Multi-hot (can have multiple art forms)

---

#### 2. **Sub-Genres** (~25 dimensions)
Specific genres within each art form:

**Dance Genres:**
- Kandyan (classical up-country)
- Low Country (coastal ritual)
- Sabaragamuwa (province specific)
- Folk
- Contemporary
- Bharatanatyam (Tamil classical)
- Fusion

**Music Genres:**
- Classical Sinhala
- Baila (party music)
- Elle (work songs)
- Folk Music
- Devotional Buddhist
- Devotional Hindu
- Carnatic (South Indian)

**Drama Genres:**
- Classical Sinhala drama
- Contemporary plays
- Street theatre
- Kolam (mask drama)
- Sokari (comedy)
- Morality plays

**Example:**
- Artist "Ravi": Strong in [Kandyan, Devotional] → Classical dancer
- User "Amani": Interested in [Baila, Contemporary] → Party music lover

**Encoding:** Multi-hot, normalized (proportions sum to 1)

---

#### 3. **Languages** (5 dimensions)
Primary languages of performance/understanding:
- Sinhala
- Tamil
- English
- Mixed Sinhala-English
- Mixed Tamil-English

**Example:**
- Artist "Thilini": [1, 0, 0, 0, 0] → Sinhala only
- User "Priya": [0, 0.5, 0, 0, 0.5] → Tamil + Mixed Tamil-English

**Encoding:** Multi-hot (multilingual artists normalized)

---

#### 4. **Cultural Category/Style** (3 dimensions)
How the art is presented:
- Traditional (adheres to ancient forms)
- Contemporary (modern interpretation)
- Fusion (blend of styles)

**Example:**
- Artist "Sampath": [1, 0, 0] → Pure traditional kandyan
- Artist "Indika": [0.33, 0.33, 0.33] → Mix of traditional, contemporary, fusion

**Encoding:** Multi-hot, normalized

---

#### 5. **Mood/Vibe** (~8 dimensions)
The emotional/spiritual quality:
- Celebratory
- Spiritual
- Energetic
- Meditative
- Intellectual
- Romantic
- Playful
- Serene

**Example:**
- Artist "Tharindu" (Perahera performer): [1, 1, 0.5, 0.5, 0, 0, 0, 0] → Celebratory + Spiritual
- Artist "Deepika" (Classical): [0, 0.8, 0, 0.8, 0.4, 0, 0, 0] → Spiritual + Meditative + Intellectual

**Encoding:** Multi-hot, normalized

---

#### 6. **Festival Alignment** (~11 dimensions)
Which festivals/occasions the artist is associated with:
- Vesak (Buddhist full moon)
- New Year (Sinhala & Tamil)
- Perahera (Kandy festival)
- Sinhala New Year
- Hindu Deepavali
- Thai Pongal
- Independence Day
- Christmas
- Easter
- Nuzul-ul-Quran (Islamic)
- Id (Islamic)

**Example:**
- Artist "Perahera Troupe": [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0] → Perahera + Sinhala New Year
- Artist "Yohani": [0, 0, 0, 0, 0, 0, 0.33, 0.33, 0.33, 0, 0] → Christmas + Independence + New Year

**Encoding:** Multi-hot, normalized

---

## Summary: Cultural DNA Vector for Artists

**Total Dimensions: 58**
```
[Art Forms (7) | Genres (25) | Languages (5) | Style (3) | Mood (8) | Festivals (11)]

Note: Region/City NOT included for artists (recommendations based on artistic attributes, not location)

Each dimension is either:
- Multi-hot: [0, 1, 0, 1, ...] with normalization
- One-hot: [0, 0, 1, 0, ...] (exactly one 1.0)
```

**Example Vector for "Chathura Rajapaksa":**
```
Art Forms:    [0, 1, 0, 0, 0, 0, 0]           → Dance
Genres:       [1, 0, 0, ..., 0]                → Kandyan
Languages:    [1, 0, 0, 0, 0]                  → Sinhala
Style:        [1, 0, 0]                        → Traditional
Mood:         [0.5, 0.5, 0, 0, 0, 0, 0, 0]   → Celebratory + Spiritual
Festivals:    [0, 0.5, 0.5, 0, 0, ...]        → Perahera + New Year

(Region removed - not needed for artist recommendations)
```

---

## Cultural DNA Vector for Users/Events (67D with Region)

When region IS needed (users for distance, events for location), the full 67D is used:
```
[Art Forms (7) | Genres (25) | Languages (5) | Region (9) | Style (3) | Mood (8) | Festivals (11)]
```
Style:        [1, 0, 0]                        → Traditional
Mood:         [0.5, 0.5, 0, 0, 0, 0, 0, 0]   → Celebratory + Spiritual
Festivals:    [0, 0.5, 0.5, 0, 0, ...]        → Perahera + New Year
```

---

## Part 2: Relationship Patterns in the Graph

### Graph Structure

```
                    USERS (150 nodes)
                           |
                  follows (1238 edges)
                           ↓↑
                    ARTISTS (60 nodes)
                      /         \
         performs_at (178)   belongs_to (78)
                    /             \
                   ↓               ↓
            EVENTS (120)       GENRES (16)
                    |          /
            held_at (120)     /
                    |        /
                    ↓       ↓
              LOCATIONS (9+)
```

### Edge Types & Relationship Patterns

#### 1. **User → follows → Artist** (1238 edges)
**What it means:** User has explicitly followed an artist

**Patterns the GNN learns:**
- Users with similar follow lists get similar embeddings
- Artists followed by many similar users get boosted
- If User A and User B both follow Artist X, and User A follows Artist Y, then Artist Y is recommended to User B

**Example:**
```
User "Madhavi" follows:
  - Chathura Rajapaksa (kandyan specialist)
  - H.R. Jothipala (classical music)
  - Sachini Dissanayake (fusion)

System learns:
  "Madhavi likes: traditional dance + classical + some fusion"
  
Recommendation:
  "Other users who like this combination also follow these artists..."
  → Nalaka (kandyan + fusion)
  → Gayan (traditional dance)
```

---

#### 2. **Artist → performs_at → Event** (178 edges)
**What it means:** Artist is performing at an event

**Patterns the GNN learns:**
- Events with many similar artists are grouped together
- Users who like certain artists → likely to attend events with those artists
- Events by the same artist or similar artists form event clusters

**Example:**
```
Artist "Dilini De Silva" performs at:
  - "Celebration of Dilini De Silva" (Ratnapura)
  - "Evening with Dilini De Silva" (Ratnapura)
  - "Night of Dilini De Silva" (Ratnapura)

System learns:
  "If you follow Dilini, you should attend these events"
```

---

#### 3. **Artist → belongs_to → Genre** (78 edges)
**What it means:** Artist specializes in a genre

**Patterns the GNN learns:**
- Artists in same genres are similar
- Users interested in a genre → should follow artists in that genre
- Genres form clusters (e.g., all kandyan artists grouped together)

**Example:**
```
Artists in "Kandyan" genre:
  - Chathura Rajapaksa
  - Upeka Amarasinghe
  - Sampath Mahasinghe
  
System learns:
  "These artists are similar → recommend them together"
```

---

#### 4. **Event → features → Genre** (199 edges)
**What it means:** Event includes a specific genre

**Patterns the GNN learns:**
- Events with similar genre combinations are similar
- Users who like certain genres → should attend events with those genres
- Multi-genre events are positioned between single-genre clusters

**Example:**
```
Event "Kandyan + Baila Night" features:
  - Kandyan (traditional)
  - Baila (party music)
  
System learns:
  "This event appeals to both traditional + party music lovers"
```

---

#### 5. **Event → held_at → Location** (120 edges)
**What it means:** Event takes place in a location/city

**Patterns the GNN learns:**
- Distance between user and event matters
- Users tend to attend events in their city/region
- Events in same location form clusters

**Example:**
```
Events in "Ratnapura":
  - Celebration of Dilini De Silva
  - Evening with Ravi De Silva
  - Night of Mahela Perera

System learns:
  "Users in Ratnapura should see these events first"
```

---

## Part 3: How Embeddings Capture Both

### The 32D Embedding

When the GNN processes the graph, it produces **32-dimensional embeddings** for each node.

These 32D embeddings capture:

```
User Embedding (32D):
├─ Cultural preferences (from Cultural DNA)
│  └─ Likes: [Kandyan, Baila, Spiritual, Meditative]
├─ Follow patterns (from graph structure)
│  └─ "Users like me follow these artists"
├─ Discovered clusters
│  └─ "I'm in cluster with other Colombo-based users who like fusion"
└─ Learned relationships
   └─ "Artists in my cluster usually perform at these venues"

Artist Embedding (32D):
├─ Cultural profile (from Cultural DNA)
│  └─ Performs: [Kandyan, Traditional, Celebratory]
├─ Follower patterns (who follows them)
│  └─ "I'm followed by users interested in traditional dance"
├─ Performance patterns (where/when they perform)
│  └─ "I usually perform at cultural festivals"
└─ Collaboration patterns
   └─ "I often perform with these other artists"
```

### Similarity Calculation

```
Recommendation Score = similarity(User_Embedding, Artist_Embedding)

Similarity captures:
1. Cultural match: Do their attributes align?
2. Pattern match: Do users like me follow artists like them?
3. Indirect connections: Are there multi-hop paths?
4. Cluster membership: Are we in the same community?
```

---

## Example: Tracing a Recommendation

### User: Madhavi (U0003)
**Cultural DNA:**
- Art Forms: Dance
- Genres: Kandyan, Baila
- Languages: Sinhala
- Region: Ratnapura (Sabaragamuwa)
- Style: Traditional
- Mood: Celebratory
- Festivals: Vesak, New Year

**Follow History:**
- Chathura Rajapaksa (Kandyan dancer)
- H.R. Jothipala (Classical musician)
- Sachini Dissanayake (Fusion artist)

### Artist: Gayan Senanayake (A0234)
**Cultural DNA:**
- Art Forms: Dance
- Genres: Kandyan, Contemporary
- Languages: Sinhala, English
- Region: Anuradhapura (North Central)
- Style: Traditional + Contemporary
- Mood: Energetic, Spiritual
- Festivals: Perahera, Vesak

**Performance History:**
- Performs at: [Perahera events, Cultural festivals]
- Followed by: [Users who like traditional dance]

### How Embeddings Connect Them:

```
Step 1: Cultural DNA Match
  Madhavi likes: Kandyan, Traditional
  Gayan performs: Kandyan, Traditional
  → 80% cultural match

Step 2: Follow Pattern Match
  Users similar to Madhavi (like traditional dance):
    - User X follows: [Kandyan artist 1, Kandyan artist 2, Gayan]
    - User Y follows: [Kandyan artist 3, Gayan]
  → Gayan frequently followed by users like Madhavi
  → Pattern match score: 75%

Step 3: Collaborative Signal
  Artists similar to Madhavi's follows:
    - Chathura (Madhavi follows) similar to Gayan (both Kandyan)
    - Both perform at cultural festivals
  → Collaborative filtering boost: +10%

Step 4: Community Detection
  Both in "Traditional Kandyan Enthusiasts" community
  → Community match: 85%

FINAL EMBEDDING SIMILARITY: 0.83
→ Gayan is high-quality recommendation for Madhavi!
```

---

## Dimension Reductions

### From 58D (artist) to 32D Embedding

The GNN learns to compress artist cultural DNA into 32-dimensional embeddings:

```
58D Artist Cultural DNA (no region):
├─ Explicit cultural information
├─ Genres, moods, festivals, style
├─ But contains redundancy
└─ No relationship/graph information

                    ↓ GNN Processing ↓

32D Embedding:
├─ Core cultural patterns (compressed)
├─ Relationship patterns (who follows whom)
├─ Graph neighborhoods (indirect connections)
├─ Community structure (taste clusters)
└─ Learned compatibility factors
```
├─ Explicit cultural information
├─ But contains redundancy
└─ No relationship/graph information

                    ↓ GNN Processing ↓

32D Embedding:
├─ Core cultural patterns (compressed)
├─ Relationship patterns (who connects to whom)
├─ Graph neighborhoods (2-hop connections)
├─ Community structure
└─ Learned compatibility factors
```

**What information is preserved:**
- Genre preferences (essential)
- Cultural style (essential)
- Region (kept via location edges)
- Mood/vibe (implicitly in neighbor patterns)

**What information is transformed:**
- Raw attribute counts → compressed patterns
- Follow history → position in graph space
- Genre memberships → cluster locations

---

## Key Insights

### 1. **Cultural Similarity ≠ Recommendation Score**
```
Two kandyan dancers might be very similar culturally,
but if no one in Madhavi's community follows them,
recommendation score is lower.
```

### 2. **Graph Patterns Trump Content**
```
If 100 users similar to Madhavi follow Artist X,
Artist X gets recommended even if not a perfect cultural match.
```

### 3. **Embeddings Learn "Taste Clusters"**
```
The GNN discovers:
- Users who like [Kandyan + Spiritual] → 32D cluster A
- Users who like [Baila + Energetic] → 32D cluster B
- Users who like [Fusion + Intellectual] → 32D cluster C

Artist positions in these clusters determine recommendations.
```

### 4. **Relationship Patterns are Learned, Not Explicit**
```
You don't tell the system:
  "Users in Colombo like modern dance"
  
It learns this from:
  - Graph structure (who follows whom)
  - Cultural DNA (what they encode)
  - Message passing (aggregating neighbor patterns)
```

---

## Visualization

### Cultural Space
```
Traditional ←──────────────→ Contemporary
     ↑
     │
  Spiritual
     │
     ├─ Kandyan (Chathura, Sampath)
     ├─ Classical (H.R. Jothipala, Deepika)
     └─ Devotional (Spiritual music performers)
     
Energetic
     │
     ├─ Baila (Party music)
     ├─ Folk (Banda, Goyam)
     └─ Fusion (Modern interpretations)
```

### Graph Space (32D projected to 2D)
```
User Madhavi • (Ratnapura, Traditional, Kandyan)
              │
              ├─ Artist Chathura • (Kandyan specialist)
              ├─ Artist Gayan • (Similar profile)
              └─ Artist Nalaka • (Fusion kandyan)
              
User Amani • (Colombo, Energetic, Baila)
            │
            ├─ Artist Yohani • (Pop-baila fusion)
            └─ Artist Kasun • (Party music)
```

---

## Conclusion

**Cultural Attributes** define what users and artists are (their identity).

**Relationship Patterns** define how they connect (their context).

**Embeddings** combine both to create a compressed representation where:
- Similar users are close in embedding space
- Recommended artists are positioned nearby in the same space
- The GNN learns to position them optimally based on training data

This is why the system can make personalized, contextual recommendations that go beyond simple attribute matching.
