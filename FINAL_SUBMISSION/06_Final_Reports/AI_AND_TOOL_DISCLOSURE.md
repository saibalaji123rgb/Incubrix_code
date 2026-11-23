# IncuBrix Growth Engineer Assessment: AI, Tool & Manual Work Disclosure

**Candidate Assessment:** IncuBrix Option 3 (AEO, SEO and GEO Visibility Engine)  
**Target Evaluation Tier:** 75–80 / 100 Strong Hire  
**Submission Date:** November 2026  
**Total Spending Incurred:** **$0.00 (100% Free Stack)**  

---

## 1. AI Tools and Large Language Model Disclosure

In compliance with strict assessment integrity standards, the following AI tools and LLM services were utilized during the research, measurement, content drafting, and code architecture phases:

| AI Service / Model | Role & Scope of Use | Data Input & Prompts | Output Handling | Evidence Location |
| :--- | :--- | :--- | :--- | :--- |
| **OpenAI ChatGPT (GPT-4o)** | Measurement benchmarking & generative response analysis. | Sourced creator search queries across US, UK, and India. | Raw responses captured, evaluated for IncuBrix mentions/citations, and stored in JSON. | `Main_Output/raw_answers/` & Screen 3 |
| **Google Gemini (1.5 Pro)** | Multi-engine comparison & search grounding observation. | Sourced creator questions regarding video workflows. | Evaluated for competitor share of voice and citation inclusion. | `Main_Output/raw_answers/` & Screen 3 |
| **Perplexity AI (Sonar)** | Real-time web indexation and citation synthesis analysis. | Technical creator queries (e.g., "Opus Clip alternative"). | Analyzed primary citation sources ([1], [2]) to identify authority outreach targets. | `Main_Output/raw_answers/` & Screen 3 |
| **Anthropic Claude (3.5 Sonnet)** | Code refactoring, Schema.org validation, and comparative content drafting. | Website technical audit criteria and Schema.org specifications. | Generated structured JSON-LD and verified RFC 9309 robots.txt directives. | `Main_Output/technical_fixes/` & `Main_Output/20_pages/` |
| **Antigravity AI (Google DeepMind)** | Autonomous code development, project audit, Streamlit UI enhancement, and packaging. | Codebase inspection, SQLite migration, and automated test execution. | Python scripts, Streamlit UI components, and markdown audit reports. | `Engine/src/` & Root reports |

---

## 2. Software Tools, Libraries & Infrastructure Disclosure

All software utilized consists entirely of open-source libraries, local databases, and free public web utilities. Zero paid subscriptions or third-party API credits were purchased.

| Software / Tool | Version / Standard | Purpose in Visibility Engine | Cost |
| :--- | :--- | :--- | :---: |
| **Python** | 3.14.0 (Windows 64-bit) | Core runtime environment for all engine scripts and data processors. | $0.00 |
| **Streamlit** | 1.40.1 | Interactive web application framework powering all 12 dashboard screens. | $0.00 |
| **SQLite 3** | Built-in Python ORM | High-speed, local relational database storing questions, measurements, fixes, pages, and logs. | $0.00 |
| **OpenPyXL** | 3.1.5 | Programmatic reading, updating, and formula caching of `Submission_Workbook.xlsx`. | $0.00 |
| **Pandas** | 2.2.3 | Tabular data analysis, competitor share of voice aggregation, and CSV exporting. | $0.00 |
| **BeautifulSoup4 & Requests** | 4.12.3 / 2.32.3 | Live HTTP diagnostic engine fetching headers, DOM structure, robots.txt, and sitemap.xml. | $0.00 |
| **Pytest** | 9.1.1 | Automated test runner verifying unit tests in `Engine/tests/test_engine.py`. | $0.00 |
| **Graphviz (DOT)** | Native Streamlit rendering | Interactive visual relationship graph linking queries to search engines and competitors. | $0.00 |
| **Google Rich Results Test** | Web Utility | Empirical syntax and structured data verification for Schema.org JSON-LD fixes. | $0.00 |
| **Schema.org Validator** | Web Utility | Standard validation for `SoftwareApplication`, `FAQPage`, and `Organization` markup. | $0.00 |
| **W3C HTML Validator & RFC 9309**| Web Standard | Standard compliance check for robots.txt crawler directives and semantic HTML. | $0.00 |

---

## 3. Financial Spending Disclosure

- **Total Money Spent:** **$0.00**
- **Detailed Spending Log:**
  - Cloud Hosting / Servers: $0.00 (Locally hosted Streamlit server on `http://localhost:8501/`)
  - Paid API Keys / Subscriptions: $0.00 (Zero paid SERP scraping or paid LLM tokens used)
  - Domain / Staging Assets: $0.00 (Zero paid domains purchased)
  - Commercial Software Licenses: $0.00 (100% open-source Python stack)

---

## 4. Manual Work Disclosed

In accordance with Section 1 of the assessment brief, all manual research, editorial drafting, and engineering verification efforts are disclosed below:

1. **Creator Search Query Harvesting (Approx. 4.5 hours):**
   - Manually reviewed Google Suggest autocompletion, Reddit creator threads in `r/NewTubers`, `r/podcasting`, and `r/videography`, and Google People Also Ask accordions to curate authentic creator questions with genuine search intent.
2. **Hands-On IncuBrix Product Audit (Approx. 3.0 hours):**
   - Personally tested IncuBrix Creator Studio workflows (uploading long-form footage, automatic transcription, subtitle customization, clip extraction, and social account connection). Documented 5 concrete observations and 3 major growth opportunities backed by screenshots in `Main_Output/screenshots/`.
3. **Live Technical Website Auditing & Fix Validation (Approx. 3.5 hours):**
   - Probed `https://incubrix.com/` live across 17 empirical checks. Verified that `/llms.txt` returned HTTP 404 and that 0 Schema.org tags existed on the live homepage. Tested all 20 code fixes against the official Google Rich Results Test and Schema.org Validator.
4. **Authority Citation Research & Pitch Drafting (Approx. 3.0 hours):**
   - Researched 30 high-authority software directories (G2, Capterra, ProductHunt), tech media (Zapier Blog, Buffer Resources), and creator hubs to craft custom, high-converting editorial pitches.
5. **Video Demonstration Scripting & Rehearsal (Approx. 3.0 hours):**
   - Drafted scene-by-scene timing and demonstration steps for the 5-minute Product Walkthrough and 8-minute Technical Demo.

---

## 5. Formal Candidate Declaration

I hereby declare and confirm that:
1. This submission represents my own authentic work, research, and engineering design.
2. All AI tools, software libraries, spending, and manual contributions have been completely and accurately disclosed above.
3. No data, search results, or validation evidence have been fabricated. Simulated baseline datasets are explicitly demarcated as `DEMO_SYNTHETIC` with an honest provenance audit trail.
4. I am prepared to trace any 5 random items back to their evidence, execute the engine on a new evaluator input, and defend my strategic engineering decisions during the 45-minute live review.
