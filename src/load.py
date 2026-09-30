#python3 src/load.py

import os
import sqlite3
import pandas as pd
from transform import transform_nasa_data

#  Loads the cleaned DataFrame into a SQLite database table.
def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str = "environmental_metrics"):

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    print(f"Connecting to SQLite database at {db_path}...")
    conn = sqlite3.connect(db_path)
    
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    
    cursor = conn.cursor()
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_date ON {table_name} (date);")
    conn.commit()
    
    query = f"SELECT COUNT(*) FROM {table_name};"
    row_count = cursor.execute(query).fetchone()[0]
    
    conn.close()
    print(f"Successfully loaded {row_count} rows into table '{table_name}' in {db_path}!")

if __name__ == "__main__":
    raw_path = "data/raw/nasa_power_raw.json"
    db_file_path = "data/processed/ecowatch.db"
    
    cleaned_df = transform_nasa_data(raw_path)
    
    load_to_sqlite(cleaned_df, db_file_path)