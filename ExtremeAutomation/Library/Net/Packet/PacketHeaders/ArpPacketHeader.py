from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.arp_pb2 import arp
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject


class ArpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ARP Packet Header
        # hardware = 16bits
        # proto = 16bits
        # id = 8bits  This might be hardware add length
        # seq = 8bits  This might be protocol add length
        # operation = 16bits
        # sender hardware address = 48bits
        # source protocol address = 32bits
        # target hardware address = 48bits
        # target protocol address = 32bits
    """

    def __init__(self):
        self.add_arp_header()
        self.HEADER_SIZE_ARP = (16 + 16 + 8 + 8 + 16 + 48 + 32 + 48 + 32) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Arp hardware methods
    #  hardware is a 16 bit INTEGER example: 1
    def set_arp_hardware(self, hardware, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_HARDWARE, ignore_check)
        hardware = self.normalize_value(hardware, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_HARDWARE, hardware)

    def get_arp_hardware(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_HARDWARE),
            PacketConstants.INTEGER)

    def get_arp_hardware_hltapi_cmd(self, dummy_dict):
        hardware = self.get_arp_hardware()
        if isinstance(hardware, int):
            hardware = str(hardware)
        if hardware and 'Not Set' not in hardware:
            dummy_dict[TrafficConfigConstants.ARP_HW_TYPE_CMD] = hardware
    # end Arp hardware methods

    # start Arp proto methods
    #  proto is a 16 bit INTEGER example: 1
    def set_arp_proto(self, proto, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_PROTO, ignore_check)
        proto = self.normalize_value(proto, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_PROTO, proto)

    def get_arp_proto(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_PROTO),
            PacketConstants.INTEGER)

    def get_arp_proto_hltapi_cmd(self, dummy_dict):
        proto = self.get_arp_proto()
        if isinstance(proto, int):
            proto = str(proto)
        if proto and 'Not Set' not in proto:
            dummy_dict[TrafficConfigConstants.ARP_PROTOCOL_TYPE_CMD] = proto
    # end Arp proto methods

    # start Arp id methods
    #  id is a 8 bit INTEGER example: 1
    def set_arp_id(self, pkt_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_SEQ, ignore_check)
        pkt_id = self.normalize_value(pkt_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_ID, pkt_id)

    def get_arp_id(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_SEQ),
            PacketConstants.INTEGER)

    def get_arp_id_hltapi_cmd(self, dummy_dict):
        pkt_id = self.get_arp_id()
        if isinstance(pkt_id, int):
            pkt_id = str(pkt_id)
        if pkt_id and 'Not Set' not in pkt_id:
            dummy_dict[TrafficConfigConstants.ARP_HW_ADDRESS_LENGTH_CMD] = pkt_id
    # end Arp id methods

    # start Arp seq methods
    #  seq is a 8 bit INTEGER example: 1
    def set_arp_seq(self, seq, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_SEQ, ignore_check)
        seq = self.normalize_value(seq, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_SEQ, seq)

    def get_arp_seq(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_SEQ),
            PacketConstants.INTEGER)

    def get_arp_seq_hltapi_cmd(self, dummy_dict):
        seq = self.get_arp_seq()
        if isinstance(seq, int):
            seq = str(seq)
        if seq and 'Not Set' not in seq:
            dummy_dict[TrafficConfigConstants.ARP_PROTOCOL_ADDR_LENGTH_CMD] = seq
    # end Arp seq methods

    # start Arp operation methods
    #  operation is a 16 bit INTEGER example: 1
    def set_arp_operation(self, operation, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_OPERATION, ignore_check)
        operation = self.normalize_value(operation, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_OPERATION, operation)

    def get_arp_operation(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_OPERATION),
            PacketConstants.INTEGER)

    def get_arp_operation_hltapi_cmd(self, dummy_dict):
        operation = self.get_arp_operation()
        if isinstance(operation, int):
            operation = str(operation)
        if operation and 'Not Set' not in operation:

            if operation in ArpPacketConstants.ARP_VALUES:
                dummy_dict[TrafficConfigConstants.ARP_OPERATION_CMD] = ArpPacketConstants.ARP_VALUES[operation]
            else:
                dummy_dict[TrafficConfigConstants.ARP_OPERATION_CMD] = operation
    # end Arp operation methods

    # start Arp sender hardware address methods
    #  sender_hardware_address is a 48 bit ENET_ADDRESS example: 00:33:44:55:66:44
    def set_arp_sender_hardware_address(self, sender_hardware_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS, ignore_check)
        sender_hardware_address = self.normalize_value(sender_hardware_address, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS,
                                  sender_hardware_address)

    def get_arp_sender_hardware_address(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                                              ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS),
                                    PacketConstants.ENET_ADDRESS)

    def get_arp_sender_hardware_address_hltapi_cmd(self, dummy_dict):
        sender_hardware_address = self.get_arp_sender_hardware_address()
        if sender_hardware_address and 'Not Set' not in sender_hardware_address:
            dummy_dict[TrafficConfigConstants.ARP_SRC_HW_ADDR_CMD] = sender_hardware_address

    def set_arp_sender_hardware_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_MODE, ip)

    def get_arp_sender_hardware_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_MODE)

    def set_arp_sender_hardware_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_COUNT, ip)

    def get_arp_sender_hardware_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_COUNT)

    def set_arp_sender_hardware_address_step(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_STEP, ip)

    def get_arp_sender_hardware_address_step(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS_STEP)
    # end Arp sender hardware address methods

    # start Arp source protocol address methods
    #  source_protocol_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_arp_source_protocol_address(self, source_protocol_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_SOURCE_PROTOCOL_ADDRESS, ignore_check)
        source_protocol_address = self.normalize_value(source_protocol_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_SOURCE_PROTOCOL_ADDRESS,
                                  source_protocol_address)

    def get_arp_source_protocol_address(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                                              ArpPacketConstants.ARP_SOURCE_PROTOCOL_ADDRESS),
                                    PacketConstants.IPV4_ADDRESS)

    def get_arp_source_protocol_address_hex_string(self):
        ip = self.get_arp_source_protocol_address()
        if Ipv4Address.is_valid_ipv4(ip):
            ip = Ipv4Address(ip)
            return ip.to_formated_string(16, "")
        else:
            return None

    def get_arp_source_protocol_address_hltapi_cmd(self, dummy_dict):
        source_protocol_address = self.get_arp_source_protocol_address()
        if source_protocol_address and 'Not Set' not in source_protocol_address:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_PROTOCOL_ADDRESS_CMD] = source_protocol_address

    def set_arp_source_protocol_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_MODE, ip)

    def get_arp_source_protocol_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_MODE)

    def set_arp_source_protocol_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_COUNT, ip)

    def get_arp_source_protocol_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_COUNT)

    def set_arp_source_protocol_address_step(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_STEP, ip)

    def get_arp_source_protocol_address_step(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_SENDER_PROTOCOL_ADDRESS_STEP)
    # end Arp source protocol address methods

    # start Arp target hardware address methods
    #  target_hardware_address is a 48 bit ENET_ADDRESS example: 00:33:44:55:66:44
    def set_arp_target_hardware_address(self, target_hardware_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS, ignore_check)
        target_hardware_address = self.normalize_value(target_hardware_address, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS,
                                  target_hardware_address)

    def get_arp_target_hardware_address(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                                              ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS),
                                    PacketConstants.ENET_ADDRESS)

    def get_arp_target_hardware_address_hltapi_cmd(self, dummy_dict):
        target_hardware_address = self.get_arp_target_hardware_address()
        if target_hardware_address and 'Not Set' not in target_hardware_address:
            dummy_dict[TrafficConfigConstants.ARP_DST_HW_ADDR_CMD] = target_hardware_address

    def set_arp_target_hardware_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_MODE, ip)

    def get_arp_target_hardware_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_MODE)

    def set_arp_target_hardware_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_COUNT, ip)

    def get_arp_target_hardware_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_COUNT)

    def set_arp_target_hardware_address_step(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_STEP, ip)

    def get_arp_target_hardware_address_step(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS_STEP)
    # end Arp target hardware address methods

    # start Arp target protocol address methods
    #  target_protocol_address is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_arp_target_protocol_address(self, target_protocol_address, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS, ignore_check)
        target_protocol_address = self.normalize_value(target_protocol_address, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP, ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS,
                                  target_protocol_address)

    def get_arp_target_protocol_address(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                                              ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS),
                                    PacketConstants.IPV4_ADDRESS)

    def get_arp_target_protocol_address_hex_string(self):
        ip = self.get_arp_target_protocol_address()
        if Ipv4Address.is_valid_ipv4(ip):
            ip = Ipv4Address(ip)
            return ip.to_formated_string(16, "")
        else:
            return None

    def get_arp_target_protocol_address_hltapi_cmd(self, dummy_dict):
        target_protocol_address = self.get_arp_target_protocol_address()
        if target_protocol_address and 'Not Set' not in target_protocol_address:
            dummy_dict[TrafficConfigConstants.TEMP_TARGET_PROTOCOL_ADDRESS_CMD] = target_protocol_address
    # end Arp target protocol address methods

    def set_arp_target_protocol_address_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_MODE, ip)

    def get_arp_target_protocol_address_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_MODE)

    def set_arp_target_protocol_address_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_COUNT, ip)

    def get_arp_target_protocol_address_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_COUNT)

    def set_arp_target_protocol_address_step(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                  ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_STEP, ip)

    def get_arp_target_protocol_address_step(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_ARP,
                                         ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS_STEP)

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("hardware", self.format_int(self.get_arp_hardware(), 4))
        table.add_row_value("proto", self.format_int(self.get_arp_proto(), 4))
        table.add_row_value("id", self.format_int(self.get_arp_id(), 2))
        table.add_row_value("seq", self.format_int(self.get_arp_seq(), 2))
        table.add_row_value("operation", self.format_int(self.get_arp_operation(), 4))
        table.add_row_value("sender hardware address", self.get_arp_sender_hardware_address())
        table.add_row_value("source protocol address", self.get_arp_source_protocol_address())
        table.add_row_value("target hardware address", self.get_arp_target_hardware_address())
        table.add_row_value("target protocol address", self.get_arp_target_protocol_address())
        return "\n\nARP HEADER" + table.to_table_string()

    def add_arp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ARP)

    def build(self):
        self.add_arp_header()
        self.set_ether_type("0x0806", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_arp_hardware_hltapi_cmd(dummy_dict)
        self.get_arp_proto_hltapi_cmd(dummy_dict)
        self.get_arp_id_hltapi_cmd(dummy_dict)
        self.get_arp_seq_hltapi_cmd(dummy_dict)
        self.get_arp_operation_hltapi_cmd(dummy_dict)
        self.get_arp_sender_hardware_address_hltapi_cmd(dummy_dict)
        # self.get_arp_source_protocol_address_hltapi_cmd(dummy_dict)
        self.get_arp_target_hardware_address_hltapi_cmd(dummy_dict)
        # self.get_arp_target_protocol_address_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.L3_PROTOCOL_CMD] = TrafficConfigConstants.L3_PROTOCOL_ARP
        return dummy_dict

    @staticmethod
    def translateArpValue(data):
        value = "arp"
        if "cont" in data.lower():
            value += "Continuous"
        if "dec" in data.lower():
            value += "Decrement"
        elif "inc" in data.lower():
            value += "Increment"
        else:
            value += "Idle"
        return value

    def get_ixtclhal_arp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = list()
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        dummy_dict.append("arp setDefault")

        if self.is_field_set(self.get_arp_source_protocol_address()):
            dummy_dict.append("arp config -sourceProtocolAddr                 \"" +
                              self.get_arp_source_protocol_address() + "\"")
        if self.is_field_set(self.get_arp_target_protocol_address()):
            dummy_dict.append("arp config -destProtocolAddr                   \"" +
                              self.get_arp_target_protocol_address() + "\"")
        operation = self.get_arp_operation()
        if operation in ArpPacketConstants.ARP_VALUES:
            dummy_dict.append("arp config -operation                          " +
                              ArpPacketConstants.ARP_VALUES[operation])

        if self.is_field_set(self.get_arp_sender_hardware_address()):
            dummy_dict.append("arp config -sourceHardwareAddr                 \"" +
                              self.get_arp_sender_hardware_address().replace(":", " ") + "\"")

        if self.is_field_set(self.get_arp_target_hardware_address()):
            dummy_dict.append("arp config -destHardwareAddr                   \"" +
                              self.get_arp_target_hardware_address().replace(":", " ") + "\"")

        if self.is_field_set(self.get_arp_target_hardware_address_mode()):
            value = ArpPacketHeader.translateArpValue(self.get_arp_target_hardware_address_mode())
            dummy_dict.append("arp config -destHardwareAddrMode                   \"" + value + "\"")
        if self.is_field_set(self.get_arp_target_hardware_address_count()):
            dummy_dict.append("arp config -destHardwareAddrRepeatCount                   \"" +
                              self.get_arp_target_hardware_address_count().replace(":", " ") + "\"")

        if self.is_field_set(self.get_arp_sender_hardware_address_mode()):
            value = ArpPacketHeader.translateArpValue(self.get_arp_sender_hardware_address_mode())
            dummy_dict.append("arp config -sourceHardwareAddrMode                   \"" + value + "\"")
        if self.is_field_set(self.get_arp_sender_hardware_address_count()):
            dummy_dict.append("arp config -sourceHardwareAddrRepeatCount                   \"" +
                              self.get_arp_sender_hardware_address_count().replace(":", " ") + "\"")

        if self.is_field_set(self.get_arp_target_protocol_address_mode()):
            value = ArpPacketHeader.translateArpValue(self.get_arp_target_protocol_address_mode())
            dummy_dict.append("arp config -destProtocolAddrMode                   \"" + value + "\"")
        if self.is_field_set(self.get_arp_target_protocol_address_count()):
            dummy_dict.append("arp config -destProtocolAddrRepeatCount                   \"" +
                              self.get_arp_target_protocol_address_count().replace(":", " ") + "\"")

        if self.is_field_set(self.get_arp_source_protocol_address_mode()):
            value = ArpPacketHeader.translateArpValue(self.get_arp_source_protocol_address_mode())
            dummy_dict.append("arp config -sourceProtocolAddrMode                   \"" + value + "\"")
        if self.is_field_set(self.get_arp_source_protocol_address_count()):
            dummy_dict.append("arp config -sourceProtocolAddrRepeatCount                   \"" +
                              self.get_arp_source_protocol_address_count().replace(":", " ") + "\"")

        # arp setDefault
# arp config -sourceProtocolAddr                 "1.1.12.12"
# arp config -destProtocolAddr                   "2.2.12.12"
# arp config -operation                          arpReply
# arp config -sourceHardwareAddr                 "00 44 33 66 22 00"
# arp config -destHardwareAddr                   "00 55 44 33 22 00"
# arp config -sourceProtocolAddrMode             arpContinuousIncrement
# arp config -sourceProtocolAddrRepeatCount      1
# arp config -destProtocolAddrMode               arpContinuousDecrement
# arp config -destProtocolAddrRepeatCount        1
# arp config -sourceHardwareAddrMode             arpIncrement
# arp config -sourceHardwareAddrRepeatCount      1
# arp config -destHardwareAddrMode               arpDecrement
# arp config -destHardwareAddrRepeatCount        1
        # protocol config -appName                            Arp

# protocol setDefault
# protocol config -name                               mac
# protocol config -appName                            Arp
# protocol config -ethernetType                       ethernetII
# protocol config -enable802dot1qTag                  vlanNone
# protocol config -enableISLtag                       false
# protocol config -enableMPLS                         false
# protocol config -enableMacSec                       false
# protocol config -enableOAM                          false
# protocol config -enableDataCenterEncapsulation      false
# protocol config -enableProtocolPad                  false
#
# arp setDefault
# arp config -sourceProtocolAddr                 "1.1.12.12"
# arp config -destProtocolAddr                   "2.2.12.12"
# arp config -operation                          arpReply
# arp config -sourceHardwareAddr                 "00 44 33 66 22 00"
# arp config -destHardwareAddr                   "00 55 44 33 22 00"
# arp config -sourceProtocolAddrMode             arpIncrement
# arp config -sourceProtocolAddrRepeatCount      1
# arp config -destProtocolAddrMode               arpIncrement
# arp config -destProtocolAddrRepeatCount        1
# arp config -sourceHardwareAddrMode             arpIncrement
# arp config -sourceHardwareAddrRepeatCount      1
# arp config -destHardwareAddrMode               arpIncrement
# arp config -destHardwareAddrRepeatCount        1
# if {[arp set $chassis $card $port]} {
# 	errorMsg "Error calling arp set $chassis $card $port"
# 	set retCode $::TCL_ERROR
# }

        dummy_dict.append("arp set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_arp_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_arp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_arp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_arp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_arp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kArpFieldNumber
        arpField = p.Extensions[arp]

        # p.Extensions[arp].sender_hw_addr = 0x100
        if self.is_field_set(self.get_arp_sender_hardware_address()):
            arpField.sender_hw_addr = int(self.get_arp_sender_hardware_address().replace(":", ""), 16)
        # p.Extensions[arp].sender_proto_addr = 0x6f6f6f6f
        if self.is_field_set(self.get_arp_source_protocol_address()):
            arpField.sender_proto_addr = int(self.get_arp_source_protocol_address_hex_string(), 16)
        # p.Extensions[arp].target_hw_addr = 0x300
        if self.is_field_set(self.get_arp_target_hardware_address()):
            arpField.target_hw_addr = int(self.get_arp_target_hardware_address().replace(":", ""), 16)
        # p.Extensions[arp].target_proto_addr = 0xdededede
        if self.is_field_set(self.get_arp_target_protocol_address()):
            arpField.target_proto_addr = int(self.get_arp_target_protocol_address_hex_string(), 16)

        if self.is_field_set(self.get_arp_operation()):
            arpField.op_code = int(self.get_arp_operation())

    def config_jets_stream_arp(self, jets_dev, port_string, stream_id, **kwargs):
        """
        ARP_HDR {
          ar_hrd : 16 : default=1, legal_values=(ENET=1, EXP3M_ENET=2, AX25=3, ProNET_TR=4, Chaos=5, A802=6, ARCnet=7,
                        HyperChannel=8, Lanstar=9, Autonet_Short=10, LocalTalk=11, LocalNet=12, Ultra_Link=13, SMDS=14,
                        FR=15, ATM=16, HDLC=17, Fibre_channel=18, ATM_1577=19, Serial_Ln=20 ),
                        display="Hardware", index=1;
          ar_pro : 16 : default=0x0800, legal_values=(IP_Protocol=0x800), display="Protocol Ident. ", index=2;
          ar_hln : 8  : default=6, display="Hardware length %dec", index=3;
          ar_pln : 8  : default=4, display="Protocol length %dec", index=4;
          ar_op  : 16 : default=1, legal_values=(REQ=1, RES=2, RARP_REQ=3, RARP_RES=4, DRARP_REQ=5, DRARP_RES=6,
                        DRARP_ERR=7, INVREQ=8, INVRES=9, ARP_NAK=10 ), display="ARP Op Codes", index=5;
          ar_sha : ar_hln * 8 : default=ENET_HDR.src, display="Source Hardware %mac", index=6;
          ar_spa : ar_pln * 8 : display="Source Protocol %ipa", index=7;
          ar_tha : ar_hln * 8 : display="Target Hardware %mac", index=8;
          ar_tpa : ar_pln * 8 : display="Target Protocol %ipa", index=9;
        } display="ARP Header", index=5002;
        """
        pkt_fields = {}

        if self.is_field_set(self.get_arp_hardware()):
            pkt_fields["ar_hrd"] = str(self.get_arp_hardware())
        if self.is_field_set(self.get_arp_proto()):
            pkt_fields["ar_pro"] = str(self.get_arp_proto())
        if self.is_field_set(self.get_arp_id()):
            pkt_fields["ar_hln"] = str(self.get_arp_id())
        if self.is_field_set(self.get_arp_seq()):
            pkt_fields["ar_pln"] = str(self.get_arp_seq())
        if self.is_field_set(self.get_arp_operation()):
            pkt_fields["ar_op"] = str(self.get_arp_operation())
        if self.is_field_set(self.get_arp_sender_hardware_address()):
            pkt_fields["ar_sha"] = str(self.get_arp_sender_hardware_address())
        if self.is_field_set(self.get_arp_source_protocol_address()):
            pkt_fields["ar_spa"] = str(self.get_arp_source_protocol_address())
        if self.is_field_set(self.get_arp_target_hardware_address()):
            pkt_fields["ar_tha"] = str(self.get_arp_target_hardware_address())
        if self.is_field_set(self.get_arp_target_protocol_address()):
            pkt_fields["ar_tpa"] = str(self.get_arp_target_protocol_address())
        jets_dev.pdl_add_packet_header("ARP_HDR", pkt_fields)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        hardware = self.get_bits_from_string(16, payload)
        self.set_arp_hardware("0x" + hardware)
        payload = self.remove_bits_from_string(16, payload)
        proto = self.get_bits_from_string(16, payload)
        self.set_arp_proto("0x" + proto)
        payload = self.remove_bits_from_string(16, payload)
        pkt_id = self.get_bits_from_string(8, payload)
        self.set_arp_id("0x" + pkt_id)
        payload = self.remove_bits_from_string(8, payload)
        seq = self.get_bits_from_string(8, payload)
        self.set_arp_seq("0x" + seq)
        payload = self.remove_bits_from_string(8, payload)
        operation = self.get_bits_from_string(16, payload)
        self.set_arp_operation("0x" + operation)
        payload = self.remove_bits_from_string(16, payload)
        sender_hardware_address = self.get_bits_from_string(48, payload)
        self.set_arp_sender_hardware_address("0x" + sender_hardware_address)
        payload = self.remove_bits_from_string(48, payload)
        source_protocol_address = self.get_bits_from_string(32, payload)
        self.set_arp_source_protocol_address("0x" + source_protocol_address)
        payload = self.remove_bits_from_string(32, payload)
        target_hardware_address = self.get_bits_from_string(48, payload)
        self.set_arp_target_hardware_address("0x" + target_hardware_address)
        payload = self.remove_bits_from_string(48, payload)
        target_protocol_address = self.get_bits_from_string(32, payload)
        self.set_arp_target_protocol_address("0x" + target_protocol_address)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_arp_hardware(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_arp_proto(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_arp_id(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_arp_seq(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_arp_operation(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_arp_sender_hardware_address(), PacketConstants.ENET_ADDRESS, 48)
        ret_string += self.format_byte_string(self.get_arp_source_protocol_address(), PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_arp_target_hardware_address(), PacketConstants.ENET_ADDRESS, 48)
        ret_string += self.format_byte_string(self.get_arp_target_protocol_address(), PacketConstants.IPV4_ADDRESS, 32)
        return ret_string

    @staticmethod
    def compare_arp_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                  print_failures=True):
        results = True
        try:
            assert isinstance(expected, ArpPacketHeader)
            assert isinstance(actual, ArpPacketHeader)
            if expected.do_i_check_this_field(expected.get_arp_hardware(), ArpPacketConstants.ARP_HARDWARE,
                                              ignore_list, include_list):
                name = "ARP hardware : "
                if expected.get_arp_hardware() != actual.get_arp_hardware():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_hardware()) + " != " +
                                                      str(actual.get_arp_hardware()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_hardware()) + " == " +
                                                 str(actual.get_arp_hardware()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_proto(), ArpPacketConstants.ARP_PROTO,
                                              ignore_list, include_list):
                name = "ARP proto : "
                if expected.get_arp_proto() != actual.get_arp_proto():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_proto()) + " != " +
                                                      str(actual.get_arp_proto()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_proto()) + " == " +
                                                 str(actual.get_arp_proto()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_id(), ArpPacketConstants.ARP_ID,
                                              ignore_list, include_list):
                name = "ARP id : "
                if expected.get_arp_id() != actual.get_arp_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_id()) + " != " +
                                                      str(actual.get_arp_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_id()) + " == " +
                                                 str(actual.get_arp_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_seq(), ArpPacketConstants.ARP_SEQ,
                                              ignore_list, include_list):
                name = "ARP seq : "
                if expected.get_arp_seq() != actual.get_arp_seq():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_seq()) + " != " +
                                                      str(actual.get_arp_seq()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_seq()) + " == " +
                                                 str(actual.get_arp_seq()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_operation(), ArpPacketConstants.ARP_OPERATION,
                                              ignore_list, include_list):
                name = "ARP operation : "
                if expected.get_arp_operation() != actual.get_arp_operation():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_operation()) + " != " +
                                                      str(actual.get_arp_operation()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_operation()) + " == " +
                                                 str(actual.get_arp_operation()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_sender_hardware_address(),
                                              ArpPacketConstants.ARP_SENDER_HARDWARE_ADDRESS,
                                              ignore_list, include_list):
                name = "ARP sender hardware address : "
                if expected.get_arp_sender_hardware_address() != actual.get_arp_sender_hardware_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_sender_hardware_address()) + " != " +
                                                      str(actual.get_arp_sender_hardware_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_sender_hardware_address()) + " == " +
                                                 str(actual.get_arp_sender_hardware_address()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_source_protocol_address(),
                                              ArpPacketConstants.ARP_SOURCE_PROTOCOL_ADDRESS,
                                              ignore_list, include_list):
                name = "ARP source protocol address : "
                if expected.get_arp_source_protocol_address() != actual.get_arp_source_protocol_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_source_protocol_address()) + " != " +
                                                      str(actual.get_arp_source_protocol_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_source_protocol_address()) + " == " +
                                                 str(actual.get_arp_source_protocol_address()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_target_hardware_address(),
                                              ArpPacketConstants.ARP_TARGET_HARDWARE_ADDRESS,
                                              ignore_list, include_list):
                name = "ARP target hardware address : "
                if expected.get_arp_target_hardware_address() != actual.get_arp_target_hardware_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_target_hardware_address()) + " != " +
                                                      str(actual.get_arp_target_hardware_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_target_hardware_address()) + " == " +
                                                 str(actual.get_arp_target_hardware_address()) + " Pass")

            if expected.do_i_check_this_field(expected.get_arp_target_protocol_address(),
                                              ArpPacketConstants.ARP_TARGET_PROTOCOL_ADDRESS,
                                              ignore_list, include_list):
                name = "ARP target protocol address : "
                if expected.get_arp_target_protocol_address() != actual.get_arp_target_protocol_address():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_arp_target_protocol_address()) + " != " +
                                                      str(actual.get_arp_target_protocol_address()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_arp_target_protocol_address()) + " == " +
                                                 str(actual.get_arp_target_protocol_address()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with ArpPacketHeader")
        return results


class ArpPacketConstants:
    def __init__(self):
        pass

    ARP_HARDWARE = "ARP_HARDWARE"
    ARP_HARDWARE_ETHERNET = "1"

    ARP_PROTO = "ARP_PROTO"

    ARP_ID = "ARP_ID"

    ARP_SEQ = "ARP_SEQ"

    ARP_OPERATION = "ARP_OPERATION"
    ARP_OPERATION_RESERVED = "0"
    ARP_OPERATION_REQUEST = "1"
    ARP_OPERATION_REPLY = "2"
    ARP_OPERATION_REQUEST_REVERSE = "3"
    ARP_OPERATION_REPLY_REVERSE = "4"
    ARP_OPERATION_DRARP_REQUEST = "5"
    ARP_OPERATION_DRARP_REPLY = "6"
    ARP_OPERATION_DRARP_ERROR = "7"
    ARP_OPERATION_INARP_REQUEST = "8"
    ARP_OPERATION_INARP_REPLY = "9"

    ARP_VALUES = {"0": "unknown", "1": "arpRequest", "2": "arpReply", "3": "rarpRequest", "4": "rarpReply",
                  0: "unknown", 1: "arpRequest", 2: "arpReply", 3: "rarpRequest", 4: "rarpReply"}

    ARP_SENDER_HARDWARE_ADDRESS = "ARP_SENDER_HARDWARE_ADDRESS"

    ARP_SOURCE_PROTOCOL_ADDRESS = "ARP_SOURCE_PROTOCOL_ADDRESS"

    ARP_TARGET_HARDWARE_ADDRESS = "ARP_TARGET_HARDWARE_ADDRESS"

    ARP_TARGET_PROTOCOL_ADDRESS = "ARP_TARGET_PROTOCOL_ADDRESS"

    ARP_SENDER_HARDWARE_ADDRESS_MODE = "ARP_SENDER_HARDWARE_ADDRESS_MODE"
    ARP_SENDER_HARDWARE_ADDRESS_COUNT = "ARP_SENDER_HARDWARE_ADDRESS_COUNT"
    ARP_SENDER_HARDWARE_ADDRESS_STEP = "ARP_SENDER_HARDWARE_ADDRESS_STEP"

    ARP_SENDER_PROTOCOL_ADDRESS_MODE = "ARP_SENDER_PROTOCOL_ADDRESS_MODE"
    ARP_SENDER_PROTOCOL_ADDRESS_COUNT = "ARP_SENDER_PROTOCOL_ADDRESS_COUNT"
    ARP_SENDER_PROTOCOL_ADDRESS_STEP = "ARP_SENDER_PROTOCOL_ADDRESS_STEP"

    ARP_TARGET_PROTOCOL_ADDRESS_MODE = "ARP_TARGET_PROTOCOL_ADDRESS_MODE"
    ARP_TARGET_PROTOCOL_ADDRESS_COUNT = "ARP_TARGET_PROTOCOL_ADDRESS_COUNT"
    ARP_TARGET_PROTOCOL_ADDRESS_STEP = "ARP_TARGET_PROTOCOL_ADDRESS_STEP"

    ARP_TARGET_HARDWARE_ADDRESS_MODE = "ARP_TARGET_HARDWARE_ADDRESS_MODE"
    ARP_TARGET_HARDWARE_ADDRESS_COUNT = "ARP_TARGET_HARDWARE_ADDRESS_COUNT"
    ARP_TARGET_HARDWARE_ADDRESS_STEP = "ARP_TARGET_HARDWARE_ADDRESS_STEP"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
