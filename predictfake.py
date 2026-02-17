import joblib
import re
import os

# Get the current directory where this file is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths to the model and vectorizer files inside 'model' folder
model_path = os.path.join(base_dir, 'model', 'fake_news.pkl')
vectorizer_path = os.path.join(base_dir, 'model', 'tfidf_vectorizer.pkl')

def predict_news(news_text, model, vectorizer):
    """
    Cleans, vectorizes, and predicts whether news is fake or real.
    """
    # Clean the input news text (remove non-alphabet characters)
    cleaned_input = re.sub(r'[^A-Za-z\s]', '', news_text.lower())

    # Vectorize the cleaned input using the trained vectorizer
    news_vectorized = vectorizer.transform([cleaned_input])

    # Predict whether the news is real (1) or fake (0)
    prediction = model.predict(news_vectorized)[0]

    return "Real News" if prediction == 1 else "Fake News"

# Test the function in stand-alone mode
if __name__ == "__main__":
    # Load the model and vectorizer
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    # Sample news text (pdata)
    sample = '''Fact check: Trump and Clinton at the 'commander-in-chief' forum	"Hillary Clinton and Donald Trump made some inaccurate claims during an NBC â€œcommander-in-chiefâ€ forum on military and veterans issues:

â€¢ Clinton wrongly claimed Trump supported the war in Iraq after it started, while Trump was wrong, once again, in saying he was against the war before it started.

â€¢Â Trump said that President Obama set a â€œcertain dateâ€ for withdrawing troops from Iraq, when that date was set before Obama was sworn in.

â€¢Â Trump said that Obamaâ€™s visits to China, Saudi Arabia and Cuba were â€œthe first time in the history, the storied history of Air Force Oneâ€ when â€œhigh officialsâ€ of a host country did not appear to greet the president. Not true.

â€¢Â Clinton said that Trump supports privatizing the Veterans Health Administration. Thatâ€™s false. Trump said he supports allowing veterans to seek care at either public or private hospitals.

â€¢Â Trump said Clinton made â€œa terrible mistake on Libyaâ€ when she was secretary of State. But, at the time, Trump also supported U.S. action that led to the removal of Moammar Gadhafi from power.
'''

    # Run prediction
    print("Prediction:", predict_news(sample, model, vectorizer))
