import requests
try:    
    response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": "pass123" } )
except requests.exceptions.ConnectionError:
    response = False
    print("Connection Error.")
if response:    
    print(response.text)
