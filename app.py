import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="EcoWatch SA | Environmental Intelligence Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_environmental_data(db_path: str = "data/processed/ecowatch.db") -> pd.DataFrame:
    """
    Connects to the SQLite data warehouse, loads environmental metrics,
    and caches the result for optimal dashboard performance.
    """

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM environmental_metrics ORDER BY date ASC;", conn, parse_dates=["date"])
    conn.close()

    return df

def main():
    try:
        df = load_environmental_data()
    except Exception as e:
        st.error(f"Database connection error: {e}. Please ensure Phase 1 load script has been run.")
        return

    
    # Sidebar
    st.sidebar.title("🌍 EcoWatch SA")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navigation & Filters")
    
    navigation = st.sidebar.radio("Go to:", ["Overview & Trends", "Raw Data Inspector"])
    
    st.sidebar.markdown("---")

    st.sidebar.subheader("Spatial & Temporal Filters")
    unique_coords = df[['latitude', 'longitude']].drop_duplicates().apply(
        lambda row: f"Lat: {row['latitude']}, Lon: {row['longitude']}", axis=1
    ).tolist()
    
    selected_coord_str = st.sidebar.selectbox("Select Target Grid Point:", unique_coords)
    
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    
    date_range = st.sidebar.date_input(
        "Filter Date Range:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("EcoWatch SA v1.0 • Built for regional climate tracking & environmental monitoring.")


    selected_lat = float(selected_coord_str.split(",")[0].replace("Lat: ", ""))
    selected_lon = float(selected_coord_str.split(",")[1].replace(" Lon: ", ""))
    
    filtered_df = df[
        (df["latitude"] == selected_lat) & 
        (df["longitude"] == selected_lon) &
        (df["date"].dt.date >= date_range[0]) &
        (df["date"].dt.date <= date_range[1])
    ].copy()

    st.title("EcoWatch SA: Regional Environmental Intelligence")
    st.markdown(
        "Welcome to the operational dashboard for tracking historical climate telemetry, "
        "meteorological trends, and environmental risks across Southern Africa."
    )
    st.markdown("---")

    if navigation == "Overview & Trends":
        st.subheader("Regional Climate Trends")
        if not filtered_df.empty:
            avg_temp = filtered_df["temperature_2m"].mean()
            total_precip = filtered_df["precipitation"].sum()
            avg_solar = filtered_df["solar_radiation"].mean()
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Avg Temperature", f"{avg_temp:.2f} °C")
            col2.metric("Total Precipitation", f"{total_precip:.2f} mm")
            col3.metric("Avg Solar Radiation", f"{avg_solar:.2f} MJ/m²")

            st.markdown("---")
            
            st.subheader("Trends")
            
            filtered_df["temp_rolling"] = filtered_df["temperature_2m"].rolling(window=30).mean()
            
            chart_data_temp = filtered_df.set_index("date")[["temperature_2m", "temp_rolling"]]
            st.markdown("**Temperature Trend (°C) with 30-Day Moving Average**")
            st.line_chart(chart_data_temp)
            
            chart_data_precip = filtered_df.set_index("date")["precipitation"]
            st.markdown("**Daily Precipitation Distribution (mm)**")
            st.bar_chart(chart_data_precip)

        else:
            st.warning("No data available for the selected filters.")
            
        st.markdown("---")
        st.write(f"Displaying analytics for coordinate grid **({selected_lat}, {selected_lon})** across **{len(filtered_df)}** records.")

    elif navigation == "Raw Data Inspector":
        st.subheader("Raw Data Inspector")
        st.write(f"Filtered dataset preview ({len(filtered_df)} matching rows):")
        st.dataframe(filtered_df, use_container_width=True)

        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Data as CSV",
            data=csv_data,
            file_name="ecowatch_filtered_export.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()