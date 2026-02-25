"""
Rasaswadaya.lk GNN Model Configuration
======================================
Central configuration for the entire model pipeline.
"""

from dataclasses import dataclass, field
from typing import List, Dict
import torch


@dataclass
class CulturalDNAConfig:
    """Configuration for Cultural DNA Mapping dimensions."""
    
    # Art Form dimensions (4 Primary)
    art_forms: List[str] = field(default_factory=lambda: [
        "music", "dance", "film", "drama"
    ])
    
    # Music styles (10 major categories)
    music_styles: List[str] = field(default_factory=lambda: [
        "traditional_indigenous", "classical_semi_classical", "baila",
        "sinhala_commercial", "tamil_commercial", "hip_hop_rap",
        "rock_alternative", "devotional_religious", "fusion", "film_music"
    ])
    
    # Dance styles (9 major categories)
    dance_styles: List[str] = field(default_factory=lambda: [
        "kandyan_dance", "low_country_dance", "sabaragamuwa_dance",
        "tamil_classical", "muslim_cultural_dance", "folk_dance",
        "contemporary_modern", "urban_street", "ballroom_western"
    ])
    
    # Film styles (10 categories)
    film_styles: List[str] = field(default_factory=lambda: [
        "commercial_cinema", "art_parallel_cinema", "political_cinema",
        "historical_period", "religious_mythological", "war_films",
        "thriller_crime", "horror", "romantic", "experimental_independent"
    ])
    
    # Drama styles (5 categories)
    drama_styles: List[str] = field(default_factory=lambda: [
        "traditional_theatre", "modern_stage_drama", "teledrama",
        "musical_drama", "experimental_avant_garde"
    ])
    
    # Languages (3 Primary)
    languages: List[str] = field(default_factory=lambda: [
        "sinhala", "tamil", "english"
    ])
    
    # Regions (Sri Lankan provinces)
    regions: List[str] = field(default_factory=lambda: [
        "western", "central", "southern", "northern", "eastern",
        "north_western", "north_central", "uva", "sabaragamuwa"
    ])
    
    # Cultural categories
    cultural_categories: List[str] = field(default_factory=lambda: [
        "traditional", "contemporary", "fusion", "festival_specific",
        "ritual", "entertainment", "educational"
    ])
    
    # Mood/Vibe tags (Comprehensive - 70+ moods)
    moods: List[str] = field(default_factory=lambda: [
        # Core emotional moods
        "celebratory", "spiritual", "devotional", "patriotic", "romantic",
        "energetic", "reflective", "melancholic", "sad", "joyful",
        "peaceful", "intense", "dramatic", "emotional", "hopeful",
        "inspirational", "motivational", "serious", "dark", "mysterious",
        "suspenseful", "fearful", "tense", "angry", "aggressive",
        "powerful", "uplifting",
        # Cultural moods
        "ritualistic", "ceremonial", "heroic", "mythological", "traditional",
        "festive", "spiritual_trance", "cultural_pride", "national_pride",
        "rural_village", "urban_street", "political_awareness", "social_awareness",
        "religious_reverence", "historical_nostalgia",
        # Music-specific
        "party", "danceable", "chill", "acoustic_warm", "love_longing",
        "heartbreak", "empowerment", "meditative", "dramatic_ballad",
        "fusion_energy", "rebel",
        # Dance-specific
        "rhythmic", "theatrical", "expressive", "graceful", "fierce",
        "sacred", "competitive",
        # Film & Drama
        "suspense", "thriller_tension", "romantic_longing", "comic_relief",
        "satirical", "social_critique", "political_intensity", "war_tension",
        "tragic", "inspirational_biographical", "psychological"
    ])
    
    # Festival/Season alignment
    festivals: List[str] = field(default_factory=lambda: [
        "sinhala_tamil_new_year", "vesak", "poson", "esala_perahera",
        "deepavali", "thai_pongal", "independence_day", "christmas",
        "peradeniya_arts_festival", "galle_literary_festival"
    ])
    
    @property
    def total_dimensions(self) -> int:
        """Total dimensions in the Cultural DNA vector."""
        return (
            len(self.art_forms) +
            len(self.music_styles) +
            len(self.dance_styles) +
            len(self.film_styles) +
            len(self.drama_styles) +
            len(self.languages) +
            len(self.regions) +
            len(self.cultural_categories) +
            len(self.moods) +
            len(self.festivals)
        )


