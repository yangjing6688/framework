from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject


class SyslogBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(SyslogBaseCustomShowTools, self).__init__()
        self.device = device
        self.it = self.device.inspection_toolkit

    def verify_login_exists(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_syslog_server(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def base_function(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function
