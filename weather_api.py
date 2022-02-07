import os
import requests
from typing import Dict
from dotenv import load_dotenv


class WeatherApi:
    def __init__(self):
        """Loads API configuration from environment variables."""
        load_dotenv()
        self.city_name = os.getenv("default_city")
        self.api_key = os.getenv("weather_api_key")
        self.api_url = os.getenv("weather_api_url")

    def get_weather_request(self) -> Dict:
        """Compiles the weather API url and returns the JSON."""
        api = {"q": self.city_name, "units": "metric", "appid": self.api_key}
        response = requests.get(self.api_url, params=api)
        return response.json()
