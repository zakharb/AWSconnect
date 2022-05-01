import paramiko


class SSHClient:
    """
    SSH client to connect and run command in EC2 instance
    """
    def __init__(self, ip, user):
        self.key = paramiko.RSAKey.from_private_key_file('config/key.pem')
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