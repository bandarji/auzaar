# OS functions

from os import environ as os_environ
from os import path as os_path
from socket import error as socket_error
from socket import inet_aton as socket_inet_aton
from subprocess import PIPE as ppipe
from subprocess import Popen as popen
from sys import argv as sysargv
from time import time as s_epoch

def exec_command(cmd_list=None):
    """ Run a command and return output as a list """
    if cmd_list:
        try:
            proc = popen(cmd_list, stdout=ppipe)
            return proc.communicate()[0].split('\n')
        except OSError:
            return ['ERROR: OSError']

def get_env(env_var):
    """ Return environment variable value or None """
    return os_environ.get(env_var, None)

def is_valid_address(address):
    """ Validate an IP address """
    try:
        socket_inet_aton(address)
    except socket_error:
        return False
    return True

def argv_count():
    """ How many command line arguments submitted """
    return len(sysargv)

def get_program_name():
    """ Return the name of the executable run, without path """
    return os_path.basename(sysargv[0])

def epoch_seconds():
    """ Return seconds since UNIX epoch; not accurate """
    return int(s_epoch())

if __name__ == '__main__':
    raise SystemExit('Do not execute this package component')
