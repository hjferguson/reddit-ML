#Written by Harlan Ferguson. Wanted to dip my toes into ML
from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from auth0_token import show_sub_stats
import pandas as pd
import time
from cleanFunction import redditCleaner
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

#pulls credentials from .env file. Required for working with reddit API
load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')

#set reddit sort methods
SORT = ('hot','controversial','new','rising','top')

# Check if the CSV file already exists
if os.path.exists("reddit_title_data.csv"):
    print("It looks like you already have a csv file.")
    print("Do you want to overwrite it and collect new data, or continue with the existing file?")
    print("1: Overwrite")
    print("2: Continue")
    uInput = input()
    
    while uInput != "1" and uInput != "2":
        print("Bruh. Type 1 or 2...")
        uInput = input()

    # User chose to overwrite the existing file
    if uInput == "1":
        print("Collecting new data. This may take a few minutes...")
        
        df = pd.DataFrame(columns=['subreddit','title']) #store the name of the subreddit and it's title

        with open("subreddits.txt","r") as f: #add as many subreddit as you like, just maintain the format because there is no error handling :D
            for x in f:
                for y in SORT:

                    sub = x.strip('\r\n')
                    df_sub = show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD, sub, y)
                    df = pd.concat([df, df_sub], ignore_index=True)

                    #pause for 1 sec per request to stay within Reddit's 60 req/min rule
                    time.sleep(1) #IMPORTANT

        df.drop_duplicates(subset=['post_id'], keep='first', inplace=True)
        df.to_csv('reddit_title_data.csv', index=False)
        
    # User chose to continue with the existing file
    elif uInput == "2":
        print("Continuing with existing file.")
        
        df = pd.read_csv('reddit_title_data.csv')

# If the CSV file doesn't exist, collect new data
else:
    print("Collecting new data. This may take a few minutes...")
    
    df = pd.DataFrame(columns=['subreddit','title']) #store the name of the subreddit and it's title

    with open("subreddits.txt","r") as f: #add as many subreddit as you like, just maintain the format because there is no error handling :D
        for x in f:
            for y in SORT:

                sub = x.strip('\r\n')
                df_sub = show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD, sub, y)
                df = pd.concat([df, df_sub], ignore_index=True)

                #pause for 1 sec per request to stay within Reddit's 60 req/min rule
                time.sleep(1) #IMPORTANT

    df.drop_duplicates(subset=['subreddit','title'], keep='first', inplace=True)
    df.to_csv('reddit_title_data.csv', index=False)

# Once you have your DataFrame, whether it's from a new collection or an existing file, you can clean it
X = redditCleaner(df) #returns cleaned and vectorized array
y = df['subreddit']

#split the data into training and tests
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()

#training time!
model.fit(X_train, y_train)

#predict the labels for test data
y_pred = model.predict(X_test)

#evaluation
report = classification_report(y_test, y_pred)

#save the report to a file
with open('classification_report.txt', 'w') as f:
    f.write(report)