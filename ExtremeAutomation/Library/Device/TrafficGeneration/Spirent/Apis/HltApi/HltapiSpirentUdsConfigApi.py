from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsConfigApi import UdsConfigApi, UdsConfigConstants

"""
    This is the API class for the command: uds_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentUdsConfigApi(UdsConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentUdsConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_config
    use this by passing in a dict() of all the commands

        api = device.getApi(UdsConfigConstants.UDS_CONFIG_API)
        api.uds_config(dummyDict)
    """
    def uds_config(self, argdictionary):
        return super(SpirentUdsConfigApi, self).uds_config(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def uds_config_uds1(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds1_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds2_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds3_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds4_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds5_pattern(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_DA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_SA(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_error(self, opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize_from(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_framesize_to(self, numeric):
        return self.logger.log_unimplemented_method()

    def uds_config_uds6_pattern(self, opt):
        return self.logger.log_unimplemented_method()


    supportedSpirentHltapiCommands = {UdsConfigConstants.PORT_HANDLE_CMD}
