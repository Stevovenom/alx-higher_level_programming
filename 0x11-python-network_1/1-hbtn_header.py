#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""

if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
