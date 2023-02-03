from pathlib import Path
import os

class Config:
    """
    Set AWS configuration
    """
    def __init__(self):
        home = str(Path.home())
        self.aws_dir = home + '/.aws'
        self.credential_file = self.aws_dir + '/credentials'
        self.config_file = self.aws_dir + '/config'

    def set_config(self):
        print(self.credential_file)
        print(self.config_file)
        print('[*] Enter aws_access_key_id:')
        aws_access_key_id = input()
        print('[*] Enter aws_secret_access_key:')
        aws_secret_access_key = input()
        print('[*] Enter aws_session_token:')
        aws_session_token = input()
        #if not aws_session_token:
        #    aws_session_token = aws_secret_access_key
        print('[*] Enter region:')
        region = input()
        creds = ('[default]\n'
                 'aws_access_key_id = ' + aws_access_key_id + '\n'
                 'aws_secret_access_key = ' + aws_secret_access_key + '\n'
                 'aws_session_token = ' + aws_session_token + '\n')
        if not os.path.exists(self.aws_dir):
            os.mkdir(self.aws_dir)            
        with open(self.credential_file, 'w') as f:
            f.write(creds)
        config = ('[default]\n'
                 'region = ' + region + '\n')
        with open(self.config_file, 'w') as f:
            f.write(config)
        print('[+] Config saved')
