import json
import sys


def fallback_results(query: str, error_msg: str):
    return {
        "query": query,
        "results": [
            {
                "title": f"Headless browser unavailable: {error_msg}",
                "url": "",
                "image": "",
                "price": "",
                "mileage": "",
            }
        ],
        "ok": False,
    }


def run_search(query: str):
    try:
        from playwright.sync_api import sync_playwright
    except Exception as ex:
        return fallback_results(query, f"Playwright import failed ({ex})")

    try:
        with sync_playwright() as p:
            print("DEBUG: launching browser...")
            browser = p.chromium.launch(headless=True)
            print("DEBUG: browser launched")
            page = browser.new_page()
            page.goto("https://duckduckgo.com", wait_until="domcontentloaded", timeout=20000)
            page.fill("input[name=q]", query)
            page.keyboard.press("Enter")
            page.wait_for_timeout(1800)

            # Try multiple selectors to extract titles/links for broader compatibility
            selectors = ["a[data-testid='result-title-a']", "a.result__a", "h2 a", "a"]
            results = []
            seen = set()
            for sel in selectors:
                try:
                    els = page.locator(sel)
                    texts = els.all_text_contents()
                    hrefs = els.evaluate_all("els => els.map(e => e.href)")
                    for i, t in enumerate(texts):
                        title = (t or "").strip()
                        url = hrefs[i] if i < len(hrefs) else ""
                        if title and title not in seen:
                            seen.add(title)
                            results.append({"title": title, "url": url, "image": "", "price": "", "mileage": ""})
                            if len(results) >= 8:
                                break
                    if len(results) >= 8:
                        break
                except Exception:
                    continue

            browser.close()

            if not results:
                results = [
                    {
                        "title": f"No web results returned for '{query}'",
                        "url": "",
                        "image": "",
                        "price": "",
                        "mileage": "",
                    }
                ]

            return {"query": query, "results": results, "ok": True}
    except Exception as ex:
        return fallback_results(query, f"Playwright runtime failed ({ex})")


def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "example domain"
    print(json.dumps(run_search(query)))


if __name__ == "__main__":
    main()