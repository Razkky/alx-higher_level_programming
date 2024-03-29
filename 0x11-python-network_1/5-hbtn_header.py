#!/usr/bin/python3
""" A python scripts that take a url sends request and displays
    the value of the variable X-Request-Id"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
