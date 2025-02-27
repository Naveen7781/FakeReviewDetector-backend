import gdown
import pickle
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

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

@app.post("/predict")
def predict_review(request: ReviewRequest):
    if model is None or vectorizer is None:
        raise HTTPException(status_code=500, detail="Model or vectorizer is not loaded.")

    # Convert text to numerical features
    transformed_text = vectorizer.transform([request.review_text])
    
    # Make prediction
    prediction = model.predict(transformed_text)[0]
    
    return {"prediction": "Fake" if prediction == 1 else "Real"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
