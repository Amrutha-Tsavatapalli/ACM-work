
import requests
from secret import WEATHER_API_KEY

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
    else:
        return f"Sorry, could not fetch weather for {city}."
