import streamlit as st
import pytesseract
from PIL import Image
import io

st.title("📄 Scan Hospital Report")

option = st.radio("Choose input method", ["Upload Report Image", "Use Camera"])

if option == "Upload Report Image":
    uploaded = st.file_uploader("Upload report (image/PDF page)", type=['jpg', 'png', 'jpeg'])
    img_bytes = uploaded.getvalue() if uploaded else None
else:
    img_bytes = st.camera_input("Take photo of report")

if img_bytes:
    img = Image.open(io.BytesIO(img_bytes))
    st.image(img, caption="Report Image")
    
    if st.button("Extract & Analyze Text"):
        with st.spinner("Extracting text..."):
            text = pytesseract.image_to_string(img)
        
        st.text_area("Extracted Text", text, height=200)
        
        text_lower = text.lower()
        if any(word in text_lower for word in ['tumor', 'mass', 'glioma', 'meningioma']):
            st.warning("Report mentions possible tumor.")
            st.write("**Recommendation:** Immediate consultation with neurologist.")
        else:
            st.success("No tumor-related terms detected in text.")