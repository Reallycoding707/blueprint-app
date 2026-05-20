import streamlit as st
import requests

st.set_page_config(page_title="Blueprint AI", layout="wide")

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center;'>🧠 Blueprint AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>Generate mechanical design blueprints instantly</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns([2, 1])

with col1:
    idea = st.text_input("Enter your design idea", placeholder="e.g. phone stand, bracket, clamp")

with col2:
    st.write("")
    st.write("")
    generate = st.button("⚡ Generate Blueprint")

API_URL = "https://blueprint-app-1-3hcj.onrender.com/blueprint"

# ---------------- OUTPUT SECTION ----------------
if generate and idea:

    with st.spinner("Generating blueprint..."):
        response = requests.get(API_URL, params={"idea": idea})
        data = response.json()

    st.divider()

    # ---------------- CARD STYLE OUTPUT ----------------
    st.markdown("## 📌 Result")

    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:10px;
        background-color:#0e1117;
        border:1px solid #333;
    ">
        <h3>Design Idea</h3>
        <p>{data.get('idea', idea)}</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ---------------- TWO COLUMN LAYOUT ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧱 Materials")
        for m in data.get("materials", []):
            st.write(f"• {m}")

        st.markdown("### ⚙️ Considerations")
        for c in data.get("considerations", []):
            st.write(f"• {c}")

    with col2:
        st.markdown("### 🧩 CAD Steps")
        for i, step in enumerate(data.get("cad_steps", []), 1):
            st.write(f"{i}. {step}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;font-size:12px;'>Built with Streamlit • Mechanical Engineering Tool</p>",
    unsafe_allow_html=True
)
