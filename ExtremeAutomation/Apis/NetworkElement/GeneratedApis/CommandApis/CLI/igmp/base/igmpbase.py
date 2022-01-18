"""
Base class for all igmp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class IgmpBase(CliBaseApi):
    def __init__(self, device):
        super(IgmpBase, self).__init__()
        self.device = device

    def set_version(self, *args, **kwargs):
        return self.base_function()

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_version(self, *args, **kwargs):
        return self.base_function()

    def show_state(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_proxy(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_proxy(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_group(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_querier(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_querier(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_querier_address(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_querier_address(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_compatibility_mode_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_compatibility_mode_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_dynamic_downgrade_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_dynamic_downgrade_vlan(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_explicit_host_tracking_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_explicit_host_tracking_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_port(self, *args, **kwargs):
        return self.base_function()

    def show_snooping(self, *args, **kwargs):
        return self.base_function()

    def show_snooping_querier_address(self, *args, **kwargs):
        return self.base_function()

    def show_sender(self, *args, **kwargs):
        return self.base_function()

    def show_snoop_trace(self, *args, **kwargs):
        return self.base_function()

    def show_router_alert(self, *args, **kwargs):
        return self.base_function()

    def set_version_interface(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_fast_leave(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_fast_leave(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_last_member_query_interval(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_last_member_query_count(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_query_interval(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_query_max_response_time(self, *args, **kwargs):
        return self.base_function()

    def show_groups_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_statistics_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_statistics_port(self, *args, **kwargs):
        return self.base_function()
