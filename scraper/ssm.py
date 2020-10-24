#!/usr/bin/env python3

import boto3
import botocore

class SSM(object):
    def __init__(self):
        self.client = boto3.client('ssm')

    def get_parameter(self, name, value):
        try:
            return self.client.get_parameter(
                Name=name
            )
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'ParameterNotFound':
                self.put_parameter(name, value)
                return {'Parameter': {'Value': None }}
            else:
                raise error
        
    def put_parameter(self, name, value):
        return self.client.put_parameter(
            Name=name,
            Value=value,
            Type='String',
            Overwrite=True
        )

if __name__ == "__main__":
    ssm = SSM()
    print(ssm.get_parameter('/copilot/applications/twitter-backend-tests', 'test'))