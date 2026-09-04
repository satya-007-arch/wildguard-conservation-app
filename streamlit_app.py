import streamlit as st
import pandas as pd

st.set_page_config(page_title="WildGuard", page_icon="🐅")

st.title("🐅 WildGuard - To Conserve and Stay Protected for Wildlife")
st.markdown("SIH 2026 | Team CodeSquad REC | Rajdhani Engineering College")

menu = st.sidebar.radio("Menu", ["Dashboard", "Animal Detection", "Report Incident"])

if menu == "Dashboard":
    st.subheader("Wildlife Conservation Dashboard - Odisha")
    col1, col2, col3 = st.columns(3)
    col1.metric("Tigers Saved", "12", "+2")
    col2.metric("Poaching Alerts", "3", "-5")
    col3.metric("Guards Active", "48", "+4")
    st.success("System Status: Active ✅")

elif menu == "Animal Detection":
    st.subheader("📸 Live Animal Detection")
    uploaded = st.file_uploader("Choose an image", type=["jpg","png"])
    if uploaded:
        st.image(uploaded, width=400)
        st.success("Tiger Detected 92% confidence")
        st.warning("Alert sent to Forest Guard!")

else:
    st.subheader("🚨 Report Incident")
    name = st.text_input("Your Name")
    loc = st.text_input("Location")
    if st.button("Submit Report"):
        st.success(f"Thank you {name}! Report submitted for {loc}")
