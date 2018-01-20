#!/bin/python

import boto3, sys, botocore

action = sys.argv[1]  
bucket_name = sys.argv[2]

s3_client = boto3.client('s3')

if action == 'create-bucket'):
    print "Creating bucket"
    s3_client.create_bucket(Bucket=bucket_name)

s3_resource = boto3.resource('s3')

if action == 'delete-bucket':
    print "Deleting bucket"
    try:
        bucket = s3_resource.Bucket(bucket_name)
        #loop to delete everything inside the bucket so we can delete bucket
        for item in bucket.objects.all():
            item.delete()
        bucket.delete()
    except botocore.exceptions.ClientError as e:
        print e.response['Error']['Code']

if action == 'upload-object':
    print "Uploading object"
    s3_resource.Object(bucket_name,
                       'hello.txt').put(Body=open('/tmp/hello.txt', 'r'))


