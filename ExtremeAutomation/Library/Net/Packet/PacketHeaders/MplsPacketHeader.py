import binascii
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacketConstants
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.hexdump_pb2 import hexDump


class MplsPacketHeader(object):
    packet_name = None
    pkt_bytes = None
    """
    MPLS Packet Header
        # label = 20bits
        # experimental bits = 3bits
        # bottom of label stack = 1bits
        # ttl = 8bits
    """

    def __init__(self):
        self.num_labels = 0
        self.add_mpls_header()
        self.HEADER_SIZE_MPLS = 4  # BYTES

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    def add_mpls_label(self):
        self.num_labels += 1
        return self.num_labels

    def get_label_num(self):
        return self.num_labels

    def set_label_num(self, num_tags):
        self.num_labels = NumberUtils.to_integer_value(num_tags)

    # start Mpls label methods
    #  label is a 20 bit INTEGER example: 1
    def set_mpls_label(self, label, stack, ignore_check=False):
        label = self.normalize_value(label, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_LABEL + " " +
                                  str(stack), label)

    def get_mpls_label(self, stack):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_LABEL + " " + str(stack)),
            PacketConstants.INTEGER)

    def get_mpls_label_hltapi_cmd(self, dummy_dict, stack):
        label = self.get_mpls_label(stack)
        if isinstance(label, int):
            label = str(label)
        if label and 'Not Set' not in label:
            dummy_dict[TrafficConfigConstants.TEMP_LABEL_CMD] = label
    # end Mpls label methods

    # start Mpls experimental bits methods
    #  experimental_bits is a 3 bit INTEGER example: 1
    def set_mpls_experimental_bits(self, experimental_bits, stack, ignore_check=False):
        experimental_bits = self.normalize_value(experimental_bits, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MPLS,
                                  MplsPacketConstants.MPLS_EXPERIMENTAL_BITS + " " + str(stack), experimental_bits)

    def get_mpls_experimental_bits(self, stack):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_EXPERIMENTAL_BITS + " " + str(stack)),
            PacketConstants.INTEGER)

    def get_mpls_experimental_bits_hltapi_cmd(self, dummy_dict, stack):
        experimental_bits = self.get_mpls_experimental_bits(stack)
        if isinstance(experimental_bits, int):
            experimental_bits = str(experimental_bits)
        if experimental_bits and 'Not Set' not in experimental_bits:
            dummy_dict[TrafficConfigConstants.TEMP_EXPERIMENTAL_BITS_CMD] = experimental_bits
    # end Mpls experimental bits methods

    # start Mpls bottom of label stack methods
    #  bottom_of_label_stack is a 1 bit INTEGER example: 1
    def set_mpls_bottom_of_label_stack(self, bottom_of_label_stack, stack, ignore_check=False):
        bottom_of_label_stack = self.normalize_value(bottom_of_label_stack, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MPLS,
                                  MplsPacketConstants.MPLS_BOTTOM_OF_LABEL_STACK + " " + str(stack),
                                  bottom_of_label_stack)

    def get_mpls_bottom_of_label_stack(self, stack):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_BOTTOM_OF_LABEL_STACK + " " + str(stack)),
            PacketConstants.INTEGER)

    def get_mpls_bottom_of_label_stack_hltapi_cmd(self, dummy_dict, stack):
        bottom_of_label_stack = self.get_mpls_bottom_of_label_stack(stack)
        if isinstance(bottom_of_label_stack, int):
            bottom_of_label_stack = str(bottom_of_label_stack)
        if bottom_of_label_stack and 'Not Set' not in bottom_of_label_stack:
            dummy_dict[TrafficConfigConstants.TEMP_BOTTOM_OF_LABEL_STACK_CMD] = bottom_of_label_stack
    # end Mpls bottom of label stack methods

    # start Mpls ttl methods
    #  ttl is a 8 bit INTEGER example: 1
    def set_mpls_ttl(self, ttl, stack, ignore_check=False):
        ttl = self.normalize_value(ttl, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_TTL + " " +
                                  str(stack), ttl)

    def get_mpls_ttl(self, stack):
        return self.normalize_value(self.get_packet_component(
            PacketConstants.PACKET_HEADER_L3_MPLS, MplsPacketConstants.MPLS_TTL + " " + str(stack)),
            PacketConstants.INTEGER)

    def get_mpls_ttl_hltapi_cmd(self, dummy_dict, stack):
        ttl = self.get_mpls_ttl(stack)
        if isinstance(ttl, int):
            ttl = str(ttl)
        if ttl and 'Not Set' not in ttl:
            dummy_dict[TrafficConfigConstants.TEMP_TTL_CMD] = ttl
    # end Mpls ttl methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        index = 1
        ret_string = "\nMPLS Label number : " + str(self.get_label_num())
        table = TableFormatter()
        for index in range(1, NumberUtils.to_integer_value(self.get_label_num()) + 1):
            table.add_row_value("Label", self.format_int(self.get_mpls_label(index), 2))
            table.add_row_value("Experimental Bits", self.format_int(self.get_mpls_experimental_bits(index), 1))
            table.add_row_value("Bottom Of Stack", self.format_int(self.get_mpls_bottom_of_label_stack(index), 1))
            table.add_row_value("TRL", self.format_int(self.get_mpls_ttl(index), 1))
            index += 1
        return "\n\nMPLS HEADER" + table.to_table_string()

    def add_mpls_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_MPLS)

    def build(self):
        self.add_mpls_header()
        self.set_ether_type("0x8847", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        # self.get_mpls_label_hltapi_cmd(dummy_dict)
        # self.get_mpls_experimental_bits_hltapi_cmd(dummy_dict)
        # self.get_mpls_bottom_of_label_stack_hltapi_cmd(dummy_dict)
        # self.get_mpls_ttl_hltapi_cmd(dummy_dict)
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_mpls(self, tgen_type, generator_ref, port_string, stream_id,
                                                        **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_mpls(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_mpls(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_mpls(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
        payloadData = MplsPacketHeader.get_header_bytes(self).replace(" ", "")
        payloadData = binascii.a2b_hex(payloadData)
        p.Extensions[hexDump].content = payloadData
        # update this from the ostinato docs.
        #     mplsField = p.Extensions[mpls]
        #     if self.is_field_set(self.get_mpls_label()):
        #         mplsField.version = int(self.get_mpls_label())
        #     if self.is_field_set(self.get_mpls_experimental_bits()):
        #         mplsField.version = int(self.get_mpls_experimental_bits())
        #     if self.is_field_set(self.get_mpls_bottom_of_label_stack()):
        #         mplsField.version = int(self.get_mpls_bottom_of_label_stack())
        #     if self.is_field_set(self.get_mpls_ttl()):
        #         mplsField.version = int(self.get_mpls_ttl())

    def config_jets_stream_mpls(self, jets_dev, port_string, stream_id, **kwargs):
        return self.log_unimplemented_method()
        # """
        # MPLS_HDR {
        #   MPLS_INFO [] : pdu_length() - frag_offset();
        # } display="MPLS Stack";
        #
        # MPLS_INFO {
        #   value		: 20 : default=0, display="Label Value %dec", index=1;
        #   reserved	: 3 : display="Reserved", index=2, default=0;
        #   bottom_of_stack : 1 : default=0x1, display="Bottom of Stack %dec", index=3;
        #   ttl		: 8 : default=0xff, display="Time to Live %dec", index=4;
        #   child (bottom_of_stack) : 0 : {
        #     MPLS_INFO (0),
        #     ENET_VPN_HDR(1)
        #   };
        # } display="MPLS Information %dec";
        #
        # :param jets_dev:
        # :param port_string:
        # :param stream_id:
        # :param options:
        # :return:
        # """
        # pkt_fields = {}
        # header_name = "MPLS_HDR"
        # header_name_2 = "MPLS_INFO"
        # jets_dev.pdl_add_packet_header(header_name, pkt_fields)
        # index = 1
        # for index in range(1, NumberUtils.to_integer_value(self.get_label_num()) + 1):
        #     if self.is_field_set(self.get_mpls_label(index)):
        #         pkt_fields["value"] = int(self.get_mpls_label(index))
        #     if self.is_field_set(self.get_mpls_experimental_bits(index)):
        #         pkt_fields["reserved"] = int(self.get_mpls_experimental_bits(index))
        #     if self.is_field_set(self.get_mpls_bottom_of_label_stack(index)):
        #         pkt_fields["bottom_of_stack"] = int(self.get_mpls_bottom_of_label_stack(index))
        #     if self.is_field_set(self.get_mpls_ttl(index)):
        #         pkt_fields["ttl"] = int(self.get_mpls_ttl(index))
        #     jets_dev.pdl_add_packet_header(header_name_2, pkt_fields)
        #     index +=1
        # pkt_bytes = "0x" + MplsPacketHeader.get_header_bytes(self)
        # jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})

    def get_ixtclhal_mpls_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        num = self.get_label_num()
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        num = NumberUtils.to_integer_value(self.get_label_num())
        dummy_dict.append("protocol config -enableMPLS                         true")
        dummy_dict.append("protocolServer set " + port_string)
        index = 1
        dummy_dict.append("mpls setDefault")
        dummy_dict.append("mpls config -type                               mplsUnicast")
        dummy_dict.append("mpls config -forceBottomOfStack                 true")
        dummy_dict.append("mpls config -enableAutomaticallySetLabel        true")
        for index in range(1, num + 1):
            dummy_dict.append("mplsLabel setDefault")
            if self.is_field_set(self.get_mpls_label(index)):
                dummy_dict.append("mplsLabel config -label                              " +
                                  str(self.get_mpls_label(index)))
            else:
                dummy_dict.append("mplsLabel config -label                              0")

            if self.is_field_set(self.get_mpls_experimental_bits(index)):
                dummy_dict.append("mplsLabel config -experimentalUse                    " +
                                  str(self.get_mpls_experimental_bits(index)))
            else:
                dummy_dict.append("mplsLabel config -experimentalUse                    0")

            if self.is_field_set(self.get_mpls_ttl(index)):
                dummy_dict.append("mplsLabel config -timeToLive                         " +
                                  str(self.get_mpls_ttl(index)))
            else:
                dummy_dict.append("mplsLabel config -timeToLive                         64")

            if self.is_field_set(self.get_mpls_bottom_of_label_stack(index)):
                dummy_dict.append("mplsLabel config -bottomOfStack                      true")
            else:
                dummy_dict.append("mplsLabel config -bottomOfStack                      false")

            dummy_dict.append("mplsLabel set " + str(index))
        dummy_dict.append("mpls set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        bFound = False
        index = 1
        self.set_label_num(0)
        while len(payload) > 0 and not bFound:
            self.add_mpls_label()
            value = self.get_bits_from_string(24, payload)
            value = NumberUtils.to_integer_value("0x" + value)
            payload = self.remove_bits_from_string(24, payload)
            label = (value & 0x0FFF0) >> 4
            self.set_mpls_label(label, index)
            experimental_bits = (value & 0x0E) >> 1
            self.set_mpls_experimental_bits(experimental_bits, index)
            bottom_of_label_stack = (value & 0x01)
            self.set_mpls_bottom_of_label_stack(bottom_of_label_stack, index)
            bFound = NumberUtils.to_integer_value(bottom_of_label_stack) > 0
            ttl = self.get_bits_from_string(8, payload)
            self.set_mpls_ttl("0x" + ttl, index)
            payload = self.remove_bits_from_string(8, payload)
            index += 1
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        index = 1
        for index in range(1, NumberUtils.to_integer_value(self.get_label_num()) + 1):
            value = 0
            if self.is_field_set(self.get_mpls_label(index)):
                value |= NumberUtils.to_integer_value(self.get_mpls_label(index)) << 4
            if self.is_field_set(self.get_mpls_experimental_bits(index)):
                value |= NumberUtils.to_integer_value(self.get_mpls_experimental_bits(index)) << 1
            if self.is_field_set(self.get_mpls_bottom_of_label_stack(index)):
                value |= NumberUtils.to_integer_value(self.get_mpls_bottom_of_label_stack(index))
            ret_string += self.format_byte_string(value, PacketConstants.INTEGER, 24)
            ret_string += self.format_byte_string(self.get_mpls_ttl(index), PacketConstants.INTEGER, 8)
            index += 1
        return ret_string

    @staticmethod
    def compare_mpls_packet_header(expected, actual, ignore_list, print_results=True, print_failures=True):
        results = True
        try:
            assert isinstance(expected, MplsPacketHeader)
            assert isinstance(actual, MplsPacketHeader)
            index = 1
            for index in range(1, NumberUtils.to_integer_value(expected.get_mpls_label(index)) + 1):
                if expected.is_field_set(expected.get_mpls_label(index)) and \
                        MplsPacketConstants.MPLS_LABEL not in ignore_list:
                    name = "MPLS label : "
                    if expected.get_mpls_label(index) != actual.get_mpls_label(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_mpls_label(index)) + " != " +
                                                          str(actual.get_mpls_label(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_mpls_label(index)) + " == " +
                                                     str(actual.get_mpls_label(index)) + " Pass")

                if expected.is_field_set(expected.get_mpls_experimental_bits(index)) and \
                        MplsPacketConstants.MPLS_EXPERIMENTAL_BITS not in ignore_list:
                    name = "MPLS experimental bits : "
                    if expected.get_mpls_experimental_bits(index) != actual.get_mpls_experimental_bits(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_mpls_experimental_bits(index)) + " != " +
                                                          str(actual.get_mpls_experimental_bits(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_mpls_experimental_bits(index)) + " == " +
                                                     str(actual.get_mpls_experimental_bits(index)) + " Pass")

                if expected.is_field_set(expected.get_mpls_bottom_of_label_stack(index)) and \
                        MplsPacketConstants.MPLS_BOTTOM_OF_LABEL_STACK not in ignore_list:
                    name = "MPLS bottom of label stack : "
                    if expected.get_mpls_bottom_of_label_stack(index) != actual.get_mpls_bottom_of_label_stack(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_mpls_bottom_of_label_stack(index)) +
                                                          " != " + str(actual.get_mpls_bottom_of_label_stack(index)) +
                                                          " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_mpls_bottom_of_label_stack(index)) +
                                                     " == " + str(actual.get_mpls_bottom_of_label_stack(index)) +
                                                     " Pass")

                if expected.is_field_set(expected.get_mpls_ttl(index)) and \
                        MplsPacketConstants.MPLS_TTL not in ignore_list:
                    name = "MPLS ttl : "
                    if expected.get_mpls_ttl(index) != actual.get_mpls_ttl(index):
                        results = False
                        if print_results or print_failures:
                            PacketObject.logger.log_error(str(expected.get_mpls_ttl(index)) + " != " +
                                                          str(actual.get_mpls_ttl(index)) + " ERROR")
                    elif print_results:
                        PacketObject.logger.log_info(name + str(expected.get_mpls_ttl(index)) + " == " +
                                                     str(actual.get_mpls_ttl(index)) + " Pass")
                index += 1

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with MplsPacketHeader")
        return results


class MplsPacketConstants:
    def __init__(self):
        pass

    MPLS_LABEL = "MPLS_LABEL"
    MPLS_EXPERIMENTAL_BITS = "MPLS_EXPERIMENTAL_BITS"
    MPLS_BOTTOM_OF_LABEL_STACK = "MPLS_BOTTOM_OF_LABEL_STACK"
    MPLS_TTL = "MPLS_TTL"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
