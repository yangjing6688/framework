from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.mac_pb2 import mac
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants, PacketConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject


class EthernetPacketHeader(object):
    def __init__(self):
        self.add_enet_header()
        self.HEADER_SIZE_ETHERNET = 12  # bytes

    def add_enet_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ETHER)

    def config_thirdparty_traffic_generator_stream_ether(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ether(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ether(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_SCAPY:
            self.config_scapy_stream_ether(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ether(self, generator_ref, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kMacFieldNumber
        if self.is_field_set(self.get_destination_mac()):
            p.Extensions[mac].dst_mac = int(self.get_destination_mac().replace(":", ""), 16)
        if self.is_field_set(self.get_source_mac()):
            p.Extensions[mac].src_mac = int(self.get_source_mac().replace(":", ""), 16)

    def config_jets_stream_ether(self, jets_dev, port_string, stream_id, **kwargs):
        """
        ENET_HDR
        {
            dst: 48: default = 0xFFFFFFFFFFFF, display = "Destination %mac",
                     tags = ("Destination Address"), index = 1;
        src: 48: display = "Source %mac", tags = ("Source Address"), index = 2;

        type: 16: send = length(pdu, pdu) - 14, display = "Ethertype", index = 3;
        """
        pkt_field = {}
        if self.is_field_set(self.get_destination_mac()):
            pkt_field["dst"] = str(self.get_destination_mac())
        if self.is_field_set(self.get_source_mac()):
            pkt_field["src"] = str(self.get_source_mac())
        jets_dev.pdl_add_packet_header("ENET_HDR", pkt_field)

    def config_scapy_stream_ether(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_field = {}
        if self.is_field_set(self.get_destination_mac()):
            pkt_field["dst"] = str(self.get_destination_mac())
        if self.is_field_set(self.get_source_mac()):
            pkt_field["src"] = str(self.get_source_mac())
        jets_dev.pdl_add_packet_header("Ether", pkt_field)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "").upper()
        # da = 48bits
        da = self.get_bits_from_string(48, payload)
        self.set_destination_mac(da)
        payload = self.remove_bits_from_string(48, payload)
        # sa = 48bits
        sa = self.get_bits_from_string(48, payload)
        self.set_source_mac(sa)
        payload = self.remove_bits_from_string(48, payload)
        self.payload = payload

    def get_header_bytes(self):
        da = self.format_byte_string(self.get_destination_mac(), PacketConstants.ENET_ADDRESS, 12)
        sa = self.format_byte_string(self.get_source_mac(), PacketConstants.ENET_ADDRESS, 12)
        return da + " " + sa

    @staticmethod
    def compare_ethernet_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                       print_failures=True):
        results = True
        try:
            assert isinstance(expected, EthernetPacketHeader)
            assert isinstance(actual, EthernetPacketHeader)
            if expected.do_i_check_this_field(expected.get_destination_mac(),
                                              EthernetPacketConstants.ETHER_DESTINATION_ADDRESS, ignore_list,
                                              include_list):
                if expected.get_destination_mac() != actual.get_destination_mac():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error("Destination Address: " + str(expected.get_destination_mac()) +
                                                      " != " + str(actual.get_destination_mac()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info("Destination Address: " + str(expected.get_destination_mac()) +
                                                 " == " + str(actual.get_destination_mac()) + " Pass")
            if expected.do_i_check_this_field(expected.get_source_mac(), EthernetPacketConstants.ETHER_SOURCE_ADDRESS,
                                              ignore_list, include_list):
                if expected.get_source_mac() != actual.get_source_mac():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error("Source Address: " + str(expected.get_source_mac()) + " != " +
                                                      str(actual.get_source_mac()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info("Source Address: " + str(expected.get_source_mac()) + " == " +
                                                 str(actual.get_source_mac()) + " Pass")
        except Exception as e:
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("EthernetPacketHeader failed")
            results = False
        return results
