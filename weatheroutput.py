from weather import Weather
from weather_api import WeatherApi


class WeatherOutput(Weather):
    def print_weather_info(self):
        # TODO: Create default city on initial load of the program, that then can be changed.
        print(f"The weather in {WeatherApi().get_weather_request()} is with {self.weather[0]['description']}\n"
              f"Current temperature: {int(self.current_temp)}°C\n"
              f"And it feels like {int(self.feels_like)}°C\n"
              f"Current humidity is at {self.humidity}%\n"
              f"Sunrise today was at {self.sun_rise:%H:%M} AM\n"
              f"The sun will set tonight at {self.sun_set:%H:%M} PM")