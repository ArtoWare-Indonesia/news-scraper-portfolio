from urllib.parse import urljoin

from models import NewsItem
from scrapers.base import BaseScraper


class CNBCScraper(BaseScraper):
    """HTML scraper untuk CNBC Indonesia."""

    BASE_URL = "https://www.cnbcindonesia.com"

    def __init__(self, source):
        super().__init__(source)

    def parse(self, soup):
        articles = []

        cards = soup.select("article")

        self.logger.info(
            "Found %d article cards",
            len(cards)
        )

        for card in cards:

            link = card.select_one("a[href]")

            if not link:
                continue

            title_tag = card.select_one("h2")

            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                link.get("href", "")
            )

            if not self.is_valid_url(url):
                continue

            published = ""

            spans = card.select("span")

            if spans:
                published = spans[-1].get_text(
                    strip=True
                )

            img = card.select_one("img")
            image = ""

            if img:
                image = (
                    img.get("src")
                    or img.get("data-src")
                    or ""
                )

            item = NewsItem(
                title=title,
                url=url,
                source=self.source["name"],
                published=published,
                image=image,
            )

            articles.append(item.to_dict())

        self.logger.info(
            "Parsed %d articles",
            len(articles)
        )

        return articles