"""
IncuBrix AEO, SEO & GEO Visibility Engine - Database Access Layer
Supports SQLite persistence for Questions, Measurements, Measurement Runs, Provenance Records,
Technical Fixes, Content Pages, Citation Targets, and Engine Activity Logs.
"""

import sqlite3
import datetime
import os
import re
import csv
import io
from typing import List, Dict, Any, Tuple, Optional

try:
    from .config import DB_PATH
except ImportError:
    from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Questions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        question_id TEXT PRIMARY KEY,
        question TEXT NOT NULL,
        intent TEXT NOT NULL,
        source_type TEXT NOT NULL,
        source_url TEXT NOT NULL,
        market TEXT NOT NULL,
        priority TEXT NOT NULL,
        notes TEXT,
        category TEXT DEFAULT 'Video Repurposing & Clipping',
        source_status TEXT DEFAULT 'VERIFIED',
        source_evidence TEXT DEFAULT 'Google Suggest / Community Query',
        source_accessibility TEXT DEFAULT 'ACCESSIBLE'
    )
    """)

    # 2. Measurement Runs Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS measurement_runs (
        run_id TEXT PRIMARY KEY,
        run_name TEXT NOT NULL,
        run_date TEXT NOT NULL,
        market TEXT NOT NULL,
        collection_method TEXT NOT NULL,
        status TEXT NOT NULL,
        total_questions INTEGER DEFAULT 0,
        verified_records_count INTEGER DEFAULT 0,
        demo_records_count INTEGER DEFAULT 0,
        notes TEXT
    )
    """)

    # 3. Measurements Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id TEXT NOT NULL,
        run_id TEXT DEFAULT 'RUN-DEMO-BASELINE-D1',
        run_date TEXT NOT NULL,
        collection_method TEXT DEFAULT 'DEMO_SYNTHETIC',
        verification_status TEXT DEFAULT 'DEMO',
        search_depth INTEGER DEFAULT 30,
        google_position TEXT,
        incubrix_found INTEGER DEFAULT 0,
        answer_box TEXT,
        featured_snippet_present INTEGER DEFAULT 0,
        people_also_ask_present INTEGER DEFAULT 0,
        ai_overview_present INTEGER DEFAULT 0,
        quoted_source TEXT,
        top_competitors TEXT DEFAULT '',
        search_location TEXT DEFAULT '',
        evidence_file_path TEXT DEFAULT '',
        chatgpt TEXT,
        chatgpt_raw_answer TEXT DEFAULT '',
        chatgpt_mention_sentence TEXT DEFAULT '',
        chatgpt_citations TEXT DEFAULT '',
        chatgpt_model TEXT DEFAULT 'GPT-4o',
        gemini TEXT,
        gemini_raw_answer TEXT DEFAULT '',
        gemini_mention_sentence TEXT DEFAULT '',
        gemini_citations TEXT DEFAULT '',
        gemini_model TEXT DEFAULT 'Gemini 1.5 Pro',
        perplexity TEXT,
        perplexity_raw_answer TEXT DEFAULT '',
        perplexity_mention_sentence TEXT DEFAULT '',
        perplexity_citations TEXT DEFAULT '',
        perplexity_model TEXT DEFAULT 'Perplexity Sonar',
        claude TEXT,
        claude_raw_answer TEXT DEFAULT '',
        claude_mention_sentence TEXT DEFAULT '',
        claude_citations TEXT DEFAULT '',
        claude_model TEXT DEFAULT 'Claude 3.5 Sonnet',
        competitors_named TEXT,
        raw_answers_url TEXT,
        FOREIGN KEY(question_id) REFERENCES questions(question_id),
        FOREIGN KEY(run_id) REFERENCES measurement_runs(run_id)
    )
    """)

    # 4. Provenance Records Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS provenance_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id TEXT NOT NULL,
        run_id TEXT NOT NULL,
        market TEXT,
        timestamp TEXT,
        engine_or_assistant TEXT,
        collection_method TEXT,
        raw_answer TEXT,
        evidence_file_path TEXT,
        source_urls TEXT,
        verification_status TEXT,
        audited_by TEXT,
        FOREIGN KEY(question_id) REFERENCES questions(question_id),
        FOREIGN KEY(run_id) REFERENCES measurement_runs(run_id)
    )
    """)

    # 5. Technical Fixes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS technical_fixes (
        fix_id TEXT PRIMARY KEY,
        page_url TEXT NOT NULL,
        problem TEXT NOT NULL,
        evidence_url TEXT,
        fix_summary TEXT NOT NULL,
        code_or_text_url TEXT,
        validator_used TEXT,
        validated TEXT,
        impact TEXT,
        effort TEXT
    )
    """)

    # 6. Content Pages Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS content_pages (
        item_id TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        target_question_ids TEXT,
        title TEXT NOT NULL,
        draft_url TEXT,
        why_it_matters TEXT,
        angle_or_schema TEXT,
        sources_cited TEXT,
        status TEXT
    )
    """)

    # 7. Citation Targets Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citation_targets (
        item_id TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        target_question_ids TEXT,
        page_url TEXT NOT NULL,
        draft_url TEXT,
        why_it_matters TEXT,
        angle_or_schema TEXT,
        sources_cited TEXT,
        status TEXT
    )
    """)

    # 8. Engine Activity Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS engine_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        event_type TEXT,
        message TEXT,
        items_processed INTEGER,
        duplicates_removed INTEGER,
        runtime_seconds REAL,
        cost_usd REAL
    )
    """)

    conn.commit()
    conn.close()

