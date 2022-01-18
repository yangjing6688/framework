"""
All arp supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.arp.base.arpbase import ArpBase


class Arp(DeviceApi, ArpBase):
    def __init__(self, device):
        super(Arp, self).__init__(device)
        self.device = device

    def show_all_entries(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.4.22."

        return self.create_cmd_obj(command_type, oid)

    def show_entry(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.2.1.4.22.1.2."

        return self.create_cmd_obj(command_type, oid)
