"""
Base class for all interface commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class InterfaceBase(CliBaseApi):
    def __init__(self, device):
        super(InterfaceBase, self).__init__()
        self.device = device

    def create_interface(self, *args, **kwargs):
        return self.base_function()

    def delete_interface(self, *args, **kwargs):
        return self.base_function()

    def create_loopback(self, *args, **kwargs):
        return self.base_function()

    def delete_loopback(self, *args, **kwargs):
        return self.base_function()

    def enable_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_ip_forwarding(self, *args, **kwargs):
        return self.base_function()

    def disable_ip_forwarding(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_forwarding(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_forwarding(self, *args, **kwargs):
        return self.base_function()

    def enable_loopback(self, *args, **kwargs):
        return self.base_function()

    def disable_loopback(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_primary_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_primary_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_loopback_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_loopback_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_secondary_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_secondary_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_address(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_link_local_addr(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_eui64_address(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_loopback_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_addr_prefix(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_loopback_addr_netmask(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv6_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv6_loopback_address(self, *args, **kwargs):
        return self.base_function()

    def set_mac_address(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_info_basic(self, *args, **kwargs):
        return self.base_function()

    def show_loopback_info(self, *args, **kwargs):
        return self.base_function()

    def show_all(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_info(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_ip_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ip_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_forwarding_global(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan_spb_multicast(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan_spb_multicast(self, *args, **kwargs):
        return self.base_function()

    def enable_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def disable_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_brouter_port(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_brouter_port(self, *args, **kwargs):
        return self.base_function()

    def show_loopback(self, *args, **kwargs):
        return self.base_function()

    def show_brouter_port_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_brouter_port_ipv4(self, *args, **kwargs):
        return self.base_function()

    def show_chassis_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_vrf_spb(self, *args, **kwargs):
        return self.base_function()

    def show_vlan_spb(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_primary_addr_prefix_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_secondary_addr_prefix_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_address_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_link_local_addr_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_eui64_address_on_port(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_addr_prefix_on_port(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv6_address_on_port(self, *args, **kwargs):
        return self.base_function()

    def show_info_port(self, *args, **kwargs):
        return self.base_function()

    def show_info_port_basic(self, *args, **kwargs):
        return self.base_function()

    def show_all_ports(self, *args, **kwargs):
        return self.base_function()

    def show_ipv6_port_info(self, *args, **kwargs):
        return self.base_function()
