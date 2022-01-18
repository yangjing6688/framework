from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsFilterPalletteConfigApi import UdsFilterPalletteConfigApi, UdsFilterPalletteConfigConstants

"""
    This is the API class for the command: uds_filter_pallette_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentUdsFilterPalletteConfigApi(UdsFilterPalletteConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentUdsFilterPalletteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_filter_pallette_config
    use this by passing in a dict() of all the commands

        api = device.getApi(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API)
        api.uds_filter_pallette_config(dummyDict)
    """
    def uds_filter_pallette_config(self, argdictionary):
        return super(SpirentUdsFilterPalletteConfigApi, self).uds_filter_pallette_config(argdictionary, self.supportedSpirentHltapiCommands)

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


    supportedSpirentHltapiCommands = {UdsFilterPalletteConfigConstants.PORT_HANDLE_CMD}
