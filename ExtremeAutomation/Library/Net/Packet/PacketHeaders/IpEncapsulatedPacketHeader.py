import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6Packet import Ethernet2IpV6Packet
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class IpEncapsulatedPacketHeader(InnerPacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    IP Encapsulation Packet Header
    """

    def __init__(self):
        self.add_encapsulated_header()
        self.innerpacket = None
        self.HEADER_SIZE_ENCAPSULATED = 0  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################
    # start inner packet methods
    #  routing is a 32 bit INTEGER example: 1
    def set_inner_packet(self, innerpacket, ignore_check=False):
        # routing = self.normalize_value(routing, PacketConstants.INTEGER)
        # self.set_packet_component(PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING, routing)
        self.innerpacket = innerpacket

    def get_inner_packet(self):
        # return self.normalize_value(self.get_packet_component(
        #     PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)
        self.innerpacket.set_destination_mac(self.get_destination_mac())
        self.innerpacket.set_source_mac(self.get_source_mac())
        return self.innerpacket
    # end inner packet methods

    def get_inner_packet_length(self):
        pkt_buffer = self.innerpacket.get_header_length()  # add the CRC
        remove_l2 = len("000000000000" + "000000000000" + "0800") / 2
        minsize = 64
        # return max(buffer-remove_l2, minsize-remove_l2)
        return pkt_buffer - remove_l2

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        p = self.get_inner_packet()
        ip_string = p.to_packet_string()
        if "IPV4 HEADER" in ip_string:
            ip_string = "INNER IPV4 HEADER" + ip_string.split("IPV4 HEADER")[1]
        if "IPV6 HEADER" in ip_string:
            ip_string = "INNER IPV6 HEADER" + ip_string.split("IPV6 HEADER")[1]
        return "\n\n" + ip_string

    def add_encapsulated_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ENCAPSULATED)

    def build(self):
        self.add_encapsulated_header()
        if isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header(0x04, True)
        elif isinstance(self, IpV4PacketHeader):
            self.set_ip_protocol(0x04, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_encapsulated(self, tgen_type, generator_ref, port_string, stream_id,
                                                                **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_encapsulated(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_encapsulated(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_encapsulated(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    # update this from the ostinato docs.
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = IpEncapsulatedPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jets_stream_encapsulated(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + IpEncapsulatedPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_encapsulated_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = IpEncapsulatedPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        if payload.startswith("4"):
            packet = Ethernet2IpV4Packet()
            payload = "000000000000" + "000000000000" + "0800" + payload
            packet.set_payload(payload)
        elif payload.startswith("6"):
            packet = Ethernet2IpV6Packet()
            payload = "000000000000" + "000000000000" + "86DD" + payload
            packet.set_payload(payload)
        # might want to match the tag types here with the outside packet.
        self.set_inner_packet(packet)

    def get_header_bytes(self):
        ret_string = ""
        packet = self.get_inner_packet()
        ret_string = packet.get_bytes()
        return ret_string[28::]

    @staticmethod
    def compare_inner_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                    print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IpEncapsulatedPacketHeader)
            assert isinstance(actual, IpEncapsulatedPacketHeader)
            if expected.do_i_check_this_field(expected.get_inner_packet(),
                                              EncapsulatedPacketConstants.IP_ENCAP_INNER_PACKET,
                                              ignore_list, include_list):
                name = "Ip/Ip Inner packet : "
                expected_inner = expected.get_inner_packet()
                actual_inner = actual.get_inner_packet()
                results_print = PacketConstants.PRINT_FLAG_NONE
                if print_results:
                    results_print = PacketConstants.PRINT_FLAG_EVERYTHING
                elif print_failures:
                    results_print = PacketConstants.PRINT_FLAG_ERRORS
                if not expected_inner.compare_packet_fields(actual_inner, False, ignore_list, include_list,
                                                            dynamic_entries, results_print):
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error("Inner Packet ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + "Inner Packet Pass")
        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with EncapsulatedPacketHeader")
        return results


class EncapsulatedPacketConstants:
    def __init__(self):
        pass

    IP_ENCAP_INNER_PACKET = "IP_ENCAP_INNER_PACKET"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
