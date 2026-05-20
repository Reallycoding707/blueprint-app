import streamlit as st

st.set_page_config(page_title="Blueprint Creator")

st.title("🧠 Mechanical Design Blueprint Creator")

st.write("Turn your idea into a structured engineering plan")

idea = st.text_input("Describe your design idea (e.g., phone stand, bracket, clamp)")

if idea:
    st.subheader("Blueprint Output")

    st.write("### 1. Design Overview")
    st.write(f"Project: {idea}")

    st.write("### 2. Key Considerations")
    st.write("- Load requirements")
    st.write("- Material selection")
    st.write("- Stability and safety")
    st.write("- Manufacturing method")

    st.write("### 3. CAD Steps")
    st.write("1. Sketch base")
    st.write("2. Extrude main shape")
    st.write("3. Add supports")
    st.write("4. Refine edges")
    st.write("5. Final assembly (if needed)")
