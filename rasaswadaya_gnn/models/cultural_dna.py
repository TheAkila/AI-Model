"""
Cultural DNA Mapping Module
===========================
Converts cultural metadata into explainable feature vectors.
This is the semantic grounding layer that makes the GNN explainable.
"""

import numpy as np
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from config import get_config
from data.cultural_constants import SRI_LANKAN_CULTURAL_TAXONOMY


@dataclass
class CulturalDNAVector:
    """Represents a Cultural DNA fingerprint."""
    vector: np.ndarray
    dimensions: Dict[str, List[float]]  # Dimension name -> values
    metadata: Dict[str, Any]
    
    def __repr__(self):
        return f"CulturalDNA(dims={len(self.vector)}, metadata={list(self.metadata.keys())})"


class CulturalDNAEncoder:
    """
    Encodes cultural metadata into multi-dimensional feature vectors.
    
    The Cultural DNA vector captures:
    - Art form (dance, music, drama, etc.)
    - Sub-genre (kandyan, baila, kolam, etc.)
    - Language (Sinhala, Tamil, English, mixed)
    - Region (Western, Central, Southern, etc.)
    - Cultural category (traditional, contemporary, fusion)
    - Mood/Vibe (celebratory, spiritual, energetic)
    - Festival alignment (Vesak, New Year, Perahera, etc.)
    
    This creates an explainable feature space where similarity is interpretable.
    """
    
    def __init__(self):
        self.config = get_config()
        self.taxonomy = SRI_LANKAN_CULTURAL_TAXONOMY
        
        # Build vocabulary for each dimension
        self._build_vocabularies()
        
    def _build_vocabularies(self):
        """Build index mappings for all cultural dimensions."""
        cfg = self.config.cultural_dna
        
        # Art forms
        self.art_form_vocab = {af: i for i, af in enumerate(cfg.art_forms)}
        
        # Styles (combined from all art forms)
        all_styles = set()
        all_styles.update(cfg.music_styles)
        all_styles.update(cfg.dance_styles)
        all_styles.update(cfg.film_styles)
        all_styles.update(cfg.drama_styles)
        self.subgenre_vocab = {sg: i for i, sg in enumerate(sorted(all_styles))}
        
        # Languages
        self.language_vocab = {lang: i for i, lang in enumerate(cfg.languages)}
        
        # Regions
        self.region_vocab = {reg: i for i, reg in enumerate(cfg.regions)}
        
        # Cultural categories
        self.category_vocab = {cat: i for i, cat in enumerate(cfg.cultural_categories)}
        
        # Moods
        self.mood_vocab = {mood: i for i, mood in enumerate(cfg.moods)}
        
        # Festivals
        self.festival_vocab = {fest: i for i, fest in enumerate(cfg.festivals)}
        
        # Calculate total dimensions
        self.total_dims = (
            len(self.art_form_vocab) +
            len(self.subgenre_vocab) +
            len(self.language_vocab) +
            len(self.region_vocab) +
            len(self.category_vocab) +
            len(self.mood_vocab) +
            len(self.festival_vocab)
        )
        
    def encode_artist(self, artist_metadata: Dict[str, Any]) -> CulturalDNAVector:
        """
        Encode an artist's cultural profile into a DNA vector.
        
        Note: Artist region/city is NOT encoded for recommendations.
        Artist location is stored in metadata but not used for similarity calculations.
        This is because recommendations should be based on artistic style/genres/mood,
        not geographic location. Location filtering happens at event level instead.
        
        Args:
            artist_metadata: Dict with keys:
                - art_forms: List[str]
                - genres: List[str]
                - language: str or List[str]
                - style: str (traditional/contemporary/fusion)
                - mood_tags: List[str]
        
        Returns:
            CulturalDNAVector with encoded features (58D: art_forms + genres + languages + style + mood + festivals)
        """
        vector = np.zeros(self.total_dims, dtype=np.float32)
        dimensions = {}
        offset = 0
        
        # Encode art forms (multi-hot)
        art_forms = artist_metadata.get('art_forms', [])
        if isinstance(art_forms, str):
            art_forms = [art_forms]
        art_form_vec = np.zeros(len(self.art_form_vocab))
        for af in art_forms:
            if af in self.art_form_vocab:
                art_form_vec[self.art_form_vocab[af]] = 1.0
        if art_form_vec.sum() > 0:
            art_form_vec /= art_form_vec.sum()  # Normalize
        vector[offset:offset+len(art_form_vec)] = art_form_vec
        dimensions['art_forms'] = art_form_vec.tolist()
        offset += len(art_form_vec)
        
        # Encode sub-genres (multi-hot)
        genres = artist_metadata.get('genres', [])
        if isinstance(genres, str):
            genres = [genres]
        genre_vec = np.zeros(len(self.subgenre_vocab))
        for g in genres:
            if g in self.subgenre_vocab:
                genre_vec[self.subgenre_vocab[g]] = 1.0
        if genre_vec.sum() > 0:
            genre_vec /= genre_vec.sum()  # Normalize
        vector[offset:offset+len(genre_vec)] = genre_vec
        dimensions['genres'] = genre_vec.tolist()
        offset += len(genre_vec)
        
        # Encode language (multi-hot for multilingual artists)
        languages = artist_metadata.get('language', 'sinhala')
        if isinstance(languages, str):
            languages = [languages]
        lang_vec = np.zeros(len(self.language_vocab))
        for lang in languages:
            if lang in self.language_vocab:
                lang_vec[self.language_vocab[lang]] = 1.0
        if lang_vec.sum() > 0:
            lang_vec /= lang_vec.sum()
        vector[offset:offset+len(lang_vec)] = lang_vec
        dimensions['languages'] = lang_vec.tolist()
        offset += len(lang_vec)
        
        # NOTE: Artist region/city is NOT encoded here.
        # Artist location is not relevant for artist-to-user recommendations.
        # Location-based filtering happens at the event level instead.
        # This improves recommendation quality by focusing on artistic attributes.
        
        # Encode cultural category (multi-hot)
        categories = artist_metadata.get('style', ['traditional'])
        if isinstance(categories, str):
            categories = [categories]
        cat_vec = np.zeros(len(self.category_vocab))
        for cat in categories:
            if cat in self.category_vocab:
                cat_vec[self.category_vocab[cat]] = 1.0
        if cat_vec.sum() > 0:
            cat_vec /= cat_vec.sum()
        vector[offset:offset+len(cat_vec)] = cat_vec
        dimensions['categories'] = cat_vec.tolist()
        offset += len(cat_vec)
        
        # Encode moods (multi-hot)
        moods = artist_metadata.get('mood_tags', [])
        if isinstance(moods, str):
            moods = [moods]
        mood_vec = np.zeros(len(self.mood_vocab))
        for mood in moods:
            if mood in self.mood_vocab:
                mood_vec[self.mood_vocab[mood]] = 1.0
        if mood_vec.sum() > 0:
            mood_vec /= mood_vec.sum()
        vector[offset:offset+len(mood_vec)] = mood_vec
        dimensions['moods'] = mood_vec.tolist()
        offset += len(mood_vec)
        
        # Encode festival alignment (multi-hot)
        festivals = artist_metadata.get('festivals', [])
        if isinstance(festivals, str):
            festivals = [festivals]
        fest_vec = np.zeros(len(self.festival_vocab))
        for fest in festivals:
            if fest in self.festival_vocab:
                fest_vec[self.festival_vocab[fest]] = 1.0
        if fest_vec.sum() > 0:
            fest_vec /= fest_vec.sum()
        vector[offset:offset+len(fest_vec)] = fest_vec
        dimensions['festivals'] = fest_vec.tolist()
        offset += len(fest_vec)
        
        return CulturalDNAVector(
            vector=vector,
            dimensions=dimensions,
            metadata=artist_metadata
        )
    
    def encode_event(self, event_metadata: Dict[str, Any]) -> CulturalDNAVector:
        """
        Encode an event's cultural profile.
        
        Args:
            event_metadata: Dict with keys:
                - genres: List[str] (DERIVED from performing artists)
                - art_forms: List[str] (DERIVED from performing artists)
                - language: List[str] (DERIVED from performing artists)
                - style: List[str] (DERIVED from performing artists)
                - mood_tags: List[str] (DERIVED from performing artists)
                - festivals: List[str] (DERIVED from performing artists)
                - venue: str
                - festival: str (optional specific festival)
        
        Returns:
            CulturalDNAVector
            
        Note: Event cultural profile is the UNION of all performing artists' profiles.
        This ensures semantic consistency: an event featuring Kandyan + Baila dancers
        has both Kandyan and Baila as its genres.
        """
        # Events inherit cultural profile from their artists/genres
        # The genres are already combined during data generation
        vector_data = event_metadata.copy()
        
        # If event is part of a festival, boost that festival dimension
        if 'festival' in event_metadata and event_metadata['festival']:
            festivals = vector_data.get('festivals', [])
            if isinstance(festivals, str):
                festivals = [festivals]
            if event_metadata['festival'] not in festivals:
                festivals.append(event_metadata['festival'])
            vector_data['festivals'] = festivals
        
        return self.encode_artist(vector_data)  # Same encoding logic
    
    def encode_user(self, user_interaction_history: List[Dict[str, Any]]) -> CulturalDNAVector:
        """
        Encode a user's cultural preferences from interaction history.
        
        Args:
            user_interaction_history: List of dicts with:
                - type: 'artist' or 'event'
                - metadata: cultural metadata
                - weight: interaction strength (1.0 for follow, 0.5 for like, etc.)
        
        Returns:
            CulturalDNAVector representing user preferences
        """
        if not user_interaction_history:
            # Cold start user - return neutral vector
            return CulturalDNAVector(
                vector=np.zeros(self.total_dims, dtype=np.float32),
                dimensions={},
                metadata={'type': 'user', 'cold_start': True}
            )
        
        # Aggregate cultural DNA from interactions
        weighted_sum = np.zeros(self.total_dims, dtype=np.float32)
        total_weight = 0.0
        
        for interaction in user_interaction_history:
            metadata = interaction.get('metadata', {})
            weight = interaction.get('weight', 1.0)
            
            if interaction.get('type') == 'artist':
                dna = self.encode_artist(metadata)
            else:  # event
                dna = self.encode_event(metadata)
            
            weighted_sum += dna.vector * weight
            total_weight += weight
        
        # Average the weighted vectors
        if total_weight > 0:
            user_vector = weighted_sum / total_weight
        else:
            user_vector = weighted_sum
        
        return CulturalDNAVector(
            vector=user_vector,
            dimensions={},  # Could break down dimensions if needed
            metadata={'type': 'user', 'num_interactions': len(user_interaction_history)}
        )
    
    def get_dimension_names(self) -> List[str]:
        """Get human-readable dimension names."""
        names = []
        for af in self.art_form_vocab.keys():
            names.append(f"art_form:{af}")
        for sg in self.subgenre_vocab.keys():
            names.append(f"genre:{sg}")
        for lang in self.language_vocab.keys():
            names.append(f"language:{lang}")
        for reg in self.region_vocab.keys():
            names.append(f"region:{reg}")
        for cat in self.category_vocab.keys():
            names.append(f"category:{cat}")
        for mood in self.mood_vocab.keys():
            names.append(f"mood:{mood}")
        for fest in self.festival_vocab.keys():
            names.append(f"festival:{fest}")
        return names


