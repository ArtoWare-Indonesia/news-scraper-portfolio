import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import HTML_SOURCES, RSS_SOURCES
from scrapers.registry import HTML_SCRAPERS
from scrapers.rss import RSSScraper


class ScraperManager:
    """Mengelola dan menjalankan scraper HTML dan RSS."""

    def __init__(self):
        self.html_scrapers = []
        self.rss_scrapers = []

        # HTML scraper
        for source in HTML_SOURCES:
            if not source.get("enabled", True):
                continue

            scraper_class = HTML_SCRAPERS.get(source["name"].lower())

            if scraper_class is None:
                continue

            self.html_scrapers.append(scraper_class(source))

        # RSS scraper
        for source in RSS_SOURCES:
            if not source.get("enabled", True):
                continue

            self.rss_scrapers.append(RSSScraper(source))

    def get_scrapers(self):
        """Mengembalikan seluruh scraper yang aktif."""
        return self.html_scrapers + self.rss_scrapers

    def _run_scraper(self, scraper):
        """Menjalankan satu scraper."""
        articles = scraper.scrape()
        return scraper.source["name"], articles

    def run(self, selected=None):
        """
        Menjalankan scraper.

        Parameters
        ----------
        selected : list[str] | None
            Daftar nama source yang akan dijalankan.
            Jika None, semua scraper aktif dijalankan.

        Returns
        -------
        tuple[list, dict, list]
            (
                all_articles,
                {"Antara": 15, "Tempo": 45},
                ["Tempo"]
            )
        """

        scrapers = self.get_scrapers()

        if selected:
            selected = {name.lower() for name in selected}

            scrapers = [
                scraper
                for scraper in scrapers
                if scraper.source["name"].lower() in selected
            ]

        if not scrapers:
            return [], {}, []

        logger = logging.getLogger("ScraperManager")

        logger.info(
            "Running %d scraper(s) in parallel...",
            len(scrapers),
        )

        all_articles = []
        source_counts = {}
        failed_sources = []

        with ThreadPoolExecutor(
            max_workers=min(8, len(scrapers))
        ) as executor:

            futures = {
                executor.submit(self._run_scraper, scraper): scraper
                for scraper in scrapers
            }

            for future in as_completed(futures):
                scraper = futures[future]
                source_name = scraper.source["name"]

                scraper_start = time.perf_counter()

                try:
                    _, articles = future.result()

                    count = len(articles)

                    source_counts[source_name] = count
                    all_articles.extend(articles)

                    elapsed = time.perf_counter() - scraper_start

                    logger.info(
                        "[SUCCESS] %s collected %d article(s) in %.2f seconds",
                        source_name,
                        count,
                        elapsed,
                    )

                except Exception:
                    elapsed = time.perf_counter() - scraper_start

                    source_counts[source_name] = 0
                    failed_sources.append(source_name)

                    logger.exception(
                        "[FAILED] %s failed after %.2f seconds",
                        source_name,
                        elapsed,
                    )

        logger.info(
            "Finished. Total articles collected: %d",
            len(all_articles),
        )

        return (
            all_articles,
            source_counts,
            failed_sources,
        )