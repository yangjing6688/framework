"""
All vlan supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.vlan.base.vlanbase import VlanBase


class Vlan(DeviceApi, VlanBase):
    def __init__(self, device):
        super(Vlan, self).__init__(device)
        self.device = device

    def show_all_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.7.1.4.3.1.1"

        return self.create_cmd_obj(command_type, oid)

    def show_names(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.31.1.1.1.1"

        return self.create_cmd_obj(command_type, oid)
