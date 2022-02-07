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

        """def get_weather_request(self):
        # using requests to build the URL
        api = {"q": self.city_name, "units": "metric", "appid": self.api_key}
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=api)
        return response"""

    def print_weather_info(self):
        print(f"The weather in {self.city_name} is with {self.weather[0]['description']}\n"
              f"Current temperature: {int(self.current_temp)}°C\n"
              f"And it feels like {int(self.feels_like)}°C\n"
              f"Current humidity is at {self.humidity}%\n"
              f"Sunrise today was at {self.sun_rise:%H:%M} AM\n"
              f"The sun will set tonight at {self.sun_set:%H:%M} PM")
