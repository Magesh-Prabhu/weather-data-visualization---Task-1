# 🌤️ Weather Data Visualization Using Python and OpenWeatherMap API

This beginner-friendly project demonstrates how to fetch real-time weather data from the OpenWeatherMap API and visualize it using Python's `matplotlib` and `seaborn` libraries.

It’s a great starting point for learning:
- API Integration
- JSON data handling
- Data Visualization
- GitHub project structure

---

## 📌 Project Objective

The goal is to:
1. **Fetch weather data** for a selected city using an API.
2. **Extract key metrics** like temperature, humidity, and pressure.
3. **Display them visually** using a bar chart.

---

## 🧰 Tools & Libraries Used

| Tool           | Purpose                         |
|----------------|---------------------------------|
| Python         | Programming language            |
| requests       | For calling the weather API     |
| matplotlib     | For data visualization (charts) |
| seaborn        | For clean chart styles          |
| OpenWeatherMap | Free public weather data API    |

---

## 🧑‍💻 How It Works

1. User selects a city (e.g., `Coimbatore`).
2. Python script calls OpenWeatherMap using your **API key**.
3. Data is returned in JSON format.
4. Script extracts:
   - Temperature in Celsius
   - Humidity in %
   - Atmospheric Pressure in hPa
5. The extracted values are displayed as a **bar chart** using seaborn and matplotlib.

---

## 🚀 Getting Started

### 📦 Clone the Repository
```bash
git clone https://github.com/Magesh-Prabhu/weather-data-visualization.git
cd weather-data-visualization

