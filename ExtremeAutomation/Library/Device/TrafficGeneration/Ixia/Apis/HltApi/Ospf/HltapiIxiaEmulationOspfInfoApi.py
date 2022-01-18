from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfInfoApi import EmulationOspfInfoApi, EmulationOspfInfoConstants

"""
    This is the API class for the command: emulation_ospf_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaEmulationOspfInfoApi(EmulationOspfInfoApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaEmulationOspfInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_info
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API)
        assert isinstance(api, EmulationOspfInfoApi)
        api.emulation_ospf_info(dummyDict)
    """
    def emulation_ospf_info(self, argdictionary):
        return super(IxiaEmulationOspfInfoApi, self).emulation_ospf_info(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_info_execution_timeout(self, numeric):
        """
        This is the method the command: emulation_ospf_info option execution_timeout
        Description:This is the timeout for the function. The setting is in seconds. Setting
            this setting to 60 it will mean that the command must complete in under
            60 seconds. If the command will last more than 60 seconds the command
            will be terminated by force. This flag can be used to prevent dead locks
            occuring in IxNetwork.
            DEFAULT

            1800
        Constants Available: EXECUTION_TIMEOUT_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.emulation_ospf_info({EmulationOspfInfoConstants.EXECUTION_TIMEOUT_CMD : numeric})

    def emulation_ospf_info_session_type(self, opt):
        """
        This is the method the command: emulation_ospf_info option session_type
        Description:The Type of OSPF Router - OSPFv2 or OSPFv3.
            Valid options are:
            ospfv2

            OSPF v2
            ospfv3

            OSPF v3
            DEFAULT

            ospfv2
        Constants Available: SESSION_TYPE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.emulation_ospf_info({EmulationOspfInfoConstants.SESSION_TYPE_CMD : opt})


    supportedIxiaHltapiCommands = {EmulationOspfInfoConstants.EXECUTION_TIMEOUT_CMD, EmulationOspfInfoConstants.HANDLE_CMD, EmulationOspfInfoConstants.MODE_CMD, EmulationOspfInfoConstants.PORT_HANDLE_CMD, EmulationOspfInfoConstants.SESSION_TYPE_CMD}
