"""
Base class for all acl SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class AclBase(SnmpBaseApi):
    def __init__(self, device):
        super(AclBase, self).__init__()
        self.device = device

    def create_ipv4(self, *args, **kwargs):
        return self.base_function()

    def create_ipv6(self, *args, **kwargs):
        return self.base_function()

    def delete_list(self, *args, **kwargs):
        return self.base_function()

    def create_ace_index(self, *args, **kwargs):
        return self.base_function()

    def delete_ace_index(self, *args, **kwargs):
        return self.base_function()

    def enable_list(self, *args, **kwargs):
        return self.base_function()

    def disable_list(self, *args, **kwargs):
        return self.base_function()

    def enable_ace(self, *args, **kwargs):
        return self.base_function()

    def disable_ace(self, *args, **kwargs):
        return self.base_function()

    def set_name(self, *args, **kwargs):
        return self.base_function()

    def set_default_action(self, *args, **kwargs):
        return self.base_function()

    def set_port(self, *args, **kwargs):
        return self.base_function()

    def clear_port(self, *args, **kwargs):
        return self.base_function()

    def set_vlan(self, *args, **kwargs):
        return self.base_function()

    def clear_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_ace_action(self, *args, **kwargs):
        return self.base_function()

    def set_ace_name(self, *args, **kwargs):
        return self.base_function()

    def set_ace_ethernet_ethertype(self, *args, **kwargs):
        return self.base_function()

    def clear_ace_ethernet_ethertype(self, *args, **kwargs):
        return self.base_function()

    def show_all_ipv4(self, *args, **kwargs):
        return self.base_function()

    def show_all_ipv6(self, *args, **kwargs):
        return self.base_function()

    def show_ports(self, *args, **kwargs):
        return self.base_function()

    def show_vlans(self, *args, **kwargs):
        return self.base_function()

    def show_all_aces(self, *args, **kwargs):
        return self.base_function()

    def show_id(self, *args, **kwargs):
        return self.base_function()

    def show_ace_index_oper_state(self, *args, **kwargs):
        return self.base_function()

    def show_ace_index_name(self, *args, **kwargs):
        return self.base_function()

    def show_ace_index_action(self, *args, **kwargs):
        return self.base_function()

    def show_ace_index_ethernet_ethertype(self, *args, **kwargs):
        return self.base_function()
