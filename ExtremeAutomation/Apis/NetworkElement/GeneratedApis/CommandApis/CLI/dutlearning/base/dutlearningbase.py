"""
Base class for all dutlearning commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class DutlearningBase(CliBaseApi):
    def __init__(self, device):
        super(DutlearningBase, self).__init__()
        self.device = device

    def show_system_info(self, *args, **kwargs):
        return self.base_function()

    def show_stacking_info(self, *args, **kwargs):
        return self.base_function()

    def show_stack_info(self, *args, **kwargs):
        return self.base_function()

    def show_chassis_info(self, *args, **kwargs):
        return self.base_function()

    def show_unit_info(self, *args, **kwargs):
        return self.base_function()

    def show_port_info(self, *args, **kwargs):
        return self.base_function()

    def show_license_info(self, *args, **kwargs):
        return self.base_function()
