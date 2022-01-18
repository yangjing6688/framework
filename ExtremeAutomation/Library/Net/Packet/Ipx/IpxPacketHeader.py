from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants

from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class IpxPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    IPX Packet Header
        # checksum = 16bits
        # packet length = 16bits
        # transport control = 8bits
        # packet type = 8bits
        # destination network = 32bits
        # destination node = 48bits
        # destination socket = 16bits
        # source network = 32bits
        # source node = 48bits
        # source socket = 16bits
    """

    def __init__(self):
        self.add_ipx_header()
        self.HEADER_SIZE_IPX = (16 + 16 + 8 + 8 + 32 + 48 + 16 + 32 + 48 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Ipx checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_ipx_checksum(self, checksum, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_CHECKSUM, ignore_check)
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_CHECKSUM, checksum)

    def get_ipx_checksum(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_CHECKSUM),
            PacketConstants.INTEGER)

    def get_ipx_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_ipx_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Ipx checksum methods

    # start Ipx packet length methods
    #  packet_length is a 16 bit INTEGER example: 1
    def set_ipx_packet_length(self, packet_length, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_PACKET_LENGTH, ignore_check)
        packet_length = self.normalize_value(packet_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_PACKET_LENGTH,
                                  packet_length)

    def get_ipx_packet_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_PACKET_LENGTH),
            PacketConstants.INTEGER)

    def get_ipx_packet_length_hltapi_cmd(self, dummy_dict):
        packet_length = self.get_ipx_packet_length()
        if isinstance(packet_length, int):
            packet_length = str(packet_length)
        if packet_length and 'Not Set' not in packet_length:
            dummy_dict[TrafficConfigConstants.TEMP_PACKET_LENGTH_CMD] = packet_length
    # end Ipx packet length methods

    # start Ipx transport control methods
    #  transport_control is a 8 bit INTEGER example: 1
    def set_ipx_transport_control(self, transport_control, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_TRANSPORT_CONTROL, ignore_check)
        transport_control = self.normalize_value(transport_control, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_TRANSPORT_CONTROL,
                                  transport_control)

    def get_ipx_transport_control(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_TRANSPORT_CONTROL),
            PacketConstants.INTEGER)

    def get_ipx_transport_control_hltapi_cmd(self, dummy_dict):
        transport_control = self.get_ipx_transport_control()
        if isinstance(transport_control, int):
            transport_control = str(transport_control)
        if transport_control and 'Not Set' not in transport_control:
            dummy_dict[TrafficConfigConstants.TEMP_TRANSPORT_CONTROL_CMD] = transport_control
    # end Ipx transport control methods

    # start Ipx packet type methods
    #  packet_type is a 8 bit INTEGER example: 1
    def set_ipx_packet_type(self, packet_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_PACKET_TYPE, ignore_check)
        packet_type = self.normalize_value(packet_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_PACKET_TYPE, packet_type)

    def get_ipx_packet_type(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_PACKET_TYPE),
            PacketConstants.INTEGER)

    def get_ipx_packet_type_hltapi_cmd(self, dummy_dict):
        packet_type = self.get_ipx_packet_type()
        if isinstance(packet_type, int):
            packet_type = str(packet_type)
        if packet_type and 'Not Set' not in packet_type:
            dummy_dict[TrafficConfigConstants.TEMP_PACKET_TYPE_CMD] = packet_type
    # end Ipx packet type methods

    # start Ipx destination network methods
    #  destination_network is a 32 bit HEX_STRING example: FFFFFFFF
    def set_ipx_destination_network(self, destination_network, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_DESTINATION_NETWORK, ignore_check)
        destination_network = self.normalize_value(destination_network, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_NETWORK,
                                  destination_network)

    def get_ipx_destination_network(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_NETWORK),
            PacketConstants.HEX_STRING)

    def get_ipx_destination_network_hltapi_cmd(self, dummy_dict):
        destination_network = self.get_ipx_destination_network()
        if destination_network and 'Not Set' not in destination_network:
            dummy_dict[TrafficConfigConstants.TEMP_DESTINATION_NETWORK_CMD] = destination_network
    # end Ipx destination network methods

    # start Ipx destination node methods
    #  destination_node is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_ipx_destination_node(self, destination_node, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_DESTINATION_NODE, ignore_check)
        destination_node = self.normalize_value(destination_node, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_NODE,
                                  destination_node)

    def get_ipx_destination_node(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_NODE),
            PacketConstants.HEX_STRING)

    def get_ipx_destination_node_hltapi_cmd(self, dummy_dict):
        destination_node = self.get_ipx_destination_node()
        if destination_node and 'Not Set' not in destination_node:
            dummy_dict[TrafficConfigConstants.TEMP_DESTINATION_NODE_CMD] = destination_node
    # end Ipx destination node methods

    # start Ipx destination socket methods
    #  destination_socket is a 16 bit INTEGER example: 1
    def set_ipx_destination_socket(self, destination_socket, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_DESTINATION_SOCKET, ignore_check)
        destination_socket = self.normalize_value(destination_socket, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_SOCKET,
                                  destination_socket)

    def get_ipx_destination_socket(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_DESTINATION_SOCKET),
            PacketConstants.INTEGER)

    def get_ipx_destination_socket_hltapi_cmd(self, dummy_dict):
        destination_socket = self.get_ipx_destination_socket()
        if isinstance(destination_socket, int):
            destination_socket = str(destination_socket)
        if destination_socket and 'Not Set' not in destination_socket:
            dummy_dict[TrafficConfigConstants.TEMP_DESTINATION_SOCKET_CMD] = destination_socket
    # end Ipx destination socket methods

    # start Ipx source network methods
    #  source_network is a 32 bit HEX_STRING example: FFFFFFFF
    def set_ipx_source_network(self, source_network, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_SOURCE_NETWORK, ignore_check)
        source_network = self.normalize_value(source_network, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_NETWORK,
                                  source_network)

    def get_ipx_source_network(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_NETWORK),
            PacketConstants.HEX_STRING)

    def get_ipx_source_network_hltapi_cmd(self, dummy_dict):
        source_network = self.get_ipx_source_network()
        if source_network and 'Not Set' not in source_network:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_NETWORK_CMD] = source_network
    # end Ipx source network methods

    # start Ipx source node methods
    #  source_node is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_ipx_source_node(self, source_node, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_SOURCE_NODE, ignore_check)
        source_node = self.normalize_value(source_node, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_NODE, source_node)

    def get_ipx_source_node(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_NODE),
            PacketConstants.HEX_STRING)

    def get_ipx_source_node_hltapi_cmd(self, dummy_dict):
        source_node = self.get_ipx_source_node()
        if source_node and 'Not Set' not in source_node:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_NODE_CMD] = source_node
    # end Ipx source node methods

    # start Ipx source socket methods
    #  source_socket is a 16 bit INTEGER example: 1
    def set_ipx_source_socket(self, source_socket, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IpxPacketConstants.IPX_SOURCE_SOCKET, ignore_check)
        source_socket = self.normalize_value(source_socket, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_SOCKET,
                                  source_socket)

    def get_ipx_source_socket(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPX, IpxPacketConstants.IPX_SOURCE_SOCKET),
            PacketConstants.INTEGER)

    def get_ipx_source_socket_hltapi_cmd(self, dummy_dict):
        source_socket = self.get_ipx_source_socket()
        if isinstance(source_socket, int):
            source_socket = str(source_socket)
        if source_socket and 'Not Set' not in source_socket:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_SOCKET_CMD] = source_socket
    # end Ipx source socket methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("checksum", self.format_int(self.get_ipx_checksum(), 4))
        table.add_row_value("packet length", self.format_int(self.get_ipx_packet_length(), 4))
        table.add_row_value("transport control", self.format_int(self.get_ipx_transport_control(), 2))
        table.add_row_value("packet type", self.format_int(self.get_ipx_packet_type(), 2))
        table.add_row_value("destination network", self.get_ipx_destination_network())
        table.add_row_value("destination node", self.get_ipx_destination_node())
        table.add_row_value("destination socket", self.format_int(self.get_ipx_destination_socket(), 4))
        table.add_row_value("source network", self.get_ipx_source_network())
        table.add_row_value("source node", self.get_ipx_source_node())
        table.add_row_value("source socket", self.format_int(self.get_ipx_source_socket(), 4))
        return "\n\nIPX HEADER" + table.to_table_string()

    def add_ipx_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_IPX)

    def build(self):
        self.add_ipx_header()
        self.set_llc_dsap("0xE0")
        self.set_llc_ssap("0xE0")

    def get_hltapi_commands(self):
        dummy_dict = dict()
        dummy_dict[TrafficConfigConstants.L3_PROTOCOL_CMD] = TrafficConfigConstants.L3_PROTOCOL_IPX  # constant value
        # self.get_ipx_checksum_hltapi_cmd(dummy_dict)
        # self.get_ipx_packet_length_hltapi_cmd(dummy_dict)
        # self.get_ipx_transport_control_hltapi_cmd(dummy_dict)
        # self.get_ipx_packet_type_hltapi_cmd(dummy_dict)
        # self.get_ipx_destination_network_hltapi_cmd(dummy_dict)
        # self.get_ipx_destination_node_hltapi_cmd(dummy_dict)
        # self.get_ipx_destination_socket_hltapi_cmd(dummy_dict)
        # self.get_ipx_source_network_hltapi_cmd(dummy_dict)
        # self.get_ipx_source_node_hltapi_cmd(dummy_dict)
        # self.get_ipx_source_socket_hltapi_cmd(dummy_dict)
        return dummy_dict

    def get_ixtclhal_ipx_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("protocol config -name                               ipx")
        dummy_dict.append("protocol config -ethernetType                       ieee8022")
        dummy_dict.append("protocolServer set " + port_string)
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        dummy_dict.append("ipx get " + port_string)
        # ### put some IxTclHal info here.
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_packet_length(),
                                                    "ipx config -lengthOverride true\nipx config -length",
                                                    PacketConstants.INTEGER)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_transport_control(),
                                                    "ipx config -transportControl", PacketConstants.INTEGER)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_packet_type(), "ipx config -packetType",
                                                    PacketConstants.INTEGER)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_destination_network(),
                                                    "ipx config -destNetwork", PacketConstants.HEX_STRING)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_destination_node(), "ipx config -destNode",
                                                    PacketConstants.HEX_STRING)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_destination_socket(),
                                                    "ipx config -destSocket", PacketConstants.INTEGER)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_source_network(),
                                                    "ipx config -sourceNetwork", PacketConstants.HEX_STRING)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_source_node(), "ipx config -sourceNode",
                                                    PacketConstants.HEX_STRING)
        TrafficGenerationUtils.insert_ixtcl_command(dummy_dict, self.get_ipx_source_socket(),
                                                    "ipx config -sourceSocket", PacketConstants.INTEGER)
        dummy_dict.append("ipx set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_ipx_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_ipx(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_ipx(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_ipx(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_ipx(self, drone, port_string, stream_id, **kwargs):
        pass

    def config_jets_stream_ipx(self, jets_dev, port_string, stream_id, **kwargs):
        """
        IPX_HDR {
          idp_xsum : 16 : legal_values=(NONE=0xffff), default=0xffff, display="Checksum", index=1;
          idp_len  : 16 : legal_values=(30-0xffff), send = length(node, pdu), display="Length", index=2;
          hops     : 8  : legal_values=(0-0x0f), default=0, display="Hops Traversed", index=3;
          type     : 8  : legal_values=(UNKNOWN=0, RIP=1, ECHO=2, ERROR=3, SAP=4, SPX=5, NCP=0x11, NETBIOS=0x14 ),
                          display="Packet Type", index=4;
          dna_net  : 32 : legal_values=(LOCAL=0x00000000 ), default=0, display="Destination Network", index=5;
          dna_node : 48 : legal_values=(BROADCAST=0xffffffffffff ), default=0xffffffffffff, display="Destination Host",
                          tags=("Destination Address" ), index=6;
          dna_sock : 16 : legal_values=(NCP=0x0451, SAP=0x0452, RIP=0x0453, NETBIOS=0x0455, DIAG=0x0456,
                          SERIALIZATION=0x0457, NLSP=0x9001, IPXWAN=0x9004, PING=0x9086 ), default=0x4001,
                          display="Destination Socket", index=7;
          sna_net  : 32 : legal_values=(LOCAL=0x00000000 ), default=0x00000000, display="Source Network", index=8;
          sna_node : 48 : legal_values=(BROADCAST=0xffffffffffff ), default=0x55443322110000, display="Source Host",
                          tags=("Source Address" ), index=9;
          sna_sock : 16 : legal_values=(NCP=0x0451, SAP=0x0452, RIP=0x0453, NETBIOS=0x0455, DIAG=0x0456,
                          SERIALIZATION=0x0457, NLSP=0x9001, IPXWAN=0x9004, PING=0x9086 ), default=0x4002,
                          display="Source Socket", index=10;
        } display="IPX Header", tags=("Network Layer" ), index=6001;
        """
        # pkt_fields = {}
        # if self.is_field_set(self.get_ipx_checksum()):
        #     pkt_fields["idp_xsum"] = str(self.get_ipx_checksum())
        # if self.is_field_set(self.get_ipx_packet_length()):
        #     pkt_fields["idp_len"] = str(self.get_ipx_packet_length())
        # if self.is_field_set(self.get_ipx_transport_control()):
        #     pkt_fields["hops"] = str(self.get_ipx_transport_control())
        # if self.is_field_set(self.get_ipx_packet_type()):
        #     pkt_fields["type"] = str(self.get_ipx_packet_type())
        #
        # if self.is_field_set(self.get_ipx_destination_network()):
        #     pkt_fields["dna_net"] = "0x" + str(self.get_ipx_destination_network()).replace(" ","")
        # if self.is_field_set(self.get_ipx_destination_node()):
        #     pkt_fields["dna_node"] = "0x" + str(self.get_ipx_destination_node()).replace(" ","")
        # if self.is_field_set(self.get_ipx_destination_socket()):
        #     pkt_fields["dna_sock"] = str(self.get_ipx_destination_socket())
        #
        # if self.is_field_set(self.get_ipx_source_network()):
        #     pkt_fields["sna_net"] = "0x" + str(self.get_ipx_source_network()).replace(" ","")
        # if self.is_field_set(self.get_ipx_source_node()):
        #     pkt_fields["sna_node"] = "0x" + str(self.get_ipx_source_node()).replace(" ","")
        # if self.is_field_set(self.get_ipx_source_socket()):
        #     pkt_fields["sna_sock"] = str(self.get_ipx_source_socket())
        #
        # jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPX_HDR, pkt_fields)

        pkt_bytes = "0x" + IpxPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        checksum = self.get_bits_from_string(16, payload)
        self.set_ipx_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)
        packet_length = self.get_bits_from_string(16, payload)
        self.set_ipx_packet_length("0x" + packet_length)
        payload = self.remove_bits_from_string(16, payload)
        transport_control = self.get_bits_from_string(8, payload)
        self.set_ipx_transport_control("0x" + transport_control)
        payload = self.remove_bits_from_string(8, payload)
        packet_type = self.get_bits_from_string(8, payload)
        self.set_ipx_packet_type("0x" + packet_type)
        payload = self.remove_bits_from_string(8, payload)
        destination_network = self.get_bits_from_string(32, payload)
        self.set_ipx_destination_network("0x" + destination_network)
        payload = self.remove_bits_from_string(32, payload)
        destination_node = self.get_bits_from_string(48, payload)
        self.set_ipx_destination_node("0x" + destination_node)
        payload = self.remove_bits_from_string(48, payload)
        destination_socket = self.get_bits_from_string(16, payload)
        self.set_ipx_destination_socket("0x" + destination_socket)
        payload = self.remove_bits_from_string(16, payload)
        source_network = self.get_bits_from_string(32, payload)
        self.set_ipx_source_network("0x" + source_network)
        payload = self.remove_bits_from_string(32, payload)
        source_node = self.get_bits_from_string(48, payload)
        self.set_ipx_source_node("0x" + source_node)
        payload = self.remove_bits_from_string(48, payload)
        source_socket = self.get_bits_from_string(16, payload)
        self.set_ipx_source_socket("0x" + source_socket)
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_ipx_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ipx_packet_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ipx_transport_control(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ipx_packet_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_ipx_destination_network(), PacketConstants.HEX_STRING, 32)
        ret_string += self.format_byte_string(self.get_ipx_destination_node(), PacketConstants.HEX_STRING, 48)
        ret_string += self.format_byte_string(self.get_ipx_destination_socket(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_ipx_source_network(), PacketConstants.HEX_STRING, 32)
        ret_string += self.format_byte_string(self.get_ipx_source_node(), PacketConstants.HEX_STRING, 48)
        ret_string += self.format_byte_string(self.get_ipx_source_socket(), PacketConstants.INTEGER, 16)
        return ret_string

    @staticmethod
    def compare_ipx_packet_header(expected, actual, ignore_list, include_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IpxPacketHeader)
            assert isinstance(actual, IpxPacketHeader)
            if expected.do_i_check_this_field(expected.get_ipx_checksum(), IpxPacketConstants.IPX_CHECKSUM,
                                              ignore_list, include_list):
                name = "IPX checksum : "
                if expected.get_ipx_checksum() != actual.get_ipx_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_checksum()) + " != " +
                                                      str(actual.get_ipx_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_checksum()) + " == " +
                                                 str(actual.get_ipx_checksum()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_packet_length(),
                                              IpxPacketConstants.IPX_PACKET_LENGTH, ignore_list, include_list):
                name = "IPX packet length : "
                if expected.get_ipx_packet_length() != actual.get_ipx_packet_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_packet_length()) + " != " +
                                                      str(actual.get_ipx_packet_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_packet_length()) + " == " +
                                                 str(actual.get_ipx_packet_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_transport_control(),
                                              IpxPacketConstants.IPX_TRANSPORT_CONTROL, ignore_list, include_list):
                name = "IPX transport control : "
                if expected.get_ipx_transport_control() != actual.get_ipx_transport_control():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_transport_control()) + " != " +
                                                      str(actual.get_ipx_transport_control()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_transport_control()) + " == " +
                                                 str(actual.get_ipx_transport_control()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_packet_type(), IpxPacketConstants.IPX_PACKET_TYPE,
                                              ignore_list, include_list):
                name = "IPX packet type : "
                if expected.get_ipx_packet_type() != actual.get_ipx_packet_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_packet_type()) + " != " +
                                                      str(actual.get_ipx_packet_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_packet_type()) + " == " +
                                                 str(actual.get_ipx_packet_type()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_destination_network(),
                                              IpxPacketConstants.IPX_DESTINATION_NETWORK, ignore_list, include_list):
                name = "IPX destination network : "
                if expected.get_ipx_destination_network() != actual.get_ipx_destination_network():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_destination_network()) + " != " +
                                                      str(actual.get_ipx_destination_network()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_destination_network()) + " == " +
                                                 str(actual.get_ipx_destination_network()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_destination_node(),
                                              IpxPacketConstants.IPX_DESTINATION_NODE, ignore_list, include_list):
                name = "IPX destination node : "
                if expected.get_ipx_destination_node() != actual.get_ipx_destination_node():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_destination_node()) + " != " +
                                                      str(actual.get_ipx_destination_node()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_destination_node()) + " == " +
                                                 str(actual.get_ipx_destination_node()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_destination_socket(),
                                              IpxPacketConstants.IPX_DESTINATION_SOCKET, ignore_list, include_list):
                name = "IPX destination socket : "
                if expected.get_ipx_destination_socket() != actual.get_ipx_destination_socket():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_destination_socket()) + " != " +
                                                      str(actual.get_ipx_destination_socket()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_destination_socket()) + " == " +
                                                 str(actual.get_ipx_destination_socket()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_source_network(), IpxPacketConstants.IPX_SOURCE_NETWORK,
                                              ignore_list, include_list):
                name = "IPX source network : "
                if expected.get_ipx_source_network() != actual.get_ipx_source_network():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_source_network()) + " != " +
                                                      str(actual.get_ipx_source_network()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_source_network()) + " == " +
                                                 str(actual.get_ipx_source_network()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_source_node(), IpxPacketConstants.IPX_SOURCE_NODE,
                                              ignore_list, include_list):
                name = "IPX source node : "
                if expected.get_ipx_source_node() != actual.get_ipx_source_node():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_source_node()) + " != " +
                                                      str(actual.get_ipx_source_node()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_source_node()) + " == " +
                                                 str(actual.get_ipx_source_node()) + " Pass")

            if expected.do_i_check_this_field(expected.get_ipx_source_socket(), IpxPacketConstants.IPX_SOURCE_SOCKET,
                                              ignore_list, include_list):
                name = "IPX source socket : "
                if expected.get_ipx_source_socket() != actual.get_ipx_source_socket():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_ipx_source_socket()) + " != " +
                                                      str(actual.get_ipx_source_socket()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_ipx_source_socket()) + " == " +
                                                 str(actual.get_ipx_source_socket()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with IpxPacketHeader")
        return results


class IpxPacketConstants:
    def __init__(self):
        pass

    IPX_CHECKSUM = "IPX_CHECKSUM"

    IPX_PACKET_LENGTH = "IPX_PACKET_LENGTH"

    IPX_TRANSPORT_CONTROL = "IPX_TRANSPORT_CONTROL"

    IPX_PACKET_TYPE = "IPX_PACKET_TYPE"
    IPX_PACKET_TYPE_UNKNOWN = "0"
    IPX_PACKET_TYPE_NCP = "17"
    IPX_PACKET_TYPE_RIP = "1"
    IPX_PACKET_TYPE_ERROR_PACKET = "3"
    IPX_PACKET_TYPE_ECHO_PACKET = "2"
    IPX_PACKET_TYPE_SPX = "5"
    IPX_PACKET_TYPE_PEP = "4"

    IPX_DESTINATION_NETWORK = "IPX_DESTINATION_NETWORK"
    IPX_DESTINATION_NODE = "IPX_DESTINATION_NODE"
    IPX_DESTINATION_SOCKET = "IPX_DESTINATION_SOCKET"

    IPX_SOURCE_NETWORK = "IPX_SOURCE_NETWORK"
    IPX_SOURCE_NODE = "IPX_SOURCE_NODE"
    IPX_SOURCE_SOCKET = "IPX_SOURCE_SOCKET"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
