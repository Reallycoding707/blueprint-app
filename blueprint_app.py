import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Blueprint Creator", layout="centered")

st.title("🧠 AI Mechanical Design Blueprint Creator")
st.write("Turn your idea into a professional engineering design plan using AI")

# API key input (simple version for now)
api_key = st.text_input("Enter your OpenAI API Key", type="password")

idea = st.text_input("Describe your design idea (e.g., phone stand, bracket, clamp)")

if idea and api_key:

    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are a mechanical engineering assistant.

    Create a structured CAD design blueprint for this idea:
    {idea}

    Include:
    1. Design overview
    2. Material suggestions
    3. Structural considerations
    4. Suggested dimensions (rough)
    5. Step-by-step CAD instructions (SolidWorks style)
    Keep it clear and practical for an engineering student.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.subheader("📌 AI Generated Blueprint")
    st.write(response.choices[0].message.content)
