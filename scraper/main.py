#!/usr/bin/env python3

from os import getenv
from json import dumps
from twitter_capture import TwitterCapture
from api import API
from ssm import SSM

API_ENDPOINT = "http://{}.{}:8080/tweets/create".format(getenv('API_ENDPOINT'), getenv('COPILOT_SERVICE_DISCOVERY_ENDPOINT'))
CHECKPOINT_PARAMETER_NAME = getenv('CHECKPOINT_PARAMETER_NAME')

def set_parameter(value):
    return SSM().put_parameter(CHECKPOINT_PARAMETER_NAME, value)

def main():
    print("Beginning Twitter capture...")
    tweets = TwitterCapture().main()
    for tweet in tweets:
        _rslt = API.post_api(endpoint=API_ENDPOINT, payload=tweet)
        if getenv('DEBUG'):
            print(_rslt)
            print(_rslt.text)
    try:
        last_tweet_id = eval(tweets[-1]).get('id')
        print("Setting parameter for next run. Last tweet id: {}".format(last_tweet_id))
        print(set_parameter(value=str(last_tweet_id)))
    except IndexError as e:
        print("Unable to set the checkpoint parameter in SSM: {}".format(e))
        pass
        
        
if __name__ == "__main__":
    main()