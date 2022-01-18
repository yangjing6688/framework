import binascii
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class VxlanPacketHeader(InnerPacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    VxLAN Packet Header
        # flags = 16bits
        # group policy id = 16bits
        # vxlan network identifier = 24bits
        # reserved = 8bits

        ##this might be wrong, it might be:
        # flags = 8bits
        # group policy id = 24bits
        # vxlan network identifier = 24bits
        # reserved = 8bits
    """

    def __init__(self):
        self.add_vxlan_header()
        self.innerpacket = None
        self.HEADER_SIZE_VXLAN = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Vxlan flags methods
    #  flags is a 16 bit INTEGER example: 1
    def set_vxlan_flags(self, flags, ignore_check=False):
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_FLAGS, flags)

    def get_vxlan_flags(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_FLAGS), PacketConstants.INTEGER)

    def get_vxlan_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_vxlan_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_CMD] = flags
    # end Vxlan flags methods

    # start Vxlan group policy id methods
    #  group_policy_id is a 16 bit INTEGER example: 1
    def set_vxlan_group_policy_id(self, group_policy_id, ignore_check=False):
        group_policy_id = self.normalize_value(group_policy_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_VXLAN,
                                  VxlanPacketConstants.VXLAN_GROUP_POLICY_ID, group_policy_id)

    def get_vxlan_group_policy_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_GROUP_POLICY_ID),
            PacketConstants.INTEGER)

    def get_vxlan_group_policy_id_hltapi_cmd(self, dummy_dict):
        group_policy_id = self.get_vxlan_group_policy_id()
        if isinstance(group_policy_id, int):
            group_policy_id = str(group_policy_id)
        if group_policy_id and 'Not Set' not in group_policy_id:
            dummy_dict[TrafficConfigConstants.TEMP_GROUP_POLICY_ID_CMD] = group_policy_id
    # end Vxlan group policy id methods

    # start Vxlan vxlan network identifier methods
    #  vxlan_network_identifier is a 24 bit INTEGER example: 1
    def set_vxlan_vxlan_network_identifier(self, vxlan_network_identifier, ignore_check=False):
        vxlan_network_identifier = self.normalize_value(vxlan_network_identifier, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_VXLAN,
                                  VxlanPacketConstants.VXLAN_VXLAN_NETWORK_IDENTIFIER, vxlan_network_identifier)

    def get_vxlan_vxlan_network_identifier(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_VXLAN_NETWORK_IDENTIFIER),
            PacketConstants.INTEGER)

    def get_vxlan_vxlan_network_identifier_hltapi_cmd(self, dummy_dict):
        vxlan_network_identifier = self.get_vxlan_vxlan_network_identifier()
        if isinstance(vxlan_network_identifier, int):
            vxlan_network_identifier = str(vxlan_network_identifier)
        if vxlan_network_identifier and 'Not Set' not in vxlan_network_identifier:
            dummy_dict[TrafficConfigConstants.TEMP_VXLAN_NETWORK_IDENTIFIER_CMD] = vxlan_network_identifier
    # end Vxlan vxlan network identifier methods

    # start Vxlan reserved methods
    #  reserved is a 8 bit INTEGER example: 1
    def set_vxlan_reserved(self, reserved, ignore_check=False):
        reserved = self.normalize_value(reserved, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_RESERVED, reserved)

    def get_vxlan_reserved(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_VXLAN, VxlanPacketConstants.VXLAN_RESERVED),
            PacketConstants.INTEGER)

    def get_vxlan_reserved_hltapi_cmd(self, dummy_dict):
        reserved = self.get_vxlan_reserved()
        if isinstance(reserved, int):
            reserved = str(reserved)
        if reserved and 'Not Set' not in reserved:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVED_CMD] = reserved
    # end Vxlan reserved methods

    # start vxlan inner packet methods
    #  routing is a 32 bit INTEGER example: 1
    def set_vxlan_inner_packet(self, innerpacket, ignore_check=False):
        # routing = self.normalize_value(routing, PacketConstants.INTEGER)
        # self.set_packet_component(PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING, routing)
        self.innerpacket = innerpacket

    def get_vxlan_inner_packet(self):
        # return self.normalize_value(self.get_packet_component(
        #     PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)
        return self.innerpacket

    def get_inner_packet(self):
        return self.get_vxlan_inner_packet()

    # def get_gre_inner_packet_hltapi_cmd(self, dummy_dict):
    #     routing = self.get_gre_routing()
    #     if isinstance(routing, int):
    #         routing = str(routing)
    #     if routing and 'Not Set' not in routing:
    #         dummy_dict[TrafficConfigConstants.TEMP_ROUTING_CMD] = routing
    # end Gre routing methods

    def get_vxlan_inner_packet_length(self):
        pkt_buffer = self.innerpacket.get_header_length()  # + 4  # add the CRC
        minsize = 64
        if isinstance(self, TaggedPacketHeader):
            minsize += 4
        elif isinstance(self, VlanStackPacketHeader):
            minsize += (4 * self.get_vlan_num())
        return max(pkt_buffer, minsize)

    def get_inner_packet_length(self):
        return self.get_vxlan_inner_packet_length()

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("flags", self.format_int(self.get_vxlan_flags(), 4))
        table.add_row_value("group policy id", self.format_int(self.get_vxlan_group_policy_id(), 4))
        table.add_row_value("vxlan network identifier", self.format_int(self.get_vxlan_vxlan_network_identifier(), 6))
        table.add_row_value("reserved", self.format_int(self.get_vxlan_reserved(), 2))
        return "\n\nVXLAN HEADER" + table.to_table_string() + "\n\nInner Packet\n" + \
               self.get_vxlan_inner_packet().to_packet_string()

    def add_vxlan_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_VXLAN)

    def build(self):
        self.add_vxlan_header()
        assert isinstance(self, UdpPacketHeader)
        self.set_destination_port(4789, True)  # 8472

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_vxlan_flags_hltapi_cmd(dummy_dict)
        # self.get_vxlan_group_policy_id_hltapi_cmd(dummy_dict)
        # self.get_vxlan_vxlan_network_identifier_hltapi_cmd(dummy_dict)
        # self.get_vxlan_reserved_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_vxlan(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_vxlan(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_vxlan(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_vxlan(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    # update this from the ostinato docs.
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = VxlanPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def get_ixtclhal_vxlan_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        payload = VxlanPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def config_jets_stream_vxlan(self, jets_dev, port_string, stream_id, **kwargs):
        """
        VXLAN_HDR {
          flags : 8 : display="Flags %dec", index=1;
          reserved : 24 : display="Reserved %dec",  index=2;
          vxlan_id : 24 : display="VXLAN id %dec", index=3;
          reserved2 : 8  : display="Reserved %dec", index=4;
        } display="VXLAN Header";
        """
        pkt_fields = {}
        if self.is_field_set(self.get_vxlan_flags()):
            pkt_fields["flags"] = str(self.get_vxlan_flags())
        if self.is_field_set(self.get_vxlan_group_policy_id()):
            pkt_fields["reserved"] = str(self.get_vxlan_group_policy_id())
        if self.is_field_set(self.get_vxlan_vxlan_network_identifier()):
            pkt_fields["vxlan_id"] = str(self.get_vxlan_vxlan_network_identifier())
        if self.is_field_set(self.get_vxlan_reserved()):
            pkt_fields["reserved2"] = str(self.get_vxlan_reserved())

        jets_dev.pdl_add_packet_header(JetsDeviceConstants.VXLAN_HDR, pkt_fields)
        if self.is_field_set(self.get_vxlan_inner_packet()):
            inner_packet = self.get_vxlan_inner_packet()
            jets_dev.pdl_down_encap_level()
            inner_packet.config_thirdparty_traffic_generator_stream(EthernetPacketConstants.TRAFFIC_GENERATION_JETS,
                                                                    jets_dev, port_string, stream_id, **kwargs)
            jets_dev.pdl_up_encap_level()

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        flags = self.get_bits_from_string(8, payload)
        self.set_vxlan_flags("0x" + flags)
        payload = self.remove_bits_from_string(8, payload)
        group_policy_id = self.get_bits_from_string(24, payload)
        self.set_vxlan_group_policy_id("0x" + group_policy_id)
        payload = self.remove_bits_from_string(24, payload)
        vxlan_network_identifier = self.get_bits_from_string(24, payload)
        self.set_vxlan_vxlan_network_identifier("0x" + vxlan_network_identifier)
        payload = self.remove_bits_from_string(24, payload)
        reserved = self.get_bits_from_string(8, payload)
        self.set_vxlan_reserved("0x" + reserved)
        payload = self.remove_bits_from_string(8, payload)
        self.payload = payload
        packet = EthernetPacket()
        packet.set_payload(payload)
        self.set_vxlan_inner_packet(packet)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_vxlan_flags(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_vxlan_group_policy_id(), PacketConstants.INTEGER, 24)
        ret_string += self.format_byte_string(self.get_vxlan_vxlan_network_identifier(), PacketConstants.INTEGER, 24)
        ret_string += self.format_byte_string(self.get_vxlan_reserved(), PacketConstants.INTEGER, 8)
        ret_string += self.get_vxlan_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_inner_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                    print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, VxlanPacketHeader)
            assert isinstance(actual, VxlanPacketHeader)
            if expected.do_i_check_this_field(expected.get_vxlan_flags(), VxlanPacketConstants.VXLAN_FLAGS,
                                              ignore_list, include_list):
                name = "VXLAN flags : "
                if expected.get_vxlan_flags() != actual.get_vxlan_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vxlan_flags()) + " != " +
                                                      str(actual.get_vxlan_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vxlan_flags()) + " == " +
                                                 str(actual.get_vxlan_flags()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vxlan_group_policy_id(),
                                              VxlanPacketConstants.VXLAN_GROUP_POLICY_ID, ignore_list, include_list):
                name = "VXLAN group policy id : "
                if expected.get_vxlan_group_policy_id() != actual.get_vxlan_group_policy_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vxlan_group_policy_id()) + " != " +
                                                      str(actual.get_vxlan_group_policy_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vxlan_group_policy_id()) + " == " +
                                                 str(actual.get_vxlan_group_policy_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vxlan_vxlan_network_identifier(),
                                              VxlanPacketConstants.VXLAN_VXLAN_NETWORK_IDENTIFIER,
                                              ignore_list, include_list):
                name = "VXLAN vxlan network identifier : "
                if expected.get_vxlan_vxlan_network_identifier() != actual.get_vxlan_vxlan_network_identifier():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vxlan_vxlan_network_identifier()) + " != " +
                                                      str(actual.get_vxlan_vxlan_network_identifier()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vxlan_vxlan_network_identifier()) + " == " +
                                                 str(actual.get_vxlan_vxlan_network_identifier()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vxlan_reserved(), VxlanPacketConstants.VXLAN_RESERVED,
                                              ignore_list, include_list):
                name = "VXLAN reserved : "
                if expected.get_vxlan_reserved() != actual.get_vxlan_reserved():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_vxlan_reserved()) + " != " +
                                                      str(actual.get_vxlan_reserved()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vxlan_reserved()) + " == " +
                                                 str(actual.get_vxlan_reserved()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vxlan_inner_packet(),
                                              VxlanPacketConstants.VXLAN_INNER_PACKET, ignore_list, include_list):
                name = "VXLAN Inner packet : "
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
                PacketObject.logger.log_error("Error with VxlanPacketHeader")
        return results


class VxlanPacketConstants:
    def __init__(self):
        pass

    VXLAN_FLAGS = "VXLAN_FLAGS"
    VXLAN_GROUP_POLICY_ID = "VXLAN_GROUP_POLICY_ID"
    VXLAN_VXLAN_NETWORK_IDENTIFIER = "VXLAN_VXLAN_NETWORK_IDENTIFIER"
    VXLAN_RESERVED = "VXLAN_RESERVED"
    VXLAN_INNER_PACKET = "VXLAN_INNER_PACKET"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
