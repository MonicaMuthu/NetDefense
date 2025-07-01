import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# # Load dataset
# df = pd.read_csv("data.csv")

# # Convert text data into numerical format (TF-IDF)
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(df["request"])
# y = df["label"]

# # Train ML model
# model = RandomForestClassifier()
# model.fit(X, y)

# # Save the model & vectorizer
# joblib.dump(model, "waf_model.pkl")
# joblib.dump(vectorizer, "vectorizer.pkl")

# print("Model trained and saved successfully!")


import joblib

# Load dataset
df = pd.read_csv('data.csv')

# Split data
X = df['request']
y = df['label']

# Vectorize
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, 'waf_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved!")
