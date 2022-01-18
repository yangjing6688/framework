from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsFilterPalletteConfigApi import UdsFilterPalletteConfigApi, UdsFilterPalletteConfigConstants

"""
    This is the API class for the command: uds_filter_pallette_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaUdsFilterPalletteConfigApi(UdsFilterPalletteConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaUdsFilterPalletteConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_filter_pallette_config
    use this by passing in a dict() of all the commands

        api = device.getApi(UdsFilterPalletteConfigConstants.UDS_FILTER_PALLETTE_CONFIG_API)
        api.uds_filter_pallette_config(dummyDict)
    """
    def uds_filter_pallette_config(self, argdictionary):
        return super(IxiaUdsFilterPalletteConfigApi, self).uds_filter_pallette_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def uds_filter_pallette_config_DA1(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option DA1
        Description:Configure the MAC destination address 1 filter.
            DEFAULT
                None
        Constants Available: DA1_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.DA1_CMD : mac})

    def uds_filter_pallette_config_DA2(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option DA2
        Description:Configure the MAC destination address 2 filter.
            DEFAULT
                None
        Constants Available: DA2_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.DA2_CMD : mac})

    def uds_filter_pallette_config_DA_mask1(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option DA_mask1
        Description:Configure the MAC destination address 1 mask filter.
            DEFAULT
                None
        Constants Available: DA_MASK1_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.DA_MASK1_CMD : mac})

    def uds_filter_pallette_config_DA_mask2(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option DA_mask2
        Description:Configure the MAC destination address 2 mask filter.
            DEFAULT
                None
        Constants Available: DA_MASK2_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.DA_MASK2_CMD : mac})

    def uds_filter_pallette_config_SA2(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option SA2
        Description:Configure the MAC source address 2 filter.
            DEFAULT
                None
        Constants Available: SA2_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.SA2_CMD : mac})

    def uds_filter_pallette_config_SA_mask1(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option SA_mask1
        Description:Configure the MAC source address 1 mask filter.
            DEFAULT
                None
        Constants Available: SA_MASK1_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.SA_MASK1_CMD : mac})

    def uds_filter_pallette_config_SA_mask2(self, mac):
        """
        This is the method the command: uds_filter_pallette_config option SA_mask2
        Description:Configure the MAC source address 2 mask filter.
            DEFAULT
                None
        Constants Available: SA_MASK2_CMD
        Supported:IxNetwork
        Keyword arguments:
        mac --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.SA_MASK2_CMD : mac})

    def uds_filter_pallette_config_clone_capture_filter(self, bool_opt):
        """
        This is the method the command: uds_filter_pallette_config option clone_capture_filter
        Description:Enable copy of the filter pallette configured with
            ::::packet_config_filter.
            Valid options are:
            0

            (default) Do not copy the capture filter pallette
            1

            Copy the capture filter pallette settings for the options that were not
            specified
            x

            Copy the capture filter pallette settings for the options that were not
            specified
            DEFAULT
                None
        Constants Available: CLONE_CAPTURE_FILTER_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.CLONE_CAPTURE_FILTER_CMD : bool_opt})

    def uds_filter_pallette_config_pattern1(self, hex):
        """
        This is the method the command: uds_filter_pallette_config option pattern1
        Description:Configure the pattern1 hex filter.
            DEFAULT
                None
        Constants Available: PATTERN1_CMD
        Supported:IxNetwork
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN1_CMD : hex})

    def uds_filter_pallette_config_pattern2(self, hex):
        """
        This is the method the command: uds_filter_pallette_config option pattern2
        Description:Configure the pattern2 hex filter.
            DEFAULT
                None
        Constants Available: PATTERN2_CMD
        Supported:IxNetwork
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN2_CMD : hex})

    def uds_filter_pallette_config_pattern_mask1(self, hex):
        """
        This is the method the command: uds_filter_pallette_config option pattern_mask1
        Description:Configure the pattern1 mask.
            DEFAULT
                None
        Constants Available: PATTERN_MASK1_CMD
        Supported:IxNetwork
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_MASK1_CMD : hex})

    def uds_filter_pallette_config_pattern_mask2(self, hex):
        """
        This is the method the command: uds_filter_pallette_config option pattern_mask2
        Description:Configure the pattern2 mask.
            DEFAULT
                None
        Constants Available: PATTERN_MASK2_CMD
        Supported:IxNetwork
        Keyword arguments:
        hex --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_MASK2_CMD : hex})

    def uds_filter_pallette_config_pattern_offset1(self, numeric):
        """
        This is the method the command: uds_filter_pallette_config option pattern_offset1
        Description:Offset for pattern1 in bytes.
            DEFAULT
                None
        Constants Available: PATTERN_OFFSET1_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_OFFSET1_CMD : numeric})

    def uds_filter_pallette_config_pattern_offset2(self, numeric):
        """
        This is the method the command: uds_filter_pallette_config option pattern_offset2
        Description:Offset for pattern2 in bytes.
            DEFAULT
                None
        Constants Available: PATTERN_OFFSET2_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_OFFSET2_CMD : numeric})

    def uds_filter_pallette_config_pattern_offset_type1(self, opt):
        """
        This is the method the command: uds_filter_pallette_config option pattern_offset_type1
        Description:Not defined
            Valid options are:
            startOfFrame

            (default) Offset from the start of the frame.
            startOfIp

            Offset from the start of the IP header
            startOfProtocol

            Offset from the start of the protocol
            x

            Offset from the start of the protocol
            startOfSonet

            Offset from the start of the SONET frame.
            DEFAULT
                None
        Constants Available: PATTERN_OFFSET_TYPE1_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE1_CMD : opt})

    def uds_filter_pallette_config_pattern_offset_type2(self, opt):
        """
        This is the method the command: uds_filter_pallette_config option pattern_offset_type2
        Description:Not defined
            Valid options are:
            startOfFrame

            (default) Offset from the start of the frame.
            startOfIp

            Offset from the start of the IP header
            startOfProtocol

            Offset from the start of the protocol
            x

            Offset from the start of the protocol
            startOfSonet

            Offset from the start of the SONET frame.
            DEFAULT
                None
        Constants Available: PATTERN_OFFSET_TYPE2_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_filter_pallette_config({UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE2_CMD : opt})


    supportedIxiaHltapiCommands = {UdsFilterPalletteConfigConstants.DA1_CMD, UdsFilterPalletteConfigConstants.DA2_CMD, UdsFilterPalletteConfigConstants.DA_MASK1_CMD, UdsFilterPalletteConfigConstants.DA_MASK2_CMD, UdsFilterPalletteConfigConstants.SA2_CMD, UdsFilterPalletteConfigConstants.SA_MASK1_CMD, UdsFilterPalletteConfigConstants.SA_MASK2_CMD, UdsFilterPalletteConfigConstants.CLONE_CAPTURE_FILTER_CMD, UdsFilterPalletteConfigConstants.PATTERN1_CMD, UdsFilterPalletteConfigConstants.PATTERN2_CMD, UdsFilterPalletteConfigConstants.PATTERN_MASK1_CMD, UdsFilterPalletteConfigConstants.PATTERN_MASK2_CMD, UdsFilterPalletteConfigConstants.PATTERN_OFFSET1_CMD, UdsFilterPalletteConfigConstants.PATTERN_OFFSET2_CMD, UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE1_CMD, UdsFilterPalletteConfigConstants.PATTERN_OFFSET_TYPE2_CMD, UdsFilterPalletteConfigConstants.PORT_HANDLE_CMD}
