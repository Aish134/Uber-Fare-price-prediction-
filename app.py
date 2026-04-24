import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
st.title("🚖 Uber Fare Prediction App")
st.write("Enter trip details:")
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6)

hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)

if st.button("Predict Fare"):
    features = np.array([[pickup_longitude, pickup_latitude,
                          dropoff_longitude, dropoff_latitude,
                          passenger_count, hour, day, month]])

    prediction = model.predict(features)

    st.success(f"Estimated Fare: ₹ {prediction[0]:.2f}")