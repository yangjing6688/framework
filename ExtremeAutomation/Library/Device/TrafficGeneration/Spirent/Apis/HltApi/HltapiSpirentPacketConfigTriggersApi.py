from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigTriggersApi import PacketConfigTriggersApi, PacketConfigTriggersConstants

"""
    This is the API class for the command: packet_config_triggers

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SpirentPacketConfigTriggersApi(PacketConfigTriggersApi):

    """
    init function
    """
    def __init__(self, device):
        super(SpirentPacketConfigTriggersApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: packet_config_triggers
    use this by passing in a dict() of all the commands

        api = device.getApi(PacketConfigTriggersConstants.PACKET_CONFIG_TRIGGERS_API)
        api.packet_config_triggers(dummyDict)
    """
    def packet_config_triggers(self, argdictionary):
        return super(SpirentPacketConfigTriggersApi, self).packet_config_triggers(argdictionary, self.supportedSpirentHltapiCommands)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def packet_config_triggers_async_trigger1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger1_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_async_trigger2_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_expression_string(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_filter_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_expression_string(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_capture_trigger_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_handle(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_mode(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds1_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_DA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_SA(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_error(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize_from(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_framesize_to(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def packet_config_triggers_uds2_pattern(self, opt):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


    supportedSpirentHltapiCommands = {PacketConfigTriggersConstants.PORT_HANDLE_CMD}
