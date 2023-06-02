from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from auth0_token import show_sub_stats
import pandas as pd
import time

df = pd.DataFrame(columns=['subreddit','title']) #store the title of the subreddit and it's title

load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')
SUB = "Showerthoughts"

#loop through subreddits.txt and insert results into the df
with open("subreddits.txt","r") as f:
    for x in f:
        sub = x.strip('\r\n')
        df_sub = show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD, sub)
        df = pd.concat([df, df_sub], ignore_index=True)

        #pause for 1 sec per request to stay within Reddit's 60 req/min rule
        time.sleep(1)

while True:
    print("Would you like to save the dataframe? Y/N")
    answer = input()
    if answer == "y" or answer == "Y":
        df.to_csv('reddit_title_data.csv', index=False)
        break
    if answer == "n" or answer == "N":
        print("ok bye")
        break
    else:
        print("Please input Y/N")

#so at this point, we have titles from 25 different sub reddits. Around 11.2k at the time of writing.
#now need to clean the text. I first noticed there are emojis. So that needs to get dealt with. 

