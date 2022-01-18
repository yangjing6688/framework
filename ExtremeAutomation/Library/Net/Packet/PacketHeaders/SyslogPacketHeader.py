###########################################################################
# ###   start SyslogPacketHeader
###########################################################################
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
# from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer5PacketHeader import Layer5PacketHeader
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
# from ExtremeAutomation.Library.Utils.NumberUtils import *
# import ostinato # pip install python-ostinato
# from ostinato.core import ost_pb, DroneProxy
# # from ostinato.protocols.syslog_pb2 import syslog
# import binascii


# from ostinato.core import ost_pb
# from ostinato.protocols.hexdump_pb2 import hexDump


class SyslogPacketHeader(Layer5PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    init function
        # Facility = 8bits
        # Level = 8bits
        # Message = 8bits
    """

    def __init__(self):
        self.add_syslog_header()
        self.HEADER_SIZE_SYSLOG = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Syslog Facility methods
    #  facility is a 8 bit INTEGER example: 1
    def set_syslog_facility_and_level(self, facility, ignore_check=False):
        facility = self.normalize_value(facility, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_SYSLOG,
                                  SyslogPacketConstants.SYSLOG_FACILITY_AND_LEVEL, facility)

    def get_syslog_facility_and_level(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_SYSLOG,
                                                              SyslogPacketConstants.SYSLOG_FACILITY_AND_LEVEL),
                                    PacketConstants.INTEGER)

    def get_syslog_facility_and_level_hltapi_cmd(self, dummy_dict):
        facility = self.get_syslog_facility_and_level()
        if isinstance(facility, int):
            facility = str(facility)
        if facility and 'Not Set' not in facility:
            dummy_dict[TrafficConfigConstants.TEMP_FACILITY_CMD] = facility

    # end Syslog Facility methods

    # start Syslog Message methods
    #  message is a 8 bit ASCII_STRING example: 1
    def set_syslog_message(self, message, ignore_check=False):
        if not message.startswith("0x"):
            message = self.normalize_value(message, PacketConstants.ASCII_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_SYSLOG, SyslogPacketConstants.SYSLOG_MESSAGE,
                                  message)

    def get_syslog_message(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L3_SYSLOG, SyslogPacketConstants.SYSLOG_MESSAGE),
            PacketConstants.HEX_STRING)

    def get_syslog_message_hltapi_cmd(self, dummy_dict):
        message = self.get_syslog_message()
        if message and 'Not Set' not in message:
            dummy_dict[TrafficConfigConstants.TEMP_MESSAGE_CMD] = message

    # end Syslog Message methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Facility", self.format_int(self.get_syslog_facility_and_level(), 3))
        table.add_row_value("Facility", self.format_hex_to_ascii(self.get_syslog_facility_and_level(), 3))
        table.add_row_value("Message", self.get_syslog_message())
        table.add_row_value("Message", self.format_hex_to_ascii(self.get_syslog_message(), -1))
        return "\n\nSYSLOG HEADER" + table.to_table_string()

    def add_syslog_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_SYSLOG)

    def build(self):
        self.add_syslog_header()
        self.set_source_port(514, True)
        self.set_destination_port(514, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_syslog_facility_hltapi_cmd(dummy_dict)
        # self.get_syslog_level_hltapi_cmd(dummy_dict)
        # self.get_syslog_message_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_syslog(self, tgen_type, generator_ref, port_string, stream_id,
                                                          **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_syslog(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_syslog(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_syslog(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        # p.protocol_id.id = ost_pb.Protocol.ksyslogFieldNumber
        # p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        # payloadData = SyslogPacketHeader.get_header_bytes(self).replace(, )
        # payloadData = binascii.a2b_hex(payloadData)
        # p.Extensions[hexDump].content = payloadData

    # update this from the ostinato docs.
    # syslogField = p.Extensions[syslog]
    # if self.is_field_set(self.get_syslog_facility()) :
    #    syslogField.version = int(self.get_syslog_facility())
    # if self.is_field_set(self.get_syslog_level()) :
    #    syslogField.version = int(self.get_syslog_level())
    # if self.is_field_set(self.get_syslog_message()) :
    #    syslogField.version = int(self.get_syslog_message())

    def config_jets_stream_syslog(self, jets_dev, port_string, stream_id, **kwargs):
        # pkt_fields = {}
        header_name = "SYSLOG_HDR"
        pkt_bytes = "0x" + SyslogPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_syslog_facility_and_level()):
        #     pkt_fields["facility"] = int(self.get_syslog_facility_and_level())
        # if self.is_field_set(self.get_syslog_message()):
        #     pkt_fields["message"] = int(self.get_syslog_message())

    def get_ixtclhal_syslog_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        payload = SyslogPacketHeader.get_header_bytes(self)
        payload = StringUtils.place_character_every_n_characters(payload.replace(" ", ""), " ", 2)
        dummy_dict.append("stream config -patternType                        nonRepeat")
        dummy_dict.append("stream config -dataPattern                        userpattern")
        dummy_dict.append("stream config -pattern                            \"" + payload + "\"")
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
        facility_and_level = self.get_bits_from_string(8 * 5, payload)
        self.set_syslog_facility_and_level("0x" + facility_and_level)
        payload = self.remove_bits_from_string(8 * 5, payload)
        message = payload
        self.set_syslog_message("0x" + message)
        payload = ""
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_syslog_facility_and_level(), PacketConstants.INTEGER, 8 * 5)
        if self.get_syslog_message().startswith("0x"):
            ret_string += self.get_syslog_message()[2:]
        else:
            ret_string += self.format_byte_string(self.get_syslog_message(), PacketConstants.ASCII_STRING)
        return ret_string

    @staticmethod
    def compare_syslog_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, SyslogPacketHeader)
            assert isinstance(actual, SyslogPacketHeader)
            if expected.is_field_set(
                    expected.get_syslog_facility_and_level()) and \
                    SyslogPacketConstants.SYSLOG_FACILITY_AND_LEVEL not in ignore_list:
                name = "SYSLOG facility : "
                if expected.get_syslog_facility_and_level() != actual.get_syslog_facility_and_level():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_syslog_facility_and_level()) + " != " + str(
                            actual.get_syslog_facility_and_level()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_syslog_facility_and_level()) + " == " + str(
                        actual.get_syslog_facility_and_level()) + " Pass")

            if expected.is_field_set(
                    expected.get_syslog_message()) and SyslogPacketConstants.SYSLOG_MESSAGE not in ignore_list:
                name = "SYSLOG message : "
                if expected.get_syslog_message() != actual.get_syslog_message():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(
                            str(expected.get_syslog_message()) + " != " + str(actual.get_syslog_message()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(
                        name + str(expected.get_syslog_message()) + " == " + str(actual.get_syslog_message()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with SyslogPacketHeader")
        return results


class SyslogPacketConstants:
    """
    init function
    """

    def __init__(self):
        pass

    SYSLOG_FACILITY_AND_LEVEL = "SYSLOG_FACILITY"

    SYSLOG_LEVEL = "SYSLOG_LEVEL"

    SYSLOG_MESSAGE = "SYSLOG_MESSAGE"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
###########################################################################
# ###   end SyslogPacketHeader
###########################################################################
