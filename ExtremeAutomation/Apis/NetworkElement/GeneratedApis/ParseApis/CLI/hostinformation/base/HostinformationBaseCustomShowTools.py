from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject


class HostinformationBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(HostinformationBaseCustomShowTools, self).__init__()
        self.device = device
        self.it = self.device.inspection_toolkit

    def check_prompt(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_host_location(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_host_contact(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_host_name(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_app_iqagent(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def base_function(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function
