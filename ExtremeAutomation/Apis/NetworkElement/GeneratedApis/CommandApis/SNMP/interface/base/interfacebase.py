"""
Base class for all interface SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class InterfaceBase(SnmpBaseApi):
    def __init__(self, device):
        super(InterfaceBase, self).__init__()
        self.device = device

    def enable_ip_forwarding(self, *args, **kwargs):
        return self.base_function()

    def disable_ip_forwarding(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_forwarding(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_forwarding(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_primary_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_primary_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_loopback_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_loopback_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_loopback_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv6_loopback_address(self, *args, **kwargs):
        return self.base_function()

    def enable_ip_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ip_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def enable_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def disable_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_brouter_port(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_brouter_port(self, *args, **kwargs):
        return self.base_function()

    def show_loopback_info(self, *args, **kwargs):
        return self.base_function()

    def show_brouter_port_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_brouter_port_ipv4(self, *args, **kwargs):
        return self.base_function()

    def show_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()
