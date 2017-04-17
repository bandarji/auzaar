# F5 Networks

from ast import literal_eval as ast_eval
from requests import ConnectionError as r_ConnectionError
from requests import get as r_get
from f5.bigip import ManagementRoot
from requests import Timeout as r_Timeout
from requests import TooManyRedirects as r_TooManyRedirects
from requests.packages.urllib3 import disable_warnings as https_warn_disable

class BigIPCluster(object):
    """ F5 Networks BIG-IP cluster class """

    def __init__(self, addr_list=None, username=None, password=None):
        """ Check and store basic BIG-IP cluster information """
        self.addr_active = None
        if addr_list and type(addr_list) is list:
            self.addr_list = addr_list
            if len(addr_list) == 1:
                self.addr_active = addr_list[0]
            elif len(addr_list) == 0:
                self.addr_active = None
            else:
                https_warn_disable()
                self.get_active_bigip(addr_list, username, password)
        else:
            self.addr_list = []

    def get_active_bigip(self, addr_list, username, password):
        """ Determine the ACTIVE unit in a cluster """
        addr_active = None
        for address in addr_list:
            url = 'https://{}/mgmt/tm/cm/failover-status'.format(address)
            try:
                r = r_get(
                    url,
                    auth=(username, password),
                    verify=False,
                    timeout=(0.400,12.0)
                )
            except r_ConnectionError:
                raise SystemExit('ERROR: ConnectionError {}'.format(address))
            except r_Timeout:
                raise SystemExit('ERROR: Timeout {}'.format(address))
            except r_TooManyRedirects:
                raise SystemExit('ERROR: TooManyRedirects {}'.format(address))
            except Exception, e:
                raise SystemExit('ERROR: r_get failed')
            x = ast_eval(str(r.text))
            try:
                status = x['entries']['https://localhost/mgmt/tm/cm/failover-status/0']['nestedStats']['entries']['status']['description']
            except KeyError:
                raise SystemExit('ERROR: KeyError')
            except Exception, e:
                raise SystemExit('ERROR: {}'.format(e))
            if status == "ACTIVE":
                self.addr_active = address

class BigIP(object):
    """ Single BIG-IP system """

    def __init__(self, hostname=None, username=None, password=None):
        """ Validate BIG-IP credentials """
        if hostname and username and password:
            self.hostname = hostname
            self.username = username
            self.password = password
        else:
            raise SystemExit("0")

if __name__ == '__main__':
    raise SystemExit('Do not execute this package component')
