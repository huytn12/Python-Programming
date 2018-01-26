#!/usr/bin/python
import boto3
import sys

s3 = boto3.resource('s3')
for bucket_name in sys.argv[1:]:
    try:
        response = s3.create_bucket(Bucket=bucket_name)
        print response
    except Exception as error:
        print error

