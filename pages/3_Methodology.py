import streamlit as st
from PIL import Image  # Import the Image module from the PIL library

# Combined Welcome and About Us page
st.title("Methodology")

# Load and display the local image from the "images" folder
image = Image.open('images/methodology.png')  # Ensure the image is in the correct directory
st.image(image, use_column_width=True)
