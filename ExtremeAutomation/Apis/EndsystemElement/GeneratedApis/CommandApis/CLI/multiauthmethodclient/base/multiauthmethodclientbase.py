"""
Base class for all multiauthmethodclient commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class MultiauthmethodclientBase(CliBaseApi):
    def __init__(self, device):
        super(MultiauthmethodclientBase, self).__init__()
        self.device = device

    def run_multiuser_config(self, *args, **kwargs):
        return self.base_function()

    def run_multiuser_config_no_logoff(self, *args, **kwargs):
        return self.base_function()

    def switch_to_root(self, *args, **kwargs):
        return self.base_function()

    def change_to_atgapps_dir(self, *args, **kwargs):
        return self.base_function()
