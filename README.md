# reddit-ML
<h1>Brief Description</h1>
Self-taught introduction to Machine Learning. I made a dataset using the Reddit api and collected thousands of post titles
with subreddits as their labels. After cleaning and vectorizing the data, I use scikit-learn's Bayes model to predict what subreddit the title 
belongs to. It doesn't have much real-world use, I was more interested in learning about Pandas, making my own dataset, and training it.

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

<h2>Design thoughts</h2>
I decided to save the created dataframe to csv and give an option to the user to overwrite the data or continue with it. I went with this approach because
creating the dataset takes time (as of writing 30+ minutes) so in order to test and tune the Bayes model, I wanted to skip having to make the data each time. Loading it into memory saves a boat load of testing time! I wanted to split the main functions into seperate files for more readability and then left
all of the scikit library stuff in the main. So I have the reddit api function in it's own place, the cleaning and vectorizing function in it's own place, 
and I also save and read from the working directory which allows for users to add their own subreddits if they choose to do so!

All in all, this has been a very fun and interesting project and I can't wait to keep exploring these seriously impressive libraries. 

Harlan
