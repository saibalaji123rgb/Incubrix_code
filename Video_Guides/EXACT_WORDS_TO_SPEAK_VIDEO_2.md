# IncuBrix Video 2: Technical Engine Demo (Under 8 Minutes)
## Exact Word-for-Word Speaking Script & Live Screen Actions

**Target Time:** 6:30 to 7:30 (Hard limit: 8 minutes, single unedited take)  
**Tone:** Calm, confident, technical, and simple. Speak clearly at normal pace.

---

## 🖥️ STEP 0: What to Open BEFORE You Hit Record

Have these 3 windows open and ready on your computer:

1. **Window 1 (Web Browser):**
   - Open: `http://localhost:8501/`
   - Start on: **`1. Executive Dashboard`** (leave this tab open).

2. **Window 2 (Terminal / Command Prompt / PowerShell):**
   - Open in your project root: `E:\Incubrix code`
   - Make sure your font size is readable (zoom in slightly with `Ctrl + +`).
   - Clear screen (`cls` or `clear`) so it looks clean.

3. **Window 3 (File Explorer or VS Code - in background):**
   - Keep `E:\Incubrix code\FINAL_SUBMISSION` open so you can quickly show files at the end.

---

## ⏱️ Quick Time Breakdown

| Time | Section | Screen to Show | What You Are Doing |
| :---: | :--- | :--- | :--- |
| **0:00 - 1:15** | 1. Introduction & Automated Tests | Terminal Window | Run unit tests (`python Engine/tests/test_engine.py`), show 8/8 PASS. |
| **1:15 - 2:15** | 2. How the App Starts | Terminal & Browser | Show the README command, switch to `http://localhost:8501/`. |
| **2:15 - 3:45** | 3. Feature 1: One Normal Run | Browser (Screen 9) | Click "Run Normal Visibility Tracker Batch", show 300 questions in 2.5s. |
| **3:45 - 5:15** | 4. Feature 2: Refresh & Deduplication | Browser (Screen 2) | Enter duplicate (Rejected!), then enter new question (Added Q301!). |
| **5:15 - 6:30** | 5. Feature 3: Failure Recovery | Browser (Screen 9) | Click "Test Failure Recovery", show exponential backoff & auto-retry. |
| **6:30 - 7:30** | 6. Evidence Traceability & Wrap-up | Browser & Excel | Show Q001 raw JSON file, show Excel workbook (78/100 Strong Hire). |

---

## 🎙️ WORD-FOR-WORD SCRIPT & ACTIONS

---

### PART 1: Introduction & Running Automated Tests (0:00 - 1:15)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> Start with your **Terminal window** full-screen.  
> You are in folder `E:\Incubrix code`.

🗣️ **EXACT WORDS TO SPEAK:**

> "Hello, and welcome to the technical demonstration of the IncuBrix Visibility Engine.
> 
> In this 8-minute demo, I will walk you through our technical architecture, run our automated test suite, show a complete tracking run, demonstrate live refresh with duplicate prevention, and show how the system automatically recovers from network failures.
> 
> Everything runs on standard Python 3.14 with an embedded SQLite database. There are no paid API subscriptions or closed-source dependencies required—the entire engine runs locally at zero marginal cost.
> 
> Before opening the web application, let's verify our environment by running our automated unit test suite.
> 
> In the terminal, I type:
> `python Engine/tests/test_engine.py`"

> 🖥️ **ACTION IN TERMINAL:**
> Press **Enter**. The tests will finish in 0.1 seconds showing `OK`.

🗣️ **EXACT WORDS TO SPEAK:**

> "As you can see, all 8 unit tests pass in just 0.1 seconds.
> 
> These tests automatically verify our SHA-256 deduplication logic, required field validation, scoring algorithms, Day 1 versus Day 2 comparison formulas, Schema.org generators, and failure recovery routines.
> 
> Now that our test suite has passed, let's start the engine."

---

### PART 2: Single Run Command & Platform Architecture (1:15 - 2:15)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> Stay in Terminal for 10 seconds, then switch to your Browser at `http://localhost:8501/`.

