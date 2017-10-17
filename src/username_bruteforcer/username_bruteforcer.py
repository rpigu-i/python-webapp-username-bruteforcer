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

    valid_users = {'users': []}
    invalid_users = {'users': []}
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

            if key['data'] and key['data'] != None:
                data_vals = key['data']
                for k in data_vals:
                    self.data[k] = data_vals[k]

            if key['users']:
                users_list = key['users']
                self.check_for_valid_users(users_list)

    def check_for_valid_users(self, users_list):
        """
        Using input parameters
        test target url/api
        to see if user exists
        """

        for u in users_list:

            self.data[self.user_field] = u
            r = requests.post(self.url, data=self.data)

            dictdata = json.loads(r.text)

            if dictdata[self.response_key] == self.valid_response:

                print "Status code is: "+str(r.status_code)
                print "Response message is: "+str(r.reason)
                print "Valid username: "+u
                self.valid_users['users'].append(u)
            else:
                self.invalid_users['users'].append(u)

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
