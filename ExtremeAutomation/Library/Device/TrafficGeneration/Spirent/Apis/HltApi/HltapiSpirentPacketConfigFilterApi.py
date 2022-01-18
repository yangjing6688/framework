from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigFilterApi import PacketConfigFilterApi, PacketConfigFilterConstants

"""
    This is the API class for the command: packet_config_filter

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentPacketConfigFilterApi(PacketConfigFilterApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentPacketConfigFilterApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_filter
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigFilterConstants.PACKET_CONFIG_FILTER_API)
        api.packet_config_filter(dummyDict)
    """
    def packet_config_filter(self, argdictionary):
        return super(SpirentPacketConfigFilterApi, self).packet_config_filter(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_filter_DA1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA_mask1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_DA_mask2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA_mask1(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_SA_mask2(self, mac):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_bad_fcs_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_eHec_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_error_condition(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_payload_crc(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_gfp_tHec_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_match_type1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_match_type2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_no_write(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern1(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern2(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_atm(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask1(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask2(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_mask_atm(self, hex):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset1(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset2(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_atm(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_type1(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_pattern_offset_type2(self, num):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vci(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vci_count(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vci_step(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi_count(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_filter_vpi_step(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {PacketConfigFilterConstants.PORT_HANDLE_CMD}
