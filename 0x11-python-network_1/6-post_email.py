#!/usr/bin/python3

"""
To accomplish the task of sending a POST request with an email parameter to a
specified URL and displaying the response body using Python's
requests library, follow the script below:
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Read URL from command-line argument
    email = sys.argv[2]  # Read email from command-line argument

    # Send POST request with email as parameter
    payload = {'email': email}
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)
