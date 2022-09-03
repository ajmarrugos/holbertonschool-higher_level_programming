#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the X-Request-Id """
if __name__ == "__main__":

    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(response.info().get('X-Request-Id'))
