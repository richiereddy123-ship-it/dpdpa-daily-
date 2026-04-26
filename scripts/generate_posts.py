"""Daily privacy-law content generator: India-first with global context.

Generates two posts per day:
  1. News roundup — DPDPA, RBI, MeitY, plus selected global enforcement/regulation
  2. Analysis — alternates between India-focused deep-dive and comparative cross-jurisdiction piece
"""
import os
import re
import json
import time
import random
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import feedparser
import requests

# ---------- Config ----------
IST = ZoneInfo("Asia/Kolkata")
TODAY = datetime.now(IST)
DATE_STR = TODAY.strftime("%Y-%m-%d")
DISPLAY_DATE = TODAY.strftime("%B %d, %Y")
DAY_OF_YEAR = TODAY.timetuple().tm_yday  # used to alternate analysis type

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + GEMINI_API_KEY
)

# ---------- Sources ----------
# India-priority feeds first, then global. Filtering happens by keyword later.
FEEDS = [
    # India - DPDPA and broader data law
    "https://news.google.com/rss/search?q=%22DPDPA%22+OR+%22Digital+Personal+Data+Protection%22+India&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=data+privacy+India+MeitY&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=%22Data+Protection+Board%22+India&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=RBI+data+localisation+OR+CERT-In+OR+Aadhaar+privacy&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=India+Supreme+Court+privacy+OR+%22right+to+privacy%22&hl=en-IN&gl=IN&ceid=IN:en",
    # Global - GDPR, EU, US, UK
    "https://news.google.com/rss/search?q=GDPR+enforcement+OR+%22EDPB%22+OR+%22ICO+fine%22&hl=en&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22FTC%22+privacy+OR+CCPA+OR+%22California+Privacy%22&hl=en&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22EU+AI+Act%22+OR+%22Digital+Services+Act%22+enforcement&hl=en&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=cross-border+data+transfer+OR+%22standard+contractual+clauses%22&hl=en&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=%22data+breach%22+regulator+fine&hl=en&gl=US&ceid=US:en",
]

POSTS_DIR = Path("_posts")
POSTS_DIR.mkdir(exist_ok=True)

KEYWORDS = [
    # India-specific
    "dpdp", "meity", "data protection board", "data fiduciary", "data principal",
    "consent manager", "cert-in", "rbi data", "aadhaar", "digital india", "it rules",
    # General privacy law
    "privacy", "data protection", "personal data", "data breach", "biometric",
    # Global frameworks
    "gdpr", "ccpa", "cpra", "edpb", "ico", "cnil", "ftc", "lgpd", "pdpa",
    "ai act", "digital services act", "dsa", "schrems",
    # Enforcement / litigation
    "fine", "penalty", "enforcement", "regulator", "supervisory authority",
    "consent", "data transfer", "localisation", "localization",
]

# Comparative analysis themes — rotate through these on "comparative" days
COMPARATIVE_THEMES = [
    "Consent under DPDPA Section 6 vs GDPR Article 7: granularity, withdrawal, and onus of proof",
    "Children's data: DPDPA Section 9 vs GDPR Article 8 vs US COPPA",
    "Breach notification timelines: India (DPDP Rules) vs EU (GDPR Article 33) vs Singapore PDPA vs Australia",
    "Cross-border data transfers: DPDPA Section 16 (negative-list approach) vs GDPR Chapter V",
    "Data Protection Officer roles: GDPR Article 37 vs DPDPA's 'Significant Data Fiduciary' framework",
    "Right to erasure: DPDPA Section 12 vs GDPR Article 17",
    "Penalties and enforcement powers: Data Protection Board of India vs CNIL vs ICO vs FTC",
    "Data localisation: India (RBI, sectoral) vs China (PIPL) vs Russia vs EU",
    "Algorithmic decision-making: DPDPA silence vs GDPR Article 22 vs EU AI Act vs Colorado AI Act",
    "Health data: DPDPA general framework vs HIPAA vs GDPR Article 9",
    "Employee monitoring: India (no explicit rules) vs EU (Article 88 + Member State law) vs US patchwork",
    "Public-interest exemptions: DPDPA Section 17 vs GDPR Article 23",
    "Consent managers (DPDPA Rules) vs CMP frameworks under EU ePrivacy/GDPR",
    "Sensitive personal data definitions: DPDPA (uniform) vs GDPR Article 9 vs Indian SPDI Rules legacy",
    "Class action / representative actions: GDPR Article 80 vs India's silent framework",
    "Profiling and direct marketing: GDPR vs DPDPA vs CAN-SPAM/TCPA",
    "Government surveillance carve-outs: DPDPA Section 17(2) vs Schrems II / EU adequacy",
    "Biometric data regulation: India (Aadhaar Act + DPDPA) vs Illinois BIPA vs GDPR",
    "Fintech privacy: RBI Digital Lending Guidelines vs GLBA vs PSD2/GDPR",
    "Healthtech data sharing: DISHA (proposed) + DPDPA vs HIPAA vs EHDS",
    "AI training data: DPDPA's deemed-consent gap vs GDPR Article 6(1)(f) vs UK ICO guidance",
    "Cookie consent: DPDPA (no specific rule) vs ePrivacy Directive vs CCPA opt-out",
    "Data Protection Impact Assessments: DPDPA Rules vs GDPR Article 35",
    "Whistleblower data handling: India (no framework) vs EU Whistleblower Directive vs SOX",
    "M&A and privacy due diligence: DPDPA implications vs GDPR transfer issues vs CCPA",
    "Telecom data: India (Telecom Act 2023 + DPDPA) vs EU ePrivacy vs CALEA",
    "Edtech and student data: India vs FERPA vs GDPR",
    "Insurance and DPDPA: IRDAI obligations layered with DPDPA",
    "Cybersecurity incident reporting: CERT-In Directions vs NIS2 vs SEC cyber rules",
    "Open banking and account aggregators: India RBI-AA vs PSD2 vs CFPB Section 1033",
]

