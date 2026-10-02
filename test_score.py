from utils.water_score import calculate_water_risk


score, level = calculate_water_risk(
    "Low",
    "High",
    "High"
)

print("Water Risk Score:", score)
print("Risk Level:", level)