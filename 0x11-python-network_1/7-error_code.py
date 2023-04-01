#!/usr/bin/python3
""" sends a request to a url and display body of response
    and error if encountered"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code > 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
