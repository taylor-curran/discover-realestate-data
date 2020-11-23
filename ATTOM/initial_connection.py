import os
from dotenv import load_dotenv
import requests
import json
from xml.etree import ElementTree

# Load API Keys
load_dotenv()

ATTOM_API_KEY = os.getenv('ATTOM_API_KEY')

url = "http://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detail?"

headers = {
    'accept': "application/json",
    'apikey': ATTOM_API_KEY
}

params = {
    'address1': '4529 Winona Court' ,
    'address2': 'Denver, CO'
}

response = requests.request("GET", url, headers=headers, params=params)

print(response.json())
