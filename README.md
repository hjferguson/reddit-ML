# reddit-ML
<h1>Brief Description</h1>
A webapp that uses machine learning to predict what subreddit a user-provided title belongs in.
This project includes a feature to generate your own training data using the Reddit API. 
Average F1 score of 80%

<h1>Set up:</h1>
🟢Developed on Win11 using bash terminal

🟢In root directory create a .env file and fill in your secrets using this format:

<br>SECRET = "reddit-api-secret"
<br>PERSONAL = "reddit-api-personal-key"
<br>
<br>#reddit credentials
<br>USER = "reddit-user-name"
<br>PASS = "reddit-password"

🟢In root directory run: pip install -r requirements.txt

🟢In setup_scripts: 'subreddits.txt' will be the the subreddits the model will get trained on. These are specifically popular subreddits,
with titles that have some form of continuity. Subreddits with more randomized topics, or media centered communities won't be as successful with training.
There will be a 'classification_report.txt' generated after training is done which you can use for tuning if necessary.

🟢Navigate to the backend directory and run:

python manage.py runserver

🟢Open another bash terminal and navigate to the frontend/react_app directory and run:

npm start


<h1>Design thoughts</h1>
When I first began this project, I had never used Pandas (dataframes), the reddit API, or anything related to machine learning / artificial intelligence. 
So this project has been a really good starting point. I initially was going to start with ML on a professionally created dataset so that I could just focus on implementing ML, but I ultimately decided to make my own dataset because I want the skills to go out and gather data, process the data, and then train on the data. I also had this project working as a console app, then refactored everything to work as a full-stack application. I'm a full-stack student so I figured I should have full-stack projects for my portfolio 😅 Needless to say, I should have started the project with the boilerplate React and Django frameworks in place, but I did learn a lot on the refactoring process so it was totally worth it!

<br>Harlan
