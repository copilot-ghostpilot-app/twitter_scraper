#!/usr/bin/env python3

import boto3
import botocore

class DynamoDb(object):
    def __init__(self):
        self.client = boto3.client('dynamodb')

    def get_value(self, key, table):
        results = self.client.scan(
            TableName=table,
            AttributesToGet=['TwitterCheckpoint']
        )['Items']
        
        if not results:
            self.put_item(key, "None", table)
            return None
        else:
            return results
        
    def put_item(self, key, value, table):
        return self.client.put_item(
            TableName=table, 
            Item={key: {"S": value}}
        ) 

if __name__ == "__main__":
    ssm = SSM()
    print(ssm.get_parameter('/copilot/applications/twitter-backend-tests', 'test'))