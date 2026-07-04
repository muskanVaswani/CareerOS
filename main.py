from fastapi import FastAPI


app = FastAPI(
    title="CareerOS",
    version="1.0.0",
    description="AI-powered multi-agent career mentor."
)

@app.get("/")
def home():
    return{
        "message": "Welcome to CareerOS"
    }