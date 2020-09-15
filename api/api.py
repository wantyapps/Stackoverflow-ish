import requests
import json

try:    
    response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": "pass123" } )
except requests.exceptions.ConnectionError:
    response = False
    print("Connection Error.")
if response:    
    data = json.loads(response.text)
    print(data)
    if data["password"] == "oao":
        print("oao")
    else:
        print("nope.")
