from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfControlApi import EmulationOspfControlApi, EmulationOspfControlConstants

"""
    This is the API class for the command: emulation_ospf_control

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfControlApi(EmulationOspfControlApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfControlApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_control
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API)
        assert isinstance(api, EmulationOspfControlApi)
        api.emulation_ospf_control(dummyDict)
    """
    def emulation_ospf_control(self, argdictionary):
        return super(IxiaEmulationOspfControlApi, self).emulation_ospf_control(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_control_age_out_percent(self, numeric):
        """
        This is the method the command: emulation_ospf_control option age_out_percent
        Description:The percentage of addresses that will be aged out. This argument is
            ignored when mode is not age_out_routes and *must* be specified in such
            circumstances.
            DEFAULT
                None
        Constants Available: AGE_OUT_PERCENT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_control({EmulationOspfControlConstants.AGE_OUT_PERCENT_CMD : numeric})


    supportedIxiaHltapiCommands = {EmulationOspfControlConstants.ADVERTISE_CMD, EmulationOspfControlConstants.ADVERTISE_LSA_CMD, EmulationOspfControlConstants.AGE_OUT_PERCENT_CMD, EmulationOspfControlConstants.FLAP_COUNT_CMD, EmulationOspfControlConstants.FLAP_DOWN_TIME_CMD, EmulationOspfControlConstants.FLAP_INTERVAL_TIME_CMD, EmulationOspfControlConstants.FLAP_LSA_CMD, EmulationOspfControlConstants.FLAP_ROUTES_CMD, EmulationOspfControlConstants.HANDLE_CMD, EmulationOspfControlConstants.MODE_CMD, EmulationOspfControlConstants.PORT_HANDLE_CMD, EmulationOspfControlConstants.WITHDRAW_CMD, EmulationOspfControlConstants.WITHDRAW_LSA_CMD}
