#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument,
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
