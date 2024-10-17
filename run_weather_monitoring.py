from weather_monitoring.fetcher import fetch_weather_data
from weather_monitoring.processor import kelvin_to_celsius
from weather_monitoring.alert import check_alerts

def main():
    # Fetch weather data for a specific city
    city = "Delhi"
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
    weather_data = fetch_weather_data(city, api_key)

    # Convert temperature to Celsius
    temp_k = weather_data['main']['temp']
    temp_c = kelvin_to_celsius(temp_k)
    print(f"Temperature in {city}: {temp_c:.2f} °C")

    # Check for alerts (e.g., if temperature exceeds 35 °C)
    check_alerts(temp_c, threshold=35)

if _name_ == "_main_":
    main()
