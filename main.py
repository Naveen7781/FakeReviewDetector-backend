from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scrape_amazon_reviews
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# ✅ Check if model and vectorizer exist before loading
if not os.path.exists("fake_review_model.pkl") or not os.path.exists("vectorizer.pkl"):
    raise FileNotFoundError("Model or vectorizer file is missing!")

with open("fake_review_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# ✅ Define Request Model
class ReviewRequest(BaseModel):
    url: str

# ✅ Root Route (to check if API is running)
@app.get("/")
def home():
    return {"message": "Fake Review Detector API is running!"}

# ✅ Prediction Endpoint
@app.post("/predict")
def predict_fake_reviews(data: ReviewRequest):
    reviews = scrape_amazon_reviews(data.url)

    if not reviews:
        return {"error": "No reviews found"}

    try:
        review_vectors = vectorizer.transform(reviews)
        predictions = model.predict(review_vectors)
        results = [{"review": rev, "prediction": "Fake" if pred == 1 else "Real"} for rev, pred in zip(reviews, predictions)]
        return {"results": results}
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}
