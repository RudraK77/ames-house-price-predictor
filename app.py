from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

model_path = Path(__file__).parent / "house_price_model.joblib"
model = joblib.load(model_path)

st.title("House Price Prediction")
st.caption("Educational estimator using historical Ames, Iowa housing data.")

area = st.number_input("Living area (square feet)", min_value=1, value=1500)
bedrooms = st.number_input("Bedrooms above ground", min_value=0, value=3)
year = st.number_input("Year built", min_value=1800, max_value=2010, value=2005)
quality = st.slider("Overall material and finish quality", 1, 10, 7)

if st.button("Predict price"):
    house = pd.DataFrame({
        "GrLivArea": [area],
        "BedroomAbvGr": [bedrooms],
        "YearBuilt": [year],
        "OverallQual": [quality]
    })

    price = model.predict(house)[0]

    st.metric("Estimated sale price", f"${price:,.0f}")
    st.caption("Test MAE: about $23,233. Individual errors can be larger.")

