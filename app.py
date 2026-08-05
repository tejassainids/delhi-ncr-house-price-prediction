import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
Predict house prices in Delhi NCR using a **Random Forest Regressor** trained on the Delhi NCR Housing Dataset.
""")

st.divider()

# -----------------------------
# Model Performance
# -----------------------------
st.subheader("📊 Model Performance")

m1, m2, m3 = st.columns(3)

m1.metric("MAE", "₹1.05 Cr")
m2.metric("RMSE", "₹2.30 Cr")
m3.metric("R² Score", "0.69")

st.divider()

# -----------------------------
# Inputs
# -----------------------------
st.subheader("🏡 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sq ft)",
        min_value=100,
        max_value=10000,
        value=1600,
        help="Total carpet area in square feet."
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=10,
        value=3,
        help="Number of bedrooms."
    )

with col2:
    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=2,
        help="Number of parking spaces available."
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("💵 Predict Price", use_container_width=True):

    new_house = pd.DataFrame({
        "bhk": [bhk],
        "area_sqft": [area],
        "parking": [parking]
    })

    prediction = model.predict(new_house)[0]

    st.success(
        f"💰 **Estimated Price:** ₹ {prediction/1e7:.2f} Crore"
    )

    st.info(
        f"""
### 📝 Prediction Summary

- **Area:** {area:,} sq ft
- **BHK:** {bhk}
- **Parking:** {parking}
"""
    )

st.divider()

# -----------------------------
# Feature Importance
# -----------------------------
st.subheader("📈 Feature Importance")

importance = pd.DataFrame({
    "Feature": [
        "Area",
        "BHK",
        "Parking"
    ],
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

importance = importance.set_index("Feature")

st.bar_chart(importance)

st.caption(
    "Higher importance means the model relied more on that feature while making predictions."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("📌 Project Information")

    st.markdown("""
**Model Used**
- Random Forest Regressor

**Dataset**
- Delhi NCR Housing Dataset

**Features**
- Area (sq ft)
- BHK
- Parking

**Author**
- Tejas Saini
""")


# Footer
# -----------------------------
st.divider()

st.caption("© 2026 Tejas Saini • Data Science Portfolio")