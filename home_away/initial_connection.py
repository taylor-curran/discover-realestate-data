
# TODO: Not sure about the authentication?
# https://www.homeaway.com/platform/documentation

import requests

url = "https://ws.homeaway.com/public"

response = requests.request("POST", url, headers=headers, params=querystring)

json = response.json()