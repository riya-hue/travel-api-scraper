# travel-api-scraper
A Python API that collects flight data and makes it available through a simple web interface.
```markdown
# Travel API Scraper

A FastAPI project that provides flight data through a REST API. Built to practice web scraping and API development.

## Quick Start

1. **Setup environment:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the API:**
```bash
python main.py
```

4. **Test the endpoints:**
- http://localhost:8000/ - API status
- http://localhost:8000/flights - All flights data
- http://localhost:8000/flights/paris - Flights to Paris

## Project Structure

```
travel-api-scraper/
├── main.py                 # FastAPI server
├── scrapers/
│   ├── flight_scraper.py   # Flight data handling
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Features

- REST API with FastAPI
- Flight data filtering by destination
- JSON responses
- Easy to extend with real data sources

## Tech Used

- Python
- FastAPI
- BeautifulSoup
- Requests

## About

This was a practice project to learn backend development with Python and FastAPI. Planning to add more features like real-time flight data and AI-powered travel suggestions.

---
*Learning backend development one project at a time.*
```
