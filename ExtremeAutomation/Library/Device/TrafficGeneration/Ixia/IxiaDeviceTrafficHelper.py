from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceTrafficHelper import \
    HltapiTrafficGeneratingDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaStreamConfigIxTclHalApi import \
    IxiaStreamConfigIxTclHalApi


class IxiaDeviceTrafficHelper(HltapiTrafficGeneratingDeviceTrafficHelper):
    def __init__(self, ixia_device):
        super(IxiaDeviceTrafficHelper, self).__init__(ixia_device)

    def configure_stream_fcs_dribble(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.configure_stream_fcs_dribble(port_string, stream_id, IxiaDeviceConstants.FCS_DRIBBLE_ERROR)

    def configure_stream_fcs_alignment(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.configure_stream_fcs_alignment(port_string, stream_id, IxiaDeviceConstants.FCS_ALIGN_ERROR)

    def configure_stream_fcs_jabber(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_none(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.configure_stream_fcs_none(port_string, stream_id, IxiaDeviceConstants.FCS_NONE)

    def configure_stream_arp_source_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.configure_stream_arp_source_protocol_options(port_string, stream_id, addr, mode, count)

    def configure_stream_arp_target_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        api = self.get_api(IxiaDeviceConstants.IXIA_STREAM_CONFIG_IX_TCL_HAL_API)
        assert isinstance(api, IxiaStreamConfigIxTclHalApi)
        cmd_obj = api.configure_stream_arp_target_protocol_options(port_string, stream_id, addr, mode, count)
