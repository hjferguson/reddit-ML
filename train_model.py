from cleanFunction import redditCleaner
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle
import pandas as pd
#model tuning
from sklearn.model_selection import GridSearchCV
import numpy as np

def training_montage():
    # Once you have your DataFrame, whether it's from a new collection or an existing file, you can clean it
    df = pd.read_csv("reddit_title_data.csv")

    X, vectorizer = redditCleaner(df, None) #returns cleaned and vectorized array
    y = df['subreddit']

    #split the data into training and tests
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = MultinomialNB()

    #Without tuning, I am getting 65% accuracy on f1 score. Adding tuning and may also remove low performing labels from the df
    #scikit-learn has automatic tuning that will test different versions of the model and compare performances to each other... (my understanding of it)
    alpha_range = list(np.arange(0.1, 1.1, 0.1))
    param_grid = dict(alpha=alpha_range)

    grid = GridSearchCV(model, param_grid, cv=10, scoring='accuracy')
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_

    #predict the labels for test data
    y_pred = best_model.predict(X_test)

    #evaluation
    report = classification_report(y_test, y_pred)

    #save the report to a file
    with open('classification_report.txt', 'w') as f:
        f.write(report)

    #save instance of model
    with open('model.pkl', 'wb') as f:
        pickle.dump(best_model, f)

    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
