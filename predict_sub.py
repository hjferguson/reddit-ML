import pickle
from cleanFunction import redditCleaner




def predict_subreddit(title):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('vectorizer.pkl' , 'rb') as f:
        vectorizer = pickle.load(f)

    #clean user input
    clean_title = redditCleaner(title, vectorizer)

    prediction = model.predict(clean_title)

    return prediction
