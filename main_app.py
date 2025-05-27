import streamlit as st
from analyzer import analyze_image
from utils import estimate_roi

st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")
st.title("☀️ AI-Powered Rooftop Solar Analysis Tool")

uploaded_file = st.file_uploader("Upload a rooftop satellite image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Rooftop Image", use_column_width=True)
    st.write("🔍 Analyzing rooftop...")

    result = analyze_image(uploaded_file)

    st.subheader("📐 Rooftop Analysis")
    st.write(f"Usable Rooftop Area: **{result['usable_area_m2']} m²**")
    st.write(f"Detected Obstructions: **{result['obstructions']}**")
    st.write(f"Estimated Panel Count: **{result['panel_count']}**")

    st.subheader("⚡ Solar Potential")
    st.write(f"Annual Generation: **{result['annual_generation_kwh']} kWh**")

    st.subheader("📊 ROI Estimation")
    roi = estimate_roi(result['annual_generation_kwh'], result['panel_count'])
    st.write(f"Estimated Cost: ₹{roi['cost']:,}")
    st.write(f"Estimated Annual Savings: ₹{roi['savings']:,}")
    st.write(f"Payback Period: {roi['payback_years']} years")

