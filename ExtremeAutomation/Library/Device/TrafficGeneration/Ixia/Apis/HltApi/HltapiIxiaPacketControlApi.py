from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketControlApi import PacketControlApi, PacketControlConstants

"""
    This is the API class for the command: packet_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketControlApi(PacketControlApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_control
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketControlConstants.PACKET_CONTROL_API)
        api.packet_control(dummyDict)
    """
    def packet_control(self, argdictionary):
        return super(IxiaPacketControlApi, self).packet_control(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_control_action(self, opt):
        """
        This is the method the command: packet_control option action
        Description:Not defined
            Valid options are:
            start: Closes in progres captures and starts packet capturing on the specified port_handle.
            cumulative_start: Starts packet capturing on the specified port_handle. In progress captures remain started.
            stop: Stop packet capturing
            reset: Reset the filters and triggers to the default values
        Constants Available: ACTION_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_control({PacketControlConstants.ACTION_CMD : opt})

    def packet_control_packet_type(self, opt):
        """
        This is the method the command: packet_control option packet_type
        Description:Not defined
            Valid options are:
            both: (DEFAULT) both control and data frames will be captured
            control: only control frames will be captured
            data: only data frames will be captured
        Constants Available: PACKET_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_control({PacketControlConstants.PACKET_TYPE_CMD : opt})


    supportedIxiaHltapiCommands = {PacketControlConstants.ACTION_CMD, PacketControlConstants.PACKET_TYPE_CMD, PacketControlConstants.PORT_HANDLE_CMD}
