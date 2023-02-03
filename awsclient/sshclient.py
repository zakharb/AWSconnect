"""
    AWSClient
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
        Class to work with SSHClient
        
"""

import paramiko
from pathlib import Path


class SSHClient:
    """
    SSH client to connect and run command in EC2 instance
    """
    def __init__(self, ip, user):
        home = str(Path.home())
        self.key = paramiko.RSAKey.from_private_key_file(home + '/.ssh/key.pem')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
        self.user = user

    def run_cmd(self, cmd):
        try:
            print('[*] SSH connection to IP: ' + self.ip)
            result = ''
            self.client.connect(hostname=self.ip, 
                                username=self.user, 
                                pkey=self.key,
                                timeout=5)
            stdin, stdout, stderr = self.client.exec_command(cmd)
            result = stdout.read().decode()
            self.client.close()
            print('[+] SSH connection success')
        except Exception as e:
            print('[-] SSH connection error: ' + repr(e))
        finally:
            return result