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
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump


class ProviderBackboneBridgePacketHeader(InnerPacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    Provider Backbone Bridge Packet Header
        # Flag Priority = 3bits
        # Flag DROP = 1bits
        # Flag NCA = 1bits
        # Flag Res1 = 1bits
        # Flag Res2 = 2bits
        # iSID = 24bits
    """

    def __init__(self):
        self.add_providerbackbonebridge_header()
        self.innerpacket = None
        self.HEADER_SIZE_PROVIDERBACKBONEBRIDGE = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start ProviderBackboneBridge Flag Priority methods
    #  flag_priority is a 3 bit INTEGER example: 1
    def set_providerbackbonebridge_flag_priority(self, flag_priority, ignore_check=False):
        flag_priority = self.normalize_value(flag_priority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_PRIORITY,
                                  flag_priority)

    def get_providerbackbonebridge_flag_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_PRIORITY), PacketConstants.INTEGER)

    def get_providerbackbonebridge_flag_priority_hltapi_cmd(self, dummy_dict):
        flag_priority = self.get_providerbackbonebridge_flag_priority()
        if isinstance(flag_priority, int):
            flag_priority = str(flag_priority)
        if flag_priority and 'Not Set' not in flag_priority:
            dummy_dict[TrafficConfigConstants.TEMP_FLAG_PRIORITY_CMD] = flag_priority
    # end ProviderBackboneBridge Flag Priority methods

    # start ProviderBackboneBridge Flag DROP methods
    #  flag_drop is a 1 bit INTEGER example: 1
    def set_providerbackbonebridge_flag_drop(self, flag_drop, ignore_check=False):
        flag_drop = self.normalize_value(flag_drop, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_DROP, flag_drop)

    def get_providerbackbonebridge_flag_drop(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_DROP), PacketConstants.INTEGER)

    def get_providerbackbonebridge_flag_drop_hltapi_cmd(self, dummy_dict):
        flag_drop = self.get_providerbackbonebridge_flag_drop()
        if isinstance(flag_drop, int):
            flag_drop = str(flag_drop)
        if flag_drop and 'Not Set' not in flag_drop:
            dummy_dict[TrafficConfigConstants.TEMP_FLAG_DROP_CMD] = flag_drop
    # end ProviderBackboneBridge Flag DROP methods

    # start ProviderBackboneBridge Flag NCA methods
    #  flag_nca is a 1 bit INTEGER example: 1
    def set_providerbackbonebridge_flag_nca(self, flag_nca, ignore_check=False):
        flag_nca = self.normalize_value(flag_nca, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_NCA, flag_nca)

    def get_providerbackbonebridge_flag_nca(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_NCA), PacketConstants.INTEGER)

    def get_providerbackbonebridge_flag_nca_hltapi_cmd(self, dummy_dict):
        flag_nca = self.get_providerbackbonebridge_flag_nca()
        if isinstance(flag_nca, int):
            flag_nca = str(flag_nca)
        if flag_nca and 'Not Set' not in flag_nca:
            dummy_dict[TrafficConfigConstants.TEMP_FLAG_NCA_CMD] = flag_nca
    # end ProviderBackboneBridge Flag NCA methods

    # start ProviderBackboneBridge Flag Res1 methods
    #  flag_res1 is a 1 bit INTEGER example: 1
    def set_providerbackbonebridge_flag_res1(self, flag_res1, ignore_check=False):
        flag_res1 = self.normalize_value(flag_res1, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES1, flag_res1)

    def get_providerbackbonebridge_flag_res1(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES1), PacketConstants.INTEGER)

    def get_providerbackbonebridge_flag_res1_hltapi_cmd(self, dummy_dict):
        flag_res1 = self.get_providerbackbonebridge_flag_res1()
        if isinstance(flag_res1, int):
            flag_res1 = str(flag_res1)
        if flag_res1 and 'Not Set' not in flag_res1:
            dummy_dict[TrafficConfigConstants.TEMP_FLAG_RES1_CMD] = flag_res1
    # end ProviderBackboneBridge Flag Res1 methods

    # start ProviderBackboneBridge Flag Res2 methods
    #  flag_res2 is a 2 bit INTEGER example: 1
    def set_providerbackbonebridge_flag_res2(self, flag_res2, ignore_check=False):
        flag_res2 = self.normalize_value(flag_res2, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES2, flag_res2)

    def get_providerbackbonebridge_flag_res2(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES2), PacketConstants.INTEGER)

    def get_providerbackbonebridge_flag_res2_hltapi_cmd(self, dummy_dict):
        flag_res2 = self.get_providerbackbonebridge_flag_res2()
        if isinstance(flag_res2, int):
            flag_res2 = str(flag_res2)
        if flag_res2 and 'Not Set' not in flag_res2:
            dummy_dict[TrafficConfigConstants.TEMP_FLAG_RES2_CMD] = flag_res2
    # end ProviderBackboneBridge Flag Res2 methods

    # start ProviderBackboneBridge iSID methods
    #  isid is a 24 bit INTEGER example: 1
    def set_providerbackbonebridge_isid(self, isid, ignore_check=False):
        isid = self.normalize_value(isid, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
                                  ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_ISID, isid)

    def get_providerbackbonebridge_isid(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L2_PROVIDERBACKBONEBRIDGE,
            ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_ISID), PacketConstants.INTEGER)

    def get_providerbackbonebridge_isid_hltapi_cmd(self, dummy_dict):
        isid = self.get_providerbackbonebridge_isid()
        if isinstance(isid, int):
            isid = str(isid)
        if isid and 'Not Set' not in isid:
            dummy_dict[TrafficConfigConstants.TEMP_ISID_CMD] = isid
    # end ProviderBackboneBridge iSID methods

    # start pbb inner packet methods
    #  routing is a 32 bit INTEGER example: 1
    def set_providerbackbonebridge_inner_packet(self, innerpacket, ignore_check=False):
        # routing = self.normalize_value(routing, PacketConstants.INTEGER)
        # self.set_packet_component(PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING, routing)
        self.innerpacket = innerpacket

    def get_providerbackbonebridge_inner_packet(self):
        # return self.normalize_value(self.get_packet_component(
        #     PacketConstants.PACKET_HEADER_L3_GRE, GrePacketConstants.GRE_ROUTING), PacketConstants.INTEGER)
        return self.innerpacket

    def set_inner_packet(self, packet):
        return self.set_providerbackbonebridge_inner_packet(packet)

    def get_inner_packet(self):
        return self.get_providerbackbonebridge_inner_packet()

        # def get_gre_inner_packet_hltapi_cmd(self, dummy_dict):
        #     routing = self.get_gre_routing()
        #     if isinstance(routing, int):
        #         routing = str(routing)
        #     if routing and 'Not Set' not in routing:
        #         dummy_dict[TrafficConfigConstants.TEMP_ROUTING_CMD] = routing
        # end Gre routing methods

    def get_providerbackbonebridge_inner_packet_length(self):
        pkt_buffer = self.innerpacket.get_header_length()  # + 4  # add the CRC
        minsize = 64
        if isinstance(self, TaggedPacketHeader):
            minsize += 4
        elif isinstance(self, VlanStackPacketHeader):
            minsize += (4 * self.get_vlan_num())
        return max(pkt_buffer, minsize)

    def get_inner_packet_length(self):
        return self.get_providerbackbonebridge_inner_packet_length()

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Flag Priority", self.format_int(self.get_providerbackbonebridge_flag_priority(), 0))
        table.add_row_value("Flag DROP", self.format_int(self.get_providerbackbonebridge_flag_drop(), 0))
        table.add_row_value("Flag NCA", self.format_int(self.get_providerbackbonebridge_flag_nca(), 0))
        table.add_row_value("Flag Res1", self.format_int(self.get_providerbackbonebridge_flag_res1(), 0))
        table.add_row_value("Flag Res2", self.format_int(self.get_providerbackbonebridge_flag_res2(), 0))
        table.add_row_value("iSID", self.format_int(self.get_providerbackbonebridge_isid(), 3))
        inner_packet = self.get_providerbackbonebridge_inner_packet()
        if inner_packet:
            return "\n\nPROVIDERBACKBONEBRIDGE HEADER" + table.to_table_string() + "\n\nInner Packet\n" + \
                   inner_packet.to_packet_string()
        else:
            return "\n\nPROVIDERBACKBONEBRIDGE HEADER" + table.to_table_string() + "\n\nInner Packet\n" + \
                   "No inner packet"

    def add_providerbackbonebridge_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_PROVIDERBACKBONEBRIDGE)

    def build(self):
        self.add_providerbackbonebridge_header()
        try:
            self.set_ether_type("0x88E7", True)
        except Exception as e:
            PacketObject.logger.log_info("The following Exception was caught, Continuing on:\n" + repr(e))

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_providerbackbonebridge_flag_priority_hltapi_cmd(dummy_dict)
        # self.get_providerbackbonebridge_flag_drop_hltapi_cmd(dummy_dict)
        # self.get_providerbackbonebridge_flag_nca_hltapi_cmd(dummy_dict)
        # self.get_providerbackbonebridge_flag_res1_hltapi_cmd(dummy_dict)
        # self.get_providerbackbonebridge_flag_res2_hltapi_cmd(dummy_dict)
        # self.get_providerbackbonebridge_isid_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_providerbackbonebridge(self, tgen_type, generator_ref, port_string,
                                                                          stream_id, **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_providerbackbonebridge(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_providerbackbonebridge(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_providerbackbonebridge(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        # p.protocol_id.id = ost_pb.Protocol.kproviderbackbonebridgeFieldNumber
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = ProviderBackboneBridgePacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
        # # update this from the ostinato docs.
        #     providerbackbonebridgeField = p.Extensions[providerbackbonebridge]
        #     if self.is_field_set(self.get_providerbackbonebridge_flag_priority()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_flag_priority())
        #     if self.is_field_set(self.get_providerbackbonebridge_flag_drop()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_flag_drop())
        #     if self.is_field_set(self.get_providerbackbonebridge_flag_nca()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_flag_nca())
        #     if self.is_field_set(self.get_providerbackbonebridge_flag_res1()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_flag_res1())
        #     if self.is_field_set(self.get_providerbackbonebridge_flag_res2()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_flag_res2())
        #     if self.is_field_set(self.get_providerbackbonebridge_isid()):
        #         providerbackbonebridgeField.version = int(self.get_providerbackbonebridge_isid())

    def config_jets_stream_providerbackbonebridge(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "PROVIDERBACKBONEBRIDGE_HDR"
        pkt_bytes = "0x" + ProviderBackboneBridgePacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_providerbackbonebridge_flag_priority()):
        #     pkt_fields["flag_priority"] = int(self.get_providerbackbonebridge_flag_priority())
        # if self.is_field_set(self.get_providerbackbonebridge_flag_drop()):
        #     pkt_fields["flag_drop"] = int(self.get_providerbackbonebridge_flag_drop())
        # if self.is_field_set(self.get_providerbackbonebridge_flag_nca()):
        #     pkt_fields["flag_nca"] = int(self.get_providerbackbonebridge_flag_nca())
        # if self.is_field_set(self.get_providerbackbonebridge_flag_res1()):
        #     pkt_fields["flag_res1"] = int(self.get_providerbackbonebridge_flag_res1())
        # if self.is_field_set(self.get_providerbackbonebridge_flag_res2()):
        #     pkt_fields["flag_res2"] = int(self.get_providerbackbonebridge_flag_res2())
        # if self.is_field_set(self.get_providerbackbonebridge_isid()):
        #     pkt_fields["isid"] = int(self.get_providerbackbonebridge_isid())

    def get_ixtclhal_providerbackbonebridge_api_commands(self, port_string, streamid):
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

        value = self.get_bits_from_string(8, payload)
        value = NumberUtils.to_integer_value("0x" + value)
        payload = self.remove_bits_from_string(8, payload)
        flag_priority = (value & 0x0E0) >> 5
        self.set_providerbackbonebridge_flag_priority(flag_priority)
        flag_drop = (value & 0x010) >> 4
        self.set_providerbackbonebridge_flag_drop(flag_drop)
        flag_nca = (value & 0x08) >> 3
        self.set_providerbackbonebridge_flag_nca(flag_nca)
        flag_res1 = (value & 0x04) >> 2
        self.set_providerbackbonebridge_flag_res1(flag_res1)
        flag_res2 = (value & 0x03)
        self.set_providerbackbonebridge_flag_res2(flag_res2)

        isid = self.get_bits_from_string(24, payload)
        self.set_providerbackbonebridge_isid("0x" + isid)
        payload = self.remove_bits_from_string(24, payload)
        self.payload = payload
        packet = EthernetPacket()
        packet.set_payload(payload)
        self.set_providerbackbonebridge_inner_packet(packet)

    def get_header_bytes(self):
        ret_string = ""
        value = 0
        if self.is_field_set(self.get_providerbackbonebridge_flag_priority()):
            value |= NumberUtils.to_integer_value(self.get_providerbackbonebridge_flag_priority()) << 5
        if self.is_field_set(self.get_providerbackbonebridge_flag_drop()):
            value |= NumberUtils.to_integer_value(self.get_providerbackbonebridge_flag_drop()) << 4
        if self.is_field_set(self.get_providerbackbonebridge_flag_nca()):
            value |= NumberUtils.to_integer_value(self.get_providerbackbonebridge_flag_nca()) << 3
        if self.is_field_set(self.get_providerbackbonebridge_flag_priority()):
            value |= NumberUtils.to_integer_value(self.get_providerbackbonebridge_flag_res1()) << 2
        if self.is_field_set(self.get_providerbackbonebridge_flag_res2()):
            value |= NumberUtils.to_integer_value(self.get_providerbackbonebridge_flag_res2()) << 0
        ret_string += self.format_byte_string(value, PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_providerbackbonebridge_isid(), PacketConstants.INTEGER, 24)
        ret_string += self.get_providerbackbonebridge_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_providerbackbonebridge_packet_header(expected, actual, ignore_list, print_results=True,
                                                     print_failures=True):
        results = True
        try:
            assert isinstance(expected, ProviderBackboneBridgePacketHeader)
            assert isinstance(actual, ProviderBackboneBridgePacketHeader)
            if expected.is_field_set(expected.get_providerbackbonebridge_flag_priority()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_PRIORITY not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE flag priority : "
                if expected.get_providerbackbonebridge_flag_priority() != \
                        actual.get_providerbackbonebridge_flag_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_flag_priority()) +
                                                      " != " + str(actual.get_providerbackbonebridge_flag_priority()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_flag_priority()) +
                                                 " == " + str(actual.get_providerbackbonebridge_flag_priority()) +
                                                 " Pass")

            if expected.is_field_set(expected.get_providerbackbonebridge_flag_drop()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_DROP not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE flag drop : "
                if expected.get_providerbackbonebridge_flag_drop() != actual.get_providerbackbonebridge_flag_drop():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_flag_drop()) + " != " +
                                                      str(actual.get_providerbackbonebridge_flag_drop()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_flag_drop()) + " == " +
                                                 str(actual.get_providerbackbonebridge_flag_drop()) + " Pass")

            if expected.is_field_set(expected.get_providerbackbonebridge_flag_nca()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_NCA not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE flag nca : "
                if expected.get_providerbackbonebridge_flag_nca() != actual.get_providerbackbonebridge_flag_nca():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_flag_nca()) + " != " +
                                                      str(actual.get_providerbackbonebridge_flag_nca()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_flag_nca()) + " == " +
                                                 str(actual.get_providerbackbonebridge_flag_nca()) + " Pass")

            if expected.is_field_set(expected.get_providerbackbonebridge_flag_res1()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES1 not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE flag res1 : "
                if expected.get_providerbackbonebridge_flag_res1() != actual.get_providerbackbonebridge_flag_res1():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_flag_res1()) + " != " +
                                                      str(actual.get_providerbackbonebridge_flag_res1()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_flag_res1()) + " == " +
                                                 str(actual.get_providerbackbonebridge_flag_res1()) + " Pass")

            if expected.is_field_set(expected.get_providerbackbonebridge_flag_res2()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_FLAG_RES2 not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE flag res2 : "
                if expected.get_providerbackbonebridge_flag_res2() != actual.get_providerbackbonebridge_flag_res2():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_flag_res2()) + " != " +
                                                      str(actual.get_providerbackbonebridge_flag_res2()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_flag_res2()) + " == " +
                                                 str(actual.get_providerbackbonebridge_flag_res2()) + " Pass")

            if expected.is_field_set(expected.get_providerbackbonebridge_isid()) and \
                    ProviderBackboneBridgePacketConstants.PROVIDERBACKBONEBRIDGE_ISID not in ignore_list:
                name = "PROVIDERBACKBONEBRIDGE isid : "
                if expected.get_providerbackbonebridge_isid() != actual.get_providerbackbonebridge_isid():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_providerbackbonebridge_isid()) + " != " +
                                                      str(actual.get_providerbackbonebridge_isid()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_providerbackbonebridge_isid()) + " == " +
                                                 str(actual.get_providerbackbonebridge_isid()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with ProviderBackboneBridgePacketHeader")
        return results


class ProviderBackboneBridgePacketConstants:
    def __init__(self):
        pass

    PROVIDERBACKBONEBRIDGE_FLAG_PRIORITY = "PROVIDERBACKBONEBRIDGE_FLAG_PRIORITY"
    PROVIDERBACKBONEBRIDGE_FLAG_DROP = "PROVIDERBACKBONEBRIDGE_FLAG_DROP"
    PROVIDERBACKBONEBRIDGE_FLAG_NCA = "PROVIDERBACKBONEBRIDGE_FLAG_NCA"
    PROVIDERBACKBONEBRIDGE_FLAG_RES1 = "PROVIDERBACKBONEBRIDGE_FLAG_RES1"
    PROVIDERBACKBONEBRIDGE_FLAG_RES2 = "PROVIDERBACKBONEBRIDGE_FLAG_RES2"
    PROVIDERBACKBONEBRIDGE_ISID = "PROVIDERBACKBONEBRIDGE_ISID"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
