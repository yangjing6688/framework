from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import PacketConfigBuffersApi, PacketConfigBuffersConstants

"""
    This is the API class for the command: packet_config_buffers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentPacketConfigBuffersApi(PacketConfigBuffersApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentPacketConfigBuffersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_buffers
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API)
        api.packet_config_buffers(dummyDict)
    """
    def packet_config_buffers(self, argdictionary):
        return super(SpirentPacketConfigBuffersApi, self).packet_config_buffers(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_buffers_capture_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {PacketConfigBuffersConstants.ACTION_CMD, PacketConfigBuffersConstants.PORT_HANDLE_CMD}
