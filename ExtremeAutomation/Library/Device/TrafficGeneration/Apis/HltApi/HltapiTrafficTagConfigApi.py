from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: traffic_tag_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class TrafficTagConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(TrafficTagConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: traffic_tag_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[TrafficTagConfigConstants._CMD] = "dummyValue1" # static value
        dummyDict[TrafficTagConfigConstants.ENABLED_CMD] = "dummyValue2" # static value
        dummyDict[TrafficTagConfigConstants.HANDLE_CMD] = "dummyValue3" # static value
        dummyDict[TrafficTagConfigConstants.ID_CMD] = "dummyValue4" # static value
        dummyDict[TrafficTagConfigConstants.MODE_CMD] = TrafficTagConfigConstants.MODE_CREATE # constant value
        dummyDict[TrafficTagConfigConstants.NAME_CMD] = "dummyValue6" # static value

        api = device.getApi(TrafficTagConfigConstants.TRAFFIC_TAG_CONFIG_API)
        api.traffic_tag_config(dummyDict)
    """
    def traffic_tag_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::traffic_tag_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def traffic_tag_config_(self):
        """
        This is the method the command: traffic_tag_config option
        Description:delete: Delete the specified tag.
        Constants Available: _CMD
        Keyword arguments:
        return -- pass/fail
        """
        return self.traffic_tag_config({TrafficTagConfigConstants._CMD : ""})

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


"""
    This is the Constants class for the command: traffic_tag_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class TrafficTagConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_TAG_CONFIG_API = "TRAFFIC_TAG_CONFIG_API"

    _CMD = ""

    ENABLED_CMD = "enabled"

    HANDLE_CMD = "handle"

    ID_CMD = "id"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CREATE = "create"
    MODE_MODIFY = "modify"
    MODE_DELETE = "delete"

    NAME_CMD = "name"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -
    -enabled
    -handle
    -id
    -mode
    -name
If you want to update this file, look in the CSV
"""
