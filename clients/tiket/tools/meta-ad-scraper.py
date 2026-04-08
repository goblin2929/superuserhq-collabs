"""
Meta Ad Library Scraper — Travel/Hotel Ads in Indonesia
Scrapes the Meta Ad Library web interface using Playwright.
Outputs structured JSON for Airtable ingestion.

Usage:
    python meta-ad-scraper.py
    python meta-ad-scraper.py --country ID --sector travel --days 30 --limit 50
"""

import argparse
import json
import time
import re
from datetime import datetime, timedelta
from pathlib import Path
from playwright.sync_api import sync_playwright


def parse_args():
    parser = argparse.ArgumentParser(description="Scrape Meta Ad Library for travel ads")
    parser.add_argument("--country", default="ID", help="Country code (default: ID for Indonesia)")
    parser.add_argument("--sector", default="travel", help="Search keyword/sector")
    parser.add_argument("--days", type=int, default=30, help="Look back N days (default: 30)")
    parser.add_argument("--limit", type=int, default=50, help="Max ads to collect (default: 50)")
    parser.add_argument("--output", default=None, help="Output JSON path (default: auto-generated)")
    parser.add_argument("--screenshots", action="store_true", help="Save screenshots of each ad")
    return parser.parse_args()


def build_url(country, search_term):
    """Build Meta Ad Library search URL."""
    base = "https://www.facebook.com/ads/library/"
    params = (
        f"?active_status=active"
        f"&ad_type=all"
        f"&country={country}"
        f"&q={search_term}"
        f"&search_type=keyword_unordered"
        f"&media_type=all"
    )
    return base + params


TRAVEL_KEYWORDS = [
    "hotel deals",
    "travel booking",
    "hotel promo",
    "liburan",        # Indonesian: vacation
    "hotel murah",    # Indonesian: cheap hotel
    "tiket pesawat",  # Indonesian: flight ticket
    "staycation",
    "resort",
    "Traveloka",
    "Agoda",
    "Booking.com",
    "Klook",
]


def scrape_ads(page, url, limit, screenshot_dir=None):
    """Scrape ads from a single Meta Ad Library search page."""
    ads = []

    print(f"  Loading: {url[:80]}...")
    page.goto(url, wait_until="networkidle", timeout=30000)
    time.sleep(3)

    # Handle cookie consent if present
    try:
        consent = page.locator("button:has-text('Allow'), button:has-text('Accept')")
        if consent.count() > 0:
            consent.first.click()
            time.sleep(1)
    except Exception:
        pass

    # Scroll to load more ads
    scroll_count = 0
    max_scrolls = limit // 5  # rough estimate: ~5 ads per scroll
    last_count = 0

    while scroll_count < max_scrolls:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        scroll_count += 1

        # Check how many ad cards are loaded
        ad_cards = page.locator("[class*='_7jvw'], [class*='xrvj5dj'], div[role='article']")
        current_count = ad_cards.count()

        if current_count >= limit:
            break
        if current_count == last_count:
            # No new ads loaded after scroll
            break
        last_count = current_count

    print(f"  Found {last_count} ad cards")

    # Extract ad data from each card
    ad_cards = page.locator("[class*='_7jvw'], [class*='xrvj5dj'], div[role='article']")
    count = min(ad_cards.count(), limit)

    for i in range(count):
        try:
            card = ad_cards.nth(i)
            ad_data = extract_ad_data(card, i)
            if ad_data:
                ads.append(ad_data)

                if screenshot_dir:
                    try:
                        card.screenshot(path=str(screenshot_dir / f"ad_{i:03d}.png"))
                    except Exception:
                        pass

        except Exception as e:
            print(f"  Error extracting ad {i}: {e}")
            continue

    return ads


