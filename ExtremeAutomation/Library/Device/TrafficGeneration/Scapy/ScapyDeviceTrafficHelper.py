from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceTrafficHelper import \
    TrafficGeneratingDeviceTrafficHelper


class ScapyDeviceTrafficHelper(TrafficGeneratingDeviceTrafficHelper):
    def __init__(self, ixia_device):
        super(ScapyDeviceTrafficHelper, self).__init__(ixia_device)
        self.dev = ixia_device

    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def __get_protocol_class_from_stream_cfg(self, stream_cfg, extention_id):
        return self.logger.log_unimplemented_method()

    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def __get_stream_cfg_class(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def __get_stream_class(self, port_string, stream_id):
        return self.logger.log_unimplemented_method()

    def __get_protocol_class(self, port_string, stream_id, extention_id):
        return self.logger.log_unimplemented_method()