# India-focused analysis themes
INDIA_THEMES = [
    "How DPDPA Section 8 obligations of Data Fiduciaries apply to Indian SaaS businesses",
    "DPDPA Rules on Consent Managers: business model, liability, and open questions",
    "Significant Data Fiduciary thresholds under the DPDPA — what it means for large platforms",
    "DPDPA's interplay with the IT Rules 2021 for intermediaries",
    "RBI data localisation directive and how DPDPA layers on top",
    "Children's data under DPDPA Section 9: verifiable parental consent in the Indian context",
    "Enforcement mechanics of the Data Protection Board: timelines, appeals, and penalties",
    "Cross-border transfers under DPDPA Section 16: the negative-list model",
    "DPDPA and the Right to Information Act tension: what the recent Supreme Court notice signals",
    "Sector-specific privacy: DPDPA implications for fintech under RBI norms",
    "Healthtech and DPDPA: handling sensitive health data without a separate sectoral law",
    "DPDPA and edtech: managing minors' data in Indian online learning",
    "Employer obligations under DPDPA for workforce data",
    "DPDPA breach notification: timelines, content, and Board reporting practicalities",
    "DPDPA's deemed consent provisions under Section 7 — scope and risk",
    "Data principal rights: practical workflows for Indian companies to honour Sections 11–14",
    "DPDPA and AI training: the legal gap for foundation models trained on Indian personal data",
    "DPDPA contracts and processor relationships under Section 8(2)",
    "DPDPA penalties up to ₹250 crore: how Schedule 1 will likely be applied",
    "Lessons from GDPR enforcement that Indian companies should pre-empt under DPDPA",
]


# ---------- Helpers ----------
def fetch_items():
    items = []
    seen_titles = set()
    for url in FEEDS:
        try:
            d = feedparser.parse(url)
        except Exception as e:
            print(f"Feed error {url}: {e}")
            continue
        for entry in d.entries[:20]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            summary = re.sub("<[^<]+?>", "", entry.get("summary", "")).strip()
            if not title or not link:
                continue
            key = title.lower()[:80]
            if key in seen_titles:
                continue
            blob = (title + " " + summary).lower()
            if not any(k in blob for k in KEYWORDS):
                continue
            seen_titles.add(key)
            items.append({
                "title": title,
                "link": link,
                "summary": summary[:600],
            })
    return items[:20]


def call_gemini(prompt: str, retries: int = 3) -> str:
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.55, "maxOutputTokens": 4096},
    }
    for attempt in range(retries):
        try:
            r = requests.post(GEMINI_URL, json=payload, timeout=120)
            r.raise_for_status()
            data = r.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print(f"Gemini call failed (attempt {attempt+1}): {e}")
            time.sleep(8 * (attempt + 1))
    raise RuntimeError("Gemini API failed after retries")


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).lower().strip()
    text = re.sub(r"\s+", "-", text)
    return text[:60].strip("-")


def yaml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_front_matter(title: str, date_str: str, categories: list, tags: list) -> str:
    lines = [
        "---",
        f'title: "{yaml_escape(title)}"',
        f'date: {date_str}',
        f'categories: [{", ".join(categories)}]',
        f'tags: [{", ".join(tags)}]',
        "---",
        "",
    ]
    return "\n".join(lines)


def write_post(filename: str, front_matter: str, body: str):
    content = front_matter + "\n" + body.strip() + "\n"
    path = POSTS_DIR / filename
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path}")


