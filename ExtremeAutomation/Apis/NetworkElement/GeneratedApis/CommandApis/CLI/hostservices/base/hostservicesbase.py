"""
Base class for all hostservices commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class HostservicesBase(CliBaseApi):
    def __init__(self, device):
        super(HostservicesBase, self).__init__()
        self.device = device

    def enable_sys_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def disable_sys_force_topology_ip_flag(self, *args, **kwargs):
        return self.base_function()

    def set_sys_clipid_topology_ip(self, *args, **kwargs):
        return self.base_function()

    def clear_sys_clipid_topology_ip(self, *args, **kwargs):
        return self.base_function()

    def show_sys_setting(self, *args, **kwargs):
        return self.base_function()

    def show_autotopology_nmm_table(self, *args, **kwargs):
        return self.base_function()
