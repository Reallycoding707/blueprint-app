from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Blueprint API running"}

@app.get("/blueprint")
def blueprint(idea: str):

    return {
        "idea": idea,
        "design_overview": f"Design plan for {idea}",
        "materials": [
            "ABS plastic",
            "Aluminum",
            "Steel (if high load)"
        ],
        "considerations": [
            "Load distribution",
            "Stability",
            "Manufacturing method",
            "Safety factor"
        ],
        "cad_steps": [
            "Sketch base geometry",
            "Extrude main body",
            "Add support features",
            "Refine edges (fillets)",
            "Final assembly check"
        ]
    }