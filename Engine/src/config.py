"""
IncuBrix AEO, SEO & GEO Visibility Engine - Configuration Module
"""

import os

# Base paths
ENGINE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKSPACE_DIR = os.path.dirname(ENGINE_DIR)
DATA_DIR = os.path.join(ENGINE_DIR, "data")
SRC_DIR = os.path.join(ENGINE_DIR, "src")
MAIN_OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "Main_Output")
RAW_ANSWERS_DIR = os.path.join(MAIN_OUTPUT_DIR, "raw_answers")

# Database path
DB_PATH = os.path.join(DATA_DIR, "incubrix_visibility.db")

# Target Domain
TARGET_DOMAIN = "incubrix.com"
TARGET_BRAND = "IncuBrix"

# Supported Markets
SUPPORTED_MARKETS = [
    "United States (US)",
    "United Kingdom (UK)",
    "India (IN)"
]

# Supported Search Intents
INTENT_TYPES = [
    "Informational",
    "Commercial",
    "Comparison"
]

# Supported AI Assistants
AI_ASSISTANTS = [
    "ChatGPT",
    "Gemini",
    "Perplexity",
    "Claude"
]

# Scoring Weights for Visibility Index
SCORING_WEIGHTS = {
    "google_top_10": 25,
    "google_top_30": 10,
    "featured_snippet_or_overview": 25,
    "ai_assistant_mention": 25,
    "ai_assistant_citation": 15
}

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)
