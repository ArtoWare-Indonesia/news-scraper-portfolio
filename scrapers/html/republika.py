from urllib.parse import urljoin

from models import NewsItem
from scrapers.base import BaseScraper


class RepublikaScraper(BaseScraper):
    """HTML scraper untuk Republika."""

    BASE_URL = "https://news.republika.co.id"

    def __init__(self, source):
        super().__init__(source)

    def parse(self, soup):
        articles = []

        cards = soup.select(
            "ul.list-group.wrap-latest > li"
        )

        self.logger.info(
            "Found %d article cards",
            len(cards)
        )

        for card in cards:

            link = card.select_one("a[href]")

            if not link:
                continue

            title_tag = card.select_one(
                "div.caption h3 span"
            )

            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                link.get("href", "")
            )

            if not self.is_valid_url(url):
                continue

            category = ""
            published = ""

            category_tag = card.select_one(
                "span.kanal-info"
            )

            if category_tag:
                category = category_tag.get_text(
                    strip=True
                )

            date_tag = card.select_one("div.date")

            if date_tag:
                published = date_tag.get_text(
                    " ",
                    strip=True,
                ).replace(category, "").strip()

            img = card.select_one(
                "div.image img"
            )

            image = ""

            if img:
                image = (
                    img.get("src")
                    or img.get("data-original")
                    or img.get("data-src")
                    or ""
                )

            item = NewsItem(
                title=title,
                url=url,
                source=self.source["name"],
                category=category,
                published=published,
                image=image,
            )

            articles.append(item.to_dict())

        self.logger.info(
            "Parsed %d articles",
            len(articles)
        )

        return articles