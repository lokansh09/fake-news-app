import joblib

try:
    # Try to load the model and vectorizer
    model = joblib.load('best_fake_news_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    print("✅ Files loaded successfully!")

    # Try using the vectorizer with a sample text
    sample_text = ["This is a sample news text."]
    transformed_text = vectorizer.transform(sample_text)
    print("✅ TF-IDF vectorizer works! Transformed text:", transformed_text.toarray())

    # Try predicting with the model
    prediction = model.predict(transformed_text)
    print("✅ Prediction:", prediction)

except Exception as e:
    print("❌ Error:", e)
