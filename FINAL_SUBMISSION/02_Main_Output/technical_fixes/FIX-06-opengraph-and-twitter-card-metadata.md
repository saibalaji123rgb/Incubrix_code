# FIX-06: Add complete OpenGraph and Twitter summary_large_image meta tags with 1200x630px high-resolution banner.

**Target Page:** `https://incubrix.com/`  
**Impact:** `Medium` | **Effort:** `Low`  
**Validator:** `Twitter Card Validator & OpenGraph.xyz` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-06_og_cards.png`  

---

## 1. Problem Description
Missing explicit OpenGraph and Twitter Card social metadata, causing degraded image previews when shared across Twitter/X, LinkedIn, Discord, and Slack.

---

## 2. Recommended Solution
Add complete OpenGraph and Twitter summary_large_image meta tags with 1200x630px high-resolution banner.

---

## 3. Ready-to-Paste Code / Text
```html
<!-- Open Graph Metadata -->
<meta property="og:type" content="website" />
<meta property="og:url" content="https://incubrix.com/" />
<meta property="og:title" content="IncuBrix - The AI CreatorOS for Video Editing & Repurposing" />
<meta property="og:description" content="Turn 1 long video into 10 viral clips, auto-generate animated captions, and schedule across all social channels from one screen." />
<meta property="og:image" content="https://incubrix.com/assets/images/og-preview-1200x630.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:site_name" content="IncuBrix" />

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@incubrix" />
<meta name="twitter:creator" content="@incubrix" />
<meta name="twitter:title" content="IncuBrix - The AI CreatorOS for Video Editing & Repurposing" />
<meta name="twitter:description" content="Edit video by editing text, clip viral shorts automatically, and publish everywhere." />
<meta name="twitter:image" content="https://incubrix.com/assets/images/og-preview-1200x630.png" />

```

---

## 4. Validation & Verification
- **Validator Tool:** Twitter Card Validator & OpenGraph.xyz
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
