"""
Base class for all sysinfo commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class SysinfoBase(CliBaseApi):
    def __init__(self, device):
        super(SysinfoBase, self).__init__()
        self.device = device

    def show_hardware_summary(self, *args, **kwargs):
        return self.base_function()

    def show_core_files(self, *args, **kwargs):
        return self.base_function()

    def show_system_cpu_usage(self, *args, **kwargs):
        return self.base_function()

    def show_system_info(self, *args, **kwargs):
        return self.base_function()

    def show_system_slot_info(self, *args, **kwargs):
        return self.base_function()

    def show_slot_files(self, *args, **kwargs):
        return self.base_function()
