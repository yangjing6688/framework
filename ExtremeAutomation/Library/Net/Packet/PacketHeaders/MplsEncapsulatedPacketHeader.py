import binascii
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump


class MplsEncapsulatedPacketHeader(InnerPacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    MPLS Encapsulated Packet Header
        # PW = 32bits
    """

    def __init__(self):
        self.add_mplsencapsulated_header()
        self.innerpacket = None
        self.HEADER_SIZE_MPLSENCAPSULATED = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start MplsEncapsulated PW methods
    #  pw is a 32 bit INTEGER example: 1
    def set_mplsencapsulated_pw(self, pw, ignore_check=False):
        pw = self.normalize_value(pw, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MPLSENCAPSULATED,
                                  MplsEncapsulatedPacketConstants.MPLSENCAPSULATED_PW, pw)

    def get_mplsencapsulated_pw(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MPLSENCAPSULATED, MplsEncapsulatedPacketConstants.MPLSENCAPSULATED_PW),
            PacketConstants.INTEGER)

    def get_mplsencapsulated_pw_hltapi_cmd(self, dummy_dict):
        pw = self.get_mplsencapsulated_pw()
        if isinstance(pw, int):
            pw = str(pw)
        if pw and 'Not Set' not in pw:
            dummy_dict[TrafficConfigConstants.TEMP_PW_CMD] = pw
    # end MplsEncapsulated PW methods

    # start vxlan inner packet methods
    #  routing is a 32 bit INTEGER example: 1
    def set_mpls_inner_packet(self, innerpacket, ignore_check=False):
        # routing = self.normalize_value(routing, PacketConstants.INTEGER)
        # self.set_packet_component(PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING, routing)
        self.innerpacket = innerpacket

    def get_mpls_inner_packet(self):
        # return self.normalize_value(self.get_packet_component(
        #     PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)
        return self.innerpacket

    def get_inner_packet(self):
        return self.get_mpls_inner_packet()

        # def get_gre_inner_packet_hltapi_cmd(self, dummy_dict):
        #     routing = self.get_gre_routing()
        #     if isinstance(routing, int):
        #         routing = str(routing)
        #     if routing and 'Not Set' not in routing:
        #         dummy_dict[TrafficConfigConstants.TEMP_ROUTING_CMD] = routing
        # end Gre routing methods

    def get_mpls_inner_packet_length(self):
        pkt_buffer = self.innerpacket.get_header_length()  # + 4# add the CRC
        minsize = 64
        if isinstance(self, TaggedPacketHeader):
            minsize += 4
        elif isinstance(self, VlanStackPacketHeader):
            minsize += (4 * self.get_vlan_num())
        return max(pkt_buffer, minsize)

    def get_inner_packet_length(self):
        return self.get_mpls_inner_packet_length()

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("PW", self.format_int(self.get_mplsencapsulated_pw(), 4))
        return "\n\nMPLSENCAPSULATED HEADER" + table.to_table_string() + "\n\nInner Packet\n" + \
               self.get_mpls_inner_packet().to_packet_string()

    def add_mplsencapsulated_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_MPLSENCAPSULATED)

    def build(self):
        self.add_mplsencapsulated_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_mplsencapsulated_pw_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_mplsencapsulated(self, tgen_type, generator_ref, port_string,
                                                                    stream_id, **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_mplsencapsulated(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_mplsencapsulated(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_mplsencapsulated(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = MplsEncapsulatedPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jets_stream_mplsencapsulated(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "MPLSENCAPSULATED_HDR"
        pkt_bytes = "0x" + MplsEncapsulatedPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_mplsencapsulated_pw()) :
        #     pkt_fields["pw"] = int(self.get_mplsencapsulated_pw())

        if self.is_field_set(self.get_mpls_inner_packet()):
            inner_packet = self.get_mpls_inner_packet()
            jets_dev.pdl_down_encap_level()
            inner_packet.config_thirdparty_traffic_generator_stream(EthernetPacketConstants.TRAFFIC_GENERATION_JETS,
                                                                    jets_dev, port_string, stream_id, **kwargs)
            jets_dev.pdl_up_encap_level()

    def get_ixtclhal_mplsencapsulated_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        pw = self.get_bits_from_string(32, payload)
        self.set_mplsencapsulated_pw("0x" + pw)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload
        packet = EthernetPacket()
        packet.set_payload(payload)
        self.set_mpls_inner_packet(packet)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_mplsencapsulated_pw(), PacketConstants.INTEGER, 32)
        ret_string += self.get_mpls_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_mplsencapsulated_packet_header(expected, actual, ignore_list=None, include_list=None,
                                               dynamic_entries=None, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, MplsEncapsulatedPacketHeader)
            assert isinstance(actual, MplsEncapsulatedPacketHeader)
            if expected.is_field_set(expected.get_mplsencapsulated_pw()) and \
                    MplsEncapsulatedPacketConstants.MPLSENCAPSULATED_PW not in ignore_list:
                name = "MPLSENCAPSULATED pw : "
                if expected.get_mplsencapsulated_pw() != actual.get_mplsencapsulated_pw():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_mplsencapsulated_pw()) + " != " +
                                                      str(actual.get_mplsencapsulated_pw()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mplsencapsulated_pw()) + " == " +
                                                 str(actual.get_mplsencapsulated_pw()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vxlan_inner_packet(),
                                              MplsEncapsulatedPacketConstants.MPLSENCAPSULATED_INNER_PACKET,
                                              ignore_list, include_list):
                name = "Mpls Inner packet : "
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
                PacketObject.logger.log_error("Error with MplsEncapsulatedPacketHeader")
        return results


class MplsEncapsulatedPacketConstants:
    def __init__(self):
        pass

    MPLSENCAPSULATED_PW = "MPLSENCAPSULATED_PW"
    MPLSENCAPSULATED_INNER_PACKET = "MPLSENCAPSULATED_INNER_PACKET"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
