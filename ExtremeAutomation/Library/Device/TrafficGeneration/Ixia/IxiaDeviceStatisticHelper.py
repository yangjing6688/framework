from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaStatisticsIxTclHal import \
    IxiaStatisticsIxTclHal
from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceStatisticHelper import \
    HltapiTrafficGeneratingDeviceStatisticHelper


class IxiaDeviceStatisticHelper(HltapiTrafficGeneratingDeviceStatisticHelper):
    def __init__(self, ixia_device):
        super(IxiaDeviceStatisticHelper, self).__init__(ixia_device)

    def get_port_statistic_capture_filter_count(self, port_string, options=None):
        if options is None:
            options = {}
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_STATISTIC_IX_TCL_HAL_API")
        assert isinstance(api, IxiaStatisticsIxTclHal)
        return api.get_capture_filter_statistic(port_string)

    def get_port_statistic_capture_trigger_count(self, port_string, options=None):
        if options is None:
            options = {}
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_STATISTIC_IX_TCL_HAL_API")
        assert isinstance(api, IxiaStatisticsIxTclHal)
        return api.get_capture_trigger_statistic(port_string)

    def get_port_statistic_capture_filter_rate(self, port_string, options=None):
        if options is None:
            options = {}
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_STATISTIC_IX_TCL_HAL_API")
        assert isinstance(api, IxiaStatisticsIxTclHal)
        return api.get_capture_filter_rate(port_string)

    def get_port_statistic_capture_trigger_rate(self, port_string, options=None):
        if options is None:
            options = {}
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_STATISTIC_IX_TCL_HAL_API")
        assert isinstance(api, IxiaStatisticsIxTclHal)
        return api.get_capture_trigger_rate(port_string)
