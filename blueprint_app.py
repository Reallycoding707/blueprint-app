import streamlit as st

st.set_page_config(
    page_title="Blueprint Creator",
    page_icon="🧠",
    layout="centered"
)

# Header
st.markdown("<h1 style='text-align: center;'>🧠 Mechanical Design Blueprint Creator</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>Turn your idea into a structured engineering design plan</p>", unsafe_allow_html=True)

st.divider()

# Input
idea = st.text_input("💡 Describe your design idea (e.g., phone stand, bracket, clamp)")

# If user enters idea
if idea:

    st.subheader("📌 Project Overview")
    st.info(f"Design Idea: {idea}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚙️ Key Considerations")
        st.write("- Load requirements")
        st.write("- Material selection")
        st.write("- Stability & safety factors")
        st.write("- Manufacturing method")

    with col2:
        st.subheader("📏 Suggested Structure")
        st.write("- Base support")
        st.write("- Load distribution elements")
        st.write("- Connection/joint points")
        st.write("- Reinforcement areas")

    st.divider()

    st.subheader("🧩 CAD Modeling Steps (SOLIDWORKS)")
    steps = [
        "Create base sketch",
        "Extrude main structure",
        "Add support features",
        "Refine edges (fillets/chamfers)",
        "Assemble components if needed"
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"{i}. {step}")

    st.divider()

    st.success("✔ Recommended Next Step: Start by sketching the base and defining key dimensions in CAD.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>Built by a Mechanical Engineering student • SOLIDWORKS + Python</p>", unsafe_allow_html=True)
