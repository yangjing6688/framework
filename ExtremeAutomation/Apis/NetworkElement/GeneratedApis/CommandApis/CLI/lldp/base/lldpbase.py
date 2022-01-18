"""
Base class for all lldp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class LldpBase(CliBaseApi):
    def __init__(self, device):
        super(LldpBase, self).__init__()
        self.device = device

    def enable(self, *args, **kwargs):
        return self.base_function()

    def disable(self, *args, **kwargs):
        return self.base_function()

    def enable_tx(self, *args, **kwargs):
        return self.base_function()

    def enable_rx(self, *args, **kwargs):
        return self.base_function()

    def enable_port_both(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def set_tx_interval(self, *args, **kwargs):
        return self.base_function()

    def set_sys_name(self, *args, **kwargs):
        return self.base_function()

    def clear_sys_name(self, *args, **kwargs):
        return self.base_function()

    def set_profile(self, *args, **kwargs):
        return self.base_function()

    def set_profile_interface(self, *args, **kwargs):
        return self.base_function()

    def set_tx_hold_multiplier(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_port_status(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors_detail(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors_port(self, *args, **kwargs):
        return self.base_function()

    def show_neighbors_port_detail(self, *args, **kwargs):
        return self.base_function()

    def show_statistics(self, *args, **kwargs):
        return self.base_function()

    def show_statistics_port(self, *args, **kwargs):
        return self.base_function()

    def enable_port_tx(self, *args, **kwargs):
        return self.base_function()

    def enable_port_rx(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_all(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_all(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_port_desc(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_port_desc(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_sys_name(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_sys_name(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_sys_desc(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_sys_desc(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_sys_cap(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_sys_cap(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_mgmt_addr(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_mgmt_addr(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_vlan_id(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_vlan_id(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_stp(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_stp(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_lacp(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_lacp(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_gvrp(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_gvrp(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_mac_phy(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_mac_phy(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_poe(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_poe(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_link_aggr(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_link_aggr(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_max_frame(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_max_frame(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_med_cap(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_med_cap(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_med_pol(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_med_pol(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_med_loc(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_med_loc(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_med_poe(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_med_poe(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_enhanced_trans_config(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_enhanced_trans_config(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_enhanced_trans_rec(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_enhanced_trans_rec(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_priority_flowctrl(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_priority_flowctrl(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_application_pri(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_application_pri(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_congestion_notif(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_congestion_notif(self, *args, **kwargs):
        return self.base_function()

    def enable_tlv_energy_eff_eth(self, *args, **kwargs):
        return self.base_function()

    def disable_tlv_energy_eff_eth(self, *args, **kwargs):
        return self.base_function()

    def show_remote_info(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_port_desc(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_sys_name(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_sys_desc(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_sys_cap(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_mgmt_addr(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_vlan_id(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_stp(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_lacp(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_gvrp(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_mac_phy(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_poe(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_link_aggr(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_max_frame(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_med_cap(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_med_pol(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_med_loc(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_med_poe(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_enhanced_trans_config(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_enhanced_trans_rec(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_priority_flowctrl(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_application_pri(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_congestion_notif(self, *args, **kwargs):
        return self.base_function()

    def show_port_tlv_energy_eff_eth(self, *args, **kwargs):
        return self.base_function()
