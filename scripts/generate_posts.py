"""Daily DPDPA news roundup + analysis post generator."""
import os
import re
import json
import time
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

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash-lite:generateContent?key=" + GEMINI_API_KEY
)

# DPDPA-relevant feeds. Add or remove as you like.
FEEDS = [
    "https://news.google.com/rss/search?q=%22DPDPA%22+OR+%22Digital+Personal+Data+Protection%22+India&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=data+privacy+India+MeitY&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=%22Data+Protection+Board%22+India&hl=en-IN&gl=IN&ceid=IN:en",
]

POSTS_DIR = Path("_posts")
POSTS_DIR.mkdir(exist_ok=True)

KEYWORDS = [
    "dpdp", "data protection", "privacy", "meity", "data protection board",
    "personal data", "consent manager", "data fiduciary", "data principal",
    "cert-in", "rbi data", "telecom data", "biometric", "aadhaar privacy",
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
        for entry in d.entries[:25]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            summary = re.sub("<[^<]+?>", "", entry.get("summary", "")).strip()
            published = entry.get("published", "")
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
                "published": published,
            })
    return items[:15]


def call_gemini(prompt: str, retries: int = 3) -> str:
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.6, "maxOutputTokens": 4096},
    }
    for attempt in range(retries):
        try:
            r = requests.post(GEMINI_URL, json=payload, timeout=90)
            r.raise_for_status()
            data = r.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print(f"Gemini call failed (attempt {attempt+1}): {e}")
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("Gemini API failed after retries")


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).lower().strip()
    text = re.sub(r"\s+", "-", text)
    return text[:60].strip("-")


def write_post(filename: str, front_matter: dict, body: str):
    fm_lines = ["---"]
    for k, v in front_matter.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}: [{', '.join(v)}]")
        else:
            fm_lines.append(f'{k}: "{v}"')
    fm_lines.append("---\n")
    content = "\n".join(fm_lines) + "\n" + body.strip() + "\n"
    path = POSTS_DIR / filename
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path}")


# ---------- Generators ----------
def make_news_roundup(items):
    if not items:
        body = "_No notable DPDPA-related news items were found in the past 24 hours._"
    else:
        sources_block = "\n".join(
            f"- {i['title']} | {i['summary']} | {i['link']}" for i in items
        )
        prompt = f"""You are an editor for an Indian data-protection news blog.
Write a concise news roundup post for {DISPLAY_DATE} covering the DPDPA, Indian privacy
law, MeitY actions, and the Data Protection Board.

Rules:
- Group related items together; ignore items unrelated to Indian privacy/data law.
- For each item, write 2-3 sentences in your own words. Do NOT copy phrasing from sources.
- Always cite the source as a markdown link at the end of each item: ([Source](URL)).
- No quotation marks around copied text. Paraphrase entirely.
- Use ## headings to group themes (e.g. ## Regulatory Updates, ## Industry Reactions).
- End with a one-line "Why it matters" summary.
- Do NOT include a title (it's set separately). Start directly with content.

Source items:
{sources_block}
"""
        body = call_gemini(prompt)

    title = f"DPDPA News Roundup — {DISPLAY_DATE}"
    front = {
        "layout": "post",
        "title": title,
        "date": TODAY.strftime("%Y-%m-%d %H:%M:%S +0530"),
        "categories": ["news", "roundup"],
        "tags": ["dpdpa", "india", "privacy", "news"],
    }
    fname = f"{DATE_STR}-news-roundup.md"
    write_post(fname, front, body)
    return items


def make_analysis(items):
    anchor = items[:3] if items else []
    anchor_block = "\n".join(f"- {i['title']} ({i['link']})" for i in anchor)
    prompt = f"""You are a data-protection legal analyst writing for an Indian audience.
Write an original analysis piece (~500-700 words) for {DISPLAY_DATE} on a current topic
under India's Digital Personal Data Protection Act, 2023 (DPDPA) or related Indian privacy law.

If the news items below suggest a clear theme, anchor your analysis there. Otherwise pick
an evergreen angle (consent managers, cross-border data transfers, children's data, breach
notification, the Data Protection Board, employer data practices, healthtech, fintech).

Rules:
- Original commentary, not a news rewrite.
- No quotations from any source. Express everything in your own words.
- Reference the DPDPA section/rule by number where relevant.
- Use 2-4 ## subheadings for structure.
- End with a "Practical takeaway" paragraph for businesses or individuals.
- Do NOT include a title (it's set separately). Start directly with content.
- Output a JSON object on the FIRST line in this exact format, then the article:
  {{"title": "Short article title here", "tags": ["tag1", "tag2", "tag3"]}}

Recent news context (for inspiration only — do not summarize these):
{anchor_block or "No news items today; pick an evergreen angle."}
"""
    raw = call_gemini(prompt)
    title = f"DPDPA Analysis — {DISPLAY_DATE}"
    tags = ["dpdpa", "analysis", "privacy", "india"]
    body = raw
    try:
        first_line, rest = raw.split("\n", 1)
        meta = json.loads(first_line.strip())
        title = meta.get("title", title)
        tags = meta.get("tags", tags) + ["analysis"]
        body = rest
    except Exception as e:
        print(f"Could not parse analysis metadata: {e}")

    front = {
        "layout": "post",
        "title": title,
        "date": (TODAY.replace(minute=5)).strftime("%Y-%m-%d %H:%M:%S +0530"),
        "categories": ["analysis"],
        "tags": tags[:6],
    }
    slug = slugify(title) or "analysis"
    fname = f"{DATE_STR}-analysis-{slug}.md"
    write_post(fname, front, body)


# ---------- Main ----------
if __name__ == "__main__":
    items = fetch_items()
    print(f"Fetched {len(items)} relevant items")
    make_news_roundup(items)
    make_analysis(items)
    print("Done.")
