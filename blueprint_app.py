import streamlit as st

st.set_page_config(page_title="AI Blueprint Creator", layout="centered")

st.title("🧠 AI Mechanical Design Blueprint Creator")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
idea = st.text_input("Describe your design idea")

if api_key and idea:
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        prompt = f"""
        You are a mechanical engineering assistant.

        Create a structured CAD blueprint for this idea:
        {idea}

        Include:
        - Design overview
        - Materials
        - Structural considerations
        - Rough dimensions
        - CAD steps
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Blueprint Output")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error("OpenAI failed to load or run.")
        st.write(e)
