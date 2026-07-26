# News Scraper Portfolio

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-v0.7.0-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)

A modular Python news scraper framework built as a freelance portfolio project.

This project demonstrates how to build reusable, maintainable, and extensible web scrapers using modern Python architecture. It supports scraping news from multiple sources using both **HTML** and **RSS**, exporting the collected articles into various formats.

---

# Current Release

**Latest Version:** **v0.7.0**

## Command Line Interface

```bash
python main.py --help

python main.py --source antara

python main.py --source republika

python main.py --limit 10

python main.py --format json

python main.py --source tempo --limit 5 --format csv
```

---

# Features

- Modular scraper architecture
- HTML and RSS scraper support
- Parallel scraping manager
- Reusable `BaseScraper`
- Automatic HTTP retry using `requests.Session`
- BeautifulSoup HTML parsing
- Feedparser RSS parsing
- Standardized `NewsItem` data model
- CSV, JSON and Excel export
- Timestamped output files
- Configurable scraper registry
- Improved logging and execution timing
- Scraping summary report
- Initial unit tests with `pytest`
- Lightweight (no pandas dependency)
- Cross-platform (Windows & Linux)

## New in v0.7.0

- Added **Detik** scraper
- Added **CNBC Indonesia** scraper
- Added **Republika RSS** scraper
- Parallel scraper execution
- CLI improvements
- Better logging and execution summary
- Cleaner exporter implementation

---

# Supported Sources

## HTML

| Source | Status |
|---------|--------|
| Antara | ✅ |
| Tempo | ✅ |
| Detik | ✅ |
| CNBC Indonesia | ✅ |

## RSS

| Source | Status |
|---------|--------|
| Republika | ✅ |

---

# Architecture

```
                    main.py
                        │
                        ▼
                 ScraperManager
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 HTML Scrapers     RSS Scrapers      Exporter
      │                 │
      ▼                 ▼
 BaseScraper      RSSScraper
      │                 │
      └──────────┬──────┘
                 ▼
             NewsItem
                 │
                 ▼
       CSV / JSON / XLSX
```

---

# Project Structure

```
news-scraper-portfolio/

├── config.py
├── main.py
├── pytest.ini
├── requirements.txt
│
├── models/
│   └── news.py
│
├── scrapers/
│   ├── base.py
│   ├── manager.py
│   ├── registry.py
│   ├── rss.py
│   └── html/
│       ├── antara.py
│       ├── tempo.py
│       ├── detik.py
│       └── cnbc.py
│
├── utils/
│   ├── cli.py
│   ├── exporter.py
│   └── logger.py
│
├── docs/
│   └── images/
│
├── output/
│
└── tests/
    ├── test_exporter.py
    ├── test_manager.py
    └── test_newsitem.py
```

---

# Tech Stack

- Python 3.13
- Requests
- BeautifulSoup4
- Feedparser
- urllib3
- openpyxl
- pytest

---

# Requirements

- Python 3.13+
- pip
- Virtual Environment (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Installation

```bash
git clone https://github.com/ArtoWare-Indonesia/news-scraper-portfolio.git

cd news-scraper-portfolio

python -m venv .venv

source .venv/bin/activate      # Linux

.venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

---

# Running the Project

Example:

```text
Source : None
Format : all
Limit  : None

============================================================
News Scraper Portfolio v0.7.0
============================================================

Starting news scraping...

Running 5 scraper(s)...

Running Antara
Running Tempo
Running Detik
Running CNBC Indonesia
Running Republika

Finished.

============================================================
SCRAPING SUMMARY
============================================================
Successful : 5
Failed     : 0
Articles   : 78

Articles by source

Antara      : 15
Tempo       : 12
Detik       : 20
CNBC        : 31
Republika   : 10

Exported files

output/news_20260724_170611.csv
output/news_20260724_170611.json
output/news_20260724_170611.xlsx

Elapsed time : 2.01 seconds
============================================================
```

---

# Output Preview

### CSV

![CSV Output](docs/images/news.csv.png)

### Excel

![Excel Output](docs/images/news.xlsx.png)

### JSON

![JSON Output](docs/images/news.json.png)

---

# Output Directory

Generated files are stored inside:

```
output/

news_YYYYMMDD_HHMMSS.csv
news_YYYYMMDD_HHMMSS.json
news_YYYYMMDD_HHMMSS.xlsx
```

---

# Testing

Run all unit tests:

```bash
pytest
```

---

# Design Principles

- Modular Architecture
- Template Method Pattern
- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Reusable Components
- Standardized Data Model

---

# Roadmap

## v0.8.0

- YAML configuration support
- JSON configuration support
- Date filtering
- Category filtering

## v1.0.0

- Stable API
- Plugin-based scraper system
- GitHub Actions CI
- Complete documentation
- PyPI package

---

# License

This project is intended for educational purposes, portfolio demonstrations, and freelance showcasing.

Licensed under the MIT License.
