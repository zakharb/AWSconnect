"""
    AWSConnect
    Copyright (C) 2022

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Author:
        Bengart Zakhar

    Description:
        Class to work with AWS S3
        
"""

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
