# House-price-app-streamlit
import streamlit as st
import joblib
st.write("JOBLIB IMPORTED")
# Load the saved model
model = joblib.load('model.pkl')

# App title
st.title("🏠 House Price Predictor")

# Description
st.markdown("Enter property details below to estimate the house price:")

# User inputs
area = st.slider("Area (in square feet)", 500, 5000, step=100)
bedrooms = st.selectbox("Number of bedrooms", [1, 2, 3, 4, 5])

# Prediction
if st.button("Predict Price"):
    input_data = [[area, bedrooms]]
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ${prediction[0]:,.2f}")
