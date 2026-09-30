# python3 src/extract.py 

import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Fetches daily environmental/meteorological data from NASA POWER API for given coordinates and date range.

def fetch_nasa_power_data(lat: float, lon: float, start_date: str, end_date: str) -> dict:

    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    params = {
        "parameters": "T2M,PRECTOTCORR,ALLSKY_SFC_SW_DWN", # Temp, Precipitation, Solar Radiation
        "community": "AG", # Agroclimatology community
        "longitude": lon,
        "latitude": lat,
        "start": start_date,
        "end": end_date,
        "format": "JSON"
    }
    
    print(f"Fetching NASA POWER data for Lat: {lat}, Lon: {lon}...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("Successfully fetched data from NASA API!")
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")

if __name__ == "__main__":

    # Example coordinates for a region in South Africa
    LATITUDE = -29.1181
    LONGITUDE = 26.2247
    START_DATE = "20240101"
    END_DATE = datetime.now().strftime("%Y%m%d")
    
    data = fetch_nasa_power_data(LATITUDE, LONGITUDE, START_DATE, END_DATE)
    
    # Save raw output
    os.makedirs("data/raw", exist_ok=True)
    raw_file_path = "data/raw/nasa_power_raw.json"
    
    with open(raw_file_path, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"Raw data saved successfully to {raw_file_path}")