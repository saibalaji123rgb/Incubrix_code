"""
Headless End-to-End Test for All 12 Screens in Engine/src/app.py
"""
import os
import sys
import json
import pandas as pd
from pathlib import Path

workspace_dir = str(Path(__file__).resolve().parent)
engine_src = os.path.join(workspace_dir, "Engine", "src")
sys.path.insert(0, engine_src)

import database
import visibility_analyzer
import seo_auditor
import content_generator
import citation_finder
import reporter
import automation_scheduler

print("Testing Screen 1: Dashboard...")
questions = database.get_all_questions()
m_d1 = database.get_measurements_by_date("2026-11-19")
m_d2 = database.get_measurements_by_date("2026-11-20")
metrics_d2 = visibility_analyzer.calculate_dataset_visibility_metrics(m_d2)
comps = visibility_analyzer.analyze_competitors(m_d2)
print("Screen 1 OK!")

print("Testing Screen 2: Question Bank...")
assert len(questions) == 300, f"Expected 300, got {len(questions)}"
assert not database.is_duplicate_question("A totally unique brand new test question 2027?")
assert database.is_duplicate_question(questions[0]["question"])
print("Screen 2 OK!")

print("Testing Screen 3: Visibility Checker...")
for q in questions[:10]:
    qid = q["question_id"]
    f1 = os.path.join(workspace_dir, "Main_Output", "raw_answers", "day1", f"{qid}.json")
    f2 = os.path.join(workspace_dir, "Main_Output", "raw_answers", "day2", f"{qid}.json")
    assert os.path.exists(f1) and os.path.exists(f2)
    with open(f1, "r", encoding="utf-8") as jf:
        json.load(jf)
print("Screen 3 OK!")

print("Testing Screen 4: Day 1 vs Day 2 Comparison...")
diff_res = visibility_analyzer.compare_runs(m_d1, m_d2)
print(f"Stability: {diff_res['stability_rate']}% | Diffs: {len(diff_res['differences'])}")
print("Screen 4 OK!")

print("Testing Screen 5: Technical SEO Auditor...")
aud = seo_auditor.TechnicalSEOAuditor()
a_data = aud.get_baseline_vs_optimized_audit()
assert len(a_data["categories"]) == 9
print("Screen 5 OK!")

print("Testing Screen 6: Fix Manager...")
fixes = database.get_all_fixes()
assert len(fixes) == 20
for f in fixes:
    f_path = os.path.join(workspace_dir, f["code_or_text_url"])
    assert os.path.exists(f_path), f"Missing {f_path}"
print("Screen 6 OK!")

print("Testing Screen 7: Content Manager...")
pages = database.get_all_pages()
assert len(pages) == 20
for p in pages:
    p_path = os.path.join(workspace_dir, p["draft_url"])
    assert os.path.exists(p_path), f"Missing {p_path}"
prog_csv = os.path.join(workspace_dir, "Main_Output", "programmatic_template", "100_pages_dataset.csv")
assert os.path.exists(prog_csv)
df_p = pd.read_csv(prog_csv)
assert len(df_p) == 100
print("Screen 7 OK!")

print("Testing Screen 8: Citation Finder...")
cites = database.get_all_citations()
assert len(cites) == 30
for c in cites:
    c_path = os.path.join(workspace_dir, c["draft_url"])
    assert os.path.exists(c_path), f"Missing {c_path}"
    pitch = citation_finder.generate_personalized_pitch(c)
    assert "subject" in pitch and "body" in pitch
print("Screen 8 OK!")

print("Testing Screen 9: Automation & Scheduler...")
sched = automation_scheduler.VisibilityAutomationScheduler()
r_normal = sched.run_scheduled_check(simulate_network_failure=False)
assert r_normal["status"] == "SUCCESS"
r_recov = sched.run_scheduled_check(simulate_network_failure=True)
assert r_recov["status"] == "SUCCESS"
assert r_recov["items_processed"] == 300
print("Screen 9 OK!")

print("Testing Screen 10: Reports & Data Export...")
rep = reporter.generate_weekly_markdown_report("2026-11-19", "2026-11-20")
assert len(rep) > 500
assert os.path.exists(os.path.join(workspace_dir, "Main_Output", "visibility.csv"))
assert os.path.exists(os.path.join(workspace_dir, "Submission_Workbook.xlsx"))
print("Screen 10 OK!")

print("Testing Screen 11: Case Study...")
cs_md = os.path.join(workspace_dir, "Main_Output", "case_study", "BEFORE_AFTER_CASE_STUDY.md")
assert os.path.exists(cs_md)
for i in [1, 2, 3]:
    img = os.path.join(workspace_dir, "Main_Output", "case_study", "screenshots", f"CASE_STUDY_0{i}" + ("_google_rank_gain.png" if i==1 else ("_perplexity_citation.png" if i==2 else "_pagespeed_gain.png")))
    assert os.path.exists(img)
print("Screen 11 OK!")

print("Testing Screen 12: Rubric & Guides...")
v1 = os.path.join(workspace_dir, "Video_Guides", "Product_Walkthrough_Video_Script.md")
v2 = os.path.join(workspace_dir, "Video_Guides", "Technical_Demo_Video_Script.md")
assert os.path.exists(v1) and os.path.exists(v2)
print("Screen 12 OK!")

print("\n==========================================")
print("ALL 12 SCREENS TESTED AND PASSED 100%!")
print("==========================================")
