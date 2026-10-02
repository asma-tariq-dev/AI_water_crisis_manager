from services.weather_api import get_weather


city = "Khanpur"

weather = get_weather(city)

print(weather)