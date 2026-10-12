import sqlite3
import pandas as pd

def load_data_from_db(db_path: str = "data/processed/ecowatch.db") -> pd.DataFrame:
    """
    Queries the SQLite data warehouse and returns the environmental metrics as a DataFrame.
    """

    print(f"Connecting to database at {db_path}...")
    conn = sqlite3.connect(db_path)
    
    query = "SELECT * FROM environmental_metrics ORDER BY date ASC;"
    df = pd.read_sql(query, conn, parse_dates=["date"])
    
    conn.close()
    print(f"Loaded {len(df)} records successfully for analysis!")
    return df

if __name__ == "__main__":
    
    df = load_data_from_db()
    print("\nDataset Summary Statistics:")
    print(df.describe())