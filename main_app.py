import streamlit as st
from analyzer import analyze_image
from utils import estimate_roi

st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")
st.title("🌞 Solar Rooftop Potential Estimator")

uploaded_file = st.file_uploader("Upload a rooftop satellite image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Rooftop Image", use_column_width=True)

    st.write("Analyzing image...")
    result = analyze_image(uploaded_file)

    st.subheader("Rooftop Analysis")
    st.write(f"Estimated Usable Rooftop Area: {result['area_m2']} m²")
    st.write(f"Estimated Number of Panels: {result['panel_count']}")
    st.write(f"Obstructions Detected: {result['obstructions']}")

    st.subheader("Estimated Solar Potential")
    st.write(f"Annual Power Generation: {result['annual_generation_kwh']} kWh")

    st.subheader("ROI Estimate")
    roi_result = estimate_roi(result['annual_generation_kwh'], result['panel_count'])
    st.write(f"Estimated Installation Cost: ₹{roi_result['cost']:,}")
    st.write(f"Estimated Annual Savings: ₹{roi_result['savings']:,}")
    st.write(f"Payback Period: {roi_result['payback_years']} years")
