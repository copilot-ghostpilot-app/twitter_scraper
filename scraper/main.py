#!/usr/bin/env python3

from os import getenv
from twitter_capture import TwitterCapture
from api import API
from ssm import SSM

API_ENDPOINT = getenv('API_ENDPOINT', 'https://postman-echo.com/post')

def set_parameter(value):
    param_name = "/{}/twitter_checkpoint".format(getenv("COPILOT_ENVIRONMENT_NAME"))
    return SSM().put_parameter(param_name, value)

def main():
    tweets = TwitterCapture().main()
    for tweet in tweets:
        print(API.post_api(endpoint=API_ENDPOINT, payload=tweet))
    try:
        set_parameter(value=str(tweets[-1]['id']))
    except IndexError as e:
        print("Unable to set the checkpoint parameter in SSM: {}".format(e))
        pass
        
        
if __name__ == "__main__":
    main()