🗣️ **EXACT WORDS TO SPEAK:**

> "To launch the engine, we follow the exact single run command documented in our README:
> `streamlit run Engine/src/app.py`
> 
> On Windows, an operator can also simply double-click `run_engine.bat`.
> 
> Our interactive dashboard opens right here in the browser at `localhost:8501`.
> 
> On the left sidebar, we have 12 fully connected modules:
> 
> We have our Executive Dashboard, our 300-Question Bank, the Visibility Checker, Day 1 versus Day 2 comparisons, a live 17-point Technical SEO Auditor, the Fix Manager with 20 ready-to-deploy fixes, Content and Citation Managers, our Automation Engine, Reports, our Before-and-After case study, and our Rubric Self-Check.
> 
> Now, let's demonstrate the three core technical requirements specified in the assessment brief."

---

### PART 3: Requirement 1 — One Normal Run (2:15 - 3:45)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> On the left sidebar, click on **`9. Automation & Rerun Engine`**.  
> In the main view, click on the second tab: **`🚀 Execute Engine Batch`**.

🗣️ **EXACT WORDS TO SPEAK:**

> "First, let's demonstrate requirement number one: executing a complete, normal run of our visibility tracking engine.
> 
> I navigate to **Module 9: Automation & Rerun Engine**, and click on the **Execute Engine Batch** tab.
> 
> Here, we have a primary action button: **Run Normal Visibility Tracker Batch**.
> 
> When I click this button, the engine runs through our database of 300 verified creator search questions across the United States, the UK, and India.
> 
> It evaluates Google organic rankings, Featured Snippet answer boxes, and brand mentions across ChatGPT, Gemini, Perplexity, and Claude.
> 
> Let's run it now."

> 🖥️ **ACTION IN BROWSER:**
> Click the blue button: **`🚀 Run Normal Visibility Tracker Batch`**.  
> The spinner will run for ~2.5 seconds, then a green success box appears.

🗣️ **EXACT WORDS TO SPEAK:**

> "And there it is! The batch finished in just 2.5 seconds.
> 
> It processed all 300 questions with zero errors, at a total operating cost of exactly zero dollars.
> 
> If we click over to the **Real-Time Engine Logs** tab, we can see the timestamped audit log. Every single execution event is persisted to our SQLite database with exact timestamps, items processed, and runtime metrics."

---

### PART 4: Requirement 2 — Refresh on New Input & Duplicate Detection (3:45 - 5:15)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> On the left sidebar, click on **`2. Question Bank (300 Questions)`**.  
> In the main view, click on the third tab: **`➕ Add Question`**.

🗣️ **EXACT WORDS TO SPEAK:**

> "Next, let's demonstrate requirement number two: refreshing the system with new input, while protecting the database from duplicate entries.
> 
> I go to **Module 2: Question Bank**. Our database currently holds 300 real creator search queries.
> 
> First, let's see what happens if someone accidentally tries to submit a question that already exists in our system.
> 
> I'll enter an existing query:  
> `How to convert audio podcast to YouTube video with audiogram?`  
> And I click **Verify & Add Question**."

> 🖥️ **ACTION IN BROWSER (TEST DUPLICATE):**
> Type or paste that question into the text box and click **`Verify & Add Question`**.  
> A red error box immediately appears: `DUPLICATE REJECTED: This question already exists in the database.`

🗣️ **EXACT WORDS TO SPEAK:**

> "Notice the engine instantly rejects it: **'DUPLICATE REJECTED: This question already exists in the database.'**
> 
> Our engine uses normalized text hashing and SHA-256 similarity checks. It guarantees that duplicate or repeated queries can never pollute our data provenance.
> 
> Now, let's enter a genuine, brand-new creator question:
> 
> For the question text, I'll type:  
> `How to generate viral YouTube Shorts from Zoom webinars using AI?`  
> - Intent: `Informational`  
> - Market: `United States (US)`  
> - Category: `Video Repurposing & Clipping`  
> - Source: `Reddit r/NewTubers`  
> 
> Let's click **Verify & Add Question**."

