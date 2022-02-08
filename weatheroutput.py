from weather import Weather
from weather_api import WeatherApi


class WeatherOutput(Weather, WeatherApi):
    def print_weather_info(self):
        """Provides the weather output text"""
        print(f"The weather in {WeatherApi().city_name} is with {self.weather[0]['description']}\n"
              f"Current temperature: {int(self.current_temp)}°C\n"
              f"And it feels like {int(self.feels_like)}°C\n"
              f"Current humidity is at {self.humidity}%\n"
              f"Sunrise today was at {self.sun_rise:%H:%M} AM\n"
              f"The sun will set tonight at {self.sun_set:%H:%M} PM")
