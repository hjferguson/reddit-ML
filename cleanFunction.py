import pandas as pd
import nltk

try:
    nltk.data.find('corpora/wordnet')  # requires this dictionary to work
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/stopwords')  # requires this dictionary to work
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

def redditCleaner(data, vectorizer=None):
    if isinstance(data, pd.DataFrame):
        df = data
        is_df = True
    elif isinstance(data, str):
        df = pd.DataFrame([data], columns=['title'])
        is_df = False
    else:
        raise TypeError("Invalid input type. Expected pandas.DataFrame or str.")

    df['title'] = df['title'].str.lower()
    df['title'] = df['title'].str.replace('[^\w\s\?]', '')
    df['title'] = df['title'].str.replace('\d+', '')

    stop = stopwords.words('english')
    df['title'] = df['title'].apply(lambda x: ' '.join(word for word in x.split() if word not in stop))

    lemmatizer = WordNetLemmatizer()
    df['title'] = df['title'].apply(lambda x: ' '.join(lemmatizer.lemmatize(word) for word in x.split()))

    if is_df:  # If the input is a DataFrame, we need to fit the vectorizer
        vectorizer = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7)
        X = vectorizer.fit_transform(df['title'])
        return X, vectorizer
    else:  # If the input is a string, we only transform it using the already-fit vectorizer
        X = vectorizer.transform(df['title'])
        return X
