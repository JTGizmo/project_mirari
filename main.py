from datetime import datetime
from weather import get_weather_request, print_weather_info


def main():
    city_name = input("Enter City name:")
    api_response = get_weather_request(city_name)
    weather_project = api_response.json()
    weather = weather_project["weather"]

    temperature = weather_project["main"]
    current_temp = temperature["temp"]
    feels_like = temperature["feels_like"]
    humidity = temperature["humidity"]

# TODO: Check whether we need to provide time in local timezone
# TODO: For weather application will need to design setting default location
    # sunrise and sunset figures
    sun = weather_project["sys"]
    sun_rise = datetime.fromtimestamp(sun["sunrise"])
    sun_set = datetime.fromtimestamp(sun["sunset"])

    # Passing it here
    print_weather_info(city_name, weather, current_temp, feels_like, humidity, sun_rise, sun_set)


if __name__ == "__main__":
    main()
