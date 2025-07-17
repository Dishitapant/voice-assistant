import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
data = {
    'command': [
        "open youtube", "play music", "what's the weather",
        "search google", "tell me a joke", "open facebook"
    ],
    'intent': [
        "open_youtube", "play_music", "weather",
        "search_google", "joke", "open_facebook"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['command'])
model = MultinomialNB()
model.fit(X, df['intent'])

def predict_intent(user_input):
    X_test = vectorizer.transform([user_input])
    intent = model.predict(X_test)[0]
    return intent