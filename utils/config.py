import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# OpenWeather API Key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Check keys
def check_keys():
    missing = []

    if not GROQ_API_KEY:
        missing.append("GROQ_API_KEY")

    if not OPENWEATHER_API_KEY:
        missing.append("OPENWEATHER_API_KEY")

    return missing