#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":

    # URL from teh command-line
    url = sys.argv[1]
    url = sys.argv[1]  # Read URL from command-line argument
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
