import streamlit as st
import pickle
import os

# Load the model using the absolute path
model_path = r"C:\Users\anees\Data Analysis\Machine Learing\ML jupyter problems\lr.pkl"
model = pickle.load(open(model_path, "rb"))

# Display the image
image_path = "inno_image.jpeg"
st.image(image_path)

# Input fields
SquareFeet = st.number_input("Enter the size of house", min_value=60, max_value=2400, step=50)	
Bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, max_value=4, step=1)	
Bathrooms = st.number_input("Enter the number of bathrooms", min_value=0, max_value=6, step=1)	
Neighborhood = st.radio("Enter the neighborhood", ["Rural", "Urban", "Suburb"])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3
YearBuilt = st.number_input("Enter the year of construction", min_value=2000, max_value=2050, step=1)

# Prediction button
if st.button("PREDICT PRICE"):
    try:
        price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
        st.write("The price for the flat with given details is Rs.", price[0])
    except Exception as e:
        st.write("An error occurred:", e)
