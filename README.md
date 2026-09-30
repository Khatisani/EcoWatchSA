# EcoWatchSA
A Drought &amp; Vegetation Risk Intelligence Platform.

Southern Africa faces increasing vulnerability to severe climate shocks, prolonged droughts, and erratic rainfall patterns that directly threaten agricultural productivity, water security, and regional food stability. Traditional environmental monitoring infrastructure can be fragmented, slow to aggregate, or difficult to access in near-real time. National space and research agencies (such as SANSA) require scalable, automated systems capable of ingesting large volumes of Earth observation and meteorological data to monitor environmental stress and support early-warning disaster response.

**EcoWatch SA** provides a robust, modular ETL (Extract, Transform, Load) data pipeline that automates the ingestion of raw NASA spatial-temporal telemetry, cleans and normalizes variables (like temperature, precipitation, and solar radiation), and stores the structured records into an indexed SQLite data warehouse optimized for high-performance querying and downstream data analysis.

## Project Overview
**EcoWatch SA** is built as a portfolio demonstration for Earth Observation and space-tech applications.

## Project Architecture
``` text
ecowatch-sa/
│
├── data/
│   ├── raw/          # Raw downloaded JSON payloads from NASA API
│   └── processed/    # Cleaned CSVs and optimized SQLite data warehouse (ecowatch.db)
│
├── src/
│   ├── init.py
│   ├── extract.py    # NASA POWER API ingestion script
│   ├── transform.py  # Data parsing, missing value handling (-999), and structuring
│   └── load.py       # SQLite database loader
│
├── requirements.txt
└── README.md
```

## Getting Started (Phase 1: ETL Pipeline)

1. **Clone the repository and install dependencies:**
   ```bash
   git clone [https://github.com/khatisani/EcoWatchSA.git](https://github.com/khatisani/EcoWatchSA.git)
   cd EcoWatchSA
   pip install -r requirements.txt
   ```

2. **Run the complete ETL pipeline:***

    ```bash
    # Step 1: Extract raw data from NASA API
    python3 src/extract.py

    # Step 3: Cleaning, handling missing values, and formatting
    python3 src/ransform.py

    # Step 2: Transform, clean, and load into SQLite database
    python3 src/load.py
    ```






