from scrapers.manager import ScraperManager


def test_manager_creation():
    manager = ScraperManager()

    assert isinstance(manager.get_scrapers(), list)


def test_manager_return_type():
    manager = ScraperManager()

    result = manager.run(selected=[])

    assert isinstance(result, tuple)
    assert len(result) == 3

    articles, source_counts, failed_sources = result

    assert isinstance(articles, list)
    assert isinstance(source_counts, dict)
    assert isinstance(failed_sources, list)