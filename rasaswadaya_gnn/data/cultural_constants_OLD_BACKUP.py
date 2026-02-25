"""
Sri Lankan Cultural Taxonomy
============================
Comprehensive taxonomy of Sri Lankan cultural arts, traditions, and metadata.
This serves as the foundation for Cultural DNA Mapping.
"""

SRI_LANKAN_CULTURAL_TAXONOMY = {
    # =========================================================================
    # ART FORMS
    # =========================================================================
    "art_forms": {
        "dance": {
            "description": "Traditional and contemporary dance forms",
            "sub_genres": {
                "kandyan": {
                    "description": "Up-country classical dance (Uda Rata Natum)",
                    "origin": "central",
                    "traditional": True,
                    "instruments": ["geta_beraya", "davula", "thalampataa"]
                },
                "low_country": {
                    "description": "Coastal ritual dance (Pahatha Rata Natum)",
                    "origin": "southern",
                    "traditional": True,
                    "instruments": ["yak_beraya", "dawula", "horanewa"]
                },
                "sabaragamuwa": {
                    "description": "Sabaragamuwa province dance traditions",
                    "origin": "sabaragamuwa",
                    "traditional": True,
                    "instruments": ["davula", "rabana"]
                },
                "folk": {
                    "description": "Village folk dances (Wannam, Goyam)",
                    "origin": "island_wide",
                    "traditional": True,
                    "instruments": ["rabana", "udakkiya"]
                },
                "contemporary": {
                    "description": "Modern choreography with Sri Lankan elements",
                    "origin": "urban",
                    "traditional": False,
                    "instruments": ["mixed"]
                },
                "bharatanatyam": {
                    "description": "Classical Indian dance in Tamil tradition",
                    "origin": "northern",
                    "traditional": True,
                    "instruments": ["mridangam", "veena", "flute"]
                },
                "fusion": {
                    "description": "Blend of traditional and international styles",
                    "origin": "urban",
                    "traditional": False,
                    "instruments": ["mixed"]
                }
            }
        },
        "music": {
            "description": "Traditional and modern music forms",
            "sub_genres": {
                "classical_sinhala": {
                    "description": "Traditional Sinhala classical music",
                    "origin": "island_wide",
                    "traditional": True,
                    "instruments": ["violin", "harmonium", "tabla"]
                },
                "baila": {
                    "description": "Afro-Portuguese influenced party music",
                    "origin": "western",
                    "traditional": False,
                    "instruments": ["rabana", "guitar", "drums"]
                },
                "elle": {
                    "description": "Traditional work songs and chants",
                    "origin": "rural",
                    "traditional": True,
                    "instruments": ["voice", "rabana"]
                },
                "folk_music": {
                    "description": "Village songs (Jana Gee, Kavi)",
                    "origin": "rural",
                    "traditional": True,
                    "instruments": ["rabana", "flute", "voice"]
                },
                "devotional_buddhist": {
                    "description": "Buddhist devotional songs (Bhakthi Gee)",
                    "origin": "island_wide",
                    "traditional": True,
                    "instruments": ["harmonium", "tabla", "voice"]
                },
                "devotional_hindu": {
                    "description": "Hindu devotional music (Bhajans)",
                    "origin": "northern",
                    "traditional": True,
                    "instruments": ["mridangam", "veena", "harmonium"]
                },
                "carnatic": {
                    "description": "South Indian classical music tradition",
                    "origin": "northern",
                    "traditional": True,
                    "instruments": ["veena", "mridangam", "violin"]
                },
                "contemporary": {
                    "description": "Modern Sinhala/Tamil pop and rock",
                    "origin": "urban",
                    "traditional": False,
                    "instruments": ["guitar", "drums", "keyboard"]
                },
                "fusion": {
                    "description": "Blend of traditional and modern",
                    "origin": "urban",
                    "traditional": False,
                    "instruments": ["mixed"]
                }
            }
        },
        "drama": {
            "description": "Traditional and contemporary theatrical forms",
            "sub_genres": {
                "kolam": {
                    "description": "Masked folk drama from Southern province",
                    "origin": "southern",
                    "traditional": True,
                    "uses_masks": True
                },
                "sokari": {
                    "description": "Hill country folk drama",
                    "origin": "central",
                    "traditional": True,
                    "uses_masks": True
                },
                "nadagam": {
                    "description": "South Indian influenced opera-drama",
                    "origin": "western",
                    "traditional": True,
                    "uses_masks": False
                },
                "nurti": {
                    "description": "Parsee theatre influenced drama",
                    "origin": "western",
                    "traditional": False,
                    "uses_masks": False
                },
                "street_drama": {
                    "description": "Social message theatre (Jana Natya)",
                    "origin": "urban",
                    "traditional": False,
                    "uses_masks": False
                },
                "contemporary": {
                    "description": "Modern theatre productions",
                    "origin": "urban",
                    "traditional": False,
                    "uses_masks": False
                },
                "experimental": {
                    "description": "Avant-garde and experimental theatre",
                    "origin": "urban",
                    "traditional": False,
                    "uses_masks": False
                }
            }
        },
        "visual_arts": {
            "description": "Painting, sculpture, and visual arts",
            "sub_genres": {
                "temple_art": {
                    "description": "Buddhist temple paintings and murals",
                    "origin": "island_wide",
                    "traditional": True
                },
                "kandyan_painting": {
                    "description": "Kandyan school of painting",
                    "origin": "central",
                    "traditional": True
                },
                "contemporary_art": {
                    "description": "Modern and contemporary visual arts",
                    "origin": "urban",
                    "traditional": False
                },
                "sculpture": {
                    "description": "Traditional and modern sculpture",
                    "origin": "island_wide",
                    "traditional": True
                }
            }
        },
        "crafts": {
            "description": "Traditional handicrafts and artisanal work",
            "sub_genres": {
                "mask_carving": {
                    "description": "Ambalangoda mask carving tradition",
                    "origin": "southern",
                    "traditional": True
                },
                "batik": {
                    "description": "Batik fabric art",
                    "origin": "western",
                    "traditional": False
                },
                "lacquerware": {
                    "description": "Traditional lacquer work",
                    "origin": "central",
                    "traditional": True
                },
                "brasswork": {
                    "description": "Traditional brass crafting",
                    "origin": "central",
                    "traditional": True
                },
                "pottery": {
                    "description": "Traditional pottery (Kelaniya style)",
                    "origin": "western",
                    "traditional": True
                },
                "weaving": {
                    "description": "Traditional handloom weaving",
                    "origin": "island_wide",
                    "traditional": True
                }
            }
        },
        "literature": {
            "description": "Literary arts and poetry",
            "sub_genres": {
                "classical_poetry": {
                    "description": "Sandeshaya and classical poetry",
                    "origin": "island_wide",
                    "traditional": True
                },
                "modern_poetry": {
                    "description": "Contemporary Sinhala/Tamil poetry",
                    "origin": "urban",
                    "traditional": False
                },
                "folk_tales": {
                    "description": "Traditional storytelling",
                    "origin": "rural",
                    "traditional": True
                }
            }
        }
    },
    
    # =========================================================================
    # LANGUAGES
    # =========================================================================
    "languages": {
        "sinhala": {"population_percentage": 74.9, "script": "sinhala"},
        "tamil": {"population_percentage": 15.4, "script": "tamil"},
        "english": {"population_percentage": 10.0, "script": "latin"},
        "mixed_sinhala_english": {"description": "Singlish/Code-switching"},
        "mixed_tamil_english": {"description": "Tanglish/Code-switching"},
        "trilingual": {"description": "Content in all three languages"}
    },
    
    # =========================================================================
    # REGIONS (PROVINCES)
    # =========================================================================
    "regions": {
        "western": {
            "capital": "Colombo",
            "key_cities": ["Colombo", "Gampaha", "Kalutara"],
            "cultural_identity": "urban_cosmopolitan",
            "signature_arts": ["nurti", "contemporary", "baila"]
        },
        "central": {
            "capital": "Kandy",
            "key_cities": ["Kandy", "Matale", "Nuwara Eliya"],
            "cultural_identity": "kandyan_kingdom",
            "signature_arts": ["kandyan_dance", "esala_perahera", "temple_art"]
        },
        "southern": {
            "capital": "Galle",
            "key_cities": ["Galle", "Matara", "Hambantota"],
            "cultural_identity": "coastal_traditional",
            "signature_arts": ["low_country_dance", "mask_carving", "kolam"]
        },
        "northern": {
            "capital": "Jaffna",
            "key_cities": ["Jaffna", "Kilinochchi", "Mannar"],
            "cultural_identity": "tamil_heritage",
            "signature_arts": ["bharatanatyam", "carnatic", "hindu_temple_arts"]
        },
        "eastern": {
            "capital": "Trincomalee",
            "key_cities": ["Trincomalee", "Batticaloa", "Ampara"],
            "cultural_identity": "mixed_heritage",
            "signature_arts": ["folk_music", "traditional_crafts"]
        },
        "north_western": {
            "capital": "Kurunegala",
            "key_cities": ["Kurunegala", "Puttalam", "Chilaw"],
            "cultural_identity": "agricultural_folk",
            "signature_arts": ["folk_music", "weaving"]
        },
        "north_central": {
            "capital": "Anuradhapura",
            "key_cities": ["Anuradhapura", "Polonnaruwa"],
            "cultural_identity": "ancient_kingdoms",
            "signature_arts": ["temple_art", "traditional_crafts", "devotional"]
        },
        "uva": {
            "capital": "Badulla",
            "key_cities": ["Badulla", "Monaragala"],
            "cultural_identity": "hill_country_folk",
            "signature_arts": ["folk_dance", "folk_music"]
        },
        "sabaragamuwa": {
            "capital": "Ratnapura",
            "key_cities": ["Ratnapura", "Kegalle"],
            "cultural_identity": "gem_land_traditions",
            "signature_arts": ["sabaragamuwa_dance", "folk_music"]
        }
    },
    
    # =========================================================================
    # FESTIVALS & SEASONS
    # =========================================================================
    "festivals": {
        "sinhala_tamil_new_year": {
            "month": "april",
            "duration_days": 3,
            "cultural_scope": "national",
            "associated_arts": ["folk_music", "traditional_games", "kolam"],
            "mood": "celebratory"
        },
        "vesak": {
            "month": "may",
            "duration_days": 2,
            "cultural_scope": "buddhist",
            "associated_arts": ["devotional_music", "pandol", "dansala"],
            "mood": "spiritual"
        },
        "poson": {
            "month": "june",
            "duration_days": 2,
            "cultural_scope": "buddhist",
            "associated_arts": ["devotional_music", "pilgrimages"],
            "mood": "spiritual"
        },
        "esala_perahera": {
            "month": "august",
            "duration_days": 10,
            "cultural_scope": "kandyan",
            "associated_arts": ["kandyan_dance", "drumming", "fire_walking"],
            "mood": "celebratory"
        },
        "deepavali": {
            "month": "october_november",
            "duration_days": 1,
            "cultural_scope": "hindu",
            "associated_arts": ["bharatanatyam", "carnatic", "kolam_art"],
            "mood": "celebratory"
        },
        "thai_pongal": {
            "month": "january",
            "duration_days": 4,
            "cultural_scope": "tamil",
            "associated_arts": ["folk_music", "kolam_rangoli"],
            "mood": "celebratory"
        },
        "independence_day": {
            "month": "february",
            "duration_days": 1,
            "cultural_scope": "national",
            "associated_arts": ["patriotic_music", "dance_pageants"],
            "mood": "patriotic"
        },
        "christmas": {
            "month": "december",
            "duration_days": 1,
            "cultural_scope": "christian",
            "associated_arts": ["carols", "baila"],
            "mood": "celebratory"
        },
        "peradeniya_arts_festival": {
            "month": "varies",
            "duration_days": 7,
            "cultural_scope": "academic",
            "associated_arts": ["contemporary", "experimental", "fusion"],
            "mood": "intellectual"
        },
        "galle_literary_festival": {
            "month": "january",
            "duration_days": 4,
            "cultural_scope": "literary",
            "associated_arts": ["literature", "poetry", "storytelling"],
            "mood": "intellectual"
        }
    },
    
    # =========================================================================
    # MOODS / VIBES
    # =========================================================================
    "moods": {
        "celebratory": {
            "description": "Festive, joyful, high-energy",
            "typical_contexts": ["festivals", "weddings", "new_year"]
        },
        "spiritual": {
            "description": "Devotional, meditative, transcendent",
            "typical_contexts": ["vesak", "poson", "temple_events"]
        },
        "reflective": {
            "description": "Thoughtful, introspective, melancholic",
            "typical_contexts": ["art_exhibitions", "poetry_readings"]
        },
        "energetic": {
            "description": "Upbeat, dynamic, youthful",
            "typical_contexts": ["concerts", "dance_performances"]
        },
        "romantic": {
            "description": "Love-themed, emotional",
            "typical_contexts": ["music_concerts", "drama"]
        },
        "patriotic": {
            "description": "National pride, historical",
            "typical_contexts": ["independence_day", "national_events"]
        },
        "devotional": {
            "description": "Religious, prayer-like",
            "typical_contexts": ["temple_events", "religious_festivals"]
        },
        "intellectual": {
            "description": "Academic, analytical, avant-garde",
            "typical_contexts": ["festivals", "university_events"]
        }
    },
    
    # =========================================================================
    # VENUE TYPES
    # =========================================================================
    "venue_types": {
        "temple": {"indoor": False, "capacity": "varies", "typical_events": ["devotional", "perahera"]},
        "theatre": {"indoor": True, "capacity": "medium", "typical_events": ["drama", "concerts"]},
        "amphitheatre": {"indoor": False, "capacity": "large", "typical_events": ["concerts", "festivals"]},
        "art_gallery": {"indoor": True, "capacity": "small", "typical_events": ["exhibitions"]},
        "university_hall": {"indoor": True, "capacity": "medium", "typical_events": ["academic", "literary"]},
        "community_hall": {"indoor": True, "capacity": "medium", "typical_events": ["folk", "community"]},
        "outdoor_ground": {"indoor": False, "capacity": "large", "typical_events": ["festivals", "concerts"]},
        "hotel_ballroom": {"indoor": True, "capacity": "medium", "typical_events": ["formal", "concerts"]}
    }
}


