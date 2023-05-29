from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from auth0_token import show_sub_stats

load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')
SUB = "Showerthoughts"

#see if I can loop through the subreddits
f = open("subreddits.txt","r")
for x in f:
    if x == "crazyideas":
        break
    sub = x.rstrip()

with open("subreddits.txt","r") as f:
    for x in f:
        sub = x.strip('\r\n')
        if sub == "changemyview": #for testing
            break
        print("=======")
        print(f"Sub is: {sub}")
        print("=======")
        #sub = x.strip('\r\n')
        show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD,sub)
