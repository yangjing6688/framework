from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import IcmpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import RadiusPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import ArpPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import Ethernet2PacketHeader
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import TaggedPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Device.TrafficGeneration.Spirent.Apis.SpirentTclApi import SpirentTclApi


class SpirentStreamConfigTclApi(SpirentTclApi):
    def __init__(self, device):
        super(SpirentStreamConfigTclApi, self).__init__(device)

    def configure_fixed_length(self, port_name_stream, packet):
        assert isinstance(packet, EthernetPacket)
        commands = packet.get_spirent_packet_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_ethernet2_traffic(self, port_name_stream, packet):
        assert isinstance(packet, Ethernet2PacketHeader)
        commands = packet.get_spirent_etherii_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_sap_traffic(self, port_name_stream, packet):
        assert isinstance(packet, SapPacketHeader)
        commands = packet.get_spirent_sap_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_ipx_traffic(self, port_name_stream, packet):
        assert isinstance(packet, IpxPacketHeader)
        commands = packet.get_spirent_ipx_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_vlan_stack_traffic(self, port_name_stream, packet):
        assert isinstance(packet, VlanStackPacketHeader)
        commands = packet.get_spirent_vlan_stack_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_tagged_traffic(self, port_name_stream, packet):
        assert isinstance(packet, TaggedPacketHeader)
        commands = packet.get_spirent_tagged_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_ipv4_traffic(self, port_name_stream, packet):
        assert isinstance(packet, IpV4PacketHeader)
        commands = packet.get_spirent_ipv4_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_arp_traffic(self, port_name_stream, packet):
        assert isinstance(packet, ArpPacketHeader)
        commands = packet.get_spirent_arp_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_icmp_traffic(self, port_name_stream, packet):
        assert isinstance(packet, IcmpPacketHeader)
        commands = packet.get_spirent_icmp_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_ipv6_traffic(self, port_name_stream, packet):
        assert isinstance(packet, IpV6PacketHeader)
        commands = packet.get_spirent_ipv6_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_tcp_traffic(self, port_name_stream, packet):
        assert isinstance(packet, TcpPacketHeader)
        commands = packet.get_spirent_tcp_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_bpdu_traffic(self, port_name_stream, packet):
        assert isinstance(packet, BpduPacketHeader)
        commands = packet.get_spirent_bpdu_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_lldp_traffic(self, port_name_stream, packet):
        assert isinstance(packet, LldpPacketHeader)
        commands = packet.get_spirent_lldp_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_radius_traffic(self, port_name_stream, packet):
        assert isinstance(packet, RadiusPacketHeader)
        commands = packet.get_spirent_radius_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_mstp_traffic(self, port_name_stream, packet):
        assert isinstance(packet, MstpPacketHeader)
        commands = packet.get_spirent_mstp_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_spanningtree_traffic(self, port_name_stream, packet):
        assert isinstance(packet, SpanningTreePacketHeader)
        commands = packet.get_spirent_spanningtree_api_commands(port_name_stream)
        return self.send_commands(commands)

    def configure_stream_fcs_dribble(self, port_name_stream, stream_id, options={}):
        self.__modify_ixia_stream(port_name_stream, stream_id, IxiaDeviceConstants.FCS_DRIBBLE_ERROR)

    def configure_stream_fcs_alignment(self, port_name_stream, stream_id, options={}):
        self.__modify_ixia_stream(port_name_stream, stream_id, IxiaDeviceConstants.FCS_ALIGN_ERROR)

    def configure_stream_fcs_jabber(self, port_name_stream, stream_id, options={}):
        return self.logger.log_unimplemented_method()

    def configure_stream_fcs_none(self, port_name_stream, stream_id, options={}):
        self.__modify_ixia_stream(port_name_stream, stream_id, IxiaDeviceConstants.FCS_NONE)

    def __modify_ixia_stream(self, port_name_stream, stream_id, fcs):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # commands = []
        # commands.append("stream get " + port_name_stream + " " + str(stream_id))
        # commands.append("stream config -fcs " + str(fcs))
        # commands.append("stream set " + port_name_stream + " " + str(stream_id))
        # commands.append("stream write " + port_name_stream + " " + str(stream_id))
        # commands.append("set portList [ list [ list " + port_name_stream + "]]")
        # commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        # self.send_commands(commands)

    def set_dma_mode(self, port_name_stream, stream_id, dma_mode):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # commands = []
        # commands.append("port get " + str(port_name_stream))
        # commands.append("stream get " + port_name_stream + " " + str(stream_id))
        # commands.append("stream config -dma " + str(dma_mode))
        # commands.append("stream set " + port_name_stream + " " + str(stream_id))
        # commands.append("stream write " + port_name_stream + " " + str(stream_id))
        # commands.append("port set " + str(port_name_stream))
        # commands.append("port write " + str(port_name_stream))
        # commands.append("set portList [ list [ list " + port_name_stream + "]]")
        # commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        # self.send_commands(commands)

    def get_dma_mode(self, port_name_stream, stream_id):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # self.send_command("port get " + str(port_name_stream))
        # self.send_command("stream get " + port_name_stream + " " + str(stream_id))
        # return self.strip_return(self.send_command("stream cget -dma "))

    def disable_time_stamp(self, port_name_stream, stream_id):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # commands = []
        # commands.append("port get " + str(port_name_stream))
        # commands.append("stream get " + port_name_stream + " " + str(stream_id))
        # commands.append("stream config -enableTimestamp 0")
        # commands.append("stream set " + port_name_stream + " " + str(stream_id))
        # commands.append("stream write " + port_name_stream + " " + str(stream_id))
        # commands.append("port set " + str(port_name_stream))
        # commands.append("port write " + str(port_name_stream))
        # commands.append("set portList [ list [ list " + port_name_stream + "]]")
        # commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        # self.send_commands(commands)

    # def disable_time_stamp(self, port_name_stream, stream_id):
    #     port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
    #     commands = []
    #     commands.append("port get " + str(port_name_stream))
    #     commands.append("stream get " + port_name_stream + " " + str(stream_id))
    #     commands.append("stream config -enableTimestamp 0")
    #     commands.append("stream set " + port_name_stream + " " + str(stream_id))
    #     commands.append("stream write " + port_name_stream + " " + str(stream_id))
    #     commands.append("port set " + str(port_name_stream))
    #     commands.append("port write " + str(port_name_stream))
    #     commands.append("set portList [ list [ list " + port_name_stream + "]]")
    #     commands.append("ixWriteConfigToHardware portList -noProtocolServer")
    #     self.send_commands(commands)

    def configure_stream_arp_source_protocol_options(self, port_name_stream, streamid, addr, mode, count):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # dummy_dict = []
        # dummy_dict.append("stream get " + port_name_stream + " " + str(streamid))
        # # ### put some IxTclHal info here.
        # dummy_dict.append("arp get " + port_name_stream)
        # if addr:
        #     dummy_dict.append("arp config -sourceProtocolAddr                 \"" + str(addr) + "\"")
        # if mode:
        #     dummy_dict.append("arp config -sourceProtocolAddrMode                   \"" +
        #                       str(ArpPacketHeader.translateArpValue(mode)) + "\"")
        # if count:
        #     dummy_dict.append("arp config -sourceProtocolAddrRepeatCount                   \"" + str(count) + "\"")
        # dummy_dict.append("arp set " + port_name_stream)
        # dummy_dict.append("stream set " + port_name_stream + " " + str(streamid))
        # dummy_dict.append("stream write " + port_name_stream + " " + str(streamid))
        # dummy_dict.append("set portList [ list [ list " + port_name_stream + "]]")
        # dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        # self.send_commands(dummy_dict)

    def configure_stream_arp_target_protocol_options(self, port_name_stream, streamid, addr, mode, count):
        port_name_stream = TrafficGenerationUtils.convert_port_name_stream_to_ixtclhal_port(port_name_stream)
        # dummy_dict = []
        # dummy_dict.append("stream get " + port_name_stream + " " + str(streamid))
        # # ### put some IxTclHal info here.
        # #dummy_dict.append("arp setDefault")
        # dummy_dict.append("arp get " + port_name_stream)
        # if addr:
        #     dummy_dict.append("arp config -destProtocolAddr                 \"" + str(addr) + "\"")
        # if mode:
        #     dummy_dict.append("arp config -destProtocolAddrMode                   \"" +
        #                       str(ArpPacketHeader.translateArpValue(mode)) + "\"")
        # if count:
        #     dummy_dict.append("arp config -destProtocolAddrRepeatCount                   \"" + str(count) + "\"")
        # dummy_dict.append("arp set " + port_name_stream)
        # dummy_dict.append("stream set " + port_name_stream + " " + str(streamid))
        # dummy_dict.append("stream write " + port_name_stream + " " + str(streamid))
        # dummy_dict.append("set portList [ list [ list " + port_name_stream + "]]")
        # dummy_dict.append("ixWriteConfigToHardware portList -noProtocolServer")
        # self.send_commands(dummy_dict)


class SpirentStreamConfigTclConstants(object, metaclass=Singleton):
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
