import os

import requests
from dotenv import load_dotenv

# create .env file to load the private API keys
load_dotenv()
weather_api_key = os.getenv("weather_api_key")


def get_weather_request(city_name):
    api_key = weather_api_key
    # using requests to build the URL
    api = {"q": city_name, "units": "metric", "appid": api_key}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=api)
    return response


def print_weather_info(city_name, weather, celsius, feels_like, humidity, sun_rise, sun_set):
    print(f"The weather in {city_name} is with {weather[0]['description']}\n"
          f"Current temperature: {int(celsius)}°C\n"
          f"And it feels like {int(feels_like)}°C\n"
          f"Current humidity is at {humidity}%\n"
          f"Sunrise today was at {sun_rise:%H:%M} AM\n"
          f"The sun will set tonight at {sun_set:%H:%M} PM")




