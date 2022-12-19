#!/usr/bin/python3
""" Script that fetches from a url using urllib package"""

import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as respo:
        cont = respo.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode('utf-8')))
