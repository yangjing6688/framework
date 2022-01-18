from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketInfoApi import PacketInfoApi, PacketInfoConstants

"""
    This is the API class for the command: packet_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketInfoApi(PacketInfoApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_info
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketInfoConstants.PACKET_INFO_API)
        assert isinstance(api, PacketInfoApi)
        api.packet_info(dummyDict)
    """
    def packet_info(self, argdictionary):
        return super(IxiaPacketInfoApi, self).packet_info(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    supportedIxiaHltapiCommands = {}
