"""
Base class for all ospf SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class OspfBase(SnmpBaseApi):
    def __init__(self, device):
        super(OspfBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def set_router_id(self, *args, **kwargs):
        return self.base_function()

    def clear_router_id(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_interface(self, *args, **kwargs):
        return self.base_function()

    def show_interface(self, *args, **kwargs):
        return self.base_function()
