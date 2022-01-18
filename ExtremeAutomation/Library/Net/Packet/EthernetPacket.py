from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket
from ExtremeAutomation.Library.Net.Packet.EthernetPacketHeader import EthernetPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
import copy
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import InnerPacketHeader


class EthernetPacket(AbstractPacket, EthernetPacketHeader):
    def __init__(self):
        super(EthernetPacket, self).__init__()
        EthernetPacketHeader.__init__(self)
        self.set_name("EthernetPacket")
        self.build()

    def set_destination_mac(self, da, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(EthernetPacketConstants.ETHER_DESTINATION_ADDRESS, ignore_check)
        da = self.normalize_value(da, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L1_ETHERNET,
                                  EthernetPacketConstants.ETHER_DESTINATION_ADDRESS, da)

    def get_destination_mac(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L1_ETHERNET, EthernetPacketConstants.ETHER_DESTINATION_ADDRESS),
            PacketConstants.ENET_ADDRESS)

    def set_destination_mac_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_MODE, ip)

    def get_destination_mac_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_MODE)

    def set_destination_mac_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_COUNT, ip)

    def get_destination_mac_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_COUNT)

    def set_destination_mac_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_MASK, ip)

    def get_destination_mac_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_MASK)

    def set_destination_mac_seed(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_SEED, ip)

    def get_destination_mac_seed(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_DESTINATION_ADDRESS_SEED)

    def set_source_mac(self, sa, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(EthernetPacketConstants.ETHER_SOURCE_ADDRESS, ignore_check)
        sa = self.normalize_value(sa, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L1_ETHERNET,
                                  EthernetPacketConstants.ETHER_SOURCE_ADDRESS, sa)

    def get_source_mac(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L1_ETHERNET, EthernetPacketConstants.ETHER_SOURCE_ADDRESS),
            PacketConstants.ENET_ADDRESS)

    def set_source_mac_mode(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_SOURCE_ADDRESS_MODE, ip)

    def get_source_mac_mode(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_SOURCE_ADDRESS_MODE)

    def set_source_mac_count(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_SOURCE_ADDRESS_COUNT, ip)

    def get_source_mac_count(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_SOURCE_ADDRESS_COUNT)

    def set_source_mac_mask(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_SOURCE_ADDRESS_MASK, ip)

    def get_source_mac_mask(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_SOURCE_ADDRESS_MASK)

    def set_source_mac_seed(self, ip):
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                  EthernetPacketConstants.ETHER_SOURCE_ADDRESS_SEED, ip)

    def get_source_mac_seed(self):
        return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_IPV6,
                                         EthernetPacketConstants.ETHER_SOURCE_ADDRESS_SEED)

    def build(self):
        self.add_enet_header()
        # self.set_destination_mac("00:00:00:00:00:00", True)
        # self.set_source_mac("00:00:00:00:00:00", True)

    def get_header_length(self):
        return self.HEADER_SIZE_ETHERNET

    def to_packet_string(self):
        ret_string = "Packet Class -- " + self.get_name()
        if self.length:
            ret_string += ":\n length = " + str(self.length)
        else:
            ret_string += ":\n length = Not Set"
        if self.payload:
            ret_string += ":\n Payload = " + str(self.payload)
        else:
            ret_string += ":\n Payload = Not Set"
        if self.status:
            ret_string += ":\n Status = " + str(self.status)
        else:
            ret_string += ":\n Status = Not Set"
        table = TableFormatter()
        table.add_row_value("Destination Address", self.get_destination_mac())
        table.add_row_value("Source Address", self.get_source_mac())
        ret_string += table.to_table_string() + "\n"
        return ret_string

    def get_hltapi_commands(self):
        dummy_dict = dict()
        dummy_dict[TrafficConfigConstants.MAC_DST_CMD] = self.get_destination_mac()
        dummy_dict[TrafficConfigConstants.MAC_SRC_CMD] = self.get_source_mac()
        return dummy_dict

    def get_ixtclhal_payload_api_commands(self, port, streamid):
        dummy_dict = []
        if self.is_field_set(self.get_payload()):
            dummy_dict.append("stream get " + port + " " + str(streamid))
            dummy_dict.append("stream config -patternType                        nonRepeat")
            dummy_dict.append("stream config -dataPattern                        userpattern")
            dummy_dict.append("stream config -pattern                            \"" +
                              StringUtils.place_character_every_n_characters(self.get_payload(), " ", 2) + "\"")
            dummy_dict.append("stream set " + port + " " + str(streamid))
            dummy_dict.append("stream write " + port + " " + str(streamid))
            dummy_dict.append("set portList [ list [ list " + port + "]]")
            dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_packet_api_commands(self, port_name_stream):
        dummy_dict = list()
        dummy_dict.append("stc::config $" + port_name_stream +
                          " -InsertSig false -FrameLengthMode FIXED -FixedFrameLength " + str(self.get_length()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        payload = payload.replace(" ", "").upper()
        super(EthernetPacket, self).set_payload(payload)
        EthernetPacketHeader.parse_bytes(self)

    def clone(self, packet):
        super(EthernetPacket, self).clone(packet)
        self.length = copy.deepcopy(packet.length)
        self.status = copy.deepcopy(packet.status)
        self.payload = copy.deepcopy(packet.payload)
        self.timestamp = copy.deepcopy(packet.timestamp)

    def __str__(self):
        return super(EthernetPacket, self).__str__() + "\n" + self.to_packet_string()

    def get_header_bytes(self, break_up_header=False):
        temp_bytes = super(EthernetPacket, self).get_header_bytes(break_up_header)
        temp_bytes += EthernetPacketHeader.get_header_bytes(self)
        return temp_bytes.replace(" ", "")

    def get_bytes(self, break_up_header=False):
        temp_bytes = self.get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "+"
        if not isinstance(self, InnerPacketHeader):
            temp_bytes += self.get_payload()
        return temp_bytes.replace(" ", "").replace("0x", "")

    def get_bytes_with_fcs(self, break_up_header=False):
        temp_bytes = self.get_header_bytes(break_up_header)
        if break_up_header:
            temp_bytes += "+"
        return (temp_bytes + self.get_payload()).replace(" ", "")

    def get_minimum_packet_size(self):
        pkt_buffer = self.get_header_length() + 4  # add the CRC
        minsize = 64
        if isinstance(self, TaggedPacketHeader):
            minsize += 4
        elif isinstance(self, VlanStackPacketHeader):
            minsize += (4 * self.get_vlan_num())
        return int(max(pkt_buffer, minsize))

    def auto_set_minimum_length(self):
        self.set_length(self.get_minimum_packet_size())

    def configure_packet(self, length=False):
        if not length:
            self.auto_set_minimum_length()
        length = self.get_length()
        self.configure_packet_length_fields(length)
        self.configure_packet_checksum_fields()

    def configure_packet_length_fields(self, length=False):
        if not length:
            self.auto_set_minimum_length()
        self.get_length()

    def configure_packet_checksum_fields(self):
        pass

    def config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, **kwargs):
        EthernetPacketHeader.config_thirdparty_traffic_generator_stream_ether(self, tgen_type, generator_ref,
                                                                              port_string, stream_id, **kwargs)
