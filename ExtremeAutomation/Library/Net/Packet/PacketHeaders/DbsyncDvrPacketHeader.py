import binascii
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject


class DbsyncDvrPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    DB Sync DVR Packet
        # Version = 8bits
        # App Id = 4*32bits
        # Packet Type = 8bits
        # Packet Length = 16bits
        # Source ID = 6*8bits
    """

    def __init__(self):
        self.add_dbsyncdvr_header()
        self.HEADER_SIZE_DBSYNCDVR = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start DbsyncDvr Version methods
    #  version is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_version(self, version, ignore_check=False):
        version = self.normalize_value(version, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_DBSYNCDVR,
                                  DbsyncDvrPacketConstants.DBSYNCDVR_VERSION, version)

    def get_dbsyncdvr_version(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_VERSION),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_version_hltapi_cmd(self, dummy_dict):
        version = self.get_dbsyncdvr_version()
        if isinstance(version, int):
            version = str(version)
        if version and 'Not Set' not in version:
            dummy_dict[TrafficConfigConstants.TEMP_VERSION_CMD] = version
    # end DbsyncDvr Version methods

    # start DbsyncDvr App Id methods
    #  app_id is a 16 bit INTEGER example: 1
    def set_dbsyncdvr_app_id(self, app_id, ignore_check=False):
        app_id = self.normalize_value(app_id, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_APP_ID,
                                  app_id)

    def get_dbsyncdvr_app_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_APP_ID),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_app_id_hltapi_cmd(self, dummy_dict):
        app_id = self.get_dbsyncdvr_app_id()
        if isinstance(app_id, int):
            app_id = str(app_id)
        if app_id and 'Not Set' not in app_id:
            dummy_dict[TrafficConfigConstants.TEMP_APP_ID_CMD] = app_id
    # end DbsyncDvr App Id methods

    # start DbsyncDvr Packet Type methods
    #  packet_type is a 8 bit INTEGER example: 1
    def set_dbsyncdvr_packet_type(self, packet_type, ignore_check=False):
        packet_type = self.normalize_value(packet_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_DBSYNCDVR,
                                  DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_TYPE, packet_type)

    def get_dbsyncdvr_packet_type(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_TYPE),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_packet_type_hltapi_cmd(self, dummy_dict):
        packet_type = self.get_dbsyncdvr_packet_type()
        if isinstance(packet_type, int):
            packet_type = str(packet_type)
        if packet_type and 'Not Set' not in packet_type:
            dummy_dict[TrafficConfigConstants.TEMP_PACKET_TYPE_CMD] = packet_type
    # end DbsyncDvr Packet Type methods

    # start DbsyncDvr Packet Length methods
    #  packet_length is a 16 bit INTEGER example: 1
    def set_dbsyncdvr_packet_length(self, packet_length, ignore_check=False):
        packet_length = self.normalize_value(packet_length, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_DBSYNCDVR,
                                  DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_LENGTH, packet_length)

    def get_dbsyncdvr_packet_length(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_LENGTH),
            PacketConstants.INTEGER)

    def get_dbsyncdvr_packet_length_hltapi_cmd(self, dummy_dict):
        packet_length = self.get_dbsyncdvr_packet_length()
        if isinstance(packet_length, int):
            packet_length = str(packet_length)
        if packet_length and 'Not Set' not in packet_length:
            dummy_dict[TrafficConfigConstants.TEMP_PACKET_LENGTH_CMD] = packet_length
    # end DbsyncDvr Packet Length methods

    # start DbsyncDvr Source ID methods
    #  source_id is a 32 bit HEX_STRING example: FFFFFFFF
    def set_dbsyncdvr_source_id(self, source_id, ignore_check=False):
        source_id = self.normalize_value(source_id, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_DBSYNCDVR,
                                  DbsyncDvrPacketConstants.DBSYNCDVR_SOURCE_ID, source_id)

    def get_dbsyncdvr_source_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_DBSYNCDVR, DbsyncDvrPacketConstants.DBSYNCDVR_SOURCE_ID),
            PacketConstants.HEX_STRING)

    def get_dbsyncdvr_source_id_hltapi_cmd(self, dummy_dict):
        source_id = self.get_dbsyncdvr_source_id()
        if source_id and 'Not Set' not in source_id:
            dummy_dict[TrafficConfigConstants.TEMP_SOURCE_ID_CMD] = source_id
    # end DbsyncDvr Source ID methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Version", self.format_int(self.get_dbsyncdvr_version(), 1))
        table.add_row_value("App Id", self.format_int(self.get_dbsyncdvr_app_id(), 4))
        table.add_row_value("Packet Type", self.format_int(self.get_dbsyncdvr_packet_type(), 1))
        table.add_row_value("Packet Length", self.format_int(self.get_dbsyncdvr_packet_length(), 2))
        table.add_row_value("Source ID", self.get_dbsyncdvr_source_id())
        ret_string = table.to_table_string()
        return "\n\nDBSYNCDVR HEADER" + ret_string

    def add_dbsyncdvr_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_DBSYNCDVR)

    def build(self):
        self.add_dbsyncdvr_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_dbsyncdvr_version_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_app_id_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_packet_type_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_packet_length_hltapi_cmd(dummy_dict)
        # self.get_dbsyncdvr_source_id_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_dbsyncdvr(self, tgen_type, generator_ref, port_string, stream_id,
                                                             **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_dbsyncdvr(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_dbsyncdvr(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_dbsyncdvr(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kdbsyncdvrFieldNumber
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = DbsyncDvrPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
    # update this from the ostinato docs.
    # dbsyncdvrField = p.Extensions[dbsyncdvr]
    # if self.is_field_set(self.get_dbsyncdvr_version()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_version())
    # if self.is_field_set(self.get_dbsyncdvr_app_id()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_app_id())
    # if self.is_field_set(self.get_dbsyncdvr_packet_type()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_packet_type())
    # if self.is_field_set(self.get_dbsyncdvr_packet_length()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_packet_length())
    # if self.is_field_set(self.get_dbsyncdvr_source_id()) :
    #    dbsyncdvrField.version = int(self.get_dbsyncdvr_source_id())

    def config_jets_stream_dbsyncdvr(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "DBSYNCDVR_HDR"
        pkt_bytes = "0x" + DbsyncDvrPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        if self.is_field_set(self.get_dbsyncdvr_version()):
            pkt_fields["version"] = int(self.get_dbsyncdvr_version())
        if self.is_field_set(self.get_dbsyncdvr_app_id()):
            pkt_fields["app_id"] = int(self.get_dbsyncdvr_app_id())
        if self.is_field_set(self.get_dbsyncdvr_packet_type()):
            pkt_fields["packet_type"] = int(self.get_dbsyncdvr_packet_type())
        if self.is_field_set(self.get_dbsyncdvr_packet_length()):
            pkt_fields["packet_length"] = int(self.get_dbsyncdvr_packet_length())
        if self.is_field_set(self.get_dbsyncdvr_source_id()):
            pkt_fields["source_id"] = int(self.get_dbsyncdvr_source_id())

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
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        version = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_version("0x" + version)
        payload = self.remove_bits_from_string(8, payload)
        app_id = self.get_bits_from_string(32, payload)
        self.set_dbsyncdvr_app_id("0x" + app_id)
        payload = self.remove_bits_from_string(32, payload)
        packet_type = self.get_bits_from_string(8, payload)
        self.set_dbsyncdvr_packet_type("0x" + packet_type)
        payload = self.remove_bits_from_string(8, payload)
        packet_length = self.get_bits_from_string(16, payload)
        self.set_dbsyncdvr_packet_length("0x" + packet_length)
        payload = self.remove_bits_from_string(16, payload)
        source_id = self.get_bits_from_string(6 * 8, payload)
        self.set_dbsyncdvr_source_id("0x" + source_id)
        payload = self.remove_bits_from_string(6 * 8, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_dbsyncdvr_version(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_app_id(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_packet_type(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_packet_length(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_dbsyncdvr_source_id(), PacketConstants.HEX_STRING, 6 * 8)
        return ret_string

    @staticmethod
    def compare_dbsyncdvr_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, DbsyncDvrPacketHeader)
            assert isinstance(actual, DbsyncDvrPacketHeader)
            if expected.is_field_set(
                    expected.get_dbsyncdvr_version()) and DbsyncDvrPacketConstants.DBSYNCDVR_VERSION not in ignore_list:
                name = "DBSYNCDVR version : "
                if expected.get_dbsyncdvr_version() != actual.get_dbsyncdvr_version():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_version()) + " != " +
                                                      str(actual.get_dbsyncdvr_version()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_version()) + " == " +
                                                 str(actual.get_dbsyncdvr_version()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_app_id()) and DbsyncDvrPacketConstants.DBSYNCDVR_APP_ID not in ignore_list:
                name = "DBSYNCDVR app id : "
                if expected.get_dbsyncdvr_app_id() != actual.get_dbsyncdvr_app_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_app_id()) + " != " +
                                                      str(actual.get_dbsyncdvr_app_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_app_id()) + " == " +
                                                 str(actual.get_dbsyncdvr_app_id()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_packet_type()) and \
                    DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_TYPE not in ignore_list:
                name = "DBSYNCDVR packet type : "
                if expected.get_dbsyncdvr_packet_type() != actual.get_dbsyncdvr_packet_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_packet_type()) + " != " +
                                                      str(actual.get_dbsyncdvr_packet_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_packet_type()) + " == " +
                                                 str(actual.get_dbsyncdvr_packet_type()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_packet_length()) and \
                    DbsyncDvrPacketConstants.DBSYNCDVR_PACKET_LENGTH not in ignore_list:
                name = "DBSYNCDVR packet length : "
                if expected.get_dbsyncdvr_packet_length() != actual.get_dbsyncdvr_packet_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_packet_length()) + " != " +
                                                      str(actual.get_dbsyncdvr_packet_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_packet_length()) + " == " +
                                                 str(actual.get_dbsyncdvr_packet_length()) + " Pass")

            if expected.is_field_set(
                    expected.get_dbsyncdvr_source_id()) and \
                    DbsyncDvrPacketConstants.DBSYNCDVR_SOURCE_ID not in ignore_list:
                name = "DBSYNCDVR source id : "
                if expected.get_dbsyncdvr_source_id() != actual.get_dbsyncdvr_source_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_dbsyncdvr_source_id()) + " != " +
                                                      str(actual.get_dbsyncdvr_source_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_dbsyncdvr_source_id()) + " == " +
                                                 str(actual.get_dbsyncdvr_source_id()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with DbsyncDvrPacketHeader")
        return results


class DbsyncDvrPacketConstants:
    def __init__(self):
        pass

    DBSYNCDVR_VERSION = "DBSYNCDVR_VERSION"
    DBSYNCDVR_VERSION_ETHERNET = "1"
    DBSYNCDVR_VERSIONS = {1: "Ethernet",
                          }

    DBSYNCDVR_APP_ID = "DBSYNCDVR_APP_ID"
    DBSYNCDVR_PACKET_TYPE = "DBSYNCDVR_PACKET_TYPE"
    DBSYNCDVR_PACKET_LENGTH = "DBSYNCDVR_PACKET_LENGTH"
    DBSYNCDVR_SOURCE_ID = "DBSYNCDVR_SOURCE_ID"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class DvrTlvEntry(object):
    def __init__(self, pkt_type, length, data):
        self.pkt_type = pkt_type
        # self.type_string = self.get_type_string(pkt_type)
        self.length = length
        self.data = data

    def get_type_string(self, pkt_type):
        if pkt_type == 0x01:
            return "Area Address(es)"
        else:
            return "Unknown Type"

    @staticmethod
    def process_tlv(payload, tlv_entries, pdu_length, handler):
        pdu_length = int(pdu_length, 16)
        try:
            while pdu_length > 0 and payload.replace("0", "").strip() != "":
                tlv_type = handler.get_bits_from_string(8, payload)
                tlv_type = int(tlv_type, 16)
                payload = handler.remove_bits_from_string(8, payload)
                pdu_length -= 1
                tlv_length = handler.get_bits_from_string(8, payload)
                tlv_length = int(tlv_length, 16)
                payload = handler.remove_bits_from_string(8, payload)
                pdu_length -= 1
                tlv_data = handler.get_bits_from_string(tlv_length * 8, payload)
                payload = handler.remove_bits_from_string(tlv_length * 8, payload)
                pdu_length -= tlv_length
                tlv_entries.append(DvrTlvEntry(tlv_type, tlv_length, tlv_data))
        except Exception as e:
            PacketObject.logger.log_info(repr(e))
        return payload

    @staticmethod
    def to_packet_string(packet):
        table_tlv = TableFormatter()
        for entry in packet.tlv_entries:
            # table_tlv.add_row_value("type",  entry.type_string + " " + packet.format_int(entry.type, 1))
            table_tlv.add_row_value("type", packet.format_int(entry.type, 1))
            table_tlv.add_row_value("length", packet.format_int(entry.length, 1))
            table_tlv.add_row_value("data", entry.data)
        return table_tlv
