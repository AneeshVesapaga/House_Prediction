import streamlit as st
import pickle
import os

# Define the paths
model_path = r"C:\Users\anees\Data Analysis\Machine Learing\ML jupyter problems\lr.pkl"
image_path = "inno_image.jpeg"

# Debug: Print the current working directory and paths
st.write("Current working directory:", os.getcwd())
st.write("Model path:", model_path)
st.write("Image path:", image_path)

# Load the model
try:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.write(f"Model file not found at {model_path}")
    model = None

# Display the image
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.write(f"Image file not found at {image_path}")

# Input fields
SquareFeet = st.number_input("Enter the size of house", min_value=60, max_value=2400, step=50)
Bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, max_value=4, step=1)
Bathrooms = st.number_input("Enter the number of bathrooms", min_value=0, max_value=6, step=1)
Neighborhood = st.radio("Enter the neighborhood", ["Rural", "Urban", "Suburb"])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3
YearBuilt = st.number_input("Enter the year of construction", min_value=2000, max_value=2050, step=1)

# Prediction button
if model and st.button("PREDICT PRICE"):
    try:
        price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
        st.write("The price for the flat with given details is Rs.", price[0])
    except Exception as e:
        st.write("An error occurred:", e)

