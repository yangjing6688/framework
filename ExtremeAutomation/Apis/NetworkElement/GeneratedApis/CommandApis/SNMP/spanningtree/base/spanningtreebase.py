"""
Base class for all spanningtree SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class SpanningtreeBase(SnmpBaseApi):
    def __init__(self, device):
        super(SpanningtreeBase, self).__init__()
        self.device = device

    def enable_mstp_on_port(self, *args, **kwargs):
        return self.base_function()

    def disable_mstp_on_port(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_port_info(self, *args, **kwargs):
        return self.base_function()
