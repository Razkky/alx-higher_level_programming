#!/usr/bin/python3
"""Takes a github cridentials and uses the github api to display the id"""
import requests
from sys import argv

if __name__ == "__main__":
    paswd = argv[2]
    username = argv[1]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(username, paswd))
    if req.status_code == 200:
        req = req.json()
        print(req.get('id'))
    else:
        print("None")
