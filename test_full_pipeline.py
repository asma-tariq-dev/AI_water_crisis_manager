from services.weather_api import get_weather
from services.water_analysis import analyze_water_crisis
from services.groq_service import ask_groq


city = "Khanpur"

# 1. Get weather
weather = get_weather(city)

print("\n🌦️ Weather Data:")
print(weather)


# 2. Analyze water risk
analysis = analyze_water_crisis(weather, city)

print("\n💧 Water Analysis:")
print(analysis)


# 3. Ask AI for recommendations
prompt = f"""
Location: {city}

Weather Data:
{weather}

Water Analysis:
{analysis}

Give practical water crisis management recommendations for this area.
"""

response = ask_groq(prompt)

print("\n🤖 AI Recommendation:")
print(response)