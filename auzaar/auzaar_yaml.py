#!/bin/false
# YAML Processing

try:
    from yaml import safe_load as yaml_load
except ImportError as import_error:
    raise SystemExit('ERROR: {}'.format(import_error))
    
class YAML(object):
    """
        Processing YAML files
        Humans can write YAML and they read easily
    """

    def __init__(self, yaml_file_name=None):
        """ YAML-grabbing function """
        self.yaml_dict = {}
        if yaml_file_name:
            try:
                with open(yaml_file_name) as yf:
                    self.yaml_dict = yaml_load(yf)
                yf.close()
            except IOError:
                self.yaml_dict = {
                    'ERROR': "Cannot read YAML {}".format(yaml_file_name)
                }
        else:
            self.yaml_dict = {
                'ERROR': "No YAML file supplied"
            }

    def get_dict(self):
        """ Return a dictionary of the YAML data """
        return self.yaml_dict

if __name__ == '__main__':
    raise SystemExit('Do not execute this package component')
