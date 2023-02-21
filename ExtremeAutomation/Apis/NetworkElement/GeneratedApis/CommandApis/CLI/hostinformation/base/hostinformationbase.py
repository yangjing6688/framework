"""
Base class for all hostinformation commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class HostinformationBase(CliBaseApi):
    def __init__(self, device):
        super(HostinformationBase, self).__init__()
        self.device = device

    def set_prompt(self, *args, **kwargs):
        return self.base_function()

    def set_host_contact(self, *args, **kwargs):
        return self.base_function()

    def set_host_name(self, *args, **kwargs):
        return self.base_function()

    def set_host_location(self, *args, **kwargs):
        return self.base_function()

    def clear_prompt(self, *args, **kwargs):
        return self.base_function()

    def show_system_name(self, *args, **kwargs):
        return self.base_function()

    def show_host_contact(self, *args, **kwargs):
        return self.base_function()

    def show_host_name(self, *args, **kwargs):
        return self.base_function()

    def show_host_location(self, *args, **kwargs):
        return self.base_function()

    def show_app_iqagent(self, *args, **kwargs):
        return self.base_function()

    def show_system_software_version(self, *args, **kwargs):
        return self.base_function()
