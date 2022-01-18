"""
Base class for all archives northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class ArchivesBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def show_archives(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
