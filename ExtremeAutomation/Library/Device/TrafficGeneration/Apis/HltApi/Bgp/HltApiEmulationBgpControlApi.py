from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi

"""
    This is the API class for the command: emulation_bgp_control
"""


class EmulationBgpControlApi(TrafficGenerationApi):
    """
    init function
    """

    def __init__(self, device):
        TrafficGenerationApi.__init__(self, device)

    """
    This is the "One Large Method" for the command: emulation_bgp_control
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationBgpControlConstants.ARGUMENTS_CMD] = EmulationBgpControlConstants.ARGUMENTS_CONSTANTS # constant value
        dummyDict[EmulationBgpControlConstants.HANDLE_CMD] = "dummyValue2" # static value
        dummyDict[EmulationBgpControlConstants.LINK_FLAP_DOWN_TIME_CMD] = "dummyValue3" # static value
        dummyDict[EmulationBgpControlConstants.LINK_FLAP_UP_TIME_CMD] = "dummyValue4" # static value
        dummyDict[EmulationBgpControlConstants.MODE_CMD] = EmulationBgpControlConstants.MODE_LINK_FLAP # constant value
        dummyDict[EmulationBgpControlConstants.NOTIFICATION_CODE_CMD] = "dummyValue6" # static value
        dummyDict[EmulationBgpControlConstants.NOTIFICATION_SUB_CODE_CMD] = "dummyValue7" # static value
        dummyDict[EmulationBgpControlConstants.PORT_HANDLE_CMD] = "dummyValue8" # static value

        api = device.getApi(EmulationBgpControlConstants.EMULATION_BGP_CONTROL_API)
        api.emulation_bgp_control(dummyDict)
    """

    def emulation_bgp_control(self, argdictionary):
        return self.send_command_args(self._nameSpace + "::emulation_bgp_control", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """

    def emulation_bgp_control_Arguments(self, parameter):
        """
        This is the method the command: emulation_bgp_control option Arguments
        Description:Description
        Constants Available: ARGUMENTS_CMD
        Supported:Supported
        Keyword arguments:
        parameter --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.ARGUMENTS_CMD: parameter})

    def emulation_bgp_control_handle(self, string):
        """
        This is the method the command: emulation_bgp_control option handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The BGP session handle.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The BGP session handle.

            DEFAULT
             None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.HANDLE_CMD: string})

    def emulation_bgp_control_link_flap_down_time(self, numeric):
        """
        This is the method the command: emulation_bgp_control option link_flap_down_time
        Description:Supported platforms  Details
            RANGE 0 - 10000000
            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            When mode is link_flap, the amount of time in seconds that the link is disconnected.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            When mode is link_flap, the amount of time in seconds that the link is disconnected.

            DEFAULT
             None

            DEPENDENCIES


            Valid in combination with parameter(s)
            'mode' | value= 'link_flap' |
        Constants Available: LINK_FLAP_DOWN_TIME_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.LINK_FLAP_DOWN_TIME_CMD: numeric})

    def emulation_bgp_control_link_flap_up_time(self, not_supported):
        """
        This is the method the command: emulation_bgp_control option link_flap_up_time
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            When mode is link_flap, the amount of time in seconds that the link is connected.

            DEFAULT
             Not supported

            DEPENDENCIES


            Valid in combination with parameter(s)
            'mode' | value= 'link_flap' |
        Constants Available: LINK_FLAP_UP_TIME_CMD
        Supported:not supported
        Keyword arguments:
        not_supported --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.LINK_FLAP_UP_TIME_CMD: not_supported})

    def emulation_bgp_control_mode(self, opt):
        """
        This is the method the command: emulation_bgp_control option mode
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT [M]


            Same as IxNetwork.

            IxNetwork [M]


            DESCRIPTION


            What is being done to the protocol. Valid choices are:

            Valid options are:

            stop


            stop the protocol

            start


            start the protocol

            restart


            restart the protocol

            link_flap


            turns on and sets the link flapping

            statistic


            enables the retrieval of statistics for a future call of ::<namespace>::emulation_bgp_infowith parameter -mode set to stats(valid only for IxProtocol)

            DEFAULT
             None

            IxNetwork-NGPF [M]


            DESCRIPTION


            What is being done to the protocol..

            Valid options are:

            link_flap


            turns on and sets the link flapping

            restart


            restart the protocol

            abort


            aborts the protcol

            restart_down


            restart the down sessions

            start


            start the protocol

            stop


            stop the protocol

            statistic


            enables the retrieval of statistics for a future call of ::<namespace>::emulation_bgp_info with parameter -mode set to stats(valid only for IxProtocol)

            break_tcp_session


            breaks the tcp session using tcp_session_notification_code and tcp_session_notification_sub_code values

            resume_tcp_session


            resumes the tcp session using tcp_session_notification_code and tcp_session_notification_sub_code values

            resume_keep_alive


            resumes the keep alive

            stop_keep_alive


            stops the keep alive

            DEFAULT
             None
        Constants Available: MODE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.MODE_CMD: opt})

    def emulation_bgp_control_notification_code(self, numeric):
        """
        This is the method the command: emulation_bgp_control option notification_code
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            The notification code for break_tcp_session and resume_tcp_session.

            DEFAULT


            0
        Constants Available: NOTIFICATION_CODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.NOTIFICATION_CODE_CMD: numeric})

    def emulation_bgp_control_notification_sub_code(self, numeric):
        """
        This is the method the command: emulation_bgp_control option notification_sub_code
        Description:Supported platforms  Details

            IxNetwork-NGPF


            DESCRIPTION


            The notification sub code for break_tcp_session and resume_tcp_session.

            DEFAULT


            0
        Constants Available: NOTIFICATION_SUB_CODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.NOTIFICATION_SUB_CODE_CMD: numeric})

    def emulation_bgp_control_port_handle(self, port):
        """
        This is the method the command: emulation_bgp_control option port_handle
        Description:Supported platforms  Details

            IxOS/IxNetwork-FT


            Same as IxNetwork.

            IxNetwork


            DESCRIPTION


            The port on which the BGP neighbor is to be created.

            DEFAULT
             None

            IxNetwork-NGPF


            DESCRIPTION


            The port on which the BGP neighbor is to be created.

            DEFAULT
             None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork,IxNetwork-NGPF
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.emulation_bgp_control({EmulationBgpControlConstants.PORT_HANDLE_CMD: port})


"""
    This is the Constants class for the command: emulation_bgp_control
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationBgpControlConstants:
    """
    init function
    """

    def __init__(self):
        pass

    # api reference constant for this api to get it from the device
    EMULATION_BGP_CONTROL_API = "EMULATION_BGP_CONTROL_API"

    ARGUMENTS_CMD = "Arguments"
    # Constant values for ARGUMENTS_CMD
    ARGUMENTS_CONSTANTS = "Constants"

    HANDLE_CMD = "handle"

    LINK_FLAP_DOWN_TIME_CMD = "link_flap_down_time"

    LINK_FLAP_UP_TIME_CMD = "link_flap_up_time"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_LINK_FLAP = "link_flap"
    MODE_RESTART = "restart"
    MODE_ABORT_RESTART_DOWN = "abort restart_down"
    MODE_START = "start"
    MODE_STOP = "stop"
    MODE_STATISTIC = "statistic"
    MODE_BREAK_TCP_SESSION = "break_tcp_session"
    MODE_RESUME_TCP_SESSION = "resume_tcp_session"
    MODE_RESUME_KEEP_ALIVE = "resume_keep_alive"
    MODE_STOP_KEEP_ALIVE = "stop_keep_alive"

    NOTIFICATION_CODE_CMD = "notification_code"

    NOTIFICATION_SUB_CODE_CMD = "notification_sub_code"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


