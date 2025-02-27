import gdown
import pickle
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os
import time
time.sleep(10)  # Wait 10 seconds before starting

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # ✅ FastAPI instance must come before adding middleware

# ✅ CORS Middleware (fixing order issue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Google Drive file ID
file_id = "1Aqp-DREKFolOs-qQ9KvTk-VaBm7ldI9t"
model_path = "fake_review_model.pkl"
vectorizer_path = "vectorizer.pkl"

# Download the model if it doesn't exist
if not Path(model_path).exists():
    print("Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", model_path, quiet=False)
    print("Download complete.")

# Load the trained model
try:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Load the vectorizer
try:
    with open(vectorizer_path, "rb") as vec_file:
        vectorizer = pickle.load(vec_file)
    print("Vectorizer loaded successfully.")
except Exception as e:
    print(f"Error loading vectorizer: {e}")
    vectorizer = None

# Define request schema
class ReviewRequest(BaseModel):
    review_text: str

@app.get("/")
def home():
    return {"message": "Fake Review Detection API is running!"}

@app.post("/detect")  # ✅ Changed endpoint from /predict to /detect
def detect_review(request: ReviewRequest):
    if model is None or vectorizer is None:
        raise HTTPException(status_code=500, detail="Model or vectorizer is not loaded.")

    # Convert text to numerical features
    transformed_text = vectorizer.transform([request.review_text])
    
    # Make prediction
    prediction = model.predict(transformed_text)[0]
    
    return {"result": "Fake" if prediction == 1 else "Real"}  # ✅ Ensure response format matches frontend

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render provides PORT env variable
    uvicorn.run(app, host="0.0.0.0", port=port)

