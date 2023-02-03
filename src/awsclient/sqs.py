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
        Class to work with AWS SQS
        
"""

import boto3

class SQS:
    """
    Class for work with SQS AWS Service
    """
    def __init__(self, queue):
        self.sqs = boto3.client('sqs')
        self.queue = queue

    def send_message(self, message_attributes, message_body, delay=10):
        response = self.sqs.send_message(
            QueueUrl=self.queue,
            DelaySeconds=delay,
            MessageAttributes=message_attributes,
            MessageBody=message_body
        )
        if 'MessageId' in response:
            return response

    def receive_messages(self, max_messages=1, delay=10):
        messages = []
        response = self.sqs.receive_message(
            QueueUrl=self.queue,
            WaitTimeSeconds=delay,
            MaxNumberOfMessages=max_messages
            )
        if 'Messages' in response:
            for message in response['Messages']:
                messages.append(message)
                receipt_handle = message['ReceiptHandle']
                resp = self.sqs.delete_message(
                    QueueUrl=self.queue,
                    ReceiptHandle=receipt_handle
                )      
        return messages
