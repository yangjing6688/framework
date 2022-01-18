"""
Base class for all vlan SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class VlanBase(SnmpBaseApi):
    def __init__(self, device):
        super(VlanBase, self).__init__()
        self.device = device

    def show_all_info(self, *args, **kwargs):
        return self.base_function()

    def show_names(self, *args, **kwargs):
        return self.base_function()

    def create_vlan(self, *args, **kwargs):
        return self.base_function()

    def delete_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_name(self, *args, **kwargs):
        return self.base_function()

    def set_isid(self, *args, **kwargs):
        return self.base_function()

    def clear_isid(self, *args, **kwargs):
        return self.base_function()

    def create_spbm(self, *args, **kwargs):
        return self.base_function()

    def set_member(self, *args, **kwargs):
        return self.base_function()

    def clear_member(self, *args, **kwargs):
        return self.base_function()

    def set_port_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def clear_port_encapsulation_dot1q(self, *args, **kwargs):
        return self.base_function()

    def show_name(self, *args, **kwargs):
        return self.base_function()

    def show_isid(self, *args, **kwargs):
        return self.base_function()

    def show_members_port(self, *args, **kwargs):
        return self.base_function()
