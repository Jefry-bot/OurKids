from dotenv import load_dotenv
from os.path import dirname, join

def load_env(place):
    dotenv_path = join(place, '../../.env')
    load_dotenv(dotenv_path) 