from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi

"""
    This is the API class for the command: emulation_bgp_info
"""


class EmulationBgpInfoApi(TrafficGenerationApi):
    """
    init function
    """

    def __init__(self, device):
        TrafficGenerationApi.__init__(self, device)

    """
    This is the "One Large Method" for the command: emulation_bgp_info
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationBgpInfoConstants._CMD] = "dummyValue1" # static value
        dummyDict[EmulationBgpInfoConstants.ARGUMENTS_CMD] = EmulationBgpInfoConstants.ARGUMENTS_CONSTANTS # constant value
        dummyDict[EmulationBgpInfoConstants.HANDLE_CMD] = "dummyValue3" # static value
        dummyDict[EmulationBgpInfoConstants.MODE_CMD] = EmulationBgpInfoConstants.MODE_STATS # constant value

        api = device.getApi(EmulationBgpInfoConstants.EMULATION_BGP_INFO_API)
        api.emulation_bgp_info(dummyDict)
    """

    def emulation_bgp_info(self, argdictionary):
        return self.send_command_args(self._nameSpace + "::emulation_bgp_info", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    def emulation_bgp_info_(self):
        """
        This is the method the command: emulation_bgp_info option
        Constants Available: _CMD
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_bgp_info({EmulationBgpInfoConstants._CMD: ""})

    def emulation_bgp_info_Arguments(self, parameter):
        """
        This is the method the command: emulation_bgp_info option Arguments
        Description:Description
        Constants Available: ARGUMENTS_CMD
        Supported:Supported
        Keyword arguments:
        parameter --
        return -- pass/fail
        """
        return self.emulation_bgp_info({EmulationBgpInfoConstants.ARGUMENTS_CMD: parameter})

    def emulation_bgp_info_handle(self, string):
        """
        This is the method the command: emulation_bgp_info option handle
        Description:Supported platforms  Details

            IxNetwork-NGPF [M]


            DESCRIPTION


            The BGP session handle or L3 Site handle or L2 Site handle.

            DEFAULT
             None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_info({EmulationBgpInfoConstants.HANDLE_CMD: string})

    def emulation_bgp_info_mode(self, opt):
        """
        This is the method the command: emulation_bgp_info option mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT [M]


            Same as IxNetwork.

            IxNetwork [M]


            DESCRIPTION


            Specifies action to be taken. Valid choices are:

            Valid options are:

            stats


            returns Tx and Rx statistics of different BGP messages.

            clear_stats


            clears Tx and Rx statistics of different BGP messages.

            settings


            returns tester IP address and AS number.

            neighbors


            returns SUT IP address.

            labels


            returns MPLS label information like label, network, next_hop, prefix_len, distinguisher (only for MPLS VPN), version(ipV4|ipV6), type (mpls|mplsVpn)

            DEFAULT
             None

            IxNetwork-NGPF [M]


            DESCRIPTION


            Specifies action to be taken on the BGP or BGP+ Peer handle

            Valid options are:

            stats


            returns Tx and Rx statistics of different BGP messages.

            stats_per_device_group


            returns Tx and Rx statistics of different BGP messages per device group.

            clear_stats


            clears Tx and Rx statistics of different BGP messages.

            settings


            returns tester IP address and AS number.

            neighbors


            returns SUT IP address.

            session


            retrieves non-aggregated stats per handle.

            labels


            returns MPLS label information like label, network, next_hop, prefix_len, distinguisher (only for MPLS VPN), version(ipV4|ipV6), type (mpls|mplsVpn)

            learned_info


            retrieve learned information by the BGP protocol

            clear_learned_info


            clears the learned information by the BGP protocol

            DEFAULT
             None
        Constants Available: MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_info({EmulationBgpInfoConstants.MODE_CMD: opt})


"""
    This is the Constants class for the command: emulation_bgp_info
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationBgpInfoConstants:
    """
    init function
    """

    def __init__(self):
        pass

    # api reference constant for this api to get it from the device
    EMULATION_BGP_INFO_API = "EMULATION_BGP_INFO_API"

    _CMD = ""

    ARGUMENTS_CMD = "Arguments"
    # Constant values for ARGUMENTS_CMD
    ARGUMENTS_CONSTANTS = "Constants"

    HANDLE_CMD = "handle"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_STATS = "stats"
    MODE_CLEAR_STATS_SETTINGS = "clear_stats settings"
    MODE_SESSION_NEIGHBORS = "session neighbors"
    MODE_LABELS = "labels"
    MODE_LEARNED_INFO = "learned_info"
    MODE_CLEAR_LEARNED_INFO = "clear_learned_info"
    MODE_STATS_PER_DEVICE_GROUP = "stats_per_device_group"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


# instantiate the class to access the constants
#   example EmulationBgpInfoConstants.ARGUMENTS
EmulationBgpInfoConstants = EmulationBgpInfoConstants()

"""
Implemented Commands (Alphabetical)
    -
    -Arguments
    -handle
    -mode

Use this to regenerate this class in the devhelper

<?xml version="1.0" encoding="UTF-8"?>
<xml feature="emulation_bgp_info">
  <cmd name="Arguments">
    <description>Description</description>
    <param>Parameter</param>
    <constantlist>Constants</constantlist>
    <supported>Supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="mode">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT [M]


Same as IxNetwork.

IxNetwork [M]


DESCRIPTION


Specifies action to be taken. Valid choices are:

Valid options are:

stats


returns Tx and Rx statistics of different BGP messages.

clear_stats


clears Tx and Rx statistics of different BGP messages.

settings


returns tester IP address and AS number.

neighbors


returns SUT IP address.

labels


returns MPLS label information like label, network, next_hop, prefix_len, distinguisher (only for MPLS VPN), version(ipV4|ipV6), type (mpls|mplsVpn)

DEFAULT
 None

IxNetwork-NGPF [M]


DESCRIPTION


Specifies action to be taken on the BGP or BGP+ Peer handle

Valid options are:

stats


returns Tx and Rx statistics of different BGP messages.

stats_per_device_group


returns Tx and Rx statistics of different BGP messages per device group.

clear_stats


clears Tx and Rx statistics of different BGP messages.

settings


returns tester IP address and AS number.

neighbors


returns SUT IP address.

session


retrieves non-aggregated stats per handle.

labels


returns MPLS label information like label, network, next_hop, prefix_len, distinguisher (only for MPLS VPN), version(ipV4|ipV6), type (mpls|mplsVpn)

learned_info


retrieve learned information by the BGP protocol

clear_learned_info


clears the learned information by the BGP protocol

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>stats,clear_stats settings,session neighbors,labels,learned_info,clear_learned_info,stats_per_device_group</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="handle">
    <description>Supported platforms  Details

IxNetwork-NGPF [M]


DESCRIPTION


The BGP session handle or L3 Site handle or L2 Site handle.

DEFAULT
 None</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="">
    <description/>
    <param/>
    <constantlist/>
    <supported/>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
</xml>

"""
