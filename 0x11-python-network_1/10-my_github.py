#!/usr/bin/python3
"""
Takes your Github credentials and uses the GitHub API
to dispaly your ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://ai.github.com/user'
    respo = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(respo.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
