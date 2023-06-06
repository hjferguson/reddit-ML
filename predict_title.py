import pickle
from cleanFunction import redditCleaner

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_subreddit(title):
    #clean user input
    clean_title = redditCleaner(title)
    