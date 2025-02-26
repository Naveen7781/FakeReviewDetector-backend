import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data_path = "data/fake reviews dataset.csv"
df = pd.read_csv(data_path)

# Rename columns
df.rename(columns={"text_": "text"}, inplace=True)

# Drop rows with missing values
df = df.dropna(subset=["text", "label"])

# Map 'CG' to 1 (Fake) and 'OR' to 0 (Real)
label_mapping = {"CG": 1, "OR": 0}
df["label"] = df["label"].map(label_mapping)

# Ensure there are no invalid labels left
df = df[df["label"].isin([0, 1])]

# Split data
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vec, y_train)

# Save model and vectorizer
with open("fake_review_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("Model and vectorizer saved successfully!")
