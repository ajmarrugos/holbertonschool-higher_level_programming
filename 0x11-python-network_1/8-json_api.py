#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = req.json()
        if len(json_dict.keys()) > 0:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
