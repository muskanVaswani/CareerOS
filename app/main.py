from fastapi import FastAPI
from app.orchestrator.orchestrator import Orchestrator


app = FastAPI(
    title="CareerOS",
    version="1.0.0",
    description="AI-powered multi-agent career mentor."
)

orchestrator = Orchestrator()


@app.get("/")
def home():
    return{
        "message": "Welcome to CareerOS"
    }
    
@app.get("/career")
def career(user_input: str):
    result = orchestrator.run(user_input)
    
    return result