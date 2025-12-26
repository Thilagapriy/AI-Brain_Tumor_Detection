import streamlit as st

st.set_page_config(page_title="Brain Tumor AI", layout="centered")

# Dark theme CSS
st.markdown("""
<style>
    .stApp {background-color: #000000; color: #ffffff;}
    h1, h2, h3 {color: #ffffff;}
    .stButton>button {background-color: #333333; color: white; border-radius: 8px; width: 100%; height: 60px; font-size: 18px; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("🧠 Brain Tumor Detection AI")
    st.markdown("### Educational & Research Tool")
    st.markdown("**Disclaimer:** This is for educational purposes only. Always consult a medical professional.")
    if st.button("Start Application"):
        st.session_state.started = True
        st.rerun()
else:
    st.title("Brain Tumor AI Assistant")

    # 4 Big Buttons for Navigation
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 Detect Tumor"):
            st.switch_page("detection.py")
        if st.button("📄 Scan Report"):
            st.switch_page("report.py")
    
    with col2:
        if st.button("📊 View History"):
            st.switch_page("history.py")
        if st.button("💬 Chatbot"):
            st.switch_page("chatbot.py")
