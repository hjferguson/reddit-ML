# reddit-ML
<h1>Brief Description</h1>
A webapp that uses machine learning to predict what subreddit a user-provided title belongs in.
This project includes a feature to generate your own training data using the Reddit API. 
Average F1 score of 80%

<h1>Set up:</h1>
-In root directory create a .env file and fill in your secrets using this format:

SECRET = "reddit-api-secret"
PERSONAL = "reddit-api-personal-key"

#reddit credentials
USER = "reddit-user-name"
PASS = "reddit-password"

-In root directory run: pip install -r requirements.txt

-In setup_scripts 'subreddits.txt' will be the the subreddits the model will get trained on. These are specifically popular subreddits,
with titles that have some form of continuity. Subreddits with more randomized topics, or media centered communities won't be as successful with training
There will be a 'classification_report.txt' generated after training is done which you can use for tuning if necessary.

-Navigate to the backend directory and run:

python manage.py runserver

Open another bash terminal and navigate to the frontend/react_app directory

npm start


<h2>Design thoughts</h2>
When I first began this project, I had never used Pandas (dataframes), the reddit API, or anything related to machine learning / artificial intelligence. 
So this project has been a really good starting point. I think especially since I made my own dataset instead of using an exsisting dataset because it made
they tuning process more interesting. I have some Typescript / Django experience but this project also gave me the experience of fully implementing these frameworks from scratch. 

One challenge in particular was how I approached the project. I first made it a working console application and then made it full-stack after I had the console app fully functioning. In the inifficiencies I lost, I made up for in refactoring experience. I'm excited to try image recognition ML next... 