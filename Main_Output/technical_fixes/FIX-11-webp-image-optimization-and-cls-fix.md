# FIX-11: Convert raster assets to modern WebP format and specify width/height dimensions on all <img> elements to stabilize layout.

**Target Page:** `https://incubrix.com/`  
**Impact:** `High` | **Effort:** `Medium`  
**Validator:** `Google PageSpeed Insights (Core Web Vitals)` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-11_image_cls.png`  

---

## 1. Problem Description
Hero illustration and feature screenshots use heavy uncompressed PNGs (>1.8MB) lacking explicit width and height attributes, inflating Cumulative Layout Shift (CLS: 0.28).

---

## 2. Recommended Solution
Convert raster assets to modern WebP format and specify width/height dimensions on all <img> elements to stabilize layout.

---

## 3. Ready-to-Paste Code / Text
```html
<!-- Modern WebP picture markup with explicit dimensions -->
<picture>
  <source srcset="/assets/images/hero-dashboard.webp" type="image/webp" />
  <img src="/assets/images/hero-dashboard.png" 
       alt="IncuBrix AI CreatorOS Dashboard with video text editing and repurposing workspace" 
       width="1200" 
       height="675" 
       fetchpriority="high" 
       class="hero-img" />
</picture>

```

---

## 4. Validation & Verification
- **Validator Tool:** Google PageSpeed Insights (Core Web Vitals)
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
