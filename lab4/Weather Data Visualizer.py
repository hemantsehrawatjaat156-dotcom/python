
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")   # <-- change filename here
print("\n--- HEAD ---")
print(df.head())
print("\n--- INFO ---")
print(df.info())
print("\n--- DESCRIBE ---")
print(df.describe())

df['date'] = pd.to_datetime(df['date'], errors='coerce')

df = df.dropna(subset=['date'])

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

columns_needed = ['date', 'temperature', 'rainfall', 'humidity']
df = df[columns_needed]

print("\n--- CLEANED DATA ---")
print(df.head())

daily_mean = np.mean(df['temperature'])
daily_min = np.min(df['temperature'])
daily_max = np.max(df['temperature'])
daily_std = np.std(df['temperature'])

print("\n--- DAILY TEMPERATURE STATS ---")
print(f"Mean: {daily_mean:.2f}")
print(f"Min: {daily_min:.2f}")
print(f"Max: {daily_max:.2f}")
print(f"Std Dev: {daily_std:.2f}")

df['month'] = df['date'].dt.month

monthly_stats = df.groupby('month').agg({
    'temperature': ['mean', 'min', 'max'],
    'rainfall': 'sum',
    'humidity': 'mean'
})

print("\n--- MONTHLY STATS ---")
print(monthly_stats)

plt.figure(figsize=(12,5))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("daily_temperature.png")
plt.close()

monthly_rain = df.groupby('month')['rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall Total")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.tight_layout()
plt.savefig("monthly_rainfall.png")
plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.tight_layout()
plt.savefig("humidity_vs_temperature.png")
plt.close()

# Combined figure
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature")

plt.subplot(1,2,2)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temp vs Humidity")

plt.tight_layout()
plt.savefig("combined_plots.png")
plt.close()



season_map = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

df['season'] = df['month'].map(season_map)

season_stats = df.groupby('season').agg({
    'temperature': 'mean',
    'rainfall': 'sum',
    'humidity': 'mean'
})

print("\n--- SEASON STATS ---")
print(season_stats)


df.to_csv("cleaned_weather_data.csv", index=False)

with open("summary_report.txt", "w") as f:
    f.write("WEATHER DATA ANALYSIS REPORT\n")
    f.write("============================\n\n")
    f.write(f"Average Temperature: {daily_mean:.2f}\n")
    f.write(f"Highest Temperature: {daily_max:.2f}\n")
    f.write(f"Lowest Temperature: {daily_min:.2f}\n")
    f.write("\nSeason-wise summary:\n")
    f.write(str(season_stats))

print("\nAll tasks completed. Files exported.")
