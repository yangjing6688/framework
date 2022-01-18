from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceTrafficHelper import \
    TrafficGeneratingDeviceTrafficHelper
# from ostinato.core import ost_pb, DroneProxy
# from ostinato.protocols.ip4_pb2 import ip4, Ip4
# from ostinato.protocols.ip6_pb2 import ip6, Ip6
# from ostinato.protocols.arp_pb2 import arp, Arp
# from ostinato.protocols.mac_pb2 import mac, Mac
# from ostinato.protocols.protocol_pb2 import StreamControl, StreamCore, PortIdList, StreamIdList, Stream


class JetsDeviceTrafficHelper(TrafficGeneratingDeviceTrafficHelper):
    def __init__(self, ixia_device):
        super(JetsDeviceTrafficHelper, self).__init__(ixia_device)
        self.dev = ixia_device

    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_source_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_target_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_sender_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_arp_target_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        return self.logger.log_unimplemented_method()
