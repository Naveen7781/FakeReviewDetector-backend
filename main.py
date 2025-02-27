import gdown
import pickle
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Root endpoint to check if API is running
@app.get("/")
def home():
    return {"message": "Fake Review Detection API is running!"}

# Google Drive file ID extracted from your link
file_id = "1Aqp-DREKFolOs-qQ9KvTk-VaBm7ldI9t"
model_path = "fake_review_model.pkl"

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

# Define request schema
class ReviewRequest(BaseModel):
    review_text: str

@app.post("/predict")
def predict_review(request: ReviewRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded.")
    
    # Placeholder for prediction logic
    prediction = model.predict([request.review_text])[0]
    return {"prediction": "Fake" if prediction == 1 else "Real"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
