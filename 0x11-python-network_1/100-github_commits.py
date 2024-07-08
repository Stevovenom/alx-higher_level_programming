#!/usr/bin/python3
"""
challenge of listing 10 commits (from the most recent to oldest) of the
repository "rails" by the user "rails" using the GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} repository owner".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            commits = response.json()[:10]  # Limit to 10 most recent commits
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
