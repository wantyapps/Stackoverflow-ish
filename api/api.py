import requests
import json
import os
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == "--debug" or sys.argv[1] == "-d":
        #print("[API] Entering debug mode...")
        try:
            response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": sys.argv[2].replace("\n", "") } )
        except requests.exceptions.ConnectionError:
            response = False
            print("[API] Connection error")
        if response:
            print("[API] Response: {}".format(response.text).replace("\n", ""))
else:

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

# I want a colorprint here of the data...
