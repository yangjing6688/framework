from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
from ExtremeAutomation.Library.Utils.FileUtils import FileUtils


dynamic_label_type = "route_entry"
###########################################################################
# ###
# ###           This builds the packet header class
# ###
############################################################################


def generate_packet_header(protocol, fields):
    """
    Arguments:
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]

    Makes a PacketHeader for 'protocol' from the provided fields.
    """
    s = S()
    dynamic = False
    global dynamic_label_type
    for field in fields:
        if len(field) > 8 and field[8]:
            dynamic = True
    s.a("###########################################################################")
    s.a("# ###   start " + protocol + "PacketHeader")
    s.a("###########################################################################")
    s.a("from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants")
    s.a("from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter")
    s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import "
        "TrafficConfigConstants")
    s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import "
        "TrafficGenerationUtils")
    s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants")
    s.a("from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants")
    s.a("from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject")
    s.a("from ExtremeAutomation.Library.Utils.NumberUtils import *")
    s.a("import ostinato # pip install python-ostinato")
    s.a("from ostinato.core import ost_pb, DroneProxy")
    s.a("# from ostinato.protocols." + protocol.lower() + "_pb2 import " + protocol.lower())
    s.a("import binascii")
    s.a("from ostinato.core import ost_pb")
    s.a("from ostinato.protocols.hexdump_pb2 import hexDump")
    s.a("")
    s.a("")
    s.a("class " + protocol + "PacketHeader(object):")
    s.a("\tpacket_name = None")
    s.a("\tpkt_bytes = None")
    s.a("\t\"\"\"")
    s.a("\tinit function")
    printBitComments(s, fields)
    s.a("\t\"\"\"")
    s.a("")
    s.a("\tdef __init__(self):")
    s.a("\t    self.add_" + protocol.lower() + "_header()")
    if dynamic:
        s.a("\t    self." + dynamic_label_type + "_num = 0")
    s.a("\t    self.HEADER_SIZE_" + protocol.upper() + " = 4  # BYTES")
    s.a("")
    s.a("#######################################")
    s.a("# ### Start of the Accessor Methods")
    s.a("#######################################")
    s.a("\t")
    if dynamic:
        s.a("    def add_" + dynamic_label_type + "_num(self):")
        s.a("        self." + dynamic_label_type + "_num += 1")
        s.a("        return self." + dynamic_label_type + "_num")
        s.a("")
        s.a("    def get_" + dynamic_label_type + "_num(self):")
        s.a("        return self." + dynamic_label_type + "_num")
        s.a("")
        s.a("    def set_" + dynamic_label_type + "_num(self, " + dynamic_label_type + "):")
        s.a("        self." + dynamic_label_type + "_num = NumberUtils.to_integer_value(" + dynamic_label_type + ")")
        s.a("")

    printAccessorsComments(s, protocol, fields)
    s.a("#######################################")
    s.a("# ### End of the Accessor Methods")
    s.a("#######################################")
    s.a("")
    s.a("\tdef to_packet_string(self):")
    s.a("\t\ttable = TableFormatter()")
    printToPackettable(s, protocol, fields)
    s.a("\t\treturn \"\\n\\n" + protocol.upper() + " HEADER\" +table.to_table_string()")
    s.a("")
    s.a("\tdef add_" + protocol.lower() + "_header(self):")
    s.a("\t\tself.register_packet_tag(PacketTagConstants.TAG_" + protocol.upper() + ")")
    s.a("")
    s.a("\tdef build(self):")
    s.a("\t\tself.add_" + protocol.lower() + "_header()")
    s.a("")
    s.a("\tdef get_hltapi_commands(self):")
    s.a("\t\tdummy_dict = dict()")
    printAllHltapiCmds(s, protocol, fields)
    s.a("\t\treturn dummy_dict")
    s.a("")
    s.a("\tdef config_thirdparty_traffic_generator_stream_" + protocol.lower() + "(self, tgen_type, generator_ref, "
                                                                                 "port_string, stream_id, **kwargs):")
    s.a("\t\tif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:")
    s.a("\t\t\tself.config_ostinato_stream_" + protocol.lower() + "(generator_ref, port_string, stream_id, **kwargs)")
    s.a("\t\telif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:")
    s.a("\t\t\tself.config_jets_stream_" + protocol.lower() + "(generator_ref, port_string, stream_id, **kwargs)")
    s.a("\t\telse:")
    s.a("\t\t\treturn EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED")
    s.a("")
    s.a("\tdef config_ostinato_stream_" + protocol.lower() + "(self, drone, port_string, stream_id, **kwargs):")
    s.a("\t\tp = stream_id.protocol.add()")
    s.a("\t\tp.protocol_id.id = ost_pb.Protocol.k" + protocol.lower() + "FieldNumber")
    s.a("\t\tp.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber")
    s.a("\t\tpayloadData = " + protocol + "PacketHeader.get_header_bytes(self).replace(" ", "")")
    s.a("\t\tpayloadData = binascii.a2b_hex(payloadData)")
    s.a("\t\tp.Extensions[hexDump].content = payloadData")
    s.a("\t# update this from the ostinato docs.")
    s.a("\t\t#" + protocol.lower() + "Field = p.Extensions[" + protocol.lower() + "]")
    printOstinatoMethod(s, protocol, fields)
    s.a("")
    s.a("\tdef config_jets_stream_" + protocol.lower() + "(self, jets_dev, port_string, stream_id, **kwargs):")

    s.a("\t\tpkt_fields = {}")
    s.a("\t\theader_name = \"" + protocol.upper() + "_HDR\"")
    s.a("\t\tpkt_bytes = \"0x\" + " + protocol + "PacketHeader.get_header_bytes(self)")
    s.a("\t\tjets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {\"data\": pkt_bytes})")
    printJetsMethod(s, protocol, fields)
    s.a("")
    s.a("\tdef get_ixtclhal_" + protocol.lower() + "_api_commands(self, port_string, streamid):")
    s.a("\t\tport_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)")
    s.a("\t\tdummy_dict = []")
    s.a("\t\tindex = 1")
    s.a("\t\tdummy_dict.append(\"stream get \" + port_string + \" \" + str(streamid))")
    s.a("\t# ### put some IxTclHal info here.")
    printIxtclhal(s, protocol, fields)
    s.a("\t\tdummy_dict.append(\"stream set \" + port_string + \" \" + str(streamid))")
    s.a("\t\tdummy_dict.append(\"stream write \" + port_string + \" \" + str(streamid))")
    s.a("\t\tdummy_dict.append(\"set portList [ list [ list \" + port_string + \"]]\")")
    s.a("\t\tdummy_dict.append(\"ixWriteConfigToHardware portList -noProtocolServer\")")
    s.a("\t\treturn dummy_dict")
    s.a("")
    s.a("\tdef parse_bytes(self):")
    s.a("\t\tpayload = self.get_payload()")
    s.a("\t\tpayload = payload.replace(\" \",\"\")")
    printParseByte(s, protocol, fields)
    s.a("\t\tself.payload = payload")
    s.a("")
    s.a("\tdef get_header_bytes(self):")
    printHeaderByte(s, protocol, fields)
    s.a("")
    s.a("\t@staticmethod")
    s.a("\tdef compare_" + protocol.lower() + "_packet_header(expected, actual, ignore_list, print_results=True, "
                                              "print_failures=True):")
    s.a("\t\tresults = True")
    s.a("\t\ttry:")
    s.a("\t\t\tassert isinstance(expected, " + protocol + "PacketHeader)")
    s.a("\t\t\tassert isinstance(actual, " + protocol + "PacketHeader)")
    printCompareMethod(s, protocol, fields)
    s.a("")
    s.a("")
    s.a("class " + protocol + "PacketConstants:")
    s.a("\t\"\"\"")
    s.a("\tinit function")
    s.a("\t\"\"\"")
    s.a("\tdef __init__(self):")
    s.a("\t\tpass")
    s.a("")
    printConstantsOut(s, protocol, fields)
    s.a("\t#don't allow values to be updated")
    s.a("\tdef __setattr__(self, *_):")
    s.a("\t\tpass")
    s.a("###########################################################################")
    s.a("# ###   end " + protocol + "PacketHeader")
    s.a("###########################################################################\n\n")
    print(str(s))
    FileUtils.write_str_to_file("c:/temp/" + protocol + "PacketHeader.py", str(s).replace("\t", "    "), False)


