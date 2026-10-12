import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_trend_plots(db_path: str = "data/processed/ecowatch.db"):
    """
    Queries the database and generates time-series plots for temperature and precipitation.
    """

    print("Loading data from database for visualization...")
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM environmental_metrics " \
    "ORDER BY date ASC;", conn, parse_dates=["date"])
    conn.close()
    

    df["temp_rolling_30d"] = df["temperature_2m"].rolling(window=30).mean()
    df["precip_rolling_30d"] = df["precipitation"].rolling(window=30).mean()
    
    os.makedirs("data/processed/plots", exist_ok=True)
    
    # Plot 1: Temperature 
    plt.figure(figsize=(12, 5))

    plt.plot(df["date"], df["temperature_2m"], label="Daily Temp (°C)", color="orange", alpha=0.4)
    plt.plot(df["date"], df["temp_rolling_30d"], label="30-Day Avg Temp", color="red", linewidth=2)

    plt.title("EcoWatch SA: Daily vs 30 Day Rolling Temperature Trend")

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    temp_plot_path = "data/processed/plots/temperature_trend.png"
    plt.savefig(temp_plot_path)
    plt.close()
    print(f"Saved temperature trend plot to {temp_plot_path}")
    
    # Plot 2: Precipitation
    plt.figure(figsize=(12, 5))

    plt.bar(df["date"], df["precipitation"], label="Daily Precipitation (mm)", color="blue", alpha=0.3)
    plt.plot(df["date"], df["precip_rolling_30d"], label="30-Day Avg Precipitation", color="navy", linewidth=2)

    plt.title("EcoWatch SA: Regional Precipitation & Rainfall Distribution")

    plt.xlabel("Date")
    plt.ylabel("Precipitation (mm)")
    plt.legend()

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    precip_plot_path = "data/processed/plots/precipitation_trend.png"
    plt.savefig(precip_plot_path)
    plt.close()
    
    print(f"Saved precipitation trend plot to {precip_plot_path}")

if __name__ == "__main__":
    generate_trend_plots()