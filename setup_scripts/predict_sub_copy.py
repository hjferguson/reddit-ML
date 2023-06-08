import pickle
from clean_function_copy import redditCleaner

def predict_subreddit(title):
    with open('./model_copy.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('./vectorizer_copy.pkl' , 'rb') as f:
        vectorizer = pickle.load(f)

    #clean user input
    clean_title = redditCleaner(title, vectorizer)

    prediction = model.predict(clean_title)

    return prediction
