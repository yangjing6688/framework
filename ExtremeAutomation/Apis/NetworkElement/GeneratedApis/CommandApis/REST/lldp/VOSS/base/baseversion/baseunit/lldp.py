"""
All lldp supported rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.lldp.base.lldpbase import LldpBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.lldp.EXOS.base.baseversion.baseunit.lldpData \
    import LldpData


class Lldp(DeviceApi, LldpBase):
    def __init__(self, device):
        super(Lldp, self).__init__(device)
        self.data_file = LldpData()

    def enable_port_both(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp"
        request_type = "patch"
        data = self.data_file.enable_port_both_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def disable_port(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp"
        request_type = "patch"
        data = self.data_file.disable_port_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_info(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp/config"
        request_type = "get"
        data = self.data_file.show_info_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_remote_info(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp/interfaces/interface={0}/neighbors".format(arg_dict['port'])
        request_type = "get"
        data = self.data_file.show_remote_info_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_port_status(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp/interfaces/interface={0}".format(arg_dict['port'])
        request_type = "get"
        data = self.data_file.show_port_status_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)

    def show_neighbors(self, arg_dict, **kwargs):
        uri = "rest/restconf/data/openconfig-lldp:lldp/interfaces/interface={0}/neighbors".format(arg_dict['port'])
        request_type = "get"
        data = self.data_file.show_neighbors_data

        return self.create_cmd_obj(uri, request_type, data, arg_dict)
