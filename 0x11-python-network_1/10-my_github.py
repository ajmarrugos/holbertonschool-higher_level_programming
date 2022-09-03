#!/usr/bin/python3
""" Takes your GitHub credentials to display your id """
if __name__ == "__main__":

    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    from requests.auth import HTTPBasicAuth
    git_account = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=git_account)
    print(req.json().get("id"))
