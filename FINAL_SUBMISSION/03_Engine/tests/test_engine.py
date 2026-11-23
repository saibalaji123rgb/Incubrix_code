"""
IncuBrix AEO, SEO & GEO Visibility Engine - Automated Unit Test Suite
Covers deduplication, validation, scoring, run diffing, schema generation,
programmatic templates, and failure recovery.
"""

import unittest
import json
import os
import sys

# Add src to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(os.path.dirname(current_dir), "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from question_discovery import deduplicate_question_list, classify_intent, validate_question_record
from visibility_analyzer import calculate_item_visibility_score, calculate_dataset_visibility_metrics, compare_runs
from content_generator import generate_schema_jsonld, get_programmatic_100_pages_dataset
from automation_scheduler import VisibilityAutomationScheduler

class TestIncuBrixEngine(unittest.TestCase):

    def test_deduplication(self):
        sample_questions = [
            "How to repurpose YouTube videos into shorts?",
            "how to repurpose youtube videos into shorts",  # Normalized duplicate
            "Best AI video editor for podcasters in 2027",
            "How to Repurpose YouTube Videos into Shorts?", # Exact case duplicate
            "Opus Clip vs Descript comparison"
        ]
        unique_items, dupes = deduplicate_question_list(sample_questions)
        self.assertEqual(len(unique_items), 3, "Should retain exactly 3 unique questions")
        self.assertEqual(dupes, 2, "Should identify exactly 2 duplicates")

    def test_intent_classification(self):
        self.assertEqual(classify_intent("How to cut out silence in video"), "Informational")
        self.assertEqual(classify_intent("Best AI caption generator for reels"), "Commercial")
        self.assertEqual(classify_intent("Opus Clip vs Descript comparison"), "Comparison")

    def test_question_validation(self):
        valid_q = {
            "question_id": "Q101",
            "question": "Can AI edit video automatically?",
            "intent": "Informational",
            "source_type": "Google Suggest",
            "source_url": "https://www.google.com/search?q=test",
            "market": "United States (US)"
        }
        is_valid, msg = validate_question_record(valid_q)
        self.assertTrue(is_valid, "Valid record should pass")

        invalid_q = {
            "question_id": "Q102",
            "question": "Incomplete query"
            # Missing intent, source_type, source_url, market
        }
        is_valid, msg = validate_question_record(invalid_q)
        self.assertFalse(is_valid, "Incomplete record should be rejected")

    def test_scoring_algorithm(self):
        # High visibility measurement
        high_m = {
            "google_position": "3",
            "answer_box": "AI Overview",
            "quoted_source": "https://incubrix.com/blog/repurpose",
            "chatgpt": "Mentioned",
            "gemini": "Mentioned",
            "perplexity": "Cited",
            "claude": "Mentioned"
        }
        score = calculate_item_visibility_score(high_m)
        self.assertGreaterEqual(score, 60.0, "High visibility measurement should score >= 60")

        # Zero visibility measurement
        zero_m = {
            "google_position": "Not in Top 100",
            "answer_box": "None",
            "quoted_source": "",
            "chatgpt": "Not Mentioned",
            "gemini": "Not Mentioned",
            "perplexity": "Not Mentioned",
            "claude": "Not Mentioned"
        }
        score_zero = calculate_item_visibility_score(zero_m)
        self.assertEqual(score_zero, 0.0, "Zero visibility measurement should score 0")

    def test_run_comparison(self):
        m1 = [
            {"question_id": "Q001", "google_position": "Not in Top 100", "answer_box": "AI Overview", "chatgpt": "Not Mentioned", "gemini": "Not Mentioned", "perplexity": "Not Mentioned", "claude": "Not Mentioned"}
        ]
        m2 = [
            {"question_id": "Q001", "google_position": "Not in Top 100", "answer_box": "AI Overview", "chatgpt": "Mentioned", "gemini": "Not Mentioned", "perplexity": "Not Mentioned", "claude": "Not Mentioned"}
        ]
        diff = compare_runs(m1, m2)
        self.assertEqual(diff["total_compared"], 1)
        self.assertEqual(diff["changed_count"], 1)

    def test_schema_generation(self):
        schema_str = generate_schema_jsonld(
            "HowTo",
            "How to Repurpose Videos",
            "Step by step guide",
            "https://incubrix.com/blog/repurpose",
            steps=[{"name": "Upload video", "text": "Upload mp4 file"}]
        )
        parsed = json.loads(schema_str)
        self.assertEqual(parsed["@context"], "https://schema.org")
        self.assertEqual(parsed["@type"], "HowTo")
        self.assertEqual(len(parsed["step"]), 1)

    def test_programmatic_template(self):
        prog_pages = get_programmatic_100_pages_dataset()
        self.assertEqual(len(prog_pages), 100, "Should generate exactly 100 programmatic pages")
        for p in prog_pages:
            self.assertTrue(p["quality_checked"])
            self.assertTrue(p["url"].startswith("https://incubrix.com/"))

    def test_failure_recovery(self):
        scheduler = VisibilityAutomationScheduler()
        # Test simulated network timeout recovery
        result = scheduler.run_scheduled_check(simulate_network_failure=True)
        self.assertEqual(result["status"], "SUCCESS", "Engine should recover gracefully from simulated failure")
        self.assertGreater(result["items_processed"], 0, "Items should be processed after recovery")

if __name__ == "__main__":
    unittest.main()
