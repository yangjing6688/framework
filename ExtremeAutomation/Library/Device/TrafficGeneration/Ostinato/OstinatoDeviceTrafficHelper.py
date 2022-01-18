from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb, DroneProxy
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.ip4_pb2 import ip4, Ip4
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.ip6_pb2 import ip6, Ip6
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.arp_pb2 import arp, Arp
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.mac_pb2 import mac, Mac
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.protocol_pb2 import StreamIdList
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceTrafficHelper import TrafficGeneratingDeviceTrafficHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.Ipv6Address import Ipv6Address
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress


class OstinatoDeviceTrafficHelper(TrafficGeneratingDeviceTrafficHelper):
    def __init__(self, ixia_device):
        super(OstinatoDeviceTrafficHelper, self).__init__(ixia_device)
        self.dev = ixia_device

    def configure_stream_mac_dst_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kMacFieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[mac]
        assert isinstance(ip, Mac)
        if addr:
            ip.dst_mac = EnetAddress.to_long(addr)
        if mode == TrafficConfigConstants.MAC_DST_MODE_INCREMENT or 'incr' in mode.lower():
            ip.dst_mac_mode = Mac.e_mm_inc
        elif mode == TrafficConfigConstants.MAC_DST_MODE_DECREMENT or 'decr' in mode.lower():
            ip.dst_mac_mode = Mac.e_mm_dec
        elif mode == TrafficConfigConstants.MAC_DST_MODE_RANDOM or 'rand' in mode.lower():
            ip.dst_mac_mode = Mac.e_mm_resolve
        else: # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            ip.dst_mac_mode = Mac.e_mm_fixed
        if count:
            ip.dst_mac_count = count
        if step:
            ip.dst_mac_step = int(EnetAddress.to_long(step))  # make this an int
        drone.modifyStream(stream_cfg)

    def configure_stream_mac_src_options(self, port_string, stream_id, addr, mode, count, step, seed=None,
                                         options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kMacFieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[mac]
        assert isinstance(ip, Mac)
        if addr:
            ip.src_mac = EnetAddress.to_long(addr)
        if mode == TrafficConfigConstants.MAC_SRC_MODE_INCREMENT or 'incr' in mode.lower():
            ip.src_mac_mode = Mac.e_mm_inc
        elif mode == TrafficConfigConstants.MAC_SRC_MODE_DECREMENT or 'decr' in mode.lower():
            ip.src_mac_mode = Mac.e_mm_dec
        elif mode == TrafficConfigConstants.MAC_SRC_MODE_RANDOM or 'rand' in mode.lower():
            ip.src_mac_mode = Mac.e_mm_resolve
        else: # if mode == TrafficConfigConstants.MAC_SRC_MODE_FIXED:
            ip.src_mac_mode = Mac.e_mm_fixed
        if count:
            ip.src_mac_count = count
        if step:
            ip.src_mac_step = int(EnetAddress.to_long(step))  # make this an int
        drone.modifyStream(stream_cfg)

    def configure_stream_ip_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kIp4FieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[ip4]
        assert isinstance(ip, Ip4)
        if addr:
            ip.dst_ip = Ipv4Address.to_long(addr)
        if mode == TrafficConfigConstants.IP_DST_MODE_INCREMENT or 'incr' in mode.lower():
            ip.dst_ip_mode = Ip4.e_im_inc_host
        elif mode == TrafficConfigConstants.IP_DST_MODE_DECREMENT or 'decr' in mode.lower():
            ip.dst_ip_mode = Ip4.e_im_dec_host
        elif mode == TrafficConfigConstants.IP_DST_MODE_RANDOM or 'rand' in mode.lower():
            ip.dst_ip_mode = Ip4.e_im_random_host
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            ip.dst_ip_mode = Ip4.e_im_fixed
        if count:
            ip.dst_ip_count = count
        if step:
            ip.dst_ip_mask = Ipv4Address.to_long(step)  # make this an int
        drone.modifyStream(stream_cfg)

    def __get_protocol_class_from_stream_cfg(self, stream_cfg, extention_id):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        if stream_cfg:
            stream = stream_cfg.stream[0]
            for protocol in stream.protocol:
                if protocol.protocol_id.id == extention_id:
                    p = protocol
                    break
        return p

    def configure_stream_ip_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kIp4FieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[ip4]
        assert isinstance(ip, Ip4)
        if mode == TrafficConfigConstants.IP_SRC_MODE_INCREMENT or 'incr' in mode.lower():
            ip.src_ip_mode = Ip4.e_im_inc_host
        elif mode == TrafficConfigConstants.IP_SRC_MODE_DECREMENT or 'decr' in mode.lower():
            ip.src_ip_mode = Ip4.e_im_dec_host
        elif mode == TrafficConfigConstants.IP_SRC_MODE_RANDOM or 'rand' in mode.lower():
            ip.src_ip_mode = Ip4.e_im_random_host
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            ip.src_ip_mode = Ip4.e_im_fixed
        ip.src_ip_count = count
        ip.src_ip_mask = Ipv4Address.to_long(step)
        drone.modifyStream(stream_cfg)

    def configure_stream_ipv6_dst_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kIp6FieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[ip6]
        assert isinstance(ip, Ip6)
        if addr:
            ip.dst_addr_hi = Ipv6Address.to_long_upper(addr)
            ip.dst_addr_lo = Ipv6Address.to_long_lower(addr)
        if mode == TrafficConfigConstants.IPV6_DST_MODE_INCREMENT or 'incr' in mode.lower():
            ip.dst_addr_mode = Ip6.kIncHost
        elif mode == TrafficConfigConstants.IPV6_DST_MODE_DECREMENT or 'decr' in mode.lower():
            ip.dst_addr_mode = Ip6.kDecHost
        elif mode == TrafficConfigConstants.IPV6_DST_MODE_RANDOM or 'rand' in mode.lower():
            ip.dst_addr_mode = Ip6.kRandomHost
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            ip.dst_addr_mode = Ip6.kFixed
        if count:
            ip.dst_addr_count = count
        # if step:
        #     ip.src_addr_prefix = Ipv6Address.to_long(step)  # make this an int
        drone.modifyStream(stream_cfg)

    def configure_stream_ipv6_src_options(self, port_string, stream_id, addr, mode, count, step, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kIp6FieldNumber)
        if not p:
            # log error
            return
        ip = p.Extensions[ip6]
        assert isinstance(ip, Ip6)
        if addr:
            ip.src_addr_hi = Ipv6Address.to_long_upper(addr)
            ip.src_addr_lo = Ipv6Address.to_long_lower(addr)
        if mode == TrafficConfigConstants.IPV6_DST_MODE_INCREMENT or 'incr' in mode.lower():
            ip.src_addr_mode = Ip6.kIncHost
        elif mode == TrafficConfigConstants.IPV6_DST_MODE_DECREMENT or 'decr' in mode.lower():
            ip.src_addr_mode = Ip6.kDecHost
        elif mode == TrafficConfigConstants.IPV6_DST_MODE_RANDOM or 'rand' in mode.lower():
            ip.src_addr_mode = Ip6.kRandomHost
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            ip.src_addr_mode = Ip6.kFixed
        if count:
            ip.src_addr_count = count
        # if step:
        #     ip.src_addr_prefix = Ipv6Address.to_long(step)  # make this an int
        drone.modifyStream(stream_cfg)

    def configure_stream_arp_source_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kArpFieldNumber)
        if not p:
            # log error
            return
        arpField = p.Extensions[arp]
        assert isinstance(arpField, Arp)

        if addr:
            arpField.sender_proto_addr = Ipv4Address.to_long(addr)
        if mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'incr' in mode.lower():
            arpField.sender_proto_addr_mode = Arp.kIncrementHost
        elif mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'decr' in mode.lower():
            arpField.sender_proto_addr_mode = Arp.kDecrementHost
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            arpField.sender_proto_addr_mode = Arp.kFixedHost
        if count:
            arpField.sender_proto_addr_count = int(count)
        drone.modifyStream(stream_cfg)

    def configure_stream_arp_target_protocol_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kArpFieldNumber)
        if not p:
            # log error
            return
        arpField = p.Extensions[arp]
        assert isinstance(arpField, Arp)

        if addr:
            arpField.target_proto_addr = Ipv4Address.to_long(addr)
        if mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'incr' in mode.lower():
            arpField.target_proto_addr_mode = Arp.kIncrementHost
        elif mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'decr' in mode.lower():
            arpField.target_proto_addr_mode = Arp.kDecrementHost
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            arpField.target_proto_addr_mode = Arp.kFixedHost
        if count:
            arpField.target_proto_addr_count = int(count)
        drone.modifyStream(stream_cfg)

    def configure_stream_arp_sender_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kArpFieldNumber)
        if not p:
            # log error
            return
        arpField = p.Extensions[arp]
        assert isinstance(arpField, Arp)

        if addr:
            arpField.sender_hw_addr = int(addr.replace(":", ""), 16)
        if mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'incr' in mode.lower():
            arpField.sender_hw_addr_mode = Arp.kIncrement
        elif mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'decr' in mode.lower():
            arpField.sender_hw_addr_mode = Arp.kDecrement
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            arpField.sender_hw_addr_mode = Arp.kFixed
        if count:
            arpField.sender_hw_addr_count = int(count)
        drone.modifyStream(stream_cfg)

    def configure_stream_arp_target_hardware_options(self, port_string, stream_id, addr, mode, count, options=None):
        if options is None:
            options = {}
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        stream_cfg = self.__get_stream_cfg_class(port_string, stream_id)
        p = self.__get_protocol_class_from_stream_cfg(stream_cfg, ost_pb.Protocol.kArpFieldNumber)
        if not p:
            # log error
            return
        arpField = p.Extensions[arp]
        assert isinstance(arpField, Arp)

        if addr:
            arpField.target_hw_addr = int(addr.replace(":", ""), 16)
        if mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'incr' in mode.lower():
            arpField.target_hw_addr_mode = Arp.kIncrement
        elif mode == TrafficConfigConstants.ARP_DST_HW_MODE_CMD or 'decr' in mode.lower():
            arpField.target_hw_addr_mode = Arp.kDecrement
        else:  # if mode == TrafficConfigConstants.IP_DST_MODE_FIXED:
            arpField.target_hw_addr_mode = Arp.kFixed
        if count:
            arpField.target_hw_addr_count = int(count)
        drone.modifyStream(stream_cfg)

    def __get_stream_cfg_class(self, port_string, stream_id):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        if isinstance(stream_id, StreamIdList):
            sids.stream_id.add().id = stream_id.stream_id[0].id
        else:
            sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        return scfgs
        # stream = scfgs.stream[0]
        #
        # streams = drone.getStreamIdList(port_string.port_id[0])
        # stream_cfg = None
        # for stream in streams.stream_id:
        #     if stream.id == stream_id:
        #         stream_cfg = drone.getStreamConfig(streams)
        #         break
        # return stream_cfg

    def __get_stream_class(self, port_string, stream_id):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        stream = scfgs.stream[0]
        return stream

    def __get_protocol_class(self, port_string, stream_id, extention_id):
        drone = self.connection
        assert isinstance(drone, DroneProxy)
        port_string = self.ostinato_port_number_to_port(port_string)
        sids = ost_pb.StreamIdList()
        sids.port_id.id = port_string.port_id[0].id
        sids.stream_id.add().id = stream_id
        scfgs = drone.getStreamConfig(sids)
        stream = scfgs.stream[0]
        p = None
        for protocol in stream.protocol:
            if protocol.protocol_id.id == extention_id:
                p = protocol
                break
        return p
