from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketControlApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_control
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketControlConstants.ACTION_CMD] = PacketControlConstants.ACTION_START # constant value
        dummyDict[PacketControlConstants.PACKET_TYPE_CMD] = PacketControlConstants.PACKET_TYPE_START # constant value
        dummyDict[PacketControlConstants.PORT_HANDLE_CMD] = "dummyValue3" # static value

        api = device.getApi(PacketControlConstants.PACKET_CONTROL_API)
        api.packet_control(dummyDict)
    """
    def packet_control(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_control", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_control_action(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_control_packet_type(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_control_port_handle(self, port):
        """
        This is the method the command: packet_control option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_control({PacketControlConstants.PORT_HANDLE_CMD : port})


"""
    This is the Constants class for the command: packet_control
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketControlConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_CONTROL_API = "PACKET_CONTROL_API"

    ACTION_CMD = "action"
    # Constant values for ACTION_CMD
    ACTION_START = "start"
    ACTION_STOP = "stop"
    ACTION_RESET = "reset"
    ACTION_CUMULATIVE_START = "cumulative_start"

    PACKET_TYPE_CMD = "packet_type"
    # Constant values for PACKET_TYPE_CMD
    PACKET_TYPE_START = "start"
    PACKET_TYPE_STOP = "stop"
    PACKET_TYPE_RESET = "reset"
    PACKET_TYPE_CUMULATIVE_START = "cumulative_start"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -action
    -packet_type
    -port_handle
If you want to update this file, look in the CSV
"""
