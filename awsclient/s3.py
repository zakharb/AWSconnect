import json
import boto3


class S3:
    """
    Class for work with S3 instance
    """
    def __init__(self):
        self.s3 = boto3.client('s3')

    def put_object(self, file_name, bucket):
        """
        Upload data in bytes to S3
        """
        with open(file_name, 'r') as f:
            data = f.read()
        self.s3.put_object(Body=data, 
                           Bucket=bucket, 
                           Key=file_name)

    def get_object(self, file_name, bucket):
        """
        Save data to file
        """
        data = self.s3.get_object(Bucket=bucket, 
                           Key=file_name, 
                           ContentType='text')
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4, default=str, ensure_ascii=False)
