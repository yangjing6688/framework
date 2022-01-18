"""
All spanningtree supported SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.SNMP.spanningtree.base.spanningtreebase import \
    SpanningtreeBase


class Spanningtree(DeviceApi, SpanningtreeBase):
    def __init__(self, device):
        super(Spanningtree, self).__init__(device)
        self.device = device

    def enable_mstp_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.5.1.3.1.13.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "1"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def disable_mstp_on_port(self, arg_dict, **kwargs):
        command_type = "snmpset"
        oid = "1.3.6.1.4.1.45.5.5.1.3.1.13.{0}".format(arg_dict['port'])
        data_type = "i"
        value = "0"

        return self.create_cmd_obj(command_type, oid, data_type, value)

    def show_mstp_port_info(self, arg_dict, **kwargs):
        command_type = "snmpwalk"
        oid = "1.3.6.1.4.1.45.5.5.1.3.1.13"

        return self.create_cmd_obj(command_type, oid)
