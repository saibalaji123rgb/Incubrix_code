# FIX-20: Add Schema.org VideoObject JSON-LD markup and WebVTT caption tracks to all on-page demo videos to earn Google Key Moments badges.

**Target Page:** `https://incubrix.com/features/video-repurposing`  
**Impact:** `High` | **Effort:** `Medium`  
**Validator:** `Google Rich Results Test (VideoObject)` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-20_video_schema.png`  

---

## 1. Problem Description
Product demo videos are embedded using basic HTML5 <video> tags without VideoObject Schema or WebVTT transcript sidecars, rendering them invisible to Google Video Search.

---

## 2. Recommended Solution
Add Schema.org VideoObject JSON-LD markup and WebVTT caption tracks to all on-page demo videos to earn Google Key Moments badges.

---

## 3. Ready-to-Paste Code / Text
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Turn Long YouTube Videos into Viral Shorts with IncuBrix",
  "description": "Watch how IncuBrix automatically identifies high-energy moments, tracks active speakers, and generates vertical shorts in under 60 seconds.",
  "thumbnailUrl": "https://incubrix.com/assets/images/video-thumb-repurpose.jpg",
  "uploadDate": "2026-11-19T08:00:00+00:00",
  "duration": "PT2M15S",
  "contentUrl": "https://incubrix.com/assets/video/incubrix-demo-repurpose.mp4",
  "embedUrl": "https://incubrix.com/embed/repurpose-demo",
  "transcript": "Welcome to IncuBrix. In this video, we show you how to take a 45-minute podcast episode and extract 5 viral shorts..."
}
</script>
```

---

## 4. Validation & Verification
- **Validator Tool:** Google Rich Results Test (VideoObject)
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
