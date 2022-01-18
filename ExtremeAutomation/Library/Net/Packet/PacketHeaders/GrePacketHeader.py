import binascii
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


# https://tools.ietf.org/html/rfc1701
class GrePacketHeader(InnerPacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    GRE Packet Header
        # flags_and_version = 16bits
        # protocol_type = 16bits
        # checksum = 16bits
        # offset = 16bits
        # key = 32bits
        # sequence = 32bits
        # routing = 32bits
    """

    def __init__(self):
        self.add_gre_header()
        self.innerpacket = None
        self.HEADER_SIZE_GRE = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Gre flags_and_version methods
    #  flags_and_version is a 16 bit INTEGER example: 1
    def set_gre_flags_and_version(self, flags_and_version, ignore_check=False):
        flags_and_version = self.normalize_value(flags_and_version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_FLAGS_AND_VERSION,
                                  flags_and_version)

    def get_gre_flags_and_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_FLAGS_AND_VERSION), PacketConstants.INTEGER)

    def get_gre_flags_and_version_hltapi_cmd(self, dummy_dict):
        flags_and_version = self.get_gre_flags_and_version()
        if isinstance(flags_and_version, int):
            flags_and_version = str(flags_and_version)
        if flags_and_version and 'Not Set' not in flags_and_version:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_AND_VERSION_CMD] = flags_and_version
    # end Gre flags_and_version methods

    def set_gre_flag_checksum_present(self, enabled):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        if enabled:
            val |= 0x08000
        else:
            val &= 0x07FFF
        self.set_gre_flags_and_version(val)

    def get_gre_flag_checksum_present(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x08000) > 0

    def set_gre_flag_routing_present(self, enabled):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        if enabled:
            val |= 0x04000
        else:
            val &= 0x0BFFF
        self.set_gre_flags_and_version(val)

    def get_gre_flag_routing_present(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x04000) > 0

    def set_gre_flag_key_present(self, enabled):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        if enabled:
            val |= 0x02000
        else:
            val &= 0x0DFFF
        self.set_gre_flags_and_version(val)

    def get_gre_flag_key_present(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x02000) > 0

    def set_gre_flag_sequence_number_present(self, enabled):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        if enabled:
            val |= 0x01000
        else:
            val &= 0x0EFFF
        self.set_gre_flags_and_version(val)

    def get_gre_flag_sequence_number_present(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x01000) > 0

    def set_gre_flag_strict_source_route(self, enabled):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        if enabled:
            val |= 0x00800
        else:
            val &= 0x0F7FF
        self.set_gre_flags_and_version(val)

    def get_gre_flag_strict_source_route(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x00800) > 0

    def set_gre_flag_recursion_control_information(self, info):
        info = self.normalize_value(info, PacketConstants.INTEGER)
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        info <<= 8
        val &= 0x0F8FF
        val |= info
        self.set_gre_flags_and_version(val)

    def get_gre_flag_recursion_control_information(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x00700) >> 8

    def set_gre_flag_reserved_bits(self, info):
        info = self.normalize_value(info, PacketConstants.INTEGER)
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        info <<= 3
        val &= 0x0FF07
        val |= info
        self.set_gre_flags_and_version(val)

    def get_gre_flag_reserved_bits(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x000F8) >> 3

    def set_gre_flag_version_number(self, info):
        info = self.normalize_value(info, PacketConstants.INTEGER)
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        info <<= 0
        val &= 0x0FFF8
        val |= info
        self.set_gre_flags_and_version(val)

    def get_gre_flag_version_number(self):
        val = 0
        if self.is_field_set(self.get_gre_flags_and_version()):
            val = self.get_gre_flags_and_version()
        return (val & 0x00007) >> 0

        # Protocol Family                     PTYPE
        # ---------------                     -----
        # Reserved                            0000
        # SNA                                 0004
        # OSI network layer                   00FE
        # PUP                                 0200
        # XNS                                 0600
        # IP                                  0800
        # Chaos                               0804
        # RFC 826 ARP                         0806
        # Frame Relay ARP                     0808
        # VINES                               0BAD
        # VINES Echo                          0BAE
        # VINES Loopback                      0BAF
        # ERSPAN  version III                 22EB
        # DECnet (Phase IV)                   6003
        # Transparent Ethernet Bridging       6558
        # Raw Frame Relay                     6559
        # Apollo Domain                       8019
        # Ethertalk (Appletalk)               809B
        # Novell IPX                          8137
        # RFC 1144 TCP/IP compression         876B
        # IP Autonomous Systems               876C
        # Secure Data                         876D
        # ERSPAN  version  II                 88BE
        # Reserved                            FFFF

    # start Gre protocol_type methods
    #  protocol_type is a 16 bit INTEGER example: 1
    def set_gre_protocol_type(self, protocol_type, ignore_check=False):
        protocol_type = self.normalize_value(protocol_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_PROTOCOL_TYPE,
                                  protocol_type)

    def get_gre_protocol_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_PROTOCOL_TYPE), PacketConstants.INTEGER)

    def get_gre_protocol_type_spaced_hex(self):
        intvalu = self.get_gre_protocol_type()
        intvalu = NumberUtils.to_hex_value(intvalu, True)
        while len(intvalu) < 4:
            intvalu = "0" + intvalu
        return StringUtils.place_character_every_n_characters(intvalu.replace(" ", ""), " ", 2)

    def get_gre_protocol_type_hltapi_cmd(self, dummy_dict):
        protocol_type = self.get_gre_protocol_type()
        if isinstance(protocol_type, int):
            protocol_type = str(protocol_type)
        if protocol_type and 'Not Set' not in protocol_type:
            dummy_dict[TrafficConfigConstants.TEMP_PROTOCOL_TYPE_CMD] = protocol_type
    # end Gre protocol_type methods

    # start Gre checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_gre_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_CHECKSUM, checksum)

    def get_gre_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_CHECKSUM), PacketConstants.INTEGER)

    def get_gre_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_gre_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Gre checksum methods

    # start Gre offset methods
    #  offset is a 16 bit INTEGER example: 1
    def set_gre_offset(self, offset, ignore_check=False):
        offset = self.normalize_value(offset, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_OFFSET, offset)

    def get_gre_offset(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_OFFSET), PacketConstants.INTEGER)

    def get_gre_offset_hltapi_cmd(self, dummy_dict):
        offset = self.get_gre_offset()
        if isinstance(offset, int):
            offset = str(offset)
        if offset and 'Not Set' not in offset:
            dummy_dict[TrafficConfigConstants.TEMP_OFFSET_CMD] = offset
    # end Gre offset methods

    # start Gre key methods
    #  key is a 32 bit INTEGER example: 1
    def set_gre_key(self, key, ignore_check=False):
        key = self.normalize_value(key, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_KEY, key)

    def get_gre_key(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_KEY), PacketConstants.INTEGER)

    def get_gre_key_spaced_hex(self):
        intvalu = self.get_gre_key()
        intvalu = NumberUtils.to_hex_value(intvalu, True)
        while len(intvalu) < 8:
            intvalu = "0" + intvalu
        return StringUtils.place_character_every_n_characters(intvalu.replace(" ", ""), " ", 2)

    def get_gre_key_hltapi_cmd(self, dummy_dict):
        key = self.get_gre_key()
        if isinstance(key, int):
            key = str(key)
        if key and 'Not Set' not in key:
            dummy_dict[TrafficConfigConstants.TEMP_KEY_CMD] = key
    # end Gre key methods

    # start Gre sequence methods
    #  sequence is a 32 bit INTEGER example: 1
    def set_gre_sequence(self, sequence, ignore_check=False):
        sequence = self.normalize_value(sequence, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_SEQUENCE, sequence)

    def get_gre_sequence(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_SEQUENCE), PacketConstants.INTEGER)

    def get_gre_sequence_spaced_hex(self):
        intvalu = self.get_gre_sequence()
        intvalu = NumberUtils.to_hex_value(intvalu, True)
        while len(intvalu) < 8:
            intvalu = "0" + intvalu
        return StringUtils.place_character_every_n_characters(intvalu.replace(" ", ""), " ", 2)

    def get_gre_sequence_hltapi_cmd(self, dummy_dict):
        sequence = self.get_gre_sequence()
        if isinstance(sequence, int):
            sequence = str(sequence)
        if sequence and 'Not Set' not in sequence:
            dummy_dict[TrafficConfigConstants.TEMP_SEQUENCE_CMD] = sequence
    # end Gre sequence methods

    # start Gre routing methods
    #  routing is a 32 bit INTEGER example: 1
    def set_gre_routing(self, routing, ignore_check=False):
        routing = self.normalize_value(routing, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_ROUTING, routing)

    def get_gre_routing(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L5_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)

    def get_gre_routing_hltapi_cmd(self, dummy_dict):
        routing = self.get_gre_routing()
        if isinstance(routing, int):
            routing = str(routing)
        if routing and 'Not Set' not in routing:
            dummy_dict[TrafficConfigConstants.TEMP_ROUTING_CMD] = routing
    # end Gre routing methods

    # start Gre inner packet methods
    #  routing is a 32 bit INTEGER example: 1
    def set_gre_inner_packet(self, innerpacket, ignore_check=False):
        # routing = self.normalize_value(routing, PacketConstants.INTEGER)
        # self.set_packet_component(PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING, routing)
        self.innerpacket = innerpacket

    def get_gre_inner_packet(self):
        # return self.normalize_value(self.get_packet_component(
        #     PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)
        return self.innerpacket

    def get_inner_packet(self):
        return self.get_gre_inner_packet()

    # def get_gre_inner_packet_hltapi_cmd(self, dummy_dict):
    #     routing = self.get_gre_routing()
    #     if isinstance(routing, int):
    #         routing = str(routing)
    #     if routing and 'Not Set' not in routing:
    #         dummy_dict[TrafficConfigConstants.TEMP_ROUTING_CMD] = routing
    # end Gre routing methods

    def get_gre_inner_packet_length(self):
        pkt_buffer = self.innerpacket.get_header_length()  # + 4 # add the CRC
        minsize = 64
        if isinstance(self, TaggedPacketHeader):
            minsize += 4
        elif isinstance(self, VlanStackPacketHeader):
            minsize += (4 * self.get_vlan_num())
        return max(pkt_buffer, minsize)

    def get_inner_packet_length(self):
        return self.get_gre_inner_packet_length()

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("flags_and_version", self.format_int(self.get_gre_flags_and_version(), 4))
        table.add_row_value("Flags:C", self.get_gre_flag_checksum_present())
        table.add_row_value("Flags:R", self.get_gre_flag_routing_present())
        table.add_row_value("Flags:K", self.get_gre_flag_key_present())
        table.add_row_value("Flags:S", self.get_gre_flag_sequence_number_present())
        table.add_row_value("Flags:s", self.get_gre_flag_strict_source_route())
        table.add_row_value("Flags:Recur", self.get_gre_flag_recursion_control_information())
        table.add_row_value("Flag Bits", self.format_int(self.get_gre_flag_reserved_bits(), 2))
        table.add_row_value("Vers", self.format_int(self.get_gre_flag_version_number(), 1))
        table.add_row_value("protocol_type", self.format_int(self.get_gre_protocol_type(), 4))
        # if int(self.get_gre_protocol_type()) != GrePacketConstants.GRE_PROTOCOL_TRANSPARENT_ETHERNET_BRIDGING:
        table.add_row_value("checksum", self.format_int(self.get_gre_checksum(), 4))
        table.add_row_value("offset", self.format_int(self.get_gre_offset(), 4))
        table.add_row_value("key", self.format_int(self.get_gre_key(), 8))
        table.add_row_value("sequence", self.format_int(self.get_gre_sequence(), 8))
        table.add_row_value("routing", self.format_int(self.get_gre_routing(), 8))

        ret_string = "\n\nGRE HEADER" + table.to_table_string()
        if "ERSPAN" not in self.get_name().upper():
            ret_string += "\n\nInner Packet\n" + self.get_gre_inner_packet().to_packet_string()
        return ret_string

    def add_gre_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_GRE)

    def build(self):
        self.add_gre_header()
        if isinstance(self, IpV4PacketHeader):
            self.set_ip_protocol(47, True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header(47, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_gre_flags_and_version_hltapi_cmd(dummy_dict)
        # self.get_gre_protocol_type_hltapi_cmd(dummy_dict)
        # self.get_gre_checksum_hltapi_cmd(dummy_dict)
        # self.get_gre_offset_hltapi_cmd(dummy_dict)
        # self.get_gre_key_hltapi_cmd(dummy_dict)
        # self.get_gre_sequence_hltapi_cmd(dummy_dict)
        # self.get_gre_routing_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_gre(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_gre(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_gre(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_gre(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    # update this from the ostinato docs.
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = GrePacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
        p.Extensions[hexDump].pad_until_end = False

    def config_jet_stream_gre(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + GrePacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_gre_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        dummy_dict.append("gre setDefault ")
        if self.get_gre_flag_key_present():
            dummy_dict.append("gre config -enableKey                          true")
            dummy_dict.append("gre config -key                                \"" +
                              self.get_gre_key_spaced_hex() + "\"")
        else:
            dummy_dict.append("gre config -enableKey                          false")
            dummy_dict.append("gre config -key                                \"00 00 00 00\"")
        if self.get_gre_flag_sequence_number_present():
            dummy_dict.append("gre config -enableSequenceNumber               true")
            dummy_dict.append("gre config -sequenceNumber                     \"" +
                              self.get_gre_sequence_spaced_hex() + "\"")
        else:
            dummy_dict.append("gre config -enableSequenceNumber               false")
            dummy_dict.append("gre config -sequenceNumber                     \"00 00 00 00\"")

        if self.get_gre_flag_checksum_present():
            dummy_dict.append("gre config -enableChecksum                     true")
        else:
            dummy_dict.append("gre config -enableChecksum                     false")
            dummy_dict.append("gre config -enableValidChecksum                true")

        dummy_dict.append("gre config -version                            0")
        dummy_dict.append("gre config -reserved0                          \"00 00\"")
        dummy_dict.append("gre config -reserved1                          \"00 00\"")
        dummy_dict.append("gre config -protocolType                       \"" +
                          self.get_gre_protocol_type_spaced_hex().upper() + "\"")
        dummy_dict.append("gre set " + port_string)
    # ### put some IxTclHal info here.
        if "erspan" not in self.get_name().lower():
            payload = self.get_gre_inner_packet().get_bytes()  # GrePacketHeader.get_header_bytes(self)
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
        flags_and_version = self.get_bits_from_string(16, payload)
        self.set_gre_flags_and_version("0x" + flags_and_version)
        payload = self.remove_bits_from_string(16, payload)
        protocol_type = self.get_bits_from_string(16, payload)
        self.set_gre_protocol_type("0x" + protocol_type)
        payload = self.remove_bits_from_string(16, payload)

        # if int(protocol_type, 16) != GrePacketConstants.GRE_PROTOCOL_TRANSPARENT_ETHERNET_BRIDGING:
        # if the gre protocol there is L2 (0x6558) stop there.
        header_size = 0
        if self.get_gre_flag_checksum_present():
            checksum = self.get_bits_from_string(16, payload)
            self.set_gre_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
            header_size += 2
        if self.get_gre_flag_routing_present():
            offset = self.get_bits_from_string(16, payload)
            self.set_gre_offset("0x" + offset)
            payload = self.remove_bits_from_string(16, payload)
            header_size += 2
        if self.get_gre_flag_key_present():
            key = self.get_bits_from_string(32, payload)
            self.set_gre_key("0x" + key)
            payload = self.remove_bits_from_string(32, payload)
            header_size += 4
        if self.get_gre_flag_strict_source_route():
            sequence = self.get_bits_from_string(32, payload)
            self.set_gre_sequence("0x" + sequence)
            payload = self.remove_bits_from_string(32, payload)
            header_size += 4
        if self.get_gre_flag_routing_present():
            routing = self.get_bits_from_string(32, payload)
            self.set_gre_routing("0x" + routing)
            payload = self.remove_bits_from_string(32, payload)
            header_size += 4
        # strip off reserved
        if header_size % 4 > 0:
            payload = self.remove_bits_from_string((4 - (header_size % 4)) * 8, payload)
        self.payload = payload
        if "ERSPAN" not in self.get_name().upper():
            packet = EthernetPacket()
            packet.set_payload(payload)
            self.set_gre_inner_packet(packet)
        # self.set_gre_inner_packet(PacketClassifier.classify_packet_bytes())

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_gre_flags_and_version(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_gre_protocol_type(), PacketConstants.INTEGER, 16)
        header_size = 0
        if self.get_gre_flag_checksum_present():
            ret_string += self.format_byte_string(self.get_gre_checksum(), PacketConstants.INTEGER, 16)
            header_size += 2
        if self.get_gre_flag_routing_present():
            ret_string += self.format_byte_string(self.get_gre_offset(), PacketConstants.INTEGER, 16)
            header_size += 2
        if self.get_gre_flag_key_present():
            ret_string += self.format_byte_string(self.get_gre_key(), PacketConstants.INTEGER, 32)
            header_size += 4
        if self.get_gre_flag_sequence_number_present():
            ret_string += self.format_byte_string(self.get_gre_sequence(), PacketConstants.INTEGER, 32)
            header_size += 4
        if self.get_gre_flag_key_present():
            ret_string += self.format_byte_string(self.get_gre_routing(), PacketConstants.INTEGER, 32)
            header_size += 4
        if header_size % 4 > 0:  # padding
            ret_string += "0" * (((4 - (header_size % 4)) * 8) // 4)
        if "ERSPAN" not in self.get_name().upper():
            ret_string += self.get_gre_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_inner_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                    print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, GrePacketHeader)
            assert isinstance(actual, GrePacketHeader)
            if expected.do_i_check_this_field(expected.get_gre_flags_and_version(),
                                              GrePacketConstants.GRE_FLAGS_AND_VERSION, ignore_list, include_list):

                name = "GRE flags_and_version : "
                if expected.get_gre_flags_and_version() != actual.get_gre_flags_and_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_flags_and_version()) + " != " +
                                                      str(actual.get_gre_flags_and_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_flags_and_version()) + " == " +
                                                 str(actual.get_gre_flags_and_version()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_protocol_type(), GrePacketConstants.GRE_PROTOCOL_TYPE,
                                              ignore_list, include_list):
                name = "GRE protocol_type : "
                if expected.get_gre_protocol_type() != actual.get_gre_protocol_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_protocol_type()) + " != " +
                                                      str(actual.get_gre_protocol_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_protocol_type()) + " == " +
                                                 str(actual.get_gre_protocol_type()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_checksum(), GrePacketConstants.GRE_CHECKSUM,
                                              ignore_list, include_list):
                name = "GRE checksum : "
                if expected.get_gre_checksum() != actual.get_gre_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_checksum()) + " != " +
                                                      str(actual.get_gre_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_checksum()) + " == " +
                                                 str(actual.get_gre_checksum()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_offset(), GrePacketConstants.GRE_OFFSET,
                                              ignore_list, include_list):
                name = "GRE offset : "
                if expected.get_gre_offset() != actual.get_gre_offset():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_offset()) + " != " +
                                                      str(actual.get_gre_offset()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_offset()) + " == " +
                                                 str(actual.get_gre_offset()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_key(), GrePacketConstants.GRE_KEY,
                                              ignore_list, include_list):
                name = "GRE key : "
                if expected.get_gre_key() != actual.get_gre_key():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_key()) + " != " +
                                                      str(actual.get_gre_key()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_key()) + " == " +
                                                 str(actual.get_gre_key()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_sequence(), GrePacketConstants.GRE_SEQUENCE,
                                              ignore_list, include_list):
                name = "GRE sequence : "
                if expected.get_gre_sequence() != actual.get_gre_sequence():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_sequence()) + " != " +
                                                      str(actual.get_gre_sequence()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_sequence()) + " == " +
                                                 str(actual.get_gre_sequence()) + " Pass")

            if expected.do_i_check_this_field(expected.get_gre_routing(), GrePacketConstants.GRE_ROUTING,
                                              ignore_list, include_list):
                name = "GRE routing : "
                if expected.get_gre_routing() != actual.get_gre_routing():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_gre_routing()) + " != " +
                                                      str(actual.get_gre_routing()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_gre_routing()) + " == " +
                                                 str(actual.get_gre_routing()) + " Pass")

            if "ERSPAN" not in expected.get_name().upper():
                if expected.do_i_check_this_field(expected.get_gre_inner_packet(), GrePacketConstants.GRE_INNER_PACKET,
                                                  ignore_list, include_list):
                    name = "GRE Inner packet : "
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
                PacketObject.logger.log_error("Error with GrePacketHeader")
        return results


class GrePacketConstants:
    def __init__(self):
        pass

    GRE_FLAGS_AND_VERSION = "GRE_FLAGS_AND_VERSION"
    GRE_PROTOCOL_TYPE = "GRE_PROTOCOL_TYPE"
    GRE_CHECKSUM = "GRE_CHECKSUM"
    GRE_OFFSET = "GRE_OFFSET"
    GRE_KEY = "GRE_KEY"
    GRE_SEQUENCE = "GRE_SEQUENCE"
    GRE_ROUTING = "GRE_ROUTING"
    GRE_INNER_PACKET = "GRE_INNER_PACKET"
    # Reserved                            0000
    # SNA                                 0004
    # OSI network layer                   00FE
    # PUP                                 0200
    # XNS                                 0600
    # IP                                  0800
    # Chaos                               0804
    # RFC 826 ARP                         0806
    # Frame Relay ARP                     0808
    # VINES                               0BAD
    # VINES Echo                          0BAE
    # VINES Loopback                      0BAF
    # ERSPAN  version III                 22EB
    GRE_PROTOCOL_ESPAN_III = 0x22EB
    # DECnet (Phase IV)                   6003
    # Transparent Ethernet Bridging       6558
    GRE_PROTOCOL_TRANSPARENT_ETHERNET_BRIDGING = 0x6558
    # Raw Frame Relay                     6559
    # Apollo Domain                       8019
    # Ethertalk (Appletalk)               809B
    # Novell IPX                          8137
    # RFC 1144 TCP/IP compression         876B
    # IP Autonomous Systems               876C
    # Secure Data                         876D
    # ERSPAN  version  II                 88BE
    GRE_PROTOCOL_ESPAN_II = 0x88BE
    # Reserved                            FFFF

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
