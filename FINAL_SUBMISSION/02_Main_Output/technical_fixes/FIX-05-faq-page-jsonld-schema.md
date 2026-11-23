# FIX-05: Implement Schema.org FAQPage JSON-LD on pricing and feature pages to enable expandable question cards in Google SERPs.

**Target Page:** `https://incubrix.com/pricing`  
**Impact:** `High` | **Effort:** `Low`  
**Validator:** `Google Rich Results Test` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-05_faq_schema.png`  

---

## 1. Problem Description
Pricing page FAQs are rendered in unstructured HTML, disqualifying them from Google Featured Snippets and FAQ accordion rich results.

---

## 2. Recommended Solution
Implement Schema.org FAQPage JSON-LD on pricing and feature pages to enable expandable question cards in Google SERPs.

---

## 3. Ready-to-Paste Code / Text
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is there a free plan for IncuBrix?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, IncuBrix offers a permanent free tier that includes 30 export minutes per month, text-based editing, and basic AI captioning with no credit card required."
      }
    },
    {
      "@type": "Question",
      "name": "How does IncuBrix compare to Opus Clip and Descript?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unlike Opus Clip which focuses solely on clipping or Descript which focuses on editing, IncuBrix combines text-based editing, multi-format clip repurposing, AI music generation, and direct multi-platform social scheduling into a single unified CreatorOS."
      }
    },
    {
      "@type": "Question",
      "name": "Can I publish directly to YouTube, TikTok and LinkedIn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, IncuBrix integrates official APIs to schedule and publish video content directly to YouTube Shorts, Instagram Reels, TikTok, LinkedIn, and Bluesky."
      }
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
