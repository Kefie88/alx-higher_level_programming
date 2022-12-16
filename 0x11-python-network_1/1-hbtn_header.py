#!/usr/bin/python3
""" Sends request to URL provided as command and display the
    value of the X-Request-Id found in the header of the response
"""
from sys import argv
import urllib.request as req

if __name__ == "__main__":
    url = arg[1]

    with req.urlopen(url) as respo:
        print(dict(respo.headers).get("X-Request-Id"))
