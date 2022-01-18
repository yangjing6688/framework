from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfInfoApi import EmulationOspfInfoApi, EmulationOspfInfoConstants

"""
    This is the API class for the command: emulation_ospf_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentEmulationOspfInfoApi(EmulationOspfInfoApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentEmulationOspfInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: emulation_ospf_info
    use this by passing in a dict() of all the commands

        api = device.getApi(EmulationOspfInfoConstants.EMULATION_OSPF_INFO_API)
        assert isinstance(api, EmulationOspfInfoApi)
        api.emulation_ospf_info(dummyDict)
    """
    def emulation_ospf_info(self, argdictionary):
        return super(SpirentEmulationOspfInfoApi, self).emulation_ospf_info(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def emulation_ospf_info_execution_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def emulation_ospf_info_session_type(self, opt):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {EmulationOspfInfoConstants.HANDLE_CMD, EmulationOspfInfoConstants.MODE_CMD, EmulationOspfInfoConstants.PORT_HANDLE_CMD}
