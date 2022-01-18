"""
All fdb supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.fdb.base.fdbbase import FdbBase


class Fdb(DeviceApi, FdbBase):
    def __init__(self, device):
        super(Fdb, self).__init__(device)
        self.device = device

    def show_all_entries(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.7.1.2.2.1.2"

        return self.create_cmd_obj(command_type, oid)

    def show_entry(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.7.1.2.2.1.2"

        return self.create_cmd_obj(command_type, oid)

    def show_vlan(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.7.1.2.2.1.2.{0}".format(arg_dict['vlan'])

        return self.create_cmd_obj(command_type, oid)

    def show_port(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.17.7.1.2.2.1.2"

        return self.create_cmd_obj(command_type, oid)
