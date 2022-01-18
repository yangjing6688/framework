from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiUdsConfigApi import UdsConfigApi, UdsConfigConstants

"""
    This is the API class for the command: uds_config

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaUdsConfigApi(UdsConfigApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaUdsConfigApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: uds_config
    use this by passing in a dict() of all the commands

        api = device.getApi(UdsConfigConstants.UDS_CONFIG_API)
        api.uds_config(dummyDict)
    """
    def uds_config(self, argdictionary):
        return super(IxiaUdsConfigApi, self).uds_config(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def uds_config_uds1(self, bool_opt):
        """
        This is the method the command: uds_config option uds1
        Description:Not defined
            Valid options are:
            0

            disable
            1

            enable
            DEFAULT
                None
        Constants Available: UDS1_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_CMD : bool_opt})

    def uds_config_uds1_DA(self, opt):
        """
        This is the method the command: uds_config option uds1_DA
        Description:Not defined
            Valid options are:
            any

            (default) count all packets
            DA1

            count packets having the MAC destination address configured with
            x

            count packets having the MAC destination address configured with
            notDA1

            count packets that don't have the MAC destination address configured with
            DA2

            count packets having the MAC destination address configured with
            notDA2

            count packets that don't have the MAC destination address configured with
            DEFAULT
                None
        Constants Available: UDS1_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_DA_CMD : opt})

    def uds_config_uds1_SA(self, opt):
        """
        This is the method the command: uds_config option uds1_SA
        Description:Not defined
            Valid options are:
            any

            (default) count all packets
            SA1

            count packets having the MAC source address configured with
            x

            count packets having the MAC source address configured with
            notSA1

            count packets that don't have the MAC source address configured with
            SA2

            count packets having the MAC source address configured with
            notSA2

            count packets that don't have the MAC source address configured with
            DEFAULT
                None
        Constants Available: UDS1_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_SA_CMD : opt})

    def uds_config_uds1_error(self, opt):
        """
        This is the method the command: uds_config option uds1_error
        Description:Not defined
            Valid options are:
            errAnyFrame

            (default) count all packets
            errBadCRC

            count frames with bad CRC
            errBadFrame

            count corrupted frames
            errGoodFrame

            count frames with no errors
            DEFAULT
                None
        Constants Available: UDS1_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_ERROR_CMD : opt})

    def uds_config_uds1_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds1_framesize
        Description:Not defined
            Valid options are:
            any

            (default) count all packets
            custom

            count frames having framesize in the range configured with
            uds1_framesize_from and
            x

            count frames having framesize in the range configured with
            uds1_framesize_from and
            jumbo

            count frames having framesize in the range 1518-9000
            oversized

            count frames having framesize in the range 512-1024
            undersized

            count frames having framesize in the range 48-64
            DEFAULT
                None
        Constants Available: UDS1_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds1_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds1_framesize_from
        Description:Configure the starting frame size when uds1_framesize is custom
            DEFAULT
                None
        Constants Available: UDS1_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds1_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds1_framesize_to
        Description:Configure the ending frame size when uds1_framesize is custom
            DEFAULT
                None
        Constants Available: UDS1_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds1_pattern(self, opt):
        """
        This is the method the command: uds_config option uds1_pattern
        Description:Increment UDS1 counter based on the pattern configured with
            uds_filter_pallette_config
            Valid options are:
            any

            (default) count all packets
            pattern1

            count packets matching pattern1
            notPattern1

            count packets not matching pattern1
            pattern2

            count packets matching pattern2
            notPattern2

            count packets not matching pattern2
            DEFAULT
                None
        Constants Available: UDS1_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS1_PATTERN_CMD : opt})

    def uds_config_uds2(self, bool_opt):
        """
        This is the method the command: uds_config option uds2
        Description:Same as -uds1. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_CMD : bool_opt})

    def uds_config_uds2_DA(self, opt):
        """
        This is the method the command: uds_config option uds2_DA
        Description:Same as -uds1_DA. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_DA_CMD : opt})

    def uds_config_uds2_SA(self, opt):
        """
        This is the method the command: uds_config option uds2_SA
        Description:Same as -uds1_SA. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_SA_CMD : opt})

    def uds_config_uds2_error(self, opt):
        """
        This is the method the command: uds_config option uds2_error
        Description:Same as -uds1_error. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_ERROR_CMD : opt})

    def uds_config_uds2_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds2_framesize
        Description:Same as -uds1_framesize. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds2_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds2_framesize_from
        Description:Same as -uds1_framesize_from. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds2_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds2_framesize_to
        Description:Same as -uds1_framesize_to. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds2_pattern(self, opt):
        """
        This is the method the command: uds_config option uds2_pattern
        Description:Same as -uds1_pattern. Applies to UDS2
            DEFAULT
                None
        Constants Available: UDS2_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS2_PATTERN_CMD : opt})

    def uds_config_uds3(self, bool_opt):
        """
        This is the method the command: uds_config option uds3
        Description:Same as -uds1. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_CMD : bool_opt})

    def uds_config_uds3_DA(self, opt):
        """
        This is the method the command: uds_config option uds3_DA
        Description:Same as -uds1_DA. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_DA_CMD : opt})

    def uds_config_uds3_SA(self, opt):
        """
        This is the method the command: uds_config option uds3_SA
        Description:Same as -uds1_SA. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_SA_CMD : opt})

    def uds_config_uds3_error(self, opt):
        """
        This is the method the command: uds_config option uds3_error
        Description:Same as -uds1_error. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_ERROR_CMD : opt})

    def uds_config_uds3_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds3_framesize
        Description:Same as -uds1_framesize. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds3_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds3_framesize_from
        Description:Same as -uds1_framesize_from. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds3_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds3_framesize_to
        Description:Same as -uds1_framesize_to. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds3_pattern(self, opt):
        """
        This is the method the command: uds_config option uds3_pattern
        Description:Same as -uds1_pattern. Applies to UDS3
            DEFAULT
                None
        Constants Available: UDS3_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS3_PATTERN_CMD : opt})

    def uds_config_uds4(self, bool_opt):
        """
        This is the method the command: uds_config option uds4
        Description:Same as -uds1. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_CMD : bool_opt})

    def uds_config_uds4_DA(self, opt):
        """
        This is the method the command: uds_config option uds4_DA
        Description:Same as -uds1_DA. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_DA_CMD : opt})

    def uds_config_uds4_SA(self, opt):
        """
        This is the method the command: uds_config option uds4_SA
        Description:Same as -uds1_SA. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_SA_CMD : opt})

    def uds_config_uds4_error(self, opt):
        """
        This is the method the command: uds_config option uds4_error
        Description:Same as -uds1_error. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_ERROR_CMD : opt})

    def uds_config_uds4_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds4_framesize
        Description:Same as -uds1_framesize. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds4_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds4_framesize_from
        Description:Same as -uds1_framesize_from. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds4_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds4_framesize_to
        Description:Same as -uds1_framesize_to. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds4_pattern(self, opt):
        """
        This is the method the command: uds_config option uds4_pattern
        Description:Same as -uds1_pattern. Applies to UDS4
            DEFAULT
                None
        Constants Available: UDS4_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS4_PATTERN_CMD : opt})

    def uds_config_uds5(self, bool_opt):
        """
        This is the method the command: uds_config option uds5
        Description:Same as -uds1. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_CMD : bool_opt})

    def uds_config_uds5_DA(self, opt):
        """
        This is the method the command: uds_config option uds5_DA
        Description:Same as -uds1_DA. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_DA_CMD : opt})

    def uds_config_uds5_SA(self, opt):
        """
        This is the method the command: uds_config option uds5_SA
        Description:Same as -uds1_SA. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_SA_CMD : opt})

    def uds_config_uds5_error(self, opt):
        """
        This is the method the command: uds_config option uds5_error
        Description:Same as -uds1_error. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_ERROR_CMD : opt})

    def uds_config_uds5_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds5_framesize
        Description:Same as -uds1_framesize. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds5_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds5_framesize_from
        Description:Same as -uds1_framesize_from. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds5_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds5_framesize_to
        Description:Same as -uds1_framesize_to. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds5_pattern(self, opt):
        """
        This is the method the command: uds_config option uds5_pattern
        Description:Same as -uds1_pattern. Applies to UDS5
            DEFAULT
                None
        Constants Available: UDS5_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS5_PATTERN_CMD : opt})

    def uds_config_uds6(self, bool_opt):
        """
        This is the method the command: uds_config option uds6
        Description:Same as -uds1. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_CMD : bool_opt})

    def uds_config_uds6_DA(self, opt):
        """
        This is the method the command: uds_config option uds6_DA
        Description:Same as -uds1_DA. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_DA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_DA_CMD : opt})

    def uds_config_uds6_SA(self, opt):
        """
        This is the method the command: uds_config option uds6_SA
        Description:Same as -uds1_SA. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_SA_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_SA_CMD : opt})

    def uds_config_uds6_error(self, opt):
        """
        This is the method the command: uds_config option uds6_error
        Description:Same as -uds1_error. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_ERROR_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_ERROR_CMD : opt})

    def uds_config_uds6_framesize(self, bool_opt):
        """
        This is the method the command: uds_config option uds6_framesize
        Description:Same as -uds1_framesize. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_FRAMESIZE_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_FRAMESIZE_CMD : bool_opt})

    def uds_config_uds6_framesize_from(self, numeric):
        """
        This is the method the command: uds_config option uds6_framesize_from
        Description:Same as -uds1_framesize_from. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_FRAMESIZE_FROM_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_FRAMESIZE_FROM_CMD : numeric})

    def uds_config_uds6_framesize_to(self, numeric):
        """
        This is the method the command: uds_config option uds6_framesize_to
        Description:Same as -uds1_framesize_to. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_FRAMESIZE_TO_CMD
        Supported:IxNetwork
        Keyword arguments:
        numeric --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_FRAMESIZE_TO_CMD : numeric})

    def uds_config_uds6_pattern(self, opt):
        """
        This is the method the command: uds_config option uds6_pattern
        Description:Same as -uds1_pattern. Applies to UDS6
            DEFAULT
                None
        Constants Available: UDS6_PATTERN_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.uds_config({UdsConfigConstants.UDS6_PATTERN_CMD : opt})


    supportedIxiaHltapiCommands = {UdsConfigConstants.PORT_HANDLE_CMD, UdsConfigConstants.UDS1_CMD, UdsConfigConstants.UDS1_DA_CMD, UdsConfigConstants.UDS1_SA_CMD, UdsConfigConstants.UDS1_ERROR_CMD, UdsConfigConstants.UDS1_FRAMESIZE_CMD, UdsConfigConstants.UDS1_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS1_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS1_PATTERN_CMD, UdsConfigConstants.UDS2_CMD, UdsConfigConstants.UDS2_DA_CMD, UdsConfigConstants.UDS2_SA_CMD, UdsConfigConstants.UDS2_ERROR_CMD, UdsConfigConstants.UDS2_FRAMESIZE_CMD, UdsConfigConstants.UDS2_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS2_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS2_PATTERN_CMD, UdsConfigConstants.UDS3_CMD, UdsConfigConstants.UDS3_DA_CMD, UdsConfigConstants.UDS3_SA_CMD, UdsConfigConstants.UDS3_ERROR_CMD, UdsConfigConstants.UDS3_FRAMESIZE_CMD, UdsConfigConstants.UDS3_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS3_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS3_PATTERN_CMD, UdsConfigConstants.UDS4_CMD, UdsConfigConstants.UDS4_DA_CMD, UdsConfigConstants.UDS4_SA_CMD, UdsConfigConstants.UDS4_ERROR_CMD, UdsConfigConstants.UDS4_FRAMESIZE_CMD, UdsConfigConstants.UDS4_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS4_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS4_PATTERN_CMD, UdsConfigConstants.UDS5_CMD, UdsConfigConstants.UDS5_DA_CMD, UdsConfigConstants.UDS5_SA_CMD, UdsConfigConstants.UDS5_ERROR_CMD, UdsConfigConstants.UDS5_FRAMESIZE_CMD, UdsConfigConstants.UDS5_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS5_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS5_PATTERN_CMD, UdsConfigConstants.UDS6_CMD, UdsConfigConstants.UDS6_DA_CMD, UdsConfigConstants.UDS6_SA_CMD, UdsConfigConstants.UDS6_ERROR_CMD, UdsConfigConstants.UDS6_FRAMESIZE_CMD, UdsConfigConstants.UDS6_FRAMESIZE_FROM_CMD, UdsConfigConstants.UDS6_FRAMESIZE_TO_CMD, UdsConfigConstants.UDS6_PATTERN_CMD}
