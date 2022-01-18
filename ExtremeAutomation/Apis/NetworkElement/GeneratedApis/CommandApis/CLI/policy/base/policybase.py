"""
Base class for all policy commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class PolicyBase(CliBaseApi):
    def __init__(self, device):
        super(PolicyBase, self).__init__()
        self.device = device

    def set_invalid(self, *args, **kwargs):
        return self.base_function()

    def clear_invalid(self, *args, **kwargs):
        return self.base_function()

    def set_port_admin_profile(self, *args, **kwargs):
        return self.base_function()

    def clear_port_admin_profile(self, *args, **kwargs):
        return self.base_function()

    def set_mac_source_admin_profile(self, *args, **kwargs):
        return self.base_function()

    def clear_mac_source_admin_profile(self, *args, **kwargs):
        return self.base_function()

    def set_profile(self, *args, **kwargs):
        return self.base_function()

    def set_profile_with_name(self, *args, **kwargs):
        return self.base_function()

    def clear_profile(self, *args, **kwargs):
        return self.base_function()

    def set_profile_name(self, *args, **kwargs):
        return self.base_function()

    def set_profile_pvid_status(self, *args, **kwargs):
        return self.base_function()

    def set_profile_pvid(self, *args, **kwargs):
        return self.base_function()

    def set_profile_cos_status(self, *args, **kwargs):
        return self.base_function()

    def set_profile_cos(self, *args, **kwargs):
        return self.base_function()

    def set_profile_egress_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_profile_untagged_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_profile_forbidden_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_profile_tci_overwrite(self, *args, **kwargs):
        return self.base_function()

    def set_profile_pvid_pvid_status(self, *args, **kwargs):
        return self.base_function()

    def set_profile_untagged_pvid(self, *args, **kwargs):
        return self.base_function()

    def set_rule(self, *args, **kwargs):
        return self.base_function()

    def clear_profile_rules(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ether(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ether(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ip6dest(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ip6dest(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipdestsocket(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipdestsocket(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipfrag(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipfrag(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipproto(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipproto(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipsourcesocket(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipsourcesocket(self, *args, **kwargs):
        return self.base_function()

    def set_rule_iptos(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_iptos(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipttl(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipttl(self, *args, **kwargs):
        return self.base_function()

    def set_rule_macdest(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_macdest(self, *args, **kwargs):
        return self.base_function()

    def set_rule_macsource(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_macsource(self, *args, **kwargs):
        return self.base_function()

    def set_rule_port(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_port(self, *args, **kwargs):
        return self.base_function()

    def set_rule_tcpdestportip(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_tcpdestportip(self, *args, **kwargs):
        return self.base_function()

    def set_rule_tcpsourceportip(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_tcpsourceportip(self, *args, **kwargs):
        return self.base_function()

    def set_rule_udpdestportip(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_udpdestportip(self, *args, **kwargs):
        return self.base_function()

    def set_rule_udpsourceportip(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_udpsourceportip(self, *args, **kwargs):
        return self.base_function()

    def set_maptable_response(self, *args, **kwargs):
        return self.base_function()

    def clear_maptable_response(self, *args, **kwargs):
        return self.base_function()

    def enable(self, *args, **kwargs):
        return self.base_function()

    def disable(self, *args, **kwargs):
        return self.base_function()

    def set_vlanauthorization_state(self, *args, **kwargs):
        return self.base_function()

    def set_rule_model_access_list(self, *args, **kwargs):
        return self.base_function()

    def set_rule_model_hierarchical(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_profile_index(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_profile_none(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_profile_highest(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_profile_lowest(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_rule_precedence_first(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_rule_precedence_last(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_rule_precedence_before(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_rule_precedence_after(self, *args, **kwargs):
        return self.base_function()

    def set_access_list(self, *args, **kwargs):
        return self.base_function()

    def set_access_list_action_set(self, *args, **kwargs):
        return self.base_function()

    def clear_all_rules(self, *args, **kwargs):
        return self.base_function()

    def clear_access_list_all(self, *args, **kwargs):
        return self.base_function()

    def clear_access_list(self, *args, **kwargs):
        return self.base_function()

    def clear_access_list_rule(self, *args, **kwargs):
        return self.base_function()

    def clear_access_list_action_set(self, *args, **kwargs):
        return self.base_function()

    def show_state(self, *args, **kwargs):
        return self.base_function()

    def show_map_response(self, *args, **kwargs):
        return self.base_function()

    def show_profiles(self, *args, **kwargs):
        return self.base_function()

    def show_profile(self, *args, **kwargs):
        return self.base_function()

    def show_rules(self, *args, **kwargs):
        return self.base_function()

    def show_invalid_action(self, *args, **kwargs):
        return self.base_function()

    def show_vlanauthorization(self, *args, **kwargs):
        return self.base_function()

    def show_allow_type(self, *args, **kwargs):
        return self.base_function()

    def show_all_rules(self, *args, **kwargs):
        return self.base_function()

    def show_all_profiles(self, *args, **kwargs):
        return self.base_function()

    def show_rules_profile(self, *args, **kwargs):
        return self.base_function()

    def show_invalid_count(self, *args, **kwargs):
        return self.base_function()

    def show_admin_profiles(self, *args, **kwargs):
        return self.base_function()

    def show_access_list_rule_name(self, *args, **kwargs):
        return self.base_function()

    def show_access_list_list_name(self, *args, **kwargs):
        return self.base_function()

    def show_access_list_action_set(self, *args, **kwargs):
        return self.base_function()

    def set_profile_precedence(self, *args, **kwargs):
        return self.base_function()

    def set_profile_mirror_dest(self, *args, **kwargs):
        return self.base_function()

    def set_profile_syslog(self, *args, **kwargs):
        return self.base_function()

    def set_profile_trap(self, *args, **kwargs):
        return self.base_function()

    def set_profile_disable_port(self, *args, **kwargs):
        return self.base_function()

    def set_profile_fst(self, *args, **kwargs):
        return self.base_function()

    def set_profile_web_redirect(self, *args, **kwargs):
        return self.base_function()

    def set_rule_application(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_application(self, *args, **kwargs):
        return self.base_function()

    def set_rule_icmp6type(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_icmp6type(self, *args, **kwargs):
        return self.base_function()

    def set_rule_icmptype(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_icmptype(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ip6flowlabel(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ip6flowlabel(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ip6source(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ip6source(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxclass(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxclass(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxdest(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxdest(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxdestsocket(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxdestsocket(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxsource(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxsource(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxsourcesocket(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxsourcesocket(self, *args, **kwargs):
        return self.base_function()

    def set_rule_ipxtype(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_ipxtype(self, *args, **kwargs):
        return self.base_function()

    def set_rule_llcdsapssap(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_llcdsapssap(self, *args, **kwargs):
        return self.base_function()

    def set_rule_tci(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_tci(self, *args, **kwargs):
        return self.base_function()

    def set_rule_vlantag(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_vlantag(self, *args, **kwargs):
        return self.base_function()

    def set_profile_access_control(self, *args, **kwargs):
        return self.base_function()

    def set_profile_traffic_mirror(self, *args, **kwargs):
        return self.base_function()

    def set_rule_l7(self, *args, **kwargs):
        return self.base_function()

    def clear_rule_l7(self, *args, **kwargs):
        return self.base_function()

    def set_rule_l7_configure(self, *args, **kwargs):
        return self.base_function()

    def set_rule_apply(self, *args, **kwargs):
        return self.base_function()

    def show_profile_detail(self, *args, **kwargs):
        return self.base_function()
