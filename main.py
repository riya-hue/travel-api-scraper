# main.py
from fastapi import FastAPI
from scrapers.flight_scraper import FlightScraper
import uvicorn  # This belongs HERE, not in flight_scraper.py

app = FastAPI()
scraper = FlightScraper()

@app.get("/")
def home():
    return {"message": "API is working!"}

@app.get("/flights")
def get_flights():
    return scraper.scrape_demo_flights()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)