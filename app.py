from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
CORS(app)  # IMPORTANT FIX

# dataset
data = {
    "label": ["spam","ham","spam","ham","spam","ham","spam","spam","ham","ham","ham"],
    "text": [
        "Win money now",
        "How are you",
        "Free lottery ticket",
        "Let's meet tomorrow",
        "Claim your prize now",
        "Are you coming to class",
        "You won lottery",
        "Free offer just for you",
        "hii",
        "hello",
        "hey"
    ]
}

df = pd.DataFrame(data)
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.json['message']
    msg_vector = vectorizer.transform([msg])
    prediction = model.predict(msg_vector)

    result = "Spam" if prediction[0] == 1 else "Not Spam"
    return jsonify({"result": result})

app.run(debug=True)