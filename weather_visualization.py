import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = '4bfac7645d985ebfc883f6ca1abc33e0'
CITY = 'Chennai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(URL)
data = response.json()

weather_list = data['list']
df = pd.DataFrame({
    'datetime': [datetime.fromtimestamp(item['dt']) for item in weather_list],
    'temperature (°C)': [item['main']['temp'] for item in weather_list],
    'humidity (%)': [item['main']['humidity'] for item in weather_list]
})

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='datetime', y='temperature (°C)', marker='o', label='Temperature (°C)')
sns.lineplot(data=df, x='datetime', y='humidity (%)', marker='x', label='Humidity (%)')
plt.xticks(rotation=45)
plt.title(f'5-Day Weather Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()
