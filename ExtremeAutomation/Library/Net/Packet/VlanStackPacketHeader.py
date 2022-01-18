from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import SnapPacketHeader
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.vlan_pb2 import vlan
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject, PacketHeaderDynamicFieldLogic
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class VlanStackPacketHeader(object):
    def __init__(self):
        self.num_tags = 0
        self.add_vlanstack_header()
        self.HEADER_SIZE_VLAN_STACK = 4  # BYTES

    def get_vlan_num(self):
        return self.num_tags

    def set_vlan_num(self, num_tags):
        self.num_tags = NumberUtils.to_integer_value(num_tags)

    def set_vlan_protocol_id(self, stack_number, tag, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_PROTOCOL_ID +
                                                        " " + str(stack_number), ignore_check)
        tag = self.normalize_value(tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                  VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_PROTOCOL_ID + " " + str(stack_number),
                                  tag)

    def get_vlan_protocol_id(self, stack_number):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                      VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_PROTOCOL_ID + " " +
                                      str(stack_number)), PacketConstants.INTEGER)

    def set_vlan_id(self, stack_number, tag, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_ID + " " +
                                                        str(stack_number), ignore_check)
        tag = self.normalize_value(tag, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                  VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_ID + " " + str(stack_number), tag)

    def get_vlan_id(self, stack_number):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                                              VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_ID + " " +
                                                              str(stack_number)),
                                    PacketConstants.INTEGER)

    def set_vlan_tci(self, stack_number, tci, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_TCI + " " +
                                                        str(stack_number), ignore_check)
        tci = self.normalize_value(tci, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                  VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_TCI + " " + str(stack_number), tci)

    def get_vlan_tci(self, stack_number):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L2_ETHERNET_VLAN_STACK,
                                                              VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_TCI + " " +
                                                              str(stack_number)),
                                    PacketConstants.INTEGER)

    def add_vlanstack_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_VLAN_STACK)

    def build(self):
        self.add_vlanstack_header()
        # self.set_vlan_id("0")
        # self.set_vlan_tci("0")

    def to_packet_string(self):
        return self.to_packet_string_tags()

    def to_packet_string_tags(self):
        index = 1
        ret_string = "\nVlan Stack number : " + str(self.get_vlan_num())
        table = TableFormatter()
        for index in range(1, NumberUtils.to_integer_value(self.get_vlan_num()) + 1):
            table.add_row_value("Tag", str(index))
            table.add_row_value("Protocol ID", self.format_int(self.get_vlan_protocol_id(index), 4))
            table.add_row_value("Vlan ID", self.format_int(self.get_vlan_id(index), 2))
            table.add_row_value("TCI", self.format_int(self.get_vlan_tci(index), 2))
            index += 1
        ret_string += table.to_table_string() + "\n"
        return ret_string

    def get_hltapi_commands(self):
        dummy_dict = dict()
        index = 1
        ret_string = ""
        # dummy_dict[TrafficConfigConstants.VLAN_ID_CMD] = ""
        # dummy_dict[TrafficConfigConstants.VLAN_USER_PRIORITY_CMD] = ""
        # for index in range(1, int(self.get_vlan_num()) + 1):
        #     if self.get_vlan_id(index):
        #         dummy_dict[TrafficConfigConstants.VLAN_ID_CMD] += " " + str(self.get_vlan_id(index))
        #     if self.get_vlan_tci(index):
        #         dummy_dict[TrafficConfigConstants.VLAN_USER_PRIORITY_CMD] += " " + str(self.get_vlan_tci(index))
        #     # if self.get_vlan_tci(index):
        #     #     dummy_dict[TrafficConfigConstants.VLAN_] += str(self.get_vlan_protocol_id(index))
        #     index += 1
        # dummy_dict[TrafficConfigConstants.VLAN_ID_CMD] = "{" + dummy_dict[
        #     TrafficConfigConstants.VLAN_ID_CMD].strip() + "}"
        # dummy_dict[TrafficConfigConstants.VLAN_USER_PRIORITY_CMD] = "{" + dummy_dict[
        #     TrafficConfigConstants.VLAN_USER_PRIORITY_CMD].strip() + "}"
        # dummy_dict[TrafficConfigConstants.VLAN_] = "{" + dummy_dict[
        #     TrafficConfigConstants.VLAN_] + "}"
        return dummy_dict

    def get_ixtclhal_vlanstack_api_commands(self, port, streamid):
        dummy_dict = []
        num = NumberUtils.to_integer_value(self.get_vlan_num())
        index = 1
        if num > 0:
            dummy_dict.append("stream get " + port + " " + str(streamid))
            dummy_dict.append("stackedVlan setDefault")
            #
            # dummy_dict.append("protocol setDefault")
            # protocol config -name                               mac
            # protocol config -appName                            noType
            # protocol config -ethernetType                       noType
            dummy_dict.append("protocol config -enable802dot1qTag                  vlanStacked")
            dummy_dict.append("protocolServer set " + port)
            # protocol config -enableISLtag                       false
            # protocol config -enableMPLS                         false
            # protocol config -enableMacSec                       false
            # protocol config -enableOAM                          false
            # protocol config -enableDataCenterEncapsulation      false
            # protocol config -enableProtocolPad                  false
            dummy_dict.append("set vlanPosition 0")
            for index in range(1, num + 1):
                dummy_dict.append("incr vlanPosition")
                dummy_dict.append("vlan setDefault")
                dummy_dict.append("vlan config -vlanID                             " + str(self.get_vlan_id(index)))
                dummy_dict.append("vlan config -userPriority                       " + str(self.get_vlan_tci(index)))
                dummy_dict.append("vlan config -cfi                                resetCFI")
                dummy_dict.append(
                    "vlan config -protocolTagId                      " + str(self.get_vlan_protocol_id(index)))
                if index > 2:
                    dummy_dict.append("stackedVlan addVlan")
                dummy_dict.append("stackedVlan setVlan $vlanPosition")
            dummy_dict.append("stackedVlan set " + port)
            dummy_dict.append("stream set " + port + " " + str(streamid))
            dummy_dict.append("stream write " + port + " " + str(streamid))
            dummy_dict.append("set portList [ list [ list " + port + "]]")
            dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_vlan_stack_api_commands(self, port_name_stream):
        dummy_dict = []
        num = NumberUtils.to_integer_value(self.get_vlan_num())
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

            for index in range(1, num + 1):
                vlan_string = ""
                ttl = self.get_vlan_protocol_id(index)
                if isinstance(ttl, int):
                    ttl = str(ttl)
                # if isinstance(self, Ethernet2PacketHeader):
                #     dummy_dict[TrafficConfigConstants.L2_ENCAP_CMD] = TrafficConfigConstants.L2_ENCAP_ETHERNET_II_VLAN
                if ttl and 'Not Set' not in ttl:
                    vlan_string += " -type " + hex(int(ttl))[2:]
                ttl = self.get_vlan_id(index)
                if isinstance(ttl, int):
                    ttl = str(ttl)
                if ttl and 'Not Set' not in ttl:
                    vlan_string += " -id " + ttl
                ttl = self.get_vlan_tci(index)
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

    def config_thirdparty_traffic_generator_stream_vlan_stack(self, tgen_type, generator_ref, port_string, stream_id,
                                                              **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_vlan_stack(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_vlan_stack(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_vlan_stack(self, drone, port_string, stream_id, **kwargs):
        index = 0
        while index < NumberUtils.to_integer_value(self.get_vlan_num()):
            index += 1
            p = stream_id.protocol.add()
            p.protocol_id.id = ost_pb.Protocol.kVlanFieldNumber
            # reduce typing by creating a shorter reference to p.Extensions[ip4]
            # src_ip = {int} 0
            tag = p.Extensions[vlan]
            # vlan_tag = {int} 0
            vlanInfo = 0
            changedVlan = False
            if self.is_field_set(self.get_vlan_protocol_id(index)):
                tag.is_override_tpid = True
                tag.tpid = int(self.get_vlan_protocol_id(index))
            if self.is_field_set(self.get_vlan_id(index)):
                vlanInfo = int(self.get_vlan_id(index))
                changedVlan = True
            if self.is_field_set(self.get_vlan_tci(index)):
                vlanInfo |= int(self.get_vlan_tci(index)) << 13
                changedVlan = True
            if changedVlan:
                tag.vlan_tag = vlanInfo
        # vlan_tag = {int} 0
        # if self.is_field_set(self.get_vlan_id()):
        #     stack.vlan_tag = long(self.get_vlan_id())
        # # is_override_tpid = {bool} False
        # # tpid = {int} 0
        # if self.is_field_set(self.get_vlan_tci()):
        #     stack.tpid = long(self.get_vlan_tci())
        #     stack.is_override_tpid = True
        # else:
        #     stack.is_override_tpid = False

    def config_jets_stream_vlan_stack(self, jets_dev, port_string, stream_id, **kwargs):
        """
        QNQ_HDR {
            priority   : 3  : default=0, display="Outer Vlan priority", index=1;
            cfi_bit    : 1  : default=0, display="Outer Vlan CFI Bit", index=2;
            vlanid	   : 12 : default=0, display="Outer VLAN ID", index=3;
            type	   : 16 : send=length(pdu,pdu), display="Outer Ethertype", index=4;
        """
        index = 0
        while index < NumberUtils.to_integer_value(self.get_vlan_num()):
            pkt_fields = {}
            if index == 0:
                header_name = JetsDeviceConstants.QNQ_HDR + "_" + str(index)
                vlan_priority = "priority"
            else:
                header_name = JetsDeviceConstants.IEEE_8021Q_HDR + "_" + str(index + 1)
                vlan_priority = "vlan_priority"
            index += 1
            if index > 2:
                jets_dev.logError("JETS only supports 2 tags")
                return
            if self.is_field_set(self.get_vlan_protocol_id(index)):
                update_field = str(self.get_vlan_protocol_id(index))
            if self.is_field_set(self.get_vlan_tci(index)):
                pkt_fields[vlan_priority] = str(self.get_vlan_tci(index))
            # if self.is_field_set(self.get_vlan_protocol_id(index)):
            #     pkt_fields["cfi_bit"]= str(self.get_vlan_protocol_id(index))
            if self.is_field_set(self.get_vlan_id(index)):
                pkt_fields["vlanid"] = str(self.get_vlan_id(index))

            last_header = jets_dev.pdl_get_last_header()
            jets_dev.pdl_add_packet_header(header_name, pkt_fields)
            if update_field:
                jets_dev.pdl_update_packet_header_value(last_header, "type", update_field)

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "").upper()
        # tag ether type 16bits
        index = 1
        has_tags = True
        while has_tags:
            tagethertype = self.get_bits_from_string(16, payload)
            has_tags = tagethertype in ["8100", "88A8", "9100", "9200", "9300"]
            if not has_tags:
                break
            else:
                payload = self.remove_bits_from_string(16, payload)
                _vlanTci = self.get_bits_from_string(16, payload)
                self.set_vlan_protocol_id(index, int(tagethertype, 16))
                self.set_vlan_tci(index, (int(_vlanTci, 16) & 0x0F000) >> 13)
                self.set_vlan_id(index, (int(_vlanTci, 16) & 0x0FFF))
                payload = self.remove_bits_from_string(16, payload)
                index += 1
        self.set_vlan_num(index - 1)
        self.payload = payload

    def get_header_bytes(self):
        index = 1
        ret_string = ""
        for index in range(1, NumberUtils.to_integer_value(self.get_vlan_num()) + 1):
            proto = self.to_int(self.get_vlan_protocol_id(index))
            if proto == 0:
                proto = 33024  # 8100
            idval = self.to_int(self.get_vlan_id(index))
            tcival = self.to_int(self.get_vlan_tci(index))
            proto = self.format_byte_string(proto, PacketConstants.INTEGER, 16)
            tag = self.format_byte_string((tcival << 13) | idval, PacketConstants.INTEGER, 16)
            ret_string += proto + " " + tag
            index += 1
        return ret_string

    def swap_tags(self, tag1, tag2):
        vlan_id_1 = self.get_vlan_id(tag1)
        vlan_tci_1 = self.get_vlan_tci(tag1)
        vlan_tpid_1 = self.get_vlan_protocol_id(tag1)

        vlan_id_2 = self.get_vlan_id(tag2)
        vlan_tci_2 = self.get_vlan_tci(tag2)
        vlan_tpid_2 = self.get_vlan_protocol_id(tag2)

        self.set_vlan_id(tag1, vlan_id_2)
        self.set_vlan_tci(tag1, vlan_tci_2)
        self.set_vlan_protocol_id(tag1, vlan_tpid_2)

        self.set_vlan_id(tag2, vlan_id_1)
        self.set_vlan_tci(tag2, vlan_tci_1)
        self.set_vlan_protocol_id(tag2, vlan_tpid_1)

    @staticmethod
    def compare_vlanstack_packet_header(expected, actual, ignore_list=None, include_list=None, dynamic_entries=None,
                                        print_results=True, print_failures=True):
        results = True
        try:
            # if isinstance(actual, VlanStackPacketHeader):
            assert isinstance(expected, VlanStackPacketHeader)
            assert isinstance(actual, VlanStackPacketHeader)
            num_vlans = min(expected.get_vlan_num(), actual.get_vlan_num())
            index = 0
            if dynamic_entries:
                dynamic_results = dynamic_entries.compare_packet_fields(expected, actual)
                if not dynamic_results:
                    PacketObject.logger.log_error("Dynamic Ordering error ERROR")
                    PacketObject.logger.log_error(dynamic_entries)
                    PacketObject.logger.log_error("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_error("Received:" + actual.to_packet_string_tags())
                else:
                    PacketObject.logger.log_info("Dynamic Ordering Pass")
                    PacketObject.logger.log_info(dynamic_entries)
                    PacketObject.logger.log_info("Expected:" + expected.to_packet_string_tags())
                    PacketObject.logger.log_info("Received:" + actual.to_packet_string_tags())
                results &= dynamic_results
            else:
                if expected.do_i_check_this_field(expected.get_vlan_num(),
                                                  VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_NUM, ignore_list,
                                                  include_list):
                    name = "Vlan Stack Number: "
                    if str(expected.get_vlan_num()) != str(actual.get_vlan_num()):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(name + str(expected.get_vlan_num()) + " != " +
                                                          str(actual.get_vlan_num()) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_vlan_num()) + " == " +
                                                     str(actual.get_vlan_num()) + " Pass")
                while index < num_vlans:
                    index += 1
                    results &= expected.compare_tags(expected, actual, index, index, ignore_list, include_list,
                                                     print_results, print_failures)

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_error("Error with VlanStackPacketHeader")
        return results

    @staticmethod
    def compare_tags(expected, actual, expected_index, actual_index, ignore_list=None, include_list=None,
                     print_results=True, print_failures=True):
        results = True
        wasSomethingChecked = False
        if expected.do_i_check_this_field(expected.get_vlan_protocol_id(expected_index),
                                          VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_PROTOCOL_ID + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Vlan TPID " + str(expected_index) + ": "
            if expected.get_vlan_protocol_id(expected_index) != actual.get_vlan_protocol_id(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(expected.get_vlan_protocol_id(expected_index)) + " != " +
                                                  str(actual.get_vlan_protocol_id(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_protocol_id(expected_index)) + " == " +
                                                 str(actual.get_vlan_protocol_id(actual_index)) + " Pass")

        if expected.do_i_check_this_field(expected.get_vlan_id(expected_index),
                                          VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_ID + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Vlan ID " + str(expected_index) + ": "
            if expected.get_vlan_id(expected_index) != actual.get_vlan_id(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(expected.get_vlan_id(expected_index)) + " != " +
                                                  str(actual.get_vlan_id(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_id(expected_index)) + " == " +
                                                 str(actual.get_vlan_id(actual_index)) + " Pass")

        if expected.do_i_check_this_field(expected.get_vlan_tci(expected_index),
                                          VlanStackPacketHeaderConstants.VLAN_STACK_VLAN_TCI + " " +
                                          str(expected_index), ignore_list, include_list):
            name = "Vlan TCI " + str(expected_index) + ": "
            if expected.get_vlan_tci(expected_index) != actual.get_vlan_tci(actual_index):
                results = False
                if print_results or print_failures:
                    PacketObject.logger.log_error(name + str(expected.get_vlan_tci(expected_index)) + " != " +
                                                  str(actual.get_vlan_tci(actual_index)) + " ERROR")
            else:
                wasSomethingChecked = True
                if print_results:
                    PacketObject.logger.log_info(name + str(expected.get_vlan_tci(expected_index)) + " == " +
                                                 str(actual.get_vlan_tci(actual_index)) + " Pass")
        return results


class VlanStackPacketHeaderConstants:
    def __init__(self):
        pass

    VLAN_STACK_VLAN_NUM = "VLAN_STACK_VLAN_NUM"
    VLAN_STACK_VLAN_PROTOCOL_ID = "VLAN_STACK_VLAN_PROTOCOL_ID"
    VLAN_STACK_VLAN_ID = "VLAN_STACK_VLAN_ID"
    VLAN_STACK_VLAN_TCI = "VLAN_STACK_VLAN_TCI"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass


class VlanStackPacketHeaderDynamicFieldLogic(PacketHeaderDynamicFieldLogic):
    def compare_dynamic_fields(self, expected, actual, index, index_actual_vlans, print_results=False,
                               print_failures=False):
        return expected.compare_tags(expected, actual, index, index_actual_vlans, None, None, print_results,
                                     print_failures)

    def get_compare_number(self, expected):
        return expected.get_vlan_num()
