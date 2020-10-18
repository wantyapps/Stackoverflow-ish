import requests
import json
import os
import sys
from read import read

readerfn = read.reader()
readerfn.get()

if len(sys.argv) == 3:
    if sys.argv[1] == "--debug" or sys.argv[1] == "-d":
        try:
            response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": sys.argv[2].replace("\n", "") } )
        except requests.exceptions.ConnectionError:
            response = False
            print("[\033[91m!\033[0m] [API] Connection error")
        if response:
            print("[\033[92m*\033[0m] Response: {}".format(response.text).replace("\n", ""))
    elif sys.argv[1] == "--rdebug" or sys.argv[1] == "-rd":
        try:
            response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": sys.argv[2].replace("\n", "") } )
        except requests.exceptions.ConnectionError:
            response = False
            print("[\033[91m!\033[0m] [API] Connection error")
        if response:
            print("[\033[92m*\033[0m] Response: {}".format(response.text).replace("\n", ""))
            readatain = input("Read JSON Data from database? [y/n]: ")
            if readatain == "y":
                print("[\033[92m*\033[0m] ACCEPTED")
                read.read()
            elif readatain == "\n":
                print("[\033[92m*\033[0m] ACCEPTED")
            else:
                print("[\033[92m*\033[0m] ACCEPTED")
elif len(sys.argv) == 2:
    if sys.argv[1] == "--list" or sys.argv[1] == "-l":
        read.read()
else:

    try:    
        response = requests.get("http://localhost:5000/api", headers = { "username": "wantyapps", "password": "pass123" } )
    except requests.exceptions.ConnectionError:
        response = False
        print("[API] Connection Error.")
    if response:
        data = json.loads(response.text)
        print(str(data).replace("'", '"'))
        if os.path.isfile("data.json"):
            with open("data.json", "a") as f:
                f.write("\n" + str(data).replace("'", '"'))
        else:
            with open("data.json", "a") as f:
                f.write(str(data).replace("'", '"'))

