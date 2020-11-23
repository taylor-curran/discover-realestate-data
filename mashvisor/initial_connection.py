import os
from dotenv import load_dotenv
import requests
import json

# Load API Keys
load_dotenv()
X_RAPID_API_KEY = os.getenv("X_RAPID_API_KEY")
X_RAPID_API_HOST_MASHVISOR = os.getenv("X_RAPID_API_HOST_MASHVISOR")


headers = {
    'x-rapidapi-key': X_RAPID_API_KEY,
    'x-rapidapi-host': X_RAPID_API_HOST_MASHVISOR
    }

url_beginning = "https://mashvisor-api.p.rapidapi.com"
url_ending = "/airbnb-property/active-listings"

url = url_beginning + url_ending

querystring = {
    "state": "TN",
    "zip_code": "37738"
               }


response = requests.request("GET", url, headers=headers, params=querystring)

json_response = response.json()

import pandas as pd

df = pd.DataFrame(json_response['content']['properties'])

print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())