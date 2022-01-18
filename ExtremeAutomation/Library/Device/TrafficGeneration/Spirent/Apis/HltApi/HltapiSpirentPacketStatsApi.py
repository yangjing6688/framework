from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketStatsApi import PacketStatsApi, PacketStatsConstants

"""
    This is the API class for the command: packet_stats

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentPacketStatsApi(PacketStatsApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentPacketStatsApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_stats
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketStatsConstants.PACKET_STATS_API)
        api.packet_stats(dummyDict)
    """
    def packet_stats(self, argdictionary):
        return super(SpirentPacketStatsApi, self).packet_stats(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_stats_chunk_size(self, size):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_dirname(self, path):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_ethernet_type(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_enable_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_ethernet_type(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_frame_id_end(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_frame_id_start(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_framesize(self, size):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_packet_type(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_pattern(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_stats_pattern_offset(self, type):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {PacketStatsConstants.ACTION_CMD, PacketStatsConstants.FILENAME_CMD, PacketStatsConstants.FORMAT_CMD, PacketStatsConstants.PORT_HANDLE_CMD, PacketStatsConstants.STOP_CMD}
