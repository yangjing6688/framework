from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficTagConfigApi import TrafficTagConfigApi, TrafficTagConfigConstants

"""
    This is the API class for the command: traffic_tag_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaTrafficTagConfigApi(TrafficTagConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaTrafficTagConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_tag_config
    use this by passing in a dict() of all the commands

        api = device.getApi(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API)
        api.traffic_tag_config(dummyDict)
    """
    def traffic_tag_config(self, argdictionary):
        return super(IxiaTrafficTagConfigApi, self).traffic_tag_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_tag_config_enabled(self, opt):
        """
        This is the method the command: traffic_tag_config option enabled
        Description:Enables/disables tags
        Constants Available: ENABLED_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants.ENABLED_CMD : opt})

    def traffic_tag_config_handle(self, opt):
        """
        This is the method the command: traffic_tag_config option handle
        Description:For create: protocol stack handle needed to configure traffic tag. For modify/delete: tag handle that must be modified/deleted
        Constants Available: HANDLE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants.HANDLE_CMD : opt})

    def traffic_tag_config_id(self, numeric):
        """
        This is the method the command: traffic_tag_config option id
        Description:the tag ids that this entity will use/publish
        Constants Available: ID_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants.ID_CMD : numeric})

    def traffic_tag_config_mode(self, opt):
        """
        This is the method the command: traffic_tag_config option mode
        Description:Which mode is being performed.
        Constants Available: MODE_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants.MODE_CMD : opt})

    def traffic_tag_config_name(self, string):
        """
        This is the method the command: traffic_tag_config option name
        Description:specifies the name of the tag the entity will be part of
        Constants Available: NAME_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        string --
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants.NAME_CMD : string})


    supportedIxiaHltapiCommands = {TrafficTagConfigConstants._CMD, TrafficTagConfigConstants.ENABLED_CMD, TrafficTagConfigConstants.HANDLE_CMD, TrafficTagConfigConstants.ID_CMD, TrafficTagConfigConstants.MODE_CMD, TrafficTagConfigConstants.NAME_CMD}
