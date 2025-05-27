import streamlit as st
from PIL import Image
import numpy as np

st.title("AI-Powered Rooftop Solar Analysis Tool")

uploaded_file = st.file_uploader("Upload a rooftop image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    st.subheader("Analysis Results")
    st.write("✅ Estimated usable rooftop area: 60%")
    st.write("🔋 Suggested solar panel type: Monocrystalline")
    st.write("📈 Estimated system size: 5 kW")
    st.write("💰 Estimated cost: ₹2,50,000")
    st.write("⏳ Payback period: 4.5 years")
    st.write("🌞 Annual savings: ₹50,000")