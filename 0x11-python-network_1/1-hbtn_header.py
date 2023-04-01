#!/usr/bin/python3
""" sends requests to url and display vlaue of X-Request-Id"""
import urllib.request as ur
from sys import argv

if __name__ == "__main__":
    with ur.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
