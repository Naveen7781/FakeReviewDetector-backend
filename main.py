from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security (e.g., "http://localhost:3000")
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define request model
class ReviewRequest(BaseModel):
    link: str

@app.get("/")
def home():
    return {"message": "Fake review detection API is running"}

@app.post("/detect")
def detect_review(request: ReviewRequest):
    # Placeholder logic for detection
    result = "Fake" if "example" in request.link else "Real"
    return {"result": result}
