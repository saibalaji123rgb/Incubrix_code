# FIX-03: Implement comprehensive Schema.org SoftwareApplication JSON-LD markup on homepage and product landing pages.

**Target Page:** `https://incubrix.com/`  
**Impact:** `High` | **Effort:** `Low`  
**Validator:** `Google Rich Results Test & Schema.org Validator` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-03_schema_software.png`  

---

## 1. Problem Description
Homepage lacks Schema.org SoftwareApplication structured data, preventing Google from generating software rich snippets, aggregate ratings, and operating system attributes in SERPs.

---

## 2. Recommended Solution
Implement comprehensive Schema.org SoftwareApplication JSON-LD markup on homepage and product landing pages.

---

## 3. Ready-to-Paste Code / Text
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "IncuBrix",
  "applicationCategory": "MultimediaApplication",
  "operatingSystem": "Web, Windows, macOS, iOS, Android",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Free tier with 300 credits/mo; paid plans from $10/mo to $250/mo"
  },
  "description": "All-in-one CreatorOS for text-based video editing, viral short clipping, automated captions, and cross-platform publishing.",
  "url": "https://incubrix.com/",
  "publisher": {
    "@type": "Organization",
    "name": "IncuBrix Private Limited",
    "url": "https://incubrix.com"
  }
}
</script>
```

---

## 4. Validation & Verification
- **Validator Tool:** Google Rich Results Test & Schema.org Validator
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
