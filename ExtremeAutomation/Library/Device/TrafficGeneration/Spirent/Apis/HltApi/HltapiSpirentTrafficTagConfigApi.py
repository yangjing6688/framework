from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficTagConfigApi import TrafficTagConfigApi,TrafficTagConfigConstants

"""
    This is the API class for the command: traffic_tag_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentTrafficTagConfigApi(TrafficTagConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentTrafficTagConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_tag_config
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API)
        api.traffic_tag_config(dummyDict)
    """
    def traffic_tag_config(self, argdictionary):
        return super(SpirentTrafficTagConfigApi, self).traffic_tag_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_tag_config_enabled(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def traffic_tag_config_handle(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def traffic_tag_config_id(self, numeric):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def traffic_tag_config_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def traffic_tag_config_name(self, string):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {TrafficTagConfigConstants._CMD}
