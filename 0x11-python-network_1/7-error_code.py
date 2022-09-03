#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response. """

if __name__ == "__main__":

    import sys
    import requests

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
