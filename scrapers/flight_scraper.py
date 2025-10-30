# scrapers/flight_scraper.py
import requests
from bs4 import BeautifulSoup

class FlightScraper:
    def __init__(self):
        self.demo_flights = [
            {"destination": "Paris", "price": "$450", "airline": "Air France", "duration": "5 days"},
            {"destination": "Tokyo", "price": "$890", "airline": "Japan Airlines", "duration": "7 days"},
            {"destination": "New York", "price": "$320", "airline": "Delta", "duration": "3 days"},
            {"destination": "London", "price": "$550", "airline": "British Airways", "duration": "4 days"}
        ]
    
    def scrape_demo_flights(self, destination=None):
        if destination:
            return [flight for flight in self.demo_flights 
                   if destination.lower() in flight['destination'].lower()]
        return self.demo_flights
    
    def scrape_from_api(self):
        return self.demo_flights