from config import RSS_SOURCES
from scrapers.rss import RSSScraper
from utils.exporter import Exporter
from utils.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("Starting news scraping...")

    all_articles = []

    for source in RSS_SOURCES:
        logger.info(f"Scraping {source['name']}...")

        scraper = RSSScraper(source)
        articles = scraper.scrape()

        logger.info(f"Found {len(articles)} articles")

        all_articles.extend(articles)

    exporter = Exporter()

    exporter.to_csv(all_articles)
    exporter.to_json(all_articles)

    try:
        exporter.to_excel(all_articles)
    except Exception as e:
        logger.warning(f"Excel export skipped: {e}")

    logger.info("")
    logger.info("Scraping completed successfully!")
    logger.info(f"Total articles: {len(all_articles)}")
    logger.info("Files saved in output/ folder")


if __name__ == "__main__":
    main()
