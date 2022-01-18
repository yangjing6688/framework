"""
Base class for all networking commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class NetworkingBase(CliBaseApi):
    def __init__(self, device):
        super(NetworkingBase, self).__init__()
        self.device = device

    def connect_to_wireless_network(self, *args, **kwargs):
        return self.base_function()

    def disconnect_from_wireless_network(self, *args, **kwargs):
        return self.base_function()

    def show_wireless_network(self, *args, **kwargs):
        return self.base_function()
