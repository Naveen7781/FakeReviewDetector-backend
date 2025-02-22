from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Request model
class ReviewRequest(BaseModel):
    link: str

# Fake review detection function (placeholder logic)
def detect_fake_review(link: str) -> str:
    # Simulate a fake review detection process (Replace this with ML model)
    return "Fake Review" if random.choice([True, False]) else "Real Review"

@app.post("/api/detect")
async def detect_review(review: ReviewRequest):
    result = detect_fake_review(review.link)
    return {"link": review.link, "result": result}
