import requests
response = requests.get('http://localhost:5000/api')
if str(response) ==  "<Response [200]>":
    print("Server is up.")
    response = requests.get("http://localhost:5000/api", headers = {
        "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
        "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
)
    print(response.text)
else:
    print("bad")
