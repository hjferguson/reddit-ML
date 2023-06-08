import pickle
import os
from .clean_function import redditCleaner

def predict_subreddit(title):

    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    vector_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    with open(vector_path , 'rb') as f:
        vectorizer = pickle.load(f)

    #clean user input
    clean_title = redditCleaner(title, vectorizer)

    prediction = model.predict(clean_title)

    return str(prediction[0])
