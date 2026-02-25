# Rasaswadaya Streamlit UI

A simple, beautiful UI for the GNN-based cultural artist and event recommendation system.

## Features

- 🎨 **Artist Recommendations** - Personalized artist suggestions based on user interests
- 🎪 **Event Recommendations** - Location-aware event suggestions with distance
- 📈 **Trending Section** - Top trending artists and events
- 🔄 **User Selection** - Choose specific user or random selection
- 📱 **Responsive Design** - Works on desktop and tablet

## Quick Start

### 1. Install Dependencies

```bash
cd /Users/akilanishan/Desktop/AI\ Model/rasaswadaya_gnn/streamlit_app
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app will open at: `http://localhost:8501`

## Project Structure

```
streamlit_app/
├── app.py                    ← Main Streamlit app
├── requirements.txt          ← Python dependencies
├── utils/
│   ├── __init__.py
│   ├── recommender.py        ← Backend connector (calls GNN model)
│   ├── data_loader.py        ← Load dataset from pickle/CSV
│   └── helpers.py            ← Data formatting functions
└── .streamlit/
    └── config.toml           ← Streamlit configuration
```

## How It Works

1. **User Selection** - Select a user from dropdown or random
2. **Load Recommendations** - Fetch artist & event recommendations
3. **Display Results** - Show top 5 in each category
4. **Trending** - Display trending artists & events in sidebar
5. **Interact** - View profiles or take actions (Follow/Attend)

## Three-Column Layout

```
┌─────────────────────────────────────────────────────┐
│ 🎭 RASASWADAYA                                       │
│ [Select User] [Random] [Refresh]                    │
└─────────────────────────────────────────────────────┘

┌────────────────┬──────────────────┬─────────────────┐
│ 🎨 ARTISTS     │ 🎪 EVENTS        │ 📈 TRENDING     │
├────────────────┼──────────────────┼─────────────────┤
│ Top 5 Artists  │ Top 5 Events     │ Top Artists    │
│ with scores    │ with distance    │ Top Events     │
│ [View][Follow] │ [View][Attend]   │ [Show More]    │
└────────────────┴──────────────────┴─────────────────┘
```

## Features Explained

### Artist Recommendations
- **Name**: Artist name
- **Score**: Compatibility score (0-1)
- **Rating**: Star rating (0-5 stars)
- **Genre**: Primary genre/style
- **Mood**: Emotional vibe of the art
- **Buttons**: View profile or Follow

### Event Recommendations
- **Name**: Event name
- **Distance**: Distance from user's city
- **Date**: Event date
- **Genre**: Type of event
- **Artists**: Number of performing artists
- **Buttons**: View details or Mark Attend

### Trending
- **Artists**: Top artists by follow count
- **Events**: Top events by attendee count
- **Progress bars**: Visual representation of popularity

## Customization

### Change Colors
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#1f77b4"      ← Change to your color
backgroundColor = "#ffffff"
```

### Change Number of Results
Edit `app.py`:
```python
num_artists = len(recommendations['artists']) if not st.session_state.show_more_artists else 10  # Change 10 to desired number
```

### Adjust Recommendation Algorithm
Edit `utils/recommender.py`:
- `calculate_artist_score()` - Adjust artist scoring
- `calculate_event_score()` - Adjust event scoring
- Distance weighting, genre matching, etc.

## Troubleshooting

### App won't start
```bash
# Clear cache
streamlit cache clear

# Try running again
streamlit run app.py
```

### No recommendations showing
- Ensure dataset is generated: `python ../data/generate_sample_data.py`
- Check pickle file exists: `../data/sample_dataset/rasaswadaya_dataset.pkl`
- Check model is trained: `../checkpoints/best_model.pt`

### Slow performance
- Streamlit caches data - first load is slower
- Subsequent loads are instant
- Refresh button clears cache if needed

## Deployment

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repo
4. Select `streamlit_app/app.py` as main file
5. Deploy!

### Docker

```bash
# Create Dockerfile
docker build -t rasaswadaya-ui .
docker run -p 8501:8501 rasaswadaya-ui
```

### Heroku

```bash
# Create Procfile
echo "web: streamlit run streamlit_app/app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
git push heroku main
```

## API Reference

### recommender.py

```python
# Get recommendations for a user
recommendations = get_recommendations(user_data)
# Returns: {'artists': [...], 'events': [...]}

# Get trending data
trending = get_trending_data()
# Returns: {'artists': [...], 'events': [...]}
```

### data_loader.py

```python
# Load all data
users, artists, events, follows, attends = load_dataset()

# Get users list (formatted for UI)
users_list = load_users_list()

# Get specific user
user = get_user_by_name("Madhavi Rajapaksa")
```

## Performance

- **Load Time**: ~2 seconds (first run), <1 second (cached)
- **Recommendation Generation**: ~500ms per user
- **Trending Calculation**: ~200ms
- **UI Rendering**: <100ms

## Future Enhancements

- [ ] User profile page with more details
- [ ] Artist detail page
- [ ] Event calendar view
- [ ] User ratings/feedback
- [ ] Share recommendations
- [ ] Admin panel to manage data
- [ ] Real-time updates
- [ ] Mobile app

## Support

For issues or suggestions, open an issue on GitHub.

---

**Built with ❤️ using Streamlit and Graph Neural Networks**
