# reddit-ML
ML model that takes a reddit post title and guesses which subreddit it belongs to.
I decided to use Reddit because they have free API access so that I could learn how to make my own dataset. 
Chose a Pandas DataFrame because it works well with the scikit-learn library 

<h1>Set up:</h1>

🟢 Create a '.env' and add your secret and personal use script keys. Also store your reddit user and password
    The format should be this:

    SECRET = "your_secret"
    PERSONAL = "your_personal_script"

    USER = "your_reddit_username"
    PASS = "your_reddit_password"

🟢 In the correct file path, run: pip install -r requirements.txt
    This will load the correct libraries
    
🟢 I've provided a subreddits.txt file with 25 popular subreddits. Add/remove where you find necessary. Keeping in mind, subreddits that are heavily photo focused, or "joke" subreddits have a lower
accuracy for the model. For example r/funny is 0.05 accurate whereas r/IAmA is at 90%. 

🟢 Run the 'main.py' program

⛔⛔I recommend not touching any part of the code that uses the 'time' module. Reddit has specific rules with their API and if you make too many requests 
you may be blocked from using their API in the future. It is currently set to adhere to 60 requests per minute.⛔⛔
