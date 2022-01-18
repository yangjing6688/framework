from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: reset_port

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class ResetPortApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(ResetPortApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: reset_port
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[ResetPortConstants.MODE_CMD] = ResetPortConstants.MODE_SET_FACTORY_DEFAULTS # constant value
        dummyDict[ResetPortConstants.PORT_HANDLE_CMD] = "dummyValue2" # static value
        dummyDict[ResetPortConstants.PROTOCOL_CMD] = ResetPortConstants.PROTOCOL_BFD # constant value

        api = device.getApi(ResetPortConstants.RESET_PORT_API)
        api.reset_port(dummyDict)
    """
    def reset_port(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::reset_port", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def reset_port_mode(self, opt):
        """
        This is the method the command: reset_port option mode
        Description:List ofAction to be taken on the port_handle selected.
            Valid options are:
            set_factory_defaults: resets the port to factory default.
            remove_protocol: removes the protocol config on the port specified by the protocol argument
        Constants Available: MODE_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M], IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.reset_port({ResetPortConstants.MODE_CMD : opt})

    def reset_port_port_handle(self, port_string):
        """
        This is the method the command: reset_port option port_handle
        Description:List of port_handles on which to act
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M], IxNetwork-NGPF
        Keyword arguments:
        port_string --
        return -- pass/fail
        """
        return self.reset_port({ResetPortConstants.PORT_HANDLE_CMD : port_string})

    def reset_port_protocol(self, opt):
        """
        This is the method the command: reset_port option protocol
        Constants Available: PROTOCOL_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M], IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.reset_port({ResetPortConstants.PROTOCOL_CMD : opt})


"""
    This is the Constants class for the command: reset_port
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class ResetPortConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    RESET_PORT_API = "RESET_PORT_API"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_SET_FACTORY_DEFAULTS = "set_factory_defaults"
    MODE_REMOVE_PROTOCOL = "remove_protocol"

    PORT_HANDLE_CMD = "port_handle"

    PROTOCOL_CMD = "protocol"
    # Constant values for PROTOCOL_CMD
    PROTOCOL_BFD = "bfd"
    PROTOCOL_BGP = "bgp"
    PROTOCOL_CFM = "cfm"
    PROTOCOL_EIGRP = "eigrp"
    PROTOCOL_IGMP = "igmp"
    PROTOCOL_ISIS = "isis"
    PROTOCOL_LACP = "lacp"
    PROTOCOL_LDP = "ldp"
    PROTOCOL_EFM = "efm"
    PROTOCOL_MLD = "mld"
    PROTOCOL_MPLSTP = "mplstp"
    PROTOCOL_OSPFV2 = "ospfv2"
    PROTOCOL_OSPFV3 = "ospfv3"
    PROTOCOL_PIM = "pim"
    PROTOCOL_RIP = "rip"
    PROTOCOL_RIPNG = "ripng"
    PROTOCOL_RSVP = "rsvp"
    PROTOCOL_STATIC = "static"
    PROTOCOL_STP = "stp"
    PROTOCOL_ALL = "all"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -mode
    -port_handle
    -protocol
If you want to update this file, look in the CSV
"""
