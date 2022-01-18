from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import PacketStatsApi, PacketStatsConstants

"""
    This is the API class for the command: packet_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class IxiaPacketStatsApi(PacketStatsApi):

    """
    init function
    """
    def __init__(self, device):
        super(IxiaPacketStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_stats
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketStatsConstants.PACKET_STATS_API)
        api.packet_stats(dummyDict)
    """
    def packet_stats(self, argdictionary):
        return super(IxiaPacketStatsApi, self).packet_stats(argdictionary, self.supportedIxiaHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_stats_chunk_size(self, size):
        """
        This is the method the command: packet_stats option chunk_size
        Description:This parameter specifies how the average_deviation_per_chunk, standard_deviation_per_chunk, average_deviation and standard_deviation will be computed. For example, if the total number of packets is 12 and the chunk_size is 3, there will be 4 chunks of received packets, for each chunk existing an entry in the average_deviation_per_chunk and standard_deviation_per_chunk. The standard_deviation and average_deviation will be computed as the average of the standard_deviation_per_chunk and average_deviation_per_chunk respectively.If chunk_size is greater than the number if packets, there will be only a chunk of packets. This parameter is valid only for IxTclProtocol.
        Constants Available: CHUNK_SIZE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        size --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.CHUNK_SIZE_CMD : size})

    def packet_stats_dirname(self, path):
        """
        This is the method the command: packet_stats option dirname
        Description:This parameter is used in conjunction with the -format parameter.When -format is cap it represents the directory in which the cap files will be saved.When -format is csv it represents the directory in which the csv files will be saved.Valid only for IxTclNetwork.
        Constants Available: DIRNAME_CMD
        Supported:IxNetwork
        Keyword arguments:
        path --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.DIRNAME_CMD : path})

    def packet_stats_enable_ethernet_type(self, opt):
        """
        This is the method the command: packet_stats option enable_ethernet_type
        Description:Supported with IxTclHal. Enables the constraint used to calculate jitter statistics. If enabled, jitter will be calculated only for frames whose frame type field matches the ethernet type set by the option ethernet_type
        Constants Available: ENABLE_ETHERNET_TYPE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.ENABLE_ETHERNET_TYPE_CMD : opt})

    def packet_stats_enable_framesize(self, opt):
        """
        This is the method the command: packet_stats option enable_framesize
        Description:Supported with IxTclHal. Enables this constraint used to calculate jitter statistics. If enabled, jitter will be calculated only for frames whose size matches the framesize set by the command option framesize.
        Constants Available: ENABLE_FRAMESIZE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.ENABLE_FRAMESIZE_CMD : opt})

    def packet_stats_enable_pattern(self, opt):
        """
        This is the method the command: packet_stats option enable_pattern
        Description:Supported with IxTclHal. Constrain the jitter statistics calculations to frames in the capture buffer that match the ethernet pattern set by the pattern and pattern_offset options.
        Constants Available: ENABLE_PATTERN_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.ENABLE_PATTERN_CMD : opt})

    def packet_stats_ethernet_type(self, type):
        """
        This is the method the command: packet_stats option ethernet_type
        Description:Supported with IxTclHal. Constrain the jitter statistics calculations to frames in the capture buffer that match the ethernet type set by this option. A value such as {08 00} would be appropriate. Does not apply unless option enable_ethernet_type is set to 1.
        Constants Available: ETHERNET_TYPE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        type --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.ETHERNET_TYPE_CMD : type})

    def packet_stats_frame_id_end(self, opt):
        """
        This is the method the command: packet_stats option frame_id_end
        Description:The number of the last frame that needs to be retrieved. The default value is 20. The value of this parameter must be greater than frame_id_start. This parameter is needed for -format var and csv. Valid only for IxTclNetwork.
        Constants Available: FRAME_ID_END_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.FRAME_ID_END_CMD : opt})

    def packet_stats_frame_id_start(self, opt):
        """
        This is the method the command: packet_stats option frame_id_start
        Description:The number of the first frame that needs to be retrieved. The default value is 1. The value of this parameter must be less than frame_id_end. This parameter is needed for -format var and csv. Valid only for IxTclNetwork.
        Constants Available: FRAME_ID_START_CMD
        Supported:IxNetwork
        Keyword arguments:
        opt --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.FRAME_ID_START_CMD : opt})

    def packet_stats_framesize(self, size):
        """
        This is the method the command: packet_stats option framesize
        Description:Supported with IxTclHal. Constrain the jitter statistics calculations to frames in the capture buffer whose frame size matches the value set by this option.
        Constants Available: FRAMESIZE_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        size --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.FRAMESIZE_CMD : size})

    def packet_stats_packet_type(self, type):
        """
        This is the method the command: packet_stats option packet_type
        Description:Supported with IxTclNetwork.It is used to specify the types of frames that will be returned by the packet_stats procedure.Valid values are: data, control or both. The default value is both.
        Constants Available: PACKET_TYPE_CMD
        Supported:IxNetwork
        Keyword arguments:
        type --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.PACKET_TYPE_CMD : type})

    def packet_stats_pattern(self, type):
        """
        This is the method the command: packet_stats option pattern
        Description:Supported with IxTclHal. Enables this constraint used to calculate jitter statistics. If enabled, jitter will be calculated only for frames whose pattern matches the pattern in the frame at the offset set by the command option pattern_offset. A value of the form {11 12 02 44} would be appropriate.
        Constants Available: PATTERN_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        type --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.PATTERN_CMD : type})

    def packet_stats_pattern_offset(self, type):
        """
        This is the method the command: packet_stats option pattern_offset
        Description:Supported with IxTclHal. Used in conjunction with the pattern command.
        Constants Available: PATTERN_OFFSET_CMD
        Supported:IxOS/IxNetwork-FT
        Keyword arguments:
        type --
        return -- pass/fail
        """
        return self.packet_stats({PacketStatsConstants.PATTERN_OFFSET_CMD : type})


    supportedIxiaHltapiCommands = {PacketStatsConstants.CHUNK_SIZE_CMD, PacketStatsConstants.DIRNAME_CMD, PacketStatsConstants.ENABLE_ETHERNET_TYPE_CMD, PacketStatsConstants.ENABLE_FRAMESIZE_CMD, PacketStatsConstants.ENABLE_PATTERN_CMD, PacketStatsConstants.ETHERNET_TYPE_CMD, PacketStatsConstants.FILENAME_CMD, PacketStatsConstants.FORMAT_CMD, PacketStatsConstants.FRAME_ID_END_CMD, PacketStatsConstants.FRAME_ID_START_CMD, PacketStatsConstants.FRAMESIZE_CMD, PacketStatsConstants.PACKET_TYPE_CMD, PacketStatsConstants.PATTERN_CMD, PacketStatsConstants.PATTERN_OFFSET_CMD, PacketStatsConstants.PORT_HANDLE_CMD, PacketStatsConstants.STOP_CMD}
