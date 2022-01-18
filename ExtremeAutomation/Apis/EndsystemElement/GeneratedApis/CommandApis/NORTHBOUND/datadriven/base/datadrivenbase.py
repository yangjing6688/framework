"""
Base class for all devices northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class DatadrivenBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def verify_northbound_query(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def verify_northbound_query_with_regex(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
