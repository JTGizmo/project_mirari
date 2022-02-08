from weather_api import WeatherApi
from datetime import datetime


class Weather:
    def __init__(self):
        self.weather_project = WeatherApi().get_weather_request()
        self.weather = self.weather_project["weather"]

        self.temperature = self.weather_project["main"]
        self.current_temp = self.temperature["temp"]
        self.feels_like = self.temperature["feels_like"]
        self.humidity = self.temperature["humidity"]

        # TODO: Check whether we need to provide time in local timezone
        # TODO: For weather application will need to design setting default location
        # sunrise and sunset figures
        self.sun = self.weather_project["sys"]
        self.sun_rise = datetime.fromtimestamp(self.sun["sunrise"])
        self.sun_set = datetime.fromtimestamp(self.sun["sunset"])
