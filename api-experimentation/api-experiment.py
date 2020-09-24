import requests
import json

api_var = requests.get("https://api.wheretheiss.at/v1/satellites/25544").content

var_dict = json.loads(api_var)

for key,value in enumerate(var_dict):
      print(key,value)

