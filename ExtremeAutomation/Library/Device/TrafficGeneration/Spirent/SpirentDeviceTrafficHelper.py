from ExtremeAutomation.Library.Device.TrafficGeneration.HltapiTrafficGeneratingDeviceTrafficHelper import \
    HltapiTrafficGeneratingDeviceTrafficHelper


class SpirentDeviceTrafficHelper(HltapiTrafficGeneratingDeviceTrafficHelper):
    def __init__(self, smartbits_device):
        super(SpirentDeviceTrafficHelper, self).__init__(smartbits_device)

    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_mac_dst_options(port_string, port_name_stream, addr,
                                                                                 mode, count, step, seed, options)

    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_mac_src_options(port_string, port_name_stream, addr,
                                                                                 mode, count, step, seed, options)

    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_ip_dst_options(port_string, port_name_stream, addr,
                                                                                mode, count, step, options)

    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_ip_src_options(port_string, port_name_stream, addr,
                                                                                mode, count, step, options)

    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_ipv6_dst_options(port_string, port_name_stream, addr,
                                                                                  mode, count, step, options)

    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_ipv6_src_options(port_string, port_name_stream, addr,
                                                                                  mode, count, step, options)

    def configure_stream_arp_sender_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_arp_sender_hardware_options(port_string,
                                                                                             port_name_stream,
                                                                                             addr, mode, count)

    def configure_stream_arp_target_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        port_name_stream = "$" + self.convert_port_string_to_variable(port_string, stream_id)
        super(SpirentDeviceTrafficHelper, self).configure_stream_arp_target_hardware_options(port_string,
                                                                                             port_name_stream,
                                                                                             addr, mode, count, options)

    def configure_stream_fcs_dribble(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_alignment(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_jabber(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_bad_packet(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_good_packet(self, port_string, stream_id, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()
