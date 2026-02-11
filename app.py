import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Set page config
st.set_page_config(page_title="OCR Text Extractor", layout="wide")

# Tesseract path (Windows users only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("📄 OCR Model Dashboard")
st.write("Upload an image or scanned document to extract text")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    st.subheader("📝 Extracted Text")
    st.text_area("Result", text, height=300)

    st.download_button(
        label="Download Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
