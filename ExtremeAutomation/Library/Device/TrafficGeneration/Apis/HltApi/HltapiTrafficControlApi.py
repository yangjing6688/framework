from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: traffic_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class TrafficControlApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(TrafficControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_control
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[TrafficControlConstants.ACTION_CMD] = TrafficControlConstants.ACTION_SYNC_RUN # constant value
        dummyDict[TrafficControlConstants.LATENCY_ENABLE_CMD] = "dummyValue2" # static value
        dummyDict[TrafficControlConstants.LATENCY_VALUES_CMD] = "dummyValue3" # static value
        dummyDict[TrafficControlConstants.PORT_HANDLE_CMD] = "dummyValue4" # static value

        api = device.getApi(TrafficControlConstants.TRAFFIC_CONTROL_API)
        api.traffic_control(dummyDict)
    """
    def traffic_control(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::traffic_control", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_control_action(self, opt):
        """
        This is the method the command: traffic_control option action
        Description:Action to take. Valid choices are:
            Valid options are:
            sync_run: Action sync_run performs both actions: clear_stats and start traffic. This option should be used, when per stream stats or packet group stats need to be retrieved. If this option is used with large IxNetwork configs, it takes some time to configure the traffic and apply the traffic to the Ixia port. In this case, the sync_run option should be used with -max_wait_timer.If used with the handle argument it will start only the traffic sources specified by handle. If the type argument is not used, l23 traffic will be started.
            run: Starts the generators and all configured traffic sources (starts traffic). If this option is used with large IxNetwork configs, it takes some time to configure the traffic and apply the traffic to the Ixia port. In this case, the run option should be used with -max_wait_timer (usually takes less than 120 seconds).If used with the handle argument it will start only the traffic sources specified by handle. If the type argument is not used, l23 traffic will be started.This choice is valid with IxNetwork traffic generators.
            stop: Stops the generators. If used with the handle argument it will start only the traffic sources specified by handle. If the type argument is not used, l23 traffic will be started.This choice is valid with IxNetwork traffic generators. <br/>Note: Add a time delay after the traffic stop call, before doing other things such as cleanup or modify configuration. Stopping a classic protocol usually takes less than 10 seconds; stopping traffic takes about 30 seconds.
            poll: Polls the generators to determine whether they are stopped or running. This choice is valid with IxNetwork traffic generators. <br/>Note: If action -poll is issued immediately after action -start, then the poll action may return stopped 1 when the correct status should be stopped 0. This happens when the chassis is very busy. Adding a little delay (one second) between -action start and -action poll call should resolve this problem.
            reset: Clears generators to power up state and clears all traffic sources.
            destroy: Destroys the generators.
            clear_stats: Clears all stats and timestamps.
            regenerate: Regenerates traffic items. If the argument handle is not used, all traffic items will be regenerated. Valid only for traffic generator ixnetwork_540.
            apply: Applies traffic configuration to the Ixia ports. If the argument type is not used, l23 traffic will be applied.Valid only for traffic generator ixnetwork_540.
        Constants Available: ACTION_CMD
        Supported:IxOS/IxNetwork-FT [M], IxNetwork [M]
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_control({TrafficControlConstants.ACTION_CMD : opt})

    def traffic_control_latency_enable(self, opt):
        """
        This is the method the command: traffic_control option latency_enable
        Description:This options enables or disables latency statistics in the global traffic options.
            Valid options are:
            0: Disable latency statistics
            1: Enable latency statistics
        Constants Available: LATENCY_ENABLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_control({TrafficControlConstants.LATENCY_ENABLE_CMD : opt})

    def traffic_control_latency_values(self, opt):
        """
        This is the method the command: traffic_control option latency_values
        Description:The splitting values for the bins. 0 and Max will be the absolute end points. A list of {1.5 3 6.8} would create these four bins {0 - 1.5} {1.5 3} {3 6.8} {6.8 MAX}. Latency statistics, in the global traffic options, will be enabled. This parameter takes effect only if used in combination with the latency_bins argument.
        Constants Available: LATENCY_VALUES_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_control({TrafficControlConstants.LATENCY_VALUES_CMD : opt})

    def traffic_control_port_handle(self, port):
        """
        This is the method the command: traffic_control option port_handle
        Description:Depending on the traffic_generator value, this option has different meanings. If traffic_generator ixnetwork_540 is used this parameter is used ixos/ixnetwork_540 - The port for which to configure traffic. Mandatory for -mode create/reset when -traffic_generator is set to ixos. For traffic_generator ixnetwork_540 this is mandatory on mode create only if parameter -emulation_src_handle is missing.ixnetwork/ixnetwork_540 - The port_handle parameter is not necessary anymore. When using IxNetwork, traffic configurations will be done using previously created handles (IP interfaces, PPP ranges, L2TP ranges, Protocol Route Ranges etc.) as sources (parameter -emulation_src_handle) and destinations (-emulation_dst_handle).
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        port --
        return -- pass/fail
        """
        return self.traffic_control({TrafficControlConstants.PORT_HANDLE_CMD : port})


"""
    This is the Constants class for the command: traffic_control
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class TrafficControlConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_CONTROL_API = "TRAFFIC_CONTROL_API"

    ACTION_CMD = "action"
    # Constant values for ACTION_CMD
    ACTION_SYNC_RUN = "sync_run"
    ACTION_RUN = "run"
    ACTION_MANUAL_TRIGGER = "manual_trigger"
    ACTION_STOP = "stop"
    ACTION_POLL = "poll"
    ACTION_RESET = "reset"
    ACTION_DESTROY = "destroy"
    ACTION_CLEAR_STATS = "clear_stats"
    ACTION_REGENERATE = "regenerate"
    ACTION_APPLY = "apply"

    LATENCY_ENABLE_CMD = "latency_enable"

    LATENCY_VALUES_CMD = "latency_values"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -action
    -latency_enable
    -latency_values
    -port_handle
If you want to update this file, look in the CSV
"""
