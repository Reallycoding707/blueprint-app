from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/blueprint")
def blueprint(idea: str):

    return {
        "idea": idea,
        "design_overview": f"Blueprint for {idea}",
        "materials": [
            "ABS plastic",
            "Aluminum",
            "Steel"
        ],
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
