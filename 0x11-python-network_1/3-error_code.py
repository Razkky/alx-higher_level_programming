#!/usr/bin/python3
"""Takes a url and sends https requests and display body of content
    and handle error if it occurs, print error"""
import urllib.request as ur
from sys import argv
import urllib.error as error

if __name__ == "__main__":
    url = argv[1]
    try:
        with ur.urlopen(url) as data:
            print(data.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
