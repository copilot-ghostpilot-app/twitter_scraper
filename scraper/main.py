#!/usr/bin/env python3

from os import getenv
from twitter_capture import TwitterCapture
from api import API

API_ENDPOINT = getenv('API_ENDPOINT', 'https://postman-echo.com/post')

def main():
    tweets = TwitterCapture().main()
    print(tweets)
    for tweet in tweets:
        print(API.post_api(endpoint=API_ENDPOINT, payload=tweet))
        
        
if __name__ == "__main__":
    main()