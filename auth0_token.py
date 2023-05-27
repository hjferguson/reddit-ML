#in order to access the API, we need to get an Auth0 token that expires every 2 hours. 
import requests

def show_sub_stats(secret_key, personal_key,user,password,subreddit):
    

        auth = requests.auth.HTTPBasicAuth(personal_key,secret_key)

        #pass login method as a dictionary
        data = {'grant_type' : 'password',
                'username' : user,
                'password' : password
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

        res = requests.get("https://oauth.reddit.com/r/" + subreddit + "/hot", headers=headers)

        for post in res.json()['data']['children']:
                print(post['data']['title'])