from flask import Flask, request, render_template, jsonify, redirect, url_for, session
import joblib
import sqlite3

app = Flask(__name__)
app.secret_key = "a2ccf0f1cbd74481a22e7aa4fbe7f5c6"  # Needed for session management

# Load model
model = joblib.load('model/fake_news.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

# Home redirects to login/signup page
@app.route('/')
def home():
    return render_template('fake2.html')

# Login/Signup route
@app.route('/login_signup', methods=['POST'])
def login_signup():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')  # Only used during signup

    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()

    # Check if email exists in DB
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user:  # Login flow
        if user[3] == password:  # password column
            session['username'] = user[1]  # username column
            return redirect(url_for('predict_page'))
        else:
            return render_template('fake2.html', login_error="Invalid password")
    else:  # Signup flow
        if username:  # Only signup has username
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            conn.commit()
            # Redirect to login page after signup
            return redirect(url_for('home', signup_success="Registration successful! Please login."))
        else:
            return render_template('fake2.html', login_error="User does not exist. Please signup first.")

# Serve predict page
@app.route('/predict-page', methods=['GET'])
def predict_page():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('predictN.html', username=session['username'])

# Prediction API
@app.route('/predictN', methods=['POST'])
def predict_news():
    data = request.get_json()
    input_text = data.get('text', '')

    if input_text:
        prediction = model.predict([input_text])[0]
        confidence = model.predict_proba([input_text]).max() * 100
        return jsonify({'prediction': prediction, 'confidence': round(confidence, 2)})
    else:
        return jsonify({'error': 'No input text received'}), 400

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
