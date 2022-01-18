from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.eth2_pb2 import eth2
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject


class Ethernet2PacketHeader(object):
    def __init__(self):
        self.add_enet2_header()
        self.HEADER_SIZE_ETHERNET2 = 2  # bytes

    def set_ether_type(self, tgen_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(Ethernet2PacketConstants.ETHERII_TYPE, ignore_check)
        tgen_type = self.normalize_value(tgen_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_II_TYPE,
                                  Ethernet2PacketConstants.ETHERII_TYPE, tgen_type)

    def get_ether_type(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_II_TYPE,
                                                              Ethernet2PacketConstants.ETHERII_TYPE),
                                    PacketConstants.INTEGER)

    def get_ether_type_hltpapi_cmd(self, dummy_dict):
        ttl = self.get_ether_type()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.ETHERNET_VALUE_CMD] = str(hex(int(ttl)))[2:]

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Ether Type II", self.format_hex(self.get_ether_type(), 2))
        return table.to_table_string()

    def add_enet2_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_ENET2)

    def build(self):
        self.add_enet2_header()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        dummy_dict[TrafficConfigConstants.ETHERNET_TYPE_CMD] = TrafficConfigConstants.ETHERNET_TYPE_ETHERNETII
        self.get_ether_type_hltpapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_enet2(self, tgen_type, generator_ref, port_string, stream_id,
                                                         **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_enet2(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_enet2(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_SCAPY:
            self.config_scapy_stream_ether2(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_enet2(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kEth2FieldNumber
        if self.is_field_set(self.get_ether_type()):
            p.Extensions[eth2].is_override_type = True
            p.Extensions[eth2].type = int(self.get_ether_type())
        else:
            p.Extensions[eth2].is_override_type = True

    def config_jets_stream_enet2(self, generator_ref, port_string, stream_id, **kwargs):
        pkt_fields = {}
        try:
            last_header = generator_ref.pdl_get_last_header()
        except:
            last_header = "ENET_HDR"

        if self.is_field_set(self.get_ether_type()):
            pkt_fields["type"] = str(self.get_ether_type())
        generator_ref.pdl_add_packet_header(last_header, pkt_fields)

    def config_scapy_stream_ether2(self, jets_dev, port_string, stream_id, **kwargs):
        pkt_field = {}
        if self.is_field_set(self.get_ether_type()):
            pkt_field["type"] = hex(int(self.get_ether_type()))
        jets_dev.pdl_add_packet_header("Ether", pkt_field)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        # ether type = 16bits
        tgen_type = self.get_bits_from_string(16, payload)
        self.set_ether_type("0x" + tgen_type)
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        da = self.format_byte_string(self.get_ether_type(), PacketConstants.INTEGER, 16)
        return da

    def get_spirent_etherii_api_commands(self, port_name_stream):
        dummy_dict = []
        if self.is_field_set(self.get_ether_type()):
            dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
                              hex(int(str(self.get_ether_type())))[2:])
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    @staticmethod
    def compare_ethernet2_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                        print_failures=True):
        results = True
        try:
            if expected.do_i_check_this_field(expected.get_ether_type(), Ethernet2PacketConstants.ETHERII_TYPE,
                                              ignore_list, include_list):
                # if isinstance(actual, Ethernet2PacketHeader):
                assert isinstance(expected, Ethernet2PacketHeader)
                assert isinstance(actual, Ethernet2PacketHeader)
                if expected.get_ether_type() != actual.get_ether_type():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error("Ether Type: " + str(expected.get_ether_type()) + " != " +
                                                      str(actual.get_ether_type()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info("Ether Type: " + str(expected.get_ether_type()) + " == " +
                                                 str(actual.get_ether_type()) + " Pass")
        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with Ethernet2PacketHeader")
        return results


class Ethernet2PacketConstants:
    def __init__(self):
        pass
    ETHERII_TYPE = "ETHERII_TYPE"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
