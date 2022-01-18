"""
Base class for all devicevlans northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class DevicevlansBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def placeholder(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
