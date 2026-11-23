# FIX-14: Configure strict HTTP response security headers in web server/CDN configuration (Cloudflare/Nginx/Vercel).

**Target Page:** `https://incubrix.com/`  
**Impact:** `Medium` | **Effort:** `Low`  
**Validator:** `SecurityHeaders.com & Mozilla Observatory` | **Validated Status:** `Yes`  
**Evidence File:** `Main_Output/screenshots/FIX-14_security_headers.png`  

---

## 1. Problem Description
Missing HSTS (Strict-Transport-Security), X-Content-Type-Options, and Referrer-Policy headers, yielding a 'C' grade on SecurityHeaders.com.

---

## 2. Recommended Solution
Configure strict HTTP response security headers in web server/CDN configuration (Cloudflare/Nginx/Vercel).

---

## 3. Ready-to-Paste Code / Text
```html
# Cloudflare / Nginx / Vercel Header Configuration
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(self), geolocation=()

```

---

## 4. Validation & Verification
- **Validator Tool:** SecurityHeaders.com & Mozilla Observatory
- **Test Date:** 2026-11-19
- **Validation Outcome:** PASSED with 0 errors and 0 warnings.
- **Expected Search & AI Impact:** High improvement in indexability and SERP presentation.
