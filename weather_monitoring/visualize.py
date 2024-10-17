import matplotlib.pyplot as plt

def plot_temperature(dates, temperatures):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-')
    plt.title("Daily Temperatures")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weather_conditions(dates, conditions):
    plt.figure(figsize=(10, 5))
    plt.bar(dates, conditions, color='skyblue')
    plt.title("Daily Weather Conditions")
    plt.xlabel("Date")
    plt.ylabel("Weather Condition")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
