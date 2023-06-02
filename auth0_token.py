#in order to access the API, we need to get an Auth0 token that expires every 2 hours. 
import requests
import pandas as pd
import time

def show_sub_stats(secret_key, personal_key,user,password,subreddit):
    
    df = pd.DataFrame(columns=['Subreddit', 'Title'])

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

        cursor = None
        for _ in range(20):  # make 20 requests, which will give up to 2000 posts
            url = "https://oauth.reddit.com/r/" + subreddit + "/hot" #top all time only gave 9200 line csv
            if cursor is not None:
                url += "?after=" + cursor
            res = requests.get(url, headers=headers)

            if res.status_code == 200:  # successful request
                response_json = res.json()
                if 'data' in response_json:
                    for post in response_json['data']['children']:
                        new_row = {'Subreddit' : subreddit, 'Title' : post['data']['title']}
                        df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
                    cursor = response_json['data']['after']  # get the cursor for the next page of results
                    if cursor is None:  # if there's no cursor, we've reached the end of the posts
                        break
                else:
                    print("The key 'data' is not in the response.")
                    print("Response:", response_json)
            else:
                print("Failed to get data from Reddit API. Status code:", res.status_code)
            time.sleep(1)  #IMPORTANT!! KEEP OR ACCOUNT CAN LOSE API ACCESS
    else:
        print("Failed to get token from Reddit API. Status code:", res.status_code)

    return df

