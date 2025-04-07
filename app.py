import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("linear_regression.pkl", "rb"))

# Define the top 10 features (you can update these)
top_features = [
    'trip_distance', 'fare_amount', 'extra', 'mta_tax', 'tip_amount',
    'tolls_amount', 'improvement_surcharge', 'congestion_surcharge',
    'trip_duration', 'passenger_count'
]

# App Title
st.title("🚖 NYC Green Taxi Fare Estimator")
st.markdown("Enter trip details below to estimate the total fare.")

# Input form
input_data = {}
for feature in top_features:
    input_data[feature] = st.number_input(f"{feature.replace('_', ' ').title()}", min_value=0.0, step=0.1)

# Predict
if st.button("Predict Total Fare"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    st.success(f"💵 Estimated Total Fare: *${prediction:.2f}*")