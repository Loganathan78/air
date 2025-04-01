import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Air Quality Prediction System')

# Simulate a trained model for prediction
def predict_aqi(pm25, pm10, no2, co, o3, temp, humidity, wind_speed):
    # Simplified formula to calculate AQI
    aqi = (pm25 * 0.4 + pm10 * 0.3 + no2 * 0.1 + co * 5 + o3 * 0.2)
    return aqi

# Input fields for user to input data
pm25 = st.number_input('PM2.5 (µg/m³)', min_value=0.0)
pm10 = st.number_input('PM10 (µg/m³)', min_value=0.0)
no2 = st.number_input('NO2 (ppb)', min_value=0.0)
co = st.number_input('CO (mg/m³)', min_value=0.0)
o3 = st.number_input('O3 (ppb)', min_value=0.0)
temp = st.number_input('Temperature (°C)', min_value=-50.0)
humidity = st.number_input('Humidity (%)', min_value=0.0)
wind_speed = st.number_input('Wind Speed (m/s)', min_value=0.0)

# Button to predict AQI
if st.button('Predict AQI'):
    aqi = predict_aqi(pm25, pm10, no2, co, o3, temp, humidity, wind_speed)
    st.write(f"Predicted AQI: {aqi:.2f}")
    
    # Category based on AQI
    if aqi <= 50:
        category = "Good 😊"
    elif aqi <= 100:
        category = "Moderate 😐"
    elif aqi <= 150:
        category = "Unhealthy for Sensitive Groups 😷"
    elif aqi <= 200:
        category = "Unhealthy 🤢"
    elif aqi <= 300:
        category = "Very Unhealthy ☠️"
    else:
        category = "Hazardous 💀"
    
    st.write(f"AQI Category: {category}")

# Display the authorship message at the bottom of the page with larger text and bold names
st.markdown("""
    <div style="position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #f1f1f1;">
        <p style="font-size: 24px; font-weight: bold; color: black;">
            This website was created by <span style="font-weight: bold; font-size: 26px;">S. Loganathan</span> and <span style="font-weight: bold; font-size: 26px;">S. Akhash</span>
        </p>
    </div>
""", unsafe_allow_html=True)
