from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.igmp_pb2 import igmp
from ExtremeAutomation.Library.Net.Packet.Checksum import Checksum
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer4PacketHeader import Layer4PacketHeader
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader


class IgmpPacketHeader(Layer4PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    IGMP Packet Header
        # type = 8bits
        # maxresptime = 8bits
        # checksum = 16bits
        # groupaddress = 32bits
    """

    def __init__(self):
        super(IgmpPacketHeader, self).__init__()
        self.add_igmp_header()
        self.HEADER_SIZE_IGMP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Igmp type methods
    #  type is a 8 bit INTEGER example: 1
    def set_igmp_type(self, pkt_type, ignore_check=False):
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_TYPE, pkt_type)

    def get_igmp_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_TYPE), PacketConstants.INTEGER)

    def get_igmp_type_hltapi_cmd(self, dummy_dict):
        pkt_type = self.get_igmp_type()
        if isinstance(pkt_type, int):
            pkt_type = str(pkt_type)
        if pkt_type and 'Not Set' not in pkt_type:
            if pkt_type == IgmpPacketConstants.IGMP_TYPE_MEMBERSHIP_QUERY or \
                    pkt_type == IgmpPacketConstants.IGMP_TYPE_IGMP_MEMBERSHIP_QUERY:
                dummy_dict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_MEMBERSHIP_QUERY
            elif pkt_type == IgmpPacketConstants.IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV1:
                dummy_dict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_MEMBERSHIP_REPORT
            elif pkt_type == IgmpPacketConstants.IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV2:
                dummy_dict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_MEMBERSHIP_REPORT
                dummy_dict[TrafficConfigConstants.IGMP_VERSION_CMD] = TrafficConfigConstants.IGMP_VERSION_2
            elif pkt_type == IgmpPacketConstants.IGMP_TYPE_LEAVE_GROUP_V2:
                dummy_dict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_LEAVE_GROUP
                dummy_dict[TrafficConfigConstants.IGMP_VERSION_CMD] = TrafficConfigConstants.IGMP_VERSION_2
            elif pkt_type == IgmpPacketConstants.IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV3:
                dummy_dict[TrafficConfigConstants.IGMP_TYPE_CMD] = TrafficConfigConstants.IGMP_TYPE_MEMBERSHIP_REPORT
                dummy_dict[TrafficConfigConstants.IGMP_VERSION_CMD] = TrafficConfigConstants.IGMP_VERSION_3
    # end Igmp type methods

    # start Igmp maxresptime methods
    #  maxresptime is a 8 bit INTEGER example: 1
    def set_igmp_maxresptime(self, maxresptime, ignore_check=False):
        maxresptime = self.normalize_value(maxresptime, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_MAXRESPTIME,
                                  maxresptime)

    def get_igmp_maxresptime(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_MAXRESPTIME), PacketConstants.INTEGER)

    def get_igmp_maxresptime_hltapi_cmd(self, dummy_dict):
        maxresptime = self.get_igmp_maxresptime()
        if isinstance(maxresptime, int):
            maxresptime = str(maxresptime)
        if maxresptime and 'Not Set' not in maxresptime:
            dummy_dict[TrafficConfigConstants.IGMP_MAX_RESPONSE_TIME_CMD] = maxresptime
    # end Igmp maxresptime methods

    # start Igmp checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_igmp_checksum(self, checksum, ignore_check=False):
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_CHECKSUM, checksum)

    def get_igmp_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_CHECKSUM), PacketConstants.INTEGER)

    def get_igmp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_igmp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Igmp checksum methods

    # start Igmp groupaddress methods
    #  groupaddress is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_igmp_groupaddress(self, groupaddress, ignore_check=False):
        groupaddress = self.normalize_value(groupaddress, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_GROUPADDRESS,
                                  groupaddress)

    def get_igmp_groupaddress(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_IGMP, IgmpPacketConstants.IGMP_GROUPADDRESS), PacketConstants.IPV4_ADDRESS)

    def get_igmp_groupaddress_ip(self):
        return Ipv4Address(self.get_igmp_groupaddress())

    def get_igmp_groupaddress_int(self):
        return Ipv4Address.to_long(self.get_igmp_groupaddress())

    def get_igmp_groupaddress_hex(self):
        if self.is_field_set(self.get_igmp_groupaddress()):
            ip = self.get_igmp_groupaddress_ip()
            return "0x" + ip.to_formated_string(16, "")

    def get_igmp_groupaddress_hltapi_cmd(self, dummy_dict):
        groupaddress = self.get_igmp_groupaddress()
        if groupaddress and 'Not Set' not in groupaddress:
            dummy_dict[TrafficConfigConstants.IGMP_GROUP_ADDR_CMD] = groupaddress
    # end Igmp groupaddress methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("type", self.format_int(self.get_igmp_type(), 1))
        table.add_row_value("maxresptime", self.format_int(self.get_igmp_maxresptime(), 1))
        table.add_row_value("checksum", self.format_int(self.get_igmp_checksum(), 2))
        table.add_row_value("groupaddress", self.get_igmp_groupaddress())
        return "\n\nIGMP HEADER" + table.to_table_string()

    def add_igmp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_IGMP)

    def build(self):
        self.add_igmp_header()
        self.set_ip_protocol(0x02, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        dummy_dict[TrafficConfigConstants.IGMP_VERSION_CMD] = TrafficConfigConstants.IGMP_VERSION_1
        self.get_igmp_type_hltapi_cmd(dummy_dict)
        self.get_igmp_maxresptime_hltapi_cmd(dummy_dict)
        # self.get_igmp_checksum_hltapi_cmd(dummy_dict)
        self.get_igmp_groupaddress_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_IGMP  # constant value
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_igmp(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_igmp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_igmp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_igmp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kIgmpFieldNumber
        # update this from the ostinato docs.
        igmpField = p.Extensions[igmp]
        if self.is_field_set(self.get_igmp_type()):
            igmpField.type = int(self.get_igmp_type())
        if self.is_field_set(self.get_igmp_maxresptime()):
            igmpField.max_response_time = int(self.get_igmp_maxresptime())
        if self.is_field_set(self.get_igmp_checksum()):
            igmpField.is_override_checksum = True
            igmpField.checksum = int(self.get_igmp_checksum())
        # needs to be updated when ostinato gets back to me.
        if self.is_field_set(self.get_igmp_groupaddress()):
            igmpField.group_address.v4 = self.get_igmp_groupaddress_int()  # 0x01020203

    def config_jets_stream_igmp(self, jets_dev, port_string, stream_id, **kwargs):
        if not isinstance(self, IpV6PacketHeader) and not self.is_field_set(self.get_ip_protocol()):
            jets_dev.pdl_add_packet_header(JetsDeviceConstants.IP_HDR, {"ip_protocol": 1})
        elif isinstance(self, IpV6PacketHeader) and not self.is_field_set(self.get_ipv6_next_header()):
            jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPV6_HDR, {"next_header": 1})
        pkt_bytes = "0x" + IgmpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_igmp_api_commands(self, port_string, streamid):
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

    def get_spirent_igmp_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        pkt_type = self.get_bits_from_string(8, payload)
        self.set_igmp_type("0x" + pkt_type)
        payload = self.remove_bits_from_string(8, payload)
        maxresptime = self.get_bits_from_string(8, payload)
        self.set_igmp_maxresptime("0x" + maxresptime)
        payload = self.remove_bits_from_string(8, payload)
        checksum = self.get_bits_from_string(16, payload)
        self.set_igmp_checksum("0x" + checksum)
        payload = self.remove_bits_from_string(16, payload)
        groupaddress = self.get_bits_from_string(32, payload)
        self.set_igmp_groupaddress("0x" + groupaddress)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_igmp_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_igmp_maxresptime(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_igmp_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_igmp_groupaddress(), PacketConstants.IPV4_ADDRESS, 32)
        return ret_string

    def calculate_igmp_checksum(self, header_offset):
        self.set_ip_checksum(0)
        header_sum = Checksum.calculate_ip_checksum(self.get_bytes(), header_offset, self.HEADER_SIZE_IPV4)
        header_sum = Checksum.calculate_complement(header_sum)
        self.set_ip_checksum(header_sum)
        pass

    @staticmethod
    def compare_igmp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, IgmpPacketHeader)
            assert isinstance(actual, IgmpPacketHeader)
            if expected.is_field_set(expected.get_igmp_type()) and IgmpPacketConstants.IGMP_TYPE not in ignore_list:
                name = "IGMP type : "
                if expected.get_igmp_type() != actual.get_igmp_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_igmp_type()) + " != " +
                                                      str(actual.get_igmp_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_igmp_type()) + " == " +
                                                 str(actual.get_igmp_type()) + " Pass")

            if expected.is_field_set(expected.get_igmp_maxresptime()) and \
                    IgmpPacketConstants.IGMP_MAXRESPTIME not in ignore_list:
                name = "IGMP maxresptime : "
                if expected.get_igmp_maxresptime() != actual.get_igmp_maxresptime():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_igmp_maxresptime()) + " != " +
                                                      str(actual.get_igmp_maxresptime()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_igmp_maxresptime()) + " == " +
                                                 str(actual.get_igmp_maxresptime()) + " Pass")

            if expected.is_field_set(expected.get_igmp_checksum()) and \
                    IgmpPacketConstants.IGMP_CHECKSUM not in ignore_list:
                name = "IGMP checksum : "
                if expected.get_igmp_checksum() != actual.get_igmp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_igmp_checksum()) + " != " +
                                                      str(actual.get_igmp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_igmp_checksum()) + " == " +
                                                 str(actual.get_igmp_checksum()) + " Pass")

            if expected.is_field_set(expected.get_igmp_groupaddress()) and \
                    IgmpPacketConstants.IGMP_GROUPADDRESS not in ignore_list:
                name = "IGMP groupaddress : "
                if expected.get_igmp_groupaddress() != actual.get_igmp_groupaddress():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_igmp_groupaddress()) + " != " +
                                                      str(actual.get_igmp_groupaddress()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_igmp_groupaddress()) + " == " +
                                                 str(actual.get_igmp_groupaddress()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with IgmpPacketHeader")
        return results


class IgmpPacketConstants:
    def __init__(self):
        pass

    IGMP_TYPE = "IGMP_TYPE"
    IGMP_TYPE_MEMBERSHIP_QUERY = "16"               # 0x10
    IGMP_TYPE_IGMP_MEMBERSHIP_QUERY = "17"          # 0x11
    IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV1 = "18"       # 0x12
    IGMP_TYPE_DVMRP = "19"                          # 0x13
    IGMP_TYPE_PIM_v1 = "20"                         # 0x14
    IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV2 = "22"       # 0x16
    IGMP_TYPE_LEAVE_GROUP_V2 = "23"                 # 0x17
    IGMP_TYPE_MULTICAST_TRACEROUTE_RESPONSE = "30"  # 0x1e
    IGMP_TYPE_MULTICAST_TRACEROUTE = "31"           # 0x1f
    IGMP_TYPE_MEMBERSHIP_REPORT_IGMPV3 = "34"       # 0x22

    IGMP_MAXRESPTIME = "IGMP_MAXRESPTIME"
    IGMP_CHECKSUM = "IGMP_CHECKSUM"
    IGMP_GROUPADDRESS = "IGMP_GROUPADDRESS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
