import binascii
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import GrePacketHeader, GrePacketConstants
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class ErspanIIIPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    ERSPAN III Packet Header
        # version = 4bits
        # VLAN = 12bits
        # COS = 3bits
        # BSO = 2bits
        # T = 1bits
        # Session ID = 10bits
        # timestamp = 32bits
        # Security Group Tag = 16bits
        # P = 1bits
        # Frame Type = 5bits
        # Hardware ID = 6bits
        # Direction = 1bits
        # Gra Timestamp Granularity = 2bits
        # Optional Subheader = 1bits
        # platform specific ID = 6bits
        # platform specific info 1 = 10bits
        # platform specific info 2 = 16bits
        # platform specific info 3 = 32bits
    """

    def __init__(self):
        self.add_erspaniii_header()
        self.HEADER_SIZE_ERSPANIII = 12  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start ErspanIII version methods
    #  version is a 4 bit INTEGER example: 1
    def set_erspaniii_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_VERSION, version)

    def get_erspaniii_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_VERSION),
            PacketConstants.INTEGER)

    def get_erspaniii_version_hltapi_cmd(self, dummy_dict):
        version = self.get_erspaniii_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end ErspanIII version methods

    # start ErspanIII VLAN methods
    #  vlan is a 12 bit INTEGER example: 1
    def set_erspaniii_vlan(self, vlan, ignore_check=False):
        vlan = self.normalize_value(vlan, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_VLAN, vlan)

    def get_erspaniii_vlan(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_VLAN),
            PacketConstants.INTEGER)

    def get_erspaniii_vlan_hltapi_cmd(self, dummy_dict):
        vlan = self.get_erspaniii_vlan()
        if isinstance(vlan, int):
            vlan = str(vlan)
        if vlan and 'Not Set' not in vlan:
            dummy_dict[TrafficConfigConstants.TEMP_VLAN_CMD] = vlan
    # end ErspanIII VLAN methods

    # start ErspanIII COS methods
    #  cos is a 3 bit INTEGER example: 1
    def set_erspaniii_cos(self, cos, ignore_check=False):
        cos = self.normalize_value(cos, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_COS, cos)

    def get_erspaniii_cos(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_COS),
            PacketConstants.INTEGER)

    def get_erspaniii_cos_hltapi_cmd(self, dummy_dict):
        cos = self.get_erspaniii_cos()
        if isinstance(cos, int):
            cos = str(cos)
        if cos and 'Not Set' not in cos:
            dummy_dict[TrafficConfigConstants.TEMP_COS_CMD] = cos
    # end ErspanIII COS methods

    # start ErspanIII BSO methods
    #  bso is a 2 bit INTEGER example: 1
    def set_erspaniii_bso(self, bso, ignore_check=False):
        bso = self.normalize_value(bso, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_BSO, bso)

    def get_erspaniii_bso(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_BSO),
            PacketConstants.INTEGER)

    def get_erspaniii_bso_hltapi_cmd(self, dummy_dict):
        bso = self.get_erspaniii_bso()
        if isinstance(bso, int):
            bso = str(bso)
        if bso and 'Not Set' not in bso:
            dummy_dict[TrafficConfigConstants.TEMP_BSO_CMD] = bso
    # end ErspanIII BSO methods

    # start ErspanIII T methods
    #  t is a 1 bit INTEGER example: 1
    def set_erspaniii_t(self, t, ignore_check=False):
        t = self.normalize_value(t, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_T, t)

    def get_erspaniii_t(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_T), PacketConstants.INTEGER)

    def get_erspaniii_t_hltapi_cmd(self, dummy_dict):
        t = self.get_erspaniii_t()
        if isinstance(t, int):
            t = str(t)
        if t and 'Not Set' not in t:
            dummy_dict[TrafficConfigConstants.TEMP_T_CMD] = t
    # end ErspanIII T methods

    # start ErspanIII Session ID methods
    #  session_id is a 10 bit INTEGER example: 1
    def set_erspaniii_session_id(self, session_id, ignore_check=False):
        session_id = self.normalize_value(session_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_SESSION_ID, session_id)

    def get_erspaniii_session_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_SESSION_ID),
            PacketConstants.INTEGER)

    def get_erspaniii_session_id_hltapi_cmd(self, dummy_dict):
        session_id = self.get_erspaniii_session_id()
        if isinstance(session_id, int):
            session_id = str(session_id)
        if session_id and 'Not Set' not in session_id:
            dummy_dict[TrafficConfigConstants.TEMP_SESSION_ID_CMD] = session_id
    # end ErspanIII Session ID methods

    # start ErspanIII timestamp methods
    #  timestamp is a 32 bit INTEGER example: 1
    def set_erspaniii_timestamp(self, timestamp, ignore_check=False):
        timestamp = self.normalize_value(timestamp, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_TIMESTAMP, timestamp)

    def get_erspaniii_timestamp(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_TIMESTAMP),
            PacketConstants.INTEGER)

    def get_erspaniii_timestamp_hltapi_cmd(self, dummy_dict):
        timestamp = self.get_erspaniii_timestamp()
        if isinstance(timestamp, int):
            timestamp = str(timestamp)
        if timestamp and 'Not Set' not in timestamp:
            dummy_dict[TrafficConfigConstants.TEMP_TIMESTAMP_CMD] = timestamp
    # end ErspanIII timestamp methods

    # start ErspanIII Security Group Tag methods
    #  security_group_tag is a 16 bit INTEGER example: 1
    def set_erspaniii_security_group_tag(self, security_group_tag, ignore_check=False):
        security_group_tag = self.normalize_value(security_group_tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_SECURITY_GROUP_TAG, security_group_tag)

    def get_erspaniii_security_group_tag(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_SECURITY_GROUP_TAG),
            PacketConstants.INTEGER)

    def get_erspaniii_security_group_tag_hltapi_cmd(self, dummy_dict):
        security_group_tag = self.get_erspaniii_security_group_tag()
        if isinstance(security_group_tag, int):
            security_group_tag = str(security_group_tag)
        if security_group_tag and 'Not Set' not in security_group_tag:
            dummy_dict[TrafficConfigConstants.TEMP_SECURITY_GROUP_TAG_CMD] = security_group_tag
    # end ErspanIII Security Group Tag methods

    # start ErspanIII P methods
    #  p is a 1 bit INTEGER example: 1
    def set_erspaniii_p(self, p, ignore_check=False):
        p = self.normalize_value(p, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_P, p)

    def get_erspaniii_p(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_P), PacketConstants.INTEGER)

    def get_erspaniii_p_hltapi_cmd(self, dummy_dict):
        p = self.get_erspaniii_p()
        if isinstance(p, int):
            p = str(p)
        if p and 'Not Set' not in p:
            dummy_dict[TrafficConfigConstants.TEMP_P_CMD] = p
    # end ErspanIII P methods

    # start ErspanIII Frame Type methods
    #  frame_type is a 5 bit INTEGER example: 1
    def set_erspaniii_frame_type(self, frame_type, ignore_check=False):
        frame_type = self.normalize_value(frame_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_FRAME_TYPE, frame_type)

    def get_erspaniii_frame_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_FRAME_TYPE),
            PacketConstants.INTEGER)

    def get_erspaniii_frame_type_hltapi_cmd(self, dummy_dict):
        frame_type = self.get_erspaniii_frame_type()
        if isinstance(frame_type, int):
            frame_type = str(frame_type)
        if frame_type and 'Not Set' not in frame_type:
            dummy_dict[TrafficConfigConstants.TEMP_FRAME_TYPE_CMD] = frame_type
    # end ErspanIII Frame Type methods

    # start ErspanIII Hardware ID methods
    #  hardware_id is a 6 bit INTEGER example: 1
    def set_erspaniii_hardware_id(self, hardware_id, ignore_check=False):
        hardware_id = self.normalize_value(hardware_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_HARDWARE_ID, hardware_id)

    def get_erspaniii_hardware_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_HARDWARE_ID),
            PacketConstants.INTEGER)

    def get_erspaniii_hardware_id_hltapi_cmd(self, dummy_dict):
        hardware_id = self.get_erspaniii_hardware_id()
        if isinstance(hardware_id, int):
            hardware_id = str(hardware_id)
        if hardware_id and 'Not Set' not in hardware_id:
            dummy_dict[TrafficConfigConstants.TEMP_HARDWARE_ID_CMD] = hardware_id
    # end ErspanIII Hardware ID methods

    # start ErspanIII Direction methods
    #  direction is a 1 bit INTEGER example: 1
    def set_erspaniii_direction(self, direction, ignore_check=False):
        direction = self.normalize_value(direction, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_DIRECTION, direction)

    def get_erspaniii_direction(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_DIRECTION),
            PacketConstants.INTEGER)

    def get_erspaniii_direction_hltapi_cmd(self, dummy_dict):
        direction = self.get_erspaniii_direction()
        if isinstance(direction, int):
            direction = str(direction)
        if direction and 'Not Set' not in direction:
            dummy_dict[TrafficConfigConstants.TEMP_DIRECTION_CMD] = direction
    # end ErspanIII Direction methods

    # start ErspanIII Gra Timestamp Granularity methods
    #  gra_timestamp_granularity is a 2 bit INTEGER example: 1
    def set_erspaniii_gra_timestamp_granularity(self, gra_timestamp_granularity, ignore_check=False):
        gra_timestamp_granularity = self.normalize_value(gra_timestamp_granularity, PacketConstants.INTEGER)
        self.set_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_GRA_TIMESTAMP_GRANULARITY,
            gra_timestamp_granularity)

    def get_erspaniii_gra_timestamp_granularity(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_GRA_TIMESTAMP_GRANULARITY),
            PacketConstants.INTEGER)

    def get_erspaniii_gra_timestamp_granularity_hltapi_cmd(self, dummy_dict):
        gra_timestamp_granularity = self.get_erspaniii_gra_timestamp_granularity()
        if isinstance(gra_timestamp_granularity, int):
            gra_timestamp_granularity = str(gra_timestamp_granularity)
        if gra_timestamp_granularity and 'Not Set' not in gra_timestamp_granularity:
            dummy_dict[TrafficConfigConstants.TEMP_GRA_TIMESTAMP_GRANULARITY_CMD] = gra_timestamp_granularity
    # end ErspanIII Gra Timestamp Granularity methods

    # start ErspanIII Optional Subheader methods
    #  optional_subheader is a 1 bit INTEGER example: 1
    def set_erspaniii_optional_subheader(self, optional_subheader, ignore_check=False):
        optional_subheader = self.normalize_value(optional_subheader, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_OPTIONAL_SUBHEADER, optional_subheader)

    def get_erspaniii_optional_subheader(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_OPTIONAL_SUBHEADER),
            PacketConstants.INTEGER)

    def get_erspaniii_optional_subheader_hltapi_cmd(self, dummy_dict):
        optional_subheader = self.get_erspaniii_optional_subheader()
        if isinstance(optional_subheader, int):
            optional_subheader = str(optional_subheader)
        if optional_subheader and 'Not Set' not in optional_subheader:
            dummy_dict[TrafficConfigConstants.TEMP_OPTIONAL_SUBHEADER_CMD] = optional_subheader
    # end ErspanIII Optional Subheader methods

    # start ErspanIII platform specific ID methods
    #  platform_specific_id is a 6 bit INTEGER example: 1
    def set_erspaniii_platform_specific_id(self, platform_specific_id, ignore_check=False):
        platform_specific_id = self.normalize_value(platform_specific_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_ID, platform_specific_id)

    def get_erspaniii_platform_specific_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_ID),
            PacketConstants.INTEGER)

    def get_erspaniii_platform_specific_id_hltapi_cmd(self, dummy_dict):
        platform_specific_id = self.get_erspaniii_platform_specific_id()
        if isinstance(platform_specific_id, int):
            platform_specific_id = str(platform_specific_id)
        if platform_specific_id and 'Not Set' not in platform_specific_id:
            dummy_dict[TrafficConfigConstants.TEMP_PLATFORM_SPECIFIC_ID_CMD] = platform_specific_id
    # end ErspanIII platform specific ID methods

    # start ErspanIII platform specific info 1 methods
    #  platform_specific_info_1 is a 10 bit INTEGER example: 1
    def set_erspaniii_platform_specific_info_1(self, platform_specific_info_1, ignore_check=False):
        platform_specific_info_1 = self.normalize_value(platform_specific_info_1, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_1, platform_specific_info_1)

    def get_erspaniii_platform_specific_info_1(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_1),
            PacketConstants.INTEGER)

    def get_erspaniii_platform_specific_info_1_hltapi_cmd(self, dummy_dict):
        platform_specific_info_1 = self.get_erspaniii_platform_specific_info_1()
        if isinstance(platform_specific_info_1, int):
            platform_specific_info_1 = str(platform_specific_info_1)
        if platform_specific_info_1 and 'Not Set' not in platform_specific_info_1:
            dummy_dict[TrafficConfigConstants.TEMP_PLATFORM_SPECIFIC_INFO_1_CMD] = platform_specific_info_1
    # end ErspanIII platform specific info 1 methods

    # start ErspanIII platform specific info 2 methods
    #  platform_specific_info_2 is a 16 bit INTEGER example: 1
    def set_erspaniii_platform_specific_info_2(self, platform_specific_info_2, ignore_check=False):
        platform_specific_info_2 = self.normalize_value(platform_specific_info_2, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_2, platform_specific_info_2)

    def get_erspaniii_platform_specific_info_2(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_2),
            PacketConstants.INTEGER)

    def get_erspaniii_platform_specific_info_2_hltapi_cmd(self, dummy_dict):
        platform_specific_info_2 = self.get_erspaniii_platform_specific_info_2()
        if isinstance(platform_specific_info_2, int):
            platform_specific_info_2 = str(platform_specific_info_2)
        if platform_specific_info_2 and 'Not Set' not in platform_specific_info_2:
            dummy_dict[TrafficConfigConstants.TEMP_PLATFORM_SPECIFIC_INFO_2_CMD] = platform_specific_info_2
    # end ErspanIII platform specific info 2 methods

    # start ErspanIII platform specific info 3 methods
    #  platform_specific_info_3 is a 32 bit INTEGER example: 1
    def set_erspaniii_platform_specific_info_3(self, platform_specific_info_3, ignore_check=False):
        platform_specific_info_3 = self.normalize_value(platform_specific_info_3, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_ERSPANIII,
                                  ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_3, platform_specific_info_3)

    def get_erspaniii_platform_specific_info_3(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_ERSPANIII, ErspanIIIPacketConstants.ERSPANIII_PLATFORM_SPECIFIC_INFO_3),
            PacketConstants.INTEGER)

    def get_erspaniii_platform_specific_info_3_hltapi_cmd(self, dummy_dict):
        platform_specific_info_3 = self.get_erspaniii_platform_specific_info_3()
        if isinstance(platform_specific_info_3, int):
            platform_specific_info_3 = str(platform_specific_info_3)
        if platform_specific_info_3 and 'Not Set' not in platform_specific_info_3:
            dummy_dict[TrafficConfigConstants.TEMP_PLATFORM_SPECIFIC_INFO_3_CMD] = platform_specific_info_3
    # end ErspanIII platform specific info 3 methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("version", self.format_int(self.get_erspaniii_version(), 1))
        table.add_row_value("VLAN", self.format_int(self.get_erspaniii_vlan(), 3))
        table.add_row_value("COS", self.format_int(self.get_erspaniii_cos(), 0))
        table.add_row_value("BSO", self.format_int(self.get_erspaniii_bso(), 0))
        table.add_row_value("T", self.format_int(self.get_erspaniii_t(), 0))
        table.add_row_value("Session ID", self.format_int(self.get_erspaniii_session_id(), 2))
        table.add_row_value("timestamp", self.format_int(self.get_erspaniii_timestamp(), 8))
        table.add_row_value("Security Group Tag", self.format_int(self.get_erspaniii_security_group_tag(), 4))
        table.add_row_value("P", self.format_int(self.get_erspaniii_p(), 0))
        table.add_row_value("Frame Type", self.format_int(self.get_erspaniii_frame_type(), 1))
        table.add_row_value("Hardware ID", self.format_int(self.get_erspaniii_hardware_id(), 1))
        table.add_row_value("Direction", self.format_int(self.get_erspaniii_direction(), 0))
        table.add_row_value("Gra Timestamp Granularity",
                            self.format_int(self.get_erspaniii_gra_timestamp_granularity(), 0))
        table.add_row_value("Optional Subheader", self.format_int(self.get_erspaniii_optional_subheader(), 0))
        table.add_row_value("platform specific ID", self.format_int(self.get_erspaniii_platform_specific_id(), 1))
        table.add_row_value("platform specific info 1",
                            self.format_int(self.get_erspaniii_platform_specific_info_1(), 2))
        table.add_row_value("platform specific info 2",
                            self.format_int(self.get_erspaniii_platform_specific_info_2(), 4))
        table.add_row_value("platform specific info 3",
                            self.format_int(self.get_erspaniii_platform_specific_info_3(), 8))
        ret_string = "\n\nERSPANIII HEADER" + table.to_table_string()
        ret_string += "\n\nInner Packet\n" + self.get_gre_inner_packet().to_packet_string()
        return ret_string

    def add_erspaniii_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ERSPANIII)

    def build(self):
        self.add_erspaniii_header()
        self.set_gre_protocol_type(GrePacketConstants.GRE_PROTOCOL_ESPAN_III, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_erspaniii_version_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_vlan_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_cos_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_bso_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_t_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_session_id_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_timestamp_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_security_group_tag_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_p_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_frame_type_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_hardware_id_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_direction_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_gra_timestamp_granularity_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_optional_subheader_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_platform_specific_id_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_platform_specific_info_1_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_platform_specific_info_2_hltapi_cmd(dummy_dict)
        # self.get_erspaniii_platform_specific_info_3_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_erspaniii(self, tgen_type, generator_ref, port_string, stream_id,
                                                             **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_erspaniii(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_erspaniii(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_erspaniii(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
    # update this from the ostinato docs.
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = GrePacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = ErspanIIIPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jet_stream_erspaniii(self, jets_dev, port_string, stream_id, **kwargs):
        """
        :param jets_dev:
        :param port_string:
        :param stream_id:
        :param kwargs:
        :return:
        """
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + ErspanIIIPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_erspaniii_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = ErspanIIIPacketHeader.get_header_bytes(self)
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
        version = self.get_bits_from_string(4, payload)
        self.set_erspaniii_version("0x" + version)
        payload = self.remove_bits_from_string(4, payload)
        vlan = self.get_bits_from_string(12, payload)
        self.set_erspaniii_vlan("0x" + vlan)
        payload = self.remove_bits_from_string(12, payload)

        # start read 16 bits and parse out the values.
        val = self.get_bits_from_string(16, payload)
        payload = self.remove_bits_from_string(16, payload)

        cos = self.get_bits_from_string_with_positions(val, 15, 3)
        self.set_erspaniii_cos(cos)
        bso = self.get_bits_from_string_with_positions(val, 12, 2)
        self.set_erspaniii_bso(bso)
        t = self.get_bits_from_string_with_positions(val, 11, 1)
        self.set_erspaniii_t(t)
        session_id = self.get_bits_from_string_with_positions(val, 10, 10)
        self.set_erspaniii_session_id(session_id)
        # end read 16 bits and parse out the values.

        timestamp = self.get_bits_from_string(32, payload)
        self.set_erspaniii_timestamp("0x" + timestamp)
        payload = self.remove_bits_from_string(32, payload)
        security_group_tag = self.get_bits_from_string(16, payload)
        self.set_erspaniii_security_group_tag("0x" + security_group_tag)
        payload = self.remove_bits_from_string(16, payload)

        # start read 16 bits and parse out the values.
        val = self.get_bits_from_string(16, payload)
        payload = self.remove_bits_from_string(16, payload)

        p = self.get_bits_from_string_with_positions(val, 15, 1)
        self.set_erspaniii_p(cos)
        frame_type = self.get_bits_from_string_with_positions(val, 14, 5)
        self.set_erspaniii_frame_type(frame_type)
        hardware_id = self.get_bits_from_string_with_positions(val, 9, 6)
        self.set_erspaniii_hardware_id(hardware_id)
        direction = self.get_bits_from_string_with_positions(val, 3, 1)
        self.set_erspaniii_direction(direction)
        gra_timestamp_granularity = self.get_bits_from_string_with_positions(val, 2, 2)
        self.set_erspaniii_gra_timestamp_granularity(gra_timestamp_granularity)
        optional_subheader = self.get_bits_from_string_with_positions(val, 0, 1)
        self.set_erspaniii_optional_subheader(optional_subheader)
        # end read 16 bits and parse out the values.

        if 1 == optional_subheader:
            # start read 16 bits and parse out the values.
            val = self.get_bits_from_string(16, payload)
            payload = self.remove_bits_from_string(16, payload)

            platform_specific_id = self.get_bits_from_string_with_positions(val, 15, 6)
            self.set_erspaniii_platform_specific_id(platform_specific_id)
            platform_specific_info_1 = self.get_bits_from_string_with_positions(val, 9, 10)
            self.set_erspaniii_platform_specific_info_1(platform_specific_info_1)
            # end read 16 bits and parse out the values.

            platform_specific_info_2 = self.get_bits_from_string(16, payload)
            self.set_erspaniii_platform_specific_info_2("0x" + platform_specific_info_2)
            payload = self.remove_bits_from_string(16, payload)
            platform_specific_info_3 = self.get_bits_from_string(32, payload)
            self.set_erspaniii_platform_specific_info_3("0x" + platform_specific_info_3)
            payload = self.remove_bits_from_string(32, payload)
        packet = EthernetPacket()
        packet.set_payload(payload)
        self.set_gre_inner_packet(packet)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_erspaniii_version(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_erspaniii_vlan(), PacketConstants.INTEGER, 12)

        # start read 16 bits and parse out the values.
        val = 0
        val = self.shift_bits_from_string_with_positions(val, 15, 3, self.get_erspaniii_cos())
        val = self.shift_bits_from_string_with_positions(val, 12, 2, self.get_erspaniii_bso())
        val = self.shift_bits_from_string_with_positions(val, 11, 1, self.get_erspaniii_t())
        val = self.shift_bits_from_string_with_positions(val, 10, 10, self.get_erspaniii_session_id())
        ret_string += self.format_byte_string(val, PacketConstants.INTEGER, 16)
        # end read 16 bits and parse out the values.

        ret_string += self.format_byte_string(self.get_erspaniii_timestamp(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_erspaniii_security_group_tag(), PacketConstants.INTEGER, 16)

        # start read 16 bits and parse out the values.
        val = 0
        val = self.shift_bits_from_string_with_positions(val, 15, 1, self.get_erspaniii_p())
        val = self.shift_bits_from_string_with_positions(val, 14, 5, self.get_erspaniii_frame_type())
        val = self.shift_bits_from_string_with_positions(val, 9, 6, self.get_erspaniii_hardware_id())
        val = self.shift_bits_from_string_with_positions(val, 3, 1, self.get_erspaniii_direction())
        val = self.shift_bits_from_string_with_positions(val, 2, 2, self.get_erspaniii_gra_timestamp_granularity())
        val = self.shift_bits_from_string_with_positions(val, 1, 1, self.get_erspaniii_optional_subheader())
        ret_string += self.format_byte_string(val, PacketConstants.INTEGER, 16)
        # end read 16 bits and parse out the values.

        if "1" == self.get_erspaniii_optional_subheader():
            # start read 16 bits and parse out the values.
            val = 0
            val = self.shift_bits_from_string_with_positions(val, 15, 6, self.get_erspaniii_platform_specific_id())
            val = self.shift_bits_from_string_with_positions(val, 9, 10, self.get_erspaniii_platform_specific_info_1())
            ret_string += self.format_byte_string(val, PacketConstants.INTEGER, 16)
            # end read 16 bits and parse out the values.

            ret_string += self.format_byte_string(self.get_erspaniii_platform_specific_info_2(),
                                                  PacketConstants.INTEGER, 16)
            ret_string += self.format_byte_string(self.get_erspaniii_platform_specific_info_3(),
                                                  PacketConstants.INTEGER, 32)
        ret_string += self.get_gre_inner_packet().get_bytes()
        return ret_string

    @staticmethod
    def compare_erspaniii_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                        print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, ErspanIIIPacketHeader)
            assert isinstance(actual, ErspanIIIPacketHeader)
            if expected.do_i_check_this_field(expected.get_erspaniii_version(), ignore_list, include_list):
                name = "ERSPANIII version : "
                if expected.get_erspaniii_version() != actual.get_erspaniii_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_version()) + " != " +
                                                      str(actual.get_erspaniii_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_version()) + " == " +
                                                 str(actual.get_erspaniii_version()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_vlan(), ignore_list, include_list):
                name = "ERSPANIII vlan : "
                if expected.get_erspaniii_vlan() != actual.get_erspaniii_vlan():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_vlan()) + " != " +
                                                      str(actual.get_erspaniii_vlan()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_vlan()) + " == " +
                                                 str(actual.get_erspaniii_vlan()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_cos(), ignore_list, include_list):
                name = "ERSPANIII cos : "
                if expected.get_erspaniii_cos() != actual.get_erspaniii_cos():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_cos()) + " != " +
                                                      str(actual.get_erspaniii_cos()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_cos()) + " == " +
                                                 str(actual.get_erspaniii_cos()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_bso(), ignore_list, include_list):
                name = "ERSPANIII bso : "
                if expected.get_erspaniii_bso() != actual.get_erspaniii_bso():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_bso()) + " != " +
                                                      str(actual.get_erspaniii_bso()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_bso()) + " == " +
                                                 str(actual.get_erspaniii_bso()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_t(), ignore_list, include_list):
                name = "ERSPANIII t : "
                if expected.get_erspaniii_t() != actual.get_erspaniii_t():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_t()) + " != " +
                                                      str(actual.get_erspaniii_t()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_t()) + " == " +
                                                 str(actual.get_erspaniii_t()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_session_id(), ignore_list, include_list):
                name = "ERSPANIII session id : "
                if expected.get_erspaniii_session_id() != actual.get_erspaniii_session_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_session_id()) + " != " +
                                                      str(actual.get_erspaniii_session_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_session_id()) + " == " +
                                                 str(actual.get_erspaniii_session_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_timestamp(), ignore_list, include_list):
                name = "ERSPANIII timestamp : "
                if expected.get_erspaniii_timestamp() != actual.get_erspaniii_timestamp():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_timestamp()) + " != " +
                                                      str(actual.get_erspaniii_timestamp()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_timestamp()) + " == " +
                                                 str(actual.get_erspaniii_timestamp()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_security_group_tag(), ignore_list, include_list):
                name = "ERSPANIII security group tag : "
                if expected.get_erspaniii_security_group_tag() != actual.get_erspaniii_security_group_tag():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_security_group_tag()) + " != " +
                                                      str(actual.get_erspaniii_security_group_tag()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_security_group_tag()) + " == " +
                                                 str(actual.get_erspaniii_security_group_tag()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_p(), ignore_list, include_list):
                name = "ERSPANIII p : "
                if expected.get_erspaniii_p() != actual.get_erspaniii_p():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_p()) + " != " +
                                                      str(actual.get_erspaniii_p()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_p()) + " == " +
                                                 str(actual.get_erspaniii_p()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_frame_type(), ignore_list, include_list):
                name = "ERSPANIII frame type : "
                if expected.get_erspaniii_frame_type() != actual.get_erspaniii_frame_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_frame_type()) + " != " +
                                                      str(actual.get_erspaniii_frame_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_frame_type()) + " == " +
                                                 str(actual.get_erspaniii_frame_type()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_hardware_id(), ignore_list, include_list):
                name = "ERSPANIII hardware id : "
                if expected.get_erspaniii_hardware_id() != actual.get_erspaniii_hardware_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_hardware_id()) + " != " +
                                                      str(actual.get_erspaniii_hardware_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_hardware_id()) + " == " +
                                                 str(actual.get_erspaniii_hardware_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_direction(), ignore_list, include_list):
                name = "ERSPANIII direction : "
                if expected.get_erspaniii_direction() != actual.get_erspaniii_direction():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_direction()) + " != " +
                                                      str(actual.get_erspaniii_direction()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_direction()) + " == " +
                                                 str(actual.get_erspaniii_direction()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_gra_timestamp_granularity(),
                                              ignore_list, include_list):
                name = "ERSPANIII gra timestamp granularity : "
                if expected.get_erspaniii_gra_timestamp_granularity() != \
                        actual.get_erspaniii_gra_timestamp_granularity():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_gra_timestamp_granularity()) +
                                                      " != " + str(actual.get_erspaniii_gra_timestamp_granularity()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_gra_timestamp_granularity()) +
                                                 " == " + str(actual.get_erspaniii_gra_timestamp_granularity()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_optional_subheader(), ignore_list, include_list):
                name = "ERSPANIII optional subheader : "
                if expected.get_erspaniii_optional_subheader() != actual.get_erspaniii_optional_subheader():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_optional_subheader()) + " != " +
                                                      str(actual.get_erspaniii_optional_subheader()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_optional_subheader()) + " == " +
                                                 str(actual.get_erspaniii_optional_subheader()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_platform_specific_id(), ignore_list, include_list):
                name = "ERSPANIII platform specific id : "
                if expected.get_erspaniii_platform_specific_id() != actual.get_erspaniii_platform_specific_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_platform_specific_id()) + " != " +
                                                      str(actual.get_erspaniii_platform_specific_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_platform_specific_id()) + " == " +
                                                 str(actual.get_erspaniii_platform_specific_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_platform_specific_info_1(),
                                              ignore_list, include_list):
                name = "ERSPANIII platform specific info 1 : "
                if expected.get_erspaniii_platform_specific_info_1() != actual.get_erspaniii_platform_specific_info_1():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_platform_specific_info_1()) + " != " +
                                                      str(actual.get_erspaniii_platform_specific_info_1()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_platform_specific_info_1()) +
                                                 " == " + str(actual.get_erspaniii_platform_specific_info_1()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_platform_specific_info_2(),
                                              ignore_list, include_list):
                name = "ERSPANIII platform specific info 2 : "
                if expected.get_erspaniii_platform_specific_info_2() != actual.get_erspaniii_platform_specific_info_2():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_platform_specific_info_2()) +
                                                      " != " + str(actual.get_erspaniii_platform_specific_info_2()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_platform_specific_info_2()) +
                                                 " == " + str(actual.get_erspaniii_platform_specific_info_2()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_erspaniii_platform_specific_info_3(),
                                              ignore_list, include_list):
                name = "ERSPANIII platform specific info 3 : "
                if expected.get_erspaniii_platform_specific_info_3() != actual.get_erspaniii_platform_specific_info_3():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_erspaniii_platform_specific_info_3()) + " != " +
                                                      str(actual.get_erspaniii_platform_specific_info_3()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_erspaniii_platform_specific_info_3()) +
                                                 " == " + str(actual.get_erspaniii_platform_specific_info_3()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_gre_inner_packet(), ErspanIIIPacketHeader.GRE_INNER_PACKET,
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
                PacketObject.logger.log_error("Error with ErspanIIIPacketHeader")
        return results


class ErspanIIIPacketConstants:
    def __init__(self):
        pass

    ERSPANIII_VERSION = "ERSPANIII_VERSION"
    ERSPANIII_VLAN = "ERSPANIII_VLAN"
    ERSPANIII_COS = "ERSPANIII_COS"
    ERSPANIII_BSO = "ERSPANIII_BSO"
    ERSPANIII_T = "ERSPANIII_T"
    ERSPANIII_SESSION_ID = "ERSPANIII_SESSION_ID"
    ERSPANIII_TIMESTAMP = "ERSPANIII_TIMESTAMP"
    ERSPANIII_SECURITY_GROUP_TAG = "ERSPANIII_SECURITY_GROUP_TAG"
    ERSPANIII_P = "ERSPANIII_P"
    ERSPANIII_FRAME_TYPE = "ERSPANIII_FRAME_TYPE"
    ERSPANIII_HARDWARE_ID = "ERSPANIII_HARDWARE_ID"
    ERSPANIII_DIRECTION = "ERSPANIII_DIRECTION"
    ERSPANIII_GRA_TIMESTAMP_GRANULARITY = "ERSPANIII_GRA_TIMESTAMP_GRANULARITY"
    ERSPANIII_OPTIONAL_SUBHEADER = "ERSPANIII_OPTIONAL_SUBHEADER"
    ERSPANIII_PLATFORM_SPECIFIC_ID = "ERSPANIII_PLATFORM_SPECIFIC_ID"
    ERSPANIII_PLATFORM_SPECIFIC_INFO_1 = "ERSPANIII_PLATFORM_SPECIFIC_INFO_1"
    ERSPANIII_PLATFORM_SPECIFIC_INFO_2 = "ERSPANIII_PLATFORM_SPECIFIC_INFO_2"
    ERSPANIII_PLATFORM_SPECIFIC_INFO_3 = "ERSPANIII_PLATFORM_SPECIFIC_INFO_3"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
