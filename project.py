import streamlit as st
import numpy as np
import pickle
import os

# Load the model using a relative path
model_path = os.path.join(os.path.dirname(__file__), "lr.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Error: Model file '{model_path}' not found.")
    st.stop()
except Exception as e:
    st.error("Error loading the model:")
    st.error(e)
    st.stop()

# Title and image
st.title("HOUSE PRICE PREDICTION")

# Specify the path to your image file
image_path = os.path.join(os.path.dirname(__file__), "ino_img.jpeg")

# Display the image using st.image()
try:
    st.image(image_path, caption='Inno Image')  # You can add a caption for the image
except FileNotFoundError:
    st.error(f"Error: Image file '{image_path}' not found.")
    st.stop()

# Optionally, you can add some text or description
st.write("Here is the image 'ino_img.jpeg'")

# Input fields
SquareFeet = st.number_input("Enter Area of house in square feet", min_value=600, max_value=5000, step=50)
Bedrooms = st.number

