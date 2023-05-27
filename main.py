from dotenv import load_dotenv #used for grabbing credentials from the .env file
import os
from auth0_token import show_sub_stats

load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')
SUB = "mildlyinteresting"

show_sub_stats(SECRET_KEY, PERSONAL_KEY, USER, PASSWORD,SUB)