# ---------- Generators ----------
def make_news_roundup(items):
    if not items:
        body = "_No notable privacy-law news items were found in the past 24 hours._"
    else:
        sources_block = "\n".join(
            f"- {i['title']} | {i['summary']} | {i['link']}" for i in items
        )
        prompt = f"""You are an editor for an Indian privacy-law publication with a global lens.
Write a concise news roundup post for {DISPLAY_DATE}.

Editorial priorities (in this order):
1. India: DPDPA, MeitY, Data Protection Board, RBI data rules, CERT-In, Aadhaar, Indian privacy litigation.
2. Global enforcement and developments that matter to Indian businesses or to comparative privacy thinking
   (GDPR fines, EDPB/ICO/CNIL actions, FTC, EU AI Act, cross-border transfer mechanisms, major breaches).
3. Skip items that are clearly unrelated to privacy/data protection law.

Rules:
- Lead with India unless a global story is genuinely more significant.
- For each item, write 2-3 sentences in your own words. Do NOT copy phrasing from sources.
- Cite the source as a markdown link at the end of each item: ([Source](URL)).
- No quoted text from sources. Paraphrase entirely.
- Use ## headings to group themes (e.g. ## India: Regulatory Updates, ## Global Enforcement, ## Cross-Border).
- End with a one-line "Why it matters" summary tying India and global threads together.
- Do NOT include a title (it's set separately). Start directly with content.

Source items:
{sources_block}
"""
        body = call_gemini(prompt)

    title = f"Privacy Law Roundup — {DISPLAY_DATE}"
    date_str = TODAY.strftime("%Y-%m-%d %H:%M:%S +0530")
    fm = build_front_matter(
        title=title,
        date_str=date_str,
        categories=["news", "roundup"],
        tags=["dpdpa", "india", "privacy", "global", "news"],
    )
    fname = f"{DATE_STR}-news-roundup.md"
    write_post(fname, fm, body)
    return items


def make_analysis(items):
    # Alternate between India-deep-dive and comparative based on day of year
    is_comparative_day = (DAY_OF_YEAR % 2 == 0)
    pool = COMPARATIVE_THEMES if is_comparative_day else INDIA_THEMES
    # Deterministic-but-rotating pick
    theme = pool[DAY_OF_YEAR % len(pool)]
    flavor = "comparative" if is_comparative_day else "india-focused"

    anchor = items[:3] if items else []
    anchor_block = "\n".join(f"- {i['title']} ({i['link']})" for i in anchor)

    if is_comparative_day:
        guidance = """Write a COMPARATIVE analysis. Treat India (DPDPA / RBI / IT Rules) as the
anchor jurisdiction and compare against the relevant foreign frameworks named in the theme.
Be concrete about section / article numbers. Highlight where Indian law is stricter, looser,
or silent compared to its foreign counterparts. Avoid editorialising about which regime is
"better" — frame trade-offs neutrally."""
        category_list = ["analysis", "comparative"]
        default_tags = ["dpdpa", "india", "comparative", "privacy"]
    else:
        guidance = """Write an INDIA-focused analysis. Centre the piece on Indian law (DPDPA,
DPDP Rules, RBI / SEBI / IRDAI norms where relevant, IT Rules, sectoral regulators).
Reference foreign law only briefly where it sharpens the Indian point (e.g. how a GDPR
concept compares). Cite DPDPA section / rule numbers wherever you make a legal claim."""
        category_list = ["analysis", "india"]
        default_tags = ["dpdpa", "india", "privacy", "analysis"]

    prompt = f"""You are a privacy-law analyst writing for an India-first audience that also
follows global privacy developments. Today's date is {DISPLAY_DATE}.

Theme: {theme}

{guidance}

Length: 600–900 words.

Rules:
- Original commentary, not a news rewrite.
- No direct quotations from any source. Paraphrase entirely.
- Cite section / article / rule numbers where you make a legal claim.
- Use 3–5 ## subheadings.
- End with a "Practical takeaway" paragraph aimed at Indian businesses, GCs, or DPOs.
- Do NOT include the title in the body (it's set separately). Start directly with content.
- Output a JSON object on the FIRST line in this exact format, then the article on subsequent lines:
  {{"title": "Short article title here", "tags": ["tag1", "tag2", "tag3"]}}

Recent news context (use only as background, do not summarise):
{anchor_block or "No specific news items today."}
"""
    raw = call_gemini(prompt)

    title = f"Privacy Law Analysis — {DISPLAY_DATE}"
    tags = default_tags
    body = raw
    try:
        first_line, rest = raw.split("\n", 1)
        meta = json.loads(first_line.strip())
        title = meta.get("title", title)
        raw_tags = meta.get("tags", [])
        if isinstance(raw_tags, list):
            tags = [str(t) for t in raw_tags] + [flavor]
        body = rest
    except Exception as e:
        print(f"Could not parse analysis metadata: {e}")

    date_str = TODAY.replace(minute=5).strftime("%Y-%m-%d %H:%M:%S +0530")
    fm = build_front_matter(
        title=title,
        date_str=date_str,
        categories=category_list,
        tags=tags[:6],
    )
    slug = slugify(title) or f"analysis-{flavor}"
    fname = f"{DATE_STR}-analysis-{slug}.md"
    write_post(fname, fm, body)


# ---------- Main ----------
if __name__ == "__main__":
    items = fetch_items()
    print(f"Fetched {len(items)} relevant items")
    make_news_roundup(items)
    make_analysis(items)
    print("Done.")
