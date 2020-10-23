#!/usr/bin/env python3

from requests import request

class API(object):

    @staticmethod
    def post_api(endpoint="https://postman-echo.com/post", payload="Test"):
        headers= {}
        response = request("POST", endpoint, headers=headers, data=payload)
        return response

if __name__ == "__main__":
    _payload = {'id': 1319721334776029184, 'username': 'efekarakus', 'tweet_content': ' Copilot v0.5.0 is released!! \U0001f973\n Manage scheduled jobs with the new "copilot job" cmds.\n Use an existing image with the new "location" field.\n Minor improvements: backend services no longer require ports, and deletions don\'t need a profile!\n\nhttps://t.co/fME5yysOPT', 'metadata': {'media': None, 'hashtags': [], 'created_date': 'Fri Oct 23 19:24:20 +0000 2020', 'retweet_data': None}}
    api = API.post_api(payload=_payload)
    print(api)