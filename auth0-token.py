#in order to access the API, we need to get an Auth0 token that expires every 2 hours. 
import requests
from dotenv import load_dotenv
import os

load_dotenv()



SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')

def show_sub_stats(secret_key, personal key,user,password,subreddit):
    

        auth = requests.auth.HTTPBasicAuth(PERSONAL_KEY,SECRET_KEY)

        #pass login method as a dictionary
        data = {'grant_type' : 'password',
                'username' : USER,
                'password' : PASSWORD
                }

        #set up required header information
        headers = {'User-Agent' : 'community_vibe - script that predicts community engagement'}

        #send the request to auth0

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        #convert response to JSON and take the token
        TOKEN = res.json()['access_token']

        #add auth to our headers
        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        requests.get('https://oauth.reddit.com/api/v1/me, headers=headers')

        res = requests.get("https://oauth.reddit.com/r/2007scape/hot", headers=headers)

        for post in res.json()['data']['children']:
                print(post['data']['title'])