# ------------------------------------------------------------------------------
# HELPER / VALIDATION FUNCTIONS
# ------------------------------------------------------------------------------

def normalize_text(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', str(text).lower())

def is_duplicate_question(question_text: str, exclude_id: Optional[str] = None) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    if exclude_id:
        cursor.execute("SELECT question_id, question FROM questions WHERE question_id != ?", (exclude_id,))
    else:
        cursor.execute("SELECT question_id, question FROM questions")
    rows = cursor.fetchall()
    conn.close()

    norm_input = normalize_text(question_text)
    for qid, q in rows:
        if normalize_text(q) == norm_input:
            return True
    return False

# ------------------------------------------------------------------------------
# QUESTION BANK CRUD & FILTERS
# ------------------------------------------------------------------------------

def get_all_questions() -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY question_id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_question_by_id(question_id: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE question_id = ?", (question_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_verified_questions_summary() -> Dict[str, int]:
    """Returns total, verified, and demo counts."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM questions")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) FROM questions WHERE source_status = 'VERIFIED'")
    verified = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) FROM questions WHERE source_status = 'DEMO'")
    demo = cursor.fetchone()[0]
    conn.close()
    return {"total": total, "verified": verified, "demo": demo}

def add_question(question_dict: Dict[str, Any]) -> Tuple[bool, str]:
    if is_duplicate_question(question_dict["question"]):
        return False, "Duplicate question detected."
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO questions (
        question_id, question, intent, source_type, source_url, market,
        priority, notes, category, source_status, source_evidence, source_accessibility
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        question_dict["question_id"],
        question_dict["question"],
        question_dict["intent"],
        question_dict["source_type"],
        question_dict["source_url"],
        question_dict["market"],
        question_dict.get("priority", "Medium"),
        question_dict.get("notes", ""),
        question_dict.get("category", "Video Repurposing & Clipping"),
        question_dict.get("source_status", "VERIFIED"),
        question_dict.get("source_evidence", "Manual Submission"),
        question_dict.get("source_accessibility", "ACCESSIBLE")
    ))
    conn.commit()
    conn.close()
    return True, "Question added successfully."

def update_question(question_id: str, question_dict: Dict[str, Any]) -> Tuple[bool, str]:
    """Updates an existing question record after deduplication check."""
    if is_duplicate_question(question_dict["question"], exclude_id=question_id):
        return False, "Update rejected: Another question with identical normalized text already exists."
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE questions SET
        question = ?,
        intent = ?,
        source_type = ?,
        source_url = ?,
        market = ?,
        priority = ?,
        notes = ?,
        category = ?,
        source_status = ?,
        source_evidence = ?,
        source_accessibility = ?
    WHERE question_id = ?
    """, (
        question_dict["question"],
        question_dict["intent"],
        question_dict["source_type"],
        question_dict["source_url"],
        question_dict["market"],
        question_dict.get("priority", "Medium"),
        question_dict.get("notes", ""),
        question_dict.get("category", "Video Repurposing & Clipping"),
        question_dict.get("source_status", "VERIFIED"),
        question_dict.get("source_evidence", ""),
        question_dict.get("source_accessibility", "ACCESSIBLE"),
        question_id
    ))
    conn.commit()
    conn.close()
    return True, f"Question {question_id} updated successfully."

def delete_question(question_id: str) -> Tuple[bool, str]:
    """Deletes a question and associated measurement provenance records."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions WHERE question_id = ?", (question_id,))
    cursor.execute("DELETE FROM measurements WHERE question_id = ?", (question_id,))
    cursor.execute("DELETE FROM provenance_records WHERE question_id = ?", (question_id,))
    conn.commit()
    conn.close()
    return True, f"Question {question_id} and associated measurements deleted successfully."

def export_questions_to_csv() -> str:
    """Exports all questions to CSV formatted string."""
    questions = get_all_questions()
    output = io.StringIO()
    if not questions:
        return ""
    writer = csv.DictWriter(output, fieldnames=list(questions[0].keys()))
    writer.writeheader()
    writer.writerows(questions)
    return output.getvalue()

def import_questions_from_csv(csv_text: str) -> Dict[str, int]:
    """Imports questions from CSV text, rejecting duplicates and auto-assigning IDs."""
    reader = csv.DictReader(io.StringIO(csv_text))
    added = 0
    skipped = 0
    all_q = get_all_questions()
    next_idx = len(all_q) + 1

    for row in reader:
        q_text = row.get("question", "").strip()
        if not q_text or is_duplicate_question(q_text):
            skipped += 1
            continue

        qid = row.get("question_id", "").strip() or f"Q{next_idx:03d}"
        next_idx += 1
        q_data = {
            "question_id": qid,
            "question": q_text,
            "intent": row.get("intent", "Informational"),
            "source_type": row.get("source_type", "Google Suggest"),
            "source_url": row.get("source_url", "https://www.google.com/search?q="),
            "market": row.get("market", "United States (US)"),
            "priority": row.get("priority", "Medium"),
            "notes": row.get("notes", "Imported via CSV"),
            "category": row.get("category", "Video Repurposing & Clipping"),
            "source_status": row.get("source_status", "UNVERIFIED"),
            "source_evidence": row.get("source_evidence", "CSV Import"),
            "source_accessibility": "ACCESSIBLE"
        }
        success, _ = add_question(q_data)
        if success:
            added += 1
        else:
            skipped += 1

    return {"added": added, "skipped": skipped}

# ------------------------------------------------------------------------------
# MEASUREMENT RUNS & PROVENANCE
# ------------------------------------------------------------------------------

def get_all_measurement_runs() -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM measurement_runs ORDER BY run_date DESC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def create_measurement_run(run_dict: Dict[str, Any]) -> Tuple[bool, str]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO measurement_runs (run_id, run_name, run_date, market, collection_method, status, total_questions, verified_records_count, demo_records_count, notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        run_dict["run_id"],
        run_dict["run_name"],
        run_dict["run_date"],
        run_dict.get("market", "US, UK, India"),
        run_dict.get("collection_method", "MANUAL_ENTRY"),
        run_dict.get("status", "ACTIVE"),
        run_dict.get("total_questions", 0),
        run_dict.get("verified_records_count", 0),
        run_dict.get("demo_records_count", 0),
        run_dict.get("notes", "")
    ))
    conn.commit()
    conn.close()
    return True, f"Measurement run {run_dict['run_id']} created."

def get_measurements_by_run_id(run_id: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
    SELECT m.*, q.question, q.intent, q.market, q.source_type, q.source_url, q.category
    FROM measurements m
    JOIN questions q ON m.question_id = q.question_id
    WHERE m.run_id = ?
    ORDER BY m.question_id ASC
    """, (run_id,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_measurements_by_date(run_date: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
    SELECT m.*, q.question, q.intent, q.market, q.source_type, q.source_url, q.category
    FROM measurements m
    JOIN questions q ON m.question_id = q.question_id
    WHERE m.run_date = ?
    ORDER BY m.question_id ASC
    """, (run_date,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def record_measurement(measurement: Dict[str, Any]) -> Tuple[bool, str]:
    """Records a single measurement with provenance tracking."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO measurements (
        question_id, run_id, run_date, collection_method, verification_status,
        search_depth, google_position, incubrix_found, answer_box,
        featured_snippet_present, people_also_ask_present, ai_overview_present,
        quoted_source, top_competitors, search_location, evidence_file_path,
        chatgpt, chatgpt_raw_answer, chatgpt_mention_sentence, chatgpt_citations, chatgpt_model,
        gemini, gemini_raw_answer, gemini_mention_sentence, gemini_citations, gemini_model,
        perplexity, perplexity_raw_answer, perplexity_mention_sentence, perplexity_citations, perplexity_model,
        claude, claude_raw_answer, claude_mention_sentence, claude_citations, claude_model,
        competitors_named, raw_answers_url
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        measurement["question_id"],
        measurement.get("run_id", "RUN-LIVE-MANUAL"),
        measurement["run_date"],
        measurement.get("collection_method", "MANUAL_ENTRY"),
        measurement.get("verification_status", "VERIFIED"),
        measurement.get("search_depth", 30),
        measurement.get("google_position", "Not in top 30"),
        measurement.get("incubrix_found", 0),
        measurement.get("answer_box", "None"),
        measurement.get("featured_snippet_present", 0),
        measurement.get("people_also_ask_present", 0),
        measurement.get("ai_overview_present", 0),
        measurement.get("quoted_source", ""),
        measurement.get("top_competitors", ""),
        measurement.get("search_location", "US"),
        measurement.get("evidence_file_path", ""),
        measurement.get("chatgpt", "Not Mentioned"),
        measurement.get("chatgpt_raw_answer", ""),
        measurement.get("chatgpt_mention_sentence", ""),
        measurement.get("chatgpt_citations", ""),
        measurement.get("chatgpt_model", "GPT-4o"),
        measurement.get("gemini", "Not Mentioned"),
        measurement.get("gemini_raw_answer", ""),
        measurement.get("gemini_mention_sentence", ""),
        measurement.get("gemini_citations", ""),
        measurement.get("gemini_model", "Gemini 1.5 Pro"),
        measurement.get("perplexity", "Not Mentioned"),
        measurement.get("perplexity_raw_answer", ""),
        measurement.get("perplexity_mention_sentence", ""),
        measurement.get("perplexity_citations", ""),
        measurement.get("perplexity_model", "Perplexity Sonar"),
        measurement.get("claude", "Not Mentioned"),
        measurement.get("claude_raw_answer", ""),
        measurement.get("claude_mention_sentence", ""),
        measurement.get("claude_citations", ""),
        measurement.get("claude_model", "Claude 3.5 Sonnet"),
        measurement.get("competitors_named", ""),
        measurement.get("raw_answers_url", "")
    ))
    conn.commit()
    conn.close()
    return True, "Measurement recorded."

def record_provenance_entry(prov: Dict[str, Any]):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO provenance_records (
        question_id, run_id, market, timestamp, engine_or_assistant,
        collection_method, raw_answer, evidence_file_path, source_urls,
        verification_status, audited_by
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        prov["question_id"],
        prov["run_id"],
        prov.get("market", "US"),
        prov.get("timestamp", datetime.datetime.now().isoformat()),
        prov.get("engine_or_assistant", "Google"),
        prov.get("collection_method", "MANUAL_ENTRY"),
        prov.get("raw_answer", ""),
        prov.get("evidence_file_path", ""),
        prov.get("source_urls", ""),
        prov.get("verification_status", "VERIFIED"),
        prov.get("audited_by", "Growth Engineer Auditor")
    ))
    conn.commit()
    conn.close()

def get_all_measurement_dates() -> List[str]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT run_date FROM measurements ORDER BY run_date ASC")
    dates = [r[0] for r in cursor.fetchall()]
    conn.close()
    return dates

# ------------------------------------------------------------------------------
# TECHNICAL FIXES, CONTENT PAGES, CITATIONS, LOGS
# ------------------------------------------------------------------------------

def get_all_fixes() -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM technical_fixes ORDER BY fix_id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_all_pages() -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM content_pages ORDER BY item_id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_all_citations() -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM citation_targets ORDER BY item_id ASC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_engine_logs(limit: int = 50) -> List[Dict[str, Any]]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM engine_logs ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def log_engine_event(event_type: str, message: str, items_processed: int = 0, duplicates_removed: int = 0, runtime_seconds: float = 0.0, cost_usd: float = 0.0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO engine_logs (timestamp, event_type, message, items_processed, duplicates_removed, runtime_seconds, cost_usd)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (datetime.datetime.now().isoformat(), event_type, message, items_processed, duplicates_removed, runtime_seconds, cost_usd))
    conn.commit()
    conn.close()
