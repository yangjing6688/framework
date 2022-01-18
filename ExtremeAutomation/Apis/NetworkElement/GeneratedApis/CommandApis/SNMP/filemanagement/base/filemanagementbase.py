"""
Base class for all filemanagement SNMP commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi


class FilemanagementBase(SnmpBaseApi):
    def __init__(self, device):
        super(FilemanagementBase, self).__init__()
        self.device = device

    def set_system_config(self, *args, **kwargs):
        return self.base_function()

    def save_current_config(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_primary(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_secondary(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_file(self, *args, **kwargs):
        return self.base_function()

    def set_system_to_backup_config(self, *args, **kwargs):
        return self.base_function()

    def show_default_boot_config_file(self, *args, **kwargs):
        return self.base_function()