def extract_ad_data(card, index):
    """Extract structured data from a single ad card."""
    ad = {
        "index": index,
        "scraped_at": datetime.now().isoformat(),
    }

    # Advertiser name
    try:
        # Try multiple selectors for advertiser name
        for selector in ["a[href*='/ads/?']", "strong", "span[class*='x1lliihq']"]:
            el = card.locator(selector).first
            if el.count() > 0:
                text = el.inner_text().strip()
                if text and len(text) > 1:
                    ad["advertiser"] = text
                    break
    except Exception:
        pass

    # Ad body text / copy
    try:
        body_selectors = [
            "div[class*='_7jyr']",
            "div[class*='xdj266r']",
            "div[style*='webkit-line-clamp']",
        ]
        for sel in body_selectors:
            el = card.locator(sel).first
            if el.count() > 0:
                text = el.inner_text().strip()
                if text and len(text) > 10:
                    ad["ad_copy"] = text
                    break
    except Exception:
        pass

    # Started running date
    try:
        date_pattern = re.compile(r"Started running on (.+?)(?:\s*$|\s*·)", re.IGNORECASE)
        card_text = card.inner_text()
        match = date_pattern.search(card_text)
        if match:
            ad["started_date"] = match.group(1).strip()
            # Calculate days running
            try:
                start = datetime.strptime(ad["started_date"], "%b %d, %Y")
                ad["days_running"] = (datetime.now() - start).days
            except ValueError:
                try:
                    start = datetime.strptime(ad["started_date"], "%d %b %Y")
                    ad["days_running"] = (datetime.now() - start).days
                except ValueError:
                    pass
    except Exception:
        pass

    # Platform info
    try:
        platform_text = card.inner_text()
        platforms = []
        if "Facebook" in platform_text:
            platforms.append("Facebook")
        if "Instagram" in platform_text:
            platforms.append("Instagram")
        if "Messenger" in platform_text:
            platforms.append("Messenger")
        if "Audience Network" in platform_text:
            platforms.append("Audience Network")
        ad["platforms"] = platforms if platforms else ["Unknown"]
    except Exception:
        ad["platforms"] = ["Unknown"]

    # Ad format detection
    try:
        has_video = card.locator("video, [class*='video'], [aria-label*='video']").count() > 0
        has_carousel = card.locator("[class*='carousel'], [class*='scroll']").count() > 0
        if has_video:
            ad["format"] = "video"
        elif has_carousel:
            ad["format"] = "carousel"
        else:
            ad["format"] = "image"
    except Exception:
        ad["format"] = "unknown"

    # CTA button text
    try:
        cta_selectors = [
            "a[class*='_7jys']",
            "div[class*='x1ja2u2z'] a",
            "a:has-text('Book'), a:has-text('Learn'), a:has-text('Shop'), a:has-text('Sign')",
        ]
        for sel in cta_selectors:
            el = card.locator(sel).first
            if el.count() > 0:
                ad["cta"] = el.inner_text().strip()
                break
    except Exception:
        pass

    # Ad library ID / link
    try:
        link_el = card.locator("a[href*='ads/library']").first
        if link_el.count() > 0:
            ad["ad_library_url"] = link_el.get_attribute("href")
    except Exception:
        pass

    # Only return if we got meaningful data
    if ad.get("advertiser") or ad.get("ad_copy"):
        return ad
    return None


def score_virality(ad):
    """Score an ad's likely virality based on available signals."""
    score = 0

    # Longevity: longer running = likely performing
    days = ad.get("days_running", 0)
    if days > 21:
        score += 3
    elif days > 14:
        score += 2
    elif days > 7:
        score += 1

    # Multi-platform = wider distribution
    platforms = ad.get("platforms", [])
    if len(platforms) >= 3:
        score += 2
    elif len(platforms) >= 2:
        score += 1

    # Video format tends to be higher engagement
    if ad.get("format") == "video":
        score += 2
    elif ad.get("format") == "carousel":
        score += 1

    # Has CTA = direct response intent
    if ad.get("cta"):
        score += 1

    ad["virality_score"] = score
    return ad


