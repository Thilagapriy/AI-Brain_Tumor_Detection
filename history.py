import streamlit as st
from database import get_history

st.title("📊 Patient History")

history = get_history()

if history:
    for row in history:
        patient, date, result = row
        st.markdown(f"**Patient:** {patient} | **Date:** {date} | **Result:** {result.upper()}")
        st.divider()
else:
    st.info("No history saved yet.")
