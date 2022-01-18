from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiResetPortApi import ResetPortApi, ResetPortConstants

"""
    This is the API class for the command: reset_port

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentResetPortApi(ResetPortApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentResetPortApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: reset_port
    use this by passing in a dict() of all the commands

        api = device.getApi(ResetPortConstants.RESET_PORT_API)
        api.reset_port(dummyDict)
    """
    def reset_port(self, argdictionary):
        return super(SpirentResetPortApi, self).reset_port(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    supportedSpirentHltapiCommands = {ResetPortConstants.MODE_CMD, ResetPortConstants.PORT_HANDLE_CMD, ResetPortConstants.PROTOCOL_CMD}
