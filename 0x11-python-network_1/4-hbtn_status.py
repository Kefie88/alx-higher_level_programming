#!/usr/bin/python3
"""Uses requests module to fetch url status"""

import requests

if __name__ == "__main__":
    respo = requests.get('https://intranet.hbtn.io/status')
    print("Body response: \n\t- type: {}\n\t- content: {}"
            .format(type(respo.text), respo.text))
