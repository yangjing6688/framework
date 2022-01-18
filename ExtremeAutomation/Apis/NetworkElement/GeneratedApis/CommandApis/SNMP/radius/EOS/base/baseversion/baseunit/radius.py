"""
All radius supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.radius.base.radiusbase import RadiusBase


class Radius(DeviceApi, RadiusBase):
    def __init__(self, device):
        super(Radius, self).__init__(device)
        self.device = device

    def clear_server(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.5624.1.2.4.1.5.1.8.{0}".format(arg_dict['index'])
        data_type = "i"
        value = "{0}".format(arg_dict['client_ip'])

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_global(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.5624.1.2.4."

        return self.create_cmd_obj(command_type, oid)
