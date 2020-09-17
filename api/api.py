import requests
import json
import os

def read(): # only when the file is accepted as open.
    i = 0
    with open("data.json", "r") as f:
        for line in f:
            i += 1
        with open("data.json", "r") as f:
            print("{} | {}".format(i, line))

try:    
    response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": "pass123" } )
except requests.exceptions.ConnectionError:
    response = False
    print("Connection Error.")
if response:    
    data = json.loads(response.text)
    if os.path.isfile("data.json"):
        with open("data.json", "a") as f:
            f.write("\n" + str(data).replace("'", '"'))
    else:
        with open("data.json", "a") as f:
            f.write(str(data).replace("'", '"'))
