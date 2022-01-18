"""
Base class for all mld commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MldBase(CliBaseApi):
    def __init__(self, device):
        super(MldBase, self).__init__()
        self.device = device

    def enable_vlan(self, *args, **kwargs):
        return self.base_function()

    def disable_vlan(self, *args, **kwargs):
        return self.base_function()

    def set_version(self, *args, **kwargs):
        return self.base_function()

    def show_vlan(self, *args, **kwargs):
        return self.base_function()

    def show_version(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping(self, *args, **kwargs):
        return self.base_function()

    def enable_snooping_querier(self, *args, **kwargs):
        return self.base_function()

    def disable_snooping_querier(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_fast_leave(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_fast_leave(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_last_member_query_count(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_last_member_query_count(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_last_member_query_interval(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_last_member_query_interval(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_robustness_variable(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_robustness_variable(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_startup_query_count(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_startup_query_count(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_startup_query_interval(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_startup_query_interval(self, *args, **kwargs):
        return self.base_function()

    def set_snooping_mrouter(self, *args, **kwargs):
        return self.base_function()

    def clear_snooping_mrouter(self, *args, **kwargs):
        return self.base_function()

    def show_statistics(self, *args, **kwargs):
        return self.base_function()
