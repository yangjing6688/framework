from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import PacketConfigBuffersApi, PacketConfigBuffersConstants

"""
    This is the API class for the command: packet_config_buffers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketConfigBuffersApi(PacketConfigBuffersApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketConfigBuffersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_buffers
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API)
        api.packet_config_buffers(dummyDict)
    """
    def packet_config_buffers(self, argdictionary):
        return super(IxiaPacketConfigBuffersApi, self).packet_config_buffers(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_buffers_capture_mode(self, opt):
        """
        This is the method the command: packet_config_buffers option capture_mode
        Description:Supported with IxTclHal and IxTclNetwork. Controls whether data capture is performed in a continuous or triggered mode.
            Valid options are:
            continuous: capture data in the buffer continuously, regardless of trigger settings. Data may be filtered; see continuous_filter.
            trigger: (default) capture data only after triggered.
        Constants Available: CAPTURE_MODE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_buffers({PacketConfigBuffersConstants.CAPTURE_MODE_CMD : opt})

    supportedIxiaHltapiCommands = {PacketConfigBuffersConstants.ACTION_CMD,
                                   PacketConfigBuffersConstants.CAPTURE_MODE_CMD,
                                   PacketConfigBuffersConstants.PORT_HANDLE_CMD,
                                   PacketConfigBuffersConstants.CONTINUOUS_FILTER_CMD,
                                   PacketConfigBuffersConstants.AFTER_TRIGGER_CMD,
                                   PacketConfigBuffersConstants.CONTROL_PLANE_CAPTURE_ENABLE_CMD}
