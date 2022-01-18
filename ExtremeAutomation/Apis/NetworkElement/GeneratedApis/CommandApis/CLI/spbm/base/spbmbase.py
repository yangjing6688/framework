"""
Base class for all spbm commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SpbmBase(CliBaseApi):
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

    def set_virtual_ist_peer_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_virtual_ist_peer_ip(self, *args, **kwargs):
        return self.base_function()

    def show_virtual_ist(self, *args, **kwargs):
        return self.base_function()

    def show_virtual_ist_stat(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_isis_info(self, *args, **kwargs):
        return self.base_function()

    def show_isis_interface(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_all(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_all_id(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_all_nickname(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_all_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_config(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_config_id(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_config_nickname(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_config_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_discover(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_discover_id(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_discover_nickname(self, *args, **kwargs):
        return self.base_function()

    def show_isis_isid_discover_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_all(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_group(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_group_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_group_source(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_group_source_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_group_source_beb(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_group(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_group_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_group_source(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_group_source_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vlan_group_source_beb(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vrf(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vrf_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vrf_group(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vsn_isid(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vsn_isid_etail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_multicast_route_vsn_isid_group(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_unicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ipv6_unicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ipv6_unicast_fib_id(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_unicast_fib_id(self, *args, **kwargs):
        return self.base_function()

    def show_isis_ip_unicast_fib_spbm_nh_as_mac(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_detail(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_isid(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_nickname(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_summary(self, *args, **kwargs):
        return self.base_function()

    def show_isis_multicast_fib_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_nickname(self, *args, **kwargs):
        return self.base_function()

    def show_isis_nickname_smlt_virtual_bmac(self, *args, **kwargs):
        return self.base_function()

    def show_isis_nickname_sysid(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_fib(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_fib_bmac(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_fib_summary(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_fib_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_tree(self, *args, **kwargs):
        return self.base_function()

    def show_isis_unicast_tree_destination(self, *args, **kwargs):
        return self.base_function()

    def show_isid(self, *args, **kwargs):
        return self.base_function()

    def show_isid_all(self, *args, **kwargs):
        return self.base_function()

    def show_isid_elan(self, *args, **kwargs):
        return self.base_function()

    def show_isid_elan_transparent(self, *args, **kwargs):
        return self.base_function()

    def show_isid_mac_address_entry(self, *args, **kwargs):
        return self.base_function()

    def show_isid_mac_address_entry_all(self, *args, **kwargs):
        return self.base_function()

    def show_isid_mac_address_entry_mac(self, *args, **kwargs):
        return self.base_function()

    def show_isid_mac_address_entry_port(self, *args, **kwargs):
        return self.base_function()

    def show_isid_mac_address_entry_remote(self, *args, **kwargs):
        return self.base_function()
