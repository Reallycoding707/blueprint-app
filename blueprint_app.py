import streamlit as st
import requests

st.set_page_config(page_title="Blueprint Creator", layout="centered")

st.title("🧠 Mechanical Blueprint Creator")

idea = st.text_input("Enter your design idea")

API_URL = "https://your-api.onrender.com/blueprint"  # replace later

if idea:
    response = requests.get(API_URL, params={"idea": idea})

    if response.status_code == 200:
        data = response.json()

        st.subheader("Design Overview")
        st.write(data["design_overview"])

        st.subheader("Materials")
        st.write(data["materials"])

        st.subheader("Considerations")
        st.write(data["considerations"])

        st.subheader("CAD Steps")
        for i, step in enumerate(data["cad_steps"], 1):
            st.write(f"{i}. {step}")

    else:
        st.error("API not reachable")
