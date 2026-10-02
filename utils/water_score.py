def calculate_water_risk(
    rainfall,
    temperature,
    demand
):
    score = 0

    # Rainfall factor
    if rainfall == "Low":
        score += 35
    elif rainfall == "Medium":
        score += 20
    else:
        score += 10

    # Temperature factor
    if temperature == "High":
        score += 35
    elif temperature == "Medium":
        score += 20
    else:
        score += 10

    # Water demand factor
    if demand == "High":
        score += 30
    elif demand == "Medium":
        score += 15
    else:
        score += 5


    if score >= 70:
        level = "🔴 High Risk"
    elif score >= 40:
        level = "🟡 Moderate Risk"
    else:
        level = "🟢 Low Risk"

    return score, level



# Dashboard stress level function
def get_stress_level(score):

    if score >= 80:
        return "Critical Water Stress"

    elif score >= 60:
        return "High Water Stress"

    elif score >= 40:
        return "Moderate Water Stress"

    else:
        return "Low Water Stress"



# AI dashboard scoring function
def calculate_water_score(weather, risk):

    score = 0

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]


    # Temperature factor
    if temperature > 35:
        score += 40

    elif temperature > 30:
        score += 25


    # Humidity factor
    if humidity < 30:
        score += 30

    elif humidity < 50:
        score += 15


    # Rainfall factor
    if rainfall == 0:
        score += 30

    elif rainfall < 5:
        score += 15


    if score > 100:
        score = 100


    return score