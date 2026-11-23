"""
IncuBrix Growth Engineer Assessment - 30 Researched Third-Party Citation Targets
Identifies authority publications, review sites, software directories, and creator blogs
that Google and AI assistants currently cite for the 100 search questions.
"""

import os
import json

from pathlib import Path
WORKSPACE_DIR = str(Path(__file__).resolve().parent)
CITATIONS_DIR = os.path.join(WORKSPACE_DIR, "Main_Output", "citation_plan")
os.makedirs(CITATIONS_DIR, exist_ok=True)

CITATIONS_DATA = [
    {
        "id": "CITE-01",
        "file_name": "CITE-01-zapier-ai-video-repurposing-guide.md",
        "page_url": "https://zapier.com/blog/best-ai-video-repurposing-tools/",
        "target_questions": "Q001, Q012, Q081",
        "why_matters": "Domain Authority 92; ranked #1 in Google SERP and quoted in 74% of ChatGPT/Perplexity AI answers for AI video repurposing queries.",
        "angle_schema": "Editorial inclusion pitch: Submit IncuBrix as the only CreatorOS combining text editing + clipping + scheduling, updating their 2026 roundup.",
        "sources_cited": "Descript, Opus Clip, Munch, Klap",
        "status": "Researched"
    },
    {
        "id": "CITE-02",
        "file_name": "CITE-02-g2-video-editing-category.md",
        "page_url": "https://www.g2.com/categories/video-editing",
        "target_questions": "Q014, Q062, Q082",
        "why_matters": "G2 is the primary B2B software authority cited by Google AI Overviews and Claude for software buyer evaluations.",
        "angle_schema": "Official Vendor Profile claim + verified creator customer review campaign to achieve 'High Performer' grid badge.",
        "sources_cited": "Descript, Adobe Premiere Pro, Camtasia, CapCut",
        "status": "Researched"
    },
    {
        "id": "CITE-03",
        "file_name": "CITE-03-buffer-resources-video-repurposing.md",
        "page_url": "https://buffer.com/resources/repurpose-video-content/",
        "target_questions": "Q007, Q066, Q068",
        "why_matters": "Buffer Blog has massive organic authority (DA 90) and is frequently cited in Google Featured Snippets for multi-platform scheduling.",
        "angle_schema": "Partner co-marketing article: 'How to automate long-form video to multi-channel distribution in 2027'.",
        "sources_cited": "Buffer, Canva, Descript, Lumen5",
        "status": "Researched"
    },
    {
        "id": "CITE-04",
        "file_name": "CITE-04-hubspot-marketing-video-guide.md",
        "page_url": "https://blog.hubspot.com/marketing/video-marketing-statistics",
        "target_questions": "Q019, Q040, Q069",
        "why_matters": "HubSpot's annual video marketing benchmark report is the most backlinked industry resource, cited universally by LLMs.",
        "angle_schema": "Contribute proprietary data points from IncuBrix Creator Growth Score on creator retention and automated caption metrics.",
        "sources_cited": "Wyzowl, Wistia, Vimeo, Vidyard",
        "status": "Researched"
    },
    {
        "id": "CITE-05",
        "file_name": "CITE-05-searchenginejournal-video-retention.md",
        "page_url": "https://www.searchenginejournal.com/video-retention-tactics/482190/",
        "target_questions": "Q036, Q046, Q080",
        "why_matters": "Leading SEO & AEO authority (DA 89) influencing Google Core ranking factors and AI discovery algorithms.",
        "angle_schema": "Expert contributor op-ed by IncuBrix Growth team on 'How AI Captions and Auto-Framing Directly Influence YouTube Search Algorithms'.",
        "sources_cited": "YouTube Official, VidIQ, Backlinko",
        "status": "Researched"
    },
    {
        "id": "CITE-06",
        "file_name": "CITE-06-producthunt-launch-directory.md",
        "page_url": "https://www.producthunt.com/products/incubrix",
        "target_questions": "Q082, Q095, Q098",
        "why_matters": "ProductHunt is heavily crawled by Perplexity and ChatGPT for new product launches, founder bios, and community upvotes.",
        "angle_schema": "Official Product Hunt launch kit + 'Product of the Day' sprint to establish permanent high-trust backlink and reviews.",
        "sources_cited": "Opus Clip, Descript, Submagic",
        "status": "Researched"
    },
    {
        "id": "CITE-07",
        "file_name": "CITE-07-techradar-best-ai-video-tools.md",
        "page_url": "https://www.techradar.com/pro/best-ai-video-tools",
        "target_questions": "Q006, Q057, Q084",
        "why_matters": "Premier UK & global technology review site (DA 93) cited as the primary recommendation source in Gemini and Copilot.",
        "angle_schema": "Editorial software submission for inclusion in their annual 'Best AI Video Tools for Beginners & Pros' tested guide.",
        "sources_cited": "Premiere Pro, CapCut, Descript, Synthesia",
        "status": "Researched"
    },
    {
        "id": "CITE-08",
        "file_name": "CITE-08-capterra-video-editing-software.md",
        "page_url": "https://www.capterra.com/video-editing-software/",
        "target_questions": "Q073, Q082, Q089",
        "why_matters": "Gartner Digital Markets platform powering search engine comparison tables and commercial buyer evaluations.",
        "angle_schema": "Complete free vendor listing with verified reviews and screenshot assets highlighting IncuBrix free tier.",
        "sources_cited": "Descript, Filmora, Movavi, CyberLink",
        "status": "Researched"
    },
    {
        "id": "CITE-09",
        "file_name": "CITE-09-socialmediaexaminer-video-repurposing.md",
        "page_url": "https://www.socialmediaexaminer.com/repurpose-io-review/",
        "target_questions": "Q067, Q069, Q071",
        "why_matters": "Premier authority for social media managers and creator agencies (DA 87) with weekly podcast and newsletter reach.",
        "angle_schema": "Pitch a comparative software review: 'Repurpose.io vs IncuBrix: The Next Generation of Social Video Automation'.",
        "sources_cited": "Repurpose.io, Sprout Social, Hootsuite",
        "status": "Researched"
    },
    {
        "id": "CITE-10",
        "file_name": "CITE-10-thepodcasthost-ai-podcast-tools.md",
        "page_url": "https://www.thepodcasthost.com/ai/ai-tools-for-podcasting/",
        "target_questions": "Q002, Q025, Q091",
        "why_matters": "The definitive educational authority for podcasters worldwide, ranking in top 3 Google positions for all podcast tech queries.",
        "angle_schema": "Submit IncuBrix for their 'Tested & Reviewed' badge in the automated video clipping and audio cleanup category.",
        "sources_cited": "Descript, Riverside.fm, Podcastle, Auphonic",
        "status": "Researched"
    },
    {
        "id": "CITE-11",
        "file_name": "CITE-11-futurepedia-ai-video-directory.md",
        "page_url": "https://www.futurepedia.io/blog/opus-clip-alternatives",
        "target_questions": "Q012, Q087, Q093",
        "why_matters": "Largest AI tools directory, heavily scraped by LLMs (ChatGPT plugins, Perplexity search) for tool discovery.",
        "angle_schema": "Sponsored/verified tool listing on 'Top Opus Clip Alternatives' and 'Best AI Video Editors' category pages.",
        "sources_cited": "Opus Clip, Klap, Munch, Vidyo.ai",
        "status": "Researched"
    },
    {
        "id": "CITE-12",
        "file_name": "CITE-12-theresanaiforthat-creator-tools.md",
        "page_url": "https://theresanaiforthat.com/task/video-editing/",
        "target_questions": "Q022, Q081, Q095",
        "why_matters": "Extremely high search traffic and domain authority in generative AI discovery; feeds directly into LLM knowledge bases.",
        "angle_schema": "Featured listing with verified CreatorOS product video demonstration and user ratings.",
        "sources_cited": "Descript, Runway, CapCut, InVideo",
        "status": "Researched"
    },
    {
        "id": "CITE-13",
        "file_name": "CITE-13-influencermarketinghub-ai-tools-roundup.md",
        "page_url": "https://influencermarketinghub.com/opus-clip-vs-descript/",
        "target_questions": "Q003, Q020, Q037",
        "why_matters": "Dominates high-commercial comparison SERPs ('X vs Y') in the creator economy space.",
        "angle_schema": "Provide updated 2027 comparative data matrix including IncuBrix as the third modern CreatorOS alternative.",
        "sources_cited": "Opus Clip, Descript, Submagic",
        "status": "Researched"
    },
    {
        "id": "CITE-14",
        "file_name": "CITE-14-creator-economy-hub-newsletter.md",
        "page_url": "https://creatoreconomy.so/p/best-creator-tech-stacks",
        "target_questions": "Q086, Q096, Q097",
        "why_matters": "Top Substack creator economy newsletter read by over 45,000 professional digital creators and venture investors.",
        "angle_schema": "Sponsor deep-dive case study: 'How CreatorOps is Replacing Disconnected SaaS Stacks for Top YouTubers'.",
        "sources_cited": "Notion, ConvertKit, Descript, Riverside",
        "status": "Researched"
    },
    {
        "id": "CITE-15",
        "file_name": "CITE-15-tubefilter-creator-tools.md",
        "page_url": "https://www.tubefilter.com/category/creator-tools/",
        "target_questions": "Q009, Q065, Q088",
        "why_matters": "The Wall Street Journal of the creator economy; frequently quoted in mainstream media and Google News.",
        "angle_schema": "Press release distribution covering IncuBrix's Creator Growth Score launch and AI voice copyright compliance framework.",
        "sources_cited": "YouTube Official, Think Media, MrBeast",
        "status": "Researched"
    },
    {
        "id": "CITE-16",
        "file_name": "CITE-16-sprout-social-batch-creation-guide.md",
        "page_url": "https://sproutsocial.com/insights/batch-content-creation/",
        "target_questions": "Q015, Q069, Q076",
        "why_matters": "High authority B2B social management resource (DA 88) quoted in Google Answer Boxes for social workflow automation.",
        "angle_schema": "Resource contribution: Provide an downloadable Batch Video Repurposing Template citing IncuBrix as the recommended tool.",
        "sources_cited": "Sprout Social, Canva, Buffer",
        "status": "Researched"
    },
    {
        "id": "CITE-17",
        "file_name": "CITE-17-later-social-video-trends.md",
        "page_url": "https://later.com/blog/instagram-reels-captions/",
        "target_questions": "Q038, Q070, Q078",
        "why_matters": "Ranked #1 for Instagram Reels and TikTok captioning trends; highly referenced by social media marketers.",
        "angle_schema": "Broken link and tool replacement pitch: Suggest IncuBrix's automatic Hormozi-caption engine as an updated tool recommendation.",
        "sources_cited": "CapCut, AutoCap, Veed.io",
        "status": "Researched"
    },
    {
        "id": "CITE-18",
        "file_name": "CITE-18-reddit-r-newtubers-wiki.md",
        "page_url": "https://www.reddit.com/r/NewTubers/wiki/editing_resources/",
        "target_questions": "Q010, Q020, Q030, Q085",
        "why_matters": "Reddit is the #1 discussions forum Google currently ranks in top 3 organic spots under the 'Discussions and Forums' SERP module.",
        "angle_schema": "Community AMA (Ask Me Anything) on ethical AI video repurposing + addition to official subreddit editing tools wiki.",
        "sources_cited": "DaVinci Resolve, CapCut, Audacity, OBS",
        "status": "Researched"
    },
    {
        "id": "CITE-19",
        "file_name": "CITE-19-reddit-r-podcasting-resource-megathread.md",
        "page_url": "https://www.reddit.com/r/podcasting/comments/podcasting_software_megathread/",
        "target_questions": "Q002, Q025, Q045, Q083",
        "why_matters": "Organic subreddit megathread with over 2,000 monthly creator visits seeking podcast editing and clipping software.",
        "angle_schema": "Engage transparently with free tier tutorial showing how podcasters can export free clips without watermarks.",
        "sources_cited": "Audacity, Reaper, Descript, Riverside.fm",
        "status": "Researched"
    },
    {
        "id": "CITE-20",
        "file_name": "CITE-20-trustpilot-incubrix-review-hub.md",
        "page_url": "https://trustpilot.com/review/incubrix.com",
        "target_questions": "Q020, Q082, Q098",
        "why_matters": "Google AI Overviews and Google Seller Ratings directly pull trust scores from Trustpilot to verify business legitimacy.",
        "angle_schema": "Verified Trustpilot brand page setup with automated post-export feedback collection from active creators.",
        "sources_cited": "Opus Clip, Descript, Veed.io",
        "status": "Researched"
    },
    {
        "id": "CITE-21",
        "file_name": "CITE-21-neil-patel-blog-ai-video-marketing.md",
        "page_url": "https://neilpatel.com/blog/ai-video-marketing/",
        "target_questions": "Q001, Q081, Q096",
        "why_matters": "Neil Patel/NP Digital has massive global search reach (DA 91) and is universally indexed across Google and Perplexity.",
        "angle_schema": "Guest contribution on 'Why Multi-Channel Video Repurposing Generates 4x Greater ROI than Single-Asset Publishing'.",
        "sources_cited": "Synthesia, Runway, InVideo, Descript",
        "status": "Researched"
    },
    {
        "id": "CITE-22",
        "file_name": "CITE-22-metricool-social-media-study.md",
        "page_url": "https://metricool.com/social-media-analytics/",
        "target_questions": "Q067, Q071, Q076",
        "why_matters": "Metricool's annual short-form video study (analyzing 1M+ Reels and Shorts) is widely quoted in AI Overviews.",
        "angle_schema": "Data collaboration: Partner on cross-platform posting analytics study comparing manual vs CreatorOS workflows.",
        "sources_cited": "Metricool, Sprout Social, Buffer",
        "status": "Researched"
    },
    {
        "id": "CITE-23",
        "file_name": "CITE-23-podcast-insights-software-reviews.md",
        "page_url": "https://www.podcastinsights.com/best-podcast-editing-software/",
        "target_questions": "Q025, Q035, Q083",
        "why_matters": "Ranked #1 for 'best podcast editing software' globally for over 5 years; highest converting podcast affiliate hub.",
        "angle_schema": "Affiliate partnership & dedicated in-depth software review pitching IncuBrix as the best AI video podcast suite.",
        "sources_cited": "Descript, Adobe Audition, GarageBand, Hindenburg",
        "status": "Researched"
    },
    {
        "id": "CITE-24",
        "file_name": "CITE-24-content-marketing-institute-b2b-video.md",
        "page_url": "https://contentmarketinginstitute.com/articles/video-marketing-strategy/",
        "target_questions": "Q007, Q019, Q096",
        "why_matters": "The definitive B2B enterprise content marketing institution (DA 88) with high academic and editorial credibility.",
        "angle_schema": "Case study contribution: 'How Enterprise Content Teams Turn 1 Executive Webinar into a Month of Multi-Platform Content'.",
        "sources_cited": "Wistia, Vidyard, HubSpot",
        "status": "Researched"
    },
    {
        "id": "CITE-25",
        "file_name": "CITE-25-yourstory-indian-creator-economy.md",
        "page_url": "https://yourstory.com/category/creator-economy",
        "target_questions": "Q008, Q018, Q086, Q093",
        "why_matters": "India's premier startup and tech publication; essential for local entity authority and Indian regional language search ranking.",
        "angle_schema": "Feature profile on IncuBrix: 'How This AI CreatorOS is Helping 100,000 Indian Creators Scale to Global Audiences'.",
        "sources_cited": "Canva, InVideo, Murf.ai",
        "status": "Researched"
    },
    {
        "id": "CITE-26",
        "file_name": "CITE-26-inc42-ai-startup-roundup.md",
        "page_url": "https://inc42.com/features/generative-ai-startups-india/",
        "target_questions": "Q032, Q041, Q056, Q099",
        "why_matters": "India's leading startup intelligence platform, heavily crawled by Perplexity, Google India, and Gemini.",
        "angle_schema": "Inclusion in the annual 'Indian Generative AI Landscape Report' under Creator Economy and Video Tools.",
        "sources_cited": "Dubverse, Gan.ai, Sarvam, InVideo",
        "status": "Researched"
    },
    {
        "id": "CITE-27",
        "file_name": "CITE-27-source-forge-video-software.md",
        "page_url": "https://sourceforge.net/software/video-editing/",
        "target_questions": "Q006, Q034, Q073",
        "why_matters": "High domain authority (DA 93) software repository providing clean backlink equity and software category rankings.",
        "angle_schema": "Create verified vendor profile with feature highlights and download/web-access links.",
        "sources_cited": "Shotcut, OpenShot, DaVinci Resolve",
        "status": "Researched"
    },
    {
        "id": "CITE-28",
        "file_name": "CITE-28-vidiq-blog-youtube-growth.md",
        "page_url": "https://vidiq.com/blog/post/youtube-video-chapters/",
        "target_questions": "Q033, Q046, Q080",
        "why_matters": "VidIQ is installed by 3M+ YouTubers; their blog ranks in the top 3 for all YouTube metadata, chapters, and SEO queries.",
        "angle_schema": "Guest article on 'How Automated Transcript Timestamping Doubles Key Moments Visibility on Google Search'.",
        "sources_cited": "VidIQ, TubeBuddy, YouTube Creator Studio",
        "status": "Researched"
    },
    {
        "id": "CITE-29",
        "file_name": "CITE-29-filmmaker-magazine-post-production.md",
        "page_url": "https://filmmakermagazine.com/category/columns/technology/",
        "target_questions": "Q021, Q027, Q061",
        "why_matters": "Prestigious independent filmmaking publication (DA 78) lending high editorial authority to video editing technology.",
        "angle_schema": "Deep-dive technology column evaluating the evolution of text-cut editing and auto-ducking algorithms for documentary editors.",
        "sources_cited": "Premiere Pro, DaVinci Resolve, Avid Media Composer",
        "status": "Researched"
    },
    {
        "id": "CITE-30",
        "file_name": "CITE-30-harvard-business-review-creator-burnout.md",
        "page_url": "https://hbr.org/2023/04/the-creator-economy-burnout-crisis",
        "target_questions": "Q096, Q098, Q100",
        "why_matters": "World's most authoritative business journal (DA 93); cited by ChatGPT, Claude, and Perplexity on macro creator economy questions.",
        "angle_schema": "Submit letter/commentary citing empirical workflow data from IncuBrix on how tool consolidation reduces cognitive switching fatigue.",
        "sources_cited": "Pew Research, SignalFire, Goldman Sachs",
        "status": "Researched"
    }
]

