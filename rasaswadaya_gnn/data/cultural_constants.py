"""
Sri Lankan Cultural Taxonomy - UPDATED 2026
============================================
Comprehensive taxonomy focusing on 4 main art forms:
Music, Dance, Film, and Drama
"""

SRI_LANKAN_CULTURAL_TAXONOMY = {
    # =========================================================================
    # ART FORMS (4 Primary Categories)
    # =========================================================================
    "art_forms": {
        "music": {
            "description": "All music genres from traditional to contemporary",
            "styles": {
                "traditional_indigenous": {
                    "description": "Traditional and indigenous music",
                    "sub_genres": [
                        "virindu", "vannam", "kolam_songs", "nadagam_music",
                        "raban_music", "jana_kavi", "harvest_songs", 
                        "ritual_tovil_music", "sanni_yakuma_music"
                    ]
                },
                "classical_semi_classical": {
                    "description": "Classical music traditions",
                    "sub_genres": [
                        "sinhala_classical", "carnatic_sri_lankan_tamil",
                        "light_classical", "classical_vocal", "classical_instrumental"
                    ]
                },
                "baila": {
                    "description": "Baila music - Afro-Portuguese influenced",
                    "sub_genres": [
                        "traditional_baila", "modern_baila", "party_baila"
                    ]
                },
                "sinhala_commercial": {
                    "description": "Modern Sinhala commercial music",
                    "sub_genres": [
                        "sinhala_pop", "dance_pop", "acoustic_pop",
                        "ballads", "love_songs", "sad_songs"
                    ]
                },
                "tamil_commercial": {
                    "description": "Sri Lankan Tamil commercial music",
                    "sub_genres": [
                        "tamil_pop", "tamil_melody", "tamil_rap", "gaana_style"
                    ]
                },
                "hip_hop_rap": {
                    "description": "Urban hip-hop and rap",
                    "sub_genres": [
                        "sinhala_rap", "tamil_rap", "trap", "drill"
                    ]
                },
                "rock_alternative": {
                    "description": "Rock and alternative music",
                    "sub_genres": [
                        "sinhala_rock", "tamil_rock", "hard_rock",
                        "alternative_rock", "metal"
                    ]
                },
                "devotional_religious": {
                    "description": "Religious and devotional music",
                    "sub_genres": [
                        "buddhist_devotional", "bhakti_songs",
                        "catholic_hymns", "islamic_nasheed"
                    ]
                },
                "fusion": {
                    "description": "Fusion and experimental music",
                    "sub_genres": [
                        "folk_fusion", "classical_fusion",
                        "ethnic_electronic", "traditional_hip_hop_fusion"
                    ]
                },
                "film_music": {
                    "description": "Film soundtracks and scores",
                    "sub_genres": [
                        "film_songs", "background_scores", "orchestral_scores"
                    ]
                }
            }
        },
        
        "dance": {
            "description": "Traditional and contemporary dance forms",
            "styles": {
                "kandyan_dance": {
                    "description": "Up-country classical dance (Udarata Natum)",
                    "sub_genres": [
                        "ves_dance", "naiyandi", "pantheru", "uddekki", "vannam_dance"
                    ]
                },
                "low_country_dance": {
                    "description": "Coastal ritual dance (Pahatharata Natum)",
                    "sub_genres": [
                        "kolam_dance", "sanni_yakuma", "devil_dance"
                    ]
                },
                "sabaragamuwa_dance": {
                    "description": "Sabaragamuwa province dance",
                    "sub_genres": [
                        "ritual_based", "drum_centered"
                    ]
                },
                "tamil_classical": {
                    "description": "Tamil classical dance tradition",
                    "sub_genres": [
                        "bharatanatyam"
                    ]
                },
                "muslim_cultural_dance": {
                    "description": "Muslim cultural and ceremonial dance",
                    "sub_genres": [
                        "wedding_dances", "ceremonial_dances"
                    ]
                },
                "folk_dance": {
                    "description": "Village and folk dances",
                    "sub_genres": [
                        "harvest_dances", "village_festival_dances", "new_year_dances"
                    ]
                },
                "contemporary_modern": {
                    "description": "Modern choreography",
                    "sub_genres": [
                        "sri_lankan_contemporary", "interpretative", "theatrical_dance"
                    ]
                },
                "urban_street": {
                    "description": "Urban street dance styles",
                    "sub_genres": [
                        "hip_hop_dance", "breaking", "popping", "locking", "kpop_cover"
                    ]
                },
                "ballroom_western": {
                    "description": "Ballroom and Western dance",
                    "sub_genres": [
                        "waltz", "tango", "salsa", "cha_cha"
                    ]
                }
            }
        },
        
        "film": {
            "description": "Cinema and film production",
            "styles": {
                "commercial_cinema": {
                    "description": "Mainstream commercial films",
                    "sub_genres": [
                        "mass_action", "romantic_commercial", "comedy_commercial",
                        "family_drama"
                    ],
                    "example_films": ["Kosthapal Punyasoma", "Seethakalyanaya"]
                },
                "art_parallel_cinema": {
                    "description": "Art and parallel cinema",
                    "sub_genres": [
                        "realism", "social_realism", "symbolic_cinema", "festival_cinema"
                    ],
                    "influenced_by": "Lester James Peries",
                    "example_films": ["Rekava", "Gamperaliya", "Nidhanaya"]
                },
                "political_cinema": {
                    "description": "Political and social commentary",
                    "sub_genres": [
                        "civil_war_themes", "social_justice", "ethnic_conflict"
                    ]
                },
                "historical_period": {
                    "description": "Historical and period films",
                    "sub_genres": [
                        "ancient_sri_lanka", "colonial_era", "biographical"
                    ]
                },
                "religious_mythological": {
                    "description": "Religious and mythological films",
                    "sub_genres": [
                        "buddhist_films", "hindu_mythology", "jataka_tales"
                    ]
                },
                "war_films": {
                    "description": "War and conflict based films",
                    "sub_genres": [
                        "civil_war_narratives", "military_themes"
                    ]
                },
                "thriller_crime": {
                    "description": "Thriller and crime films",
                    "sub_genres": [
                        "detective", "police_procedural", "crime_drama"
                    ]
                },
                "horror": {
                    "description": "Horror and supernatural",
                    "sub_genres": [
                        "supernatural_horror", "psychological_horror"
                    ]
                },
                "romantic": {
                    "description": "Romantic films",
                    "sub_genres": [
                        "romantic_drama", "romantic_comedy"
                    ]
                },
                "experimental_independent": {
                    "description": "Experimental and independent cinema",
                    "sub_genres": [
                        "avant_garde", "low_budget_indie"
                    ]
                }
            }
        },
        
        "drama": {
            "description": "Theatre and stage drama",
            "styles": {
                "traditional_theatre": {
                    "description": "Traditional theatrical forms",
                    "sub_genres": [
                        "nadagam", "kolam_theatre", "sokari"
                    ]
                },
                "modern_stage_drama": {
                    "description": "Modern stage productions",
                    "sub_genres": [
                        "social_drama", "literary_adaptation", "political_theatre"
                    ],
                    "influenced_by": "Ediriweera Sarachchandra"
                },
                "teledrama": {
                    "description": "Television drama series",
                    "sub_genres": [
                        "family_drama", "romance_series", "crime_series",
                        "historical_series", "political_series"
                    ]
                },
                "musical_drama": {
                    "description": "Musical theatre",
                    "sub_genres": [
                        "stage_musicals", "opera"
                    ]
                },
                "experimental_avant_garde": {
                    "description": "Experimental theatre",
                    "sub_genres": [
                        "physical_theatre", "immersive_theatre"
                    ]
                }
            }
        }
    },
    
    # =========================================================================
    # LANGUAGES (3 Primary)
    # =========================================================================
    "languages": {
        "sinhala": {
            "population_percentage": 74.9,
            "script": "sinhala",
            "description": "Primary language of majority population"
        },
        "tamil": {
            "population_percentage": 15.4,
            "script": "tamil",
            "description": "Primary language of Tamil community"
        },
        "english": {
            "population_percentage": 10.0,
            "script": "latin",
            "description": "Link language and urban usage"
        }
    },
    
    # =========================================================================
    # MOODS (Comprehensive)
    # =========================================================================
    "moods": {
        # Core Emotional Moods (Universal)
        "celebratory": {"category": "core", "description": "Festive, joyful"},
        "spiritual": {"category": "core", "description": "Transcendent, meditative"},
        "devotional": {"category": "core", "description": "Prayer-like, religious"},
        "patriotic": {"category": "core", "description": "National pride"},
        "romantic": {"category": "core", "description": "Love-themed"},
        "energetic": {"category": "core", "description": "High-energy, dynamic"},
        "reflective": {"category": "core", "description": "Thoughtful, introspective"},
        "melancholic": {"category": "core", "description": "Sorrowful, wistful"},
        "sad": {"category": "core", "description": "Sorrowful, mournful"},
        "joyful": {"category": "core", "description": "Happy, uplifting"},
        "peaceful": {"category": "core", "description": "Calm, serene"},
        "intense": {"category": "core", "description": "Powerful, forceful"},
        "dramatic": {"category": "core", "description": "Theatrical, expressive"},
        "emotional": {"category": "core", "description": "Deeply feeling"},
        "hopeful": {"category": "core", "description": "Optimistic"},
        "inspirational": {"category": "core", "description": "Uplifting, motivating"},
        "motivational": {"category": "core", "description": "Encouraging"},
        "serious": {"category": "core", "description": "Grave, solemn"},
        "dark": {"category": "core", "description": "Somber, gloomy"},
        "mysterious": {"category": "core", "description": "Enigmatic"},
        "suspenseful": {"category": "core", "description": "Tense, anxious"},
        "fearful": {"category": "core", "description": "Frightening"},
        "tense": {"category": "core", "description": "Strained, nervous"},
        "angry": {"category": "core", "description": "Furious, wrathful"},
        "aggressive": {"category": "core", "description": "Forceful, hostile"},
        "powerful": {"category": "core", "description": "Mighty, strong"},
        "uplifting": {"category": "core", "description": "Elevating, inspiring"},
        
        # Culturally Relevant Moods (Sri Lankan Context)
        "ritualistic": {"category": "cultural", "description": "Ceremonial rituals"},
        "ceremonial": {"category": "cultural", "description": "Formal ceremonies"},
        "heroic": {"category": "cultural", "description": "Brave, valiant"},
        "mythological": {"category": "cultural", "description": "Legendary tales"},
        "traditional": {"category": "cultural", "description": "Heritage-based"},
        "festive": {"category": "cultural", "description": "Festival atmosphere"},
        "spiritual_trance": {"category": "cultural", "description": "Meditative state"},
        "cultural_pride": {"category": "cultural", "description": "Heritage pride"},
        "national_pride": {"category": "cultural", "description": "Patriotic feeling"},
        "rural_village": {"category": "cultural", "description": "Village life"},
        "urban_street": {"category": "cultural", "description": "City vibe"},
        "political_awareness": {"category": "cultural", "description": "Social consciousness"},
        "social_awareness": {"category": "cultural", "description": "Community mindful"},
        "religious_reverence": {"category": "cultural", "description": "Pious respect"},
        "historical_nostalgia": {"category": "cultural", "description": "Past longing"},
        
        # Music-Specific Moods
        "party": {"category": "music", "description": "Party atmosphere"},
        "danceable": {"category": "music", "description": "Makes you dance"},
        "chill": {"category": "music", "description": "Relaxed vibe"},
        "acoustic_warm": {"category": "music", "description": "Warm acoustic sound"},
        "love_longing": {"category": "music", "description": "Yearning for love"},
        "heartbreak": {"category": "music", "description": "Broken-hearted"},
        "empowerment": {"category": "music", "description": "Empowering"},
        "meditative": {"category": "music", "description": "Contemplative"},
        "dramatic_ballad": {"category": "music", "description": "Dramatic song"},
        "fusion_energy": {"category": "music", "description": "Cross-cultural energy"},
        "rebel": {"category": "music", "description": "Rebellious"},
        
        # Dance-Specific Moods
        "rhythmic": {"category": "dance", "description": "Strong rhythm"},
        "theatrical": {"category": "dance", "description": "Dramatic performance"},
        "expressive": {"category": "dance", "description": "Emotionally expressive"},
        "graceful": {"category": "dance", "description": "Elegant movements"},
        "fierce": {"category": "dance", "description": "Intense energy"},
        "sacred": {"category": "dance", "description": "Holy, consecrated"},
        "competitive": {"category": "dance", "description": "Contest-oriented"},
        
        # Film & Drama Moods
        "suspense": {"category": "film_drama", "description": "Suspenseful tension"},
        "thriller_tension": {"category": "film_drama", "description": "Thriller intensity"},
        "romantic_longing": {"category": "film_drama", "description": "Romance yearning"},
        "comic_relief": {"category": "film_drama", "description": "Humorous break"},
        "satirical": {"category": "film_drama", "description": "Satirical humor"},
        "social_critique": {"category": "film_drama", "description": "Social commentary"},
        "political_intensity": {"category": "film_drama", "description": "Political tension"},
        "war_tension": {"category": "film_drama", "description": "War conflict"},
        "tragic": {"category": "film_drama", "description": "Tragedy"},
        "inspirational_biographical": {"category": "film_drama", "description": "Life story"},
        "psychological": {"category": "film_drama", "description": "Mind-focused"}
    },
    
    # =========================================================================
    # REGIONS & CITIES (with GPS Coordinates)
    # =========================================================================
    "regions": {
        "western": {
            "capital": "Colombo",
            "cities": {
                "colombo": {"lat": 6.9271, "lon": 79.8612, "population": 750000},
                "gampaha": {"lat": 7.0873, "lon": 80.0142, "population": 90000},
                "kalutara": {"lat": 6.5854, "lon": 79.9607, "population": 38000},
                "negombo": {"lat": 7.2094, "lon": 79.8358, "population": 142000},
                "panadura": {"lat": 6.7134, "lon": 79.9026, "population": 47000}
            },
            "cultural_identity": "urban_cosmopolitan",
            "signature_arts": ["modern_music", "commercial_film", "urban_culture"]
        },
        "central": {
            "capital": "Kandy",
            "cities": {
                "kandy": {"lat": 7.2906, "lon": 80.6337, "population": 125000},
                "matale": {"lat": 7.4675, "lon": 80.6234, "population": 36000},
                "nuwara_eliya": {"lat": 6.9497, "lon": 80.7891, "population": 25000}
            },
            "cultural_identity": "kandyan_kingdom",
            "signature_arts": ["kandyan_dance", "traditional_music", "heritage"]
        },
        "southern": {
            "capital": "Galle",
            "cities": {
                "galle": {"lat": 6.0367, "lon": 80.217, "population": 93000},
                "matara": {"lat": 5.9549, "lon": 80.5550, "population": 44000},
                "hambantota": {"lat": 6.1429, "lon": 81.1212, "population": 21000},
                "ambalangoda": {"lat": 6.2358, "lon": 80.0538, "population": 20000}
            },
            "cultural_identity": "coastal_traditional",
            "signature_arts": ["low_country_dance", "mask_making", "traditional_theatre"]
        },
        "northern": {
            "capital": "Jaffna",
            "cities": {
                "jaffna": {"lat": 9.6615, "lon": 80.0255, "population": 88000},
                "kilinochchi": {"lat": 9.3847, "lon": 80.3986, "population": 20000},
                "mannar": {"lat": 8.9810, "lon": 79.9044, "population": 19000}
            },
            "cultural_identity": "tamil_heritage",
            "signature_arts": ["bharatanatyam", "carnatic_music", "tamil_culture"]
        },
        "eastern": {
            "capital": "Trincomalee",
            "cities": {
                "trincomalee": {"lat": 8.5874, "lon": 81.2152, "population": 99000},
                "batticaloa": {"lat": 7.7310, "lon": 81.6747, "population": 86000},
                "ampara": {"lat": 7.2969, "lon": 81.6686, "population": 19000}
            },
            "cultural_identity": "mixed_heritage",
            "signature_arts": ["folk_music", "traditional_crafts", "diverse_culture"]
        },
        "north_western": {
            "capital": "Kurunegala",
            "cities": {
                "kurunegala": {"lat": 7.4863, "lon": 80.3623, "population": 29000},
                "puttalam": {"lat": 8.0362, "lon": 79.8283, "population": 45000},
                "chilaw": {"lat": 7.5758, "lon": 79.7952, "population": 30000}
            },
            "cultural_identity": "agricultural",
            "signature_arts": ["folk_traditions", "agricultural_festivals"]
        },
        "north_central": {
            "capital": "Anuradhapura",
            "cities": {
                "anuradhapura": {"lat": 8.3114, "lon": 80.4037, "population": 63000},
                "polonnaruwa": {"lat": 7.9403, "lon": 81.0188, "population": 13000}
            },
            "cultural_identity": "ancient_kingdoms",
            "signature_arts": ["temple_traditions", "historical_arts"]
        },
        "uva": {
            "capital": "Badulla",
            "cities": {
                "badulla": {"lat": 6.9934, "lon": 81.0550, "population": 42000},
                "monaragala": {"lat": 6.8728, "lon": 81.3507, "population": 10000}
            },
            "cultural_identity": "hill_country",
            "signature_arts": ["folk_dance", "rural_traditions"]
        },
        "sabaragamuwa": {
            "capital": "Ratnapura",
            "cities": {
                "ratnapura": {"lat": 6.6823, "lon": 80.4016, "population": 52000},
                "kegalle": {"lat": 7.2523, "lon": 80.3436, "population": 30000}
            },
            "cultural_identity": "gem_land",
            "signature_arts": ["sabaragamuwa_dance", "folk_traditions"]
        }
    }
}


