from pathlib import Path

class Config:
    """
    Set AWS configuration
    """
    def __init__(self):
        home = str(Path.home())
        self.credential_file = home + '/.aws/credentials'
        self.config_file = home + '/.aws/config'

    def set_config(self):
        try:
            print('[*] Enter aws_access_key_id:')
            aws_access_key_id = input()
            print('[*] Enter aws_secret_access_key:')
            aws_secret_access_key = input()
            print('[*] Enter aws_session_token:')
            aws_access_key_id = input()
            print('[*] Enter region:')
            region = input()
            creds = ('[default]\n'
                     'aws_access_key_id = ' + aws_access_key_id + '\n'
                     'aws_secret_access_key = ' + aws_secret_access_key + '\n'
                     'aws_session_token = ' + aws_access_key_id + '\n')
            with open(self.credential_file, 'w') as f:
                f.write(creds)
            config = ('[default]\n'
                     'region = ' + region + '\n')
            with open(self.config_file, 'w') as f:
                f.write(config)
            print('[+] Config saved')
        except Exception as e:
            print('[-] Config saving error: ' + repr(e))
