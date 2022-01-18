from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiSessionInfoApi import SessionInfoApi

"""
    This is the API class for the command: session_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentSessionInfoApi(SessionInfoApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentSessionInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: session_info
    use this by passing in a dict() of all the commands

        api = device.getApi(SessionInfoConstants.SESSION_INFO_API)
        api.session_info(dummyDict)
    """
    def session_info(self, argdictionary):
        return super(SpirentSessionInfoApi, self).session_info(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def session_info_mode(self):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_port_handle(self, port):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_session_keys_include_filter(self, any):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_traffic_handle(self, any):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {}
