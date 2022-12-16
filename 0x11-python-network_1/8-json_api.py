#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000 """

import requests
from sys import argv

if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        respo = req.json()
        if respo == {}:
            print("No result")
        else:
            print("[{}] {}".format(respo.get("id"), respo.get("name")))
        except ValueError:
            print("Not a valid JSON")