def compute_cultural_similarity(
    dna1: CulturalDNAVector,
    dna2: CulturalDNAVector,
    method: str = "cosine"
) -> Tuple[float, Dict[str, float]]:
    """
    Compute similarity between two Cultural DNA vectors.
    
    Args:
        dna1, dna2: Cultural DNA vectors to compare
        method: "cosine" or "euclidean"
    
    Returns:
        (overall_similarity, dimension_breakdown)
        - overall_similarity: float in [0, 1]
        - dimension_breakdown: dict of dimension-level similarities
    """
    if method == "cosine":
        # Cosine similarity
        dot_product = np.dot(dna1.vector, dna2.vector)
        norm1 = np.linalg.norm(dna1.vector)
        norm2 = np.linalg.norm(dna2.vector)
        
        if norm1 == 0 or norm2 == 0:
            overall_sim = 0.0
        else:
            overall_sim = dot_product / (norm1 * norm2)
        
        # Ensure in [0, 1] range (cosine can be [-1, 1])
        overall_sim = (overall_sim + 1.0) / 2.0
        
    else:  # euclidean
        distance = np.linalg.norm(dna1.vector - dna2.vector)
        # Convert distance to similarity in [0, 1]
        overall_sim = 1.0 / (1.0 + distance)
    
    # Dimension-level breakdown (if available)
    dimension_sims = {}
    if dna1.dimensions and dna2.dimensions:
        for dim_name in dna1.dimensions.keys():
            if dim_name in dna2.dimensions:
                vec1 = np.array(dna1.dimensions[dim_name])
                vec2 = np.array(dna2.dimensions[dim_name])
                
                # Cosine similarity for this dimension
                if vec1.sum() == 0 or vec2.sum() == 0:
                    dim_sim = 0.0
                else:
                    dot = np.dot(vec1, vec2)
                    norm1 = np.linalg.norm(vec1)
                    norm2 = np.linalg.norm(vec2)
                    if norm1 > 0 and norm2 > 0:
                        dim_sim = dot / (norm1 * norm2)
                        dim_sim = (dim_sim + 1.0) / 2.0
                    else:
                        dim_sim = 0.0
                
                dimension_sims[dim_name] = float(dim_sim)
    
    return float(overall_sim), dimension_sims


