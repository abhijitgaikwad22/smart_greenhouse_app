"""
Smart Suggestion Engine
Generates dynamic advisory suggestions based on latest detection
"""

import pandas as pd

CSV_PATH = "data/history.csv"

def generate_suggestions():

    suggestions = []

    try:
        df = pd.read_csv(CSV_PATH)

        if df.empty:
            return ["No data available for suggestions"]

        latest = df.iloc[-1]

        temp = latest['Temperature']
        humidity = latest['Humidity']
        soil = latest['Soil_Moisture']
        light = latest['Light']

        # 🌡 Temperature Logic
        if temp > 30:
            suggestions.append("Improve cooling / ventilation")

        elif temp < 15:
            suggestions.append("Increase greenhouse temperature")

        # 💧 Humidity Logic
        if humidity < 60:
            suggestions.append("Improve humidity levels")

        elif humidity > 85:
            suggestions.append("Reduce excess humidity")

        # 🌱 Soil Moisture Logic
        if soil < 40:
            suggestions.append("Monitor soil moisture")

        # ☀ Light Logic
        if light < 50:
            suggestions.append("Optimize light exposure")

        if not suggestions:
            suggestions.append("All environmental conditions are stable")

    except Exception:
        suggestions = ["Unable to generate suggestions"]

    return suggestions