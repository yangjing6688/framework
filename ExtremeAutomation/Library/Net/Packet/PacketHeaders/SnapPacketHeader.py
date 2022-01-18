from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.snap_pb2 import snap
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class SnapPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    SNAP Packet Header
        # organization code = 24bits
        # ether type = 16bits
    """

    def __init__(self):
        self.add_snap_header()
        self.HEADER_SIZE_SNAP = (24 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Snap organization code methods
    #  organization_code is a 24 bit INTEGER example: 1
    def set_snap_organization_code(self, organization_code, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(SnapPacketConstants.SNAP_ORGANIZATION_CODE, ignore_check)
        organization_code = self.normalize_value(organization_code, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_SNAP, SnapPacketConstants.SNAP_ORGANIZATION_CODE,
                                  organization_code)

    def get_snap_organization_code(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_SNAP,
                                                              SnapPacketConstants.SNAP_ORGANIZATION_CODE),
                                    PacketConstants.INTEGER)

    def get_snap_organization_code_hltapi_cmd(self, dummy_dict):
        organization_code = self.get_snap_organization_code()
        if isinstance(organization_code, int):
            organization_code = str(organization_code)
        if organization_code and 'Not Set' not in organization_code:
            dummy_dict[TrafficConfigConstants.TEMP_ORGANIZATION_CODE_CMD] = organization_code
    # end Snap organization code methods

    # start Snap ether type methods
    #  ether_type is a 16 bit INTEGER example: 1
    def set_snap_ether_type(self, ether_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(SnapPacketConstants.SNAP_ETHER_TYPE, ignore_check)
        ether_type = self.normalize_value(ether_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_SNAP, SnapPacketConstants.SNAP_ETHER_TYPE,
                                  ether_type)

    def get_snap_ether_type(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_SNAP, SnapPacketConstants.SNAP_ETHER_TYPE),
            PacketConstants.INTEGER)

    # these are just wrapper so the keywords are easier
    def set_ether_type(self, ether_type, ignore_check=False):
        self.set_ether_type(ether_type, ignore_check=False)

    # these are just wrapper so the keywords are easier
    def get_ether_type(self):
        return self.get_snap_ether_type()

    def get_snap_ether_type_hltapi_cmd(self, dummy_dict):
        ether_type = self.get_snap_ether_type()
        if isinstance(ether_type, int):
            ether_type = str(ether_type)
        if ether_type and 'Not Set' not in ether_type:
            dummy_dict[TrafficConfigConstants.TEMP_ETHER_TYPE_CMD] = ether_type
    # end Snap ether type methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("organization code", self.format_int(self.get_snap_organization_code(), 6))
        table.add_row_value("ether type", self.format_int(self.get_snap_ether_type(), 4))
        return "\n\nSNAP HEADER" + table.to_table_string()

    def add_snap_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_SNAP)
        self.set_llc_dsap("0xAA", True)
        self.set_llc_ssap("0xAA", True)

    def build(self):
        self.add_snap_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_snap_organization_code_hltapi_cmd(dummy_dict)
        # self.get_snap_ether_type_hltapi_cmd(dummy_dict)
        dummy_dict[TrafficConfigConstants.ETHERNET_TYPE_CMD] = TrafficConfigConstants.ETHERNET_TYPE_IEEE8023SNAP
        return dummy_dict

    def get_ixtclhal_snap_api_commands(self, port_string, streamid):
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

    def get_spirent_snap_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_snap(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_snap(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_snap(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_snap(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol._values[-1]  # get the snap packet protocol header
        snapField = p.Extensions[snap]
        # oui = {int} 0
        # is_override_oui = {bool} False
        if self.is_field_set(self.get_snap_organization_code()):
            snapField.oui = int(self.get_snap_organization_code())
            snapField.is_override_oui = True
        else:
            snapField.is_override_oui = False
        # type = {int} 0
        # is_override_type = {bool} False
        if self.is_field_set(self.get_snap_ether_type()):
            snapField.type = int(self.get_snap_ether_type())
            snapField.is_override_type = True
        else:
            snapField.is_override_type = False

    def config_jets_stream_snap(self, jets_dev, port_string, stream_id, **kwargs):
        """
        SNAP_HDR {
          msid : 24 : display="Manufacturer ID", index=1;
          type : 16 : default=0x0800, display="Type", index=2;
        } display="SNAP (Sub-Network Access Protocol)", index=7013;
        """
        pkt_fields = {}
        # try:
        #     last_header = jets_dev.pdl_get_last_header()
        # except:
        #     last_header = JetsDeviceConstants.SNAP_HDR

        if self.is_field_set(self.get_snap_organization_code()):
            pkt_fields["msid"] = str(self.get_snap_organization_code())
        if self.is_field_set(self.get_snap_ether_type()):
            pkt_fields["type"] = str(self.get_snap_ether_type())
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.SNAP_HDR, pkt_fields)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        organization_code = self.get_bits_from_string(24, payload)
        self.set_snap_organization_code("0x" + organization_code)
        payload = self.remove_bits_from_string(24, payload)
        ether_type = self.get_bits_from_string(16, payload)
        self.set_snap_ether_type("0x" + ether_type)
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_snap_organization_code(), PacketConstants.INTEGER, 24)
        ret_string += self.format_byte_string(self.get_snap_ether_type(), PacketConstants.INTEGER, 16)
        return ret_string

    @staticmethod
    def compare_snap_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                   print_failures=True):
        results = True
        try:
            assert isinstance(expected, SnapPacketHeader)
            assert isinstance(actual, SnapPacketHeader)
            if expected.do_i_check_this_field(expected.get_snap_organization_code(),
                                              SnapPacketConstants.SNAP_ORGANIZATION_CODE, ignore_list, include_list):
                name = "SNAP organization code : "
                if expected.get_snap_organization_code() != actual.get_snap_organization_code():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_snap_organization_code()) + " != " +
                                                      str(actual.get_snap_organization_code()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snap_organization_code()) + " == " +
                                                 str(actual.get_snap_organization_code()) + " Pass")

            if expected.do_i_check_this_field(expected.get_snap_ether_type(), SnapPacketConstants.SNAP_ETHER_TYPE,
                                              ignore_list, include_list):
                name = "SNAP ether type : "
                if expected.get_snap_ether_type() != actual.get_snap_ether_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_snap_ether_type()) + " != " +
                                                      str(actual.get_snap_ether_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_snap_ether_type()) + " == " +
                                                 str(actual.get_snap_ether_type()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with SnapPacketHeader")
        return results


class SnapPacketConstants:
    def __init__(self):
        pass

    SNAP_ORGANIZATION_CODE = "SNAP_ORGANIZATION_CODE"
    SNAP_ETHER_TYPE = "SNAP_ETHER_TYPE"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
