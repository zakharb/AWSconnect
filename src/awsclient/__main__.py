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
        Main function to start AWS Client
        
"""

import json
import argparse
from awsconnect.ec2 import EC2
from awsconnect.s3 import S3
from awsconnect.sqs import SQS
from awsconnect.config import Config

def print_logo():
    print('   __    _    _  ___   ___  __    ____  ____  _  _  ____ \n'\
          '  /__\  ( \/\/ )/ __) / __)(  )  (_  _)( ___)( \( )(_  _)\n'\
          ' /(__)\  )    ( \__ \( (__  )(__  _)(_  )__)  )  (   )(  \n'\
          '(__)(__)(__/\__)(___/ \___)(____)(____)(____)(_)\_) (__) \n')

def create_parser():
    parser = argparse.ArgumentParser(prog='awsconnect', 
                                     usage='%(prog)s [options]')
    subparser = parser.add_subparsers(dest='command')
    # create parser for ec2
    ec2 = subparser.add_parser('ec2', help='Use EC2 service')
    # create parser for s3
    s3 = subparser.add_parser('s3', help='Use S3 service')
    sub = s3.add_subparsers(dest='s3')
    put = sub.add_parser('put', help='Put file to S3')
    put.add_argument('--filename', type=str, required=True, help='Name of the file')
    put.add_argument('--bucket', type=str, required=True, help='Save file to S3')
    get = sub.add_parser('get', help='Get file from S3')
    get.add_argument('--filename', type=str, required=True, help='Name of the file')
    get.add_argument('--bucket', type=str, required=True, help='Save file to S3')
    # create parser for sqs
    sqs = subparser.add_parser('sqs', help='Use SQS service')
    sub = sqs.add_subparsers(dest='sqs')
    send = sub.add_parser('send', help='Send message to SQS')
    send.add_argument('--queue', type=str, help='SQS Queue to send messages')
    send.add_argument('--filename', type=str, required=True, help='Input JSON file with messages')
    send.add_argument('--maxmessages', type=int, help='Max number to send',default=100)
    send.add_argument('--delay', type=int, help='Delay in seconds for send',default=10)
    receive = sub.add_parser('receive', help='Receive messages from SQS')
    receive.add_argument('--queue', type=str, help='SQS Queue to receive messages from')
    receive.add_argument('--filename', type=str, help='Output JSON file with messages')
    receive.add_argument('--maxmessages', type=int, help='Max number to receive',default=1)
    receive.add_argument('--delay', type=str, help='Wait time when receive',default=20)
    # create parser for config
    config = subparser.add_parser('config', help='Set AWS connection config')
    return parser

def main():
    print_logo()
    parser = create_parser()
    args = parser.parse_args()
    if args.command == 'ec2':
        print('[*] Starting working with EC2')
        ec2 = EC2()
        print('[*] Getting info')
        data = ec2.get_info()
        print('[+] Got data about EC2:')
        print(data)
        print('[+] EC2 getting info success')
    elif args.command == 's3':
        print('[*] Starting working with S3')
        s3 = S3()
        if args.s3 == 'put':
            print('[*] S3 start uploading file', args.filename)
            s3.put_object(args.filename, args.bucket)
            print('[+] S3 uploading success')
        elif args.s3 == 'get':
            print('[*] S3 start downloading data from S3')
            s3.get_object(args.filename, args.bucket)
            print('[+] S3 downloading success')
        else:
            print('[-] Set positional arguments')            
    elif args.command == 'sqs':
        print('[*] Starting working with SQS')
        if args.sqs == 'send':
            sqs = SQS(args.queue)
            print('[*] SQS start sending messages')
            with open(args.filename, 'r') as f:
                messages = json.load(f)
            print('[+] Read messages from file: ', len(messages))
            for message in messages[:args.maxmessages]:
                resp = sqs.send_message(message['MessageAttributes'], 
                                        message['MessageBody'],
                                        args.delay)
                if resp:
                    print('[+] Write message to SQS: ', resp)
            print('[+] S3 sending finished')
        elif args.sqs == 'receive':
            sqs = SQS(args.queue)
            print('[*] SQS start receiving messages')
            messages = sqs.receive_messages(args.maxmessages,
                                            args.delay)
            if messages:
                print('[+] Got messages from SQS: ', len(messages))
                if args.filename:
                    with open(args.filename, 'w') as f:
                        json.dump(messages, f, indent=4, default=str, ensure_ascii=False)
                else:
                    for m in messages:
                        print(json.dumps(messages, indent=4, default=str, ensure_ascii=False))
            print('[+] S3 receiving finished')
        else:
            print('[-] Set positional arguments')
    elif args.command == 'config':
        config = Config()
        config.set_config()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()