import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

st.set_page_config(page_title="OCR Text Extractor", layout="wide")

st.title("📄 OCR Model Dashboard")
st.write("Upload an image or scanned document to extract text")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=400)

    # Convert PIL image to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Preprocessing for OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # OCR
    text = pytesseract.image_to_string(thresh, lang="eng")

    st.subheader("📝 Extracted Text")

    if text.strip():
        st.text_area("Result", text, height=300)
    else:
        st.warning("⚠️ No text detected. Try a clearer image.")

    st.download_button(
        label="Download Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
