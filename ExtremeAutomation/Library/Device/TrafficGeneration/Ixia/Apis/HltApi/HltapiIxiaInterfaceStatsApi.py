from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceStatsApi import InterfaceStatsApi, InterfaceStatsConstants

"""
    This is the API class for the command: interface_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaInterfaceStatsApi(InterfaceStatsApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaInterfaceStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: interface_stats
    use this by passing in a dict() of all the commands

        api = device.getApi(InterfaceStatsConstants.INTERFACE_STATS_API)
        api.interface_stats(dummyDict)
    """
    def interface_stats(self, argdictionary):
        return super(IxiaInterfaceStatsApi, self).interface_stats(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    supportedIxiaHltapiCommands = {InterfaceStatsConstants.PORT_HANDLE_CMD}
