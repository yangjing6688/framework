"""
Base class for all isis SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class IsisBase(SnmpBaseApi):
    def __init__(self, device):
        super(IsisBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def set_system_id(self, *args, **kwargs):
        return self.base_function()

    def clear_system_id(self, *args, **kwargs):
        return self.base_function()

    def set_manual_area(self, *args, **kwargs):
        return self.base_function()

    def clear_manual_area(self, *args, **kwargs):
        return self.base_function()

    def set_sys_name(self, *args, **kwargs):
        return self.base_function()

    def clear_sys_name(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_source_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_source_address(self, *args, **kwargs):
        return self.base_function()

    def set_ipv6_source_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv6_source_address(self, *args, **kwargs):
        return self.base_function()

    def set_ipv4_tunnel_source_address(self, *args, **kwargs):
        return self.base_function()

    def clear_ipv4_tunnel_source_address(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_bgp(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_bgp(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_bgp(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_bgp(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_direct(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_direct_ipv6(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_direct_ipv6(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_direct_apply(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_direct_route_map_policy(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_direct_route_map_policy(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_ospf(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_ospf(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_ospf(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_ospf(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_rip(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_rip(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_rip(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_rip(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def clear_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def enable_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def disable_redistribute_static(self, *args, **kwargs):
        return self.base_function()

    def set_redistribute_apply(self, *args, **kwargs):
        return self.base_function()

    def set_circuit_on_port(self, *args, **kwargs):
        return self.base_function()

    def enable_circuit_on_port(self, *args, **kwargs):
        return self.base_function()

    def disable_circuit_on_port(self, *args, **kwargs):
        return self.base_function()

    def clear_circuit_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_circuit_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def enable_circuit_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def disable_circuit_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def clear_circuit_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_auth_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_auth_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def clear_auth_on_port(self, *args, **kwargs):
        return self.base_function()

    def clear_auth_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_l1_dr_priority_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_l1_dr_priority_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_interval_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_interval_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_multiplier_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_multiplier_on_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_port(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_port_name(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_mlt(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_mlt_name(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_ipv4(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_ipv4_name(self, *args, **kwargs):
        return self.base_function()

    def clear_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def set_circuit_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_circuit_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def disable_circuit_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def clear_circuit_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def set_auth_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def clear_auth_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def set_l1_dr_priority_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_interval_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def set_l1_hello_multiplier_on_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def show_circuit(self, *args, **kwargs):
        return self.base_function()

    def show_circuit_interfaces(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_interface(self, *args, **kwargs):
        return self.base_function()

    def show_area(self, *args, **kwargs):
        return self.base_function()

    def show_lsdb(self, *args, **kwargs):
        return self.base_function()

    def show_manual_area(self, *args, **kwargs):
        return self.base_function()

    def show_spb_mcast_summary(self, *args, **kwargs):
        return self.base_function()

    def show_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_sys_id(self, *args, **kwargs):
        return self.base_function()

    def show_adjacencies(self, *args, **kwargs):
        return self.base_function()

    def show_interface_auth(self, *args, **kwargs):
        return self.base_function()

    def show_interface_timers(self, *args, **kwargs):
        return self.base_function()

    def show_system_stats(self, *args, **kwargs):
        return self.base_function()

    def show_logical_interface(self, *args, **kwargs):
        return self.base_function()

    def show_logical_interface_name(self, *args, **kwargs):
        return self.base_function()

    def show_interface_stats(self, *args, **kwargs):
        return self.base_function()

    def show_interface_l1_packet_stats(self, *args, **kwargs):
        return self.base_function()

    def show_interface_l2_packet_stats(self, *args, **kwargs):
        return self.base_function()

    def show_ip_redistribute(self, *args, **kwargs):
        return self.base_function()