# Helper functions to access taxonomy
def get_art_forms():
    """Get list of all art forms."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"].keys())


def get_sub_genres(art_form: str):
    """Get sub-genres for a specific art form."""
    if art_form in SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"]:
        return list(SRI_LANKAN_CULTURAL_TAXONOMY["art_forms"][art_form]["sub_genres"].keys())
    return []


def get_regions():
    """Get list of all regions."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["regions"].keys())


def get_festivals():
    """Get list of all festivals."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["festivals"].keys())


def get_moods():
    """Get list of all moods."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["moods"].keys())


def get_languages():
    """Get list of all languages."""
    return list(SRI_LANKAN_CULTURAL_TAXONOMY["languages"].keys())


if __name__ == "__main__":
    # Print taxonomy summary
    print("=" * 60)
    print(" SRI LANKAN CULTURAL TAXONOMY SUMMARY")
    print("=" * 60)
    print(f"\n🎭 Art Forms: {get_art_forms()}")
    print(f"\n🗺️  Regions: {get_regions()}")
    print(f"\n🎉 Festivals: {get_festivals()}")
    print(f"\n😊 Moods: {get_moods()}")
    print(f"\n🗣️  Languages: {get_languages()}")
    
    print("\n\n📊 Sub-genres by Art Form:")
    for art_form in get_art_forms():
        sub_genres = get_sub_genres(art_form)
        print(f"   {art_form.upper()}: {sub_genres}")
