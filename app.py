import streamlit as st
import pickle
import numpy as np
# Load model
model = pickle.load(open("model.pkl", "rb"))
st.title("🚖 Uber Fare Prediction App")
st.write("Enter trip details below:")
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6)
hour = st.slider("Hour of Day", 0, 23)
day = st.slider("Day of Month", 1, 31)
month = st.slider("Month", 1, 12)
if st.button("Predict Fare"):
    # Input validation
    if (pickup_latitude == 0 and pickup_longitude == 0 and
        dropoff_latitude == 0 and dropoff_longitude == 0):
        st.error("Please enter valid location values.")
    else:
        # Calculate distance
        distance = np.sqrt(
            (dropoff_longitude - pickup_longitude)**2 +
            (dropoff_latitude - pickup_latitude)**2
        )
        # Extra validation
        if distance == 0:
            st.warning("Pickup and drop locations cannot be the same.")
        else:
            # Create feature array (9 features)
            features = np.array([[pickup_longitude, pickup_latitude,
                                  dropoff_longitude, dropoff_latitude,
                                  passenger_count, hour, day, month,
                                  distance]])
            # Prediction
            prediction = model.predict(features)
            # Output
            st.success(f"Estimated Fare: ₹ {prediction[0]:.2f}")
