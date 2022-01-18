from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants, PacketTagConstants
from ExtremeAutomation.Library.Utils.TableFormatter import TableFormatter
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import TrafficConfigConstants
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.EthernetPacketConstants import EthernetPacketConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.core import ost_pb
from ExtremeAutomation.Library.Device.TrafficGeneration.Ostinato.Dummy.ostinato.protocols.tcp_pb2 import tcp
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketObject
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer4PacketHeader import Layer4PacketHeader
from ExtremeAutomation.Library.Net.Packet.Checksum import Checksum
from ExtremeAutomation.Library.Device.TrafficGeneration.Jets.JetsDeviceConstants import JetsDeviceConstants


class TcpPacketHeader(Layer4PacketHeader):
    packet_name = None
    pkt_bytes = None
    """
    TCP Packet Header
        # source port = 16bits
        # destination port = 16bits
        # sequence number = 32bits
        # acknowledgement number = 32bits
        # data offset = 4bits
        # reserved = 8bits
        # flags = 4bits
        # window = 16bits
        # checksum = 16bits
        # urgent porter = 16bits
        # options = nbits
    """

    def __init__(self):
        super(TcpPacketHeader, self).__init__()
        self.add_header()
        self.HEADER_SIZE_TCP = (16 + 16 + 32 + 32 + 4 + 8 + 4 + 16 + 16 + 16) // 8

    #######################################
    # ### Start of the Accessor Methods
    #######################################

    # start Tcp source port methods
    #  source_port is a 16 bit INTEGER example: 1
    def set_source_port(self, source_port, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_SOURCE_PORT, ignore_check)
        source_port = self.normalize_value(source_port, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_SOURCE_PORT, source_port)

    def get_source_port(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_SOURCE_PORT),
            PacketConstants.INTEGER)

    def get_source_port_hltapi_cmd(self, dummy_dict):
        source_port = self.get_source_port()
        if isinstance(source_port, int):
            source_port = str(source_port)
        if source_port and 'Not Set' not in source_port:
            dummy_dict[TrafficConfigConstants.TCP_SRC_PORT_CMD] = source_port
    # end Tcp source port methods

    # start Tcp destination port methods
    #  destination_port is a 16 bit INTEGER example: 1
    def set_destination_port(self, destination_port, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_DESTINATION_PORT, ignore_check)
        destination_port = self.normalize_value(destination_port, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_DESTINATION_PORT,
                                  destination_port)

    def get_destination_port(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_DESTINATION_PORT),
            PacketConstants.INTEGER)

    def get_destination_port_hltapi_cmd(self, dummy_dict):
        destination_port = self.get_destination_port()
        if isinstance(destination_port, int):
            destination_port = str(destination_port)
        if destination_port and 'Not Set' not in destination_port:
            dummy_dict[TrafficConfigConstants.TCP_DST_PORT_CMD] = destination_port
    # end Tcp destination port methods

    # start Tcp sequence number methods
    #  sequence_number is a 32 bit INTEGER example: 1
    def set_sequence_number(self, sequence_number, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_SEQUENCE_NUMBER, ignore_check)
        sequence_number = self.normalize_value(sequence_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_SEQUENCE_NUMBER,
                                  sequence_number)

    def get_sequence_number(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_SEQUENCE_NUMBER),
            PacketConstants.INTEGER)

    def get_sequence_number_hltapi_cmd(self, dummy_dict):
        sequence_number = self.get_sequence_number()
        if isinstance(sequence_number, int):
            sequence_number = str(sequence_number)
        if sequence_number and 'Not Set' not in sequence_number:
            dummy_dict[TrafficConfigConstants.TEMP_SEQUENCE_NUMBER_CMD] = sequence_number
    # end Tcp sequence number methods

    # start Tcp acknowledgement number methods
    #  acknowledgement_number is a 32 bit INTEGER example: 1
    def set_acknowledgement_number(self, acknowledgement_number, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_ACKNOWLEDGEMENT_NUMBER, ignore_check)
        acknowledgement_number = self.normalize_value(acknowledgement_number, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_ACKNOWLEDGEMENT_NUMBER,
                                  acknowledgement_number)

    def get_acknowledgement_number(self):
        return self.normalize_value(self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP,
                                                              TcpPacketConstants.TCP_ACKNOWLEDGEMENT_NUMBER),
                                    PacketConstants.INTEGER)

    def get_acknowledgement_number_hltapi_cmd(self, dummy_dict):
        acknowledgement_number = self.get_acknowledgement_number()
        if isinstance(acknowledgement_number, int):
            acknowledgement_number = str(acknowledgement_number)
        if acknowledgement_number and 'Not Set' not in acknowledgement_number:
            dummy_dict[TrafficConfigConstants.TEMP_ACKNOWLEDGEMENT_NUMBER_CMD] = acknowledgement_number
    # end Tcp acknowledgement number methods

    # start Tcp data offset methods
    #  data_offset is a 4 bit INTEGER example: 1
    def set_data_offset(self, data_offset, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_DATA_OFFSET, ignore_check)
        data_offset = self.normalize_value(data_offset, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_DATA_OFFSET, data_offset)

    def get_data_offset(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_DATA_OFFSET),
            PacketConstants.INTEGER)

    def get_data_offset_hltapi_cmd(self, dummy_dict):
        data_offset = self.get_data_offset()
        if isinstance(data_offset, int):
            data_offset = str(data_offset)
        if data_offset and 'Not Set' not in data_offset:
            dummy_dict[TrafficConfigConstants.TEMP_DATA_OFFSET_CMD] = data_offset
    # end Tcp data offset methods

    # start Tcp reserved methods
    #  reserved is a 8 bit INTEGER example: 1
    def set_reserved(self, reserved, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_RESERVED, ignore_check)
        reserved = self.normalize_value(reserved, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_RESERVED, reserved)

    def get_reserved(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_RESERVED),
            PacketConstants.INTEGER)

    def get_reserved_hltapi_cmd(self, dummy_dict):
        reserved = self.get_reserved()
        if isinstance(reserved, int):
            reserved = str(reserved)
        if reserved and 'Not Set' not in reserved:
            dummy_dict[TrafficConfigConstants.TEMP_RESERVED_CMD] = reserved
    # end Tcp reserved methods

    # start Tcp flags methods
    #  flags is a 4 bit INTEGER example: 1
    def set_flags(self, flags, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_FLAGS, ignore_check)
        flags = self.normalize_value(flags, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_FLAGS, flags)

    def get_flags(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_FLAGS),
            PacketConstants.INTEGER)

    def get_flags_hltapi_cmd(self, dummy_dict):
        flags = self.get_flags()
        if isinstance(flags, int):
            flags = str(flags)
        if flags and 'Not Set' not in flags:
            dummy_dict[TrafficConfigConstants.TEMP_FLAGS_CMD] = flags
    # end Tcp flags methods

    # start Tcp window methods
    #  window is a 16 bit INTEGER example: 1
    def set_window(self, window, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_WINDOW, ignore_check)
        window = self.normalize_value(window, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_WINDOW, window)

    def get_window(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_WINDOW),
            PacketConstants.INTEGER)

    def get_window_hltapi_cmd(self, dummy_dict):
        window = self.get_window()
        if isinstance(window, int):
            window = str(window)
        if window and 'Not Set' not in window:
            dummy_dict[TrafficConfigConstants.TEMP_WINDOW_CMD] = window
    # end Tcp window methods

    # start Tcp checksum methods
    #  checksum is a 16 bit INTEGER example: 1
    def set_tcp_checksum(self, checksum, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_CHECKSUM, ignore_check)
        checksum = self.normalize_value(checksum, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_CHECKSUM, checksum)

    def get_tcp_checksum(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_CHECKSUM),
            PacketConstants.INTEGER)

    def get_tcp_checksum_hltapi_cmd(self, dummy_dict):
        checksum = self.get_tcp_checksum()
        if isinstance(checksum, int):
            checksum = str(checksum)
        if checksum and 'Not Set' not in checksum:
            dummy_dict[TrafficConfigConstants.TEMP_CHECKSUM_CMD] = checksum
    # end Tcp checksum methods

    # start Tcp urgent porter methods
    #  urgent_porter is a 16 bit INTEGER example: 1
    def set_urgent_porter(self, urgent_porter, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_URGENT_PORTER, ignore_check)
        urgent_porter = self.normalize_value(urgent_porter, PacketConstants.INTEGER)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_URGENT_PORTER,
                                  urgent_porter)

    def get_urgent_porter(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_URGENT_PORTER),
            PacketConstants.INTEGER)

    def get_urgent_porter_hltapi_cmd(self, dummy_dict):
        urgent_porter = self.get_urgent_porter()
        if isinstance(urgent_porter, int):
            urgent_porter = str(urgent_porter)
        if urgent_porter and 'Not Set' not in urgent_porter:
            dummy_dict[TrafficConfigConstants.TEMP_URGENT_PORTER_CMD] = urgent_porter
    # end Tcp urgent porter methods

    # start Tcp options methods
    #  options is a 0 bit INTEGER example: 1
    def set_options(self, options, ignore_check=False):
        self.set_packet_field_default_ignore_comparison(TcpPacketConstants.TCP_OPTIONS, ignore_check)
        options = self.normalize_value(options, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_OPTIONS, options)

    def set_options_and_auto_pad(self, ip):
        ip = self.normalize_value(ip, PacketConstants.HEX_STRING)
        if len(ip.replace(" ", "")) % 8 != 0:
            ip += "0" * (8 - len(ip.replace(" ", "")) % 8)
            ip = self.normalize_value(ip, PacketConstants.HEX_STRING)
        self.set_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_OPTIONS, ip)

    def get_options(self):
        return self.normalize_value(
            self.get_packet_component(PacketConstants.PACKET_HEADER_L4_TCP, TcpPacketConstants.TCP_OPTIONS),
            PacketConstants.HEX_STRING)

    def get_options_hltapi_cmd(self, dummy_dict):
        options = self.get_options()
        if isinstance(options, int):
            options = str(options)
        if options and 'Not Set' not in options:
            dummy_dict[TrafficConfigConstants.TEMP_OPTIONS_CMD] = options
    # end Tcp options methods

    #######################################
    # ### End of the Accessor Methods
    #######################################

    def to_packet_string(self):
        table = TableFormatter()
        table.add_row_value("source port", self.format_int(self.get_source_port(), 4))
        table.add_row_value("destination port", self.format_int(self.get_destination_port(), 4))
        table.add_row_value("sequence number", self.format_int(self.get_sequence_number(), 8))
        table.add_row_value("acknowledgement number", self.format_int(self.get_acknowledgement_number(), 8))
        table.add_row_value("data offset", self.format_int(self.get_data_offset(), 1))
        table.add_row_value("reserved", self.format_int(self.get_reserved(), 2))
        table.add_row_value("flags", self.format_int(self.get_flags(), 1))
        table.add_row_value("window", self.format_int(self.get_window(), 4))
        table.add_row_value("checksum", self.format_int(self.get_tcp_checksum(), 4))
        table.add_row_value("urgent porter", self.format_int(self.get_urgent_porter(), 4))
        table.add_row_value("options", self.get_options())
        return "\n\nTCP HEADER" + table.to_table_string()

    def get_ixtclhal_tcp_api_commands(self, port_string, streamid):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = []
        index = 1
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # dummy_dict.append("tcp get " + port_string)
        options = str(self.get_options())
        if "Not" not in options and len(options) > 0:
            dummy_dict.append("tcp configure -options \"" + options + "\"")
        options = str(self.get_data_offset())
        if "Not" not in options and len(options) > 0:
            dummy_dict.append("tcp configure -offset " + options)
        # ### put some IxTclHal info here.
        dummy_dict.append("tcp set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        return dummy_dict

    def get_spirent_tcp_api_commands(self, port_name_stream):
        dummy_dict = []

        # if self.is_field_set(self.get_ip_tos()):
        #      dummy_dict.append("stc::config $" + port_name_stream + ".ethernet:EthernetII -etherType " +
        #                        str(self.get_ether_type()))
        if len(dummy_dict) > 0:
            dummy_dict.append("puts [stc::get $" + port_name_stream + " ]")
        return dummy_dict

    def add_header(self):
        self.register_packet_tag(PacketTagConstants.TAG_TCP)

    def build(self):
        self.add_header()
        if isinstance(self, IpV4PacketHeader):  # you can either do this here OR in the build of each packet
            self.set_ip_protocol("0x06", True)
        elif isinstance(self, IpV6PacketHeader):
            self.set_ipv6_next_header("0x06", True)

    def get_hltapi_commands(self):
        dummy_dict = dict()
        self.get_destination_port_hltapi_cmd(dummy_dict)
        self.get_source_port_hltapi_cmd(dummy_dict)
        # self.get_sequence_number_hltapi_cmd(dummy_dict)
        # self.get_acknowledgement_number_hltapi_cmd(dummy_dict)
        # self.get_data_offset_hltapi_cmd(dummy_dict)
        # self.get_reserved_hltapi_cmd(dummy_dict)
        # self.get_flags_hltapi_cmd(dummy_dict)
        # self.get_window_hltapi_cmd(dummy_dict)
        # self.get_tcp_checksum_hltapi_cmd(dummy_dict)
        # self.get_urgent_porter_hltapi_cmd(dummy_dict)
        # self.get_options_hltapi_cmd(dummy_dict)

        dummy_dict[TrafficConfigConstants.L4_PROTOCOL_CMD] = TrafficConfigConstants.L4_PROTOCOL_TCP  # constant value
        return dummy_dict

    def config_thirdparty_traffic_generator_stream_tcp(self, tgen_type, generator_ref, port_string, stream_id,
                                                       **kwargs):
        if tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_OSTINATO:
            self.config_ostinato_stream_tcp(generator_ref, port_string, stream_id, **kwargs)
        elif tgen_type == EthernetPacketConstants.TRAFFIC_GENERATION_JETS:
            self.config_jets_stream_tcp(generator_ref, port_string, stream_id, **kwargs)
        else:
            return EthernetPacketConstants.TRAFFIC_GENERATION_NOT_SUPPORTED

    def config_ostinato_stream_tcp(self, drone, port_string, stream_id, **kwargs):
        p = stream_id.protocol.add()
        p.protocol_id.id = ost_pb.Protocol.kTcpFieldNumber
        tcpField = p.Extensions[tcp]
        # ack_num = {int} 0
        if self.is_field_set(self.get_acknowledgement_number()):
            tcpField.ack_num = int(self.get_acknowledgement_number())
        # cksum = {int} 0
        # is_override_cksum = {bool} False
        if self.is_field_set(self.get_tcp_checksum()):
            tcpField.cksum = int(self.get_tcp_checksum())
            tcpField.is_override_cksum = True
        else:
            tcpField.is_override_cksum = False
        # flags = {int} 0
        if self.is_field_set(self.get_flags()):
            tcpField.flags = int(self.get_flags())
        # hdrlen_rsvd = {int} 80
        # is_override_hdrlen = {bool} False
        # seq_num = {int} 129018
        if self.is_field_set(self.get_sequence_number()):
            tcpField.seq_num = int(self.get_sequence_number())
        # src_port = {int} 49152
        # is_override_src_port = {bool} False
        if self.is_field_set(self.get_source_port()):
            tcpField.src_port = int(self.get_source_port())
            tcpField.is_override_src_port = True
        else:
            tcpField.is_override_src_port = False
        # dst_port = {int} 49153
        # is_override_dst_port = {bool} False
        if self.is_field_set(self.get_destination_port()):
            tcpField.dst_port = int(self.get_destination_port())
            tcpField.is_override_dst_port = True
        else:
            tcpField.is_override_dst_port = False
        # urg_ptr = {int} 0
        if self.is_field_set(self.get_urgent_porter()):
            tcpField.urg_ptr = int(self.get_urgent_porter())
        # window = {int} 1024
        if self.is_field_set(self.get_window()):
            tcpField.window = int(self.get_window())

    def config_jets_stream_tcp(self, jets_dev, port_string, stream_id, **kwargs):
        """
        TCP_HDR {
          src_port : 16 : legal_values = (RESERVED=0, TCPMUX=1, ECHO=7, DISCARD=9, SYSTAT=11, DAYTIME=13, NETSTAT=15,
                          CHARGEN=19, FTP_DATA=20, FTP=21, TELNET=23, SMTP=25, TIME=37, WHOIS=43, TACACS=49, DNS=53,
                          TFTP=69, RJE=77, FINGER=79, HTTP=80, LINK=87, SUPDUP=95, HOSTNAMES=101, ISO_TSAP=102,
                          X400=103, X400_SND=104, CSNET_NS=105, POP_2=109, POP=110, SUNRPC=111, UUCP_PATH=117, NNTP=119,
                          NTP=123, NEWS=144, BGP=179, EXEC=512, LOGIN=513, SHELL=514, PRINTER=515, COURIER=530,
                          UUCP=540, VTALK=562, PCSERVER=600, NEWPROD=608, LDP=646, PSADMIN=964, AUTOMAT=1025,
                          INGRESLOCK=1524, IWSERVER=1540, SYBASEQUERY=1550, SYBASECONSOLE=1551, LICENSE=1700,
                          TI_EDI_XLTD=1942, CAPSERV=2000, TSC_HDR=2002, TI_EDI_CGWD=2030, SSP_READ=2065, SSP_WRITE=2067,
                          CT=2120, LISTEN=2766, SAPDP00=3200, SAPDP01=3201, SAPDP02=3202, SAPGW00=3300, SAPGW01=3301,
                          SAPGW02=3302, SAPMSDEV=3600, SAPMSTST=3601, SAPMSPRD=3602, SAPINFDEV=3800, SAPINFTST=3801,
                          SAPINFPRD=3802, INFMKT=3803, FAX=4557, RWDAEMON=5556, X_WINDOW_HDR=6000-6063, ODB=7001,
                          OVTOPMD=8888, OVWDB=9999, NPT=1240, NETPERF=1286 ), display="Source Port", index=1;
          dst_port : 16 : legal_values = (RESERVED=0, TCPMUX=1, ECHO=7, DISCARD=9, SYSTAT=11, DAYTIME=13, NETSTAT=15,
                          CHARGEN=19, FTP_DATA=20, FTP=21, TELNET=23, SMTP=25, TIME=37, WHOIS=43, TACACS=49, DNS=53,
                          TFTP=69, RJE=77, FINGER=79, HTTP=80, LINK=87, SUPDUP=95, HOSTNAMES=101, ISO_TSAP=102,
                          X400=103, X400_SND=104, CSNET_NS=105, POP_2=109, POP=110, SUNRPC=111, UUCP_PATH=117, NNTP=119,
                          NTP=123, NEWS=144, BGP=179, EXEC=512, LOGIN=513, SHELL=514, PRINTER=515, COURIER=530,
                          UUCP=540, VTALK=562, PCSERVER=600, NEWPROD=608, LDP=646, PSADMIN=964, AUTOMAT=1025,
                          INGRESLOCK=1524, IWSERVER=1540, SYBASEQUERY=1550, SYBASECONSOLE=1551, LICENSE=1700,
                          TI_EDI_XLTD=1942, CAPSERV=2000, TSC_HDR=2002, TI_EDI_CGWD=2030, SSP_READ=2065, SSP_WRITE=2067,
                          CT=2120, LISTEN=2766, SAPDP00=3200, SAPDP01=3201, SAPDP02=3202, SAPGW00=3300, SAPGW01=3301,
                          SAPGW02=3302, SAPMSDEV=3600, SAPMSTST=3601, SAPMSPRD=3602, SAPINFDEV=3800, SAPINFTST=3801,
                          SAPINFPRD=3802, INFMKT=3803, FAX=4557, RWDAEMON=5556, X_WINDOW_HDR=6000-6063, ODB=7001,
                          OVTOPMD=8888, OVWDB=9999, NPT=1240, NETPERF=1286 ), display="Destination Port", index=2;
          seq      : 32 : display="Sequence Number", index=3;
          ack_seq  : 32 : display="Acknowledge Sequence", index=4;
          hlen     : 4  : display="Header Length %dec 32-bit words", send = length(node,node) / 4, index=5;
          rsvd     : 6  : display="Reserved", index=6;
          ctrl     : 6  : legal_values = (FIN = 1, SYN = 2, RESET = 4, PUSH = 8, ACK = 16, FINACK = 17, SYNACK = 18,
                          SYNACKFIN = 19,  ACKRESET = 20, PUSHACK = 24, PUSHACKFIN = 25, PUSHACKRESET = 28, URG = 32),
                          display="Control", index=7;
          window   : 16 : display="Window %dec bytes", index=8;
          xsum     : 16 : send = checksum(tcp, ip_offset, ip_offset), display="Checksum", index=9;
          urg_ptr  : 16 : display="Urgency Pointer", index=10;
          TCP_OPTION[] : (hlen - 5) * 32;
         };
        } display="TCP Header", index=5110;
        """
        if isinstance(self, IpV6PacketHeader):
            if not self.is_field_set(self.get_ipv6_next_header()):
                jets_dev.pdl_add_packet_header(JetsDeviceConstants.IPV6_HDR, {"next_header": 0x06})
                # if extention headers, find the last one and set that.
            if self.get_ipv6_extension_headers_length() > 1:
                self.get_ipv6_extension_headers()[-1].next_next_header = 0x06
        if self.header_in_bytes_only:
            pkt_bytes = "0x" + TcpPacketHeader.get_header_bytes(self)
            jets_dev.pdl_add_packet_header(JetsDeviceConstants.RAW_DATA, {"data": pkt_bytes})
        else:
            pkt_fields = {}
            if self.is_field_set(self.get_source_port()):
                pkt_fields["src_port"] = str(self.get_source_port())
            if self.is_field_set(self.get_destination_port()):
                pkt_fields["dst_port"] = str(self.get_destination_port())
            if self.is_field_set(self.get_sequence_number()):
                pkt_fields["seq"] = str(self.get_sequence_number())
            if self.is_field_set(self.get_acknowledgement_number()):
                pkt_fields["ack_seq"] = str(self.get_acknowledgement_number())
            # if self.is_field_set(self.get_()):
            #     pkt_fields["hlen"] = str(self.get_arp_hardware())
            if self.is_field_set(self.get_reserved()):
                pkt_fields["rsvd"] = str(self.get_reserved())
            # if self.is_field_set(self.get_arp_hardware()):
            #     pkt_fields["ctrl"] = str(self.get_arp_hardware())
            if self.is_field_set(self.get_window()):
                pkt_fields["window"] = str(self.get_window())
            if self.is_field_set(self.get_tcp_checksum()):
                pkt_fields["xsum"] = str(self.get_tcp_checksum())
            if self.is_field_set(self.get_urgent_porter()):
                pkt_fields["urg_ptr"] = str(self.get_urgent_porter())
            jets_dev.pdl_add_packet_header("TCP_HDR", pkt_fields)

            # if options, need to add an options header.
            #  if self.is_field_set(self.get_urgent_porter()):
            #      pkt_fields["urg_ptr"] = str(self.get_urgent_porter())

    def calculate_tcp_checksum(self, header_offset):
        self.set_tcp_checksum(0)
        header_sum = Checksum.calculate_tcp_checksum(self, self.get_bytes(), header_offset)
        header_sum = Checksum.calculate_complement(header_sum)
        self.set_tcp_checksum(header_sum)
        pass

    def parse_bytes(self):
        payload = self.get_payload()
        payload = payload.replace(" ", "")
        if len(payload) >= 40:
            source_port = self.get_bits_from_string(16, payload)
            self.set_source_port("0x" + source_port)
            payload = self.remove_bits_from_string(16, payload)
            destination_port = self.get_bits_from_string(16, payload)
            self.set_destination_port("0x" + destination_port)
            payload = self.remove_bits_from_string(16, payload)
            sequence_number = self.get_bits_from_string(32, payload)
            self.set_sequence_number("0x" + sequence_number)
            payload = self.remove_bits_from_string(32, payload)
            acknowledgement_number = self.get_bits_from_string(32, payload)
            self.set_acknowledgement_number("0x" + acknowledgement_number)
            payload = self.remove_bits_from_string(32, payload)
            data_offset = self.get_bits_from_string(4, payload)
            self.set_data_offset("0x" + data_offset)
            payload = self.remove_bits_from_string(4, payload)
            reserved = self.get_bits_from_string(8, payload)
            self.set_reserved("0x" + reserved)
            payload = self.remove_bits_from_string(8, payload)
            flags = self.get_bits_from_string(4, payload)
            self.set_flags("0x" + flags)
            payload = self.remove_bits_from_string(4, payload)
            window = self.get_bits_from_string(16, payload)
            self.set_window("0x" + window)
            payload = self.remove_bits_from_string(16, payload)
            checksum = self.get_bits_from_string(16, payload)
            self.set_tcp_checksum("0x" + checksum)
            payload = self.remove_bits_from_string(16, payload)
            urgent_porter = self.get_bits_from_string(16, payload)
            self.set_urgent_porter("0x" + urgent_porter)
            payload = self.remove_bits_from_string(16, payload)
            # Options = Length - 20
            header_length = int(data_offset, 16) * 4
            if header_length > 20:
                option = self.get_bits_from_string((header_length - 20) * 8, payload)
                payload = self.remove_bits_from_string((header_length - 20) * 8, payload)
                self.set_options(option)
        else:
            PacketObject.logger.log_info("No TCP header in payload: " + str(payload))
        self.payload = payload

    def get_header_bytes(self):
        ret_string = ""
        ret_string += self.format_byte_string(self.get_source_port(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_destination_port(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_sequence_number(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_acknowledgement_number(), PacketConstants.INTEGER, 32)
        ret_string += self.format_byte_string(self.get_data_offset(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_reserved(), PacketConstants.INTEGER, 8)
        ret_string += self.format_byte_string(self.get_flags(), PacketConstants.INTEGER, 4)
        ret_string += self.format_byte_string(self.get_window(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_tcp_checksum(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_urgent_porter(), PacketConstants.INTEGER, 16)
        ret_string += self.format_byte_string(self.get_options(), PacketConstants.HEX_STRING, 0)
        return ret_string

    @staticmethod
    def compare_tcp_packet_header(expected, actual, ignore_list=None, include_list=None, print_results=True,
                                  print_failures=True):
        results = True
        try:
            assert isinstance(expected, TcpPacketHeader)
            assert isinstance(actual, TcpPacketHeader)
            if expected.do_i_check_this_field(expected.get_source_port(), TcpPacketConstants.TCP_SOURCE_PORT,
                                              ignore_list, include_list):
                name = "TCP source port : "
                if expected.get_source_port() != actual.get_source_port():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_source_port()) + " != " +
                                                      str(actual.get_source_port()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_source_port()) + " == " +
                                                 str(actual.get_source_port()) + " Pass")

            if expected.do_i_check_this_field(expected.get_destination_port(), TcpPacketConstants.TCP_DESTINATION_PORT,
                                              ignore_list, include_list):
                name = "TCP destination port : "
                if expected.get_destination_port() != actual.get_destination_port():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_destination_port()) + " != " +
                                                      str(actual.get_destination_port()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_destination_port()) + " == " +
                                                 str(actual.get_destination_port()) + " Pass")

            if expected.do_i_check_this_field(expected.get_sequence_number(), TcpPacketConstants.TCP_SEQUENCE_NUMBER,
                                              ignore_list, include_list):
                name = "TCP sequence number : "
                if expected.get_sequence_number() != actual.get_sequence_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_sequence_number()) + " != " +
                                                      str(actual.get_sequence_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_sequence_number()) + " == " +
                                                 str(actual.get_sequence_number()) + " Pass")

            if expected.do_i_check_this_field(expected.get_acknowledgement_number(),
                                              TcpPacketConstants.TCP_ACKNOWLEDGEMENT_NUMBER, ignore_list, include_list):
                name = "TCP acknowledgement number : "
                if expected.get_acknowledgement_number() != actual.get_acknowledgement_number():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_acknowledgement_number()) + " != " +
                                                      str(actual.get_acknowledgement_number()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_acknowledgement_number()) + " == " +
                                                 str(actual.get_acknowledgement_number()) + " Pass")

            if expected.do_i_check_this_field(expected.get_data_offset(), TcpPacketConstants.TCP_DATA_OFFSET,
                                              ignore_list, include_list):
                name = "TCP data offset : "
                if expected.get_data_offset() != actual.get_data_offset():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_data_offset()) + " != " +
                                                      str(actual.get_data_offset()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_data_offset()) + " == " +
                                                 str(actual.get_data_offset()) + " Pass")

            if expected.do_i_check_this_field(expected.get_reserved(), TcpPacketConstants.TCP_RESERVED,
                                              ignore_list, include_list):
                name = "TCP reserved : "
                if expected.get_reserved() != actual.get_reserved():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_reserved()) + " != " +
                                                      str(actual.get_reserved()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_reserved()) + " == " +
                                                 str(actual.get_reserved()) + " Pass")

            if expected.do_i_check_this_field(expected.get_flags(), TcpPacketConstants.TCP_FLAGS,
                                              ignore_list, include_list):
                name = "TCP flags : "
                if expected.get_flags() != actual.get_flags():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_flags()) + " != " +
                                                      str(actual.get_flags()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_flags()) + " == " +
                                                 str(actual.get_flags()) + " Pass")

            if expected.do_i_check_this_field(expected.get_window(), TcpPacketConstants.TCP_WINDOW,
                                              ignore_list, include_list):
                name = "TCP window : "
                if expected.get_window() != actual.get_window():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_window()) + " != " +
                                                      str(actual.get_window()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_window()) + " == " +
                                                 str(actual.get_window()) + " Pass")

            if expected.do_i_check_this_field(expected.get_tcp_checksum(), TcpPacketConstants.TCP_CHECKSUM,
                                              ignore_list, include_list):
                name = "TCP checksum : "
                if expected.get_tcp_checksum() != actual.get_tcp_checksum():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_tcp_checksum()) + " != " +
                                                      str(actual.get_tcp_checksum()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_tcp_checksum()) + " == " +
                                                 str(actual.get_tcp_checksum()) + " Pass")

            if expected.do_i_check_this_field(expected.get_urgent_porter(), TcpPacketConstants.TCP_URGENT_PORTER,
                                              ignore_list, include_list):
                name = "TCP urgent porter : "
                if expected.get_urgent_porter() != actual.get_urgent_porter():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_urgent_porter()) + " != " +
                                                      str(actual.get_urgent_porter()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_urgent_porter()) + " == " +
                                                 str(actual.get_urgent_porter()) + " Pass")

            if expected.do_i_check_this_field(expected.get_options(), TcpPacketConstants.TCP_OPTIONS,
                                              ignore_list, include_list):
                name = "TCP options : "
                if expected.get_options() != actual.get_options():
                    results = False
                    if print_results or print_failures:
                        PacketObject.logger.log_error(name + str(expected.get_options()) + " != " +
                                                      str(actual.get_options()) + " ERROR")
                elif print_results:
                    PacketObject.logger.log_info(name + str(expected.get_options()) + " == " +
                                                 str(actual.get_options()) + " Pass")

        except Exception as e:
            results = False
            if print_results or print_failures:
                PacketObject.logger.log_info(e)
                PacketObject.logger.log_error("Error with TcpPacketHeader")
        return results


class TcpPacketConstants:
    def __init__(self):
        pass

    TCP_SOURCE_PORT = "TCP_SOURCE_PORT"
    TCP_DESTINATION_PORT = "TCP_DESTINATION_PORT"
    TCP_SEQUENCE_NUMBER = "TCP_SEQUENCE_NUMBER"
    TCP_ACKNOWLEDGEMENT_NUMBER = "TCP_ACKNOWLEDGEMENT_NUMBER"
    TCP_DATA_OFFSET = "TCP_DATA_OFFSET"
    TCP_RESERVED = "TCP_RESERVED"
    TCP_FLAGS = "TCP_FLAGS"
    TCP_WINDOW = "TCP_WINDOW"
    TCP_CHECKSUM = "TCP_CHECKSUM"
    TCP_URGENT_PORTER = "TCP_URGENT_PORTER"
    TCP_OPTIONS = "TCP_OPTIONS"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
