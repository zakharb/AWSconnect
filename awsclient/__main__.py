"""
	AWS client to work with EC2 and S3 instances
"""
import argparse
from awsclient import EC2, S3, Config

if __name__ == "__main__":
    print('   __    _    _  ___   ___  __    ____  ____  _  _  ____ \n'\
          '  /__\  ( \/\/ )/ __) / __)(  )  (_  _)( ___)( \( )(_  _)\n'\
          ' /(__)\  )    ( \__ \( (__  )(__  _)(_  )__)  )  (   )(  \n'\
          '(__)(__)(__/\__)(___/ \___)(____)(____)(____)(_)\_) (__) \n')
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    getinfo = subparser.add_parser('getinfo', help='Get info from EC2')
    config = subparser.add_parser('config', help='Set AWS connection config')
    getinfo.add_argument('--filename', type=str, required=True, help='name of the file')
    getinfo.add_argument('--bucket', type=str, help='save file to S3')
    args = parser.parse_args()
    if args.command == 'getinfo':
        print('\n[*] Start AWS Client\n----------------')
        ec2 = EC2()
        data = ec2.get_info()
        if data:
            s3 = S3()
            if args.bucket:
                s3.upload_data(data, args.filename, args.bucket)
            else:
                s3.save_file(data, args.filename)
            print('[+] Finish')
        else:
            print('[-] Can not get data, run "awsclient config"')
    elif args.command == 'config':
        config = Config()
        config.set_config()
    else:
        parser.print_help()
