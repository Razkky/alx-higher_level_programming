#!/usr/bin/python3
"""Takes a github cridentials and uses the github api to display the id"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    req = requests.get(url)
    if req.status_code == 200:
        req = req.json()
        for commit in req[:10]:
            print(commit.get('sha'), end=": ")
            print(commit.get('commit')['author']['name'])
    else:
        print("None")
