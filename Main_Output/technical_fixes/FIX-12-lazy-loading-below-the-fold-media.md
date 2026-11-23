# FIX-12: Apply native loading='lazy' and decoding='async' to all below-the-fold screenshots and video demonstrations.

**Target Page:** `https://incubrix.com/features`  
**Impact:** `High` | **Effort:** `Low`  
**Validator:** `Google PageSpeed Insights` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-12_lazy_loading.png`  

---

## 1. Problem Description
Features page eagerly downloads 14 demonstration GIF and video files on initial page load, degrading Largest Contentful Paint (LCP: 4.8s).

---

## 2. Recommended Solution
Apply native loading='lazy' and decoding='async' to all below-the-fold screenshots and video demonstrations.

---

## 3. Ready-to-Paste Code / Text
```html
<!-- Apply to all below-the-fold images and videos -->
<img src="/assets/images/feature-repurpose-clip.webp" 
     alt="Automated 9:16 vertical short clip generation" 
     width="600" 
     height="400" 
     loading="lazy" 
     decoding="async" />

```

---

## 4. Validation & Verification
- **Validator Tool:** Google PageSpeed Insights
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
