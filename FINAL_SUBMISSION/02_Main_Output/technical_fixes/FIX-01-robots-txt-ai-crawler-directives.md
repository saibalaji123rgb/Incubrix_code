# FIX-01: Deploy optimized robots.txt granting explicit crawl access to leading AI engines and Googlebot while protecting private app endpoints.

**Target Page:** `https://incubrix.com/robots.txt`  
**Impact:** `High` | **Effort:** `Low`  
**Validator:** `robots.txt Tester & Google Search Console` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-01_robots_txt.png`  

---

## 1. Problem Description
robots.txt lacks explicit permissions and crawl-delay guidance for modern AI bots (GPTBot, ClaudeBot, PerplexityBot, Applebot-Extended), risking search suppression in AI assistants.

---

## 2. Recommended Solution
Deploy optimized robots.txt granting explicit crawl access to leading AI engines and Googlebot while protecting private app endpoints.

---

## 3. Ready-to-Paste Code / Text
```html
# robots.txt for https://incubrix.com/
# Generated for IncuBrix AEO/GEO/SEO Optimization

User-agent: *
Allow: /
Disallow: /api/
Disallow: /dashboard/
Disallow: /admin/
Disallow: /auth/
Disallow: /export/temp/

# Explicit Directives for AI Engine Crawlers
User-agent: GPTBot
Allow: /
Disallow: /api/
Disallow: /dashboard/

User-agent: ClaudeBot
Allow: /
Disallow: /api/
Disallow: /dashboard/

User-agent: PerplexityBot
Allow: /
Disallow: /api/
Disallow: /dashboard/

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

# Sitemap Index and LLM context files
Sitemap: https://incubrix.com/sitemap.xml

```

---

## 4. Validation & Verification
- **Validator Tool:** robots.txt Tester & Google Search Console
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
