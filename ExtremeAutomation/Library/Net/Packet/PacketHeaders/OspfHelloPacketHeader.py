from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader, OspfTlvEntry
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb


class OspfHelloPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF Hello Packet Header
        # network mask = 32bits
        # hello interval = 16bits
        # options = 8bits
        # router priority = 8bits
        # router_dead_interval = 32bits
        # designated_router = 32bits
        # backup_designated_router = 32bits
        # active_neighbor = 32bits

        http://www.freesoft.org/CIE/RFC/1583/104.htm
        0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                        Network Mask                           |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |         HelloInterval         |    Options    |    Rtr Pri    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                     RouterDeadInterval                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                      Designated Router                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                   Backup Designated Router                    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                          Neighbor                             |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                              ...                              |
    """

    def __init__(self):
        self.add_hello_header()
        self.tlv_entries = []
        self.HEADER_SIZE_HELLO = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Hello network mask methods
    #  network_mask is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_hello_network_mask(self, network_mask, ignore_check=False):
        network_mask = self.normalize_value(network_mask, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_NETWORK_MASK, network_mask)

    def get_hello_network_mask(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_NETWORK_MASK),
            PacketConstants.IPV4_ADDRESS)

    def get_hello_network_mask_hltapi_cmd(self, dummy_dict):
        network_mask = self.get_hello_network_mask()
        if network_mask and 'Not Set' not in network_mask:
            dummy_dict[TrafficConfigConstants.TEMP_NETWORK_MASK_CMD] = network_mask
    # end Hello network mask methods

    # start Hello hello interval methods
    #  hello_interval is a 16 bit INTEGER example: 1
    def set_hello_hello_interval(self, hello_interval, ignore_check=False):
        hello_interval = self.normalize_value(hello_interval, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_HELLO_INTERVAL, hello_interval)

    def get_hello_hello_interval(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_HELLO_INTERVAL),
            PacketConstants.INTEGER)

    def get_hello_hello_interval_hltapi_cmd(self, dummy_dict):
        hello_interval = self.get_hello_hello_interval()
        if isinstance(hello_interval, int):
            hello_interval = str(hello_interval)
        if hello_interval and 'Not Set' not in hello_interval:
            dummy_dict[TrafficConfigConstants.TEMP_HELLO_INTERVAL_CMD] = hello_interval
    # end Hello hello interval methods

    # start Hello options methods
    #  options is a 8 bit INTEGER example: 1
    def set_hello_options(self, options, ignore_check=False):
        options = self.normalize_value(options, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_OPTIONS, options)

    def get_hello_options(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_OPTIONS),
            PacketConstants.INTEGER)

    def get_hello_options_hltapi_cmd(self, dummy_dict):
        options = self.get_hello_options()
        if isinstance(options, int):
            options = str(options)
        if options and 'Not Set' not in options:
            dummy_dict[TrafficConfigConstants.TEMP_OPTIONS_CMD] = options
    # end Hello options methods

    # start Hello router priority methods
    #  router_priority is a 8 bit INTEGER example: 1
    def set_hello_router_priority(self, router_priority, ignore_check=False):
        router_priority = self.normalize_value(router_priority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_ROUTER_PRIORITY, router_priority)

    def get_hello_router_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_ROUTER_PRIORITY),
            PacketConstants.INTEGER)

    def get_hello_router_priority_hltapi_cmd(self, dummy_dict):
        router_priority = self.get_hello_router_priority()
        if isinstance(router_priority, int):
            router_priority = str(router_priority)
        if router_priority and 'Not Set' not in router_priority:
            dummy_dict[TrafficConfigConstants.TEMP_ROUTER_PRIORITY_CMD] = router_priority
    # end Hello router priority methods

    # start Hello router_dead_interval methods
    #  router_dead_interval is a 32 bit INTEGER example: 1
    def set_hello_router_dead_interval(self, router_dead_interval, ignore_check=False):
        router_dead_interval = self.normalize_value(router_dead_interval, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_ROUTER_DEAD_INTERVAL, router_dead_interval)

    def get_hello_router_dead_interval(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_ROUTER_DEAD_INTERVAL),
            PacketConstants.INTEGER)

    def get_hello_router_dead_interval_hltapi_cmd(self, dummy_dict):
        router_dead_interval = self.get_hello_router_dead_interval()
        if isinstance(router_dead_interval, int):
            router_dead_interval = str(router_dead_interval)
        if router_dead_interval and 'Not Set' not in router_dead_interval:
            dummy_dict[TrafficConfigConstants.TEMP_ROUTER_DEAD_INTERVAL_CMD] = router_dead_interval
    # end Hello router_dead_interval methods

    # start Hello designated_router methods
    #  designated_router is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_hello_designated_router(self, designated_router, ignore_check=False):
        designated_router = self.normalize_value(designated_router, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_DESIGNATED_ROUTER, designated_router)

    def get_hello_designated_router(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_DESIGNATED_ROUTER),
            PacketConstants.IPV4_ADDRESS)

    def get_hello_designated_router_hltapi_cmd(self, dummy_dict):
        designated_router = self.get_hello_designated_router()
        if designated_router and 'Not Set' not in designated_router:
            dummy_dict[TrafficConfigConstants.TEMP_DESIGNATED_ROUTER_CMD] = designated_router
    # end Hello designated_router methods

    # start Hello backup_designated_router methods
    #  backup_designated_router is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_hello_backup_designated_router(self, backup_designated_router, ignore_check=False):
        backup_designated_router = self.normalize_value(backup_designated_router, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_BACKUP_DESIGNATED_ROUTER, backup_designated_router)

    def get_hello_backup_designated_router(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_BACKUP_DESIGNATED_ROUTER),
            PacketConstants.IPV4_ADDRESS)

    def get_hello_backup_designated_router_hltapi_cmd(self, dummy_dict):
        backup_designated_router = self.get_hello_backup_designated_router()
        if backup_designated_router and 'Not Set' not in backup_designated_router:
            dummy_dict[TrafficConfigConstants.TEMP_BACKUP_DESIGNATED_ROUTER_CMD] = backup_designated_router
    # end Hello backup_designated_router methods

    # start Hello active_neighbor methods
    #  active_neighbor is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_hello_active_neighbor(self, active_neighbor, ignore_check=False):
        active_neighbor = self.normalize_value(active_neighbor, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.HELLO_ACTIVE_NEIGHBOR, active_neighbor)

    def get_hello_active_neighbor(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.HELLO_ACTIVE_NEIGHBOR),
            PacketConstants.IPV4_ADDRESS)

    def get_hello_active_neighbor_hltapi_cmd(self, dummy_dict):
        active_neighbor = self.get_hello_active_neighbor()
        if active_neighbor and 'Not Set' not in active_neighbor:
            dummy_dict[TrafficConfigConstants.TEMP_ACTIVE_NEIGHBOR_CMD] = active_neighbor
    # end Hello active_neighbor methods

    def set_lls_data_block_checksum(self, active_neighbor, ignore_check=False):
        active_neighbor = self.normalize_value(active_neighbor, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.LLS_DATA_BLOCK_CHECKSUM, active_neighbor)

    def get_lls_data_block_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.LLS_DATA_BLOCK_CHECKSUM),
            PacketConstants.INTEGER)

    def set_lls_data_block_lengtgh(self, active_neighbor, ignore_check=False):
        active_neighbor = self.normalize_value(active_neighbor, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_HELLO,
                                  OspfHelloPacketConstants.LLS_DATA_BLOCK_LENGTH, active_neighbor)

    def get_lls_data_block_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_HELLO, OspfHelloPacketConstants.LLS_DATA_BLOCK_LENGTH),
            PacketConstants.INTEGER)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("network mask", self.get_hello_network_mask())
        table.add_row_value("hello interval", self.format_int(self.get_hello_hello_interval(), 4))
        table.add_row_value("options", self.format_int(self.get_hello_options(), 2))
        table.add_row_value("router priority", self.format_int(self.get_hello_router_priority(), 2))
        table.add_row_value("router_dead_interval", self.format_int(self.get_hello_router_dead_interval(), 8))
        table.add_row_value("designated_router", self.get_hello_designated_router())
        table.add_row_value("backup_designated_router", self.get_hello_backup_designated_router())

        packet_length = self.get_ospf_packet_length()
        if isinstance(packet_length, str) and "Not" in packet_length:
            pass
        else:
            if packet_length > 44:
                table.add_row_value("active_neighbor", self.get_hello_active_neighbor())

        rt_string = "\n\nHELLO HEADER" + table.to_table_string()

        options = self.get_hello_options()
        if isinstance(options, str) and "Not" in options:
            pass
        else:
            has_lls_data_block = (options & 0x10) > 0
            if has_lls_data_block:
                table_lls = TableFormatter()
                table_lls.add_row_value("Checksum", self.format_int(self.get_lls_data_block_checksum(), 2))
                table_lls.add_row_value("Length", self.format_int(self.get_lls_data_block_length(), 2))

                rt_string += "\n\nLLS Data Block" + table_lls.to_table_string()
                table_tlv = OspfTlvEntry.to_packet_string(self)
                rt_string += "\nOSPF LLS TLVs " + table_tlv.to_table_string()

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            rt_string += "\n\nAuth Crypt Data:" + self.get_ospf_auth_crypt_data() + "\n\n"
        return rt_string

    def add_hello_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF_HELLO)

    def build(self):
        self.add_hello_header()
        self.set_ospf_message_type(0x01, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_hello_network_mask_hltapi_cmd(dummy_dict)
        # self.get_hello_hello_interval_hltapi_cmd(dummy_dict)
        # self.get_hello_options_hltapi_cmd(dummy_dict)
        # self.get_hello_router_priority_hltapi_cmd(dummy_dict)
        # self.get_hello_router_dead_interval_hltapi_cmd(dummy_dict)
        # self.get_hello_designated_router_hltapi_cmd(dummy_dict)
        # self.get_hello_backup_designated_router_hltapi_cmd(dummy_dict)
        # self.get_hello_active_neighbor_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_hello(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_hello(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_hello(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_hello(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.khelloFieldNumber
    # update this from the ostinato docs.
    #     helloField = p.Extensions[hello]
    #     if self.is_field_set(self.get_hello_network_mask()):
    #         helloField.version = int(self.get_hello_network_mask())
    #     if self.is_field_set(self.get_hello_hello_interval()):
    #         helloField.version = int(self.get_hello_hello_interval())
    #     if self.is_field_set(self.get_hello_options()):
    #         helloField.version = int(self.get_hello_options())
    #     if self.is_field_set(self.get_hello_router_priority()):
    #         helloField.version = int(self.get_hello_router_priority())
    #     if self.is_field_set(self.get_hello_router_dead_interval()):
    #         helloField.version = int(self.get_hello_router_dead_interval())
    #     if self.is_field_set(self.get_hello_designated_router()):
    #         helloField.version = int(self.get_hello_designated_router())
    #     if self.is_field_set(self.get_hello_backup_designated_router()):
    #         helloField.version = int(self.get_hello_backup_designated_router())
    #     if self.is_field_set(self.get_hello_active_neighbor()):
    #         helloField.version = int(self.get_hello_active_neighbor())

    def config_jets_stream_hello(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "HELLO_HDR"
        pkt_bytes = "0x" + OspfHelloPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_hello_network_mask()):
        #     pkt_fields["network_mask"] = int(self.get_hello_network_mask())
        # if self.is_field_set(self.get_hello_hello_interval()):
        #     pkt_fields["hello_interval"] = int(self.get_hello_hello_interval())
        # if self.is_field_set(self.get_hello_options()):
        #     pkt_fields["options"] = int(self.get_hello_options())
        # if self.is_field_set(self.get_hello_router_priority()):
        #     pkt_fields["router_priority"] = int(self.get_hello_router_priority())
        # if self.is_field_set(self.get_hello_router_dead_interval()):
        #     pkt_fields["router_dead_interval"] = int(self.get_hello_router_dead_interval())
        # if self.is_field_set(self.get_hello_designated_router()):
        #     pkt_fields["designated_router"] = int(self.get_hello_designated_router())
        # if self.is_field_set(self.get_hello_backup_designated_router()):
        #     pkt_fields["backup_designated_router"] = int(self.get_hello_backup_designated_router())
        # if self.is_field_set(self.get_hello_active_neighbor()):
        #     pkt_fields["active_neighbor"] = int(self.get_hello_active_neighbor())

    def get_ixtclhal_hello_api_commands(self, port_string, streamid):
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
        self.tlv_entries = []
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        network_mask = self.get_bits_from_string(32, payload)
        self.set_hello_network_mask("0x" + network_mask)
        payload = self.remove_bits_from_string(32, payload)
        hello_interval = self.get_bits_from_string(16, payload)
        self.set_hello_hello_interval("0x" + hello_interval)
        payload = self.remove_bits_from_string(16, payload)
        options = self.get_bits_from_string(8, payload)
        self.set_hello_options("0x" + options)
        options = int(options, 16)
        has_lls_data_block = (options & 0x10) > 0
        payload = self.remove_bits_from_string(8, payload)
        router_priority = self.get_bits_from_string(8, payload)
        self.set_hello_router_priority("0x" + router_priority)
        payload = self.remove_bits_from_string(8, payload)
        router_dead_interval = self.get_bits_from_string(32, payload)
        self.set_hello_router_dead_interval("0x" + router_dead_interval)
        payload = self.remove_bits_from_string(32, payload)
        designated_router = self.get_bits_from_string(32, payload)
        self.set_hello_designated_router("0x" + designated_router)
        payload = self.remove_bits_from_string(32, payload)
        backup_designated_router = self.get_bits_from_string(32, payload)
        self.set_hello_backup_designated_router("0x" + backup_designated_router)
        payload = self.remove_bits_from_string(32, payload)

        packet_length = self.get_ospf_packet_length()
        if packet_length > 44:
            active_neighbor = self.get_bits_from_string(32, payload)
            self.set_hello_active_neighbor("0x" + active_neighbor)
            payload = self.remove_bits_from_string(32, payload)

        payload = OspfPacketHeader.process_auth_entry(payload, self)

        if has_lls_data_block:
            lls_checksum = self.get_bits_from_string(16, payload)
            self.set_lls_data_block_checksum("0x" + lls_checksum)
            payload = self.remove_bits_from_string(16, payload)

            lls_data_length = self.get_bits_from_string(16, payload)
            self.set_lls_data_block_lengtgh("0x" + lls_data_length)
            payload = self.remove_bits_from_string(16, payload)

            payload = OspfTlvEntry.process_tlv(payload, self.tlv_entries, lls_data_length, self)
        else:
            payload = OspfTlvEntry.process_tlv(payload, self.tlv_entries, hex(self.get_ospf_packet_length())[2:], self)

        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_hello_network_mask(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_hello_hello_interval(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_hello_options(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_hello_router_priority(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_hello_router_dead_interval(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_hello_designated_router(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_hello_backup_designated_router(),
                                              PacketConstants.IPV4_ADDRESS, 32)

        packet_length = self.get_ospf_packet_length()
        if isinstance(packet_length, str) and "Not" in packet_length:
            pass
        else:
            if packet_length > 44:
                ret_string += self.format_byte_string(self.get_hello_active_neighbor(),
                                                      PacketConstants.IPV4_ADDRESS, 32)

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            ret_string += self.get_bytes_auth_entry(self).replace("0x", "")

        options = self.get_hello_options()
        if isinstance(options, str) and "Not" in options:
            pass
        else:
            has_lls_data_block = (options & 0x10) > 0
            if has_lls_data_block:
                ret_string += self.format_byte_string(self.get_lls_data_block_checksum(), PacketConstants.INTEGER, 16)
                ret_string += self.format_byte_string(self.get_lls_data_block_length(), PacketConstants.INTEGER, 16)
                for entry in self.tlv_entries:
                    ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 16)
                    ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 16)
                    ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string.replace("0x", "")

    @staticmethod
    def compare_hello_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfHelloPacketHeader)
            assert isinstance(actual, OspfHelloPacketHeader)
            if expected.is_field_set(expected.get_hello_network_mask()) and \
                    OspfHelloPacketConstants.HELLO_NETWORK_MASK not in ignore_list:
                name = "HELLO network mask : "
                if expected.get_hello_network_mask() != actual.get_hello_network_mask():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_network_mask()) + " != " +
                                                      str(actual.get_hello_network_mask()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_network_mask()) + " == " +
                                                 str(actual.get_hello_network_mask()) + " Pass")

            if expected.is_field_set(expected.get_hello_hello_interval()) and \
                    OspfHelloPacketConstants.HELLO_HELLO_INTERVAL not in ignore_list:
                name = "HELLO hello interval : "
                if expected.get_hello_hello_interval() != actual.get_hello_hello_interval():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_hello_interval()) + " != " +
                                                      str(actual.get_hello_hello_interval()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_hello_interval()) + " == " +
                                                 str(actual.get_hello_hello_interval()) + " Pass")

            if expected.is_field_set(expected.get_hello_options()) and \
                    OspfHelloPacketConstants.HELLO_OPTIONS not in ignore_list:
                name = "HELLO options : "
                if expected.get_hello_options() != actual.get_hello_options():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_options()) + " != " +
                                                      str(actual.get_hello_options()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_options()) + " == " +
                                                 str(actual.get_hello_options()) + " Pass")

            if expected.is_field_set(expected.get_hello_router_priority()) and \
                    OspfHelloPacketConstants.HELLO_ROUTER_PRIORITY not in ignore_list:
                name = "HELLO router priority : "
                if expected.get_hello_router_priority() != actual.get_hello_router_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_router_priority()) + " != " +
                                                      str(actual.get_hello_router_priority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_router_priority()) + " == " +
                                                 str(actual.get_hello_router_priority()) + " Pass")

            if expected.is_field_set(expected.get_hello_router_dead_interval()) and \
                    OspfHelloPacketConstants.HELLO_ROUTER_DEAD_INTERVAL not in ignore_list:
                name = "HELLO router_dead_interval : "
                if expected.get_hello_router_dead_interval() != actual.get_hello_router_dead_interval():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_router_dead_interval()) + " != " +
                                                      str(actual.get_hello_router_dead_interval()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_router_dead_interval()) + " == " +
                                                 str(actual.get_hello_router_dead_interval()) + " Pass")

            if expected.is_field_set(expected.get_hello_designated_router()) and \
                    OspfHelloPacketConstants.HELLO_DESIGNATED_ROUTER not in ignore_list:
                name = "HELLO designated_router : "
                if expected.get_hello_designated_router() != actual.get_hello_designated_router():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_designated_router()) + " != " +
                                                      str(actual.get_hello_designated_router()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_designated_router()) + " == " +
                                                 str(actual.get_hello_designated_router()) + " Pass")

            if expected.is_field_set(expected.get_hello_backup_designated_router()) and \
                    OspfHelloPacketConstants.HELLO_BACKUP_DESIGNATED_ROUTER not in ignore_list:
                name = "HELLO backup_designated_router : "
                if expected.get_hello_backup_designated_router() != actual.get_hello_backup_designated_router():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_backup_designated_router()) + " != " +
                                                      str(actual.get_hello_backup_designated_router()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_backup_designated_router()) + " == " +
                                                 str(actual.get_hello_backup_designated_router()) + " Pass")

            if expected.is_field_set(expected.get_hello_active_neighbor()) and \
                    OspfHelloPacketConstants.HELLO_ACTIVE_NEIGHBOR not in ignore_list:
                name = "HELLO active_neighbor : "
                if expected.get_hello_active_neighbor() != actual.get_hello_active_neighbor():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_hello_active_neighbor()) + " != " +
                                                      str(actual.get_hello_active_neighbor()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_hello_active_neighbor()) + " == " +
                                                 str(actual.get_hello_active_neighbor()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with HelloPacketHeader")
        return results


class OspfHelloPacketConstants:
    def __init__(self):
        pass

    HELLO_NETWORK_MASK = "HELLO_NETWORK_MASK"
    HELLO_HELLO_INTERVAL = "HELLO_HELLO_INTERVAL"
    HELLO_OPTIONS = "HELLO_OPTIONS"
    HELLO_ROUTER_PRIORITY = "HELLO_ROUTER_PRIORITY"
    HELLO_ROUTER_DEAD_INTERVAL = "HELLO_ROUTER_DEAD_INTERVAL"
    HELLO_DESIGNATED_ROUTER = "HELLO_DESIGNATED_ROUTER"
    HELLO_BACKUP_DESIGNATED_ROUTER = "HELLO_BACKUP_DESIGNATED_ROUTER"
    HELLO_ACTIVE_NEIGHBOR = "HELLO_ACTIVE_NEIGHBOR"

    LLS_DATA_BLOCK_CHECKSUM = "HELLO_LLS_DATA_BLOCK_CHECKSUM"
    LLS_DATA_BLOCK_LENGTH = "HELLO_LLS_DATA_BLOCK_LENGTH"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
