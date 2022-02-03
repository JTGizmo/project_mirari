from weather import Weather


def main():
    input_city_name = input("Enter City name:")
    weather_output = Weather(input_city_name)
    weather_output.print_weather_info()

if __name__ == "__main__":
    main()
