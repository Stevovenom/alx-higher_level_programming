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
    response = requests.get(url)

    # Check if X-Request-Id header exists in response
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(request_id)
    else:
        print("No X-Request-Id found in the headers")
