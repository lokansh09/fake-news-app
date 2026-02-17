import joblib

try:
    # Load the best model and vectorizer
    model = joblib.load('best_fake_news_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    print("✅ Files loaded successfully!")

    # Sample text to test the model
    sample_text = ["This is a sample news text to check the model's prediction."]
    
    # Transform the text using the loaded vectorizer
    transformed_text = vectorizer.transform(sample_text)
    print("✅ TF-IDF transformation successful!")

    # Make the prediction
    prediction = model.predict(transformed_text)
    print("✅ Prediction:", prediction)

except Exception as e:
    print("❌ Error:", e)
