from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET')
PERSONAL_KEY = os.getenv('PERSONAL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')


if SECRET_KEY is None:
    raise Exception('Secret key was not found!')


if PERSONAL_KEY is None:
    raise Exception('Secret key was not found!')

if USER is None:
    raise Exception('Secret key was not found!')

if PASSWORD is None:
    raise Exception('Secret key was not found!')

