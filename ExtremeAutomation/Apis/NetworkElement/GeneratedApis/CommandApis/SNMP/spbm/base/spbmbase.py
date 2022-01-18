"""
Base class for all spbm SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class SpbmBase(SnmpBaseApi):
    def __init__(self, device):
        super(SpbmBase, self).__init__()
        self.device = device

    def set_ethertype(self, *args, **kwargs):
        return self.base_function()

    def clear_ethertype(self, *args, **kwargs):
        return self.base_function()

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def enable_ip_shortcut(self, *args, **kwargs):
        return self.base_function()

    def disable_ip_shortcut(self, *args, **kwargs):
        return self.base_function()

    def enable_ipv6_shortcut(self, *args, **kwargs):
        return self.base_function()

    def disable_ipv6_shortcut(self, *args, **kwargs):
        return self.base_function()

    def enable_lsdb_trap(self, *args, **kwargs):
        return self.base_function()

    def disable_lsdb_trap(self, *args, **kwargs):
        return self.base_function()

    def set_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def set_isis_nickname(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_nickname(self, *args, **kwargs):
        return self.base_function()

    def set_isis_bvid(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_bvid(self, *args, **kwargs):
        return self.base_function()

    def enable_isis_multicast(self, *args, **kwargs):
        return self.base_function()

    def disable_isis_multicast(self, *args, **kwargs):
        return self.base_function()

    def set_isis_multicast_fwd_cache_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_multicast_fwd_cache_timeout(self, *args, **kwargs):
        return self.base_function()

    def set_isis_smlt_virtual_bmac(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_smlt_virtual_bmac(self, *args, **kwargs):
        return self.base_function()

    def set_isis_smlt_peer_system_id(self, *args, **kwargs):
        return self.base_function()

    def clear_isis_smlt_peer_system_id(self, *args, **kwargs):
        return self.base_function()

    def set_port_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def clear_port_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def clear_mlt_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def set_port_isis_interface_type_broadcast(self, *args, **kwargs):
        return self.base_function()

    def set_port_isis_interface_type_p2p(self, *args, **kwargs):
        return self.base_function()

    def clear_port_isis_interface_type(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_isis_interface_type_broadcast(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_isis_interface_type_p2p(self, *args, **kwargs):
        return self.base_function()

    def clear_mlt_isis_interface_type(self, *args, **kwargs):
        return self.base_function()

    def set_port_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def clear_port_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def set_mlt_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def clear_mlt_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def clear_logical_interface_isis_instance_id(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_isis_interface_type_broadcast(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_isis_interface_type_p2p(self, *args, **kwargs):
        return self.base_function()

    def clear_logical_interface_isis_interface_type(self, *args, **kwargs):
        return self.base_function()

    def set_logical_interface_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def clear_logical_interface_isis_l1_metric(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_isis_info(self, *args, **kwargs):
        return self.base_function()

    def show_isis_interface(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_all(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_unicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_unicast_fib_spbm_nh_as_mac(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_fib(self, *args, **kwargs):
        return self.base_function()
