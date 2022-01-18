"""
Base class for all resetdevice commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


class ResetdeviceBase(CliBaseApi):
    def __init__(self, device):
        super(ResetdeviceBase, self).__init__()
        self.device = device

    def reset_now(self, *args, **kwargs):
        return self.base_function()

    def reset_system_to_config(self, *args, **kwargs):
        return self.base_function()

    def reset_factory_default(self, *args, **kwargs):
        return self.base_function()

    def bypass_initial_setup(self, *args, **kwargs):
        return self.base_function()

    def login_after_reset(self, *args, **kwargs):
        return self.base_function()

    def run_failover(self, *args, **kwargs):
        return self.base_function()

    def run_failover_warm(self, *args, **kwargs):
        return self.base_function()

    def reset_system(self, *args, **kwargs):
        return self.base_function()
