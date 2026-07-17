from pathlib import Path

from utils.exporter import Exporter


ARTICLES = [
    {
        "title": "Article",
        "url": "https://example.com",
        "source": "Example",
        "category": "News",
        "published": "2026-07-17",
        "summary": "Summary",
        "image": "",
    }
]


def test_export_all(tmp_path):
    exporter = Exporter(output_dir=tmp_path)

    exported = exporter.export_all(ARTICLES)

    assert len(exported) == 3

    for filename in exported:
        assert Path(filename).exists()


def test_export_empty(tmp_path):
    exporter = Exporter(output_dir=tmp_path)

    exported = exporter.export_all([])

    assert exported == []