import streamlit as st
from PIL import Image
import torch

# Load your custom YOLOv5 model
# Assuming your model is saved as 'best.pt' in the same directory as this script
model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/best.pt')

# Title of the app
st.title("Endometriosis  Detection")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    # Perform object detection
    st.write("Analyzing...")
    results = model(image)

    # Display the results
    st.image(results.render()[0], caption='Detected Objects.', use_column_width=True)