#!/usr/bin/python3
"""Sends a post request to url with letter as parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    value = {}
    if len(argv) == 2:
        value['q'] = argv[1]
    else:
        value['q'] = ""
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=value)
    try:
        js = req.json()
        if js:
            print(f"[{js.get('id')}] {js.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
