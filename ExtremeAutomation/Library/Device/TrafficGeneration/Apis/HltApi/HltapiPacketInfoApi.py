from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: packet_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class PacketInfoApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(PacketInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_info
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[PacketInfoConstants.ACTION_CMD] = PacketInfoConstants.ACTION_STATUS # constant value
        dummyDict[PacketInfoConstants.PORT_HANDLE_CMD] = "dummyValue2" # static value

        api = device.getApi(PacketInfoConstants.PACKET_INFO_API)
        assert isinstance(api, PacketInfoApi)
        api.packet_info(dummyDict)
    """
    def packet_info(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::packet_info", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_info_action(self, opt):
        """
        This is the method the command: packet_info option action
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
        return self.packet_info({PacketInfoConstants.ACTION_CMD : opt})

    def packet_info_port_handle(self, port):
        """
        This is the method the command: packet_info option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.packet_info({PacketInfoConstants.PORT_HANDLE_CMD : port})


"""
    This is the Constants class for the command: packet_info
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class PacketInfoConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    PACKET_INFO_API = "PACKET_INFO_API"

    ACTION_CMD = "action"
    # Constant values for ACTION_CMD
    ACTION_STATUS = "status"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -action
    -port_handle
If you want to update this file, look in the CSV
"""
