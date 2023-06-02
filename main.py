from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from auth0_token import show_sub_stats
import pandas as pd
import time
from cleanFunction import redditCleaner

df = pd.DataFrame(columns=['subreddit','title']) #store the name of the subreddit and it's title

#pulls credentials from .env file. Required for working with reddit API
load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')


#loop through subreddits.txt and insert results into the df
with open("subreddits.txt","r") as f: #add as many subreddit as you like, just maintain the format because there is no error handling :D
    for x in f:
        sub = x.strip('\r\n')
        df_sub = show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD, sub)
        df = pd.concat([df, df_sub], ignore_index=True)

        #pause for 1 sec per request to stay within Reddit's 60 req/min rule
        time.sleep(1) #IMPORTANT

print("Saving df to csv...")
print("WARNING! If you already have a reddit_title_data.csv file in your directory, it will be overwritten!")
time.sleep(2) 
df.to_csv('reddit_title_data.csv', index=False)

X = redditCleaner(df) #returns cleaned and vectorized array

