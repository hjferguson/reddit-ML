import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('reddit_title_data.csv')

def redditCleaner(df):
    '''
    This function takes a dataframe. Two columns, subreddit and title. It then cleans the data and returns
    a vectorized array of the data for training. 
    '''

    #popular method of cleaning is to set everything to lowercase, because case sensitivity can effect training
    df['title'] = df['title'].str.lower()

    #recommended to remove special characters. I want to keep '?' tho because some subreddits are for asking questions
    df['title'] = df['title'].str.replace('[^\w\s\?]','')

    #for text analysis, recommended to remove numbers
    df['title'] = df['title'].str.replace('\d+', '')

    #remove stop words (and,the,a,an,etc). Don't carry information so they aren't useful
    stop = stopwords.words('english')
    df['title'] = df['title'].apply(lambda x: ' '.join(word for word in x.split() if word not in stop))

    #stemming/lemmatization. reduce words to their root. example running/runner reduced to run
    stemmer = PorterStemmer()
    df['title'] = df['title'].apply(lambda x: ' '.join(stemmer.stem(word) for word in x.split()))

    #Vectorization. Sounds cool. Turns text into numbers. Some models work off of a 2d array of numbers. So vectorizing is a MUST.
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7)
    X = vectorizer.fit_transform(df['title']).toarray()
    return X
