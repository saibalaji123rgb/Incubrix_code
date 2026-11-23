# FIX-15: Inject BreadcrumbList JSON-LD structured data on all feature, pricing, and article subpages.

**Target Page:** `https://incubrix.com/features/video-repurposing`  
**Impact:** `Medium` | **Effort:** `Low`  
**Validator:** `Google Rich Results Test` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-15_breadcrumbs.png`  

---

## 1. Problem Description
Deep product pages lack Schema.org BreadcrumbList markup, resulting in raw URL strings instead of clean category breadcrumbs in Google mobile SERPs.

---

## 2. Recommended Solution
Inject BreadcrumbList JSON-LD structured data on all feature, pricing, and article subpages.

---

## 3. Ready-to-Paste Code / Text
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://incubrix.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Features",
      "item": "https://incubrix.com/features"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Video Repurposing",
      "item": "https://incubrix.com/features/video-repurposing"
    }
  ]
}
</script>
```

---

## 4. Validation & Verification
- **Validator Tool:** Google Rich Results Test
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
