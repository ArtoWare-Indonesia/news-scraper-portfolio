from models.news import NewsItem


def test_newsitem_defaults():
    item = NewsItem()

    assert item.title == ""
    assert item.url == ""
    assert item.source == ""
    assert item.category == ""
    assert item.published == ""
    assert item.summary == ""
    assert item.image == ""


def test_newsitem_to_dict():
    item = NewsItem(
        title="Test Title",
        url="https://example.com",
        source="Example",
        category="Tech",
        published="2026-07-17",
        summary="Summary",
        image="image.jpg",
    )

    data = item.to_dict()

    assert data["title"] == "Test Title"
    assert data["url"] == "https://example.com"
    assert data["source"] == "Example"
    assert data["category"] == "Tech"
    assert data["published"] == "2026-07-17"
    assert data["summary"] == "Summary"
    assert data["image"] == "image.jpg"