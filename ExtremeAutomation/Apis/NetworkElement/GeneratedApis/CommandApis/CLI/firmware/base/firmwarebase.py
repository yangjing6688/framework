"""
Base class for all firmware commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class FirmwareBase(CliBaseApi):
    def __init__(self, device):
        super(FirmwareBase, self).__init__()
        self.device = device

    def determine_firmware(self, *args, **kwargs):
        return self.base_function()

    def download_firmware(self, *args, **kwargs):
        return self.base_function()

    def select_firmware(self, *args, **kwargs):
        return self.base_function()

    def delete_firmware(self, *args, **kwargs):
        return self.base_function()

    def show_firmware_info(self, *args, **kwargs):
        return self.base_function()

    def uninstall_xmod(self, *args, **kwargs):
        return self.base_function()

    def download_firmware_https(self, *args, **kwargs):
        return self.base_function()

    def show_installed_images(self, *args, **kwargs):
        return self.base_function()

    def show_firmware_version(self, *args, **kwargs):
        return self.base_function()

    def commit_firmware(self, *args, **kwargs):
        return self.base_function()

    def download_firmware_sftp(self, *args, **kwargs):
        return self.base_function()

    def download_firmware_scp(self, *args, **kwargs):
        return self.base_function()
