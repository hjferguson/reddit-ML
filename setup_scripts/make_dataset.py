#Written by Harlan Ferguson. Wanted to dip my toes into ML
from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from reddit_api import show_sub_stats
import pandas as pd
import time




#pulls credentials from .env file. Required for working with reddit API
def make_data():

    load_dotenv()
    SECRET_KEY = os.getenv('SECRET')
    PERSONAL_KEY = os.getenv('PERSONAL')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASS')

    #set reddit sort methods
    SORT = ("hot","controversial","new","rising","top")


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

            df.drop_duplicates(subset=['subreddit','title'], keep='first', inplace=True)
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



