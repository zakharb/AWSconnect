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
        Class to work with AWS EC2
        
"""

import json
import boto3
#from .sshclient import SSHClient


class EC2:
    """
    Class for work with EC2 instance
    """
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def get_info(self):
        """
        Get info from EC2 instance:
        Tags, PublicIpAddress, PublicDnsName, Version
        """
        response = self.ec2.describe_instances()
        reservations = response.get('Reservations')
        info = {}
        for res in reservations:
            instances = res.get('Instances')
            for instance in instances:
                instance_id = instance.get('InstanceId')
                public_ip = instance.get('PublicIpAddress')
                public_dns = instance.get('PublicDnsName')
                tags = instance.get('Tags')
                print('[+] Get info from EC2 instance: ' + instance_id)
                #ssh_client = SSHClient(public_ip, 'ec2-user')
                #version = ssh_client.run_cmd('cat /etc/os-release').split('\n')
                info[instance_id] = {
                    'PublicIpAddress': public_ip,
                    'PublicDnsName': public_dns,
                    'Tags': tags,
                    'Version': version,
                }
        info = json.dumps(info, indent=4, default=str, ensure_ascii=False)
        return info
