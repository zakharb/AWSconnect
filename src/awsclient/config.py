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
        Class to set config to work with AWS
        
"""
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
