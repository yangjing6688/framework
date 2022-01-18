"""
All interface supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.interface.base.interfacebase import \
    InterfaceBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.interface.SNAPROUTE.base.baseversion.\
    baseunit.interfaceData import InterfaceData


class Interface(DeviceApi, InterfaceBase):
    def __init__(self, device):
        super(Interface, self).__init__(device)
        self.data_file = InterfaceData()

    def delete_interface(self, arg_dict, **kwargs):
        uri = "public/v1/config/IPv4Intf"
        request_type = "delete"
        data = self.data_file.delete_interface_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_ipv4_primary_addr_prefix(self, arg_dict, **kwargs):
        uri = "public/v1/config/IPv4Intf"
        request_type = "post"
        data = self.data_file.set_ipv4_primary_addr_prefix_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_ipv4_primary_addr_netmask(self, arg_dict, **kwargs):
        uri = "public/v1/config/IPv4Intf"
        request_type = "post"
        data = self.data_file.set_ipv4_primary_addr_netmask_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_info(self, arg_dict, **kwargs):
        uri = "public/v1/config/IPv4Intf"
        request_type = "get"
        data = self.data_file.show_info_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_all(self, arg_dict, **kwargs):
        uri = "public/v1/state/IPv4Intfs"
        request_type = "get"
        data = self.data_file.show_all_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