def explain_similarity(
    dna1: CulturalDNAVector,
    dna2: CulturalDNAVector,
    encoder: CulturalDNAEncoder,
    top_k: int = 3
) -> str:
    """
    Generate human-readable explanation for why two cultural profiles are similar.
    
    Args:
        dna1, dna2: Cultural DNA vectors
        encoder: CulturalDNAEncoder instance
        top_k: Number of top dimensions to mention
    
    Returns:
        Human-readable explanation string
    """
    overall_sim, dim_sims = compute_cultural_similarity(dna1, dna2)
    
    # Sort dimensions by similarity
    sorted_dims = sorted(dim_sims.items(), key=lambda x: x[1], reverse=True)
    
    # Build explanation
    explanation = f"Overall similarity: {overall_sim:.1%}\n\n"
    explanation += "Key matching dimensions:\n"
    
    for i, (dim_name, sim) in enumerate(sorted_dims[:top_k]):
        if sim > 0.3:  # Only mention significant similarities
            explanation += f"  {i+1}. {dim_name.upper()}: {sim:.1%} match\n"
    
    return explanation


if __name__ == "__main__":
    # Demo usage
    print("=" * 60)
    print(" CULTURAL DNA ENCODER DEMO")
    print("=" * 60)
    
    encoder = CulturalDNAEncoder()
    print(f"\n✓ Encoder initialized with {encoder.total_dims} dimensions\n")
    
    # Example artist 1: Traditional Kandyan dancer
    artist1 = {
        'name': 'Chitrasena',
        'art_forms': ['dance'],
        'genres': ['kandyan', 'contemporary'],
        'language': 'sinhala',
        'region': 'central',
        'style': ['traditional', 'fusion'],
        'mood_tags': ['spiritual', 'celebratory'],
        'festivals': ['esala_perahera', 'vesak']
    }
    
    # Example artist 2: Baila musician
    artist2 = {
        'name': 'Desmond de Silva',
        'art_forms': ['music'],
        'genres': ['baila', 'contemporary'],
        'language': ['sinhala', 'english'],
        'region': 'western',
        'style': 'contemporary',
        'mood_tags': ['celebratory', 'energetic'],
        'festivals': ['christmas', 'sinhala_tamil_new_year']
    }
    
    dna1 = encoder.encode_artist(artist1)
    dna2 = encoder.encode_artist(artist2)
    
    print(f"Artist 1: {artist1['name']}")
    print(f"  DNA Vector Shape: {dna1.vector.shape}")
    print(f"  Non-zero dimensions: {np.count_nonzero(dna1.vector)}")
    
    print(f"\nArtist 2: {artist2['name']}")
    print(f"  DNA Vector Shape: {dna2.vector.shape}")
    print(f"  Non-zero dimensions: {np.count_nonzero(dna2.vector)}")
    
    print(f"\n{'-' * 60}")
    print(" SIMILARITY ANALYSIS")
    print("-" * 60)
    print(explain_similarity(dna1, dna2, encoder))
