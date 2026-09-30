import json
import os
import pandas as pd
import numpy as np

# Parses the JSON NASA POWER structure, cleans missing values (-999) and converts it into a DataFrame.

def transform_nasa_data(raw_json_path: str) -> pd.DataFrame:

    print(f"Loading raw data from {raw_json_path}...")
    with open(raw_json_path, "r") as f:
        raw_data = json.load(f)
        
    coordinates = raw_data.get("geometry", {}).get("coordinates", [None, None])
    lon, lat = coordinates[0], coordinates[1]
    
    parameters = raw_data.get("properties", {}).get("parameter", {})
    
    if not parameters:
        raise ValueError("No parameters found in the raw JSON file.")
        
    df = pd.DataFrame(parameters)
    
    df.reset_index(inplace=True)
    df.rename(columns={"index": "date_str"}, inplace=True)
    
    column_mapping = {
        "T2M": "temperature_2m",
        "PRECTOTCORR": "precipitation",
        "ALLSKY_SFC_SW_DWN": "solar_radiation"
    }
    df.rename(columns=column_mapping, inplace=True)
    
    df["latitude"] = lat
    df["longitude"] = lon
    
    df.replace(-999, np.nan, inplace=True)
    df.replace(-999.0, np.nan, inplace=True)
    
    df["date"] = pd.to_datetime(df["date_str"], format="%Y%m%d")
    df.drop(columns=["date_str"], inplace=True)
    
    df = df[["date", "latitude", "longitude", "temperature_2m", "precipitation", "solar_radiation"]]
    
    df.sort_values("date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    print(f"Transformation complete. Cleaned {len(df)} rows.")
    print(df.head())
    
    return df

if __name__ == "__main__":
    
    raw_path = "data/raw/nasa_power_raw.json"
    cleaned_df = transform_nasa_data(raw_path)
    
    os.makedirs("data/processed", exist_ok=True)
    processed_path = "data/processed/nasa_power_clean.csv"
    cleaned_df.to_csv(processed_path, index=False)
    print(f"Processed CSV saved to {processed_path}")