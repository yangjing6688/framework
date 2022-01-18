from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: uds_filter_pallette_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class UdsFilterPalletteConfigApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(UdsFilterPalletteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_filter_pallette_config
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[UdsFilterPalletteConfigConstants.DA1_CMD] = "dummyValue1" # static value
        dummyDict[UdsFilterPalletteConfigConstants.DA2_CMD] = "dummyValue2" # static value
        dummyDict[UdsFilterPalletteConfigConstants.DA_MASK1_CMD] = "dummyValue3" # static value
        dummyDict[UdsFilterPalletteConfigConstants.DA_MASK2_CMD] = "dummyValue4" # static value
        dummyDict[UdsFilterPalletteConfigConstants.SA2_CMD] = "dummyValue5" # static value
        dummyDict[UdsFilterPalletteConfigConstants.SA_MASK1_CMD] = "dummyValue6" # static value
        dummyDict[UdsFilterPalletteConfigConstants.SA_MASK2_CMD] = "dummyValue7" # static value
        dummyDict[UdsFilterPalletteConfigConstants.CLONE_CAPTURE_FILTER_CMD] = "dummyValue8" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN1_CMD] = "dummyValue9" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN2_CMD] = "dummyValue10" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_MASK1_CMD] = "dummyValue11" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_MASK2_CMD] = "dummyValue12" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_OFFSET1_CMD] = "dummyValue13" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_OFFSET2_CMD] = "dummyValue14" # static value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE1_CMD] = UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE1_STARTOFFRAME # constant value
        dummyDict[UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE2_CMD] = UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE2_STARTOFFRAME # constant value
        dummyDict[UdsFilterPalletteConfigConstants.PORT_HANDLE_CMD] = "dummyValue17" # static value

        api = device.getApi(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API)
        api.uds_filter_pallette_config(dummyDict)
    """
    def uds_filter_pallette_config(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::uds_filter_pallette_config", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def uds_filter_pallette_config_DA1(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_DA2(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_DA_mask1(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_DA_mask2(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_SA2(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_SA_mask1(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_SA_mask2(self, mac):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_clone_capture_filter(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern1(self, hex):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern2(self, hex):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_mask1(self, hex):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_mask2(self, hex):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_offset1(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_offset2(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_offset_type1(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_pattern_offset_type2(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_filter_pallette_config_port_handle(self, any):
        """
        This is the method the command: uds_filter_pallette_config option port_handle
        Description:Port handle or list of port handles on which to configure the user
            defined statistic counters.
            DEFAULT
                None
        Constants Available: PORT_HANDLE_CMD
        Supported:IxNetwork[M]
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PORT_HANDLE_CMD : any})


"""
    This is the Constants class for the command: uds_filter_pallette_config
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class UdsFilterPalletteConfigConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    UDS_FILTER_PALLETTE_CONFIG_API = "UDS_FILTER_PALLETTE_CONFIG_API"

    DA1_CMD = "DA1"

    DA2_CMD = "DA2"

    DA_MASK1_CMD = "DA_mask1"

    DA_MASK2_CMD = "DA_mask2"

    SA2_CMD = "SA2"

    SA_MASK1_CMD = "SA_mask1"

    SA_MASK2_CMD = "SA_mask2"

    CLONE_CAPTURE_FILTER_CMD = "clone_capture_filter"

    PATTERN1_CMD = "pattern1"

    PATTERN2_CMD = "pattern2"

    PATTERN_MASK1_CMD = "pattern_mask1"

    PATTERN_MASK2_CMD = "pattern_mask2"

    PATTERN_OFFSET1_CMD = "pattern_offset1"

    PATTERN_OFFSET2_CMD = "pattern_offset2"

    PATTERN_OFFSET_TYPE1_CMD = "pattern_offset_type1"
    # Constant values for PATTERN_OFFSET_TYPE1_CMD
    PATTERN_OFFSET_TYPE1_STARTOFFRAME = "startOfFrame"
    PATTERN_OFFSET_TYPE1_STARTOFIP = "startOfIp"
    PATTERN_OFFSET_TYPE1_STARTOFPROTOCOL = "startOfProtocol"
    PATTERN_OFFSET_TYPE1_STARTOFSONET = "startOfSonet"

    PATTERN_OFFSET_TYPE2_CMD = "pattern_offset_type2"
    # Constant values for PATTERN_OFFSET_TYPE2_CMD
    PATTERN_OFFSET_TYPE2_STARTOFFRAME = "startOfFrame"
    PATTERN_OFFSET_TYPE2_STARTOFIP = "startOfIp"
    PATTERN_OFFSET_TYPE2_STARTOFPROTOCOL = "startOfProtocol"
    PATTERN_OFFSET_TYPE2_STARTOFSONET = "startOfSonet"

    PORT_HANDLE_CMD = "port_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -DA1
    -DA2
    -DA_mask1
    -DA_mask2
    -SA2
    -SA_mask1
    -SA_mask2
    -clone_capture_filter
    -pattern1
    -pattern2
    -pattern_mask1
    -pattern_mask2
    -pattern_offset1
    -pattern_offset2
    -pattern_offset_type1
    -pattern_offset_type2
    -port_handle
If you want to update this file, look in the CSV
"""
