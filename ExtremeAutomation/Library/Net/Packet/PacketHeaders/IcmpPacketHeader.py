from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.icmp_pb2 import icmp
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.Checksum import Checksum


class IcmpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ICMP Packet Header
        # type = 8bits
        # code = 8bits
        # checksum = 16bits
        # id = 16bits
        # seq = 16bits
    """

    def __init__(self):
        self.add_icmp_header()
        self.HEADER_SIZE_ICMP = (8 + 8 + 16 + 16 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Icmp type methods
    #  type is a 8 bit INTEGER example: 1
    def set_icmp_type(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IcmpPacketConstants.ICMP_TYPE, ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_TYPE, pkt_type)

    def get_icmp_type(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_TYPE),
            PacketConstants.INTEGER)

    def get_icmp_type_hltapi_cmd(self, dummy_dict):
        pkt_type = self.get_icmp_type()
        if isinstance(pkt_type, int):
            pkt_type = str(pkt_type)
        if pkt_type and 'Not Set' not in pkt_type:
            dummy_dict[TrafficConfigConstants.ICMP_TYPE_CMD] = pkt_type

    # end Icmp type methods

    # start Icmp code methods
    #  code is a 8 bit INTEGER example: 1
    def set_icmp_code(self, code, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IcmpPacketConstants.ICMP_CODE, ignore_check)
        code = self.normalize_value(code, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_CODE, code)

    def get_icmp_code(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_CODE),
            PacketConstants.INTEGER)

    def get_icmp_code_hltapi_cmd(self, dummy_dict):
        code = self.get_icmp_code()
        if isinstance(code, int):
            code = str(code)
        if code and 'Not Set' not in code:
            dummy_dict[TrafficConfigConstants.ICMP_CODE_CMD] = code

    # end Icmp code methods

    # start Icmp checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_icmp_checksum(self, checksum, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IcmpPacketConstants.ICMP_CHECKSUM, ignore_check)
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_CHECKSUM, checksum)

    def get_icmp_checksum(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_CHECKSUM),
            PacketConstants.INTEGER)

    def get_icmp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_icmp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum

    def calculate_icmp_checksum(self, header_offset):
        self.set_icmp_checksum(0)
        header_sum = Checksum.calculate_icmp_checksum(self, self.get_bytes(), header_offset, self.HEADER_SIZE_ICMP)
        header_sum = Checksum.calculate_complement(header_sum)
        self.set_icmp_checksum(header_sum)
        pass

    # end Icmp checksum methods

    # start Icmp id methods
    #  id is a 16 bit INTEGER example: 1
    def set_icmp_id(self, pkt_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IcmpPacketConstants.ICMP_ID, ignore_check)
        pkt_id = self.normalize_value(pkt_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_ID, pkt_id)

    def get_icmp_id(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_ID),
            PacketConstants.INTEGER)

    def get_icmp_id_hltapi_cmd(self, dummy_dict):
        pkt_id = self.get_icmp_id()
        if isinstance(pkt_id, int):
            pkt_id = str(pkt_id)
        if pkt_id and 'Not Set' not in pkt_id:
            dummy_dict[TrafficConfigConstants.ICMP_ID_CMD] = pkt_id

    # end Icmp id methods

    # start Icmp seq methods
    #  seq is a 16 bit INTEGER example: 1
    def set_icmp_seq(self, seq, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(IcmpPacketConstants.ICMP_SEQ, ignore_check)
        seq = self.normalize_value(seq, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_SEQ, seq)

    def get_icmp_seq(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_ICMP, IcmpPacketConstants.ICMP_SEQ),
            PacketConstants.INTEGER)

    def get_icmp_seq_hltapi_cmd(self, dummy_dict):
        seq = self.get_icmp_seq()
        if isinstance(seq, int):
            seq = str(seq)
        if seq and 'Not Set' not in seq:
            dummy_dict[TrafficConfigConstants.ICMP_SEQ_CMD] = seq
            # end Icmp seq methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("type", self.format_int(self.get_icmp_type(), 2))
        table.add_row_value("code", self.format_int(self.get_icmp_code(), 2))
        table.add_row_value("checksum", self.format_int(self.get_icmp_checksum(), 4))
        table.add_row_value("id", self.format_int(self.get_icmp_id(), 4))
        table.add_row_value("seq", self.format_int(self.get_icmp_seq(), 4))
        return "\n\nICMP HEADER" + table.to_table_string()

    def add_icmp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ICMP)

    def build(self):
        self.add_icmp_header()
        if isinstance(self, IpV4PacketHeader):
            self.set_ip_protocol(0x01, True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header(0x58, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        self.get_icmp_type_hltapi_cmd(dummy_dict)
        self.get_icmp_code_hltapi_cmd(dummy_dict)
        # self.get_icmp_checksum_hltapi_cmd(dummy_dict)
        self.get_icmp_id_hltapi_cmd(dummy_dict)
        self.get_icmp_seq_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_ICMP  # constant value
        return dummy_dict

    def get_ixtclhal_icmp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))

        # ### put some IxTclHal info here.
        if isinstance(self, IpV6PacketHeader):
            dummy_dict.append("icmpV6 get " + port_string)
            if self.is_field_set(self.get_icmp_id()):
                dummy_dict.append("icmpV6Informational config -identifier " + str(self.get_icmp_id()))
            if self.is_field_set(self.get_icmp_seq()):
                dummy_dict.append("icmpV6Informational config -sequenceNumber " + str(self.get_icmp_seq()))

            if self.is_field_set(self.get_icmp_type()):
                dummy_dict.append("icmpV6UserDefine config -type " + str(self.get_icmp_type()))
            if self.is_field_set(self.get_icmp_code()):
                dummy_dict.append("icmpV6UserDefine config -code " + str(self.get_icmp_code()))
            dummy_dict.append("icmpV6 set " + port_string)
        else:
            dummy_dict.append("icmp get " + port_string)
            if self.is_field_set(self.get_icmp_id()):
                dummy_dict.append("icmp config -id " + str(self.get_icmp_id()))
            if self.is_field_set(self.get_icmp_seq()):
                dummy_dict.append("icmp config -sequence " + str(self.get_icmp_seq()))
            dummy_dict.append("icmp set " + port_string)

        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_icmp_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_icmp(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_icmp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_icmp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_icmp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kIcmpFieldNumber
        icmpField = p.Extensions[icmp]
        # checksum = {int} 0
        # is_override_checksum = {bool} False
        if self.is_field_set(self.get_icmp_checksum()):
            icmpField.checksum = int(self.get_icmp_checksum())
            icmpField.is_override_checksum = True
        else:
            icmpField.is_override_checksum = False
        # code = {int} 0
        if self.is_field_set(self.get_icmp_code()):
            icmpField.code = int(self.get_icmp_code())
        # icmp_version = {int} 4
        # if self.is_field_set(self.get_icmp_):
        #     icmpField.icmp_version = int(self.get_icmp_)
        # identifier = {int} 1234
        if self.is_field_set(self.get_icmp_id()):
            icmpField.identifier = int(self.get_icmp_id())
        # sequence = {int} 0
        if self.is_field_set(self.get_icmp_seq()):
            icmpField.sequence = int(self.get_icmp_seq())
        # type = {int} 8
        if self.is_field_set(self.get_icmp_type()):
            icmpField.type = int(self.get_icmp_type())

    def config_jets_stream_icmp(self, jets_dev, port_string, stream_id, **kwargs):
        """
        ICMP_HDR {
          icmp_type   : 8  : legal_values=(Echo_Reply=0, Dest_Unreach=3, Source_Quench=4, Redirect=5, Echo_Request=8,
                             Rtr_Disc_Ad=9, Rtr_Disc_Sol=10, Time_Exceeded=11, Param_Problem=12, TimeStamp_Req=13,
                             TimeStamp_Reply=14, Info_Req=15, Info_Reply=16, Addr_Mask_Req=17, Addr_Mask_Reply=18,
                             Trace_Route=30 ), display="Type", index=1;
                             } display="ICMP Header", index=5092;
        ICMP_ECHO_REPLY {
          icmp_code   : 8  : display="Code %dec", index=1;
          icmp_xsum   : 16 : send = checksum(icmp, ICMP_HDR, pdu), display="Checksum", index=2;
          id          : 16 : default = 1, display="Identification %dec", index=3;
          sequence_no : 16 : default = 1, display="Sequence Number %dec", index=4;
                             } display="ICMP Echo Reply", index=5093;
        ICMPv6_HDR {
          type		  : 8 : legal_values=(DEST_UNREACH   = 1, PACKET_TOO_BIG = 2, TIME_EXCEEDED  = 3,
                            PARAM_PROBLEM  = 4, ECHO_REQUEST = 128, ECHO_REPLY=129, GRP_MEMBER_QUERY=130,
                            GRP_MEMBER_REPORT = 131, GRP_MEMBER_DONE = 132, ROUTER_SOLICIT   = 133,
                            ROUTER_ADVERTISE = 134, NEIGHBOR_SOLICIT = 135, NEIGHBOR_ADVERTISE = 136, REDIRECT = 137,
                            V2_GRP_MEMBER_REPORT = 143 ), display="Type %dec", index=1;
                            } display="ICMPv6 - Internet Control Message Protocol Version 6", index=5168;
          :param jets_dev:
          :param port_string:
          :param stream_id:
          :param kwargs:
          :return:
        """
        # this is not supported yet
        # How I knew this:
        # generator addPdlStream stream_eth6_1 1 - pdlStr "ENET_HDR src=00:33:22:33:44:66 dst=00:44:33:22:35:66
        #   type=2048,IP_HDR ip_dest_address=1.1.1.1 ip_frag_offset=2 ip_flags=3 ip_ttl=250 ip_ihl=5 ip_tos=3
        #   ip_total_length=46 ip_src_address=2.2.2.2,ICMP_HDR icmp_type=0,ICMP_ECHO_REPLY icmp_code=0
        #   sequence_no=6 id=4" - totalLen 64 - mode ManualBurst - rate 1 - burstSize 1
        # java.lang.RuntimeException: Don't support any under IP_HDR yet
        # at com.nortel.jets.adtech.generator.Flow.buildIpPdlPkt(Flow.java:637)
        # at com.nortel.jets.adtech.generator.Flow.buildEnetPdlPkt(Flow.java:924)
        # at com.nortel.jets.adtech.generator.Flow.buildPdlPkt(Flow.java:958)
        # at com.nortel.jets.adtech.generator.Flow. < init > (Flow.java:108)
        # at com.nortel.jets.adtech.generator.Flow. < init > (Flow.java:112)
        # at com.nortel.jets.adtech.generator.TrafficSrc.addPdlFlow(TrafficSrc.java:80)
        # at com.nortel.jets.adtech.generator.GeneratorObj.addPdlFlow(GeneratorObj.java:126)
        # at com.nortel.jets.adtech.generator.AddPdlStream.doCmd(AddPdlStream.java:60)
        # at com.nortel.jets.BaseCmdSet.doCmd(BaseCmdSet.java:200)

        # if isinstance(self, IpV6PacketHeader):
        #     pkt_fields = {}
        # else:
        #     pkt_fields = {}
        #     if self.is_field_set(self.get_icmp_type()):
        #         pkt_fields["icmp_type"] = str(self.get_icmp_type())
        #     jets_dev.pdl_add_packet_header("ICMP_HDR", pkt_fields)
        #
        #     pkt_fields = {}
        #     if self.is_field_set(self.get_icmp_code()):
        #         pkt_fields["icmp_code"] = str(self.get_icmp_code())
        #     if self.is_field_set(self.get_icmp_checksum()):
        #         pkt_fields["icmp_xsum"] = str(self.get_icmp_checksum())
        #     if self.is_field_set(self.get_icmp_id()):
        #         pkt_fields["id"] = str(self.get_icmp_id())
        #     if self.is_field_set(self.get_icmp_seq()):
        #         pkt_fields["sequence_no"] = str(self.get_icmp_seq())
        #     jets_dev.pdl_add_packet_header("ICMP_ECHO_REPLY", pkt_fields)

        # do it with rawdata instead
        if isinstance(self, IpV4PacketHeader):
            if not self.is_field_set(self.get_ip_protocol()):
                jets_dev.pdl_add_packet_header(JetsDeviceConstants.IP_HDR, {"ip_protocol": 1})
        elif isinstance(self, IpV6PacketHeader):
            if not self.is_field_set(self.get_ipv6_next_header()):
                jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPV6_HDR, {"next_header": 58})
            # if extention headers, find the last one and set that.
            if self.get_ipv6_extension_headers_length() > 1:
                self.get_ipv6_extension_headers()[-1].next_next_header = 58
        pkt_bytes = "0x" + IcmpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        pkt_type = self.get_bits_from_string(8, payload)
        self.set_icmp_type("0x" + pkt_type)
        payload = self.remove_bits_from_string(8, payload)
        code = self.get_bits_from_string(8, payload)
        self.set_icmp_code("0x" + code)
        payload = self.remove_bits_from_string(8, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_icmp_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)
        pkt_id = self.get_bits_from_string(16, payload)
        self.set_icmp_id("0x" + pkt_id)
        payload = self.remove_bits_from_string(16, payload)
        seq = self.get_bits_from_string(16, payload)
        self.set_icmp_seq("0x" + seq)
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_icmp_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_icmp_code(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_icmp_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_icmp_id(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_icmp_seq(), PacketConstants.INTEGER, 16)
        return ret_string

    @staticmethod
    def compare_icmp_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, IcmpPacketHeader)
            assert isinstance(actual, IcmpPacketHeader)
            if expected.do_i_check_this_field(expected.get_icmp_type(), IcmpPacketConstants.ICMP_TYPE,
                                              ignore_list, include_list):
                name = "ICMP type : "
                if expected.get_icmp_type() != actual.get_icmp_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_icmp_type()) + " != " +
                                                      str(actual.get_icmp_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_icmp_type()) + " == " +
                                                 str(actual.get_icmp_type()) + " Pass")

            if expected.do_i_check_this_field(expected.get_icmp_code(), IcmpPacketConstants.ICMP_CODE,
                                              ignore_list, include_list):
                name = "ICMP code : "
                if expected.get_icmp_code() != actual.get_icmp_code():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_icmp_code()) + " != " +
                                                      str(actual.get_icmp_code()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_icmp_code()) + " == " +
                                                 str(actual.get_icmp_code()) + " Pass")

            if expected.do_i_check_this_field(expected.get_icmp_checksum(), IcmpPacketConstants.ICMP_CHECKSUM,
                                              ignore_list, include_list):
                name = "ICMP checksum : "
                if expected.get_icmp_checksum() != actual.get_icmp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_icmp_checksum()) + " != " +
                                                      str(actual.get_icmp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_icmp_checksum()) + " == " +
                                                 str(actual.get_icmp_checksum()) + " Pass")

            if expected.do_i_check_this_field(expected.get_icmp_id(), IcmpPacketConstants.ICMP_ID,
                                              ignore_list, include_list):
                name = "ICMP id : "
                if expected.get_icmp_id() != actual.get_icmp_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_icmp_id()) + " != " +
                                                      str(actual.get_icmp_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_icmp_id()) + " == " +
                                                 str(actual.get_icmp_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_icmp_seq(), IcmpPacketConstants.ICMP_SEQ,
                                              ignore_list, include_list):
                name = "ICMP seq : "
                if expected.get_icmp_seq() != actual.get_icmp_seq():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_icmp_seq()) + " != " +
                                                      str(actual.get_icmp_seq()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_icmp_seq()) + " == " +
                                                 str(actual.get_icmp_seq()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with IcmpPacketHeader")
        return results


class IcmpPacketConstants:
    def __init__(self):
        pass

    ICMP_TYPE = "ICMP_TYPE"
    ICMP_TYPE_ECHO_REPLY = "0"
    ICMP_TYPE_DESTINATION_UNREACHABLE = "3"
    ICMP_TYPE_SOURCE_QUENCH = "4"
    ICMP_TYPE_REDIRECT_MESSAGE = "5"
    ICMP_TYPE_ECHO_REQUEST = "8"
    ICMP_TYPE_ROUTER_ADVERTISEMENT = "9"
    ICMP_TYPE_ROUTER__SOLICITATION = "10"
    ICMP_TYPE_TIME_EXCEEDED = "11"
    ICMP_TYPE_PARAMETER_PROBLEM_BAD_IP_HEADER = "12"
    ICMP_TYPE_TIMESTAMP = "13"
    ICMP_TYPE_TIMESTAMP_REPLY = "14"
    ICMP_TYPE_INFORMATION_REQUEST = "15"
    ICMP_TYPE_INFORMATION_REPLY = "16"
    ICMP_TYPE_ADDRESS_MASK_REQUEST = "17"
    ICMP_TYPE_ADDRESS_MASK_REPLY = "18"
    ICMP_TYPE_TRACEROUTE = "30"

    ICMP_CODE = "ICMP_CODE"
    ICMP_CODE_DESTINATION_NETWORK_UNREACHABLE = "0"
    ICMP_CODE_DESTINATION_HOST_UNREACHABLE = "1"
    ICMP_CODE_DESTINATION_PROTOCOL_UNREACHABLE = "2"
    ICMP_CODE_DESTINATION_PORT_UNREACHABLE = "3"
    ICMP_CODE_FRAGMENTATION_REQUIRED_AND_DF_FLAG_SET = "4"
    ICMP_CODE_SOURCE_ROUTE_FAILED = "5"
    ICMP_CODE_DESTINATION_NETWORK_UNKNOWN = "6"
    ICMP_CODE_DESTINATION_HOST_UNKNOWN = "7"
    ICMP_CODE_SOURCE_HOST_ISOLATED = "8"
    ICMP_CODE_NETWORK_ADMINISTRATIVELY_PROHIBITED = "9"
    ICMP_CODE_HOST_ADMINISTRATIVELY_PROHIBITED = "10"
    ICMP_CODE_NETWORK_UNREACHABLE_FOR_TOS = "11"
    ICMP_CODE_HOST_UNREACHABLE_FOR_TOS = "12"
    ICMP_CODE_COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = "13"
    ICMP_CODE_HOST_PRECEDENCE_VIOLATION = "14"
    ICMP_CODE_PRECEDENCE_CUTOFF_IN_EFFECT = "15"

    ICMP_CHECKSUM = "ICMP_CHECKSUM"
    ICMP_ID = "ICMP_ID"
    ICMP_SEQ = "ICMP_SEQ"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
