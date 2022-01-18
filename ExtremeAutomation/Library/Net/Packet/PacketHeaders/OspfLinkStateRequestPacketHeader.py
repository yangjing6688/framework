from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import OspfPacketHeader


class OspfLinkStateRequestPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    OSPF LS Request Packet Header
        # lsa = 32bits
        # link state id = 32bits
        # advertising router = 32bits
                0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                          LS type                              |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Link State ID                           |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                     Advertising Router                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                              ...                              |
    """

    def __init__(self):
        self.add_linkstaterequest_header()
        self.HEADER_SIZE_LINKSTATEREQUEST = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start LinkStateRequest lsa methods
    #  lsa is a 32 bit INTEGER example: 1
    def set_linkstaterequest_lsa(self, lsa, ignore_check=False):
        lsa = self.normalize_value(lsa, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
                                  LinkStateRequestPacketConstants.LINKSTATEREQUEST_LSA, lsa)

    def get_linkstaterequest_lsa(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
            LinkStateRequestPacketConstants.LINKSTATEREQUEST_LSA), PacketConstants.INTEGER)

    def get_linkstaterequest_lsa_string(self):
        try:
            return LinkStateRequestPacketConstants.LINKSTATEREQUEST_LINK_STATE_TYPES[self.get_linkstaterequest_lsa()]
        except Exception as e:
            PacketObject.logger.log_info(repr(e))
            return "Unknown"

    def get_linkstaterequest_lsa_hltapi_cmd(self, dummy_dict):
        lsa = self.get_linkstaterequest_lsa()
        if isinstance(lsa, int):
            lsa = str(lsa)
        if lsa and 'Not Set' not in lsa:
            dummy_dict[TrafficConfigConstants.TEMP_LSA_CMD] = lsa
    # end LinkStateRequest lsa methods

    # start LinkStateRequest link state id methods
    #  link_state_id is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_linkstaterequest_link_state_id(self, link_state_id, ignore_check=False):
        link_state_id = self.normalize_value(link_state_id, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
                                  LinkStateRequestPacketConstants.LINKSTATEREQUEST_LINK_STATE_ID, link_state_id)

    def get_linkstaterequest_link_state_id(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
            LinkStateRequestPacketConstants.LINKSTATEREQUEST_LINK_STATE_ID), PacketConstants.IPV4_ADDRESS)

    def get_linkstaterequest_link_state_id_hltapi_cmd(self, dummy_dict):
        link_state_id = self.get_linkstaterequest_link_state_id()
        if link_state_id and 'Not Set' not in link_state_id:
            dummy_dict[TrafficConfigConstants.TEMP_LINK_STATE_ID_CMD] = link_state_id
    # end LinkStateRequest link state id methods

    # start LinkStateRequest advertising router methods
    #  advertising_router is a 32 bit IPV4_ADDRESS example: 1.2.3.4
    def set_linkstaterequest_advertising_router(self, advertising_router, ignore_check=False):
        advertising_router = self.normalize_value(advertising_router, PacketConstants.IPV4_ADDRESS)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
                                  LinkStateRequestPacketConstants.LINKSTATEREQUEST_ADVERTISING_ROUTER,
                                  advertising_router)

    def get_linkstaterequest_advertising_router(self):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L4_OSPF_LINKSTATEREQUEST,
            LinkStateRequestPacketConstants.LINKSTATEREQUEST_ADVERTISING_ROUTER), PacketConstants.IPV4_ADDRESS)

    def get_linkstaterequest_advertising_router_hltapi_cmd(self, dummy_dict):
        advertising_router = self.get_linkstaterequest_advertising_router()
        if advertising_router and 'Not Set' not in advertising_router:
            dummy_dict[TrafficConfigConstants.TEMP_ADVERTISING_ROUTER_CMD] = advertising_router
    # end LinkStateRequest advertising router methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("lsa", self.get_linkstaterequest_lsa_string() + " " +
                            str(self.format_int(self.get_linkstaterequest_lsa(), 8)))
        table.add_row_value("link state id", self.get_linkstaterequest_link_state_id())
        table.add_row_value("advertising router", self.get_linkstaterequest_advertising_router())

        rt_string = ""
        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            rt_string += "\n\nAuth Crypt Data:" + self.get_ospf_auth_crypt_data() + "\n\n"
        return "\n\nLINKSTATEREQUEST HEADER" + table.to_table_string() + rt_string

    def add_linkstaterequest_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_OSPF_LINKSTATEREQUEST)

    def build(self):
        self.add_linkstaterequest_header()
        self.set_ospf_message_type(0x03, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_linkstaterequest_lsa_hltapi_cmd(dummy_dict)
        # self.get_linkstaterequest_link_state_id_hltapi_cmd(dummy_dict)
        # self.get_linkstaterequest_advertising_router_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_linkstaterequest(self, tgen_type, generator_ref, port_string,
                                                                    stream_id, **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_linkstaterequest(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_linkstaterequest(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_linkstaterequest(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.klinkstaterequestFieldNumber
        # update this from the ostinato docs.
        #     linkstaterequestField = p.Extensions[linkstaterequest]
        #     if self.is_field_set(self.get_linkstaterequest_lsa()) :
        #         linkstaterequestField.version = int(self.get_linkstaterequest_lsa())
        #     if self.is_field_set(self.get_linkstaterequest_link_state_id()) :
        #         linkstaterequestField.version = int(self.get_linkstaterequest_link_state_id())
        #     if self.is_field_set(self.get_linkstaterequest_advertising_router()) :
        #         linkstaterequestField.version = int(self.get_linkstaterequest_advertising_router())

    def config_jets_stream_linkstaterequest(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_fields = {}
        header_name = "LINKSTATEREQUEST_HDR"
        pkt_bytes = "0x" + OspfLinkStateRequestPacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        # if self.is_field_set(self.get_linkstaterequest_lsa()) :
        #     pkt_fields["lsa"] = int(self.get_linkstaterequest_lsa())
        # if self.is_field_set(self.get_linkstaterequest_link_state_id()) :
        #     pkt_fields["link_state_id"] = int(self.get_linkstaterequest_link_state_id())
        # if self.is_field_set(self.get_linkstaterequest_advertising_router()) :
        #     pkt_fields["advertising_router"] = int(self.get_linkstaterequest_advertising_router())

    def get_ixtclhal_linkstaterequest_api_commands(self, port_string, streamid):
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
        lsa = self.get_bits_from_string(32, payload)
        self.set_linkstaterequest_lsa("0x" + lsa)
        payload = self.remove_bits_from_string(32, payload)
        link_state_id = self.get_bits_from_string(32, payload)
        self.set_linkstaterequest_link_state_id("0x" + link_state_id)
        payload = self.remove_bits_from_string(32, payload)
        advertising_router = self.get_bits_from_string(32, payload)
        self.set_linkstaterequest_advertising_router("0x" + advertising_router)
        payload = self.remove_bits_from_string(32, payload)

        self.payload = payload
        payload = OspfPacketHeader.process_auth_entry(payload, self)
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_linkstaterequest_lsa(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_linkstaterequest_link_state_id(),
                                              PacketConstants.IPV4_ADDRESS, 32)
        ret_string += self.format_byte_string(self.get_linkstaterequest_advertising_router(),
                                              PacketConstants.IPV4_ADDRESS, 32)

        auth_type = self.get_ospf_auth_type()
        if auth_type == 2:
            ret_string += self.get_bytes_auth_entry(self).replace("0x", "")

        return ret_string

    @staticmethod
    def compare_linkstaterequest_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, OspfLinkStateRequestPacketHeader)
            assert isinstance(actual, OspfLinkStateRequestPacketHeader)
            if expected.is_field_set(expected.get_linkstaterequest_lsa()) and \
                    LinkStateRequestPacketConstants.LINKSTATEREQUEST_LSA not in ignore_list:
                name = "LINKSTATEREQUEST lsa : "
                if expected.get_linkstaterequest_lsa() != actual.get_linkstaterequest_lsa():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_linkstaterequest_lsa()) + " != " +
                                                      str(actual.get_linkstaterequest_lsa()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_linkstaterequest_lsa()) + " == " +
                                                 str(actual.get_linkstaterequest_lsa()) + " Pass")

            if expected.is_field_set(expected.get_linkstaterequest_link_state_id()) and \
                    LinkStateRequestPacketConstants.LINKSTATEREQUEST_LINK_STATE_ID not in ignore_list:
                name = "LINKSTATEREQUEST link state id : "
                if expected.get_linkstaterequest_link_state_id() != actual.get_linkstaterequest_link_state_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_linkstaterequest_link_state_id()) + " != " +
                                                      str(actual.get_linkstaterequest_link_state_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_linkstaterequest_link_state_id()) + " == " +
                                                 str(actual.get_linkstaterequest_link_state_id()) + " Pass")

            if expected.is_field_set(expected.get_linkstaterequest_advertising_router()) and \
                    LinkStateRequestPacketConstants.LINKSTATEREQUEST_ADVERTISING_ROUTER not in ignore_list:
                name = "LINKSTATEREQUEST advertising router : "
                if expected.get_linkstaterequest_advertising_router() != \
                        actual.get_linkstaterequest_advertising_router():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(str(expected.get_linkstaterequest_advertising_router()) + " != " +
                                                      str(actual.get_linkstaterequest_advertising_router()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_linkstaterequest_advertising_router()) +
                                                 " == " + str(actual.get_linkstaterequest_advertising_router()) +
                                                 " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with LinkStateRequestPacketHeader")
        return results


class LinkStateRequestPacketConstants:
    def __init__(self):
        pass

    LINKSTATEREQUEST_LSA = "LINKSTATEREQUEST_LSA"

    LINKSTATEREQUEST_LINK_STATE_ID = "LINKSTATEREQUEST_LINK_STATE_ID"

    LINKSTATEREQUEST_ADVERTISING_ROUTER = "LINKSTATEREQUEST_ADVERTISING_ROUTER"

    LINKSTATEREQUEST_LINK_STATE_TYPE = "DBDESCRIPTION_LINK_STATE_TYPE"
    LINKSTATEREQUEST_LINK_STATE_TYPE_ROUTER_LINKS = "1"
    LINKSTATEREQUEST_LINK_STATE_TYPE_NETWORK_LINKS = "2"
    LINKSTATEREQUEST_LINK_STATE_TYPE_SUMMARY_LINK_IP_NETWORK = "3"
    LINKSTATEREQUEST_LINK_STATE_TYPE_SUMMARY_LINK_ASBR = "4"
    LINKSTATEREQUEST_LINK_STATE_TYPE_AS_EXTERNAL_LINK = "5"
    LINKSTATEREQUEST_LINK_STATE_TYPES = {1: "Router-LSA",
                                         2: "Network links",
                                         3: "Summary link(IP network)",
                                         4: "Summary link(ASBR)",
                                         5: "AS external link"}

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
