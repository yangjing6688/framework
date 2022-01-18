from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class SpanningTreePacketHeader(object):
    packet_name = None
    pkt_bytes = None

    def __init__(self):
        self.add_spanningtree_header()

    def to_packet_string(self):
        table = TableFormatter()
        return "\n\nSPANNINGTREE HEADER" + table.to_table_string()

    def add_spanningtree_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_SPANNINGTREE)

    def build(self):
        self.add_spanningtree_header()
        self.set_bpdu_version(0x01, True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        return dummy_dict

    def get_spirent_spanningtree_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_spanningtree(self, tgen_type, generator_ref, port_string, stream_id,
                                                                **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_spanningtree(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jet_stream_spanningtree(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_spanningtree(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kspanningtreeFieldNumber
        # update this from the ostinato docs.
        spanningtreeField = p.Extensions[-1]

    def config_jet_stream_spanningtree(self, jets_dev, port_string, stream_id, **kwargs):
        # this is not supported yet
        # do it with rawdata instead
        pkt_bytes = "0x" + SpanningTreePacketHeader.get_header_bytes(self)
        jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_spanningtree_api_commands(self, port_string, streamid):
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
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        return ret_string

    @staticmethod
    def compare_spanningtree_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, SpanningTreePacketHeader)
            assert isinstance(actual, SpanningTreePacketHeader)
        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with SpanningTreePacketHeader")
        return results


class SpanningTreePacketConstants:
    def __init__(self):
        pass

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
