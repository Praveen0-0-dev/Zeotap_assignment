#fetcher.py
import requests
def fetch_weather_data(city,api_key):
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
  response=requests.get(url)
  return response.json()
