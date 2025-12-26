import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_docs(start_url, max_pages=30):
    visited = set()
    to_visit = [start_url]
    domain = urlparse(start_url).netloc
    pages = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        visited.add(url)
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            pages.append(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if urlparse(full_url).netloc == domain:
                    to_visit.append(full_url)

        except Exception:
            continue

    return pages
