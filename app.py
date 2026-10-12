import streamlit as st

st.set_page_config(
    page_title="EcoWatch SA | Environmental Intelligence Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Sidebar
    st.sidebar.title("🌍 EcoWatch SA")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navigation & Filters")
    
    navigation = st.sidebar.radio("Go to:", ["Overview & Trends", "Raw Data Inspector"])
    
    st.sidebar.markdown("---")
    st.sidebar.info("EcoWatch SA v1.0 • Built for regional climate tracking & environmental monitoring.")

    st.title("🌱 EcoWatch SA: Regional Environmental Intelligence")
    st.markdown(
        "Welcome to the operational dashboard for tracking historical climate telemetry, "
        "meteorological trends, and environmental risks across Southern Africa."
    )
    st.markdown("---")

    if navigation == "Overview & Trends":
        st.subheader("Regional Climate Trends")
        st.write("*(Interactive charts and KPIs will load here in upcoming steps)*")
        
    elif navigation == "Raw Data Inspector":
        st.subheader("🔍 Raw Data Inspector")
        st.write("*(Database table viewer will load here in upcoming steps)*")

if __name__ == "__main__":
    main()