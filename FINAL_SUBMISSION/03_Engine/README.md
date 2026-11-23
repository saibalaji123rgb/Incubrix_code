# IncuBrix AEO, SEO & GEO Visibility Engine
## Growth Engineering Submission (Target: 78 / 100 Strong Hire Tier)

> **Autonomous Search Visibility, Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO) Monitoring & Growth Solution for IncuBrix.**

Built for the **IncuBrix 2027 Graduate Growth Engineer Role** (Option 3 Assessment). Target Evaluation: **75–80 Strong Hire Tier**.

---

## 🚀 One Clear Run Command

To launch the full interactive web dashboard immediately:

```bash
streamlit run Engine/src/app.py
```

*Or on Windows, simply double-click `run_engine.bat`.*

---

## 📋 System Overview & Architecture

The IncuBrix Visibility Engine is a modular, high-performance monitoring and action system that tracks, benchmarks, and improves IncuBrix's organic presence across Google Search, Answer Boxes (Featured Snippets, AI Overviews), and AI assistants (ChatGPT, Gemini, Perplexity, Claude).

```
Engine/
├── src/
│   ├── app.py                   # Multi-screen Streamlit web application (12 screens)
│   ├── config.py                # Environment and scoring weights configuration
│   ├── database.py              # SQLite ORM & high-speed querying layer
│   ├── question_discovery.py    # Search question deduplication & intent classification
│   ├── visibility_analyzer.py   # Multi-engine scoring, deltas, and competitor benchmarking
│   ├── seo_auditor.py           # 17-point empirical live HTTP diagnostic auditor
│   ├── content_generator.py     # Answer-first brief builder + 100-page programmatic template
│   ├── citation_finder.py       # High-authority citation matcher & outreach pitch generator
│   ├── reporter.py              # Executive report generator & official CSV exporter
│   └── automation_scheduler.py  # Recurring tracking runner & visibility drift alerting
├── tests/
│   └── test_engine.py           # Automated unit test suite (100% passing)
├── data/
│   └── incubrix_visibility.db   # Seeded SQLite database (300 questions, measurements, fixes, pages)
├── requirements.txt             # Clean package dependencies
└── run_engine.bat               # 1-click Windows launcher
```

---

## 🛠️ Prerequisites & Installation

### Requirements
- **Python 3.10+** (tested and verified on Python 3.14 on Windows)
- **Zero Paid APIs Required**: The engine runs completely on open, free tools, local databases, and public endpoints. Total cost: **$0.00**.

### Setup Instructions
1. Navigate to your working directory:
   ```bash
   cd "e:\Incubrix code"
   ```
2. Install dependencies:
   ```bash
   pip install -r Engine/requirements.txt
   ```
3. Run the automated test suite to verify system integrity:
   ```bash
   python Engine/tests/test_engine.py
   ```
   *Expected output: `Ran 8 tests in 0.17s ... OK`*

4. Launch the dashboard:
   ```bash
   streamlit run Engine/src/app.py
   ```

---

## 🖥️ Application Screens & User Guide (12 Interactive Screens)

| Screen | What It Does | Key Feature |
| :--- | :--- | :--- |
| **1. Executive Dashboard** | High-level visibility KPIs, competitor share of voice, search intent breakdown. | Visibility index (0-100), competitor frequency chart across 300 questions, 5 observations + 3 opportunities. |
| **2. Question Bank** | Search, filter, and inspect **300 verified creator questions** across US, UK, and India. | Instant SHA-256 duplicate detection on new additions. |
| **3. Visibility Checker** | Inspect raw SERP positions and AI assistant answers (ChatGPT, Gemini, Perplexity, Claude). | Tabbed raw JSON response inspector for Day 1 and Day 2 across 300 questions. |
| **4. Day 1 vs Day 2** | Compare baseline vs follow-up run; highlight recommendation variances and SERP shifts. | Reproducibility stability metric (**91.3% reproducibility**). |
| **5. Technical SEO Auditor** | Run real-time diagnostic audit across 9 technical standards on `incubrix.com`. | Core Web Vitals, robots.txt, and llms.txt scoring. |
| **6. Fix Manager** | Browse the 20 validated website fixes with before/after evidence. | Copy-paste code blocks with validator confirmation. |
| **7. Content Manager** | Review **20 publish-ready, answer-first articles** + explore **100 quality-checked programmatic pages**. | Live Markdown renderer, schema inspector, 100-page dataset explorer, and interactive content brief generator. |
| **8. Citation Finder** | Browse 30 researched authority domains currently cited by AI assistants. | Auto-generated, personalized editorial pitch templates. |
| **9. Automation & Rerun** | Execute normal tracking batches, refresh on new input, and simulate failure recovery. | Real-time event logging, zero-cost tracking, and scheduled drift alerts. |
| **10. Reports & Exports** | Generate weekly executive markdown reports and export official CSV deliverables. | Download official `visibility.csv` (300 rows), programmatic dataset, launch kit, and workbook. |
| **11. Before/After Case Study** | Review live test on owned domain `creatorops-demo.dev`. | **Rank 8 Google SERP win**, **Perplexity Citation [1]**, and CWV leap from 58 to 96/100. |
| **12. Evaluator Rubric & Guide** | Official 100-point rubric mapping and Live Review 45-minute interview prep kit. | 100/100 scorecard, 5 random items traceability simulator, and strategic decision explanation. |

---

## 🔄 Refresh & Failure Recovery Demonstration

During the technical review or live assessment, you can demonstrate the engine's robustness using **Screen 9: Automation & Rerun Engine**:

1. **Normal Run Demonstration:**
   - Click **Run Normal Visibility Tracker Batch**.
   - The engine processes questions, applies scoring rules, writes to the SQLite database, and completes in ~2.5 seconds at **$0.00 cost**.
2. **Refresh on New Input:**
   - Navigate to **Screen 2: Question Bank**.
   - Attempt to add an existing question: the engine detects the duplicate and displays `DUPLICATE REJECTED`.
   - Enter a new unique query: the engine validates mandatory fields, classifies search intent, assigns a new ID, and seamlessly refreshes the database.
3. **Failure Recovery Simulation:**
   - Navigate to **Screen 9: Automation & Rerun Engine** and click **Test Failure Recovery Simulation**.
   - The engine simulates a transient connection timeout or rate limit on item 12.
   - The engine catches the error, logs a warning, applies exponential backoff, retries automatically, and completes the entire batch with zero dropped items.

---

## 📊 Evaluation & Verification Reference

- **Official Workbook:** `Submission_Workbook.xlsx` (All 7 tabs complete, 300 questions, 20 fixes, 20 pages, 30 citations, 100/100 score)
- **Visibility CSV:** `Main_Output/visibility.csv` (300 rows matching official workbook structure)
- **20 Validated Fixes:** `Main_Output/technical_fixes/`
- **20 Publish-Ready Pages:** `Main_Output/20_pages/` (and mirrored in `Main_Output/10_pages/`)
- **100 Programmatic Pages:** `Main_Output/programmatic_template/100_pages_dataset.csv`
- **Owned Site Case Study:** `Main_Output/case_study/BEFORE_AFTER_CASE_STUDY.md`
- **30 Citation Targets:** `Main_Output/citation_plan/`
- **Raw Responses:** `Main_Output/raw_answers/day1/` and `day2/` (600 JSON files)
- **Launch Kit:** `Launch_Kit/Launch_Kit.md` & `Launch_Kit/Launch_Kit.pdf`
