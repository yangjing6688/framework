from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class DemoBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(DemoBaseCustomShowTools, self).__init__()
        self.device = device
        self.it = self.device.inspection_toolkit

    def verify_guest_onboarding_template(self, *func_args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def base_function(self, *args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def __getattr__(self, item):
        # Return the base_function if the called function does not exist.
        return self.base_function
