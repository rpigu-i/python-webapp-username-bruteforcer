import requests
import json
import yaml


class UsernameBruteforcer():
    """"
    Class that takes input from
    a YAML file and then attempts to
    ascertain if a user account is
    valid on target application
    """

    valid_users = {}
    invalid_users = {}
    yamldump = {}
    user_field = ""
    data = {}
    url = ""
    response_key = ""
    valid_response = ""

    def __init__(self, yaml_config):
        """
        Kick off the application
        """
        self.load_yaml(yaml_config)
        self.load_params()
        self.dump_yaml_output()

    def load_yaml(self, yaml_config):
        """"
        Load params from
        a YAML document
        """
        opendoc = open(yaml_config, "r")
        self.yamldump = yaml.load_all(opendoc)

    def load_params(self):
        """
        Load parameters
        from yamldump
        """

        for key in self.yamldump:

            self.data = {}
            self.user_field = key['user_field']
            self.response_key = key['response']['response_key']
            self.valid_response = key['response']['valid_response']
            self.url = key['url']
            self.data[self.user_field] = ""

            try:
                self.proxies = key['proxies']
            except KeyError:
                self.proxies = None

            try:
                self.methods = [m.lower().strip() for m in key['methods']]
            except KeyError:
                raise ValueError('Missing "methods" list')

            if key['data'] and key['data'] != None:
                data_vals = key['data']
                for k in data_vals:
                    self.data[k] = data_vals[k]

            try:
                for m in self.methods:
                    self.check_for_valid_users(key['users'], m)
            except KeyError:
                raise ValueError('Missing "users" list')

    def check_for_valid_users(self, users_list, method):
        """
        Using input parameters
        test target url/api
        to see if user exists
        """

        self.valid_users[method] = {'users': []}
        self.invalid_users[method] = {'users': []}

        for u in users_list:

            self.data[self.user_field] = u
            requestMethod = getattr(requests, method, None)

            if requestMethod is None:
                raise ValueError('Method "{method}" is not supported'.format(
                    method=repr(method)))

            data_key = 'params' if method == 'get' else 'data'
            req_params = {'url': self.url,
                          'proxies': self.proxies, data_key: self.data}

            r = requestMethod(**req_params)
            dictdata = json.loads(r.text)

            if dictdata[self.response_key] == self.valid_response:

                print ("\nMethod is: " + method.upper())
                print ("Status code is: " + str(r.status_code))
                print ("Response message is: " + str(r.reason))
                print ("Valid username: " + u)
                self.valid_users[method]['users'].append(u)
            else:
                self.invalid_users[method]['users'].append(u)

    def dump_yaml_output(self):
        """
        Dump a lsit of valid and
        invalid users to two separate
        docs
        """
        valid_users_doc = file('valid_users.yaml', 'w')
        yaml.dump(self.valid_users, valid_users_doc, default_flow_style=False)

        invalid_users_doc = file('invalid_users.yaml', 'w')
        yaml.dump(self.invalid_users, invalid_users_doc,
                  default_flow_style=False)