def printBitComments(s, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:
        s.a("\t\t# " + str(field[1]) + " = " + str(field[2]) + "bits")
    # iterate through fields # version = 4bits
    pass


def printIxtclhal(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:
        if field[5]:
            s.a("\t\tTrafficGenerationUtils.insert_ixtcl_command(dummy_dict, " +
                get_accessor_method(True, "get", protocol, field) + ", \"" + field[5] + "\"" +
                ", PacketConstants." + field[6] + ")")


def printOstinatoMethod(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:
        v = field[1].lower().replace(" ", "_")
        htlcmd = field[4]
        const_name = (protocol + " " + field[1]).upper().replace(" ", "_")
        method = get_accessor_method(False, "get", protocol, field).replace("self", "")
        s.a("\t\t#if self.is_field_set(self." + method + ") :")
        s.a("\t\t#\t" + protocol.lower() + "Field.version = int(self." + method + ")")


def printJetsMethod(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:
        v = field[1].lower().replace(" ", "_")
        htlcmd = field[4]
        const_name = (protocol + " " + field[1]).upper().replace(" ", "_")
        method = get_accessor_method(False, "get", protocol, field).replace("self", "")
        s.a("\t\tif self.is_field_set(self." + method + ") :")
        s.a("\t\t\tpkt_fields[\"" + v + "\"] = int(self." + method + ")")


def printCompareMethod(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:

        dynamic_field = (len(field) > 8 and field[8])
        v = field[1].lower().replace(" ", "_")
        htlcmd = field[4]
        const_name = (protocol + " " + field[1]).upper().replace(" ", "_")
        if dynamic_field:
            method = get_accessor_method(False, "get", protocol, field, "dynamic").replace("self, ", "").replace("self",
                                                                                                                 "")
        else:
            method = get_accessor_method(False, "get", protocol, field).replace("self", "")
        constant_name1 = protocol + "PacketConstants." + const_name
        constant_name2 = "PacketConstants.PACKET_HEADER_L3_\"" + protocol.upper()
        s.a("\t\t\tif expected.is_field_set(expected." + method + ") " +
            "and " + constant_name1 + " not in ignore_list :")
        s.a("\t\t\t\tname = \"" + protocol.upper() + " " + field[1].lower() + " : \"")
        s.a("\t\t\t\tif expected." + method + " != actual." + method + ":")
        s.a("\t\t\t\t\tresults = False")
        s.a("\t\t\t\t\tif print_results or print_failures:")
        s.a("\t\t\t\t\t\tPacketObject.logger.log_error(str(expected." + method + ") + \" != \" + str(actual." +
            method + ") + \" ERROR\")")
        s.a("\t\t\t\telif print_results:")
        s.a("\t\t\t\t\tPacketObject.logger.log_info(name + str(expected." + method + ") + \" == \" + str(actual." +
            method + ") + \" Pass\")")
        s.a("")
    s.a("\t\texcept Exception as e:")
    s.a("\t\t\tresults = False")
    s.a("\t\t\tif print_results or print_failures:")
    s.a("\t\t\t\tPacketObject.logger.log_error(\"Error with " + protocol + "PacketHeader\")")
    s.a("\t\treturn results")


def printAccessorsComments(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    # 1, "Address Family", 2 * 8, PacketConstants.INTEGER, None, False, "", None, True
    # [0] : index
    # [1] : name
    # [2] : bit width
    # [3] : type cast
    # [4] :
    # [5] :
    # [6] :
    # [7] : constants
    # [8] : dynamic
    for field in fields:
        v = field[1].lower().replace(" ", "_")
        htlcmd = field[4]
        if not htlcmd:
            htlcmd = ("TEMP_" + v + "_CMD").upper()
        const_name = (protocol + " " + field[1]).upper().replace(" ", "_")
        s.a("\t# start " + protocol + " " + field[1] + " methods")
        example = " example: "
        if field[3] == PacketConstants.HEX_STRING:
            example += ("F" * (field[2] // 4))
        elif field[3] == PacketConstants.ENET_ADDRESS:
            example += "00:33:44:55:66:44"
        elif field[3] == PacketConstants.IPV4_ADDRESS:
            example += "1.2.3.4"
        elif field[3] == PacketConstants.IPV6_ADDRESS:
            example += "FF01::0001"
        else:  # Integer
            example += "1"
        dynamic_field = (len(field) > 8 and field[8])

        if dynamic_field:
            s.a("\t#  " + v + " is a " + str(field[2]) + " bit " + str(field[3]) + example)
            s.a("\tdef " + get_accessor_method(False, "set", protocol, v, "dynamic") + ":")
            s.a("\t\t" + v + " = self.normalize_value(" + v + ", PacketConstants." + field[3] + ")")
            s.a("\t\tself.set_packet_component(PacketConstants.PACKET_HEADER_L3_" + protocol.upper() + ", " +
                protocol + "PacketConstants." + const_name + " + \" \" + str(index) , " + v + ")")

        else:
            s.a("\t#  " + v + " is a " + str(field[2]) + " bit " + str(field[3]) + example)
            s.a("\tdef " + get_accessor_method(False, "set", protocol, v) + ":")
            s.a("\t\t" + v + " = self.normalize_value(" + v + ", PacketConstants." + field[3] + ")")
            s.a("\t\tself.set_packet_component(PacketConstants.PACKET_HEADER_L3_" + protocol.upper() + ", " +
                protocol + "PacketConstants." + const_name + ", " + v + ")")

        s.a("")
        if dynamic_field:
            s.a("\tdef " + get_accessor_method(False, "get", protocol, field, "dynamic") + ":")
            s.a("\t\treturn self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_" +
                protocol.upper() + ", " + protocol + "PacketConstants." + const_name +
                " + \" \" + str(index)), PacketConstants." + field[3] + ")")
        else:
            s.a("\tdef " + get_accessor_method(False, "get", protocol, field) + ":")
            s.a("\t\treturn self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L3_" +
                protocol.upper() + ", " + protocol + "PacketConstants." + const_name + "), PacketConstants." +
                field[3] + ")")

        s.a("")
        if dynamic_field:
            s.a("\tdef " + get_accessor_method(False, "hlt", protocol, field, "dynamic") + ":")
            s.a("\t\t" + v + " = " + get_accessor_method(True, "get", protocol, field, "dynamic"))
        else:
            s.a("\tdef " + get_accessor_method(False, "hlt", protocol, field) + ":")
            s.a("\t\t" + v + " = " + get_accessor_method(True, "get", protocol, field))

        if field[3] == PacketConstants.INTEGER:
            s.a("\t\tif isinstance(" + v + ", int):")
            s.a("\t\t\t" + v + " = str(" + v + ")")
        s.a("\t\tif " + v + " and 'Not Set' not in " + v + ":")
        s.a("\t\t\tdummy_dict[TrafficConfigConstants." + htlcmd + "] = " + v)
        # # end protocol ip methods
        s.a("\t# end " + protocol + " " + field[1] + " methods")
        s.a("")
    pass


def printToPackettable(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:

        dynamic_field = (len(field) > 8 and field[8])

        if field[3] == PacketConstants.INTEGER:
            #         table.add_row_value("Hdr Length", self.format_int(self.get_ip_hdr_length(), 2))
            if dynamic_field:
                s.a("\t\ttable.add_row_value(\"" + str(field[1]) + "\",  "
                    "self.format_int(" + get_accessor_method(True, "get", protocol, field, "dynamic") + ", " +
                    str(field[2] // 8) + "))")
            else:
                s.a("\t\ttable.add_row_value(\"" + str(field[1]) + "\",  "
                    "self.format_int(" + get_accessor_method(True, "get", protocol, field) + ", " +
                    str(field[2] // 8) + "))")
        else:
            #         table.add_row_value("Source IP", self.get_source_ip())
            if dynamic_field:
                s.a("\t\ttable.add_row_value(\"" + str(field[1]) + "\",  " + get_accessor_method(True, "get", protocol,
                                                                                                 field,
                                                                                                 "dynamic") + ")")
            else:
                s.a("\t\ttable.add_row_value(\"" + str(field[1]) + "\",  " + get_accessor_method(True, "get", protocol,
                                                                                                 field) + ")")
    pass


def printAllHltapiCmds(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    for field in fields:
        # self.get_ip_hdr_length_hltapi_cmd(dummy_dict)
        s.a("\t\t# " + get_accessor_method(True, "hlt", protocol, field))
    pass


def get_accessor_method(print_self, method_type, protocol, field, set_opt=None):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    if print_self:
        print_self = "self."
        print_self_inner = ""
    else:
        print_self = ""
        print_self_inner = "self"
    if method_type == "get":
        if set_opt == "dynamic":
            if print_self_inner != "":
                print_self_inner += ", index"
            else:
                print_self_inner += "index"
        return print_self + "get_" + protocol.lower() + "_" + field[1].lower().replace(" ", "_") + "(" + \
            print_self_inner + ")"
    if method_type == "hlt":
        if print_self_inner:
            print_self_inner += ", "
        if set_opt == "dynamic":
            print_self_inner += "index, "
        return print_self + "get_" + protocol.lower() + "_" + field[1].lower().replace(" ", "_") + \
            "_hltapi_cmd(" + print_self_inner + "dummy_dict)"
    if method_type == "set":
        if set_opt == "dynamic":
            if isinstance(field, list):
                field = field[1]
            return print_self + "set_" + protocol.lower() + "_" + field.lower().replace(" ", "_") + "(" + \
                print_self_inner + ", " + field + ", index, ignore_check=False)"
        elif not set_opt:
            return print_self + "set_" + protocol.lower() + "_" + field.lower().replace(" ", "_") + "(" + \
                print_self_inner + ", " + field + ", ignore_check=False)"
        else:
            return print_self + "set_" + protocol.lower() + "_" + field[1].lower().replace(" ", "_") + "(\"0x\" + " + \
                set_opt + ")"


def printParseByte(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    #
    # # hdlen = 4bits
    # ipv4_hdlen = self.get_bits_from_string(4, payload)
    # self.set_ip_hdr_length("0x" + ipv4_hdlen)
    # payload = self.remove_bits_from_string(4, payload)
    for field in fields:
        dynamic_field = (len(field) > 8 and field[8])
        v = field[1].lower().replace(" ", "_")
        s.a("\t\t" + v + " = self.get_bits_from_string(" + str(field[2]) + ", payload)")
        if dynamic_field:
            field[1] = v
            s.a("\t\t" + get_accessor_method(True, "set", protocol, field, "dynamic").replace("(,", "("))
        else:
            s.a("\t\t" + get_accessor_method(True, "set", protocol, field, v))
        s.a("\t\tpayload = self.remove_bits_from_string(" + str(field[2]) + ", payload)")

    pass


def printHeaderByte(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    s.a("\t\tret_string = \"\"")
    for field in fields:
        dynamic_field = (len(field) > 8 and field[8])
        v = field[1].lower().replace(" ", "_")
        if dynamic_field:
            s.a("\t\tret_string += self.format_byte_string(" + get_accessor_method(
                True, "get", protocol, field, "dynamic") + ", PacketConstants." + field[3] + ", " + str(field[2]) + ")")
        else:
            s.a("\t\tret_string += self.format_byte_string(" + get_accessor_method(
                True, "get", protocol, field) + ", PacketConstants." + field[3] + ", " + str(field[2]) + ")")
    # version = self.format_byte_string("4", PacketConstants.INTEGER, 4)
    # hdlen = self.format_byte_string(self.get_ip_hdr_length(), PacketConstants.INTEGER, 4)
    s.a("\t\treturn ret_string")
    pass


def printConstantsOut(s, protocol, fields):
    """
    fields = [position, name, bits, type, hltcomand_name, gen_ixtclhal, ixtclhal_type,constants]
    """
    # IPV4_VERSION = "IPV4_VERSION"
    for field in fields:
        v = field[1].lower().replace(" ", "_")
        s.a("\t" + (protocol + "_" + v).upper() + " = \"" + (protocol + "_" + v).upper().replace(" ", "_") + "\"")
        if field[7]:
            for key in field[7]:
                s.a("\t" + (protocol + "_" + v + "_" + str(field[7][key])).upper().replace(" ", "_") + " = \"" +
                    str(key) + "\"")
            const_str = "\t" + (protocol + "_" + v).upper() + "S = {"
            for key in field[7]:
                const_str += "\t\t" + str(key) + " : \"" + str(field[7][key]) + "\",\n"
            const_str += "\t}"
            s.a(const_str)
        s.a("")


###########################################################################
# ###
# ###           This builds the individual packet classes
# ###
###########################################################################
def generate_packet(parent, packetNameStart, packetNameEnd, protocol, fields, tag_type):
    # make a PacketHeader
    header_name = protocol + "PacketHeader"
    class_name = packetNameStart + protocol + packetNameEnd
    s = S()

    if "ipv4" in parent.lower():
        s.a("from ExtremeAutomation.Library.Net.Packet.IpV4." + parent + " import " + parent)
    elif "ipv6" in parent.lower():
        s.a("from ExtremeAutomation.Library.Net.Packet.IpV6." + parent + " import " + parent)
    else:
        s.a("from ExtremeAutomation.Library.Net.Packet." + parent + " import " + parent)
    s.a("from ExtremeAutomation.Library.Net.Packet.PacketHeaders." + header_name + " import " + header_name)
    s.a("")
    s.a("")
    s.a("class " + class_name + "(" + parent + ", " + header_name + "):")
    if tag_type == "VlanStack":
        s.a("\tdef __init__(self, num_tags):")
        s.a("\t\tsuper(" + class_name + ", self).__init__(num_tags)")
    else:
        s.a("\tdef __init__(self):")
        s.a("\t\tsuper(" + class_name + ", self).__init__()")
    s.a("\t\t" + header_name + ".__init__(self)")
    s.a("\t\tself.set_name(\"" + class_name + "\")")
    s.a("")
    s.a("\tdef to_packet_string(self):")
    s.a("\t\treturn super(" + class_name + ", self).to_packet_string() + \\")
    s.a("\t\t\t\t" + header_name + ".to_packet_string(self)")
    s.a("")
    s.a("\tdef build(self):")
    s.a("\t\tsuper(" + class_name + ", self).build()")
    s.a("\t\t" + header_name + ".build(self)")
    s.a("")
    s.a("\tdef get_header_length(self):")
    s.a("\t\tsuper(" + class_name + ", self).build()")
    s.a("\t\treturn super(" + class_name + ", self).get_header_length() + self.HEADER_SIZE_" + protocol.upper())
    s.a("")
    s.a("\tdef get_hltapi_commands(self):")
    s.a("\t\tcmd_dict = super(" + class_name + ", self).get_hltapi_commands()")
    s.a("\t\tcmd_dict.update(" + header_name + ".get_hltapi_commands(self))")
    s.a("\t\treturn cmd_dict")
    s.a("")
    s.a("\tdef set_payload(self, payload):")
    s.a("\t\tpayload = payload.replace(\" \",\"\")")
    s.a("\t\tsuper(" + class_name + ", self).set_payload(payload)")
    s.a("\t\t" + header_name + ".parse_bytes(self)")
    s.a("")
    s.a("\tdef get_header_bytes(self, break_up_header=False):")
    s.a("\t\ttemp_bytes = super(" + class_name + ", self).get_header_bytes(break_up_header)")
    s.a("\t\tif break_up_header:")
    s.a("\t\t\ttemp_bytes += \"|\"")
    s.a("\t\ttemp_bytes += \" \" + " + header_name + ".get_header_bytes(self)")
    s.a("\t\treturn temp_bytes.replace(\" \", \"\")")
    s.a("")

    s.a("\tdef config_thirdparty_traffic_generator_stream(self, tgen_type, generator_ref, port_string, stream_id, "
        "**kwargs):")
    s.a("\t\tsuper(" + class_name + ", self).config_thirdparty_traffic_generator_stream(tgen_type, generator_ref, "
                                    "port_string, stream_id, **kwargs)")
    s.a("\t\t" + header_name + ".config_thirdparty_traffic_generator_stream_" + protocol.lower() +
        "(self, tgen_type, generator_ref, port_string, stream_id, **kwargs)")
    s.a("")

    print(s)
    FileUtils.write_str_to_file("c:/temp/" + class_name + ".py", str(s).replace("\t", "    "), False)


def end_packet(protocol, fields):
    s = S()
    s.a("add this to PacketConstants")
    s.a("PACKET_HEADER_L3_" + protocol.upper() + " = \"PACKET_HEADER_L3_" + protocol.upper() + "\"")
    s.a("")
    s.a("this has to be changed and implemented in TrafficConfigConstants")
    for field in fields:
        v = field[1].lower().replace(" ", "_")
        htlcmd = field[4]
        if not htlcmd:
            htlcmd = ("TEMP_" + v + "_CMD").upper()
        s.a(htlcmd)
    print(s)


###########################################################################
# ###
# ###           basically a string buffer
# ###
###########################################################################
class S(object):
    def __init__(self):
        self.contents = ""

    def a(self, line):
        self.contents += line + "\n"

    def __str__(self):
        return self.contents
