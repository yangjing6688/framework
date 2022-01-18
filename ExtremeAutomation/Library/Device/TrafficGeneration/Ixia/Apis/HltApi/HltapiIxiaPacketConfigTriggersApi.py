from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import PacketConfigTriggersApi, PacketConfigTriggersConstants

"""
    This is the API class for the command: packet_config_triggers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketConfigTriggersApi(PacketConfigTriggersApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketConfigTriggersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_triggers
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        api.packet_config_triggers(dummyDict)
    """
    def packet_config_triggers(self, argdictionary):
        return super(IxiaPacketConfigTriggersApi, self).packet_config_triggers(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_triggers_async_trigger1(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: ASYNC_TRIGGER1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_CMD : opt})

    def packet_config_triggers_async_trigger1_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: ASYNC_TRIGGER1_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_CMD : opt})

    def packet_config_triggers_async_trigger1_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: ASYNC_TRIGGER1_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_SA_CMD : opt})

    def packet_config_triggers_async_trigger1_error(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: ASYNC_TRIGGER1_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_ERROR_CMD : opt})

    def packet_config_triggers_async_trigger1_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: ASYNC_TRIGGER1_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_CMD : opt})

    def packet_config_triggers_async_trigger1_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when async_trigger1_framesize is set to 1.
        Constants Available: ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_async_trigger1_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when async_trigger1_framesize is set to 1.
        Constants Available: ASYNC_TRIGGER1_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_async_trigger1_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger1_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: ASYNC_TRIGGER1_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER1_PATTERN_CMD : opt})

    def packet_config_triggers_async_trigger2(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: ASYNC_TRIGGER2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_CMD : opt})

    def packet_config_triggers_async_trigger2_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: ASYNC_TRIGGER2_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_DA_CMD : opt})

    def packet_config_triggers_async_trigger2_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: ASYNC_TRIGGER2_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_SA_CMD : opt})

    def packet_config_triggers_async_trigger2_error(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: ASYNC_TRIGGER2_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_ERROR_CMD : opt})

    def packet_config_triggers_async_trigger2_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: ASYNC_TRIGGER2_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_CMD : opt})

    def packet_config_triggers_async_trigger2_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when async_trigger2_framesize is set to 1.
        Constants Available: ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_async_trigger2_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when async_trigger2_framesize is set to 1.
        Constants Available: ASYNC_TRIGGER2_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_async_trigger2_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option async_trigger2_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: ASYNC_TRIGGER2_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.ASYNC_TRIGGER2_PATTERN_CMD : opt})

    def packet_config_triggers_capture_filter(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: CAPTURE_FILTER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_CMD : opt})

    def packet_config_triggers_capture_filter_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: CAPTURE_FILTER_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_DA_CMD : opt})

    def packet_config_triggers_capture_filter_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: CAPTURE_FILTER_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_SA_CMD : opt})

    def packet_config_triggers_capture_filter_error(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: CAPTURE_FILTER_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_ERROR_CMD : opt})

    def packet_config_triggers_capture_filter_expression_string(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_expression_string
        Description:Supported only with IxTclNetwork. String that is composed of SA1,DA1,P1,P2, optionally negated with ! and connected with operators 'and','or','xor','nand' or 'nor'.Eg: {DA1 and SA1 or !P1 and P2}.
        Constants Available: CAPTURE_FILTER_EXPRESSION_STRING_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_EXPRESSION_STRING_CMD : opt})

    def packet_config_triggers_capture_filter_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: CAPTURE_FILTER_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_CMD : opt})

    def packet_config_triggers_capture_filter_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when capture_filter_framesize is set to 1.
        Constants Available: CAPTURE_FILTER_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_capture_filter_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when capture_filter_framesize is set to 1.
        Constants Available: CAPTURE_FILTER_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_capture_filter_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_filter_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: CAPTURE_FILTER_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_CMD : opt})

    def packet_config_triggers_capture_trigger(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: CAPTURE_TRIGGER_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD : opt})

    def packet_config_triggers_capture_trigger_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: CAPTURE_TRIGGER_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_CMD : opt})

    def packet_config_triggers_capture_trigger_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: CAPTURE_TRIGGER_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_CMD : opt})

    def packet_config_triggers_capture_trigger_error(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: CAPTURE_TRIGGER_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_ERROR_CMD : opt})

    def packet_config_triggers_capture_trigger_expression_string(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_expression_string
        Description:Supported only with IxTclNetwork. String that is composed of SA1,DA1,P1,P2, optionally negated with ! and connected with operators 'and','or','xor','nand' or 'nor'.Eg: {DA1 and SA1 or !P1 and P2}.
        Constants Available: CAPTURE_TRIGGER_EXPRESSION_STRING_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_EXPRESSION_STRING_CMD : opt})

    def packet_config_triggers_capture_trigger_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: CAPTURE_TRIGGER_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_CMD : opt})

    def packet_config_triggers_capture_trigger_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when capture_trigger_framesize is set to 1.
        Constants Available: CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_capture_trigger_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when capture_trigger_framesize is set to 1.
        Constants Available: CAPTURE_TRIGGER_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_capture_trigger_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option capture_trigger_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: CAPTURE_TRIGGER_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.CAPTURE_TRIGGER_PATTERN_CMD : opt})

    def packet_config_triggers_handle(self, opt):
        """
        This is the method the command: packet_config_triggers option handle
        Description:Supported with IxTclHal. handle or list of handles returned by ::::packet_config_filter. The patterns and pvc pairs represented by these handles will be used as filters, triggers and/or counters if -capture_filter_pattern, capture_trigger_pattern, -uds1_pattern and/or -uds2_pattern are set to patternAtm
        Constants Available: HANDLE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.HANDLE_CMD : opt})

    def packet_config_triggers_mode(self, opt):
        """
        This is the method the command: packet_config_triggers option mode
        Description:Supported with IxTclHal and IxTclNetwork (addAtmFilter choice is not valid with IxTclNetwork). When -mode is create all the filters, triggers and counters (general and ATM specific) will be configured.When -mode is addAtmTrigger, only the ATM specific configurations will be taken in consideration. This is useful when different configurations are needed for some handles
        Constants Available: MODE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.MODE_CMD : opt})

    def packet_config_triggers_uds1(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: UDS1_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_CMD : opt})

    def packet_config_triggers_uds1_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: UDS1_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_DA_CMD : opt})

    def packet_config_triggers_uds1_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: UDS1_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_SA_CMD : opt})

    def packet_config_triggers_uds1_error(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: UDS1_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_ERROR_CMD : opt})

    def packet_config_triggers_uds1_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: UDS1_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_FRAMESIZE_CMD : opt})

    def packet_config_triggers_uds1_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when uds1_framesize is set to 1.
        Constants Available: UDS1_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_uds1_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when uds1_framesize is set to 1.
        Constants Available: UDS1_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_uds1_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option uds1_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: UDS1_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS1_PATTERN_CMD : opt})

    def packet_config_triggers_uds2(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 that counts the number of frames filtered. Async triggers can not be set when error type is other than errAnyFrame, errGoodFrame, errBadCRC, errBadFrame
        Constants Available: UDS2_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_CMD : opt})

    def packet_config_triggers_uds2_DA(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_DA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the destination MAC addresses. The possible values are as in capture_filter_DA. When configuring UDS(1-6), only one of the six UDS slots can be configured for DA1, and DA2.
        Constants Available: UDS2_DA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_DA_CMD : opt})

    def packet_config_triggers_uds2_SA(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_SA
        Description:Supported with IxTclHal and IxTclNetwork. Enables or disables User Defined Statistics counter 5 to filter on the source MAC addresses.
        Constants Available: UDS2_SA_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_SA_CMD : opt})

    def packet_config_triggers_uds2_error(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_error
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables the frame size constraint which specifies a range of frame sizes to filter for User Defined Statistics counter 5.
        Constants Available: UDS2_ERROR_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_ERROR_CMD : opt})

    def packet_config_triggers_uds2_framesize(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_framesize
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclHal). Enables or disables the frame size constraint which specifies a

            Valid options are:

            0: any framesize
            1: custom framesize
            jumbo: valid only for IxTclNetwork
            oversized: valid only for IxTclNetwork
            undersized: valid only for IxTclNetwork
        Constants Available: UDS2_FRAMESIZE_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_FRAMESIZE_CMD : opt})

    def packet_config_triggers_uds2_framesize_from(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_framesize_from
        Description:Supported with IxTclHal and IxTclNetwork. The minimum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when uds2_framesize is set to 1.
        Constants Available: UDS2_FRAMESIZE_FROM_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_FRAMESIZE_FROM_CMD : opt})

    def packet_config_triggers_uds2_framesize_to(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_framesize_to
        Description:Supported with IxTclHal and IxTclNetwork. The maximum range of the size of frame to be filtered for User Defined Statistics counter 5. Applicable only when uds2_framesize is set to 1.
        Constants Available: UDS2_FRAMESIZE_TO_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_FRAMESIZE_TO_CMD : opt})

    def packet_config_triggers_uds2_pattern(self, opt):
        """
        This is the method the command: packet_config_triggers option uds2_pattern
        Description:Supported with IxTclHal and IxTclNetwork (not all choices supported for IxTclNetwork). Enables or disables User Defined Statistics counter 5 to filter on the pattern.
            Valid options are:
            any: (default) disables the pattern filter constraint
            pattern1: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1 and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            notPattern1: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern1and patternMask1 at offset patternOffset1 as specified with ::<namespace>::packet_config_filter
            pattern2: sets the pattern filter constraint to trigger on frames with a pattern that matches pattern2 and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            notPattern2: sets the pattern filter constraint to trigger on frames except those with a pattern that matches pattern2and patternMask2 at offset patternOffset2 as specified with ::<namespace>::packet_config_filter
            pattern1and2: not supported for IxTclNetwork. Sets the pattern filter constraint to trigger on frames with a pattern that matches pattern1, pattern2 and patternMask1, patternMask2 at offset patternOffset1 and patternOffset2 as specified with ::<namespace>::packet_config_filter
            patternAtm: not supported for IxTclNetwork. -handle parameter is mandatory. The atm patterns in conjunctions with their vpi/vci pair will be extracted from the handle and set as filter criteria.
        Constants Available: UDS2_PATTERN_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_config_triggers({PacketConfigTriggersConstants.UDS2_PATTERN_CMD : opt})


    supportedIxiaHltapiCommands = {PacketConfigTriggersConstants.ASYNC_TRIGGER1_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_DA_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_SA_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_ERROR_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER1_PATTERN_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_DA_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_SA_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_ERROR_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.ASYNC_TRIGGER2_PATTERN_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_DA_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_SA_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_ERROR_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_EXPRESSION_STRING_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.CAPTURE_FILTER_PATTERN_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_DA_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_SA_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_ERROR_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_EXPRESSION_STRING_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.CAPTURE_TRIGGER_PATTERN_CMD, PacketConfigTriggersConstants.HANDLE_CMD, PacketConfigTriggersConstants.MODE_CMD, PacketConfigTriggersConstants.PORT_HANDLE_CMD, PacketConfigTriggersConstants.UDS1_CMD, PacketConfigTriggersConstants.UDS1_DA_CMD, PacketConfigTriggersConstants.UDS1_SA_CMD, PacketConfigTriggersConstants.UDS1_ERROR_CMD, PacketConfigTriggersConstants.UDS1_FRAMESIZE_CMD, PacketConfigTriggersConstants.UDS1_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.UDS1_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.UDS1_PATTERN_CMD, PacketConfigTriggersConstants.UDS2_CMD, PacketConfigTriggersConstants.UDS2_DA_CMD, PacketConfigTriggersConstants.UDS2_SA_CMD, PacketConfigTriggersConstants.UDS2_ERROR_CMD, PacketConfigTriggersConstants.UDS2_FRAMESIZE_CMD, PacketConfigTriggersConstants.UDS2_FRAMESIZE_FROM_CMD, PacketConfigTriggersConstants.UDS2_FRAMESIZE_TO_CMD, PacketConfigTriggersConstants.UDS2_PATTERN_CMD}
