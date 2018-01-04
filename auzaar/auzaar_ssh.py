#!/bin/false
# Secure Shell

try:
    from paramiko import AutoAddPolicy as ssh_auto_add_policy
    from paramiko import SSHClient as ssh_client
except ImportError as import_error:
    raise SystemExit('ERROR: {}'.format(import_error))

class SSH(object):
    """
        Secure Shell provides encrypted communications with remote systems
    """

    def __init__(self, **ssh_params):
        """
            Example parameters dictionary:
            ssh_params = {
                'hostname': '127.0.0.1',
                'username': 'jgalt',
                'password': 'AtlasShrugged',
                'port': 22,
                'pkey': None,
                'key_filename': None,
                'timeout': 5,
                'allow_agent': False,
                'look_for_keys': False,
                'compress': False,
                'sock': None,
                'gss_auth': False,
                'gss_kex': False,
                'gss_deleg_creds': False,
                'gss_host': None,
                'banner_timeout': None
            }
        """
        self.ssh_params = ssh_params

    def connect(self):
        """ Establish Secure Shell connection """
        self.ssh = ssh_client()
        self.ssh.set_missing_host_key_policy(ssh_auto_add_policy())
        try:
            self.ssh.connect(**self.ssh_params)
        except Exception as e:
            raise SystemExit('SSH error {} with {}'.\
                format(e, self.ssh_params.get('hostname', '0')))

    def disconnect(self):
        """ Close Secure Shell connection """
        if self.ssh:
            try:
                self.ssh.close()
            except:
                pass

    def exec_command(self, cmd):
        """ Execute a command on remote shell, return list of stdout lines """
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.readlines()

if __name__ == '__main__':
    raise SystemExit('Do not execute this package component')
