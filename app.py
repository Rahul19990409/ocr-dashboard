import streamlit as st
from PIL import Image
import cv2
import numpy as np
import easyocr

st.set_page_config(page_title="OCR Model Dashboard", layout="wide")

st.title("📄 OCR Model Dashboard")
st.write("Upload a document image to extract text")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=400)

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(gray)

    extracted_text = ""
    for r in results:
        extracted_text += r[1] + "\n"

    st.subheader("📝 Extracted Text")

    if extracted_text.strip():
        st.text_area("Result", extracted_text, height=300)
    else:
        st.warning("⚠️ No text detected. Try a clearer document image.")

    st.download_button(
        "Download Text",
        extracted_text,
        file_name="extracted_text.txt"
    )
