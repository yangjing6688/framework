"""
Base class for all lacp SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class LacpBase(SnmpBaseApi):
    def __init__(self, device):
        super(LacpBase, self).__init__()
        self.device = device

    def set_mlt_actor_key(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_actor_system_priority(self, *args, **kwargs):
        return self.base_function()

    def show_mlt_port(self, *args, **kwargs):
        return self.base_function()

    def show_mlt_id_logical_index(self, *args, **kwargs):
        return self.base_function()
