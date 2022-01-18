from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.vlan_pb2 import vlan
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject


class TaggedPacketHeader(object):
    def __init__(self):
        self.add_tagged_header()
        self.HEADER_SIZE_TAGGED = 4  # BYTES

    def set_vlan_protocol_id(self, pkt_type, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TaggedPacketHeaderConstants.TAGGED_VLAN_PROTOCOL_ID,
                                                        ignore_check)
        pkt_type = self.normalize_value(pkt_type, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                  TaggedPacketHeaderConstants.TAGGED_VLAN_PROTOCOL_ID, pkt_type)

    def get_vlan_protocol_id(self, ):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                                              TaggedPacketHeaderConstants.TAGGED_VLAN_PROTOCOL_ID),
                                    PacketConstants.INTEGER)

    def set_vlan_id(self, tag, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TaggedPacketHeaderConstants.TAGGED_VLAN_ID, ignore_check)
        tag = self.normalize_value(tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                  TaggedPacketHeaderConstants.TAGGED_VLAN_ID, tag)

    def get_vlan_id(self, ):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                                              TaggedPacketHeaderConstants.TAGGED_VLAN_ID),
                                    PacketConstants.INTEGER)

    def set_vlan_tci(self, tci, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TaggedPacketHeaderConstants.TAGGED_VLAN_TCI, ignore_check)
        tci = self.normalize_value(tci, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                  TaggedPacketHeaderConstants.TAGGED_VLAN_TCI, tci)

    def get_vlan_tci(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED,
                                                              TaggedPacketHeaderConstants.TAGGED_VLAN_TCI),
                                    PacketConstants.INTEGER)

    def add_tagged_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_QTAGGED)

    def build(self):
        self.add_tagged_header()
        self.set_vlan_protocol_id("0x8100", True)
        # self.set_vlan_id("0")
        # self.set_vlan_tci("0")

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("Vlan Protocol ID", self.format_int(self.get_vlan_protocol_id(), 2))
        table.add_row_value("Vlan ID", self.format_int(self.get_vlan_id(), 2))
        table.add_row_value("TCI", self.format_int(self.get_vlan_tci(), 2))
        return table.to_table_string()

    def get_hltapi_commands(self):
        dummy_dict = dict()
        ttl = self.get_vlan_protocol_id()
        if isinstance(ttl, int):
            ttl = str(ttl)
        # if isinstance(self, Ethernet2PacketHeader):
        #     dummy_dict[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_ETHERNET_II_VLAN
        if ttl and 'Not Set' not in ttl and "8100" not in str(ttl):
            dummy_dict[TrafficConfigConstants.VLAN_PROTOCOL_TAG_ID_CMD] = hex(int(ttl))[2:]
        ttl = self.get_vlan_id()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.VLAN_ID_CMD] = ttl
        ttl = self.get_vlan_tci()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.VLAN_USER_PRIORITY_CMD] = ttl
        return dummy_dict

    def get_spirent_tagged_api_commands(self, port_name_stream):
        dummy_dict = []
        ttl = self.get_vlan_protocol_id()
        if isinstance(ttl, int):
            ttl = str(ttl)
        if isinstance(self, Ethernet2PacketHeader) or \
                isinstance(self, SnapPacketHeader) or \
                isinstance(self, SapPacketHeader):
            if isinstance(self, Ethernet2PacketHeader):
                dummy_dict.append("set ether_name [stc::get $" + port_name_stream + " -children-ethernet:ethernetii]")
            elif isinstance(self, SnapPacketHeader):
                dummy_dict.append("set ether_name [stc::get $" + port_name_stream + " -children-ethernet:EthernetSnap]")
            elif isinstance(self, SapPacketHeader):
                dummy_dict.append("set ether_name [stc::get $" + port_name_stream + " -children-ethernet:Ethernet8022]")
            dummy_dict.append("set vlan_name [stc::create vlans -under $ether_name]")
            vlan_string = ""
            ttl = self.get_vlan_protocol_id()
            if isinstance(ttl, int):
                ttl = str(ttl)
            # if isinstance(self, Ethernet2PacketHeader):
            #     dummy_dict[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_ETHERNET_II_VLAN
            if ttl and 'Not Set' not in ttl:
                vlan_string += " -type " + hex(int(ttl))[2:]
            ttl = self.get_vlan_id()
            if isinstance(ttl, int):
                ttl = str(ttl)
            if ttl and 'Not Set' not in ttl:
                vlan_string += " -id " + ttl
            ttl = self.get_vlan_tci()
            if isinstance(ttl, int):
                ttl = str(ttl)
            if ttl and 'Not Set' not in ttl:
                vlan_string += " -pri " + bin(int(ttl))[2:].zfill(3)
            if len(vlan_string) > 0:
                dummy_dict.append("stc::create vlan -under $vlan_name " + vlan_string)
            # if ttl and 'Not Set' not in ttl and not "8100" in str(ttl):
            #     dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII.vlans.Vlan -type " + ttl)
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_tagged(self, tgen_type, generator_ref, port_string, stream_id,
                                                          **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_tagged(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_tagged(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_tagged(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kVlanFieldNumber
        # reduce typing by creating a shorter reference to p.Extensions[ip4]
        # src_ip = {int} 0
        tag = p.Extensions[vlan]
        # vlan_tag = {int} 0
        vlanInfo = 0
        changedVlan = False
        if self.is_field_set(self.get_vlan_protocol_id()):
            tag.is_override_tpid = True
            tag.tpid = int(self.get_vlan_protocol_id())
        if self.is_field_set(self.get_vlan_id()):
            vlanInfo = int(self.get_vlan_id())
            changedVlan = True
        if self.is_field_set(self.get_vlan_tci()):
            vlanInfo |= int(self.get_vlan_tci()) << 13
            changedVlan = True
        if changedVlan:
            tag.vlan_tag = vlanInfo
        # is_override_tpid = {bool} False
        # tpid = {int} 0
        # tpid != tci!!
        # if self.is_field_set(self.get_vlan_tci()):
        #     tag.tpid = long(self.get_vlan_tci())
        #     tag.is_override_tpid = True
        # else:
        #     tag.is_override_tpid = False

    def config_jets_stream_tagged(self, jets_dev, port_string, stream_id, **kwargs):
        """
         IEEE_8021Q_HDR {
            vlan_priority   : 3  : default=0, display="Vlan priority", index=1;
                vlan_cfi_bit    : 1  : default=0, display="Vlan CFI Bit", index=2;
            vlanid		: 12 : default=0,
                        display="Global VLAN ID", index=3;
            type		: 16 : send=length(pdu,pdu),
                        display="Ethertype", index=2;
        } display="802.1Q Header", index=11002;
        """
        pkt_fields = {}
        if self.is_field_set(self.get_vlan_tci()):
            pkt_fields["vlan_priority"] = str(self.get_vlan_tci())
        # if self.is_field_set(self.get_vlan_tci()):
        #     pkt_fields["vlan_cfi_bit"]= str(int(self.get_vlan_tci()) << 13)
        if self.is_field_set(self.get_vlan_protocol_id()):
            update_field = str(self.get_vlan_protocol_id())
        if self.is_field_set(self.get_vlan_id()):
            pkt_fields["vlanid"] = str(self.get_vlan_id())

        if "Ethernet2" in self.get_name():
            if self.is_field_set(self.get_ether_type()):
                pkt_fields["type"] = str(self.get_ether_type())
        elif "Snap" in self.get_name():
            if self.is_field_set(self.get_snap_ether_type()):
                pkt_fields["type"] = str(self.get_snap_ether_type())

        last_header = jets_dev.pdl_get_last_header()
        jets_dev.pdl_add_packet_header("IEEE_8021Q_HDR", pkt_fields)
        if update_field:
            jets_dev.pdl_update_packet_header_value(last_header, "type", update_field)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        # tag ether type 16bits
        tagethertype = self.get_bits_from_string(16, payload)
        self.set_vlan_protocol_id("0x" + tagethertype)
        payload = self.remove_bits_from_string(16, payload)
        _vlanTci = self.get_bits_from_string(16, payload)
        # vlan id = 8bits
        self.set_vlan_tci((int(_vlanTci, 16) & 0x0F000) >> 13)
        self.set_vlan_id((int(_vlanTci, 16) & 0x0FFF))
        payload = self.remove_bits_from_string(16, payload)
        self.payload = payload

    def get_header_bytes(self):
        da = "8100"  # self.format_byte_string ("8100", PacketConstants.INTEGER, 4)
        idval = self.to_int(self.get_vlan_id())
        tcival = self.to_int(self.get_vlan_tci())
        tag = self.format_byte_string((tcival << 13) | idval, PacketConstants.INTEGER, 16)
        return da + " " + tag

    @staticmethod
    def compare_tagged_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                     print_failures=True):
        results = True
        try:
            # if isinstance(actual, TaggedPacketHeader):
            assert isinstance(expected, TaggedPacketHeader)
            assert isinstance(actual, TaggedPacketHeader)
            if expected.do_i_check_this_field(expected.get_vlan_protocol_id(),
                                              TaggedPacketHeaderConstants.TAGGED_VLAN_PROTOCOL_ID, ignore_list,
                                              include_list):
                name = "Vlan TPID: "
                if expected.get_vlan_protocol_id() != actual.get_vlan_protocol_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_vlan_protocol_id()) + " != " +
                                                      str(actual.get_vlan_protocol_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_protocol_id()) + " == " +
                                                 str(actual.get_vlan_protocol_id()) + " Pass")

            if expected.do_i_check_this_field(expected.get_vlan_id(), TaggedPacketHeaderConstants.TAGGED_VLAN_ID,
                                              ignore_list, include_list):
                name = "Vlan ID: "
                if expected.get_vlan_id() != actual.get_vlan_id():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_vlan_id()) + " != " +
                                                      str(actual.get_vlan_id()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_id()) + " == " +
                                                 str(actual.get_vlan_id()) + " Pass")
            if expected.do_i_check_this_field(expected.get_vlan_tci(), TaggedPacketHeaderConstants.TAGGED_VLAN_TCI,
                                              ignore_list, include_list):
                name = "Vlan TCI: "
                if expected.get_vlan_tci() != actual.get_vlan_tci():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_vlan_tci()) + " != " +
                                                      str(actual.get_vlan_tci()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_tci()) + " == " +
                                                 str(actual.get_vlan_tci()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with Ethernet2PacketHeader")
        return results


class TaggedPacketHeaderConstants:
    def __init__(self):
        pass
    TAGGED_VLAN_ID = "TAGGED_VLAN_ID"
    TAGGED_VLAN_PROTOCOL_ID = "TAGGED_VLAN_TPID"
    TAGGED_VLAN_TCI = "TAGGED_VLAN_TCI"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
