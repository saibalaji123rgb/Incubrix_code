# FIX-04: Add Schema.org Organization structured data with official brand identifiers, contact points, founder details, and sameAs links.

**Target Page:** `https://incubrix.com/about`  
**Impact:** `Medium` | **Effort:** `Low`  
**Validator:** `Google Rich Results Test` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-04_schema_org.png`  

---

## 1. Problem Description
About page lacks structured Organization and Brand schema with sameAs social profile verification, hindering Google Knowledge Graph entity formation.

---

## 2. Recommended Solution
Add Schema.org Organization structured data with official brand identifiers, contact points, founder details, and sameAs links.

---

## 3. Ready-to-Paste Code / Text
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "IncuBrix Private Limited",
  "alternateName": "IncuBrix",
  "url": "https://incubrix.com",
  "logo": "https://incubrix.com/assets/images/incubrix-logo.png",
  "foundingDate": "2024",
  "founder": {
    "@type": "Person",
    "name": "Kamraj Subramanian"
  },
  "sameAs": [
    "https://www.linkedin.com/company/incubrix",
    "https://twitter.com/incubrix",
    "https://www.youtube.com/@incubrix",
    "https://www.instagram.com/incubrix"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "contact@incubrix.com",
    "contactType": "Customer Support"
  }
}
</script>
```

---

## 4. Validation & Verification
- **Validator Tool:** Google Rich Results Test
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
