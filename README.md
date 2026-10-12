# EcoWatchSA
A Drought &amp; Vegetation Risk Intelligence Platform.

Southern Africa faces increasing vulnerability to severe climate shocks, prolonged droughts, and erratic rainfall patterns that directly threaten agricultural productivity, water security, and regional food stability. Traditional environmental monitoring infrastructure can be fragmented, slow to aggregate, or difficult to access in near-real time. National space and research agencies (such as SANSA) require scalable, automated systems capable of ingesting large volumes of Earth observation and meteorological data to monitor environmental stress and support early-warning disaster response.

**EcoWatch SA** provides a robust, modular ETL (Extract, Transform, Load) data pipeline that automates the ingestion of raw NASA spatial-temporal telemetry, cleans and normalizes variables (like temperature, precipitation, and solar radiation), and stores the structured records into an indexed SQLite data warehouse optimized for high-performance querying and downstream data analysis.

## Project Overview
**EcoWatch SA** is built as a portfolio demonstration for Earth Observation and space-tech applications.

## Data Source
EcoWatch SA ingests daily spatial-temporal meteorological and climate telemetry directly from the **NASA POWER API** (Prediction of Worldwide Energy Resources). 

The platform captures key environmental indicators across target grid points in Southern Africa, including:
* **Temperature at 2 Meters** (`temperature_2m`)
* **Precipitation** (`precipitation`)
* **Solar Radiation** (`solar_radiation`)

## Project Architecture

```text
EcoWatchSA/
│
├── .streamlit/
│   └── config.toml   # Custom pastel pink theme configuration
├── data/
│   ├── raw/          # Raw downloaded JSON payloads from NASA API
│   └── processed/    # SQLite data warehouse (ecowatch.db) and generated EDA plots
│
├── src/
│   ├── __init__.py
│   ├── extract.py          # NASA POWER API ingestion script
│   ├── transform.py        # Data parsing, missing value handling (-999), and structuring
│   ├── load.py             # SQLite database loader
│   ├── analyze.py          # Database query loader and statistical summaries
│   ├── visualize_trends.py # Time-series rolling average plotting
│   └── correlation_analysis.py # Statistical correlation matrices & heatmaps
│
├── app.py            # Interactive Streamlit Web Dashboard
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
    python3 src/transform.py

    # Step 2: Transform, clean, and load into SQLite database
    python3 src/load.py
    ```

3. **Data Analysis & Visualizations**

   ```bash 
   # Generate statistical summaries and correlation heatmaps
   python3 src/correlation_analysis.py

   # Generate rolling average time-series trend plots
   python3 src/visualize_trends.py
   ```

4. **Streamlit Dashboard**
   `streamlit run app.py`






