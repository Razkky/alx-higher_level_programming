#!/usr/bin/python3
""" Fetches the url https://alx-intranet.hbtn.io/status"""
import urllib.request as ur

if __name__ == "__main__":
    with ur.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")

