from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import IpV4PacketHeader
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import IpV6PacketHeader
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import IpxPacketHeader
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import SapPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import TcpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import BpduPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import SpanningTreePacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import LldpPacketHeader
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import MstpPacketHeader
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import VlanStackPacketHeader
from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDeviceConstants import IxiaDeviceConstants

from ExtremeAutomation.Library.Utils.Singleton import Singleton


class OstinatoStreamConfigApi(IxiaIxTclHalApi):
    """
    init function
    """

    def __init__(self, device):
        super(OstinatoStreamConfigApi, self).__init__(device)


class OstinatoStreamConfigConstants(object, metaclass=Singleton):
    DMA_MODE_CONTPACKET = "contPacket" # 0 (default) continuously transmit the frames on this stream
    DMA_MODE_CONTBURST = "contBurst" # 1 continuously transmit bursts of frames on this stream
    DMA_MODE_STOPSTREAM = "stopStream" # 2 stop all transmission from the port where this stream resides regardless of existence of other streams on this port
    DMA_MODE_ADVANCE = "advance" # 3 after all the frames are sent from the current stream, the frames from the next stream on the port are transmitted.
    DMA_MODE_GOTOFIRST = "gotoFirst" # 4 the last stream on the port is set to this mode to begin transmission of frames of the first stream in the list
    DMA_MODE_FIRSTLOOPCOUNT = "firstLoopCount" # 5 the last stream on the port is set to this mode to begin transmission of the first stream in the list for loopCount intervals

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
