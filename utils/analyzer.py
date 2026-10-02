def analyze_water_risk(weather):
    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]

    risk_level = "Low"
    recommendations = []

    if temperature > 35:
        risk_level = "High"
        recommendations.append(
            "High temperature detected. Increase water conservation measures."
        )

    if humidity < 30:
        risk_level = "High"
        recommendations.append(
            "Low humidity detected. Risk of water shortage may increase."
        )

    if rainfall == 0:
        risk_level = "High"
        recommendations.append(
            "No rainfall detected. Consider water storage and efficient usage."
        )

    return {
        "location": weather["city"],
        "risk_level": risk_level,
        "recommendations": recommendations
    }