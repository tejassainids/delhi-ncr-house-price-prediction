import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Delhi NCR House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/random_forest_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🏠 Delhi NCR House Price Prediction")

st.markdown("""
Predict house prices in Delhi NCR using a **Forest Tree Regressor** trained on the Delhi NCR Housing Dataset 2025.
""")

st.divider()

# -----------------------------
# Inputs
# -----------------------------
st.subheader("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sq ft)",
        min_value=100,
        max_value=10000,
        value=1600
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=10,
        value=3
    )

with col2:
    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=2
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    new_house = pd.DataFrame({
        "bhk": [bhk],
        "area_sqft": [area],
        "parking": [parking]
    })

    prediction = model.predict(new_house)[0]

    st.success(f"🏡 Estimated Price: ₹ {prediction/1e7:.2f} Crore")

    st.info(
        f"""
        **Summary**

        • Area : **{area} sq ft**

        • BHK : **{bhk}**

        • Parking : **{parking}**
        """
    )

st.divider()

st.caption(
    "Developed by Tejas Saini © 2026"
)