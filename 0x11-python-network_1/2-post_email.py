#!/usr/bin/python3
"""takes a url and email and sends a post request to the url passed"""
import urllib.request as ur
import urllib.parse as up
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    url = argv[1]
    data = up.urlencode(value)
    data = data.encode('utf-8')
    req = ur.Request(url, data)
    with ur.urlopen(req) as response:
        print(response.read().decode('utf-8'))
