from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanPacketHeader import ErspanPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanIIIPacketHeader import ErspanIIIPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class IxiaStreamConfigIxTclHalApi(IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxiaStreamConfigIxTclHalApi, self).__init__(device)

    def configure_sap_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, SapPacketHeader)
        commands = packet.get_ixtclhal_sap_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_ipx_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, IpxPacketHeader)
        commands = packet.get_ixtclhal_ipx_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_vlan_stack_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, VlanStackPacketHeader)
        commands = packet.get_ixtclhal_vlanstack_api_commands(port_string, streamid)

        self.send_commands(commands)

    def configure_ipv4_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, IpV4PacketHeader)
        commands = packet.get_ixtclhal_ipv4_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_arp_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, ArpPacketHeader)
        commands = packet.get_ixtclhal_arp_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_icmp_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, IcmpPacketHeader)
        commands = packet.get_ixtclhal_icmp_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_ipv6_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, IpV6PacketHeader)
        commands = packet.get_ixtclhal_ipv6_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_tcp_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, TcpPacketHeader)
        commands = packet.get_ixtclhal_tcp_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_bpdu_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, BpduPacketHeader)
        commands = packet.get_ixtclhal_bpdu_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_lldp_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, LldpPacketHeader)
        commands = packet.get_ixtclhal_lldp_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_radius_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, RadiusPacketHeader)
        commands = packet.get_ixtclhal_radius_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_gre_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, GrePacketHeader)
        commands = packet.get_ixtclhal_gre_api_commands(port_string, streamid)
        self.send_commands(commands)
        if isinstance(packet, ErspanIIIPacketHeader):
            commands = packet.get_ixtclhal_erspaniii_api_commands(port_string, streamid)
        elif isinstance(packet, ErspanPacketHeader):
            commands = packet.get_ixtclhal_erspan_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_vxlan_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, VxlanPacketHeader)
        commands = packet.get_ixtclhal_vxlan_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_ipencap_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, IpEncapsulatedPacketHeader)
        commands = packet.get_ixtclhal_encapsulated_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_mstp_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, MstpPacketHeader)
        commands = packet.get_ixtclhal_mstp_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_spanningtree_traffic(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, SpanningTreePacketHeader)
        commands = packet.get_ixtclhal_spanningtree_api_commands(port_string, streamid)
        self.send_commands(commands)

    def configure_stream_fcs_dribble(self, port_string, stream_id, options=None):
        self.__modify_ixia_stream(port_string, stream_id, IxiaDeviceConstants.FCS_DRIBBLE_ERROR)

    def configure_stream_fcs_alignment(self, port_string, stream_id, options=None):
        self.__modify_ixia_stream(port_string, stream_id, IxiaDeviceConstants.FCS_ALIGN_ERROR)

    def configure_stream_fcs_jabber(self, port_string, stream_id, options=None):
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_none(self, port_string, stream_id, options=None):
        self.__modify_ixia_stream(port_string, stream_id, IxiaDeviceConstants.FCS_NONE)

    def configure_payload(self, port_string, streamid, packet):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        # assert isinstance(packet, EthernetPacket)
        commands = packet.get_ixtclhal_payload_api_commands(port_string, streamid)
        self.send_commands(commands)

    def __modify_ixia_stream(self, port_string, stream_id, fcs):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("stream get " + port_string + " " + str(stream_id))
        commands.append("stream config -fcs " + str(fcs))
        commands.append("stream set " + port_string + " " + str(stream_id))
        commands.append("stream write " + port_string + " " + str(stream_id))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

    def set_dma_mode(self, port_string, stream_id, dma_mode):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        commands.append("stream get " + port_string + " " + str(stream_id))
        commands.append("stream config -dma " + str(dma_mode))
        commands.append("stream set " + port_string + " " + str(stream_id))
        commands.append("stream write " + port_string + " " + str(stream_id))
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

    def get_dma_mode(self, port_string, stream_id):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        self.send_command("port get " + str(port_string))
        self.send_command("stream get " + port_string + " " + str(stream_id))
        return self.strip_return(self.send_command("stream cget -dma "))

    def disable_time_stamp(self, port_string, stream_id):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        commands.append("stream get " + port_string + " " + str(stream_id))
        commands.append("stream config -enableTimestamp 0")
        commands.append("stream set " + port_string + " " + str(stream_id))
        commands.append("stream write " + port_string + " " + str(stream_id))
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

    def configure_stream_arp_source_protocol_options(self, port_string, streamid, addr, mode, count):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = list()
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        dummy_dict.append("arp get " + port_string)
        if addr:
            dummy_dict.append("arp config -sourceProtocolAddr                 \"" + str(addr) + "\"")
        if mode:
            dummy_dict.append("arp config -sourceProtocolAddrMode                   \"" +
                              str(ArpPacketHeader.translateArpValue(mode)) + "\"")
        if count:
            dummy_dict.append("arp config -sourceProtocolAddrRepeatCount                   \"" + str(count) + "\"")
        dummy_dict.append("arp set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(dummy_dict)

    def configure_stream_arp_target_protocol_options(self, port_string, streamid, addr, mode, count):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        dummy_dict = list()
        dummy_dict.append("stream get " + port_string + " " + str(streamid))
        # ### put some IxTclHal info here.
        # dummy_dict.append("arp setDefault")
        dummy_dict.append("arp get " + port_string)
        if addr:
            dummy_dict.append("arp config -destProtocolAddr                 \"" + str(addr) + "\"")
        if mode:
            dummy_dict.append("arp config -destProtocolAddrMode                   \"" +
                              str(ArpPacketHeader.translateArpValue(mode)) + "\"")
        if count:
            dummy_dict.append("arp config -destProtocolAddrRepeatCount                   \"" + str(count) + "\"")
        dummy_dict.append("arp set " + port_string)
        dummy_dict.append("stream set " + port_string + " " + str(streamid))
        dummy_dict.append("stream write " + port_string + " " + str(streamid))
        dummy_dict.append("set portList [ list [ list " + port_string + "]]")
        dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(dummy_dict)


class IxiaStreamConfigIxTclHalConstants(object, metaclass=Singleton):
    DMA_MODE_CONTPACKET = "contPacket"  # 0 (default) continuously transmit the frames on this stream
    DMA_MODE_CONTBURST = "contBurst"  # 1 continuously transmit bursts of frames on this stream
    DMA_MODE_STOPSTREAM = "stopStream"  # 2 stop all transmission from the port where this stream resides regardless of
    #                                   # existence of other streams on this port
    DMA_MODE_ADVANCE = "advance"  # 3 after all the frames are sent from the current stream, the frames from the next
    #                             # stream on the port are transmitted.
    DMA_MODE_GOTOFIRST = "gotoFirst"  # 4 the last stream on the port is set to this mode to begin transmission of
    #                                 # frames of the first stream in the list
    DMA_MODE_FIRSTLOOPCOUNT = "firstLoopCount"  # 5 the last stream on the port is set to this mode to begin
    #                                           # transmission of the first stream in the list for loopCount intervals

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
