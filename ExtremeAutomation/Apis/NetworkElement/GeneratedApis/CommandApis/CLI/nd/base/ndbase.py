"""
Base class for all nd commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class NdBase(CliBaseApi):
    def __init__(self, device):
        super(NdBase, self).__init__()
        self.device = device

    def set_v6_neighbor(self, *args, **kwargs):
        return self.base_function()

    def clear_v6_neighbor(self, *args, **kwargs):
        return self.base_function()

    def show_table(self, *args, **kwargs):
        return self.base_function()

    def clear_v6_neighbor_port(self, *args, **kwargs):
        return self.base_function()
