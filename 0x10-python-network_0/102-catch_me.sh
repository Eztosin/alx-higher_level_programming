#!/bin/bash
# a bash script that sends a request to the server to get the response "You got me!"
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" -L -H "Content-Type: application/json"
