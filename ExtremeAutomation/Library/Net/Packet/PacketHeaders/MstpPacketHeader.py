import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject, PacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class MstpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    MSTP Packet Header
        # version 1 length = 8bits
        # version 3 length = 16bits
        # version 3 id format = 8bits
        # version 3 name = 256bits
        # version 3 revision = 16bits
        # version 3 digest = 128bits
        # version 3 cist internal root path cost = 32bits
        # version 3 cist bridge internal priority = 16bits
        # version 3 cist bridge internal system id = 48bits
        # version 3 cist remaining hops = 8bits
    """

    def __init__(self):
        self.add_mstp_header()
        self.set_mstid_num(0, True)
        self.HEADER_SIZE_MSTP = ((8 + 16 + 8 + 256 + 16 + 128 + 32 + 16 + 48 + 8) // 8)

    def get_mstid_num(self):
        return self.num_mstids

    def set_mstid_num(self, num_mstids, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_MSTID_NUM, ignore_check)
        self.num_mstids = NumberUtils.to_integer_value(num_mstids)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_MSTID_NUM,
                                  num_mstids)

    def add_mstid_entry(self):
        self.set_mstid_num(self.num_mstids + 1)

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Mstp version 1 length methods
    #  version_1_length is a 8 bit INTEGER example: 1
    def set_mstp_version_1_length(self, version_1_length, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_1_LENGTH, ignore_check)
        version_1_length = self.normalize_value(version_1_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_1_LENGTH,
                                  version_1_length)

    def get_mstp_version_1_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_1_LENGTH), PacketConstants.INTEGER)

    def get_mstp_version_1_length_hltapi_cmd(self, dummy_dict):
        version_1_length = self.get_mstp_version_1_length()
        if isinstance(version_1_length, int):
            version_1_length = str(version_1_length)
        if version_1_length and 'Not Set' not in version_1_length:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_1_LENGTH_CMD] = version_1_length
    # end Mstp version 1 length methods

    # start Mstp version 3 length methods
    #  version_3_length is a 16 bit INTEGER example: 1
    # this is 64 + (16 * num MSTI entries)
    def set_mstp_version_3_length(self, version_3_length, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_LENGTH, ignore_check)
        version_3_length = self.normalize_value(version_3_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_LENGTH,
                                  version_3_length)

    def get_mstp_version_3_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_LENGTH), PacketConstants.INTEGER)

    def get_mstp_version_3_length_hltapi_cmd(self, dummy_dict):
        version_3_length = self.get_mstp_version_3_length()
        if isinstance(version_3_length, int):
            version_3_length = str(version_3_length)
        if version_3_length and 'Not Set' not in version_3_length:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_LENGTH_CMD] = version_3_length
    # end Mstp version 3 length methods

    # start Mstp version 3 id format methods
    #  version_3_id_format is a 8 bit INTEGER example: 1
    def set_mstp_version_3_id_format(self, version_3_id_format, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_ID_FORMAT, ignore_check)
        version_3_id_format = self.normalize_value(version_3_id_format, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_ID_FORMAT,
                                  version_3_id_format)

    def get_mstp_version_3_id_format(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_ID_FORMAT),
            PacketConstants.INTEGER)

    def get_mstp_version_3_id_format_hltapi_cmd(self, dummy_dict):
        version_3_id_format = self.get_mstp_version_3_id_format()
        if isinstance(version_3_id_format, int):
            version_3_id_format = str(version_3_id_format)
        if version_3_id_format and 'Not Set' not in version_3_id_format:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_ID_FORMAT_CMD] = version_3_id_format
    # end Mstp version 3 id format methods

    # start Mstp version 3 name methods
    #  version_3_name is a 256 bit ASCII_STRING example: 1
    def set_mstp_version_3_name(self, version_3_name_ascii_string, ascii_string=True, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_NAME, ignore_check)
        if not ascii_string:
            version_3_name_ascii_string = version_3_name_ascii_string.replace(" ", "").decode('hex')
            while version_3_name_ascii_string.endswith("00"):
                version_3_name_ascii_string = version_3_name_ascii_string[:-2]
        # version_3_name_ascii_string = self.normalize_value(version_3_name_ascii_string, PacketConstants.ASCII_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_NAME,
                                  version_3_name_ascii_string)

    def get_mstp_version_3_name(self, ascii_string=True):
        if ascii_string:
            return self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                             MstpPacketConstants.MSTP_VERSION_3_NAME)
        else:
            value = self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                              MstpPacketConstants.MSTP_VERSION_3_NAME)
            return value  # .encode('hex')

    def get_mstp_version_3_name_hltapi_cmd(self, dummy_dict):
        version_3_name = self.get_mstp_version_3_name()
        if version_3_name and 'Not Set' not in version_3_name:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_NAME_CMD] = version_3_name
    # end Mstp version 3 name methods

    # start Mstp version 3 revision methods
    #  version_3_revision is a 16 bit INTEGER example: 1
    def set_mstp_version_3_revision(self, version_3_revision, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_REVISION, ignore_check)
        version_3_revision = self.normalize_value(version_3_revision, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_REVISION,
                                  version_3_revision)

    def get_mstp_version_3_revision(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_REVISION),
            PacketConstants.INTEGER)

    def get_mstp_version_3_revision_hltapi_cmd(self, dummy_dict):
        version_3_revision = self.get_mstp_version_3_revision()
        if isinstance(version_3_revision, int):
            version_3_revision = str(version_3_revision)
        if version_3_revision and 'Not Set' not in version_3_revision:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_REVISION_CMD] = version_3_revision
    # end Mstp version 3 revision methods

    # start Mstp version 3 digest methods
    #  version_3_digest is a 128 bit HEX_STRING example: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    def set_mstp_version_3_digest(self, version_3_digest, hex_string=True, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_DIGEST, ignore_check)
        version_3_digest = self.normalize_value(version_3_digest, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_DIGEST,
                                  version_3_digest)

    def get_mstp_version_3_digest(self, hex_string=True):
        if hex_string:
            return self.normalize_value(self.get_packet_component(
                PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_DIGEST),
                PacketConstants.HEX_STRING)
        else:
            value = self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                              MstpPacketConstants.MSTP_VERSION_3_NAME)
            return value.replace(" ", "").decode('hex')

    def get_mstp_version_3_digest_hltapi_cmd(self, dummy_dict):
        version_3_digest = self.get_mstp_version_3_digest()
        if version_3_digest and 'Not Set' not in version_3_digest:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_DIGEST_CMD] = version_3_digest
    # end Mstp version 3 digest methods

    # start Mstp version 3 cist internal root path cost methods
    #  version_3_cist_internal_root_path_cost is a 32 bit INTEGER example: 1
    def set_mstp_version_3_cist_internal_root_path_cost(self, version_3_cist_internal_root_path_cost,
                                                        ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST,
                                                        ignore_check)
        version_3_cist_internal_root_path_cost = self.normalize_value(version_3_cist_internal_root_path_cost,
                                                                      PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST,
                                  version_3_cist_internal_root_path_cost)

    def get_mstp_version_3_cist_internal_root_path_cost(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST),
            PacketConstants.INTEGER)

    def get_mstp_version_3_cist_internal_root_path_cost_hltapi_cmd(self, dummy_dict):
        version_3_cist_internal_root_path_cost = self.get_mstp_version_3_cist_internal_root_path_cost()
        if isinstance(version_3_cist_internal_root_path_cost, int):
            version_3_cist_internal_root_path_cost = str(version_3_cist_internal_root_path_cost)
        if version_3_cist_internal_root_path_cost and 'Not Set' not in version_3_cist_internal_root_path_cost:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST_CMD] = \
                version_3_cist_internal_root_path_cost
    # end Mstp version 3 cist internal root path cost methods

    # start Mstp version 3 cist bridge internal priority methods
    #  version_3_cist_bridge_internal_priority is a 16 bit INTEGER example: 1
    def set_mstp_version_3_cist_bridge_internal_priority(self, version_3_cist_bridge_internal_priority,
                                                         ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY, ignore_check)
        version_3_cist_bridge_internal_priority = self.normalize_value(version_3_cist_bridge_internal_priority,
                                                                       PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY,
                                  version_3_cist_bridge_internal_priority)

    def get_mstp_version_3_cist_bridge_internal_priority(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY),
            PacketConstants.INTEGER)

    def get_mstp_version_3_cist_bridge_internal_priority_hltapi_cmd(self, dummy_dict):
        version_3_cist_bridge_internal_priority = self.get_mstp_version_3_cist_bridge_internal_priority()
        if isinstance(version_3_cist_bridge_internal_priority, int):
            version_3_cist_bridge_internal_priority = str(version_3_cist_bridge_internal_priority)
        if version_3_cist_bridge_internal_priority and 'Not Set' not in version_3_cist_bridge_internal_priority:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY_CMD] = \
                version_3_cist_bridge_internal_priority
    # end Mstp version 3 cist bridge internal priority methods

    # start Mstp version 3 cist bridge internal system id methods
    #  version_3_cist_bridge_internal_system_id is a 48 bit ENET_ADDRESS example: 00:33:44:55:66:44
    def set_mstp_version_3_cist_bridge_internal_system_id(self, version_3_cist_bridge_internal_system_id,
                                                          ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID, ignore_check)
        version_3_cist_bridge_internal_system_id = self.normalize_value(version_3_cist_bridge_internal_system_id,
                                                                        PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID,
                                  version_3_cist_bridge_internal_system_id)

    def get_mstp_version_3_cist_bridge_internal_system_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID),
            PacketConstants.ENET_ADDRESS)

    def get_mstp_version_3_cist_bridge_internal_system_id_hltapi_cmd(self, dummy_dict):
        version_3_cist_bridge_internal_system_id = self.get_mstp_version_3_cist_bridge_internal_system_id()
        if version_3_cist_bridge_internal_system_id and 'Not Set' not in version_3_cist_bridge_internal_system_id:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID_CMD] = \
                version_3_cist_bridge_internal_system_id
    # end Mstp version 3 cist bridge internal system id methods

    # start Mstp version 3 cist remaining hops methods
    #  version_3_cist_remaining_hops is a 8 bit INTEGER example: 1
    def set_mstp_version_3_cist_remaining_hops(self, version_3_cist_remaining_hops, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_CIST_REMAINING_HOPS,
                                                        ignore_check)
        version_3_cist_remaining_hops = self.normalize_value(version_3_cist_remaining_hops, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_CIST_REMAINING_HOPS, version_3_cist_remaining_hops)

    def get_mstp_version_3_cist_remaining_hops(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_CIST_REMAINING_HOPS),
            PacketConstants.INTEGER)

    def get_mstp_version_3_cist_remaining_hops_hltapi_cmd(self, dummy_dict):
        version_3_cist_remaining_hops = self.get_mstp_version_3_cist_remaining_hops()
        if isinstance(version_3_cist_remaining_hops, int):
            version_3_cist_remaining_hops = str(version_3_cist_remaining_hops)
        if version_3_cist_remaining_hops and 'Not Set' not in version_3_cist_remaining_hops:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_3_CIST_REMAINING_HOPS_CMD] = version_3_cist_remaining_hops
    # end Mstp version 3 cist remaining hops methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_flags(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_MSTID_FLAG + " " +
                                                        str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_FLAG + " " + str(mstid_id),
                                  flag)

    def get_mstp_version_3_mstid_flags(self, mstid_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                                              MstpPacketConstants.MSTP_VERSION_3_MSTID_FLAG + " " +
                                                              str(mstid_id)), PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

        # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_priority(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_MSTID_PRIORITY + " " +
                                                        str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_PRIORITY + " " + str(mstid_id),
                                  flag)

    def get_mstp_version_3_mstid_priority(self, mstid_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                                              MstpPacketConstants.MSTP_VERSION_3_MSTID_PRIORITY + " " +
                                                              str(mstid_id)), PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

        # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_mstid(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_MSTID_MSTID + " " +
                                                        str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_MSTID + " " + str(mstid_id), flag)

    def get_mstp_version_3_mstid_mstid(self, mstid_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                                              MstpPacketConstants.MSTP_VERSION_3_MSTID_MSTID + " " +
                                                              str(mstid_id)), PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_regional_root(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(MstpPacketConstants.MSTP_VERSION_3_MSTID_REGIONAL_ROOT + " " +
                                                        str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.ENET_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_REGIONAL_ROOT + " " + str(mstid_id), flag)

    def get_mstp_version_3_mstid_regional_root(self, mstid_id):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                                              MstpPacketConstants.MSTP_VERSION_3_MSTID_REGIONAL_ROOT +
                                                              " " + str(mstid_id)), PacketConstants.ENET_ADDRESS)
    # end Mstp mstp_version_3_mstid_flags methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_internal_root_path_cost(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST + " " + str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST + " " +
                                  str(mstid_id), flag)

    def get_mstp_version_3_mstid_internal_root_path_cost(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP,
            MstpPacketConstants.MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST + " " + str(mstid_id)),
            PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_bridge_identifier_priority(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY + " " + str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY + " " +
                                  str(mstid_id), flag)

    def get_mstp_version_3_mstid_bridge_identifier_priority(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP,
            MstpPacketConstants.MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY + " " + str(mstid_id)),
            PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_port_identifier_priority(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY + " " + str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY + " " +
                                  str(mstid_id), flag)

    def get_mstp_version_3_mstid_port_identifier_priority(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP,
            MstpPacketConstants.MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY + " " + str(mstid_id)),
            PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

    # start Mstp version 3 cist remaining hops methods
    #  mstp_version_3_mstid_flags is a 8 bit INTEGER example: 1
    def set_mstp_version_3_mstid_remaining_hops(self, flag, mstid_id, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(
            MstpPacketConstants.MSTP_VERSION_3_MSTID_REMAINING_HOPS + " " + str(mstid_id), ignore_check)
        flag = self.normalize_value(flag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MSTP,
                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_REMAINING_HOPS + " " + str(mstid_id), flag)

    def get_mstp_version_3_mstid_remaining_hops(self, mstid_id):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MSTP, MstpPacketConstants.MSTP_VERSION_3_MSTID_REMAINING_HOPS + " " +
            str(mstid_id)), PacketConstants.INTEGER)
    # end Mstp mstp_version_3_mstid_flags methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("version 1 length", self.format_int(self.get_mstp_version_1_length(), 2))
        table.add_row_value("version 3 length", self.format_int(self.get_mstp_version_3_length(), 4))
        table.add_row_value("version 3 id format", self.format_int(self.get_mstp_version_3_id_format(), 2))
        table.add_row_value("version 3 name", self.get_mstp_version_3_name())
        table.add_row_value("version 3 revision", self.format_int(self.get_mstp_version_3_revision(), 4))
        table.add_row_value("version 3 digest", self.get_mstp_version_3_digest())
        table.add_row_value("version 3 cist internal root path cost",
                            self.format_int(self.get_mstp_version_3_cist_internal_root_path_cost(), 8))
        table.add_row_value("version 3 cist bridge internal priority",
                            self.format_int(self.get_mstp_version_3_cist_bridge_internal_priority(), 4))
        table.add_row_value("version 3 cist bridge internal system id",
                            self.get_mstp_version_3_cist_bridge_internal_system_id())
        table.add_row_value("version 3 cist remaining hops",
                            self.format_int(self.get_mstp_version_3_cist_remaining_hops(), 2))
        ret_string = "\n\nMSTP HEADER" + table.to_table_string()
        return ret_string + self.to_packet_string_tags()

    def to_packet_string_tags(self):
        table = TableFormatter()
        for index in range(1, NumberUtils.to_integer_value(self.get_mstid_num()) + 1):
            table.add_row_value("Row", self.format_int(index, 1))
            table.add_row_value("Flags", self.format_int(self.get_mstp_version_3_mstid_flags(index), 1))
            table.add_row_value("Priority", self.format_int(self.get_mstp_version_3_mstid_priority(index), 1))
            table.add_row_value("MSTID", self.format_int(self.get_mstp_version_3_mstid_mstid(index), 3))
            table.add_row_value("Regional Root", str(self.get_mstp_version_3_mstid_regional_root(index)))
            table.add_row_value("Internal Root Path Cost",
                                self.format_int(self.get_mstp_version_3_mstid_internal_root_path_cost(index), 4))
            table.add_row_value("Bridge ID Priority",
                                self.format_int(self.get_mstp_version_3_mstid_bridge_identifier_priority(index), 4))
            table.add_row_value("Port ID Priority",
                                self.format_int(self.get_mstp_version_3_mstid_port_identifier_priority(index), 4))
            table.add_row_value("Remaining Hops",
                                self.format_int(self.get_mstp_version_3_mstid_remaining_hops(index), 4))
            index += 1
        return table.to_table_string()

    def add_mstp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_MSTP)

    def build(self):
        self.add_mstp_header()
        self.set_bpdu_version(0x03, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_mstp_version_1_length_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_length_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_id_format_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_name_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_revision_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_digest_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_cist_internal_root_path_cost_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_cist_bridge_internal_priority_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_cist_bridge_internal_system_id_hltapi_cmd(dummy_dict)
        # self.get_mstp_version_3_cist_remaining_hops_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_mstp(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_mstp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_mstp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_mstp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = MstpPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    def config_jets_stream_mstp(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + MstpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_mstp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
    # ### put some IxTclHal info here.
        payload = BpduPacketHeader.get_header_bytes(self) + " " + MstpPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_mstp_api_commands(self, port_name_stream):
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
        version_1_length = self.get_bits_from_string(8, payload)
        self.set_mstp_version_1_length("0x" + version_1_length)
        payload = self.remove_bits_from_string(8, payload)
        version_3_length = self.get_bits_from_string(16, payload)
        self.set_mstp_version_3_length("0x" + version_3_length)
        payload = self.remove_bits_from_string(16, payload)
        version_3_id_format = self.get_bits_from_string(8, payload)
        self.set_mstp_version_3_id_format("0x" + version_3_id_format)
        payload = self.remove_bits_from_string(8, payload)
        version_3_name = self.get_bits_from_string(256, payload)
        while version_3_name.endswith("00"):
            version_3_name = version_3_name[:-2]
        self.set_mstp_version_3_name(version_3_name, True)
        payload = self.remove_bits_from_string(256, payload)
        version_3_revision = self.get_bits_from_string(16, payload)
        self.set_mstp_version_3_revision("0x" + version_3_revision)
        payload = self.remove_bits_from_string(16, payload)
        version_3_digest = self.get_bits_from_string(128, payload)
        self.set_mstp_version_3_digest(version_3_digest)
        payload = self.remove_bits_from_string(128, payload)
        version_3_cist_internal_root_path_cost = self.get_bits_from_string(32, payload)
        self.set_mstp_version_3_cist_internal_root_path_cost("0x" + version_3_cist_internal_root_path_cost)
        payload = self.remove_bits_from_string(32, payload)
        version_3_cist_bridge_internal_priority = self.get_bits_from_string(16, payload)
        self.set_mstp_version_3_cist_bridge_internal_priority("0x" + version_3_cist_bridge_internal_priority)
        payload = self.remove_bits_from_string(16, payload)
        version_3_cist_bridge_internal_system_id = self.get_bits_from_string(48, payload)
        self.set_mstp_version_3_cist_bridge_internal_system_id("0x" + version_3_cist_bridge_internal_system_id)
        payload = self.remove_bits_from_string(48, payload)
        version_3_cist_remaining_hops = self.get_bits_from_string(8, payload)
        self.set_mstp_version_3_cist_remaining_hops("0x" + version_3_cist_remaining_hops)
        payload = self.remove_bits_from_string(8, payload)
        self.payload = payload
        if self.get_mstp_version_3_length() > 0:
            size = int((self.get_mstp_version_3_length() - 64) / 16)
            self.set_mstid_num(size)
            index = 1
            for index in range(1, self.get_mstid_num() + 1):
                mstp_version_3_mstid_flags = self.get_bits_from_string(8, payload)
                self.set_mstp_version_3_mstid_flags("0x" + mstp_version_3_mstid_flags, index)
                payload = self.remove_bits_from_string(8, payload)

                get_mstp_version_3_mstid_priority = self.get_bits_from_string(4, payload)
                self.set_mstp_version_3_mstid_priority("0x" + get_mstp_version_3_mstid_priority, index)
                payload = self.remove_bits_from_string(4, payload)

                get_mstp_version_3_mstid_mstid = self.get_bits_from_string(12, payload)
                self.set_mstp_version_3_mstid_mstid("0x" + get_mstp_version_3_mstid_mstid, index)
                payload = self.remove_bits_from_string(12, payload)

                get_mstp_version_3_mstid_regional_root = self.get_bits_from_string(48, payload)
                self.set_mstp_version_3_mstid_regional_root("0x" + get_mstp_version_3_mstid_regional_root, index)
                payload = self.remove_bits_from_string(48, payload)

                get_mstp_version_3_mstid_internal_root_path_cost = self.get_bits_from_string(32, payload)
                self.set_mstp_version_3_mstid_internal_root_path_cost(
                    "0x" + get_mstp_version_3_mstid_internal_root_path_cost, index)
                payload = self.remove_bits_from_string(32, payload)

                get_mstp_version_3_mstid_bridge_identifier_priority = self.get_bits_from_string(8, payload)
                self.set_mstp_version_3_mstid_bridge_identifier_priority(
                    "0x" + get_mstp_version_3_mstid_bridge_identifier_priority, index)
                payload = self.remove_bits_from_string(8, payload)

                get_mstp_version_3_mstid_port_identifier_priority = self.get_bits_from_string(8, payload)
                self.set_mstp_version_3_mstid_port_identifier_priority(
                    "0x" + get_mstp_version_3_mstid_port_identifier_priority, index)
                payload = self.remove_bits_from_string(8, payload)

                get_mstp_version_3_mstid_remaining_hops = self.get_bits_from_string(8, payload)
                self.set_mstp_version_3_mstid_remaining_hops("0x" + get_mstp_version_3_mstid_remaining_hops, index)
                payload = self.remove_bits_from_string(8, payload)

                index += 1
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_mstp_version_1_length(), PacketConstants.INTEGER, 8)
        if not self.is_field_set(self.get_mstp_version_3_length()) and self.get_mstid_num() > 0:
            ret_string += self.format_byte_string(64 + (16 * self.get_mstid_num()), PacketConstants.INTEGER, 16)
        else:
            ret_string += self.format_byte_string(self.get_mstp_version_3_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_mstp_version_3_id_format(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_mstp_version_3_name(False), PacketConstants.HEX_STRING, 256)
        ret_string += self.format_byte_string(self.get_mstp_version_3_revision(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_mstp_version_3_digest(), PacketConstants.HEX_STRING, 128)
        ret_string += self.format_byte_string(self.get_mstp_version_3_cist_internal_root_path_cost(),
                                              PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_mstp_version_3_cist_bridge_internal_priority(),
                                              PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_mstp_version_3_cist_bridge_internal_system_id(),
                                              PacketConstants.ENET_ADDRESS, 48)
        ret_string += self.format_byte_string(self.get_mstp_version_3_cist_remaining_hops(),
                                              PacketConstants.INTEGER, 8)
        index = 1
        for index in range(1, self.get_mstid_num() + 1):
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_flags(index),
                                                  PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_priority(index),
                                                  PacketConstants.INTEGER, 4)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_mstid(index),
                                                  PacketConstants.INTEGER, 12)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_regional_root(index),
                                                  PacketConstants.ENET_ADDRESS, 48)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_internal_root_path_cost(index),
                                                  PacketConstants.INTEGER, 32)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_bridge_identifier_priority(index),
                                                  PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_port_identifier_priority(index),
                                                  PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(self.get_mstp_version_3_mstid_remaining_hops(index),
                                                  PacketConstants.INTEGER, 8)
            index += 1
        return ret_string

    @staticmethod
    def compare_mstp_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                   print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, MstpPacketHeader)
            assert isinstance(actual, MstpPacketHeader)
            if expected.do_i_check_this_field(expected.get_mstp_version_1_length(),
                                              MstpPacketConstants.MSTP_VERSION_1_LENGTH, ignore_list, include_list):
                name = "MSTP version 1 length : "
                if expected.get_mstp_version_1_length() != actual.get_mstp_version_1_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_1_length()) + " != " +
                                                      str(actual.get_mstp_version_1_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_1_length()) + " == " +
                                                 str(actual.get_mstp_version_1_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_length(),
                                              MstpPacketConstants.MSTP_VERSION_3_LENGTH, ignore_list, include_list):
                name = "MSTP version 3 length : "
                if expected.get_mstp_version_3_length() != actual.get_mstp_version_3_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_3_length()) + " != " +
                                                      str(actual.get_mstp_version_3_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_3_length()) + " == " +
                                                 str(actual.get_mstp_version_3_length()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_id_format(),
                                              MstpPacketConstants.MSTP_VERSION_3_ID_FORMAT, ignore_list, include_list):
                name = "MSTP version 3 id format : "
                if expected.get_mstp_version_3_id_format() != actual.get_mstp_version_3_id_format():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_3_id_format()) + " != " +
                                                      str(actual.get_mstp_version_3_id_format()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_3_id_format()) + " == " +
                                                 str(actual.get_mstp_version_3_id_format()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_name(),
                                              MstpPacketConstants.MSTP_VERSION_3_NAME, ignore_list, include_list):
                name = "MSTP version 3 name : "
                if expected.get_mstp_version_3_name().strip() != actual.get_mstp_version_3_name().strip():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_3_name()) + " != " +
                                                      str(actual.get_mstp_version_3_name()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_3_name()) + " == " +
                                                 str(actual.get_mstp_version_3_name()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_revision(),
                                              MstpPacketConstants.MSTP_VERSION_3_REVISION, ignore_list, include_list):
                name = "MSTP version 3 revision : "
                if expected.get_mstp_version_3_revision() != actual.get_mstp_version_3_revision():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_3_revision()) + " != " +
                                                      str(actual.get_mstp_version_3_revision()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_3_revision()) + " == " +
                                                 str(actual.get_mstp_version_3_revision()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_digest(),
                                              MstpPacketConstants.MSTP_VERSION_3_DIGEST, ignore_list, include_list):
                name = "MSTP version 3 digest : "
                if expected.get_mstp_version_3_digest() != actual.get_mstp_version_3_digest():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_mstp_version_3_digest()) + " != " +
                                                      str(actual.get_mstp_version_3_digest()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_mstp_version_3_digest()) + " == " +
                                                 str(actual.get_mstp_version_3_digest()) + " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_cist_internal_root_path_cost(),
                                              MstpPacketConstants.MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST,
                                              ignore_list, include_list):
                name = "MSTP version 3 cist internal root path cost : "
                if expected.get_mstp_version_3_cist_internal_root_path_cost() != \
                        actual.get_mstp_version_3_cist_internal_root_path_cost():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name +
                                                      str(expected.get_mstp_version_3_cist_internal_root_path_cost()) +
                                                      " != " +
                                                      str(actual.get_mstp_version_3_cist_internal_root_path_cost()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_cist_internal_root_path_cost()) +
                                                 " == " +
                                                 str(actual.get_mstp_version_3_cist_internal_root_path_cost()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_cist_bridge_internal_priority(),
                                              MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY,
                                              ignore_list, include_list):
                name = "MSTP version 3 cist bridge internal priority : "
                if expected.get_mstp_version_3_cist_bridge_internal_priority() != \
                        actual.get_mstp_version_3_cist_bridge_internal_priority():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name +
                                                      str(expected.get_mstp_version_3_cist_bridge_internal_priority()) +
                                                      " != " +
                                                      str(actual.get_mstp_version_3_cist_bridge_internal_priority()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_cist_bridge_internal_priority()) +
                                                 " == " +
                                                 str(actual.get_mstp_version_3_cist_bridge_internal_priority()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_cist_bridge_internal_system_id(),
                                              MstpPacketConstants.MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID,
                                              ignore_list, include_list):
                name = "MSTP version 3 cist bridge internal system id : "
                if expected.get_mstp_version_3_cist_bridge_internal_system_id() != \
                        actual.get_mstp_version_3_cist_bridge_internal_system_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            name + str(expected.get_mstp_version_3_cist_bridge_internal_system_id()) + " != " +
                            str(actual.get_mstp_version_3_cist_bridge_internal_system_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_cist_bridge_internal_system_id()) +
                                                 " == " +
                                                 str(actual.get_mstp_version_3_cist_bridge_internal_system_id()) +
                                                 " Pass")

            if expected.do_i_check_this_field(expected.get_mstp_version_3_cist_remaining_hops(),
                                              MstpPacketConstants.MSTP_VERSION_3_CIST_REMAINING_HOPS,
                                              ignore_list, include_list):
                name = "MSTP version 3 cist remaining hops : "
                if expected.get_mstp_version_3_cist_remaining_hops() != actual.get_mstp_version_3_cist_remaining_hops():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name +
                                                      str(expected.get_mstp_version_3_cist_remaining_hops()) +
                                                      " != " + str(actual.get_mstp_version_3_cist_remaining_hops()) +
                                                      " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_cist_remaining_hops()) + " == " +
                                                 str(actual.get_mstp_version_3_cist_remaining_hops()) + " Pass")

            if dynamic_entries:
                dynamic_results = dynamic_entries.compare_packet_fields(expected, actual)
                if not dynamic_results:
                    PacketObject.logger.log_error("Dynamic Ordering error ERROR")
                    PacketObject.logger.log_error(dynamic_entries)
                    PacketObject.logger.log_error("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_error("Received:" + actual.to_packet_string_tags())
                else:
                    PacketObject.logger.log_info("Dynamic Ordering Pass")
                    PacketObject.logger.log_info(dynamic_entries)
                    PacketObject.logger.log_info("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_info("Received:" + actual.to_packet_string_tags())
                results &= dynamic_results
            else:
                name = "MSTID Number: "
                if expected.do_i_check_this_field(expected.get_mstid_num(),
                                                  MstpPacketConstants.MSTP_VERSION_3_MSTID_NUM,
                                                  ignore_list, include_list):
                    if str(expected.get_mstid_num()) != str(actual.get_mstid_num()):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(name + str(expected.get_mstid_num()) + " != " +
                                                          str(actual.get_mstid_num()) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_mstid_num()) + " == " +
                                                     str(actual.get_mstid_num()) + " Pass")
                num_mstid = min(expected.get_mstid_num(), actual.get_mstid_num())
                index = 0
                while index < num_mstid:
                    index += 1
                    results &= expected.compare_tags(expected, actual, index, index, ignore_list, include_list,
                                                     print_results, print_failures)

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with MstpPacketHeader")
        return results

    @staticmethod
    def compare_tags(expected, actual, expected_index, actual_index, ignore_list=None, include_list=None,
                     print_results=True, print_failures=True):
        results = True
        wasSomethingChecked = False
        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_flags(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_FLAG + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "MSTP MSTI Flags " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_flags(expected_index) != \
                    actual.get_mstp_version_3_mstid_flags(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_mstp_version_3_mstid_flags(expected_index)) +
                                                  " != " + str(actual.get_mstp_version_3_mstid_flags(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_mstid_flags(expected_index)) + " == " +
                                                 str(actual.get_mstp_version_3_mstid_flags(actual_index)) + " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_priority(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_PRIORITY + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "MSTP MSTI Priority " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_priority(expected_index) != \
                    actual.get_mstp_version_3_mstid_priority(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_mstp_version_3_mstid_priority(expected_index)) +
                                                  " != " +
                                                  str(actual.get_mstp_version_3_mstid_priority(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_mstid_priority(expected_index)) +
                                                 " == " + str(actual.get_mstp_version_3_mstid_priority(actual_index)) +
                                                 " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_mstid(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_MSTID + " " + str(expected_index),
                                          ignore_list, include_list):
            name = "MSTP MSTI MSTID " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_mstid(expected_index) != \
                    actual.get_mstp_version_3_mstid_mstid(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_mstp_version_3_mstid_mstid(expected_index)) +
                                                  " != " + str(actual.get_mstp_version_3_mstid_mstid(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_mstid_mstid(expected_index)) +
                                                 " == " + str(actual.get_mstp_version_3_mstid_mstid(actual_index)) +
                                                 " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_regional_root(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_REGIONAL_ROOT + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "MSTP MSTI Regional Root " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_regional_root(expected_index) != \
                    actual.get_mstp_version_3_mstid_regional_root(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name +
                                                  str(expected.get_mstp_version_3_mstid_regional_root(expected_index)) +
                                                  " != " +
                                                  str(actual.get_mstp_version_3_mstid_regional_root(actual_index)) +
                                                  " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name +
                                                 str(expected.get_mstp_version_3_mstid_regional_root(expected_index)) +
                                                 " == " +
                                                 str(actual.get_mstp_version_3_mstid_regional_root(actual_index)) +
                                                 " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_internal_root_path_cost(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "MSTP MSTID Internal Root Path Cost " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_internal_root_path_cost(expected_index) != \
                    actual.get_mstp_version_3_mstid_internal_root_path_cost(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(
                        name + str(expected.get_mstp_version_3_mstid_internal_root_path_cost(expected_index)) + " != " +
                        str(actual.get_mstp_version_3_mstid_internal_root_path_cost(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_mstp_version_3_mstid_internal_root_path_cost(expected_index)) + " == " +
                        str(actual.get_mstp_version_3_mstid_internal_root_path_cost(actual_index)) + " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_bridge_identifier_priority(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "MSTP MSTID Bridge Identifier Priority " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_bridge_identifier_priority(expected_index) != \
                    actual.get_mstp_version_3_mstid_bridge_identifier_priority(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(
                        name + str(expected.get_mstp_version_3_mstid_bridge_identifier_priority(expected_index)) +
                        " != " + str(actual.get_mstp_version_3_mstid_bridge_identifier_priority(actual_index)) +
                        " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_mstp_version_3_mstid_bridge_identifier_priority(expected_index)) +
                        " == " + str(actual.get_mstp_version_3_mstid_bridge_identifier_priority(actual_index)) +
                        " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_port_identifier_priority(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "MSTP MSTID Port Identifier Priority " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_port_identifier_priority(expected_index) != \
                    actual.get_mstp_version_3_mstid_port_identifier_priority(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(
                        name + str(expected.get_mstp_version_3_mstid_port_identifier_priority(expected_index)) +
                        " != " + str(actual.get_mstp_version_3_mstid_port_identifier_priority(actual_index)) +
                        " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_mstp_version_3_mstid_port_identifier_priority(expected_index)) +
                        " == " + str(actual.get_mstp_version_3_mstid_port_identifier_priority(actual_index)) +
                        " Pass")

        if expected.do_i_check_this_field(expected.get_mstp_version_3_mstid_remaining_hops(expected_index),
                                          MstpPacketConstants.MSTP_VERSION_3_MSTID_REMAINING_HOPS + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "MSTP MSTID Remaining Hops " + str(expected_index) + ": "
            if expected.get_mstp_version_3_mstid_remaining_hops(expected_index) != \
                    actual.get_mstp_version_3_mstid_remaining_hops(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(
                        name + str(expected.get_mstp_version_3_mstid_remaining_hops(expected_index)) + " != " +
                        str(actual.get_mstp_version_3_mstid_remaining_hops(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_mstp_version_3_mstid_remaining_hops(expected_index)) + " == " +
                        str(actual.get_mstp_version_3_mstid_remaining_hops(actual_index)) + " Pass")

        return results


class MstpPacketConstants:
    def __init__(self):
        pass

    MSTP_VERSION_1_LENGTH = "MSTP_VERSION_1_LENGTH"
    MSTP_VERSION_3_LENGTH = "MSTP_VERSION_3_LENGTH"
    MSTP_VERSION_3_ID_FORMAT = "MSTP_VERSION_3_ID_FORMAT"
    MSTP_VERSION_3_NAME = "MSTP_VERSION_3_NAME"
    MSTP_VERSION_3_REVISION = "MSTP_VERSION_3_REVISION"
    MSTP_VERSION_3_DIGEST = "MSTP_VERSION_3_DIGEST"
    MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST = "MSTP_VERSION_3_CIST_INTERNAL_ROOT_PATH_COST"
    MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY = "MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_PRIORITY"
    MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID = "MSTP_VERSION_3_CIST_BRIDGE_INTERNAL_SYSTEM_ID"
    MSTP_VERSION_3_CIST_REMAINING_HOPS = "MSTP_VERSION_3_CIST_REMAINING_HOPS"

    MSTP_VERSION_3_MSTID_NUM = "MSTP_VERSION_3_MSTID_NUM"
    MSTP_VERSION_3_MSTID_FLAG = "MSTP_VERSION_3_MSTID_FLAG"
    MSTP_VERSION_3_MSTID_PRIORITY = "MSTP_VERSION_3_MSTID_PRIORITY"
    MSTP_VERSION_3_MSTID_MSTID = "MSTP_VERSION_3_MSTID_MSTID"
    MSTP_VERSION_3_MSTID_REGIONAL_ROOT = "MSTP_VERSION_3_MSTID_REGIONAL_ROOT"
    MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST = "MSTP_VERSION_3_MSTID_INTERNAL_ROOT_PATH_COST"
    MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY = "MSTP_VERSION_3_MSTID_BRIDGE_IDENTIFIER_PRIORITY"
    MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY = "MSTP_VERSION_3_MSTID_PORT_IDENTIFIER_PRIORITY"
    MSTP_VERSION_3_MSTID_REMAINING_HOPS = "MSTP_VERSION_3_MSTID_REMAINING_HOPS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class MstpPacketHeaderDynamicFieldLogic(PacketHeaderDynamicFieldLogic):

    def compare_dynamic_fields(self, expected, actual, index, index_actual_vlans, print_results=False,
                               print_failures=False):
        return expected.compare_tags(expected, actual, index, index_actual_vlans, None, None, print_results,
                                     print_failures)

    def get_compare_number(self, expected):
        return expected.get_mstid_num()
