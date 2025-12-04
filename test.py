# requirements: pip install requests beautifulsoup4 html5lib
import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://santoshimaarcmpuc.netlify.app/"

def fetch(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; scraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.text

def extract_all_text(html):
    soup = BeautifulSoup(html, "html5lib")
    # remove scripts & styles
    for tag in soup(["script","style","noscript"]):
        tag.decompose()
    # get visible text
    text = soup.get_text(separator="\n")
    # collapse blank lines
    lines = [ln.strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]
    return "\n".join(lines), soup

def extract_structured(soup):
    data = {}
    # Example: grab headings, paragraphs, links
    data["title"] = soup.title.string.strip() if soup.title and soup.title.string else ""
    data["headings"] = [h.get_text(strip=True) for h in soup.find_all(["h1","h2","h3","h4","h5"])]
    data["paragraphs"] = [p.get_text(strip=True) for p in soup.find_all("p")]
    data["links"] = [{"text": a.get_text(strip=True), "href": a.get("href")} for a in soup.find_all("a")]
    return data

def save_outputs(html, text, structured, outdir="scrape_output"):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "page.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(outdir, "page_text.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(outdir, "structured.json"), "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)
    print("Saved: page.html, page_text.txt, structured.json in", outdir)

if __name__ == "__main__":
    html = fetch(URL)
    text, soup = extract_all_text(html)
    structured = extract_structured(soup)
    save_outputs(html, text, structured)

