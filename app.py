import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
st.title("🚖 Uber Fare Prediction App")
st.write("Enter trip details:")

pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")

dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")

passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6)

hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)

def haversine(lon1, lat1, lon2, lat2):
    R = 6371
    dlon = np.radians(lon2 - lon1)
    dlat = np.radians(lat2 - lat1)
    a = np.sin(dlat/2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c
if st.button("Predict Fare"):

    # Validation
    if not (-90 <= pickup_latitude <= 90 and -90 <= dropoff_latitude <= 90):
        st.error("Latitude must be between -90 and 90")

    elif not (-180 <= pickup_longitude <= 180 and -180 <= dropoff_longitude <= 180):
        st.error("Longitude must be between -180 and 180")

    else:
        # Calculate distance
        distance = haversine(
            pickup_longitude, pickup_latitude,
            dropoff_longitude, dropoff_latitude
        )

        st.write(f"Distance: {distance:.2f} km")

        if distance == 0:
            st.warning("Pickup and drop locations cannot be the same.")
        else:
            # ======================
            # EXACT FEATURE ORDER (IMPORTANT)
            # ======================
            features = np.array([[pickup_longitude, pickup_latitude,
                                  dropoff_longitude, dropoff_latitude,
                                  passenger_count, distance,
                                  hour, day, month]])

            # Debug check
            st.write("Model expects:", model.n_features_in_)

            # Prediction
            prediction = model.predict(features)

            st.success(f"Estimated Fare: ₹ {prediction[0]:.2f}")