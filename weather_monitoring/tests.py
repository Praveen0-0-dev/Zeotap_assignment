import unittest
from .fetcher import fetch_weather_data
from .processor import kelvin_to_celsius

class TestWeatherMonitoring(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        temp_k = 300  # Example Kelvin temperature
        temp_c = kelvin_to_celsius(temp_k)
        self.assertAlmostEqual(temp_c, 26.85, places=2)  # 300K should be about 26.85°C

    def test_fetch_weather_data(self):
        # You might want to mock this if you don't want to hit the API each time
        city = "Delhi"
        api_key = "your_api_key"  # Replace with your API key
        data = fetch_weather_data(city, api_key)
        self.assertIn("main", data)  # Ensure data has the 'main' key

if _name_ == "_main_":
    unittest.main()
