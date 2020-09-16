import requests
import json
import os

try:    
    response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": "pass123" } )
except requests.exceptions.ConnectionError:
    response = False
    print("Connection Error.")
if response:    
    data = json.loads(response.text)
    if os.path.isfile("data.json"):
        with open("data.json", "a") as f:
            f.write("\n" + str(data))
    else:
        with open("data.json", "a") as f:
            f.write(str(data))
