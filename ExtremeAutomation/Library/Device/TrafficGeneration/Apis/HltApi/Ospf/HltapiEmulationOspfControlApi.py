from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: emulation_ospf_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class EmulationOspfControlApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(EmulationOspfControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_control
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[EmulationOspfControlConstants.ADVERTISE_CMD] = "dummyValue1" # static value
        dummyDict[EmulationOspfControlConstants.ADVERTISE_LSA_CMD] = "dummyValue2" # static value
        dummyDict[EmulationOspfControlConstants.AGE_OUT_PERCENT_CMD] = "dummyValue3" # static value
        dummyDict[EmulationOspfControlConstants.FLAP_COUNT_CMD] = "dummyValue4" # static value
        dummyDict[EmulationOspfControlConstants.FLAP_DOWN_TIME_CMD] = "dummyValue5" # static value
        dummyDict[EmulationOspfControlConstants.FLAP_INTERVAL_TIME_CMD] = "dummyValue6" # static value
        dummyDict[EmulationOspfControlConstants.FLAP_LSA_CMD] = "dummyValue7" # static value
        dummyDict[EmulationOspfControlConstants.FLAP_ROUTES_CMD] = "dummyValue8" # static value
        dummyDict[EmulationOspfControlConstants.HANDLE_CMD] = "dummyValue9" # static value
        dummyDict[EmulationOspfControlConstants.MODE_CMD] = EmulationOspfControlConstants.MODE_ABORT # constant value
        dummyDict[EmulationOspfControlConstants.PORT_HANDLE_CMD] = "dummyValue11" # static value
        dummyDict[EmulationOspfControlConstants.WITHDRAW_CMD] = "dummyValue12" # static value
        dummyDict[EmulationOspfControlConstants.WITHDRAW_LSA_CMD] = "dummyValue13" # static value

        api = device.getApi(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API)
        assert isinstance(api, EmulationOspfControlApi)
        api.emulation_ospf_control(dummyDict)
    """
    def emulation_ospf_control(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::emulation_ospf_control", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_control_advertise(self, any):
        """
        This is the method the command: emulation_ospf_control option advertise
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: ADVERTISE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.ADVERTISE_CMD : any})

    def emulation_ospf_control_advertise_lsa(self, any):
        """
        This is the method the command: emulation_ospf_control option advertise_lsa
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: ADVERTISE_LSA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.ADVERTISE_LSA_CMD : any})

    def emulation_ospf_control_age_out_percent(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_control_flap_count(self, any):
        """
        This is the method the command: emulation_ospf_control option flap_count
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: FLAP_COUNT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.FLAP_COUNT_CMD : any})

    def emulation_ospf_control_flap_down_time(self, any):
        """
        This is the method the command: emulation_ospf_control option flap_down_time
        Description:Not defined
            DEFAULT
                None
        Constants Available: FLAP_DOWN_TIME_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.FLAP_DOWN_TIME_CMD : any})

    def emulation_ospf_control_flap_interval_time(self, any):
        """
        This is the method the command: emulation_ospf_control option flap_interval_time
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: FLAP_INTERVAL_TIME_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.FLAP_INTERVAL_TIME_CMD : any})

    def emulation_ospf_control_flap_lsa(self, any):
        """
        This is the method the command: emulation_ospf_control option flap_lsa
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: FLAP_LSA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.FLAP_LSA_CMD : any})

    def emulation_ospf_control_flap_routes(self, any):
        """
        This is the method the command: emulation_ospf_control option flap_routes
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: FLAP_ROUTES_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.FLAP_ROUTES_CMD : any})

    def emulation_ospf_control_handle(self, any):
        """
        This is the method the command: emulation_ospf_control option handle
        Description:This option represents the handle the user *must* pass to the
            'emulation_ospf_control' procedure. This option specifies on which OSPF
            session to control. If port_handle option is present, the port_handle
            takes precedence over port in the router handle. The OSPF router
            handle(s) is returned by the procedure
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            This option represents the handle the user *must* pass to the
            'emulation_ospf_control' procedure. This option specifies on which OSPF
            session to control. If port_handle option is present, the port_handle
            takes precedence over port in the router handle. The OSPF router
            handle(s) is returned by the procedure
            DEFAULT
                None
        Constants Available: HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.HANDLE_CMD : any})

    def emulation_ospf_control_mode(self, opt):
        """
        This is the method the command: emulation_ospf_control option mode
        Description:Tells which option will be performed on the OSPF protocol. Valid options
            are:restartstartstop
            DEFAULT
                None
            IxNetwork-NGPF[M]

            DESCRIPTION

            Tells which option will be performed on the OSPF protocol. Valid options
            are: restart start stop abort restart_down resume_hello stop_hello
            age_out_routes readvertise_routes advertise withdraw disconnect reconnect
            Valid options are:
            start

            stop

            restart

            abort

            restart_down

            resume_hello

            stop_hello

            age_out_routes

            readvertise_routes

            advertise

            withdraw

            disconnect

            reconnect

            DEFAULT
                None
        Constants Available: MODE_CMD
        Supported:IxNetwork[M] , IxOS/IxNetwork-FT[M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.MODE_CMD : opt})

    def emulation_ospf_control_port_handle(self, any):
        """
        This is the method the command: emulation_ospf_control option port_handle
        Description:A list of ports on which to control the OSPF protocol. If this option is
            not present, the port in the handle option will be applied.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            A list of ports on which to control the OSPF protocol. If this option is
            not present, the port in the handle option will be applied.
            DEFAULT
                None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.PORT_HANDLE_CMD : any})

    def emulation_ospf_control_withdraw(self, any):
        """
        This is the method the command: emulation_ospf_control option withdraw
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: WITHDRAW_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.WITHDRAW_CMD : any})

    def emulation_ospf_control_withdraw_lsa(self):
        """
        This is the method the command: emulation_ospf_control option withdraw_lsa
        Constants Available: WITHDRAW_LSA_CMD
        Supported:Supported platforms     Details
        Keyword arguments:
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.WITHDRAW_LSA_CMD : ""})


"""
    This is the Constants class for the command: emulation_ospf_control
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class EmulationOspfControlConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    EMULATION_OSPF_CONTROL_API = "EMULATION_OSPF_CONTROL_API"

    ADVERTISE_CMD = "advertise"

    ADVERTISE_LSA_CMD = "advertise_lsa"

    AGE_OUT_PERCENT_CMD = "age_out_percent"

    FLAP_COUNT_CMD = "flap_count"

    FLAP_DOWN_TIME_CMD = "flap_down_time"

    FLAP_INTERVAL_TIME_CMD = "flap_interval_time"

    FLAP_LSA_CMD = "flap_lsa"

    FLAP_ROUTES_CMD = "flap_routes"

    HANDLE_CMD = "handle"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_ABORT = "abort"
    MODE_ADVERTISE = "advertise"
    MODE_AGE_OUT_ROUTES = "age_out_routes"
    MODE_DISCONNECT = "disconnect"
    MODE_READVERTISE_ROUTES = "readvertise_routes"
    MODE_RECONNECT = "reconnect"
    MODE_RESTART = "restart"
    MODE_RESTART_DOWN = "restart_down"
    MODE_RESUME_HELLO = "resume_hello"
    MODE_START = "start"
    MODE_STOP = "stop"
    MODE_STOP_HELLO = "stop_hello"
    MODE_WITHDRAW = "withdraw"

    PORT_HANDLE_CMD = "port_handle"

    WITHDRAW_CMD = "withdraw"

    WITHDRAW_LSA_CMD = "withdraw_lsa"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -advertise
    -advertise_lsa
    -age_out_percent
    -flap_count
    -flap_down_time
    -flap_interval_time
    -flap_lsa
    -flap_routes
    -handle
    -mode
    -port_handle
    -withdraw
    -withdraw_lsa
If you want to update this file, look in the CSV
"""