@dataclass
class GraphConfig:
    """Configuration for graph construction."""
    
    # Node types in the heterogeneous graph
    node_types: List[str] = field(default_factory=lambda: [
        "user", "artist", "event", "genre", "location"
    ])
    
    # Edge types (relations)
    edge_types: List[tuple] = field(default_factory=lambda: [
        ("user", "follows", "artist"),
        ("user", "attends", "event"),
        ("user", "likes", "genre"),
        ("artist", "performs_at", "event"),
        ("artist", "belongs_to", "genre"),
        ("artist", "based_in", "location"),
        ("event", "held_at", "location"),
        ("event", "features", "genre"),
        # Reverse edges for message passing
        ("artist", "followed_by", "user"),
        ("event", "attended_by", "user"),
        ("genre", "liked_by", "user"),
        ("event", "hosts", "artist"),
        ("genre", "includes", "artist"),
        ("location", "home_of", "artist"),
        ("location", "venue_for", "event"),
        ("genre", "featured_in", "event"),
    ])
    
    # Community detection algorithm
    community_algorithm: str = "louvain"
    
    # Minimum edges for a node to be considered active
    min_node_degree: int = 1


@dataclass
class GNNConfig:
    """Configuration for the GNN model."""
    
    # Model architecture
    model_type: str = "graphsage"  # Options: "graphsage", "gat"
    
    # Layer configuration
    num_layers: int = 2  # 2-3 layers recommended for social graphs
    hidden_channels: int = 64
    out_channels: int = 32  # Final embedding dimension
    
    # GAT-specific (if using GAT)
    num_attention_heads: int = 4
    attention_dropout: float = 0.1
    
    # Training parameters
    learning_rate: float = 0.01
    weight_decay: float = 5e-4
    dropout: float = 0.3
    
    # GraphSAGE aggregation type
    aggregation: str = "mean"  # Options: "mean", "max", "lstm"
    
    # Device configuration
    device: str = field(default_factory=lambda: "cuda" if torch.cuda.is_available() else "cpu")


@dataclass
class TemporalConfig:
    """Configuration for temporal enhancement."""
    
    # Time window for graph snapshots
    snapshot_window: str = "weekly"  # Options: "daily", "weekly", "monthly"
    
    # Number of historical snapshots to consider
    num_snapshots: int = 4
    
    # Recency weighting decay factor
    recency_decay: float = 0.9
    
    # Enable seasonal pattern encoding
    enable_seasonal: bool = True


@dataclass
class TrainingConfig:
    """Configuration for training pipeline."""
    
    # Training epochs
    epochs: int = 100
    
    # Batch size for mini-batch training
    batch_size: int = 256
    
    # Train/Val/Test split ratios
    train_ratio: float = 0.7
    val_ratio: float = 0.15
    test_ratio: float = 0.15
    
    # Early stopping
    early_stopping_patience: int = 10
    
    # Learning rate scheduler
    lr_scheduler: str = "plateau"  # Options: "plateau", "step", "cosine"
    lr_patience: int = 5
    lr_factor: float = 0.5
    
    # Negative sampling ratio for link prediction
    neg_sampling_ratio: float = 1.0
    
    # Checkpoint saving
    save_checkpoints: bool = True
    checkpoint_dir: str = "checkpoints"
    
    # Random seed for reproducibility
    random_seed: int = 42


@dataclass
class ExplainabilityConfig:
    """Configuration for explainability features."""
    
    # GNNExplainer parameters
    explainer_epochs: int = 100
    explainer_lr: float = 0.01
    
    # Number of top features to show in explanations
    top_k_features: int = 5
    
    # Attention visualization threshold
    attention_threshold: float = 0.1
    
    # Enable Cultural DNA diff in explanations
    enable_cultural_diff: bool = True


@dataclass
class RasaswadayaConfig:
    """Master configuration combining all sub-configs."""
    
    cultural_dna: CulturalDNAConfig = field(default_factory=CulturalDNAConfig)
    graph: GraphConfig = field(default_factory=GraphConfig)
    gnn: GNNConfig = field(default_factory=GNNConfig)
    temporal: TemporalConfig = field(default_factory=TemporalConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    explainability: ExplainabilityConfig = field(default_factory=ExplainabilityConfig)
    
    # Project metadata
    project_name: str = "Rasaswadaya.lk GNN Model"
    version: str = "1.0.0"


# Default configuration instance
config = RasaswadayaConfig()


def get_config() -> RasaswadayaConfig:
    """Get the default configuration."""
    return config


def print_config_summary():
    """Print a summary of the current configuration."""
    cfg = get_config()
    print(f"\n{'='*60}")
    print(f" {cfg.project_name} v{cfg.version}")
    print(f"{'='*60}")
    print(f"\n📊 Cultural DNA Dimensions: {cfg.cultural_dna.total_dimensions}")
    print(f"🔗 Node Types: {cfg.graph.node_types}")
    print(f"🧠 GNN Model: {cfg.gnn.model_type.upper()}")
    print(f"   - Layers: {cfg.gnn.num_layers}")
    print(f"   - Hidden Channels: {cfg.gnn.hidden_channels}")
    print(f"   - Output Embedding: {cfg.gnn.out_channels}")
    print(f"⏱️  Temporal Window: {cfg.temporal.snapshot_window}")
    print(f"🎯 Training Epochs: {cfg.training.epochs}")
    print(f"💻 Device: {cfg.gnn.device}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    print_config_summary()
