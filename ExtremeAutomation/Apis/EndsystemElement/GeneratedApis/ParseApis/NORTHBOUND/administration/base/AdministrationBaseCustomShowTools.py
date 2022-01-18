from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class AdministrationBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(AdministrationBaseCustomShowTools, self).__init__()
        self.device = device

    def show_administration_server_info(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
