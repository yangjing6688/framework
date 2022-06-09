import inspect
import sys
import logging
import json
import io
import os
from datetime import datetime
import boto3
from botocore.exceptions import ClientError


class S3():
    ############################################################
    # Initialize logging:
    #
    # fileConfig('logging.ini')
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.bucket_name = 'raneto'
        dataDict    = {
            "access_key": os.environ['AWS_KEY'],
            "access_secret": os.environ['AWS_SECRET']}
        self.s3_client = self.connectToService(dataDict)['client']

    def connectToService(self,data):
        assert isinstance(data,dict)
        assert data['access_key'] and isinstance(data['access_key'],str)
        assert data['access_secret'] and isinstance(data['access_secret'],str)

        access_key    = data['access_key']
        access_secret = data['access_secret']
        retVal        = {}

        try:
            s3_client =  boto3.client(
                's3',
                aws_access_key_id     = access_key,
                aws_secret_access_key = access_secret
            )
        except ClientError as e:
            # Invalid creds?:
            retVal['error']  = str(e)

        else:
            retVal['client'] = s3_client
        return retVal

    def upload_file(self, file, bucket, object_name):
        with open(file, "rb") as f:
            self.s3_client.upload_fileobj(f, bucket, object_name)


if __name__ == "__main__":
    s3 = S3()
    # API Docs
    doc_api_bucket = "Documentation/Generated/"
    doc_file_location = os.path.join(os.getcwd(), "..","Documentation","Generated")
    for filename in os.listdir(doc_file_location):
        if filename != "index.md":
            fileObject = os.path.join(doc_file_location, filename)
            # checking if it is a file
            if os.path.isfile(fileObject):
                print("Uploading " + str(filename) + " to S3 " + doc_api_bucket)
                s3.upload_file(fileObject, s3.bucket_name , doc_api_bucket + filename)





