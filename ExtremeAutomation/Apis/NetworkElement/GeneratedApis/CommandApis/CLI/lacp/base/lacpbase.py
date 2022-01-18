"""
Base class for all lacp commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class LacpBase(CliBaseApi):
    def __init__(self, device):
        super(LacpBase, self).__init__()
        self.device = device

    def enable_global(self, *args, **kwargs):
        return self.base_function()

    def disable_global(self, *args, **kwargs):
        return self.base_function()

    def create_lag(self, *args, **kwargs):
        return self.base_function()

    def delete_lag(self, *args, **kwargs):
        return self.base_function()

    def set_lag_port(self, *args, **kwargs):
        return self.base_function()

    def clear_lag_port(self, *args, **kwargs):
        return self.base_function()

    def show_info(self, *args, **kwargs):
        return self.base_function()

    def show_lag_info(self, *args, **kwargs):
        return self.base_function()

    def show_port_all(self, *args, **kwargs):
        return self.base_function()

    def show_mlt_port(self, *args, **kwargs):
        return self.base_function()

    def show_mlt_id_logical_index(self, *args, **kwargs):
        return self.base_function()

    def disable_port(self, *args, **kwargs):
        return self.base_function()

    def enable_port(self, *args, **kwargs):
        return self.base_function()

    def set_port_priority(self, *args, **kwargs):
        return self.base_function()

    def set_system_priority(self, *args, **kwargs):
        return self.base_function()

    def clear_counters(self, *args, **kwargs):
        return self.base_function()

    def clear_all_counters(self, *args, **kwargs):
        return self.base_function()

    def show_counter(self, *args, **kwargs):
        return self.base_function()

    def show_sysid(self, *args, **kwargs):
        return self.base_function()

    def show_lag(self, *args, **kwargs):
        return self.base_function()
