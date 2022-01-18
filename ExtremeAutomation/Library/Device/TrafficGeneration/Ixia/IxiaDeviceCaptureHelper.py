from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaCaptureIxTclHalApi import \
    IxiaCaptureIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceCaptureHelper import \
    HltapiTrafficGeneratingDeviceCaptureHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants


class IxiaDeviceCaptureHelper(HltapiTrafficGeneratingDeviceCaptureHelper):
    def __init__(self, ixia_device):
        super(IxiaDeviceCaptureHelper, self).__init__(ixia_device)

    def get_captured_frame_count(self, port_string, options=None):
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_CAPTURE_IX_TCL_HAL_API")
        assert isinstance(api, IxiaCaptureIxTclHalApi)
        return api.get_captured_frame_count(port_string)

    def get_running_captured_frame_count(self, port_handle, options=None):
        frame_count = self.get_captured_frame_count(port_handle)
        frame_count = frame_count.strip()
        try:
            return int(frame_count)
        except:
            return 0

    def get_captured_frame_status(self, port_string, frame_num):
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_CAPTURE_IX_TCL_HAL_API")
        assert isinstance(api, IxiaCaptureIxTclHalApi)
        return api.get_captured_frame_status(port_string, frame_num)

    def get_captured_frame(self, port_string, frame_num, options=None):
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_CAPTURE_IX_TCL_HAL_API")
        assert isinstance(api, IxiaCaptureIxTclHalApi)
        return api.get_captured_packet(port_string, frame_num)

    def get_captured_frames(self, port_string, first_frame_num, last_frame_num, options=None):
        # port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api("IXIA_CAPTURE_IX_TCL_HAL_API")
        assert isinstance(api, IxiaCaptureIxTclHalApi)
        return api.get_captured_packets(port_string, first_frame_num, last_frame_num)

    def get_capture_filter_and_trigger_settings(self, port_string):
        api = self.dev.get_api(IxiaDeviceConstants.IXIA_FILER_IX_TCL_HAL_API)
        ret_string = "Port " + str(port_string) + "\nCapture Filters:"
        ret_string += api.get_capture_filter_settings(port_string)
        ret_string += "\nCapture Trigger:"
        api = self.dev.get_api(IxiaDeviceConstants.IXIA_FILER_PALLETTE_IX_TCL_HAL_API)
        ret_string += api.get_capture_filter_pallette_settings(port_string)

        return ret_string
