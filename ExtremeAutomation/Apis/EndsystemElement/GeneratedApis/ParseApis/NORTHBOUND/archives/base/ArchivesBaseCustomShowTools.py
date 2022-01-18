from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class ArchivesBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(ArchivesBaseCustomShowTools, self).__init__()
        self.device = device

    def show_archives(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
