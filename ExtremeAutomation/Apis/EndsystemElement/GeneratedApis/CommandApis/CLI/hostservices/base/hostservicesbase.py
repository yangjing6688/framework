"""
Base class for all hostservices commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class HostservicesBase(CliBaseApi):
    def __init__(self, device):
        super(HostservicesBase, self).__init__()
        self.device = device

    def ping_host_from_endsys(self, *args, **kwargs):
        return self.base_function()

    def download_file_via_ftp(self, *args, **kwargs):
        return self.base_function()