# instantiate the class to access the constants
#   example EmulationBgpControlConstants.ARGUMENTS
EmulationBgpControlConstants = EmulationBgpControlConstants()

"""
Implemented Commands (Alphabetical)
    -Arguments
    -handle
    -link_flap_down_time
    -link_flap_up_time
    -mode
    -notification_code
    -notification_sub_code
    -port_handle

Use this to regenerate this class in the devhelper

<?xml version="1.0" encoding="UTF-8"?>
<xml feature="emulation_bgp_control">
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


What is being done to the protocol. Valid choices are:

Valid options are:

stop


stop the protocol

start


start the protocol

restart


restart the protocol

link_flap


turns on and sets the link flapping

statistic


enables the retrieval of statistics for a future call of ::&lt;namespace&gt;::emulation_bgp_infowith parameter -mode set to stats(valid only for IxProtocol)

DEFAULT
 None

IxNetwork-NGPF [M]


DESCRIPTION


What is being done to the protocol..

Valid options are:

link_flap


turns on and sets the link flapping

restart


restart the protocol

abort


aborts the protcol

restart_down


restart the down sessions

start


start the protocol

stop


stop the protocol

statistic


enables the retrieval of statistics for a future call of ::&lt;namespace&gt;::emulation_bgp_info with parameter -mode set to stats(valid only for IxProtocol)

break_tcp_session


breaks the tcp session using tcp_session_notification_code and tcp_session_notification_sub_code values

resume_tcp_session


resumes the tcp session using tcp_session_notification_code and tcp_session_notification_sub_code values

resume_keep_alive


resumes the keep alive

stop_keep_alive


stops the keep alive

DEFAULT
 None</description>
    <param>opt</param>
    <constantlist>link_flap,restart,abort restart_down,start,stop,statistic,break_tcp_session,resume_tcp_session,resume_keep_alive,stop_keep_alive</constantlist>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The BGP session handle.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The BGP session handle.

DEFAULT
 None</description>
    <param>STRING</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="notification_code">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


The notification code for break_tcp_session and resume_tcp_session.

DEFAULT


0</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="notification_sub_code">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


The notification sub code for break_tcp_session and resume_tcp_session.

DEFAULT


0</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>ixia_only</supportedPlatform>
  </cmd>
  <cmd name="link_flap_up_time">
    <description>Supported platforms  Details

IxNetwork-NGPF


DESCRIPTION


When mode is link_flap, the amount of time in seconds that the link is connected.

DEFAULT
 Not supported

DEPENDENCIES


Valid in combination with parameter(s)
'mode' | value= 'link_flap' |</description>
    <param>not supported</param>
    <constantlist/>
    <supported>not supported</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>not supported</supportedPlatform>
  </cmd>
  <cmd name="link_flap_down_time">
    <description>Supported platforms  Details
RANGE 0 - 10000000
IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


When mode is link_flap, the amount of time in seconds that the link is disconnected.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


When mode is link_flap, the amount of time in seconds that the link is disconnected.

DEFAULT
 None

DEPENDENCIES


Valid in combination with parameter(s)
'mode' | value= 'link_flap' |</description>
    <param>NUMERIC</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
  <cmd name="port_handle">
    <description>Supported platforms  Details

IxOS/IxNetwork-FT


Same as IxNetwork.

IxNetwork


DESCRIPTION


The port on which the BGP neighbor is to be created.

DEFAULT
 None

IxNetwork-NGPF


DESCRIPTION


The port on which the BGP neighbor is to be created.

DEFAULT
 None</description>
    <param>port</param>
    <constantlist/>
    <supported>IxNetwork,IxNetwork-NGPF</supported>
    <example/>
    <returnvalue/>
    <supportedPlatform>universal</supportedPlatform>
  </cmd>
</xml>

"""
