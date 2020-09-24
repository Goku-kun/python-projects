"""
https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=3324b11e-7046-4303-b345-6dbeda7e5c76
"""
import json
import requests

word = input("Enter a word: ")
url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=3324b11e-7046-4303-b345-6dbeda7e5c76"
respone = requests.get(url).content

var_dict = json.loads(respone)

for key,value in enumerate(var_dict):
      print(key,value)
