"""
https://www.tronalddump.io/random/quote
"""
import json
import requests

response = requests.get('https://www.tronalddump.io/random/quote').text

dictonary = json.loads(response)
print(dictonary)
print(dictonary['value'])