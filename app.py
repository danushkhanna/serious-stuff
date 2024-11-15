import streamlit as st
import pandas as pd
import plotly.express as px
import json
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(page_title="Orbit Predictor", page_icon="🛰️", layout="wide")

# Load Lottie animation
def load_lottie_animation(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_data = load_lottie_animation("assets/lottie.json")

# Sidebar
with st.sidebar:
    st.title("Orbit Predictor")
    st_lottie(lottie_data, height=200, key="lottie")
    st.markdown("---")
    st.header("Navigation")
    st.markdown("Use the sidebar to navigate through different modules.")

    st.markdown("### About")
    st.info(
        """
        This app allows you to visualize and predict satellite orbits using TLE data.
        For more information, visit [Your Project Website](https://your-project-link.com).
        """
    )

# Main layout
st.title("Orbit Predictor - Satellite Data Visualization")

# Sample TLE Data (replace with actual data as needed)
sample_data = {
    "OBJECT_NAME": ["STARLINK-1008", "STARLINK-1009", "STARLINK-1010", "STARLINK-1011", "STARLINK-1012"],
    "OBJECT_ID": ["2019-074B", "2019-074C", "2019-074D", "2019-074E", "2019-074F"],
    "EPOCH": ["2024-11-14T14:50:59", "2024-11-15T06:00:00", "2024-11-13T21:30:40", "2024-11-15T02:07:42", "2024-11-15T01:27:54"],
    "MEAN_MOTION": [15.06417543, 15.22839408, 15.06407753, 15.06417043, 15.06414096],
    "ECCENTRICITY": [0.0001594, 0.0001241, 0.0001563, 0.0001683, 0.0001441],
    "INCLINATION": [53.0523, 53.0538, 53.0537, 53.055, 53.0525]
}
df = pd.DataFrame(sample_data)

# Display TLE Data
st.subheader("TLE Data")
st.write("The following TLE data is used for satellite orbit visualization and prediction.")
st.dataframe(df)

# Input area for user to paste their TLE data (optional)
st.subheader("Upload or Paste TLE Data")
uploaded_file = st.file_uploader("Upload TLE data as CSV", type="csv")
if uploaded_file is not None:
    user_df = pd.read_csv(uploaded_file)
    st.write("Uploaded TLE Data:")
    st.dataframe(user_df)
else:
    st.write("Or manually enter TLE data in the input boxes above.")

# Visualization of MEAN_MOTION trends
st.subheader("Visualization: Mean Motion of Satellites")
fig = px.line(df, x="OBJECT_NAME", y="MEAN_MOTION", title="Mean Motion of Satellites", markers=True)
st.plotly_chart(fig)

# ECharts for interactive visualization
st.subheader("Interactive Visualization (ECharts)")

# Custom EChart configuration
options = {
    "title": {"text": "Eccentricity vs Inclination"},
    "tooltip": {"trigger": "axis"},
    "xAxis": {"type": "category", "data": df["OBJECT_NAME"].tolist()},
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "Eccentricity",
            "type": "line",
            "data": df["ECCENTRICITY"].tolist(),
            "smooth": True,
            "lineStyle": {"color": "red"},
        },
        {
            "name": "Inclination",
            "type": "line",
            "data": df["INCLINATION"].tolist(),
            "smooth": True,
            "lineStyle": {"color": "blue"},
        },
    ],
}

# Display EChart using streamlit-echarts library
from streamlit_echarts import st_echarts

st_echarts(options=options, height="400px")

# Footer with credits
st.markdown("---")
st.markdown(
    '<h6>Developed by [Your Name](https://twitter.com/yourprofile) using Streamlit and ECharts</h6>',
    unsafe_allow_html=True,
)
