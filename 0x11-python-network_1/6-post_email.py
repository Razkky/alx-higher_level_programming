#!/usr/bin/python3
""" sends a post request to url with email as parameter using
    requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    req = requests.post(url, value)
    print(req.text)
