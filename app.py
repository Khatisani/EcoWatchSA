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
    # Sidebar
    st.sidebar.title("🌍 EcoWatch SA")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navigation & Filters")
    
    navigation = st.sidebar.radio("Go to:", ["Overview & Trends", "Raw Data Inspector"])
    
    st.sidebar.markdown("---")
    st.sidebar.info("EcoWatch SA v1.0 • Built for regional climate tracking & environmental monitoring.")

    st.title("EcoWatch SA: Regional Environmental Intelligence")
    st.markdown(
        "Welcome to the operational dashboard for tracking historical climate telemetry, "
        "meteorological trends, and environmental risks across Southern Africa."
    )
    st.markdown("---")

    try:
        df = load_environmental_data()
    except Exception as e:
        st.error(f"Database connection error: {e}. Please ensure Phase 1 load script has been run.")
        return

    if navigation == "Overview & Trends":
        st.subheader("Regional Climate Trends")
        st.write(f"Successfully loaded **{len(df)}** historical records from the SQLite data warehouse.")
        
    elif navigation == "Raw Data Inspector":
        st.subheader("Raw Data Inspector")
        st.write(f"Dataset preview ({len(df)} total rows loaded into memory cache):")
        st.dataframe(df.head(10), use_container_width=True)

if __name__ == "__main__":
    main()