import abc
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.Ipv6Address import Ipv6Address
from ExtremeAutomation.Library.Net.Packet.EthernetPacketHeader import EthernetPacketHeader
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader, \
    LldpPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader, \
    MstpPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader, \
    RadiusPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import UdpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject, PacketConstants
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader, \
    VlanStackPacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacketHeader import Ieee802LlcPacketHeader
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
import binascii


class AbstractPacket(PacketObject, metaclass=abc.ABCMeta):
    packet_name = None

    def __init__(self):
        PacketObject.__init__(self)
        self.data_only = False
        self.length = False
        self.user_set_length = False
        self.status = "Good Packet"
        self.payload = "00 00 00 00"
        self.timestamp = "00"
        self.pkt_bytes = ""
        self.raw_captured_bytes = ""
        self.__packet_field_default_ignore_comparison = []
        self.__packet_field_default_ignore_comparison_enabled = True
        self.cloned_packet = False
        self.header_in_bytes_only = False  # if only byte support is available after a header

    @abc.abstractmethod
    def get_hltapi_commands(self):
        pass

    def set_name(self, name):
        self.packet_name = name

    def get_name(self):
        return self.packet_name

    def get_all_hltapi_commands(self, traffic_generating_device, stream_id):
        packet = self
        packet_dict = dict()
        packet_dict[TrafficConfigConstants.STREAM_ID_CMD] = stream_id
        packet_dict.update(packet.get_hltapi_commands())
        return packet_dict

    def set_length(self, length):
        self.length = length

    def get_length(self):
        if isinstance(self.length, bool):
            return self.length
        return NumberUtils.to_integer_value(self.length)

    def get_length_int(self):
        if self.is_field_set(self.get_length()):
            return int(self.get_length())

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_timestamp(self, times):
        self.timestamp = times

    def get_timestamp(self):
        return self.timestamp

    def set_data_only(self, data_only):
        self.data_only = data_only

    def is_data_only(self):
        return self.set_data_only

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        payload = payload.replace(" ", "").upper()
        self.payload = payload
        self.set_length(len(payload) // 2)

    def get_header_bytes(self, break_up_header):
        return ""

    def set_captured_bytes(self, cap_bytes):
        self.raw_captured_bytes = cap_bytes

    def get_captured_bytes(self):
        return self.raw_captured_bytes

    @staticmethod
    def get_bytes_from_string(get_bytes, payload):
        return AbstractPacket.get_bits_from_string(get_bytes * 8, payload)

    @staticmethod
    def get_bits_from_string(bits, payload):
        if bits == 4:
            return payload[0]
        nibble = (bits // 4)
        return payload[0:nibble]
        # if bits == 4:
        # elif bits == 8:
        #     return payload[0:1]
        # elif bits == 16:
        #     return payload[0:3]
        # elif bits == 32:
        #     return payload[0:7]

    @staticmethod
    def get_bits_from_string_with_positions(value, start_pos_zero_based, bit_length):
        val = NumberUtils.to_integer_value(value)
        mask = (2 ** bit_length) - 1
        shift_value = (start_pos_zero_based - bit_length) + 1
        mask <<= shift_value
        return (val & mask) >> shift_value

    @staticmethod
    def shift_bits_from_string_with_positions(value, start_pos_zero_based, bit_length, bits_to_set):
        val = NumberUtils.to_integer_value(value)
        if isinstance(bits_to_set, str) and "Not Set" in bits_to_set:
            bits_to_set = 0
        else:
            bits_to_set = NumberUtils.to_integer_value(bits_to_set)
        shift_value = (start_pos_zero_based - bit_length) + 1
        # start clear the bits out
        mask = (2 ** bit_length) - 1
        mask <<= shift_value
        val &= ~mask
        # end clear the bits out
        bits_to_set <<= shift_value
        return val | bits_to_set

    @staticmethod
    def remove_bytes_from_string(rm_bytes, payload):
        return AbstractPacket.remove_bits_from_string(rm_bytes * 8, payload)

    @staticmethod
    def remove_bits_from_string(bits, payload):
        nibble = (bits // 4)
        return payload[nibble:]
        # if bits == 4:
        #     return payload[1:]
        # elif bits == 8:
        #     return payload[2:]
        # elif bits == 16:
        #     return payload[4:]
        # elif bits == 32:
        #     return payload[8:]

    def is_tagged(self):
        return isinstance(self, TaggedPacketHeader)

    def is_ipv4(self):
        return isinstance(self, IpV4PacketHeader)

    def is_ipv6(self):
        return isinstance(self, IpV6PacketHeader)

    def is_tcp(self):
        return isinstance(self, TcpPacketHeader)

    def is_udp(self):
        return isinstance(self, UdpPacketHeader)

    @staticmethod
    def normalize_value(ip, format_type):
        return StringUtils.normalize_value(ip, format_type)

    @staticmethod
    def is_field_set(val):
        if isinstance(val, str) and "Not Set" in val:
            return False
        if val == 'False':
            return False
        else:
            return True

    def do_i_check_this_field(self, val, constant, ignore_list, include_list):
        if self.is_packet_field_default_ignore_comparison_enabled() and \
                self.is_packet_field_default_ignore_comparison(constant):
            return False
        if not ignore_list:
            ignore_list = []
        if AbstractPacket.is_field_set(val) and constant not in ignore_list:
            return (include_list and constant in include_list) or not include_list
        else:
            return False

    def on_ignore_list(self, ignore_list, l1, l2):
        pass

    def format_int(self, val, size):
        if isinstance(val, str) and "Not Set" in val:
            return val
        if val == 'False':
            return 'Field Not Set'
        if not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        elif not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        return str(val) + " (0x" + (hex(val)[2:].replace("L", "").zfill(2 * size)).upper() + ")"

    def format_hex_to_ascii(self, val, size):
        if isinstance(val, str) and "Not Set" in val:
            return val
        if val == 'False':
            return 'Field Not Set'
        if not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        elif not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        hex_string = (hex(val)[2:].replace("L", "").zfill(2 * size)).upper()
        hex_string = binascii.unhexlify(hex_string.replace(" ", ""))
        return str(hex_string.decode("utf-8")).strip()

    def to_int(self, val):
        if isinstance(val, str) and "Not Set" in val:
            return 0
        if not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        elif not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        return val

    def format_hex(self, val, size):
        if isinstance(val, str) and "Not Set" in val:
            return val
        if not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        elif not isinstance(val, int):
            val = int(self.normalize_value(val, PacketConstants.INTEGER))
        return "0x" + (hex(val)[2:].replace("L", "").zfill(2 * size)).upper() + " (" + str(val) + ")"

    @staticmethod
    def format_byte_string(val, format_type, size_in_bits):
        if isinstance(val, str) and "Not Set" in val:
            return "".zfill(2 * size_in_bits // 8)
        val = StringUtils.normalize_value(val, format_type)
        if format_type == PacketConstants.ENET_ADDRESS:
            return EnetAddress(val).get_bytes_string().zfill(2 * size_in_bits // 8)
        elif format_type == PacketConstants.IPV4_ADDRESS:
            return Ipv4Address(val).get_bytes_string().zfill(2 * size_in_bits // 8)
        elif format_type == PacketConstants.IPV6_ADDRESS:
            return Ipv6Address(val).get_bytes_string().zfill(2 * size_in_bits // 8)
        elif format_type == PacketConstants.HEX_STRING or format_type == PacketConstants.ASCII_STRING:
            val = (val.replace(" ", ""))[::-1]  # reverse
            val = val.zfill((2 * size_in_bits // 8))
            return val[::-1]  # reverse back
        return (hex(val)[2:].replace("L", "").zfill(2 * size_in_bits // 8)).upper()

    def set_packet_field_default_ignore_comparison_enabled(self, value):
        self.__packet_field_default_ignore_comparison_enabled = value

    def is_packet_field_default_ignore_comparison_enabled(self):
        return self.__packet_field_default_ignore_comparison_enabled

    def set_packet_field_default_ignore_comparison(self, key, val=True):
        if val and key not in self.__packet_field_default_ignore_comparison:
            self.__packet_field_default_ignore_comparison.append(key)
        elif not val and key in self.__packet_field_default_ignore_comparison:
            self.__packet_field_default_ignore_comparison.remove(key)

    def is_packet_field_default_ignore_comparison(self, key):
        return key in self.__packet_field_default_ignore_comparison

    def remove_packet_field_default_ignore_comparison(self, key):
        if key in self.__packet_field_default_ignore_comparison:
            self.__packet_field_default_ignore_comparison.remove(key)

    def compare_packet_fields(self, actual, check_defaults=False, ignore_list=None, include_list=None,
                              dynamic_entries=None, print_flag=PacketConstants.PRINT_FLAG_EVERYTHING):
        expected = self
        print_all = print_flag == PacketConstants.PRINT_FLAG_EVERYTHING
        print_falures = (print_flag == PacketConstants.PRINT_FLAG_ERRORS or
                         print_flag == PacketConstants.PRINT_FLAG_EVERYTHING)

        self.set_packet_field_default_ignore_comparison_enabled(not check_defaults)

        vlan_stack_dynamic_entry_checker = None
        lldp_dynamic_entry_checker = None
        msti_dynamic_entry_checker = None
        radius_dynamic_entry_checker = None
        if dynamic_entries:
            if not isinstance(dynamic_entries, list):
                dynamic_entries = [dynamic_entries]
            for entr in dynamic_entries:
                if isinstance(entr, VlanStackPacketHeaderDynamicFieldLogic):
                    vlan_stack_dynamic_entry_checker = entr
                if isinstance(entr, LldpPacketHeaderDynamicFieldLogic):
                    lldp_dynamic_entry_checker = entr
                if isinstance(entr, MstpPacketHeaderDynamicFieldLogic):
                    msti_dynamic_entry_checker = entr
                if isinstance(entr, RadiusPacketHeaderDynamicFieldLogic):
                    radius_dynamic_entry_checker = entr

        # L1/L2
        if ignore_list is None:
            ignore_list = []
        if print_all:
            self.logger.log_debug("Expected: " + expected.get_name())
            self.logger.log_debug("Actual: " + actual.get_name())
        result = True
        if isinstance(expected, EthernetPacketHeader):
            result &= EthernetPacketHeader.compare_ethernet_packet_header(expected, actual, ignore_list, include_list,
                                                                          print_all, print_falures)
        if isinstance(expected, VlanStackPacketHeader):
            result &= VlanStackPacketHeader.compare_vlanstack_packet_header(expected, actual, ignore_list, include_list,
                                                                            vlan_stack_dynamic_entry_checker, print_all,
                                                                            print_falures)
        if isinstance(expected, TaggedPacketHeader):
            result &= TaggedPacketHeader.compare_tagged_packet_header(expected, actual, ignore_list, include_list,
                                                                      print_all, print_falures)
        if isinstance(expected, Ethernet2PacketHeader):
            result &= Ethernet2PacketHeader.compare_ethernet2_packet_header(expected, actual, ignore_list, include_list,
                                                                            print_all, print_falures)
        if isinstance(expected, Ieee802LlcPacketHeader):
            result &= Ieee802LlcPacketHeader.compare_llc_packet_header(expected, actual, ignore_list, include_list,
                                                                       print_all, print_falures)
        if isinstance(expected, SnapPacketHeader):
            result &= SnapPacketHeader.compare_snap_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        # L3
        if isinstance(expected, ArpPacketHeader):
            result &= ArpPacketHeader.compare_arp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, IpV4PacketHeader):
            result &= IpV4PacketHeader.compare_ipv4_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, IpV6PacketHeader):
            result &= IpV6PacketHeader.compare_ipv6_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, LldpPacketHeader):
            result &= LldpPacketHeader.compare_lldp_packet_header(expected, actual, ignore_list, include_list,
                                                                  lldp_dynamic_entry_checker, print_all, print_falures)
        if isinstance(expected, IpxPacketHeader):
            result &= IpxPacketHeader.compare_ipx_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)

        # L4
        if isinstance(expected, TcpPacketHeader):
            result &= TcpPacketHeader.compare_tcp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, UdpPacketHeader):
            result &= UdpPacketHeader.compare_udp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, IcmpPacketHeader):
            result &= IcmpPacketHeader.compare_icmp_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, BpduPacketHeader):
            result &= BpduPacketHeader.compare_bpdu_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_results=print_all,
                                                                  print_failures=print_falures)
        if isinstance(expected, RadiusPacketHeader):
            result &= RadiusPacketHeader.compare_radius_packet_header(expected, actual, ignore_list, include_list,
                                                                      radius_dynamic_entry_checker,
                                                                      print_results=print_all,
                                                                      print_failures=print_falures)
        if isinstance(expected, MstpPacketHeader):
            result &= MstpPacketHeader.compare_mstp_packet_header(expected, actual, ignore_list, include_list,
                                                                  msti_dynamic_entry_checker, print_all, print_falures)
        if isinstance(expected, InnerPacketHeader):
            result &= expected.compare_inner_packet_header(expected, actual, ignore_list, include_list,
                                                           msti_dynamic_entry_checker, print_all, print_falures)

        # don't do these because they all need a packet inside of them. implement InnerPacketHeader
        # if isinstance(expected, GrePacketHeader):
        #     result &= GrePacketHeader.compare_gre_packet_header(expected, actual, ignore_list, include_list,
        #                                                         msti_dynamic_entry_checker, print_all, print_falures)
        # if isinstance(expected, IpEncapsulatedPacketHeader):
        #     result &= IpEncapsulatedPacketHeader.compare_encapsulated_packet_header(expected, actual, ignore_list,
        #                                                                             include_list,
        #                                                                             msti_dynamic_entry_checker,
        #                                                                             print_all, print_falures)
        # if isinstance(expected, VxlanPacketHeader):
        #     result &= VxlanPacketHeader.compare_vxlan_packet_header(expected, actual, ignore_list, include_list,
        #                                                             msti_dynamic_entry_checker,
        #                                                             print_all, print_falures)

        if print_falures and not result:
            PacketObject.logger.log_info("packet 1:" + expected.get_name())
            PacketObject.logger.log_info("packet 2:" + actual.get_name())
        return result

    def match_packet_fields(self, actual):
        check_defaults = False
        ignore_list = None
        include_list = None
        dynamic_entries = None
        print_flag = PacketConstants.PRINT_FLAG_EVERYTHING
        expected = self
        print_all = print_flag == PacketConstants.PRINT_FLAG_EVERYTHING
        print_falures = (print_flag == PacketConstants.PRINT_FLAG_ERRORS or
                         print_flag == PacketConstants.PRINT_FLAG_EVERYTHING)

        self.set_packet_field_default_ignore_comparison_enabled(not check_defaults)

        vlan_stack_dynamic_entry_checker = None
        lldp_dynamic_entry_checker = None
        msti_dynamic_entry_checker = None
        radius_dynamic_entry_checker = None
        if dynamic_entries:
            if not isinstance(dynamic_entries, list):
                dynamic_entries = [dynamic_entries]
            for entr in dynamic_entries:
                if isinstance(entr, VlanStackPacketHeaderDynamicFieldLogic):
                    vlan_stack_dynamic_entry_checker = entr
                if isinstance(entr, LldpPacketHeaderDynamicFieldLogic):
                    lldp_dynamic_entry_checker = entr
                if isinstance(entr, MstpPacketHeaderDynamicFieldLogic):
                    msti_dynamic_entry_checker = entr
                if isinstance(entr, RadiusPacketHeaderDynamicFieldLogic):
                    radius_dynamic_entry_checker = entr

        # L1/L2
        if ignore_list is None:
            ignore_list = []
        if print_all:
            self.logger.log_debug("Expected: " + expected.get_name())
            self.logger.log_debug("Actual: " + actual.get_name())
        compared_one_header = False
        result = True
        if isinstance(expected, EthernetPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L1_ETHERNET):
            compared_one_header = True
            result &= EthernetPacketHeader.compare_ethernet_packet_header(expected, actual, ignore_list, include_list,
                                                                          print_all, print_falures)
        if isinstance(expected, VlanStackPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK):
            compared_one_header = True
            result &= VlanStackPacketHeader.compare_vlanstack_packet_header(expected, actual, ignore_list, include_list,
                                                                            vlan_stack_dynamic_entry_checker, print_all,
                                                                            print_falures)
        if isinstance(expected, TaggedPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED):
            compared_one_header = True
            result &= TaggedPacketHeader.compare_tagged_packet_header(expected, actual, ignore_list, include_list,
                                                                      print_all, print_falures)
        if isinstance(expected, Ethernet2PacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L2_ETHERNET_II_TYPE):
            compared_one_header = True
            result &= Ethernet2PacketHeader.compare_ethernet2_packet_header(expected, actual, ignore_list, include_list,
                                                                            print_all, print_falures)
        if isinstance(expected, Ieee802LlcPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L2_LLC):
            compared_one_header = True
            result &= Ieee802LlcPacketHeader.compare_llc_packet_header(expected, actual, ignore_list, include_list,
                                                                       print_all, print_falures)
        if isinstance(expected, SnapPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L2_SNAP):
            compared_one_header = True
            result &= SnapPacketHeader.compare_snap_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        # L3
        if isinstance(expected, ArpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_ARP):
            compared_one_header = True
            result &= ArpPacketHeader.compare_arp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, IpV4PacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_IPV4):
            compared_one_header = True
            result &= IpV4PacketHeader.compare_ipv4_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, IpV6PacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_IPV6):
            compared_one_header = True
            result &= IpV6PacketHeader.compare_ipv6_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, LldpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_LLDP):
            compared_one_header = True
            result &= LldpPacketHeader.compare_lldp_packet_header(expected, actual, ignore_list, include_list,
                                                                  lldp_dynamic_entry_checker, print_all, print_falures)
        if isinstance(expected, IpxPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_IPX):
            compared_one_header = True
            result &= IpxPacketHeader.compare_ipx_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)

        # L4
        if isinstance(expected, TcpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L4_TCP):
            compared_one_header = True
            result &= TcpPacketHeader.compare_tcp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, UdpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L4_UDP):
            compared_one_header = True
            result &= UdpPacketHeader.compare_udp_packet_header(expected, actual, ignore_list, include_list,
                                                                print_all, print_falures)
        if isinstance(expected, IcmpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L4_ICMP):
            compared_one_header = True
            result &= IcmpPacketHeader.compare_icmp_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_all, print_falures)
        if isinstance(expected, BpduPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_BPDU):
            compared_one_header = True
            result &= BpduPacketHeader.compare_bpdu_packet_header(expected, actual, ignore_list, include_list,
                                                                  print_results=print_all,
                                                                  print_failures=print_falures)
        if isinstance(expected, RadiusPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_RADIUS):
            compared_one_header = True
            result &= RadiusPacketHeader.compare_radius_packet_header(expected, actual, ignore_list, include_list,
                                                                      radius_dynamic_entry_checker,
                                                                      print_results=print_all,
                                                                      print_failures=print_falures)
        if isinstance(expected, MstpPacketHeader) and \
                self.are_any_fields_set(PacketConstants.PACKET_HEADER_L3_MSTP):
            compared_one_header = True
            result &= MstpPacketHeader.compare_mstp_packet_header(expected, actual, ignore_list, include_list,
                                                                  msti_dynamic_entry_checker, print_all, print_falures)
        if isinstance(expected, InnerPacketHeader):
            compared_one_header = True
            result &= expected.compare_inner_packet_header(expected, actual, ignore_list, include_list,
                                                           msti_dynamic_entry_checker, print_all, print_falures)

        # don't do these because they all need a packet inside of them. implement InnerPacketHeader
        # if isinstance(expected, GrePacketHeader):
        #     result &= GrePacketHeader.compare_gre_packet_header(expected, actual, ignore_list, include_list,
        #                                                         msti_dynamic_entry_checker, print_all, print_falures)
        # if isinstance(expected, IpEncapsulatedPacketHeader):
        #     result &= IpEncapsulatedPacketHeader.compare_encapsulated_packet_header(expected, actual, ignore_list,
        #                                                                             include_list,
        #                                                                             msti_dynamic_entry_checker,
        #                                                                             print_all, print_falures)
        # if isinstance(expected, VxlanPacketHeader):
        #     result &= VxlanPacketHeader.compare_vxlan_packet_header(expected, actual, ignore_list, include_list,
        #                                                             msti_dynamic_entry_checker,
        #                                                             print_all, print_falures)
        result &= compared_one_header
        if print_falures and not result:
            PacketObject.logger.log_info("packet 1:" + expected.get_name())
            PacketObject.logger.log_info("packet 2:" + actual.get_name())
        return result

    def are_any_fields_set(self, header):
        comps = self.get_all_packet_fields()
        if header in comps:
            comps = comps[header]
            for comp in comps:
                if self.is_packet_field_default_ignore_comparison(comp):
                    pass
                else:
                    return True
        return False
