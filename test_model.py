import joblib
import re

# Load the model and vectorizer
model_path = 'model/best_fake_news_model.pkl'
vectorizer_path = 'model/tfidf_vectorizer.pkl'

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_news(news_input):
    """
    Cleans, vectorizes, and predicts whether news is fake or real.
    """
    # Clean the input news text
    cleaned_input = re.sub(r'[^A-Za-z\s]', '', news_input.lower())
    
    # Vectorize the cleaned input using the trained vectorizer
    news_vectorized = vectorizer.transform([cleaned_input])
    
    # Make the prediction (0 = Fake, 1 = Real)
    prediction = model.predict(news_vectorized)[0]
    
    return "Real News" if prediction == 1 else "Fake News"

# Test with some input news
news_input = "Government announces new policy on climate change."
print(predict_news(news_input))  # This will print the result (Real or Fake)
