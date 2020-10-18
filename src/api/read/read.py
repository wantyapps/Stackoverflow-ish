import os

def read(): # Only when the file is accepted as open.
    i = 0
    if os.path.isfile("data.json"):
        with open("data.json", "r") as f:
            for line in f:
                i += 1
                print("{} | {}".format(i, line).replace("\n", ""))
    else:
        print("File not found. Create one using the API with \"python3 api.py\" and make sure the server is running.")

class reader:
    def __init__(self):
        self.reader = "<READER OBJECT CREATED BY MODULE READ>"
    def get(self):
        print("GETDATA")
        print(self.reader)


if __name__ == "__main__":
    print("This is not the main script. Please run the main script: \033[91m../api.py\033[0m")
    exit(1)
