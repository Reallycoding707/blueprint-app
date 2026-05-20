from fastapi import FastAPI
import os

app = FastAPI()

# Optional AI import (safe fallback if no key)
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    AI_ENABLED = True
except:
    AI_ENABLED = False


@app.get("/")
def home():
    return {"status": "AI Blueprint API running", "ai": AI_ENABLED}


@app.get("/blueprint")
def blueprint(idea: str):

    # -------------------------
    # IF AI IS AVAILABLE
    # -------------------------
    if AI_ENABLED:
        prompt = f"""
        You are a mechanical engineer.

        Create a CAD blueprint plan for: {idea}

        Return:
        - Design overview
        - Materials
        - Structural considerations
        - CAD steps
        Keep it concise and practical.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "idea": idea,
            "ai_output": response.choices[0].message.content
        }

    # -------------------------
    # FALLBACK (NO AI)
    # -------------------------
    return {
        "idea": idea,
        "design_overview": f"Blueprint for {idea}",
        "materials": ["ABS plastic", "Aluminum", "Steel"],
        "considerations": [
            "Load distribution",
            "Safety factor",
            "Manufacturing method"
        ],
        "cad_steps": [
            "Sketch base geometry",
            "Extrude main shape",
            "Add supports",
            "Refine edges",
            "Final check"
        ]
    }
