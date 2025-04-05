import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

API_KEY = "ce872ca8e8da71811bb617d15df8158e"  # <-- Get this from OpenWeatherMap
CITY = "Mumbai"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def parse_data(json_data):
    dates, temps = [], []

    for item in json_data['list']:
        date = datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        dates.append(date)
        temps.append(temp)

    return pd.DataFrame({"Date": dates, "Temperature (°C)": temps})

def visualize_data(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Temperature (°C)"], marker='o', linestyle='-')
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    weather_json = get_weather_data(CITY)
    if weather_json.get("cod") == "200":
        df_weather = parse_data(weather_json)
        visualize_data(df_weather)
    else:
        print("Error:", weather_json.get("message", "Something went wrong."))
