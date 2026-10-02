def analyze_water_crisis(weather_data, location):
    """
    Analyze weather conditions and provide water management advice.
    """

    temperature = weather_data.get("temperature", 0)
    humidity = weather_data.get("humidity", 0)
    rainfall = weather_data.get("rainfall", 0)

    advice = []

    if temperature > 35:
        advice.append(
            "High temperature detected. Increase water conservation measures."
        )

    if humidity < 30:
        advice.append(
            "Low humidity detected. Risk of water shortage may increase."
        )

    if rainfall == 0:
        advice.append(
            "No rainfall detected. Consider water storage and efficient usage."
        )

    if not advice:
        advice.append(
            "Current conditions look stable. Continue monitoring water resources."
        )

    return {
        "location": location,
        "risk_level": "High" if len(advice) >= 2 else "Moderate",
        "recommendations": advice
    }