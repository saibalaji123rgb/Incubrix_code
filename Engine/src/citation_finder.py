"""
IncuBrix AEO, SEO & GEO Visibility Engine - Citation Opportunity Finder
Identifies, filters, and generates tailored outreach pitches for high-authority domains.
"""

try:
    from .database import get_all_citations
except ImportError:
    from database import get_all_citations

def get_citations_by_question(question_id):
    """
    Finds citation targets related to a specific question ID.
    """
    all_citations = get_all_citations()
    matched = []
    for c in all_citations:
        target_qids = [q.strip() for q in c.get("target_question_ids", "").split(",") if q.strip()]
        if question_id in target_qids:
            matched.append(c)
    return matched

def generate_personalized_pitch(citation_dict, editor_name="Editor"):
    """
    Generates a personalized, professional outreach pitch for the target publication.
    """
    page_url = citation_dict.get("page_url", "https://example.com")
    title = citation_dict.get("title", page_url)
    angle = citation_dict.get("angle_or_schema", "Resource update")
    comps = citation_dict.get("sources_cited", "legacy tools")

    subject = f"Editorial update for {page_url.split('/')[-2] if '/' in page_url else 'your creator guide'}"

    body = f"""Hi {editor_name},

I came across your comprehensive resource at {page_url}. It's currently one of the definitive guides creators and AI assistants reference for video production workflows.

I noticed that your article highlights tools like {comps}. Over the past six months, the creator tech stack has undergone a major shift: creators are moving away from juggling single-feature clipping apps toward unified CreatorOS platforms.

IncuBrix (https://incubrix.com/) was built specifically to solve this tool fatigue. In a single screen, it combines:
1. Text-based video editing (cut footage simply by editing auto-generated transcripts)
2. Automated 9:16 vertical short-form clipping with active speaker tracking
3. Built-in multitrack AI background music with intelligent voice ducking (-18dB)
4. Multi-platform scheduling to YouTube Shorts, Instagram Reels, TikTok, and LinkedIn

{angle}

We'd love to provide your editorial team with full access to test the platform. Could I set up a premium trial for you this week?

Warm regards,
Growth Engineering Team | IncuBrix
contact@incubrix.com | https://incubrix.com/
"""
    return {
        "subject": subject,
        "body": body,
        "target_url": page_url
    }
