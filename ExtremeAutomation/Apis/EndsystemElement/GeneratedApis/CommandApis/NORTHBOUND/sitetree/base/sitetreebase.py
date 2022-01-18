"""
Base class for all sitetree northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class SitetreeBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def placeholer(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
