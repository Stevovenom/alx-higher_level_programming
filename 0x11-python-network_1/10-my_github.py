#!/usr/bin/python3
"""
 Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} username token".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {
        'Accept': 'application/json',
    }
    auth = (username, token)

    try:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        elif response.status_code == 401:
            print("None")
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
