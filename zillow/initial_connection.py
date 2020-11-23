# Directory API, Profile Summary API, Reviews API

import os
from dotenv import load_dotenv
import requests
import json

# Load API Keys
load_dotenv()
ZWSID = os.getenv("ZWSID")

headers = {
    'zws-id': ZWSID
    }

url = 'http://www.zillow.com/webservice/ProReviews.htm'

response = requests.request('GET', url=url, headers=headers)

# For more information
# https://www.zillow.com/howto/api/ReviewsAPI.htm
