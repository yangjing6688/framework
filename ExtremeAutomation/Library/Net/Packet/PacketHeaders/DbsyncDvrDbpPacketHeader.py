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


class DbsyncDvrDbpPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    DB Sync DVR DBP Packet Header
        # DBP Reserved 1 = 8bits
        # DBP Header Length = 8bits
        # DBP Reserved 2 = 8bits
        # DBP ID Length = 8bits
        # DBP PDU Type = 8bits
        # DBP Reserved 3 = 8bits
        # DBP Reserved 4 = 8bits
        # DBP Reserved 5 = 8bits
        # DBP PDU Length = 16bits
        # DBP Remaining Lifetime = 16bits
        # DBP ID Source = 48bits
        # DBP ID Node = 8bits
        # DBP ID Number = 32bits
        # DBP Sequence Number = 32bits
        # DBP Checksum = 16bits
        # DBP Reserved 6 = 8bits
    """

    def __init__(self):
        self.add_dbpdbsyncdvr_header()
        self.tlv_entries = []
        self.HEADER_SIZE_DBSYNCDVR = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start DbsyncDvr DBP Reserved 1 methods
    #  dbp_reserved_1 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_1(self, dbp_reserved_1, ignore_check=False):
        dbp_reserved_1 = self.normalize_value(dbp_reserved_1, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_1, dbp_reserved_1)

    def get_dbsyncdvr_dbp_reserved_1(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_1),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_1_hltapi_cmd(self, dummy_dict):
        dbp_reserved_1 = self.get_dbsyncdvr_dbp_reserved_1()
        if isinstance(dbp_reserved_1, int):
            dbp_reserved_1 = str(dbp_reserved_1)
        if dbp_reserved_1 and 'Not Set' not in dbp_reserved_1:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_1_CMD] = dbp_reserved_1

    # end DbsyncDvr DBP Reserved 1 methods

    # start DbsyncDvr DBP Header Length methods
    #  dbp_header_length is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_header_length(self, dbp_header_length, ignore_check=False):
        dbp_header_length = self.normalize_value(dbp_header_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_HEADER_LENGTH, dbp_header_length)

    def get_dbsyncdvr_dbp_header_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_HEADER_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_header_length_hltapi_cmd(self, dummy_dict):
        dbp_header_length = self.get_dbsyncdvr_dbp_header_length()
        if isinstance(dbp_header_length, int):
            dbp_header_length = str(dbp_header_length)
        if dbp_header_length and 'Not Set' not in dbp_header_length:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_HEADER_LENGTH_CMD] = dbp_header_length

    # end DbsyncDvr DBP Header Length methods

    # start DbsyncDvr DBP Reserved 2 methods
    #  dbp_reserved_2 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_2(self, dbp_reserved_2, ignore_check=False):
        dbp_reserved_2 = self.normalize_value(dbp_reserved_2, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_2, dbp_reserved_2)

    def get_dbsyncdvr_dbp_reserved_2(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_2),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_2_hltapi_cmd(self, dummy_dict):
        dbp_reserved_2 = self.get_dbsyncdvr_dbp_reserved_2()
        if isinstance(dbp_reserved_2, int):
            dbp_reserved_2 = str(dbp_reserved_2)
        if dbp_reserved_2 and 'Not Set' not in dbp_reserved_2:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_2_CMD] = dbp_reserved_2

    # end DbsyncDvr DBP Reserved 2 methods

    # start DbsyncDvr DBP ID Length methods
    #  dbp_id_length is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_id_length(self, dbp_id_length, ignore_check=False):
        dbp_id_length = self.normalize_value(dbp_id_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_LENGTH, dbp_id_length)

    def get_dbsyncdvr_dbp_id_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_id_length_hltapi_cmd(self, dummy_dict):
        dbp_id_length = self.get_dbsyncdvr_dbp_id_length()
        if isinstance(dbp_id_length, int):
            dbp_id_length = str(dbp_id_length)
        if dbp_id_length and 'Not Set' not in dbp_id_length:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_ID_LENGTH_CMD] = dbp_id_length

    # end DbsyncDvr DBP ID Length methods

    # start DbsyncDvr DBP PDU Type methods
    #  dbp_pdu_type is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_pdu_type(self, dbp_pdu_type, ignore_check=False):
        dbp_pdu_type = self.normalize_value(dbp_pdu_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_TYPE, dbp_pdu_type)

    def get_dbsyncdvr_dbp_pdu_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_TYPE),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_pdu_type_hltapi_cmd(self, dummy_dict):
        dbp_pdu_type = self.get_dbsyncdvr_dbp_pdu_type()
        if isinstance(dbp_pdu_type, int):
            dbp_pdu_type = str(dbp_pdu_type)
        if dbp_pdu_type and 'Not Set' not in dbp_pdu_type:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_PDU_TYPE_CMD] = dbp_pdu_type

    # end DbsyncDvr DBP PDU Type methods

    # start DbsyncDvr DBP Reserved 3 methods
    #  dbp_reserved_3 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_3(self, dbp_reserved_3, ignore_check=False):
        dbp_reserved_3 = self.normalize_value(dbp_reserved_3, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_3, dbp_reserved_3)

    def get_dbsyncdvr_dbp_reserved_3(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_3),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_3_hltapi_cmd(self, dummy_dict):
        dbp_reserved_3 = self.get_dbsyncdvr_dbp_reserved_3()
        if isinstance(dbp_reserved_3, int):
            dbp_reserved_3 = str(dbp_reserved_3)
        if dbp_reserved_3 and 'Not Set' not in dbp_reserved_3:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_3_CMD] = dbp_reserved_3

    # end DbsyncDvr DBP Reserved 3 methods

    # start DbsyncDvr DBP Reserved 4 methods
    #  dbp_reserved_4 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_4(self, dbp_reserved_4, ignore_check=False):
        dbp_reserved_4 = self.normalize_value(dbp_reserved_4, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_4, dbp_reserved_4)

    def get_dbsyncdvr_dbp_reserved_4(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_4),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_4_hltapi_cmd(self, dummy_dict):
        dbp_reserved_4 = self.get_dbsyncdvr_dbp_reserved_4()
        if isinstance(dbp_reserved_4, int):
            dbp_reserved_4 = str(dbp_reserved_4)
        if dbp_reserved_4 and 'Not Set' not in dbp_reserved_4:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_4_CMD] = dbp_reserved_4

    # end DbsyncDvr DBP Reserved 4 methods

    # start DbsyncDvr DBP Reserved 5 methods
    #  dbp_reserved_5 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_5(self, dbp_reserved_5, ignore_check=False):
        dbp_reserved_5 = self.normalize_value(dbp_reserved_5, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_5, dbp_reserved_5)

    def get_dbsyncdvr_dbp_reserved_5(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_5),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_5_hltapi_cmd(self, dummy_dict):
        dbp_reserved_5 = self.get_dbsyncdvr_dbp_reserved_5()
        if isinstance(dbp_reserved_5, int):
            dbp_reserved_5 = str(dbp_reserved_5)
        if dbp_reserved_5 and 'Not Set' not in dbp_reserved_5:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_5_CMD] = dbp_reserved_5

    # end DbsyncDvr DBP Reserved 5 methods

    # start DbsyncDvr DBP PDU Length methods
    #  dbp_pdu_length is a 16 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_pdu_length(self, dbp_pdu_length, ignore_check=False):
        dbp_pdu_length = self.normalize_value(dbp_pdu_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_LENGTH, dbp_pdu_length)

    def get_dbsyncdvr_dbp_pdu_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_pdu_length_hltapi_cmd(self, dummy_dict):
        dbp_pdu_length = self.get_dbsyncdvr_dbp_pdu_length()
        if isinstance(dbp_pdu_length, int):
            dbp_pdu_length = str(dbp_pdu_length)
        if dbp_pdu_length and 'Not Set' not in dbp_pdu_length:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_PDU_LENGTH_CMD] = dbp_pdu_length

    # end DbsyncDvr DBP PDU Length methods

    # start DbsyncDvr DBP Remaining Lifetime methods
    #  dbp_remaining_lifetime is a 16 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_remaining_lifetime(self, dbp_remaining_lifetime, ignore_check=False):
        dbp_remaining_lifetime = self.normalize_value(dbp_remaining_lifetime, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_REMAINING_LIFETIME, dbp_remaining_lifetime)

    def get_dbsyncdvr_dbp_remaining_lifetime(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
            DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_REMAINING_LIFETIME), PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_remaining_lifetime_hltapi_cmd(self, dummy_dict):
        dbp_remaining_lifetime = self.get_dbsyncdvr_dbp_remaining_lifetime()
        if isinstance(dbp_remaining_lifetime, int):
            dbp_remaining_lifetime = str(dbp_remaining_lifetime)
        if dbp_remaining_lifetime and 'Not Set' not in dbp_remaining_lifetime:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_REMAINING_LIFETIME_CMD] = dbp_remaining_lifetime

    # end DbsyncDvr DBP Remaining Lifetime methods

    # start DbsyncDvr DBP ID Source methods
    #  dbp_id_source is a 48 bit HEX_STRING example: FFFFFFFFFFFF
    def set_dbsyncdvr_dbp_id_source(self, dbp_id_source, ignore_check=False):
        dbp_id_source = self.normalize_value(dbp_id_source, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_SOURCE, dbp_id_source)

    def get_dbsyncdvr_dbp_id_source(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_SOURCE),
            PacketConstants.HEX_STRING)

    def get_dbsyncdvr_dbp_id_source_hltapi_cmd(self, dummy_dict):
        dbp_id_source = self.get_dbsyncdvr_dbp_id_source()
        if dbp_id_source and 'Not Set' not in dbp_id_source:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_ID_SOURCE_CMD] = dbp_id_source

    # end DbsyncDvr DBP ID Source methods

    # start DbsyncDvr DBP ID Node methods
    #  dbp_id_node is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_id_node(self, dbp_id_node, ignore_check=False):
        dbp_id_node = self.normalize_value(dbp_id_node, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NODE, dbp_id_node)

    def get_dbsyncdvr_dbp_id_node(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NODE),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_id_node_hltapi_cmd(self, dummy_dict):
        dbp_id_node = self.get_dbsyncdvr_dbp_id_node()
        if isinstance(dbp_id_node, int):
            dbp_id_node = str(dbp_id_node)
        if dbp_id_node and 'Not Set' not in dbp_id_node:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_ID_NODE_CMD] = dbp_id_node

    # end DbsyncDvr DBP ID Node methods

    # start DbsyncDvr DBP ID Number methods
    #  dbp_id_number is a 32 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_id_number(self, dbp_id_number, ignore_check=False):
        dbp_id_number = self.normalize_value(dbp_id_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NUMBER, dbp_id_number)

    def get_dbsyncdvr_dbp_id_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NUMBER),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_id_number_hltapi_cmd(self, dummy_dict):
        dbp_id_number = self.get_dbsyncdvr_dbp_id_number()
        if isinstance(dbp_id_number, int):
            dbp_id_number = str(dbp_id_number)
        if dbp_id_number and 'Not Set' not in dbp_id_number:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_ID_NUMBER_CMD] = dbp_id_number

    # end DbsyncDvr DBP ID Number methods

    # start DbsyncDvr DBP Sequence Number methods
    #  dbp_sequence_number is a 32 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_sequence_number(self, dbp_sequence_number, ignore_check=False):
        dbp_sequence_number = self.normalize_value(dbp_sequence_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_SEQUENCE_NUMBER, dbp_sequence_number)

    def get_dbsyncdvr_dbp_sequence_number(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_SEQUENCE_NUMBER),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_sequence_number_hltapi_cmd(self, dummy_dict):
        dbp_sequence_number = self.get_dbsyncdvr_dbp_sequence_number()
        if isinstance(dbp_sequence_number, int):
            dbp_sequence_number = str(dbp_sequence_number)
        if dbp_sequence_number and 'Not Set' not in dbp_sequence_number:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_SEQUENCE_NUMBER_CMD] = dbp_sequence_number

    # end DbsyncDvr DBP Sequence Number methods

    # start DbsyncDvr DBP Checksum methods
    #  dbp_checksum is a 16 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_checksum(self, dbp_checksum, ignore_check=False):
        dbp_checksum = self.normalize_value(dbp_checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_CHECKSUM, dbp_checksum)

    def get_dbsyncdvr_dbp_checksum(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_CHECKSUM),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_checksum_hltapi_cmd(self, dummy_dict):
        dbp_checksum = self.get_dbsyncdvr_dbp_checksum()
        if isinstance(dbp_checksum, int):
            dbp_checksum = str(dbp_checksum)
        if dbp_checksum and 'Not Set' not in dbp_checksum:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_CHECKSUM_CMD] = dbp_checksum

    # end DbsyncDvr DBP Checksum methods

    # start DbsyncDvr DBP Reserved 6 methods
    #  dbp_reserved_6 is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_dbp_reserved_6(self, dbp_reserved_6, ignore_check=False):
        dbp_reserved_6 = self.normalize_value(dbp_reserved_6, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR,
                                  DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_6, dbp_reserved_6)

    def get_dbsyncdvr_dbp_reserved_6(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_DBPDBSYNCDVR, DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_6),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_dbp_reserved_6_hltapi_cmd(self, dummy_dict):
        dbp_reserved_6 = self.get_dbsyncdvr_dbp_reserved_6()
        if isinstance(dbp_reserved_6, int):
            dbp_reserved_6 = str(dbp_reserved_6)
        if dbp_reserved_6 and 'Not Set' not in dbp_reserved_6:
            dummy_dict[TrafficConfigConstants.TEMP_DBP_RESERVED_6_CMD] = dbp_reserved_6

    # end DbsyncDvr DBP Reserved 6 methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("DBP Reserved 1", self.format_int(self.get_dbsyncdvr_dbp_reserved_1(), 1))
        table.add_row_value("DBP Header Length", self.format_int(self.get_dbsyncdvr_dbp_header_length(), 1))
        table.add_row_value("DBP Reserved 2", self.format_int(self.get_dbsyncdvr_dbp_reserved_2(), 1))
        table.add_row_value("DBP ID Length", self.format_int(self.get_dbsyncdvr_dbp_id_length(), 1))
        table.add_row_value("DBP PDU Type", self.format_int(self.get_dbsyncdvr_dbp_pdu_type(), 1))
        table.add_row_value("DBP Reserved 3", self.format_int(self.get_dbsyncdvr_dbp_reserved_3(), 1))
        table.add_row_value("DBP Reserved 4", self.format_int(self.get_dbsyncdvr_dbp_reserved_4(), 1))
        table.add_row_value("DBP Reserved 5", self.format_int(self.get_dbsyncdvr_dbp_reserved_5(), 1))
        table.add_row_value("DBP PDU Length", self.format_int(self.get_dbsyncdvr_dbp_pdu_length(), 2))
        table.add_row_value("DBP Remaining Lifetime", self.format_int(self.get_dbsyncdvr_dbp_remaining_lifetime(), 2))
        table.add_row_value("DBP ID Source", self.get_dbsyncdvr_dbp_id_source())
        table.add_row_value("DBP ID Node", self.format_int(self.get_dbsyncdvr_dbp_id_node(), 1))
        table.add_row_value("DBP ID Number", self.format_int(self.get_dbsyncdvr_dbp_id_number(), 4))
        table.add_row_value("DBP Sequence Number", self.format_int(self.get_dbsyncdvr_dbp_sequence_number(), 4))
        table.add_row_value("DBP Checksum", self.format_int(self.get_dbsyncdvr_dbp_checksum(), 2))
        table.add_row_value("DBP Reserved 6", self.format_int(self.get_dbsyncdvr_dbp_reserved_6(), 1))
        ret_string = "\n\nDBSYNCDVR DBP HEADER" + table.to_table_string()

        table_tlv = DvrTlvEntry.to_packet_string(self)

        return ret_string + "\n\nDVR TLV ENTRIES" + table_tlv.to_table_string()

    def add_dbpdbsyncdvr_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_DBPDBSYNCDVR)

    def build(self):
        self.add_dbpdbsyncdvr_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_dbsyncdvr_dbp_reserved_1_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_header_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_reserved_2_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_id_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_pdu_type_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_reserved_3_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_reserved_4_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_reserved_5_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_pdu_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_remaining_lifetime_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_id_source_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_id_node_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_id_number_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_sequence_number_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_checksum_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_dbp_reserved_6_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_dbpdbsyncdvr(self, tgen_type, generator_ref, port_string, stream_id,
                                                                **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_dbpdbsyncdvr(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_dbpdbsyncdvr(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_dbpdbsyncdvr(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kdbsyncdvrFieldNumber
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = DbsyncDvrDbpPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData

    # update this from the ostinato docs.
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_1()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_1())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_header_length()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_header_length())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_2()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_2())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_id_length()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_id_length())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_pdu_type()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_pdu_type())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_3()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_3())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_4()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_4())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_5()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_5())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_pdu_length()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_pdu_length())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_remaining_lifetime()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_remaining_lifetime())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_id_source()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_id_source())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_id_node()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_id_node())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_id_number()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_id_number())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_sequence_number()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_sequence_number())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_checksum()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_checksum())
    # if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_6()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_dbp_reserved_6())

    def config_jets_stream_dbpdbsyncdvr(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "DBSYNCDVR_HDR"
        pkt_bytes = "0x" + DbsyncDvrDbpPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_1()):
            pkt_fields["dbp_reserved_1"] = int(self.get_dbsyncdvr_dbp_reserved_1())
        if self.is_field_set(self.get_dbsyncdvr_dbp_header_length()):
            pkt_fields["dbp_header_length"] = int(self.get_dbsyncdvr_dbp_header_length())
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_2()):
            pkt_fields["dbp_reserved_2"] = int(self.get_dbsyncdvr_dbp_reserved_2())
        if self.is_field_set(self.get_dbsyncdvr_dbp_id_length()):
            pkt_fields["dbp_id_length"] = int(self.get_dbsyncdvr_dbp_id_length())
        if self.is_field_set(self.get_dbsyncdvr_dbp_pdu_type()):
            pkt_fields["dbp_pdu_type"] = int(self.get_dbsyncdvr_dbp_pdu_type())
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_3()):
            pkt_fields["dbp_reserved_3"] = int(self.get_dbsyncdvr_dbp_reserved_3())
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_4()):
            pkt_fields["dbp_reserved_4"] = int(self.get_dbsyncdvr_dbp_reserved_4())
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_5()):
            pkt_fields["dbp_reserved_5"] = int(self.get_dbsyncdvr_dbp_reserved_5())
        if self.is_field_set(self.get_dbsyncdvr_dbp_pdu_length()):
            pkt_fields["dbp_pdu_length"] = int(self.get_dbsyncdvr_dbp_pdu_length())
        if self.is_field_set(self.get_dbsyncdvr_dbp_remaining_lifetime()):
            pkt_fields["dbp_remaining_lifetime"] = int(self.get_dbsyncdvr_dbp_remaining_lifetime())
        if self.is_field_set(self.get_dbsyncdvr_dbp_id_source()):
            pkt_fields["dbp_id_source"] = int(self.get_dbsyncdvr_dbp_id_source())
        if self.is_field_set(self.get_dbsyncdvr_dbp_id_node()):
            pkt_fields["dbp_id_node"] = int(self.get_dbsyncdvr_dbp_id_node())
        if self.is_field_set(self.get_dbsyncdvr_dbp_id_number()):
            pkt_fields["dbp_id_number"] = int(self.get_dbsyncdvr_dbp_id_number())
        if self.is_field_set(self.get_dbsyncdvr_dbp_sequence_number()):
            pkt_fields["dbp_sequence_number"] = int(self.get_dbsyncdvr_dbp_sequence_number())
        if self.is_field_set(self.get_dbsyncdvr_dbp_checksum()):
            pkt_fields["dbp_checksum"] = int(self.get_dbsyncdvr_dbp_checksum())
        if self.is_field_set(self.get_dbsyncdvr_dbp_reserved_6()):
            pkt_fields["dbp_reserved_6"] = int(self.get_dbsyncdvr_dbp_reserved_6())

    def get_ixtclhal_dbsyncdvr_api_commands(self, port_string, streamid):
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
        dbp_reserved_1 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_1("0x" + dbp_reserved_1)
        payload = self.remove_bits_from_string(8, payload)
        dbp_header_length = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_header_length("0x" + dbp_header_length)
        payload = self.remove_bits_from_string(8, payload)
        dbp_reserved_2 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_2("0x" + dbp_reserved_2)
        payload = self.remove_bits_from_string(8, payload)
        dbp_id_length = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_id_length("0x" + dbp_id_length)
        payload = self.remove_bits_from_string(8, payload)
        dbp_pdu_type = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_pdu_type("0x" + dbp_pdu_type)
        payload = self.remove_bits_from_string(8, payload)
        dbp_reserved_3 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_3("0x" + dbp_reserved_3)
        payload = self.remove_bits_from_string(8, payload)
        dbp_reserved_4 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_4("0x" + dbp_reserved_4)
        payload = self.remove_bits_from_string(8, payload)
        dbp_reserved_5 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_5("0x" + dbp_reserved_5)
        payload = self.remove_bits_from_string(8, payload)
        dbp_pdu_length = self.get_bits_from_string(16, payload)
        self.set_dbsyncdvr_dbp_pdu_length("0x" + dbp_pdu_length)
        payload = self.remove_bits_from_string(16, payload)
        dbp_remaining_lifetime = self.get_bits_from_string(16, payload)
        self.set_dbsyncdvr_dbp_remaining_lifetime("0x" + dbp_remaining_lifetime)
        payload = self.remove_bits_from_string(16, payload)
        dbp_id_source = self.get_bits_from_string(48, payload)
        self.set_dbsyncdvr_dbp_id_source("0x" + dbp_id_source)
        payload = self.remove_bits_from_string(48, payload)
        dbp_id_node = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_id_node("0x" + dbp_id_node)
        payload = self.remove_bits_from_string(8, payload)
        dbp_id_number = self.get_bits_from_string(32, payload)
        self.set_dbsyncdvr_dbp_id_number("0x" + dbp_id_number)
        payload = self.remove_bits_from_string(32, payload)
        dbp_sequence_number = self.get_bits_from_string(32, payload)
        self.set_dbsyncdvr_dbp_sequence_number("0x" + dbp_sequence_number)
        payload = self.remove_bits_from_string(32, payload)
        dbp_checksum = self.get_bits_from_string(16, payload)
        self.set_dbsyncdvr_dbp_checksum("0x" + dbp_checksum)
        payload = self.remove_bits_from_string(16, payload)
        dbp_reserved_6 = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_dbp_reserved_6("0x" + dbp_reserved_6)
        payload = self.remove_bits_from_string(8, payload)
        # processTLVs
        self.payload = DvrTlvEntry.process_tlv(payload, self.tlv_entries, dbp_pdu_length, self)

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_1(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_header_length(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_2(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_id_length(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_pdu_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_3(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_4(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_5(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_pdu_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_remaining_lifetime(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_id_source(), PacketConstants.HEX_STRING, 48)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_id_node(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_id_number(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_sequence_number(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_dbp_reserved_6(), PacketConstants.INTEGER, 8)

        for entry in self.tlv_entries:
            ret_string += self.format_byte_string(entry.type, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.length, PacketConstants.INTEGER, 8)
            ret_string += self.format_byte_string(entry.data, PacketConstants.HEX_STRING, entry.length * 8)
        return ret_string

    @staticmethod
    def compare_dbsyncdvr_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, DbsyncDvrDbpPacketHeader)
            assert isinstance(actual, DbsyncDvrDbpPacketHeader)
            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_1()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_1 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 1 : "
                if expected.get_dbsyncdvr_dbp_reserved_1() != actual.get_dbsyncdvr_dbp_reserved_1():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_1()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_1()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_1()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_1()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_header_length()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_HEADER_LENGTH not in ignore_list:
                name = "DBSYNCDVR dbp header length : "
                if expected.get_dbsyncdvr_dbp_header_length() != actual.get_dbsyncdvr_dbp_header_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_header_length()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_header_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_header_length()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_header_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_2()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_2 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 2 : "
                if expected.get_dbsyncdvr_dbp_reserved_2() != actual.get_dbsyncdvr_dbp_reserved_2():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_2()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_2()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_2()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_2()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_id_length()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_LENGTH not in ignore_list:
                name = "DBSYNCDVR dbp id length : "
                if expected.get_dbsyncdvr_dbp_id_length() != actual.get_dbsyncdvr_dbp_id_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_id_length()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_id_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_id_length()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_id_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_pdu_type()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_TYPE not in ignore_list:
                name = "DBSYNCDVR dbp pdu type : "
                if expected.get_dbsyncdvr_dbp_pdu_type() != actual.get_dbsyncdvr_dbp_pdu_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_pdu_type()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_pdu_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_pdu_type()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_pdu_type()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_3()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_3 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 3 : "
                if expected.get_dbsyncdvr_dbp_reserved_3() != actual.get_dbsyncdvr_dbp_reserved_3():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_3()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_3()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_3()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_3()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_4()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_4 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 4 : "
                if expected.get_dbsyncdvr_dbp_reserved_4() != actual.get_dbsyncdvr_dbp_reserved_4():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_4()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_4()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_4()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_4()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_5()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_5 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 5 : "
                if expected.get_dbsyncdvr_dbp_reserved_5() != actual.get_dbsyncdvr_dbp_reserved_5():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_5()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_5()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_5()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_5()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_pdu_length()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_PDU_LENGTH not in ignore_list:
                name = "DBSYNCDVR dbp pdu length : "
                if expected.get_dbsyncdvr_dbp_pdu_length() != actual.get_dbsyncdvr_dbp_pdu_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_pdu_length()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_pdu_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_pdu_length()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_pdu_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_remaining_lifetime()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_REMAINING_LIFETIME not in ignore_list:
                name = "DBSYNCDVR dbp remaining lifetime : "
                if expected.get_dbsyncdvr_dbp_remaining_lifetime() != actual.get_dbsyncdvr_dbp_remaining_lifetime():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_dbsyncdvr_dbp_remaining_lifetime()) + " != " + str(
                                actual.get_dbsyncdvr_dbp_remaining_lifetime()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvr_dbp_remaining_lifetime()) + " == " + str(
                            actual.get_dbsyncdvr_dbp_remaining_lifetime()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_id_source()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_SOURCE not in ignore_list:
                name = "DBSYNCDVR dbp id source : "
                if expected.get_dbsyncdvr_dbp_id_source() != actual.get_dbsyncdvr_dbp_id_source():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_id_source()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_id_source()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_id_source()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_id_source()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_id_node()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NODE not in ignore_list:
                name = "DBSYNCDVR dbp id node : "
                if expected.get_dbsyncdvr_dbp_id_node() != actual.get_dbsyncdvr_dbp_id_node():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_id_node()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_id_node()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_id_node()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_id_node()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_id_number()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_ID_NUMBER not in ignore_list:
                name = "DBSYNCDVR dbp id number : "
                if expected.get_dbsyncdvr_dbp_id_number() != actual.get_dbsyncdvr_dbp_id_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_id_number()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_id_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_id_number()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_id_number()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_sequence_number()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_SEQUENCE_NUMBER not in ignore_list:
                name = "DBSYNCDVR dbp sequence number : "
                if expected.get_dbsyncdvr_dbp_sequence_number() != actual.get_dbsyncdvr_dbp_sequence_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_sequence_number()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_sequence_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_dbsyncdvr_dbp_sequence_number()) + " == " + str(
                            actual.get_dbsyncdvr_dbp_sequence_number()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_checksum()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_CHECKSUM not in ignore_list:
                name = "DBSYNCDVR dbp checksum : "
                if expected.get_dbsyncdvr_dbp_checksum() != actual.get_dbsyncdvr_dbp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_checksum()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_checksum()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_checksum()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_dbp_reserved_6()) and \
                    DbsyncDvrDbpPacketConstants.DBSYNCDVR_DBP_RESERVED_6 not in ignore_list:
                name = "DBSYNCDVR dbp reserved 6 : "
                if expected.get_dbsyncdvr_dbp_reserved_6() != actual.get_dbsyncdvr_dbp_reserved_6():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_dbp_reserved_6()) + " != " + str(
                            actual.get_dbsyncdvr_dbp_reserved_6()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_dbp_reserved_6()) + " == " + str(
                        actual.get_dbsyncdvr_dbp_reserved_6()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with DbsyncDvrDbpPacketHeader")
        return results


class DbsyncDvrDbpPacketConstants:
    def __init__(self):
        pass

    DBSYNCDVR_VERSION = "DBSYNCDVR_VERSION"
    DBSYNCDVR_VERSION_ETHERNET = "1"
    DBSYNCDVR_VERSIONS = {1: "Ethernet",
                          }

    DBSYNCDVR_DBP_RESERVED_1 = "DBSYNCDVR_DBP_RESERVED_1"
    DBSYNCDVR_DBP_HEADER_LENGTH = "DBSYNCDVR_DBP_HEADER_LENGTH"
    DBSYNCDVR_DBP_RESERVED_2 = "DBSYNCDVR_DBP_RESERVED_2"
    DBSYNCDVR_DBP_ID_LENGTH = "DBSYNCDVR_DBP_ID_LENGTH"
    DBSYNCDVR_DBP_PDU_TYPE = "DBSYNCDVR_DBP_PDU_TYPE"
    DBSYNCDVR_DBP_RESERVED_3 = "DBSYNCDVR_DBP_RESERVED_3"
    DBSYNCDVR_DBP_RESERVED_4 = "DBSYNCDVR_DBP_RESERVED_4"
    DBSYNCDVR_DBP_RESERVED_5 = "DBSYNCDVR_DBP_RESERVED_5"
    DBSYNCDVR_DBP_PDU_LENGTH = "DBSYNCDVR_DBP_PDU_LENGTH"
    DBSYNCDVR_DBP_REMAINING_LIFETIME = "DBSYNCDVR_DBP_REMAINING_LIFETIME"
    DBSYNCDVR_DBP_ID_SOURCE = "DBSYNCDVR_DBP_ID_SOURCE"
    DBSYNCDVR_DBP_ID_NODE = "DBSYNCDVR_DBP_ID_NODE"
    DBSYNCDVR_DBP_ID_NUMBER = "DBSYNCDVR_DBP_ID_NUMBER"
    DBSYNCDVR_DBP_SEQUENCE_NUMBER = "DBSYNCDVR_DBP_SEQUENCE_NUMBER"
    DBSYNCDVR_DBP_CHECKSUM = "DBSYNCDVR_DBP_CHECKSUM"
    DBSYNCDVR_DBP_RESERVED_6 = "DBSYNCDVR_DBP_RESERVED_6"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
