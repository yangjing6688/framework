from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class DatadrivenBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(DatadrivenBaseCustomShowTools, self).__init__()
        self.device = device

    def verify_northbound_query(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def verify_northbound_query_with_regex(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
