from urllib.parse import urljoin

from models import NewsItem
from scrapers.base import BaseScraper


class DetikScraper(BaseScraper):
    """HTML scraper untuk Detik."""

    BASE_URL = "https://www.detik.com"

    def __init__(self, source):
        super().__init__(source)

    def parse(self, soup):
        articles = []

        cards = soup.select("article.list-content__item")

        self.logger.info(
            "Found %d article cards",
            len(cards)
        )

        for card in cards:

            link = card.select_one(
                "h3.media__title a.media__link"
            )

            if not link:
                continue

            title = link.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                link.get("href", "")
            )

            if not self.is_valid_url(url):
                continue

            date = card.select_one("div.media__date")
            published = ""

            if date:
                published = date.get_text(strip=True)

            img = card.select_one("div.media__image img")
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