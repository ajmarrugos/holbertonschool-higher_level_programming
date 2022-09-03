#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email """
if __name__ == "__main__":

    import requests
    import sys

    email = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=email)
    print(req.text)
