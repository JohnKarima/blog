from app import app
import requests
from .models import quotes

Quotes = quotes.Quotes

api_key = app.config['QUOTES_API_KEY']
base_url = app.config["QUOTES_API_BASE_URL"]

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quote_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return get_quote_response