# Helper functions
def get_art_forms():
    """Get list of all art forms."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"].keys())


def get_styles(art_form: str):
    """Get styles for a specific art form."""
    if art_form in SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"]:
        return list(SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"][art_form]["styles"].keys())
    return []


def get_sub_genres(art_form: str, style: str):
    """Get sub-genres for a specific style."""
    if art_form in SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"]:
        styles = SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"][art_form]["styles"]
        if style in styles:
            return styles[style].get("sub_genres", [])
    return []


def get_languages():
    """Get list of all languages."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["languages"].keys())


def get_moods(category=None):
    """Get list of moods, optionally filtered by category."""
    moods = SRI_LANKAN_CULTURAL_TAXONOMY["moods"]
    if category:
        return [mood for mood, data in moods.items() if data.get("category") == category]
    return list(moods.keys())


def get_regions():
    """Get list of all regions."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["regions"].keys())


def get_cities(region=None):
    """Get cities, optionally filtered by region."""
    if region and region in SRI_LANKAN_CULTURAL_TAXONOMY["regions"]:
        return list(SRI_LANKAN_CULTURAL_TAXONOMY["regions"][region]["cities"].keys())
    
    all_cities = []
    for reg_data in SRI_LANKAN_CULTURAL_TAXONOMY["regions"].values():
        all_cities.extend(reg_data["cities"].keys())
    return all_cities


def get_city_coordinates(city_name: str):
    """Get GPS coordinates for a city."""
    for region_data in SRI_LANKAN_CULTURAL_TAXONOMY["regions"].values():
        if city_name in region_data["cities"]:
            city_data = region_data["cities"][city_name]
            return city_data["lat"], city_data["lon"]
    return None, None


if __name__ == "__main__":
    print("=" * 70)
    print(" SRI LANKAN CULTURAL TAXONOMY - UPDATED 2026")
    print("=" * 70)
    
    print(f"\n🎭 Art Forms ({len(get_art_forms())}): {get_art_forms()}")
    
    print(f"\n🗣️  Languages ({len(get_languages())}): {get_languages()}")
    
    for art_form in get_art_forms():
        styles = get_styles(art_form)
        print(f"\n📊 {art_form.upper()} Styles ({len(styles)}):")
        for style in styles:
            sub_genres = get_sub_genres(art_form, style)
            print(f"   • {style}: {len(sub_genres)} sub-genres")
    
    mood_categories = ["core", "cultural", "music", "dance", "film_drama"]
    print(f"\n😊 Moods by Category:")
    for cat in mood_categories:
        moods = get_moods(cat)
        print(f"   • {cat}: {len(moods)} moods")
    
    print(f"\n🗺️  Regions: {len(get_regions())}")
    print(f"🏙️  Total Cities: {len(get_cities())}")
