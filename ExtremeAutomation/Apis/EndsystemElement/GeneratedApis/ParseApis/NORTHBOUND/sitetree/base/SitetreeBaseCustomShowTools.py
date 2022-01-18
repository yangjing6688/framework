from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class SitetreeBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(SitetreeBaseCustomShowTools, self).__init__()
        self.device = device

    def placeholder(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
