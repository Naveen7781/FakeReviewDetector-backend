from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Root route to check if API is running
@app.get("/")
def home():
    return {"message": "Fake review detection API is running"}

# Define request model
class ReviewRequest(BaseModel):
    link: str

# Fake review detection logic (dummy for now)
@app.post("/detect")
def detect_fake_review(request: ReviewRequest):
    if "example" in request.link:
        return {"result": "Fake"}
    else:
        return {"result": "Real"}
