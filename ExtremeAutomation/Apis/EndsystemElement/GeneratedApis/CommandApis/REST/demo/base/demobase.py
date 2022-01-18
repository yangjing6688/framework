"""
Base class for all demo rest commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class DemoBase(RestBaseApi):
    def __init__(self, device):
        super(DemoBase, self).__init__()
        self.device = device

    def get_guest_user_data(self, *args, **kwargs):
        rest_request = RestCommandObject()
        rest_request.not_supported = True

        return rest_request
