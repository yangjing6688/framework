"""
All policy supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.policy.base.policybase import PolicyBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.policy.EXOS.base.baseversion.baseunit.\
    policyData import PolicyData


class Policy(DeviceApi, PolicyBase):
    def __init__(self, device):
        super(Policy, self).__init__(device)
        self.data_file = PolicyData()

    def set_access_list(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls"
        request_type = "patch"
        data = self.data_file.set_access_list_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_access_list_all(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls"
        request_type = "delete"
        data = self.data_file.clear_access_list_all_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_access_list(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls/acl={0}".format(arg_dict['list_name'])
        request_type = "delete"
        data = self.data_file.clear_access_list_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def clear_access_list_rule(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls/acl={0}/aces/ace={1}".format(arg_dict['list_name'],
                                                                                             arg_dict['rule'])
        request_type = "delete"
        data = self.data_file.clear_access_list_rule_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_access_list_rule_name(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls/acl={0}/aces/ace={1}".format(arg_dict['list_name'],
                                                                                             arg_dict['rule'])
        request_type = "get"
        data = self.data_file.show_access_list_rule_name_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_access_list_list_name(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/ietf-access-control-list:acls/acl={0}".format(arg_dict['list_name'])
        request_type = "get"
        data = self.data_file.show_access_list_list_name_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