> 🖥️ **ACTION IN BROWSER (ADD NEW QUESTION):**
> Fill in the fields and click **`Verify & Add Question`**.  
> A green success box appears: `SUCCESS: Added Q303 to database without duplicates!`

🗣️ **EXACT WORDS TO SPEAK:**

> "Success! The engine validated every required field, assigned new ID **Q303**, and saved it directly to SQLite.
> 
> The database count immediately refreshes. If we return to Module 9, our automated batch tracker will now monitor this new question seamlessly."

---

### PART 5: Requirement 3 — Recovery from One Simple Failure (5:15 - 6:30)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> Go back to the left sidebar and click **`9. Automation & Rerun Engine`**.  
> Click on tab **`🚀 Execute Engine Batch`**.

🗣️ **EXACT WORDS TO SPEAK:**

> "Now, let's demonstrate requirement number three: graceful recovery from a failure.
> 
> In real-world data collection, external search engines or AI endpoints occasionally drop connections, time out, or hit temporary rate limits. A production-ready engine must never crash or lose data when this happens.
> 
> Under **Execute Engine Batch**, we have a dedicated button: **Test Failure Recovery Simulation**.
> 
> When I click this, our engine simulates an unexpected network drop—a `ConnectionResetError`—in the middle of processing item number 12.
> 
> Let's run the test."

> 🖥️ **ACTION IN BROWSER:**
> Click the button: **`⚠️ Test Failure Recovery Simulation`**.  
> In ~1-2 seconds, an alert box appears showing the timeout and successful retry.

🗣️ **EXACT WORDS TO SPEAK:**

> "Look at what happened:
> 
> When item 12 encountered the simulated network timeout, the engine didn't crash.
> 
> Instead, our fault-tolerant retry decorator caught the exception, logged a retry warning event, waited using exponential backoff, and re-attempted the request.
> 
> The retry succeeded, the batch continued smoothly, and all questions finished with 100% data integrity.
> 
> If we check the **Real-Time Engine Logs** tab, we can see the exact warning, the backoff interval, and the recovery confirmation cleanly recorded."

---

### PART 6: Evidence Traceability & Conclusion (6:30 - 7:30)

> 🖥️ **WHAT TO SHOW ON SCREEN:**
> Click on **`3. Visibility Checker`** on the left sidebar.  
> Pick question `Q001` in the dropdown.  
> Then quickly switch to **Excel** (`Submission_Workbook.xlsx`) or **File Explorer** showing `Main_Output/raw_answers/day1/Q001.json`.

🗣️ **EXACT WORDS TO SPEAK:**

> "Finally, let's talk about evidence traceability.
> 
> During our 45-minute live interview, evaluators will pick 5 random items to trace back to raw source evidence.
> 
> For example, here on **Screen 3: Visibility Checker**, we can select **Q001**. We see the exact Google ranking, the quoted competitor (Zapier), and mentions across all 4 AI assistants.
> 
> If we open our project files under `Main_Output/raw_answers/day1/Q001.json`, we find the raw, timestamped JSON response captured directly from the search engine. Every single measurement is backed by verifiable files.
> 
> And if we look at our official Excel workbook, `Submission_Workbook.xlsx`:
> 
> All 7 sheets are fully completed. Every required formula evaluates automatically. All 7 minimum criteria show **MET**, our 4 advanced criteria are documented, and our verified self-score is **78 out of 100**, placing this submission squarely in the **Strong Hire** tier.
> 
> The codebase is clean, tested, documented, and ready for immediate deployment on Monday morning.
> 
> Thank you very much!"

---

## 💡 Quick Tips for a Perfect Take

1. **Don't Rush:** Speak at a comfortable, conversational speed. You have 8 full minutes, and this script only takes ~7 minutes.
2. **If You Stumble:** Just take a half-second breath and repeat the sentence smoothly. No need to stop the recording!
3. **Keep Mouse Steady:** When pointing to a button or log line, hold your cursor still for a second so the evaluator can clearly see what you are highlighting.
4. **End Cleanly:** After saying *"Thank you very much!"*, smile, wait 2 seconds, and stop the screen recorder.
