#!/bin/bash
# script to post data (url-encoded) to the server

curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
