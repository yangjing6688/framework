"""
Base class for all hostutils commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class HostutilsBase(CliBaseApi):
    def __init__(self, device):
        super(HostutilsBase, self).__init__()
        self.device = device

    def ping_host(self, *args, **kwargs):
        return self.base_function()

    def enable_debug_mode(self, *args, **kwargs):
        return self.base_function()

    def return_debug_creds(self, *args, **kwargs):
        return self.base_function()

    def enable_feature_license(self, *args, **kwargs):
        return self.base_function()

    def telnet_to_ip(self, *args, **kwargs):
        return self.base_function()

    def ssh_to_ip(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr_burst(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr_data_tlv_size(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr_frame_size(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr_time_out(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_ipaddr_vrf(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_mac(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_burst(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_data_tlv_size(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_frame_size(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_priority(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_source_mode_nodal(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_source_mode_novlanmac(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_testfill_pattern_all_zero(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_testfill_pattern_all_zero_crc(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_testfill_pattern_pseudo_rand_bit_seq_crc(self, *args, **kwargs):
        return self.base_function()

    def l2_ping_vlan_routernodename_timeout(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_ipaddr(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_ipaddr_ttl(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_ipaddr_vrf(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_vlan_mac(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_vlan_routernodename_priority(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_vlan_routernodename_source_mode_nodal(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_vlan_routernodename_source_mode_novlanmac(self, *args, **kwargs):
        return self.base_function()

    def l2_traceroute_vlan_routernodename_ttl(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_mac(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_priority(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_routernodename(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_routernodename_priority(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_routernodename_source_mode_nodal(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_routernodename_ttl(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_source_mode_nodal(self, *args, **kwargs):
        return self.base_function()

    def l2_tracetree_vlan_isid_ttl(self, *args, **kwargs):
        return self.base_function()

    def l2_tracemroute(self, *args, **kwargs):
        return self.base_function()

    def l2_tracemroute_priority(self, *args, **kwargs):
        return self.base_function()

    def l2_tracemroute_ttl(self, *args, **kwargs):
        return self.base_function()

    def l2_tracemroute_vlan(self, *args, **kwargs):
        return self.base_function()

    def l2_tracemroute_vrf(self, *args, **kwargs):
        return self.base_function()