def analyze_hook(ad):
    """Analyze the ad's hook / opening approach."""
    copy = ad.get("ad_copy", "")
    if not copy:
        ad["hook_analysis"] = "No copy available"
        return ad

    first_line = copy.split("\n")[0] if "\n" in copy else copy[:100]

    # Detect hook patterns
    patterns = {
        "urgency": ["limited", "last chance", "ending", "hurry", "only", "today", "now"],
        "discount": ["%", "off", "save", "free", "promo", "diskon", "gratis", "murah"],
        "question": ["?"],
        "social_proof": ["#1", "most popular", "best", "top rated", "award", "terbaik"],
        "fomo": ["don't miss", "selling fast", "almost gone", "jangan lewatkan"],
        "emotional": ["dream", "escape", "paradise", "imagine", "impian", "surga"],
    }

    detected = []
    for pattern_name, keywords in patterns.items():
        for kw in keywords:
            if kw.lower() in copy.lower():
                detected.append(pattern_name)
                break

    ad["hook_type"] = list(set(detected)) if detected else ["informational"]
    ad["hook_first_line"] = first_line
    return ad


def main():
    args = parse_args()

    output_dir = Path("/Users/tinachu/superuserhq-collabs/clients/tiket/tools/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    screenshot_dir = None
    if args.screenshots:
        screenshot_dir = output_dir / f"screenshots_{datetime.now().strftime('%Y%m%d')}"
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = args.output or str(output_dir / f"meta_ads_{args.country}_{timestamp}.json")

    all_ads = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()

        for keyword in TRAVEL_KEYWORDS:
            if len(all_ads) >= args.limit:
                break

            url = build_url(args.country, keyword)
            remaining = args.limit - len(all_ads)

            print(f"\nSearching: '{keyword}' (need {remaining} more ads)")
            try:
                ads = scrape_ads(page, url, min(remaining, 20), screenshot_dir)
                # Deduplicate by advertiser + ad_copy combo
                for ad in ads:
                    ad["search_keyword"] = keyword
                    key = (ad.get("advertiser", ""), ad.get("ad_copy", "")[:50])
                    if not any(
                        (a.get("advertiser", ""), a.get("ad_copy", "")[:50]) == key
                        for a in all_ads
                    ):
                        all_ads.append(ad)
            except Exception as e:
                print(f"  Error searching '{keyword}': {e}")
                continue

        browser.close()

    print(f"\nCollected {len(all_ads)} unique ads")

    # Score and analyze
    all_ads = [score_virality(ad) for ad in all_ads]
    all_ads = [analyze_hook(ad) for ad in all_ads]

    # Sort by virality score
    all_ads.sort(key=lambda x: x.get("virality_score", 0), reverse=True)

    # Add rank
    for i, ad in enumerate(all_ads):
        ad["rank"] = i + 1

    # Save results
    result = {
        "scrape_meta": {
            "country": args.country,
            "sector": args.sector,
            "lookback_days": args.days,
            "scraped_at": datetime.now().isoformat(),
            "total_ads": len(all_ads),
            "keywords_searched": TRAVEL_KEYWORDS,
        },
        "ads": all_ads,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Saved to: {output_path}")

    # Print top 10 summary
    print(f"\n{'='*80}")
    print(f"TOP 10 VIRAL ADS — Travel/Hotel in Indonesia (last {args.days} days)")
    print(f"{'='*80}\n")

    for ad in all_ads[:10]:
        print(f"#{ad['rank']} | Score: {ad.get('virality_score', '?')}/8")
        print(f"  Advertiser: {ad.get('advertiser', 'Unknown')}")
        print(f"  Format: {ad.get('format', '?')} | Platforms: {', '.join(ad.get('platforms', []))}")
        print(f"  Running: {ad.get('days_running', '?')} days | Started: {ad.get('started_date', '?')}")
        print(f"  Hook: {ad.get('hook_first_line', 'N/A')[:80]}")
        print(f"  Hook type: {', '.join(ad.get('hook_type', []))}")
        print(f"  CTA: {ad.get('cta', 'None')}")
        print(f"  URL: {ad.get('ad_library_url', 'N/A')}")
        print()

    return output_path


if __name__ == "__main__":
    main()
