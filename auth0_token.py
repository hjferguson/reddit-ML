#in order to access the API, we need to get an Auth0 token that expires every 2 hours. 
import requests

def show_sub_stats(secret_key, personal_key,user,password,subreddit):
    

        auth = requests.auth.HTTPBasicAuth(personal_key,secret_key)

        data = {
        'grant_type' : 'password',
        'username' : user,
        'password' : password
        }

        headers = {'User-Agent' : 'predicts subreddit based off title of post'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        if res.status_code == 200:
                TOKEN = res.json()['access_token']
                headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

                res = requests.get("https://oauth.reddit.com/r/" + subreddit + "/hot", headers=headers)

                if res.status_code == 200:  # successful request
                        response_json = res.json()
                        if 'data' in response_json:
                                for post in response_json['data']['children']:
                                        print(post['data']['title'])
                        else:
                                print("The key 'data' is not in the response.")
                                print("Response:", response_json)
                else:
                        print("Failed to get data from Reddit API. Status code:", res.status_code)
        else:
                print("Failed to get token from Reddit API. Status code:", res.status_code)
