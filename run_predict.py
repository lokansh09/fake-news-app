# run_predict.py

import joblib
import re

# Load the model and vectorizer
model = joblib.load('model.pkl/best_fake_news_model.pkl')
vectorizer = joblib.load('model.pkl/tfidf_vectorizer.pkl')

# Clean input
def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text.lower())
    return text

# Predict function
def predict_news(news_input):
    cleaned = clean_text(news_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)
    return "Real News ✅" if prediction[0] == 1 else "Fake News ❌"

# CLI input
if __name__ == "__main__":
    print("📰 Enter your news article text (press Enter to submit):")
    user_input = input("> ")
    result = predict_news(user_input)
    print("\nPrediction:", result)
