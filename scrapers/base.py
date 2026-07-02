import requests
from abc import ABC, abstractmethod
from config import HEADERS


class BaseScraper(ABC):
    """
    Base class untuk semua scraper.
    """

    def __init__(self):
        self.headers = HEADERS

    def fetch(self, url):
        response = requests.get(
            url,
            headers=self.headers,
            timeout=15
        )
        response.raise_for_status()
        return response

    @abstractmethod
    def scrape(self):
        """
        Harus diimplementasikan oleh setiap scraper.
        """
        pass