from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfInfoApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_info
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfInfoConstants.EXECUTION_TIMEOUT_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfInfoConstants.HANDLE_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfInfoConstants.MODE_CMD] = EmulationOspfInfoConstants.MODE_CYCLIC # constant value
        dummyDict[EmulationOspfInfoConstants.PORT_HANDLE_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfInfoConstants.SESSION_TYPE_CMD] = EmulationOspfInfoConstants.SESSION_TYPE_OSPFV2 # constant value

        api = device.getApi(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API)
        assert isinstance(api, EmulationOspfInfoApi)
        api.emulation_ospf_info(dummyDict)
    """
    def emulation_ospf_info(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_info", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_info_execution_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_info_handle(self, any):
        """
        This is the method the command: emulation_ospf_info option handle
        Description:The routers from which to extract OSPF data. One of the two parameters
            is required: port_handle/handle.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The routers from which to extract OSPF data. One of the two parameters
            is required: port_handle/handle.
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_info({EmulationOspfInfoConstants.HANDLE_CMD : any})

    def emulation_ospf_info_mode(self, opt):
        """
        This is the method the command: emulation_ospf_info option mode
        Description:aggregate_stats - retrieve stats aggregated per port/handlelearned_info
            - retrieve learned information by the OSPF protocolclear_stats - clear stats
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            The action that should be taken.
            Valid options are:
            aggregate_stats

            retrieve stats aggregated per port/handle
            learned_info

            retrieve learned information by the OSPF protocol
            clear_stats

            clear stats
            session

            retrieves non-aggregated stats per handle
            DEFAULT
                None
        Constants Available: MODE_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_info({EmulationOspfInfoConstants.MODE_CMD : opt})

    def emulation_ospf_info_port_handle(self, any):
        """
        This is the method the command: emulation_ospf_info option port_handle
        Description:The port from which to extract OSPF data. One of the two parameters is
            required: port_handle/handle.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            The port from which to extract OSPF data. One of the two parameters is
            required: port_handle/handle.
            DEFAULT
                None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_info({EmulationOspfInfoConstants.PORT_HANDLE_CMD : any})

    def emulation_ospf_info_session_type(self, opt):
        return self.logger.log_unimplemented_method()


"""
    This is the Constants class for the command: emulation_ospf_info
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfInfoConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_INFO_API = "EMULATION_OSPF_INFO_API"

    EXECUTION_TIMEOUT_CMD = "execution_timeout"

    HANDLE_CMD = "handle"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CYCLIC = "CYCLIC"
    MODE_REF = "REF"
    MODE_AGGREGATE_STATS = "aggregate_stats"
    MODE_CLEAR_STATS = "clear_stats"
    MODE_LEARNED_INFO = "learned_info"
    MODE_SESSION = "session"

    PORT_HANDLE_CMD = "port_handle"

    SESSION_TYPE_CMD = "session_type"
    # Constant values for SESSION_TYPE_CMD
    SESSION_TYPE_OSPFV2 = "ospfv2"
    SESSION_TYPE_OSPFV3 = "ospfv3"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -execution_timeout
    -handle
    -mode
    -port_handle
    -session_type
If you want to update this file, look in the CSV
"""
