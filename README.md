# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY: CODETECH IT SOLUTION

NAME: BHARGAV SAAWANT B

INTERN ID: CT04WU190

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

---

## Project Overview  
This project fetches real-time **5-day weather forecast** data from the **OpenWeatherMap API** for a given city and visualizes the temperature trends using **Matplotlib**. The tool parses and displays temperature forecasts at 3-hour intervals, making it useful for planning and analysis.

---

## Features

1. **Real-Time Weather Forecast**  
   Fetches the latest 5-day temperature data using OpenWeatherMap’s API.

2. **Automatic Parsing & Formatting**  
   Converts timestamps into human-readable date formats and extracts temperature data.

3. **Data Visualization**  
   Plots temperature variation over time using line plots for easy understanding.

4. **City-Based Forecasting**  
   Customizable to any city by changing the `CITY` variable.

5. **User-Friendly Output**  
   Handles API errors gracefully and shows useful messages if anything goes wrong.

---

## Installation & Setup

### Required Libraries:
```bash
pip install requests matplotlib pandas
```

### Configuration:
- Get your API key from: [https://openweathermap.org/api](https://openweathermap.org/api)
- Replace `API_KEY` in the script with your personal API key:
  ```python
  API_KEY = "your_api_key_here"
  ```

---

## How It Works

1. **Fetching Weather Data**  
   The function `get_weather_data()` sends a request to the OpenWeatherMap 5-day forecast endpoint for the specified city.

2. **Parsing the Forecast**  
   The `parse_data()` function extracts:
   - Forecast timestamp
   - Temperature in °C  
   It returns a DataFrame with parsed information.

3. **Visualizing the Forecast**  
   `visualize_data()` generates a clean line plot using **Matplotlib** to display temperature variation across the 5-day forecast.

---

## Libraries Used

- **Requests**: To fetch data from the OpenWeatherMap API  
- **Matplotlib**: To plot the forecast data  
- **Pandas**: For data manipulation and formatting  
- **Datetime**: For timestamp conversion

---
## OUTPUT
![task1_output](https://github.com/user-attachments/assets/a504a73d-5b19-40d0-a066-7e239714eed8)
