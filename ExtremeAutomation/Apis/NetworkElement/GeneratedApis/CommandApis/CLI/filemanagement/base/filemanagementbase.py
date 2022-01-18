"""
Base class for all filemanagement commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class FilemanagementBase(CliBaseApi):
    def __init__(self, device):
        super(FilemanagementBase, self).__init__()
        self.device = device

    def copy_file_from_server(self, *args, **kwargs):
        return self.base_function()

    def copy_file(self, *args, **kwargs):
        return self.base_function()

    def set_system_config(self, *args, **kwargs):
        return self.base_function()

    def upload_core_file(self, *args, **kwargs):
        return self.base_function()

    def upload_file(self, *args, **kwargs):
        return self.base_function()

    def generate_support_file(self, *args, **kwargs):
        return self.base_function()

    def delete_file_on_slot(self, *args, **kwargs):
        return self.base_function()

    def show_logging_files(self, *args, **kwargs):
        return self.base_function()

    def show_config_files(self, *args, **kwargs):
        return self.base_function()

    def show_config_files_per_slot(self, *args, **kwargs):
        return self.base_function()

    def delete_file(self, *args, **kwargs):
        return self.base_function()

    def save_current_config(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_primary(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_secondary(self, *args, **kwargs):
        return self.base_function()

    def save_config_to_file(self, *args, **kwargs):
        return self.base_function()

    def set_system_to_primary_config(self, *args, **kwargs):
        return self.base_function()

    def set_system_to_backup_config(self, *args, **kwargs):
        return self.base_function()

    def show_default_boot_config_file(self, *args, **kwargs):
        return self.base_function()
