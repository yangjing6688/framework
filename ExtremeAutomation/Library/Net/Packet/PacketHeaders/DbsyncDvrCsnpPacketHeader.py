from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrPacketHeader import DvrTlvEntry
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump


class DbsyncDvrCsnpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    DB Sync DVR CSNP Packet Header
        # CSNP Reserved 1 = 8bits
        # CSNP Header Length = 8bits
        # CSNP Reserved 2 = 8bits
        # CSNP ID Length = 8bits
        # CSNP PDU Type = 8bits
        # CSNP Reserved 3 = 8bits
        # CSNP Reserved 4 = 8bits
        # CSNP Reserved 5 = 8bits
        # CSNP PDU Length = 16bits
        # CSNP DBP Source = 48bits
        # CSNP Reserved 6 = 8bits
        # CSNP Start ID Source = 48bits
        # CSNP Start ID Node = 8bits
        # CSNP Start ID Number = 32bits
        # CSNP End ID Source = 48bits
        # CSNP End ID Node = 8bits
        # CSNP End ID Number = 32bits
    """

    def __init__(self):
        self.add_dbsyncdvrcsnp_header()
        self.tlv_entries = []
        self.HEADER_SIZE_DBSYNCDVRCSNP = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start DbsyncDvrCsnp CSNP Reserved 1 methods
    #  csnp_reserved_1 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_1(self, csnp_reserved_1, ignore_check=False):
        csnp_reserved_1 = self.normalize_value(csnp_reserved_1, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_1, csnp_reserved_1)

    def get_dbsyncdvrcsnp_csnp_reserved_1(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_1),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_1_hltapi_cmd(self, dummy_dict):
        csnp_reserved_1 = self.get_dbsyncdvrcsnp_csnp_reserved_1()
        if isinstance(csnp_reserved_1, int):
            csnp_reserved_1 = str(csnp_reserved_1)
        if csnp_reserved_1 and 'Not Set' not in csnp_reserved_1:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_1_CMD] = csnp_reserved_1

    # end DbsyncDvrCsnp CSNP Reserved 1 methods

    # start DbsyncDvrCsnp CSNP Header Length methods
    #  csnp_header_length is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_header_length(self, csnp_header_length, ignore_check=False):
        csnp_header_length = self.normalize_value(csnp_header_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_HEADER_LENGTH, csnp_header_length)

    def get_dbsyncdvrcsnp_csnp_header_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_HEADER_LENGTH), PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_header_length_hltapi_cmd(self, dummy_dict):
        csnp_header_length = self.get_dbsyncdvrcsnp_csnp_header_length()
        if isinstance(csnp_header_length, int):
            csnp_header_length = str(csnp_header_length)
        if csnp_header_length and 'Not Set' not in csnp_header_length:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_HEADER_LENGTH_CMD] = csnp_header_length

    # end DbsyncDvrCsnp CSNP Header Length methods

    # start DbsyncDvrCsnp CSNP Reserved 2 methods
    #  csnp_reserved_2 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_2(self, csnp_reserved_2, ignore_check=False):
        csnp_reserved_2 = self.normalize_value(csnp_reserved_2, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_2, csnp_reserved_2)

    def get_dbsyncdvrcsnp_csnp_reserved_2(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_2),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_2_hltapi_cmd(self, dummy_dict):
        csnp_reserved_2 = self.get_dbsyncdvrcsnp_csnp_reserved_2()
        if isinstance(csnp_reserved_2, int):
            csnp_reserved_2 = str(csnp_reserved_2)
        if csnp_reserved_2 and 'Not Set' not in csnp_reserved_2:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_2_CMD] = csnp_reserved_2

    # end DbsyncDvrCsnp CSNP Reserved 2 methods

    # start DbsyncDvrCsnp CSNP ID Length methods
    #  csnp_id_length is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_id_length(self, csnp_id_length, ignore_check=False):
        csnp_id_length = self.normalize_value(csnp_id_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_ID_LENGTH, csnp_id_length)

    def get_dbsyncdvrcsnp_csnp_id_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_ID_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_id_length_hltapi_cmd(self, dummy_dict):
        csnp_id_length = self.get_dbsyncdvrcsnp_csnp_id_length()
        if isinstance(csnp_id_length, int):
            csnp_id_length = str(csnp_id_length)
        if csnp_id_length and 'Not Set' not in csnp_id_length:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_ID_LENGTH_CMD] = csnp_id_length

    # end DbsyncDvrCsnp CSNP ID Length methods

    # start DbsyncDvrCsnp CSNP PDU Type methods
    #  csnp_pdu_type is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_pdu_type(self, csnp_pdu_type, ignore_check=False):
        csnp_pdu_type = self.normalize_value(csnp_pdu_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_TYPE, csnp_pdu_type)

    def get_dbsyncdvrcsnp_csnp_pdu_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_TYPE),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_pdu_type_hltapi_cmd(self, dummy_dict):
        csnp_pdu_type = self.get_dbsyncdvrcsnp_csnp_pdu_type()
        if isinstance(csnp_pdu_type, int):
            csnp_pdu_type = str(csnp_pdu_type)
        if csnp_pdu_type and 'Not Set' not in csnp_pdu_type:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_PDU_TYPE_CMD] = csnp_pdu_type

    # end DbsyncDvrCsnp CSNP PDU Type methods

    # start DbsyncDvrCsnp CSNP Reserved 3 methods
    #  csnp_reserved_3 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_3(self, csnp_reserved_3, ignore_check=False):
        csnp_reserved_3 = self.normalize_value(csnp_reserved_3, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_3, csnp_reserved_3)

    def get_dbsyncdvrcsnp_csnp_reserved_3(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_3),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_3_hltapi_cmd(self, dummy_dict):
        csnp_reserved_3 = self.get_dbsyncdvrcsnp_csnp_reserved_3()
        if isinstance(csnp_reserved_3, int):
            csnp_reserved_3 = str(csnp_reserved_3)
        if csnp_reserved_3 and 'Not Set' not in csnp_reserved_3:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_3_CMD] = csnp_reserved_3

    # end DbsyncDvrCsnp CSNP Reserved 3 methods

    # start DbsyncDvrCsnp CSNP Reserved 4 methods
    #  csnp_reserved_4 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_4(self, csnp_reserved_4, ignore_check=False):
        csnp_reserved_4 = self.normalize_value(csnp_reserved_4, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_4, csnp_reserved_4)

    def get_dbsyncdvrcsnp_csnp_reserved_4(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_4),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_4_hltapi_cmd(self, dummy_dict):
        csnp_reserved_4 = self.get_dbsyncdvrcsnp_csnp_reserved_4()
        if isinstance(csnp_reserved_4, int):
            csnp_reserved_4 = str(csnp_reserved_4)
        if csnp_reserved_4 and 'Not Set' not in csnp_reserved_4:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_4_CMD] = csnp_reserved_4

    # end DbsyncDvrCsnp CSNP Reserved 4 methods

    # start DbsyncDvrCsnp CSNP Reserved 5 methods
    #  csnp_reserved_5 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_5(self, csnp_reserved_5, ignore_check=False):
        csnp_reserved_5 = self.normalize_value(csnp_reserved_5, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_5, csnp_reserved_5)

    def get_dbsyncdvrcsnp_csnp_reserved_5(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_5),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_5_hltapi_cmd(self, dummy_dict):
        csnp_reserved_5 = self.get_dbsyncdvrcsnp_csnp_reserved_5()
        if isinstance(csnp_reserved_5, int):
            csnp_reserved_5 = str(csnp_reserved_5)
        if csnp_reserved_5 and 'Not Set' not in csnp_reserved_5:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_5_CMD] = csnp_reserved_5

    # end DbsyncDvrCsnp CSNP Reserved 5 methods

    # start DbsyncDvrCsnp CSNP PDU Length methods
    #  csnp_pdu_length is a 16 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_pdu_length(self, csnp_pdu_length, ignore_check=False):
        csnp_pdu_length = self.normalize_value(csnp_pdu_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_LENGTH, csnp_pdu_length)

    def get_dbsyncdvrcsnp_csnp_pdu_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_pdu_length_hltapi_cmd(self, dummy_dict):
        csnp_pdu_length = self.get_dbsyncdvrcsnp_csnp_pdu_length()
        if isinstance(csnp_pdu_length, int):
            csnp_pdu_length = str(csnp_pdu_length)
        if csnp_pdu_length and 'Not Set' not in csnp_pdu_length:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_PDU_LENGTH_CMD] = csnp_pdu_length

    # end DbsyncDvrCsnp CSNP PDU Length methods

    # start DbsyncDvrCsnp CSNP DBP Source methods
    #  csnp_dbp_source is a 48 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_dbp_source(self, csnp_dbp_source, ignore_check=False):
        csnp_dbp_source = self.normalize_value(csnp_dbp_source, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_DBP_SOURCE, csnp_dbp_source)

    def get_dbsyncdvrcsnp_csnp_dbp_source(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_DBP_SOURCE),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_dbp_source_hltapi_cmd(self, dummy_dict):
        csnp_dbp_source = self.get_dbsyncdvrcsnp_csnp_dbp_source()
        if isinstance(csnp_dbp_source, int):
            csnp_dbp_source = str(csnp_dbp_source)
        if csnp_dbp_source and 'Not Set' not in csnp_dbp_source:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_DBP_SOURCE_CMD] = csnp_dbp_source

    # end DbsyncDvrCsnp CSNP DBP Source methods

    # start DbsyncDvrCsnp CSNP Reserved 6 methods
    #  csnp_reserved_6 is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_reserved_6(self, csnp_reserved_6, ignore_check=False):
        csnp_reserved_6 = self.normalize_value(csnp_reserved_6, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_6, csnp_reserved_6)

    def get_dbsyncdvrcsnp_csnp_reserved_6(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR, DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_6),
            PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_reserved_6_hltapi_cmd(self, dummy_dict):
        csnp_reserved_6 = self.get_dbsyncdvrcsnp_csnp_reserved_6()
        if isinstance(csnp_reserved_6, int):
            csnp_reserved_6 = str(csnp_reserved_6)
        if csnp_reserved_6 and 'Not Set' not in csnp_reserved_6:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_RESERVED_6_CMD] = csnp_reserved_6

    # end DbsyncDvrCsnp CSNP Reserved 6 methods

    # start DbsyncDvrCsnp CSNP Start ID Source methods
    #  csnp_start_id_source is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_dbsyncdvrcsnp_csnp_start_id_source(self, csnp_start_id_source, ignore_check=False):
        csnp_start_id_source = self.normalize_value(csnp_start_id_source, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_SOURCE, csnp_start_id_source)

    def get_dbsyncdvrcsnp_csnp_start_id_source(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_SOURCE), PacketConstants.HEX_STRING)

    def get_dbsyncdvrcsnp_csnp_start_id_source_hltapi_cmd(self, dummy_dict):
        csnp_start_id_source = self.get_dbsyncdvrcsnp_csnp_start_id_source()
        if csnp_start_id_source and 'Not Set' not in csnp_start_id_source:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_START_ID_SOURCE_CMD] = csnp_start_id_source

    # end DbsyncDvrCsnp CSNP Start ID Source methods

    # start DbsyncDvrCsnp CSNP Start ID Node methods
    #  csnp_start_id_node is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_start_id_node(self, csnp_start_id_node, ignore_check=False):
        csnp_start_id_node = self.normalize_value(csnp_start_id_node, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NODE, csnp_start_id_node)

    def get_dbsyncdvrcsnp_csnp_start_id_node(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NODE), PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_start_id_node_hltapi_cmd(self, dummy_dict):
        csnp_start_id_node = self.get_dbsyncdvrcsnp_csnp_start_id_node()
        if isinstance(csnp_start_id_node, int):
            csnp_start_id_node = str(csnp_start_id_node)
        if csnp_start_id_node and 'Not Set' not in csnp_start_id_node:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_START_ID_NODE_CMD] = csnp_start_id_node

    # end DbsyncDvrCsnp CSNP Start ID Node methods

    # start DbsyncDvrCsnp CSNP Start ID Number methods
    #  csnp_start_id_number is a 32 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_start_id_number(self, csnp_start_id_number, ignore_check=False):
        csnp_start_id_number = self.normalize_value(csnp_start_id_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NUMBER, csnp_start_id_number)

    def get_dbsyncdvrcsnp_csnp_start_id_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NUMBER), PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_start_id_number_hltapi_cmd(self, dummy_dict):
        csnp_start_id_number = self.get_dbsyncdvrcsnp_csnp_start_id_number()
        if isinstance(csnp_start_id_number, int):
            csnp_start_id_number = str(csnp_start_id_number)
        if csnp_start_id_number and 'Not Set' not in csnp_start_id_number:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_START_ID_NUMBER_CMD] = csnp_start_id_number

    # end DbsyncDvrCsnp CSNP Start ID Number methods

    # start DbsyncDvrCsnp CSNP End ID Source methods
    #  csnp_end_id_source is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_dbsyncdvrcsnp_csnp_end_id_source(self, csnp_end_id_source, ignore_check=False):
        csnp_end_id_source = self.normalize_value(csnp_end_id_source, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_SOURCE, csnp_end_id_source)

    def get_dbsyncdvrcsnp_csnp_end_id_source(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_SOURCE), PacketConstants.HEX_STRING)

    def get_dbsyncdvrcsnp_csnp_end_id_source_hltapi_cmd(self, dummy_dict):
        csnp_end_id_source = self.get_dbsyncdvrcsnp_csnp_end_id_source()
        if csnp_end_id_source and 'Not Set' not in csnp_end_id_source:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_END_ID_SOURCE_CMD] = csnp_end_id_source

    # end DbsyncDvrCsnp CSNP End ID Source methods

    # start DbsyncDvrCsnp CSNP End ID Node methods
    #  csnp_end_id_node is a 8 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_end_id_node(self, csnp_end_id_node, ignore_check=False):
        csnp_end_id_node = self.normalize_value(csnp_end_id_node, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NODE, csnp_end_id_node)

    def get_dbsyncdvrcsnp_csnp_end_id_node(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NODE), PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_end_id_node_hltapi_cmd(self, dummy_dict):
        csnp_end_id_node = self.get_dbsyncdvrcsnp_csnp_end_id_node()
        if isinstance(csnp_end_id_node, int):
            csnp_end_id_node = str(csnp_end_id_node)
        if csnp_end_id_node and 'Not Set' not in csnp_end_id_node:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_END_ID_NODE_CMD] = csnp_end_id_node

    # end DbsyncDvrCsnp CSNP End ID Node methods

    # start DbsyncDvrCsnp CSNP End ID Number methods
    #  csnp_end_id_number is a 32 bit INTEGER example: 1
    def set_dbsyncdvrcsnp_csnp_end_id_number(self, csnp_end_id_number, ignore_check=False):
        csnp_end_id_number = self.normalize_value(csnp_end_id_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
                                  DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NUMBER, csnp_end_id_number)

    def get_dbsyncdvrcsnp_csnp_end_id_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_CSNPDBSYNCDVR,
            DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NUMBER), PacketConstants.INTEGER)

    def get_dbsyncdvrcsnp_csnp_end_id_number_hltapi_cmd(self, dummy_dict):
        csnp_end_id_number = self.get_dbsyncdvrcsnp_csnp_end_id_number()
        if isinstance(csnp_end_id_number, int):
            csnp_end_id_number = str(csnp_end_id_number)
        if csnp_end_id_number and 'Not Set' not in csnp_end_id_number:
            dummy_dict[TrafficConfigConstants.TEMP_CSNP_END_ID_NUMBER_CMD] = csnp_end_id_number

    # end DbsyncDvrCsnp CSNP End ID Number methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("CSNP Reserved 1", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_1(), 1))
        table.add_row_value("CSNP Header Length", self.format_int(self.get_dbsyncdvrcsnp_csnp_header_length(), 1))
        table.add_row_value("CSNP Reserved 2", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_2(), 1))
        table.add_row_value("CSNP ID Length", self.format_int(self.get_dbsyncdvrcsnp_csnp_id_length(), 1))
        table.add_row_value("CSNP PDU Type", self.format_int(self.get_dbsyncdvrcsnp_csnp_pdu_type(), 1))
        table.add_row_value("CSNP Reserved 3", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_3(), 1))
        table.add_row_value("CSNP Reserved 4", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_4(), 1))
        table.add_row_value("CSNP Reserved 5", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_5(), 1))
        table.add_row_value("CSNP PDU Length", self.format_int(self.get_dbsyncdvrcsnp_csnp_pdu_length(), 2))
        table.add_row_value("CSNP DBP Source", self.format_int(self.get_dbsyncdvrcsnp_csnp_dbp_source(), 6))
        table.add_row_value("CSNP Reserved 6", self.format_int(self.get_dbsyncdvrcsnp_csnp_reserved_6(), 1))
        table.add_row_value("CSNP Start ID Source", self.get_dbsyncdvrcsnp_csnp_start_id_source())
        table.add_row_value("CSNP Start ID Node", self.format_int(self.get_dbsyncdvrcsnp_csnp_start_id_node(), 1))
        table.add_row_value("CSNP Start ID Number", self.format_int(self.get_dbsyncdvrcsnp_csnp_start_id_number(), 4))
        table.add_row_value("CSNP End ID Source", self.get_dbsyncdvrcsnp_csnp_end_id_source())
        table.add_row_value("CSNP End ID Node", self.format_int(self.get_dbsyncdvrcsnp_csnp_end_id_node(), 1))
        table.add_row_value("CSNP End ID Number", self.format_int(self.get_dbsyncdvrcsnp_csnp_end_id_number(), 4))
        ret_string = "\n\nDBSYNCDVRCSNP HEADER" + table.to_table_string()
        table_tlv = DvrTlvEntry.to_packet_string(self)

        return ret_string + "\n\nDVR TLV ENTRIES" + table_tlv.to_table_string()

    def add_dbsyncdvrcsnp_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_CSNPDBSYNCDVR)

    def build(self):
        self.add_dbsyncdvrcsnp_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_dbsyncdvrcsnp_csnp_reserved_1_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_header_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_reserved_2_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_id_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_pdu_type_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_reserved_3_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_reserved_4_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_reserved_5_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_pdu_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_dbp_source_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_reserved_6_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_start_id_source_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_start_id_node_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_start_id_number_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_end_id_source_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_end_id_node_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvrcsnp_csnp_end_id_number_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_dbsyncdvrcsnp(self, tgen_type, generator_ref, port_string, stream_id,
                                                                 **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_dbsyncdvrcsnp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_dbsyncdvrcsnp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_dbsyncdvrcsnp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kdbsyncdvrcsnpFieldNumber
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = DbsyncDvrCsnpPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    # update this from the ostinato docs.
    # dbsyncdvrcsnpField = p.Extensions[dbsyncdvrcsnp]
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_1()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_1())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_header_length()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_header_length())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_2()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_2())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_id_length()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_id_length())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_pdu_type()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_pdu_type())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_3()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_3())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_4()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_4())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_5()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_5())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_pdu_length()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_pdu_length())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_dbp_source()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_dbp_source())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_6()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_reserved_6())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_source()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_start_id_source())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_node()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_start_id_node())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_number()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_start_id_number())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_source()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_end_id_source())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_node()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_end_id_node())
    # if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_number()) :
    #    dbsyncdvrcsnpField.version = int(self.get_dbsyncdvrcsnp_csnp_end_id_number())

    def config_jets_stream_dbsyncdvrcsnp(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "DBSYNCDVRCSNP_HDR"
        pkt_bytes = "0x" + DbsyncDvrCsnpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_1()):
            pkt_fields["csnp_reserved_1"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_1())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_header_length()):
            pkt_fields["csnp_header_length"] = int(self.get_dbsyncdvrcsnp_csnp_header_length())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_2()):
            pkt_fields["csnp_reserved_2"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_2())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_id_length()):
            pkt_fields["csnp_id_length"] = int(self.get_dbsyncdvrcsnp_csnp_id_length())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_pdu_type()):
            pkt_fields["csnp_pdu_type"] = int(self.get_dbsyncdvrcsnp_csnp_pdu_type())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_3()):
            pkt_fields["csnp_reserved_3"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_3())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_4()):
            pkt_fields["csnp_reserved_4"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_4())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_5()):
            pkt_fields["csnp_reserved_5"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_5())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_pdu_length()):
            pkt_fields["csnp_pdu_length"] = int(self.get_dbsyncdvrcsnp_csnp_pdu_length())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_dbp_source()):
            pkt_fields["csnp_dbp_source"] = int(self.get_dbsyncdvrcsnp_csnp_dbp_source())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_reserved_6()):
            pkt_fields["csnp_reserved_6"] = int(self.get_dbsyncdvrcsnp_csnp_reserved_6())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_source()):
            pkt_fields["csnp_start_id_source"] = int(self.get_dbsyncdvrcsnp_csnp_start_id_source())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_node()):
            pkt_fields["csnp_start_id_node"] = int(self.get_dbsyncdvrcsnp_csnp_start_id_node())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_start_id_number()):
            pkt_fields["csnp_start_id_number"] = int(self.get_dbsyncdvrcsnp_csnp_start_id_number())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_source()):
            pkt_fields["csnp_end_id_source"] = int(self.get_dbsyncdvrcsnp_csnp_end_id_source())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_node()):
            pkt_fields["csnp_end_id_node"] = int(self.get_dbsyncdvrcsnp_csnp_end_id_node())
        if self.is_field_set(self.get_dbsyncdvrcsnp_csnp_end_id_number()):
            pkt_fields["csnp_end_id_number"] = int(self.get_dbsyncdvrcsnp_csnp_end_id_number())

    def get_ixtclhal_dbsyncdvrcsnp_api_commands(self, port_string, streamid):
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
        csnp_reserved_1 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_1("0x" + csnp_reserved_1)
        payload = self.remove_bits_from_string(8, payload)
        csnp_header_length = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_header_length("0x" + csnp_header_length)
        payload = self.remove_bits_from_string(8, payload)
        csnp_reserved_2 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_2("0x" + csnp_reserved_2)
        payload = self.remove_bits_from_string(8, payload)
        csnp_id_length = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_id_length("0x" + csnp_id_length)
        payload = self.remove_bits_from_string(8, payload)
        csnp_pdu_type = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_pdu_type("0x" + csnp_pdu_type)
        payload = self.remove_bits_from_string(8, payload)
        csnp_reserved_3 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_3("0x" + csnp_reserved_3)
        payload = self.remove_bits_from_string(8, payload)
        csnp_reserved_4 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_4("0x" + csnp_reserved_4)
        payload = self.remove_bits_from_string(8, payload)
        csnp_reserved_5 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_5("0x" + csnp_reserved_5)
        payload = self.remove_bits_from_string(8, payload)
        csnp_pdu_length = self.get_bits_from_string(16, payload)
        self.set_dbsyncdvrcsnp_csnp_pdu_length("0x" + csnp_pdu_length)
        payload = self.remove_bits_from_string(16, payload)
        csnp_dbp_source = self.get_bits_from_string(48, payload)
        self.set_dbsyncdvrcsnp_csnp_dbp_source("0x" + csnp_dbp_source)
        payload = self.remove_bits_from_string(48, payload)
        csnp_reserved_6 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_reserved_6("0x" + csnp_reserved_6)
        payload = self.remove_bits_from_string(8, payload)
        csnp_start_id_source = self.get_bits_from_string(48, payload)
        self.set_dbsyncdvrcsnp_csnp_start_id_source("0x" + csnp_start_id_source)
        payload = self.remove_bits_from_string(48, payload)
        csnp_start_id_node = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_start_id_node("0x" + csnp_start_id_node)
        payload = self.remove_bits_from_string(8, payload)
        csnp_start_id_number = self.get_bits_from_string(32, payload)
        self.set_dbsyncdvrcsnp_csnp_start_id_number("0x" + csnp_start_id_number)
        payload = self.remove_bits_from_string(32, payload)
        csnp_end_id_source = self.get_bits_from_string(48, payload)
        self.set_dbsyncdvrcsnp_csnp_end_id_source("0x" + csnp_end_id_source)
        payload = self.remove_bits_from_string(48, payload)
        csnp_end_id_node = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvrcsnp_csnp_end_id_node("0x" + csnp_end_id_node)
        payload = self.remove_bits_from_string(8, payload)
        csnp_end_id_number = self.get_bits_from_string(32, payload)
        self.set_dbsyncdvrcsnp_csnp_end_id_number("0x" + csnp_end_id_number)
        payload = self.remove_bits_from_string(32, payload)
        self.payload = payload
        # processTLVs
        self.payload = DvrTlvEntry.process_tlv(payload, self.tlv_entries, csnp_pdu_length, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_1(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_header_length(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_2(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_id_length(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_pdu_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_3(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_4(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_5(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_pdu_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_dbp_source(), PacketConstants.INTEGER, 48)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_reserved_6(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_start_id_source(), PacketConstants.HEX_STRING,
                                              48)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_start_id_node(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_start_id_number(), PacketConstants.INTEGER,
                                              32)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_end_id_source(), PacketConstants.HEX_STRING,
                                              48)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_end_id_node(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvrcsnp_csnp_end_id_number(), PacketConstants.INTEGER, 32)

        for entry in self.tlv_entries:
            ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string

    @staticmethod
    def compare_dbsyncdvrcsnp_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, DbsyncDvrCsnpPacketHeader)
            assert isinstance(actual, DbsyncDvrCsnpPacketHeader)
            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_1()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_1 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 1 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_1() != actual.get_dbsyncdvrcsnp_csnp_reserved_1():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_1()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_1()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_1()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_1()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_header_length()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_HEADER_LENGTH not in ignore_list:
                name = "DBSYNCDVRCSNP csnp header length : "
                if expected.get_dbsyncdvrcsnp_csnp_header_length() != actual.get_dbsyncdvrcsnp_csnp_header_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_header_length()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_header_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_header_length()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_header_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_2()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_2 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 2 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_2() != actual.get_dbsyncdvrcsnp_csnp_reserved_2():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_2()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_2()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_2()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_2()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_id_length()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_ID_LENGTH not in ignore_list:
                name = "DBSYNCDVRCSNP csnp id length : "
                if expected.get_dbsyncdvrcsnp_csnp_id_length() != actual.get_dbsyncdvrcsnp_csnp_id_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_id_length()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_id_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvrcsnp_csnp_id_length()) + " == " + str(
                        actual.get_dbsyncdvrcsnp_csnp_id_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_pdu_type()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_TYPE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp pdu type : "
                if expected.get_dbsyncdvrcsnp_csnp_pdu_type() != actual.get_dbsyncdvrcsnp_csnp_pdu_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_pdu_type()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_pdu_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvrcsnp_csnp_pdu_type()) + " == " + str(
                        actual.get_dbsyncdvrcsnp_csnp_pdu_type()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_3()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_3 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 3 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_3() != actual.get_dbsyncdvrcsnp_csnp_reserved_3():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_3()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_3()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_3()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_3()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_4()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_4 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 4 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_4() != actual.get_dbsyncdvrcsnp_csnp_reserved_4():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_4()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_4()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_4()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_4()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_5()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_5 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 5 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_5() != actual.get_dbsyncdvrcsnp_csnp_reserved_5():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_5()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_5()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_5()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_5()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_pdu_length()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_PDU_LENGTH not in ignore_list:
                name = "DBSYNCDVRCSNP csnp pdu length : "
                if expected.get_dbsyncdvrcsnp_csnp_pdu_length() != actual.get_dbsyncdvrcsnp_csnp_pdu_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_pdu_length()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_pdu_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_pdu_length()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_pdu_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_dbp_source()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_DBP_SOURCE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp dbp source : "
                if expected.get_dbsyncdvrcsnp_csnp_dbp_source() != actual.get_dbsyncdvrcsnp_csnp_dbp_source():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_dbp_source()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_dbp_source()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_dbp_source()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_dbp_source()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_reserved_6()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_RESERVED_6 not in ignore_list:
                name = "DBSYNCDVRCSNP csnp reserved 6 : "
                if expected.get_dbsyncdvrcsnp_csnp_reserved_6() != actual.get_dbsyncdvrcsnp_csnp_reserved_6():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_reserved_6()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_6()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_reserved_6()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_reserved_6()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_start_id_source()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_SOURCE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp start id source : "
                if expected.get_dbsyncdvrcsnp_csnp_start_id_source() != actual.get_dbsyncdvrcsnp_csnp_start_id_source():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_start_id_source()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_start_id_source()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_start_id_source()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_start_id_source()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_start_id_node()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NODE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp start id node : "
                if expected.get_dbsyncdvrcsnp_csnp_start_id_node() != actual.get_dbsyncdvrcsnp_csnp_start_id_node():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_start_id_node()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_start_id_node()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_start_id_node()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_start_id_node()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_start_id_number()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_START_ID_NUMBER not in ignore_list:
                name = "DBSYNCDVRCSNP csnp start id number : "
                if expected.get_dbsyncdvrcsnp_csnp_start_id_number() != actual.get_dbsyncdvrcsnp_csnp_start_id_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_start_id_number()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_start_id_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_start_id_number()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_start_id_number()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_end_id_source()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_SOURCE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp end id source : "
                if expected.get_dbsyncdvrcsnp_csnp_end_id_source() != actual.get_dbsyncdvrcsnp_csnp_end_id_source():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_end_id_source()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_end_id_source()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_end_id_source()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_end_id_source()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_end_id_node()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NODE not in ignore_list:
                name = "DBSYNCDVRCSNP csnp end id node : "
                if expected.get_dbsyncdvrcsnp_csnp_end_id_node() != actual.get_dbsyncdvrcsnp_csnp_end_id_node():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvrcsnp_csnp_end_id_node()) + " != " + str(
                            actual.get_dbsyncdvrcsnp_csnp_end_id_node()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_end_id_node()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_end_id_node()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvrcsnp_csnp_end_id_number()) and \
                    DbsyncDvrCsnpPacketConstants.DBSYNCDVRCSNP_CSNP_END_ID_NUMBER not in ignore_list:
                name = "DBSYNCDVRCSNP csnp end id number : "
                if expected.get_dbsyncdvrcsnp_csnp_end_id_number() != actual.get_dbsyncdvrcsnp_csnp_end_id_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvrcsnp_csnp_end_id_number()) + " != " + str(
                                actual.get_dbsyncdvrcsnp_csnp_end_id_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvrcsnp_csnp_end_id_number()) + " == " + str(
                            actual.get_dbsyncdvrcsnp_csnp_end_id_number()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with DbsyncDvrCsnpPacketHeader")
        return results


class DbsyncDvrCsnpPacketConstants:
    def __init__(self):
        pass

    DBSYNCDVRCSNP_CSNP_RESERVED_1 = "DBSYNCDVRCSNP_CSNP_RESERVED_1"
    DBSYNCDVRCSNP_CSNP_HEADER_LENGTH = "DBSYNCDVRCSNP_CSNP_HEADER_LENGTH"
    DBSYNCDVRCSNP_CSNP_RESERVED_2 = "DBSYNCDVRCSNP_CSNP_RESERVED_2"
    DBSYNCDVRCSNP_CSNP_ID_LENGTH = "DBSYNCDVRCSNP_CSNP_ID_LENGTH"
    DBSYNCDVRCSNP_CSNP_PDU_TYPE = "DBSYNCDVRCSNP_CSNP_PDU_TYPE"
    DBSYNCDVRCSNP_CSNP_RESERVED_3 = "DBSYNCDVRCSNP_CSNP_RESERVED_3"
    DBSYNCDVRCSNP_CSNP_RESERVED_4 = "DBSYNCDVRCSNP_CSNP_RESERVED_4"
    DBSYNCDVRCSNP_CSNP_RESERVED_5 = "DBSYNCDVRCSNP_CSNP_RESERVED_5"
    DBSYNCDVRCSNP_CSNP_PDU_LENGTH = "DBSYNCDVRCSNP_CSNP_PDU_LENGTH"
    DBSYNCDVRCSNP_CSNP_DBP_SOURCE = "DBSYNCDVRCSNP_CSNP_DBP_SOURCE"
    DBSYNCDVRCSNP_CSNP_RESERVED_6 = "DBSYNCDVRCSNP_CSNP_RESERVED_6"
    DBSYNCDVRCSNP_CSNP_START_ID_SOURCE = "DBSYNCDVRCSNP_CSNP_START_ID_SOURCE"
    DBSYNCDVRCSNP_CSNP_START_ID_NODE = "DBSYNCDVRCSNP_CSNP_START_ID_NODE"
    DBSYNCDVRCSNP_CSNP_START_ID_NUMBER = "DBSYNCDVRCSNP_CSNP_START_ID_NUMBER"
    DBSYNCDVRCSNP_CSNP_END_ID_SOURCE = "DBSYNCDVRCSNP_CSNP_END_ID_SOURCE"
    DBSYNCDVRCSNP_CSNP_END_ID_NODE = "DBSYNCDVRCSNP_CSNP_END_ID_NODE"
    DBSYNCDVRCSNP_CSNP_END_ID_NUMBER = "DBSYNCDVRCSNP_CSNP_END_ID_NUMBER"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
