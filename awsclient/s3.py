import json
import boto3


class S3:
    """
    Class for work with S3 instance
    """
    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_data(self, data, file_name, bucket):
        """
        Upload data in bytes to S3
        """
        try:
            print('[*] S3 start uploading data')
            data = json.dumps(data, indent=4, default=str, ensure_ascii=False).encode()
            self.s3.put_object(Body=data, 
                               Bucket=bucket, 
                               Key=file_name, 
                               ContentType='text')
            print('[*] S3 uploading success')
        except Exception as e:
            print('[-] S3 uploading error: ' + repr(e))

    def save_file(self, data, file_name):
        """
        Save data to file
        """
        try:
            print('[*] S3 start saving data to file')
            data = json.dumps(data, indent=4, default=str, ensure_ascii=False)
            with open(file_name, 'w') as f:
                f.write(data)
            print('[+] S3 saving data to success')
        except Exception as e:
            print('[-] S3 saving data to file error: ' + repr(e))
