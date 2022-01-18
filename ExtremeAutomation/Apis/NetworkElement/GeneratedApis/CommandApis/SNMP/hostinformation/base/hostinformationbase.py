"""
Base class for all hostinformation SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class HostinformationBase(SnmpBaseApi):
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

    def show_system_name(self, *args, **kwargs):
        return self.base_function()

    def show_host_contact(self, *args, **kwargs):
        return self.base_function()

    def show_host_name(self, *args, **kwargs):
        return self.base_function()

    def show_host_location(self, *args, **kwargs):
        return self.base_function()

    def show_host_description(self, *args, **kwargs):
        return self.base_function()

    def show_host_uptime(self, *args, **kwargs):
        return self.base_function()

    def show_host_services(self, *args, **kwargs):
        return self.base_function()

    def show_host_object_id(self, *args, **kwargs):
        return self.base_function()