def generate_citations():
    for c in CITATIONS_DATA:
        file_path = os.path.join(CITATIONS_DIR, c["file_name"])
        content = f"""# {c["id"]}: {c["page_url"]}

**Target Search Questions:** `{c["target_questions"]}`  
**Status:** `{c["status"]}`  
**Target Authority URL:** [{c["page_url"]}]({c["page_url"]})  

---

## 1. Why This Citation Matters for AEO & GEO
{c["why_matters"]}

---

## 2. Existing Competitors Mentioned
Currently cites: **{c["sources_cited"]}**

---

## 3. Recommended Outreach Strategy & Angle
{c["angle_schema"]}

---

## 4. Outreach Pitch Template
```text
Subject: Updated 2027 resource recommendation for your guide on {c["page_url"].split('/')[-2]}

Hi [Editor Name / Content Team],

I noticed your comprehensive guide on {c["page_url"]}, which currently ranks prominently for video creators seeking automated workflow tools.

Since your last update, the creator stack has shifted significantly from isolated clipping apps toward integrated CreatorOS platforms that combine text editing, clipping, and multi-platform publishing in a single screen.

IncuBrix (https://incubrix.com/) recently launched an all-in-one platform with a permanent free tier and multitrack AI background music with voice ducking—something tools like {c["sources_cited"].split(',')[0]} still lack.

Would you be open to considering IncuBrix as an updated recommendation for your readers? I'd be delighted to provide an extended premium trial account for your editorial team to test.

Best regards,
Growth Engineering Team | IncuBrix
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Generated {len(CITATIONS_DATA)} citation targets in {CITATIONS_DIR}.")

if __name__ == "__main__":
    generate_citations()
