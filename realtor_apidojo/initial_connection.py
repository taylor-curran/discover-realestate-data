import os
from dotenv import load_dotenv
import requests
import json

# Load API Keys
load_dotenv()
X_RAPID_API_KEY=os.getenv("X_RAPID_API_KEY")
X_RAPID_API_HOST_DOJO=os.getenv("X_RAPID_API_HOST_DOJO")

headers = {
    'x-rapidapi-key': X_RAPID_API_KEY,
    'x-rapidapi-host': X_RAPID_API_HOST_DOJO
    }

url = "https://realtor.p.rapidapi.com/mortgage/calculate"

querystring = {"hoi":"56.0",
               "tax_rate":"1.2485549449920654",
               "downpayment":"44980",
               "price":"224900",
               "term":"30.0",
               "rate":"3.827"}


response = requests.request("GET", url, headers=headers, params=querystring)

json_response = response.json()

import pandas as pd

row = pd.Series(json_response['mortgage'])

print("Shape:", row.shape)
print("Columns:", row.index)
print(row)