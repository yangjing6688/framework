"""
All eciqdevices supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.eciqdevices.base.eciqdevicesbase import \
    EciqdevicesBase
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.REST.eciqdevices.ECIQ.base.baseversion.baseunit.\
    eciqdevicesData import EciqdevicesData


class Eciqdevices(DeviceApi, EciqdevicesBase):
    def __init__(self, device):
        super(Eciqdevices, self).__init__(device)
        self.data_file = EciqdevicesData()

    def get_client_list_on_device(self, arg_dict, **kwargs):
        uri = "xapi/v1/monitor/devices/{0}/clientList?ownerId={1}".format(arg_dict['device_id'],
                                                                          arg_dict['owner_id'])
        request_type = "get"
        data = self.data_file.get_client_list_on_device_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def get_device(self, arg_dict, **kwargs):
        uri = "xapi/v1/monitor/devices/{0}?ownerId={1}".format(arg_dict['device_id'],
                                                               arg_dict['owner_id'])
        request_type = "get"
        data = self.data_file.get_device_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def get_device_list(self, arg_dict, **kwargs):
        uri = "xapi/v1/monitor/devices?ownerId={0}".format(arg_dict['owner_id'])
        request_type = "get"
        data = self.data_file.get_device_list_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def get_network_policy_list(self, arg_dict, **kwargs):
        uri = "xapi/v1/configuration/networkpolicy/policies?ownerId={0}".format(arg_dict['owner_id'])
        request_type = "get"
        data = self.data_file.get_network_policy_list_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def remove_device(self, arg_dict, **kwargs):
        uri = "xapi/v1/configuration/device?ownerId={0}&ids={1}".format(arg_dict['owner_id'],
                                                                        arg_dict['device_id'])
        request_type = "delete"
        data = self.data_file.remove_device_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
