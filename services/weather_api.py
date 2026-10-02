import requests
from utils.config import OPENWEATHER_API_KEY


def get_weather(city):
    """
    Fetch current weather data from OpenWeather API.
    """

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
    "q": f"{city}, Pakistan",
    "appid": OPENWEATHER_API_KEY,
    "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("message", "Weather API error")
            }

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "rainfall": data.get("rain", {}).get("1h", 0)
        }

        return weather_data

    except Exception as e:
        return {
            "error": str(e)
        }