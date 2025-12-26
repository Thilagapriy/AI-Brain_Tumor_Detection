import streamlit as st
from inference import predict
from database import save_history
import os

st.title("🔍 Tumor Detection")

uploaded_file = st.file_uploader("Upload MRI Image (JPG/PNG)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded MRI", use_column_width=True)
    
    # Save temporarily
    temp_path = "temp_upload.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if st.button("Analyze Image"):
        with st.spinner("Analyzing..."):
            cls, form, treat, surv = predict(temp_path)
        
        st.success(f"**Detected Tumor Type: {cls.upper()}**")
        st.write(f"**How it forms:** {form}")
        st.write(f"**Suggested Treatment:** {treat}")
        st.write(f"**Estimated Survival:** {surv}")
        st.info("⚠️ This is AI prediction for educational use only. Consult a doctor.")
        
        patient = st.text_input("Patient Name (to save in history)")
        if st.button("Save Result to History") and patient:
            save_history(patient, cls)
            st.success("Saved!")