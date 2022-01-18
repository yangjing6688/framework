"""
Base class for all spanningtree commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SpanningtreeBase(CliBaseApi):
    def __init__(self, device):
        super(SpanningtreeBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def create_mst_instance(self, *args, **kwargs):
        return self.base_function()

    def delete_mst_instance(self, *args, **kwargs):
        return self.base_function()

    def enable_port_admin(self, *args, **kwargs):
        return self.base_function()

    def disable_port_admin(self, *args, **kwargs):
        return self.base_function()

    def enable_auto_edge(self, *args, **kwargs):
        return self.base_function()

    def disable_auto_edge(self, *args, **kwargs):
        return self.base_function()

    def set_stp_mode(self, *args, **kwargs):
        return self.base_function()

    def clear_stp_mode(self, *args, **kwargs):
        return self.base_function()

    def set_restricted_role(self, *args, **kwargs):
        return self.base_function()

    def set_restricted_tcn(self, *args, **kwargs):
        return self.base_function()

    def set_priority(self, *args, **kwargs):
        return self.base_function()

    def set_priority_mode(self, *args, **kwargs):
        return self.base_function()

    def set_tc_trap(self, *args, **kwargs):
        return self.base_function()

    def clear_tc_trap(self, *args, **kwargs):
        return self.base_function()

    def set_msti_vlan_mapping(self, *args, **kwargs):
        return self.base_function()

    def clear_msti_vlan_mapping(self, *args, **kwargs):
        return self.base_function()

    def set_mst_region_name(self, *args, **kwargs):
        return self.base_function()

    def set_mst_revision_level(self, *args, **kwargs):
        return self.base_function()

    def set_hello_time(self, *args, **kwargs):
        return self.base_function()

    def set_fwd_delay(self, *args, **kwargs):
        return self.base_function()

    def set_max_age(self, *args, **kwargs):
        return self.base_function()

    def show_info_detail(self, *args, **kwargs):
        return self.base_function()

    def show_info_summary(self, *args, **kwargs):
        return self.base_function()

    def show_instance_info(self, *args, **kwargs):
        return self.base_function()

    def show_instance_info_detail(self, *args, **kwargs):
        return self.base_function()

    def show_port_info(self, *args, **kwargs):
        return self.base_function()

    def show_port_info_detail(self, *args, **kwargs):
        return self.base_function()

    def show_version(self, *args, **kwargs):
        return self.base_function()

    def show_port_admin(self, *args, **kwargs):
        return self.base_function()

    def show_autoedge(self, *args, **kwargs):
        return self.base_function()

    def show_mst_digest(self, *args, **kwargs):
        return self.base_function()

    def enable_mst_instance(self, *args, **kwargs):
        return self.base_function()

    def disable_mst_instance(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan_autobind(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan_autobind(self, *args, **kwargs):
        return self.base_function()

    def set_mst_instance_tag(self, *args, **kwargs):
        return self.base_function()

    def set_port_link_type_point_to_point(self, *args, **kwargs):
        return self.base_function()

    def set_port_link_type_edge(self, *args, **kwargs):
        return self.base_function()

    def set_instance_msti(self, *args, **kwargs):
        return self.base_function()

    def set_instance_cist(self, *args, **kwargs):
        return self.base_function()

    def enable_mstp_global(self, *args, **kwargs):
        return self.base_function()

    def disable_mstp_global(self, *args, **kwargs):
        return self.base_function()

    def enable_rstp_global(self, *args, **kwargs):
        return self.base_function()

    def disable_rstp_global(self, *args, **kwargs):
        return self.base_function()

    def enable_bpduguard(self, *args, **kwargs):
        return self.base_function()

    def disable_bpduguard(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_info_summary(self, *args, **kwargs):
        return self.base_function()

    def create_mst_vlan_instance(self, *args, **kwargs):
        return self.base_function()

    def delete_mst_vlan_instance(self, *args, **kwargs):
        return self.base_function()

    def enable_mstp_on_port(self, *args, **kwargs):
        return self.base_function()

    def disable_mstp_on_port(self, *args, **kwargs):
        return self.base_function()

    def set_boot_flag_rstp(self, *args, **kwargs):
        return self.base_function()

    def set_boot_flag_mstp(self, *args, **kwargs):
        return self.base_function()

    def set_bpduguard_timeout(self, *args, **kwargs):
        return self.base_function()

    def clear_bpduguard_timeout(self, *args, **kwargs):
        return self.base_function()

    def show_port_edge(self, *args, **kwargs):
        return self.base_function()

    def show_port_role(self, *args, **kwargs):
        return self.base_function()

    def show_boot_flag(self, *args, **kwargs):
        return self.base_function()

    def show_bpduguard(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_info_detail(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_instance_info(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_port_info(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_port_info_detail(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_port_role(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_port_admin(self, *args, **kwargs):
        return self.base_function()

    def show_mstp_edge(self, *args, **kwargs):
        return self.base_function()

    def show_stp_port_role(self, *args, **kwargs):
        return self.base_function()
