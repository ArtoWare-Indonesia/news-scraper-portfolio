from scrapers.html.antara import AntaraScraper
from scrapers.html.tempo import TempoScraper
from scrapers.html.detik import DetikScraper
from scrapers.html.cnbc import CNBCScraper
from scrapers.html.republika import RepublikaScraper

HTML_SCRAPERS = {
    "antara": AntaraScraper,
    "tempo": TempoScraper,
    "detik": DetikScraper,
    "cnbc": CNBCScraper,
    "republika": RepublikaScraper,
}