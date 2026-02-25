# Rasaswadaya.lk GNN-Based AI Model

A Graph Neural Network model for cultural event and artist recommendations on the Rasaswadaya.lk platform.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA INPUT LAYER                            │
│  User Profiles · Artist Metadata · Events · Interactions        │
└─────────────────────────────┬───────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                                           ▼
┌───────────────────┐                   ┌───────────────────────┐
│ SOCIAL GRAPH      │                   │ CULTURAL DNA          │
│ MINING            │                   │ MAPPING               │
│ ─────────────     │                   │ ─────────────         │
│ • Graph Build     │                   │ • Art Form Encoding   │
│ • Edge Typing     │                   │ • Regional Vectors    │
│ • Community       │                   │ • Language Features   │
│   Detection       │                   │ • Mood/Season Tags    │
└─────────┬─────────┘                   └───────────┬───────────┘
          │                                         │
          │         Graph Structure                 │ Node Features
          └─────────────────┬───────────────────────┘
                            ▼
              ┌─────────────────────────┐
              │     GNN CORE ENGINE     │
              │     ─────────────────   │
              │  GraphSAGE / GAT        │
              │  2-3 Message Passing    │
              │  Layers                 │
              └───────────┬─────────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │ TEMPORAL ENHANCEMENT    │
              │ ─────────────────────   │
              │ Time-aware Embeddings   │
              └───────────┬─────────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │   DOWNSTREAM TASKS      │
              │   ────────────────      │
              │ • Link Prediction       │
              │ • Trend Detection       │
              │ • Recommendations       │
              └───────────┬─────────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │  EXPLAINABILITY LAYER   │
              │  ─────────────────────  │
              │ • GNNExplainer          │
              │ • Attention Weights     │
              │ • Cultural DNA Diff     │
              └─────────────────────────┘
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Quick Demo
```bash
python demo.py
```

### Training the Model
```bash
python train.py --epochs 100 --lr 0.01
```

### Generate Sample Data
```bash
python data/generate_sample_data.py
```

## Project Structure

```
rasaswadaya_gnn/
├── README.md
├── requirements.txt
├── config.py                 # Configuration settings
├── demo.py                   # Interactive demo script
├── train.py                  # Training pipeline
├── data/
│   ├── __init__.py
│   ├── generate_sample_data.py
│   └── cultural_constants.py # Sri Lankan cultural taxonomy
├── models/
│   ├── __init__.py
│   ├── cultural_dna.py       # Cultural DNA Mapping module
│   ├── graph_builder.py      # Heterogeneous graph construction
│   ├── gnn_model.py          # GraphSAGE/GAT implementation
│   └── temporal.py           # Temporal enhancement layer
├── tasks/
│   ├── __init__.py
│   ├── link_prediction.py    # Edge prediction task
│   ├── recommendation.py     # User-event/artist recommendations
│   └── trend_detection.py    # Emerging trend detection
└── explainability/
    ├── __init__.py
    ├── gnn_explainer.py      # GNNExplainer integration
    └── cultural_explanations.py
```

## Key Features

1. **Cultural DNA Mapping**: Explainable feature vectors encoding Sri Lankan cultural dimensions
2. **Heterogeneous Graph**: Supports multiple node types (Users, Artists, Events, Genres, Locations)
3. **GraphSAGE/GAT**: Efficient message-passing for inductive learning
4. **Explainability**: Human-readable recommendation reasons
5. **Lightweight**: Designed for academic research, not industrial scale

## Research Contribution

- Novel Cultural DNA feature space for Sri Lankan arts
- Explainable GNN recommendations on cultural platforms
- Graph-based trend detection for emerging artists/genres
- Small-scale, culturally-specific case study

## License

Academic Research Use - Rasaswadaya.lk
