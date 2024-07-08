#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Read URL from command-line argument

    try:
        response = requests.get(url)

        # Raise an exception for 4xx and 5xx errors
        response.raise_for_status()

        # If no exception was raised, print the body of the response
        print(response.text)

    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
