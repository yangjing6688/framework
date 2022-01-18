from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_config_buffers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketConfigBuffersApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketConfigBuffersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_buffers
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketConfigBuffersConstants.ACTION_CMD] = PacketConfigBuffersConstants.ACTION_WRAP # constant value
        dummyDict[PacketConfigBuffersConstants.CAPTURE_MODE_CMD] = PacketConfigBuffersConstants.CAPTURE_MODE_CONTINUOUS # constant value
        dummyDict[PacketConfigBuffersConstants.PORT_HANDLE_CMD] = "dummyValue3" # static value

        api = device.getApi(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API)
        api.packet_config_buffers(dummyDict)
    """
    def packet_config_buffers(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_config_buffers", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_buffers_action(self, opt):
        """
        This is the method the command: packet_config_buffers option action
        Description:Supported with IxTclHal. Controls the action of the buffer when it reaches the full status. Not supported with IxTclNetwork and warning will be printed on stdout if this parameter is used.DEFAULT: wrap
        Constants Available: ACTION_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_buffers({PacketConfigBuffersConstants.ACTION_CMD : opt})

    def packet_config_buffers_capture_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_buffers_port_handle(self, port):
        """
        This is the method the command: packet_config_buffers option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_config_buffers({PacketConfigBuffersConstants.PORT_HANDLE_CMD : port})


"""
    This is the Constants class for the command: packet_config_buffers
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketConfigBuffersConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_CONFIG_BUFFERS_API = "PACKET_CONFIG_BUFFERS_API"

    ACTION_CMD = "action"
    # Constant values for ACTION_CMD
    ACTION_WRAP = "wrap"
    ACTION_STOP = "stop"

    CAPTURE_MODE_CMD = "capture_mode"
    # Constant values for CAPTURE_MODE_CMD
    CAPTURE_MODE_CONTINUOUS = "continuous"
    CAPTURE_MODE_TRIGGER = "trigger"

    PORT_HANDLE_CMD = "port_handle"

    CONTROL_PLANE_CAPTURE_ENABLE_CMD = "control_plane_capture_enable"

    AFTER_TRIGGER_CMD = "after_trigger"
    AFTER_TRIGGER_FILTER = "filter"

    CONTINUOUS_FILTER_CMD = "continuous_filter"
    CONTINUOUS_FILTER_ALL = "all"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -action
    -capture_mode
    -port_handle
If you want to update this file, look in the CSV
"""
