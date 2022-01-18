from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import PacketControlApi, PacketControlConstants

"""
    This is the API class for the command: packet_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentPacketControlApi(PacketControlApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentPacketControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_control
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketControlConstants.PACKET_CONTROL_API)
        api.packet_control(dummyDict)
    """
    def packet_control(self, argdictionary):
        return super(SpirentPacketControlApi, self).packet_control(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_control_action(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_control_packet_type(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {PacketControlConstants.PORT_HANDLE_CMD, PacketControlConstants.ACTION_CMD}
