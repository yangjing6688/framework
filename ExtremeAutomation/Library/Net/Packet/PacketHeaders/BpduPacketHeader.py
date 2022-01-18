from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.stp_pb2 import stp
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class BpduPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    BPDU Packet Header
        # protocol id = 16bits
        # version = 8bits
        # message type = 8bits
        # flags = 8bits
        # root priority = 16bits
        # root mac = 48bits
        # cost = 32bits
        # bridge priority = 16bits
        # bridge mac = 48bits
        # port id = 16bits
        # age = 16bits
        # max age = 16bits
        # hello timer = 16bits
        # forward delay = 16bits
    """

    def __init__(self):
        self.add_bpdu_header()
        self.HEADER_SIZE_BPDU = (16 + 8 + 8 + 8 + 16 + 48 + 32 + 16 + 48 + 16 + 16 + 16 + 16 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Bpdu protocol id methods
    #  protocol_id is a 16 bit INTEGER example: 1
    def set_bpdu_protocol_id(self, protocol_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_PROTOCOL_ID, ignore_check)
        protocol_id = self.normalize_value(protocol_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_PROTOCOL_ID, protocol_id)

    def get_bpdu_protocol_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_PROTOCOL_ID), PacketConstants.INTEGER)

    def get_bpdu_protocol_id_hltapi_cmd(self, dummy_dict):
        protocol_id = self.get_bpdu_protocol_id()
        if isinstance(protocol_id, int):
            protocol_id = str(protocol_id)
        if protocol_id and 'Not Set' not in protocol_id:
            dummy_dict[TrafficConfigConstants.TEMP_PROTOCOL_ID_CMD] = protocol_id
    # end Bpdu protocol id methods

    # start Bpdu version methods
    #  version is a 8 bit INTEGER example: 1
    def set_bpdu_version(self, version, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_VERSION, ignore_check)
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_VERSION, version)

    def get_bpdu_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_VERSION), PacketConstants.INTEGER)

    def get_bpdu_version_hltapi_cmd(self, dummy_dict):
        version = self.get_bpdu_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end Bpdu version methods

    # start Bpdu message type methods
    #  message_type is a 8 bit INTEGER example: 1
    def set_bpdu_message_type(self, message_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_MESSAGE_TYPE, ignore_check)
        message_type = self.normalize_value(message_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_MESSAGE_TYPE, message_type)

    def get_bpdu_message_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_MESSAGE_TYPE), PacketConstants.INTEGER)

    def get_bpdu_message_type_hltapi_cmd(self, dummy_dict):
        message_type = self.get_bpdu_message_type()
        if isinstance(message_type, int):
            message_type = str(message_type)
        if message_type and 'Not Set' not in message_type:
            dummy_dict[TrafficConfigConstants.TEMP_MESSAGE_TYPE_CMD] = message_type
    # end Bpdu message type methods

    # start Bpdu flags methods
    #  flags is a 8 bit INTEGER example: 1
    def set_bpdu_flags(self, flags, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_FLAGS, ignore_check)
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_FLAGS, flags)

    def get_bpdu_flags(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_FLAGS), PacketConstants.INTEGER)

    def get_bpdu_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_bpdu_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_CMD] = flags
    # end Bpdu flags methods

    # start Bpdu root priority methods
    #  root_priority is a 16 bit INTEGER example: 1
    def set_bpdu_root_priority(self, root_priority, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_ROOT_PRIORITY, ignore_check)
        root_priority = self.normalize_value(root_priority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_ROOT_PRIORITY, root_priority)

    def get_bpdu_root_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_ROOT_PRIORITY), PacketConstants.INTEGER)

    def get_bpdu_root_priority_hltapi_cmd(self, dummy_dict):
        root_priority = self.get_bpdu_root_priority()
        if isinstance(root_priority, int):
            root_priority = str(root_priority)
        if root_priority and 'Not Set' not in root_priority:
            dummy_dict[TrafficConfigConstants.TEMP_ROOT_PRIORITY_CMD] = root_priority
    # end Bpdu root priority methods

    # start Bpdu root mac methods
    #  root_mac is a 48 bit ENET_ADDRESS example: 00:33:44:55:66:44
    def set_bpdu_root_mac(self, root_mac, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_ROOT_MAC, ignore_check)
        root_mac = self.normalize_value(root_mac, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_ROOT_MAC, root_mac)

    def get_bpdu_root_mac(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_ROOT_MAC), PacketConstants.ENET_ADDRESS)

    def get_bpdu_root_mac_hltapi_cmd(self, dummy_dict):
        root_mac = self.get_bpdu_root_mac()
        if root_mac and 'Not Set' not in root_mac:
            dummy_dict[TrafficConfigConstants.TEMP_ROOT_MAC_CMD] = root_mac
    # end Bpdu root mac methods

    # start Bpdu cost methods
    #  cost is a 32 bit INTEGER example: 1
    def set_bpdu_cost(self, cost, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_COST, ignore_check)
        cost = self.normalize_value(cost, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_COST, cost)

    def get_bpdu_cost(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_COST), PacketConstants.INTEGER)

    def get_bpdu_cost_hltapi_cmd(self, dummy_dict):
        cost = self.get_bpdu_cost()
        if isinstance(cost, int):
            cost = str(cost)
        if cost and 'Not Set' not in cost:
            dummy_dict[TrafficConfigConstants.TEMP_COST_CMD] = cost
    # end Bpdu cost methods

    # start Bpdu bridge priority methods
    #  bridge_priority is a 16 bit INTEGER example: 1
    def set_bpdu_bridge_priority(self, bridge_priority, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_BRIDGE_PRIORITY, ignore_check)
        bridge_priority = self.normalize_value(bridge_priority, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_BRIDGE_PRIORITY, bridge_priority)

    def get_bpdu_bridge_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_BRIDGE_PRIORITY), PacketConstants.INTEGER)

    def get_bpdu_bridge_priority_hltapi_cmd(self, dummy_dict):
        bridge_priority = self.get_bpdu_bridge_priority()
        if isinstance(bridge_priority, int):
            bridge_priority = str(bridge_priority)
        if bridge_priority and 'Not Set' not in bridge_priority:
            dummy_dict[TrafficConfigConstants.TEMP_BRIDGE_PRIORITY_CMD] = bridge_priority
    # end Bpdu bridge priority methods

    # start Bpdu bridge mac methods
    #  bridge_mac is a 48 bit ENET_ADDRESS example: 00:33:44:55:66:44
    def set_bpdu_bridge_mac(self, bridge_mac, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_BRIDGE_MAC, ignore_check)
        bridge_mac = self.normalize_value(bridge_mac, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_BRIDGE_MAC, bridge_mac)

    def get_bpdu_bridge_mac(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_BRIDGE_MAC), PacketConstants.ENET_ADDRESS)

    def get_bpdu_bridge_mac_hltapi_cmd(self, dummy_dict):
        bridge_mac = self.get_bpdu_bridge_mac()
        if bridge_mac and 'Not Set' not in bridge_mac:
            dummy_dict[TrafficConfigConstants.TEMP_BRIDGE_MAC_CMD] = bridge_mac
    # end Bpdu bridge mac methods

    # start Bpdu port id methods
    #  port_id is a 16 bit INTEGER example: 1
    def set_bpdu_port_id(self, port_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_PORT_ID, ignore_check)
        port_id = self.normalize_value(port_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_PORT_ID, port_id)

    def get_bpdu_port_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_PORT_ID), PacketConstants.INTEGER)

    def get_bpdu_port_id_hltapi_cmd(self, dummy_dict):
        port_id = self.get_bpdu_port_id()
        if isinstance(port_id, int):
            port_id = str(port_id)
        if port_id and 'Not Set' not in port_id:
            dummy_dict[TrafficConfigConstants.TEMP_PORT_ID_CMD] = port_id
    # end Bpdu port id methods

    # start Bpdu age methods
    #  age is a 16 bit INTEGER example: 1
    def set_bpdu_age(self, age, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_AGE, ignore_check)
        age = self.normalize_value(age, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_AGE, age)

    def get_bpdu_age(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_AGE), PacketConstants.INTEGER)

    def get_bpdu_age_hltapi_cmd(self, dummy_dict):
        age = self.get_bpdu_age()
        if isinstance(age, int):
            age = str(age)
        if age and 'Not Set' not in age:
            dummy_dict[TrafficConfigConstants.TEMP_AGE_CMD] = age
    # end Bpdu age methods

    # start Bpdu max age methods
    #  max_age is a 16 bit INTEGER example: 1
    def set_bpdu_max_age(self, max_age, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_MAX_AGE, ignore_check)
        max_age = self.normalize_value(max_age, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_MAX_AGE, max_age)

    def get_bpdu_max_age(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_MAX_AGE), PacketConstants.INTEGER)

    def get_bpdu_max_age_hltapi_cmd(self, dummy_dict):
        max_age = self.get_bpdu_max_age()
        if isinstance(max_age, int):
            max_age = str(max_age)
        if max_age and 'Not Set' not in max_age:
            dummy_dict[TrafficConfigConstants.TEMP_MAX_AGE_CMD] = max_age
    # end Bpdu max age methods

    # start Bpdu hello timer methods
    #  hello_timer is a 16 bit INTEGER example: 1
    def set_bpdu_hello_timer(self, hello_timer, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_HELLO_TIMER, ignore_check)
        hello_timer = self.normalize_value(hello_timer, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_HELLO_TIMER, hello_timer)

    def get_bpdu_hello_timer(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_HELLO_TIMER), PacketConstants.INTEGER)

    def get_bpdu_hello_timer_hltapi_cmd(self, dummy_dict):
        hello_timer = self.get_bpdu_hello_timer()
        if isinstance(hello_timer, int):
            hello_timer = str(hello_timer)
        if hello_timer and 'Not Set' not in hello_timer:
            dummy_dict[TrafficConfigConstants.TEMP_HELLO_TIMER_CMD] = hello_timer
    # end Bpdu hello timer methods

    # start Bpdu forward delay methods
    #  forward_delay is a 16 bit INTEGER example: 1
    def set_bpdu_forward_delay(self, forward_delay, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(BpduPacketConstants.BPDU_FORWARD_DELAY, ignore_check)
        forward_delay = self.normalize_value(forward_delay, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_BPDU,
                                  BpduPacketConstants.BPDU_FORWARD_DELAY, forward_delay)

    def get_bpdu_forward_delay(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_BPDU, BpduPacketConstants.BPDU_FORWARD_DELAY), PacketConstants.INTEGER)

    def get_bpdu_forward_delay_hltapi_cmd(self, dummy_dict):
        forward_delay = self.get_bpdu_forward_delay()
        if isinstance(forward_delay, int):
            forward_delay = str(forward_delay)
        if forward_delay and 'Not Set' not in forward_delay:
            dummy_dict[TrafficConfigConstants.TEMP_FORWARD_DELAY_CMD] = forward_delay
    # end Bpdu forward delay methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("protocol id", self.format_int(self.get_bpdu_protocol_id(), 4))
        table.add_row_value("version", self.format_int(self.get_bpdu_version(), 2))
        table.add_row_value("message type", self.format_int(self.get_bpdu_message_type(), 2))
        table.add_row_value("flags", self.format_int(self.get_bpdu_flags(), 2))
        table.add_row_value("root priority", self.format_int(self.get_bpdu_root_priority(), 4))
        table.add_row_value("root mac", self.get_bpdu_root_mac())
        table.add_row_value("cost", self.format_int(self.get_bpdu_cost(), 8))
        table.add_row_value("bridge priority", self.format_int(self.get_bpdu_bridge_priority(), 4))
        table.add_row_value("bridge mac", self.get_bpdu_bridge_mac())
        table.add_row_value("port id", self.format_int(self.get_bpdu_port_id(), 4))
        table.add_row_value("age", self.format_int(self.get_bpdu_age(), 4))
        table.add_row_value("max age", self.format_int(self.get_bpdu_max_age(), 4))
        table.add_row_value("hello timer", self.format_int(self.get_bpdu_hello_timer(), 4))
        table.add_row_value("forward delay", self.format_int(self.get_bpdu_forward_delay(), 4))
        return "\n\nBPDU HEADER" + table.to_table_string()

    def add_bpdu_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_BPDU)

    def build(self):
        self.add_bpdu_header()
        self.set_llc_dsap(0x42, True)
        self.set_llc_ssap(0x42, True)
        self.set_llc_control(0x03, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_bpdu_protocol_id_hltapi_cmd(dummy_dict)
        # self.get_bpdu_version_hltapi_cmd(dummy_dict)
        # self.get_bpdu_message_type_hltapi_cmd(dummy_dict)
        # self.get_bpdu_flags_hltapi_cmd(dummy_dict)
        # self.get_bpdu_root_priority_hltapi_cmd(dummy_dict)
        # self.get_bpdu_root_mac_hltapi_cmd(dummy_dict)
        # self.get_bpdu_cost_hltapi_cmd(dummy_dict)
        # self.get_bpdu_bridge_priority_hltapi_cmd(dummy_dict)
        # self.get_bpdu_bridge_mac_hltapi_cmd(dummy_dict)
        # self.get_bpdu_port_id_hltapi_cmd(dummy_dict)
        # self.get_bpdu_age_hltapi_cmd(dummy_dict)
        # self.get_bpdu_max_age_hltapi_cmd(dummy_dict)
        # self.get_bpdu_hello_timer_hltapi_cmd(dummy_dict)
        # self.get_bpdu_forward_delay_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_bpdu(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_bpdu(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_bpdu(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_bpdu(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kStpFieldNumber
    # update this from the ostinato docs.
        bpduField = p.Extensions[stp]
        if self.is_field_set(self.get_bpdu_protocol_id()):
            bpduField.protocol_id = int(self.get_bpdu_protocol_id())
        if self.is_field_set(self.get_bpdu_version()):
            bpduField.protocol_version_id = int(self.get_bpdu_version())
        if self.is_field_set(self.get_bpdu_message_type()):
            bpduField.bpdu_type = int(self.get_bpdu_message_type())
        if self.is_field_set(self.get_bpdu_flags()):
            bpduField.flags = int(self.get_bpdu_flags())
        if self.is_field_set(self.get_bpdu_root_mac()):
            bpduField.root_id = int(self.get_bpdu_root_mac().replace(":", ""), 16)
        if self.is_field_set(self.get_bpdu_cost()):
            bpduField.root_path_cost = int(self.get_bpdu_cost())
        if self.is_field_set(self.get_bpdu_bridge_mac()):
            bpduField.bridge_id = int(self.get_bpdu_bridge_mac().replace(":", ""), 16)
        if self.is_field_set(self.get_bpdu_port_id()):
            bpduField.port_id = int(self.get_bpdu_port_id())
        if self.is_field_set(self.get_bpdu_age()):
            bpduField.message_age = int(self.get_bpdu_age())
        if self.is_field_set(self.get_bpdu_max_age()):
            bpduField.max_age = int(self.get_bpdu_max_age())
        if self.is_field_set(self.get_bpdu_hello_timer()):
            bpduField.hello_time = int(self.get_bpdu_hello_timer())
        if self.is_field_set(self.get_bpdu_forward_delay()):
            bpduField.forward_delay = int(self.get_bpdu_forward_delay())

        # if self.is_field_set(self.get_bpdu_root_priority()) :
        #     bpduField.version = int(self.get_bpdu_root_priority())
        # if self.is_field_set(self.get_bpdu_bridge_priority()) :
        #     bpduField.version = int(self.get_bpdu_bridge_priority())

    def config_jets_stream_bpdu(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        # if not isinstance(self, IpV6PacketHeader) and not self.is_field_set(self.get_ip_protocol()):
        #     jets_dev.pdl_add_packet_header(JetsDeviceConstants.IP_HDR, {"ip_protocol": 1})
        # elif isinstance(self, IpV6PacketHeader) and not self.is_field_set(self.get_ipv6_next_header()):
        #     jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPV6_HDR, {"next_header": 1})
        pkt_bytes = "0x" + BpduPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_bpdu_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = BpduPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_bpdu_api_commands(self, port_name_stream):
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
        protocol_id = self.get_bits_from_string(16, payload)
        self.set_bpdu_protocol_id("0x" + protocol_id)
        payload = self.remove_bits_from_string(16, payload)
        version = self.get_bits_from_string(8, payload)
        self.set_bpdu_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        message_type = self.get_bits_from_string(8, payload)
        self.set_bpdu_message_type("0x" + message_type)
        payload = self.remove_bits_from_string(8, payload)
        flags = self.get_bits_from_string(8, payload)
        self.set_bpdu_flags("0x" + flags)
        payload = self.remove_bits_from_string(8, payload)
        root_priority = self.get_bits_from_string(16, payload)
        self.set_bpdu_root_priority("0x" + root_priority)
        payload = self.remove_bits_from_string(16, payload)
        root_mac = self.get_bits_from_string(48, payload)
        self.set_bpdu_root_mac("0x" + root_mac)
        payload = self.remove_bits_from_string(48, payload)
        cost = self.get_bits_from_string(32, payload)
        self.set_bpdu_cost("0x" + cost)
        payload = self.remove_bits_from_string(32, payload)
        bridge_priority = self.get_bits_from_string(16, payload)
        self.set_bpdu_bridge_priority("0x" + bridge_priority)
        payload = self.remove_bits_from_string(16, payload)
        bridge_mac = self.get_bits_from_string(48, payload)
        self.set_bpdu_bridge_mac("0x" + bridge_mac)
        payload = self.remove_bits_from_string(48, payload)
        port_id = self.get_bits_from_string(16, payload)
        self.set_bpdu_port_id("0x" + port_id)
        payload = self.remove_bits_from_string(16, payload)
        age = self.get_bits_from_string(16, payload)
        self.set_bpdu_age("0x" + age)
        payload = self.remove_bits_from_string(16, payload)
        max_age = self.get_bits_from_string(16, payload)
        self.set_bpdu_max_age("0x" + max_age)
        payload = self.remove_bits_from_string(16, payload)
        hello_timer = self.get_bits_from_string(16, payload)
        self.set_bpdu_hello_timer("0x" + hello_timer)
        payload = self.remove_bits_from_string(16, payload)
        forward_delay = self.get_bits_from_string(16, payload)
        self.set_bpdu_forward_delay("0x" + forward_delay)
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_bpdu_protocol_id(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_version(), PacketConstants.INTEGER, 8) + " "
        ret_string += self.format_byte_string(self.get_bpdu_message_type(), PacketConstants.INTEGER, 8) + " "
        ret_string += self.format_byte_string(self.get_bpdu_flags(), PacketConstants.INTEGER, 8) + " "
        ret_string += self.format_byte_string(self.get_bpdu_root_priority(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_root_mac(), PacketConstants.ENET_ADDRESS, 48) + " "
        ret_string += self.format_byte_string(self.get_bpdu_cost(), PacketConstants.INTEGER, 32) + " "
        ret_string += self.format_byte_string(self.get_bpdu_bridge_priority(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_bridge_mac(), PacketConstants.ENET_ADDRESS, 48) + " "
        ret_string += self.format_byte_string(self.get_bpdu_port_id(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_age(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_max_age(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_hello_timer(), PacketConstants.INTEGER, 16) + " "
        ret_string += self.format_byte_string(self.get_bpdu_forward_delay(), PacketConstants.INTEGER, 16) + " "
        return ret_string

    @staticmethod
    def compare_bpdu_packet_header(expected, actual, ignore_list, include_list=None, print_results=True,
                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, BpduPacketHeader)
            assert isinstance(actual, BpduPacketHeader)
            if expected.do_i_check_this_field(expected.get_bpdu_protocol_id(), BpduPacketConstants.BPDU_PROTOCOL_ID,
                                              ignore_list, include_list):
                name = "BPDU protocol id : "
                if expected.get_bpdu_protocol_id() != actual.get_bpdu_protocol_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_protocol_id()) + " != " +
                                                      str(actual.get_bpdu_protocol_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_protocol_id()) + " == " +
                                                 str(actual.get_bpdu_protocol_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_version(), BpduPacketConstants.BPDU_VERSION,
                                              ignore_list, include_list):
                name = "BPDU version : "
                if expected.get_bpdu_version() != actual.get_bpdu_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_version()) + " != " +
                                                      str(actual.get_bpdu_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_version()) + " == " +
                                                 str(actual.get_bpdu_version()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_message_type(), BpduPacketConstants.BPDU_MESSAGE_TYPE,
                                              ignore_list, include_list):
                name = "BPDU message type : "
                if expected.get_bpdu_message_type() != actual.get_bpdu_message_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_message_type()) + " != " +
                                                      str(actual.get_bpdu_message_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_message_type()) + " == " +
                                                 str(actual.get_bpdu_message_type()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_flags(), BpduPacketConstants.BPDU_FLAGS,
                                              ignore_list, include_list):
                name = "BPDU flags : "
                if expected.get_bpdu_flags() != actual.get_bpdu_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_flags()) + " != " +
                                                      str(actual.get_bpdu_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_flags()) + " == " +
                                                 str(actual.get_bpdu_flags()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_root_priority(), BpduPacketConstants.BPDU_ROOT_PRIORITY,
                                              ignore_list, include_list):
                name = "BPDU root priority : "
                if expected.get_bpdu_root_priority() != actual.get_bpdu_root_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_root_priority()) + " != " +
                                                      str(actual.get_bpdu_root_priority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_root_priority()) + " == " +
                                                 str(actual.get_bpdu_root_priority()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_root_mac(), BpduPacketConstants.BPDU_ROOT_MAC,
                                              ignore_list, include_list):
                name = "BPDU root mac : "
                if expected.get_bpdu_root_mac() != actual.get_bpdu_root_mac():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_root_mac()) + " != " +
                                                      str(actual.get_bpdu_root_mac()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_root_mac()) + " == " +
                                                 str(actual.get_bpdu_root_mac()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_cost(), BpduPacketConstants.BPDU_COST,
                                              ignore_list, include_list):
                name = "BPDU cost : "
                if expected.get_bpdu_cost() != actual.get_bpdu_cost():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_cost()) + " != " +
                                                      str(actual.get_bpdu_cost()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_cost()) + " == " +
                                                 str(actual.get_bpdu_cost()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_bridge_priority(),
                                              BpduPacketConstants.BPDU_BRIDGE_PRIORITY, ignore_list, include_list):
                name = "BPDU bridge priority : "
                if expected.get_bpdu_bridge_priority() != actual.get_bpdu_bridge_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_bridge_priority()) + " != " +
                                                      str(actual.get_bpdu_bridge_priority()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_bridge_priority()) + " == " +
                                                 str(actual.get_bpdu_bridge_priority()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_bridge_mac(), BpduPacketConstants.BPDU_BRIDGE_MAC,
                                              ignore_list, include_list):
                name = "BPDU bridge mac : "
                if expected.get_bpdu_bridge_mac() != actual.get_bpdu_bridge_mac():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_bridge_mac()) + " != " +
                                                      str(actual.get_bpdu_bridge_mac()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_bridge_mac()) + " == " +
                                                 str(actual.get_bpdu_bridge_mac()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_port_id(), BpduPacketConstants.BPDU_PORT_ID,
                                              ignore_list, include_list):
                name = "BPDU port id : "
                if expected.get_bpdu_port_id() != actual.get_bpdu_port_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_port_id()) + " != " +
                                                      str(actual.get_bpdu_port_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_port_id()) + " == " +
                                                 str(actual.get_bpdu_port_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_age(), BpduPacketConstants.BPDU_AGE,
                                              ignore_list, include_list):
                name = "BPDU age : "
                if expected.get_bpdu_age() != actual.get_bpdu_age():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_age()) + " != " +
                                                      str(actual.get_bpdu_age()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_age()) + " == " +
                                                 str(actual.get_bpdu_age()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_max_age(), BpduPacketConstants.BPDU_MAX_AGE,
                                              ignore_list, include_list):
                name = "BPDU max age : "
                if expected.get_bpdu_max_age() != actual.get_bpdu_max_age():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_max_age()) + " != " +
                                                      str(actual.get_bpdu_max_age()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_max_age()) + " == " +
                                                 str(actual.get_bpdu_max_age()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_hello_timer(), BpduPacketConstants.BPDU_HELLO_TIMER,
                                              ignore_list, include_list):
                name = "BPDU hello timer : "
                if expected.get_bpdu_hello_timer() != actual.get_bpdu_hello_timer():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_hello_timer()) + " != " +
                                                      str(actual.get_bpdu_hello_timer()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_hello_timer()) + " == " +
                                                 str(actual.get_bpdu_hello_timer()) + " Pass")

            if expected.do_i_check_this_field(expected.get_bpdu_forward_delay(), BpduPacketConstants.BPDU_FORWARD_DELAY,
                                              ignore_list, include_list):
                name = "BPDU forward delay : "
                if expected.get_bpdu_forward_delay() != actual.get_bpdu_forward_delay():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_bpdu_forward_delay()) + " != " +
                                                      str(actual.get_bpdu_forward_delay()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_bpdu_forward_delay()) + " == " +
                                                 str(actual.get_bpdu_forward_delay()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with BpduPacketHeader")
        return results


class BpduPacketConstants:
    def __init__(self):
        pass

    BPDU_PROTOCOL_ID = "BPDU_PROTOCOL_ID"
    BPDU_VERSION = "BPDU_VERSION"
    BPDU_MESSAGE_TYPE = "BPDU_MESSAGE_TYPE"
    BPDU_FLAGS = "BPDU_FLAGS"

    BPDU_ROOT_PRIORITY = "BPDU_ROOT_PRIORITY"
    BPDU_ROOT_MAC = "BPDU_ROOT_MAC"
    BPDU_COST = "BPDU_COST"
    BPDU_BRIDGE_PRIORITY = "BPDU_BRIDGE_PRIORITY"
    BPDU_BRIDGE_MAC = "BPDU_BRIDGE_MAC"
    BPDU_PORT_ID = "BPDU_PORT_ID"

    BPDU_AGE = "BPDU_AGE"
    BPDU_MAX_AGE = "BPDU_MAX_AGE"
    BPDU_HELLO_TIMER = "BPDU_HELLO_TIMER"
    BPDU_FORWARD_DELAY = "BPDU_FORWARD_DELAY"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
