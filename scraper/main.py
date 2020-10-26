#!/usr/bin/env python3

from os import getenv
from twitter_capture import TwitterCapture
from api import API
from ssm import SSM

API_ENDPOINT = getenv('API_ENDPOINT', 'https://postman-echo.com/post')
CHECKPOINT_PARAMETER_NAME = getenv('CHECKPOINT_PARAMETER_NAME')

def set_parameter(value):
    return SSM().put_parameter(CHECKPOINT_PARAMETER_NAME, value)

def main():
    tweets = TwitterCapture().main()
    for tweet in tweets:
        _rslt = API.post_api(endpoint=API_ENDPOINT, payload=tweet)
        if getenv('DEBUG'):
            print(_rslt)
    try:
        print("Setting parameter for next run. Last tweet id: {}".format(
            set_parameter(value=str(tweets[-1]['id']))))
    except IndexError as e:
        print("Unable to set the checkpoint parameter in SSM: {}".format(e))
        pass
        
        
if __name__ == "__main__":
    main()