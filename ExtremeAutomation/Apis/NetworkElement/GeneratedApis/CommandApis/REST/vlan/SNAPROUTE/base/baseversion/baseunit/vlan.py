"""
All vlan supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.vlan.base.vlanbase import VlanBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.vlan.SNAPROUTE.base.baseversion.baseunit.\
    vlanData import VlanData


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device):
        super(Vlan, self).__init__(device)
        self.data_file = VlanData()

    def create_vlan(self, arg_dict, **kwargs):
        uri = "public/v1/config/Vlan"
        request_type = "post"
        data = self.data_file.create_vlan_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def delete_vlan(self, arg_dict, **kwargs):
        uri = "public/v1/config/Vlan"
        request_type = "delete"
        data = self.data_file.delete_vlan_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_egress_untagged(self, arg_dict, **kwargs):
        uri = "public/v1/config/Vlan"
        request_type = "patch"
        data = self.data_file.set_egress_untagged_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def set_egress_tagged(self, arg_dict, **kwargs):
        uri = "public/v1/config/Vlan"
        request_type = "patch"
        data = self.data_file.set_egress_tagged_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_all_info(self, arg_dict, **kwargs):
        uri = "public/v1/state/Vlans"
        request_type = "get"
        data = self.data_file.show_all_info_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_info(self, arg_dict, **kwargs):
        uri = "public/v1/config/Vlan"
        request_type = "get"
        data = self.data_file.show_info_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
