import streamlit as st
import numpy as np
import pickle
import os

# Load the model using a relative path

model_path = r"C:\Users\anees\Data Analysis\Machine Learing\ML jupyter problems\lr.pkl"

image_path = "ino_img.jpeg"
st.image(image_path)

# Title and image
st.title("HOUSE PRICE PREDICTION")

# Input fields
SquareFeet = st.number_input("Enter Area of house in square feet", min_value=600, max_value=5000, step=50)
Bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, max_value=5, step=1)
Bathrooms = st.number_input("Enter the number of bathrooms", min_value=0, max_value=5, step=1)
Neighborhood = st.radio("Select type of neighbourhood", ['Rural', 'Urban', 'Suburb'])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3
YearBuilt = st.number_input("Enter year of Construction of property", min_value=1900, max_value=2030, step=1)

# Prediction
if st.button("PREDICT PRICE"):
    try:
        price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
        st.write("The price for the flat with given details is Rs.", price[0])
    except Exception as e:
        st.write("An error occurred:", e)
