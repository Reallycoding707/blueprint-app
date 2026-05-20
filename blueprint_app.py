import streamlit as st
import requests

st.set_page_config(page_title="Blueprint Creator", layout="centered")

st.title("🧠 Mechanical Blueprint Creator (No AI)")

idea = st.text_input("Enter your design idea")

if idea:

    url = "https://your-api-url.onrender.com/blueprint"

    response = requests.get(url, params={"idea": idea})

    if response.status_code == 200:
        data = response.json()

        st.subheader("📌 Design Overview")
        st.write(data["design_overview"])

        st.subheader("🧱 Materials")
        for m in data["materials"]:
            st.write("- " + m)

        st.subheader("⚙️ Considerations")
        for c in data["considerations"]:
            st.write("- " + c)

        st.subheader("🧩 CAD Steps")
        for i, step in enumerate(data["cad_steps"], 1):
            st.write(f"{i}. {step}")

    else:
        st.error("API not reachable")
