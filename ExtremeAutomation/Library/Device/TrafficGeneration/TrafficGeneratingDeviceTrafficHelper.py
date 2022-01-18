import abc
from ExtremeAutomation.Library.Logger.Logger import Logger


class TrafficGeneratingDeviceTrafficHelper(object, metaclass=abc.ABCMeta):
    def __init__(self, ixia_device):
        self.dev = ixia_device
        self.logger = Logger()

    @abc.abstractmethod
    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    @abc.abstractmethod
    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_sender_address_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_source_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_target_address_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_target_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        return self.logger.log_unimplemented_method()
