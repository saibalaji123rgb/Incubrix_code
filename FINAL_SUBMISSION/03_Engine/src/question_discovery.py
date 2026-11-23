"""
IncuBrix AEO, SEO & GEO Visibility Engine - Question Discovery & Deduplication
"""

import re
import hashlib
try:
    from .config import SUPPORTED_MARKETS, INTENT_TYPES
    from .database import is_duplicate_question, add_question, get_all_questions
except ImportError:
    from config import SUPPORTED_MARKETS, INTENT_TYPES
    from database import is_duplicate_question, add_question, get_all_questions

def normalize_text(text):
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return ' '.join(clean.split())

def compute_hash(text):
    return hashlib.sha256(normalize_text(text).encode('utf-8')).hexdigest()

def classify_intent(question_text):
    q_lower = question_text.lower()
    if any(k in q_lower for k in [" vs ", " versus ", " or ", "alternative", "compare", "comparison"]):
        return "Comparison"
    elif any(k in q_lower for k in ["best", "top ", "tools for", "software", "pricing", "affordable", "review", "cheaper"]):
        return "Commercial"
    else:
        return "Informational"

def deduplicate_question_list(raw_questions):
    """
    Takes a list of question strings or dicts, removes duplicates, and classifies intent.
    Returns: (unique_items, duplicates_count)
    """
    seen_hashes = set()
    unique_items = []
    duplicates_count = 0

    for item in raw_questions:
        if isinstance(item, dict):
            q_text = item.get("question", "")
        else:
            q_text = str(item)

        q_clean = q_text.strip()
        if not q_clean:
            continue

        h = compute_hash(q_clean)
        if h in seen_hashes:
            duplicates_count += 1
            continue

        seen_hashes.add(h)

        if isinstance(item, dict):
            entry = dict(item)
            if "intent" not in entry or not entry["intent"]:
                entry["intent"] = classify_intent(q_clean)
            unique_items.append(entry)
        else:
            unique_items.append({
                "question": q_clean,
                "intent": classify_intent(q_clean)
            })

    return unique_items, duplicates_count

def validate_question_record(q_dict):
    """
    Validates that a question record contains all required fields:
    question_id, question, intent, source_type, source_url, market
    """
    required_fields = ["question_id", "question", "intent", "source_type", "source_url", "market"]
    missing = [f for f in required_fields if not q_dict.get(f)]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    if q_dict["market"] not in SUPPORTED_MARKETS:
        # Default or allow valid format
        pass

    if not q_dict["source_url"].startswith("http"):
        return False, "source_url must start with http:// or https://"

    return True, "Valid record."
