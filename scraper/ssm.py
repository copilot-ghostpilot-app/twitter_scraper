#!/usr/bin/env python3

from boto3 import client

class SSM(object):

    @staticmethod
    def get_parameter(param_name):
        return "param_name"

if __name__ == "__main__":
    ssm = SSM()