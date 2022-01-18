from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.llc_pb2 import llc
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.dot3_pb2 import dot3
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class SapPacketHeader(object):
    packet_name = None
    pkt_bytes = None

    def __init__(self):
        self.add_ipx_header()
        self.HEADER_SIZE_SAP = 4 + 2 + 2 + 2

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("LLC Length", self.format_int(self.get_llc_length(), 4))
        table.add_row_value("DSAP", self.format_int(self.get_llc_dsap(), 2))
        table.add_row_value("SSAP", self.format_int(self.get_llc_ssap(), 2))
        table.add_row_value("Control", self.format_int(self.get_llc_control(), 2))
        return "\n\nIPX HEADER" + table.to_table_string()

    # start of the lls portion
    def set_llc_length(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(Ieee803LlcPacketConstants.LLC_LENGTH, ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_LENGTH, pkt_type)

    def get_llc_length(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_LENGTH),
            PacketConstants.INTEGER)

    def get_llc_length_hltpapi_cmd(self, dummy_dict):
        ttl = self.get_llc_length()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.ETHERNET_VALUE_CMD] = ttl
    # end of the lls portion

    # start of the dsap portion
    def set_llc_dsap(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(Ieee803LlcPacketConstants.LLC_DSAP, ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_DSAP, pkt_type)

    def get_llc_dsap(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_DSAP),
            PacketConstants.INTEGER)
    # end of the dsap portion

    # start of the ssap portion
    def set_llc_ssap(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(Ieee803LlcPacketConstants.LLC_SSAP, ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_SSAP, pkt_type)

    def get_llc_ssap(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_SSAP),
            PacketConstants.INTEGER)
    # end of the ssap portion

    # start of the ssap portion
    def set_llc_control(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(Ieee803LlcPacketConstants.LLC_CTL, ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_CTL, pkt_type)

    def get_llc_control(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_LLC, Ieee803LlcPacketConstants.LLC_CTL),
            PacketConstants.INTEGER)
    # end of the ssap portion

    def add_ipx_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_LLC)

    def build(self):
        self.add_ipx_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        dummy_dict[TrafficConfigConstants.ETHERNET_TYPE_CMD] = TrafficConfigConstants.ETHERNET_TYPE_IEEE8023
        self.get_llc_length_hltpapi_cmd(dummy_dict)
        return dummy_dict

    def get_ixtclhal_sap_api_commands(self, port, streamid):
        dummy_dict = []
        protocol_pad = ""
        if self.is_field_set(self.get_llc_dsap()):
            protocol_pad += (hex(self.get_llc_dsap())[2:]).zfill(2)
        else:
            protocol_pad += "00"
        protocol_pad += " "
        if self.is_field_set(self.get_llc_ssap()):
            protocol_pad += (hex(self.get_llc_ssap())[2:]).zfill(2)
        else:
            protocol_pad += "00"
        protocol_pad += " "
        if self.is_field_set(self.get_llc_control()):
            protocol_pad += (hex(self.get_llc_control())[2:]).zfill(2)
        else:
            protocol_pad += "00"
        dummy_dict.append("stream get " + port + " " + str(streamid))
        dummy_dict.append("protocol config -enableProtocolPad                  true")
        dummy_dict.append("protocolPad setDefault")
        dummy_dict.append("protocolPad config -dataBytes \"" + protocol_pad + "\"")
        dummy_dict.append("protocolPad set " + port)
        dummy_dict.append("stream set " + port + " " + str(streamid))
        dummy_dict.append("stream write " + port + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_sap_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_llc(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_llc(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_llc(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_llc(self, drone, port_string, stream_id, **kwargs):

        p = stream_id.protocol.add()
        if "Snap" in self.get_name():
            p.protocol_id.id = ost_pb.Protocol.kDot2SnapFieldNumber
        else:
            p.protocol_id.id = ost_pb.Protocol.kDot2LlcFieldNumber
        dot3Field = p.Extensions[dot3]
        if self.is_field_set(self.get_llc_length()):
            dot3Field.is_override_length = True
            dot3Field.length = int(self.get_llc_length())
        else:
            dot3Field.is_override_length = False

        # self.get_llc_length_hltpapi_cmd(dummy_dict)

        # ctl = {int} 0
        # is_override_ctl = {bool} False
        # self.get_llc_control_hltpapi_cmd(dummy_dict)
        llcField = p.Extensions[llc]
        if self.is_field_set(self.get_llc_control()):
            llcField.ctl = int(self.get_llc_control())
            llcField.is_override_ctl = True
        else:
            llcField.is_override_ctl = False

        # dsap = {int} 0
        # is_override_dsap = {bool} False
        # self.get_llc_dsap_hltpapi_cmd(dummy_dict)
        if self.is_field_set(self.get_llc_dsap()):
            llcField.dsap = int(self.get_llc_dsap())
            llcField.is_override_dsap = True
        else:
            llcField.is_override_dsap = False
        # ssap = {int} 0
        # is_override_ssap = {bool} False
        # self.get_llc_ssap_hltpapi_cmd(dummy_dict)
        if self.is_field_set(self.get_llc_ssap()):
            llcField.ssap = int(self.get_llc_ssap())
            llcField.is_override_ssap = True
        else:
            llcField.is_override_ssap = False

    def config_jets_stream_llc(self, jets_dev, port_string, stream_id, **kwargs):
        """
        LLC
        {
            dsap: 8: default = 0xaa, display = "Destination SAP", index = 1;
            ssap: 8: default = 0xaa,  display = "Source      SAP", index = 2;
            ctrl: 8: default = 0x03, legal_values = (Supervisory_RR=1, Unnumbered_UI=3, Supervisory_RNR=5,
                     Supervisory_REJ=9, Unnum_DM=0x0f, Unnum_DM_FINAL=0x1f, Unnum_DISC=0x43, Unnum_DISC_POLL=0x53,
                     Unnum_UA=0x63, Unnum_UA_FINAL=0x73, Unnum_SABME=0x6f, Unnum_SABME_POLL=0x7f, Unnum_FRMR=0x87,
                     Unnum_FRMR_FINAL=0x97, Unnum_XID=0xaf, Unnum_XID_PF=0xbf, Unnum_TEST=0xe3, Unnum_TEST_PF=0xf3),
                     display = "Control", index = 3;
        } display = "LLC (Logical Link Control) HDR", index = 7004;
        """
        pkt_fields = {}
        if self.is_field_set(self.get_llc_dsap()):
            pkt_fields["dsap"] = str(self.get_llc_dsap())
        if self.is_field_set(self.get_llc_ssap()):
            pkt_fields["ssap"] = str(self.get_llc_ssap())
        if self.is_field_set(self.get_llc_control()):
            pkt_fields["ctrl"] = str(self.get_llc_control())
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.LLC_HDR, pkt_fields)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        length = self.get_bits_from_string(16, payload)
        self.set_llc_length("0x" + length)
        payload = self.remove_bits_from_string(16, payload)

        dsap = self.get_bits_from_string(8, payload)
        self.set_llc_dsap("0x" + dsap)
        payload = self.remove_bits_from_string(8, payload)

        ssap = self.get_bits_from_string(8, payload)
        self.set_llc_ssap("0x" + ssap)
        payload = self.remove_bits_from_string(8, payload)
        self.payload = payload

        control = self.get_bits_from_string(8, payload)
        self.set_llc_control("0x" + control)
        payload = self.remove_bits_from_string(8, payload)
        self.payload = payload

    def get_header_bytes(self):
        da = self.format_byte_string(self.get_llc_length(), PacketConstants.INTEGER, 16)
        da += self.format_byte_string(self.get_llc_dsap(), PacketConstants.INTEGER, 8)
        da += self.format_byte_string(self.get_llc_ssap(), PacketConstants.INTEGER, 8)
        da += self.format_byte_string(self.get_llc_control(), PacketConstants.INTEGER, 8)
        return da

    @staticmethod
    def compare_llc_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, SapPacketHeader)
            assert isinstance(actual, SapPacketHeader)

            if expected.is_field_set(expected.get_llc_control()):
                name = "LLC Control : "
                if expected.get_llc_control() != actual.get_llc_control():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_llc_control()) + " != " +
                                                      str(actual.get_llc_control()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_llc_control()) + " == " +
                                                 str(actual.get_llc_control()) + " Pass")

            if expected.is_field_set(expected.get_llc_dsap()):
                name = "LLC Control : "
                if expected.get_llc_dsap() != actual.get_llc_dsap():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_llc_dsap()) + " != " +
                                                      str(actual.get_llc_dsap()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_llc_dsap()) + " == " +
                                                 str(actual.get_llc_dsap()) + " Pass")

            if expected.is_field_set(expected.get_llc_ssap()):
                name = "LLC Control : "
                if expected.get_llc_ssap() != actual.get_llc_ssap():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_llc_ssap()) + " != " +
                                                      str(actual.get_llc_ssap()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_llc_ssap()) + " == " +
                                                 str(actual.get_llc_ssap()) + " Pass")

            if expected.is_field_set(expected.get_llc_length()):
                name = "LLC Control : "
                if expected.get_llc_length() != actual.get_llc_length():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_llc_length()) + " != " +
                                                      str(actual.get_llc_length()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_llc_length()) + " == " +
                                                 str(actual.get_llc_length()) + " Pass")

        except Exception as e:
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Ieee803LlcPacketHeader failed")
            results = False

        return results


class Ieee803LlcPacketConstants:
    LLC_LENGTH = "LLC_LENGTH"
    LLC_DSAP = "LLC_DSAP"
    LLC_SSAP = "LLC_SSAP"
    LLC_CTL = "LLC_CTL"

    def __init__(self):
        pass

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
