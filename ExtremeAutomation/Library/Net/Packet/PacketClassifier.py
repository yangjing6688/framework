import copy
from collections import deque
########################################################################################################################
# ### Start Packets Auto-generated ####
########################################################################################################################
# ### Start Packets Auto-generated ####
from ExtremeAutomation.Library.Net.Packet.AbstractPacket import AbstractPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2ArpPacket import Ethernet2ArpPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2ArpTaggedPacket import Ethernet2ArpTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2ArpVlanStackPacket import Ethernet2ArpVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2MplsPacket import Ethernet2MplsPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2MplsTaggedPacket import Ethernet2MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2MplsVlanStackPacket import Ethernet2MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2Packet import Ethernet2Packet
from ExtremeAutomation.Library.Net.Packet.Ethernet2TaggedPacket import Ethernet2TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ethernet2VlanStackPacket import Ethernet2VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.EthernetPacket import EthernetPacket
from ExtremeAutomation.Library.Net.Packet.EthernetTaggedPacket import EthernetTaggedPacket
from ExtremeAutomation.Library.Net.Packet.EthernetVlanStackPacket import EthernetVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacket import Ieee802LlcPacket
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcTaggedPacket import Ieee802LlcTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcVlanStackPacket import Ieee802LlcVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.SapPacket import SapPacket
from ExtremeAutomation.Library.Net.Packet.SapTaggedPacket import SapTaggedPacket
from ExtremeAutomation.Library.Net.Packet.SapVlanStackPacket import SapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2MplsEncapsulatedPacket import \
    Ethernet2MplsEncapsulatedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2MplsEncapsulatedTaggedPacket import \
    Ethernet2MplsEncapsulatedTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2MplsEncapsulatedVlanStackPacket import \
    Ethernet2MplsEncapsulatedVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2ProviderBackboneBridgePacket import \
    Ethernet2ProviderBackboneBridgePacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2ProviderBackboneBridgeTaggedPacket import \
    Ethernet2ProviderBackboneBridgeTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.Ethernet2ProviderBackboneBridgeVlanStackPacket import \
    Ethernet2ProviderBackboneBridgeVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanGreIpV4Packet import \
    Ethernet2ErspanGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanGreIpV4TaggedPacket import \
    Ethernet2ErspanGreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanGreIpV4VlanStackPacket import \
    Ethernet2ErspanGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanIIIGreIpV4Packet import \
    Ethernet2ErspanIIIGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanIIIGreIpV4TaggedPacket import \
    Ethernet2ErspanIIIGreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2ErspanIIIGreIpV4VlanStackPacket import \
    Ethernet2ErspanIIIGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2GreIpV4Packet import Ethernet2GreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2GreIpV4TaggedPacket import \
    Ethernet2GreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2GreIpV4VlanStackPacket import \
    Ethernet2GreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2IpEncapsulatedIpV4Packet import \
    Ethernet2IpEncapsulatedIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2IpEncapsulatedIpV4TaggedPacket import \
    Ethernet2IpEncapsulatedIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2IpEncapsulatedIpV4VlanStackPacket import \
    Ethernet2IpEncapsulatedIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2VxlanUdpIpV4Packet import \
    Ethernet2VxlanUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2VxlanUdpIpV4TaggedPacket import \
    Ethernet2VxlanUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.Ethernet2VxlanUdpIpV4VlanStackPacket import \
    Ethernet2VxlanUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanGreIpV4Packet import \
    EthernetSnapErspanGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanGreIpV4TaggedPacket import \
    EthernetSnapErspanGreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanGreIpV4VlanStackPacket import \
    EthernetSnapErspanGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanIIIGreIpV4Packet import \
    EthernetSnapErspanIIIGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanIIIGreIpV4TaggedPacket import \
    EthernetSnapErspanIIIGreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapErspanIIIGreIpV4VlanStackPacket import \
    EthernetSnapErspanIIIGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapGreIpV4Packet import EthernetSnapGreIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapGreIpV4TaggedPacket import \
    EthernetSnapGreIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapGreIpV4VlanStackPacket import \
    EthernetSnapGreIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapIpEncapsulatedIpV4Packet import \
    EthernetSnapIpEncapsulatedIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapIpEncapsulatedIpV4TaggedPacket import \
    EthernetSnapIpEncapsulatedIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV4.EthernetSnapIpEncapsulatedIpV4VlanStackPacket import \
    EthernetSnapIpEncapsulatedIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanGreIpV6Packet import \
    Ethernet2ErspanGreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanGreIpV6TaggedPacket import \
    Ethernet2ErspanGreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanGreIpV6VlanStackPacket import \
    Ethernet2ErspanGreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanIIIGreIpV6Packet import \
    Ethernet2ErspanIIIGreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanIIIGreIpV6TaggedPacket import \
    Ethernet2ErspanIIIGreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2ErspanIIIGreIpV6VlanStackPacket import \
    Ethernet2ErspanIIIGreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2GreIpV6Packet import Ethernet2GreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2GreIpV6TaggedPacket import \
    Ethernet2GreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2GreIpV6VlanStackPacket import \
    Ethernet2GreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2IpEncapsulatedIpV6Packet import \
    Ethernet2IpEncapsulatedIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2IpEncapsulatedIpV6TaggedPacket import \
    Ethernet2IpEncapsulatedIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2IpEncapsulatedIpV6VlanStackPacket import \
    Ethernet2IpEncapsulatedIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2VxlanUdpIpV6Packet import \
    Ethernet2VxlanUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2VxlanUdpIpV6TaggedPacket import \
    Ethernet2VxlanUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.Ethernet2VxlanUdpIpV6VlanStackPacket import \
    Ethernet2VxlanUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanGreIpV6Packet import \
    EthernetSnapErspanGreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanGreIpV6TaggedPacket import \
    EthernetSnapErspanGreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanGreIpV6VlanStackPacket import \
    EthernetSnapErspanGreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanIIIGreIpV6Packet import \
    EthernetSnapErspanIIIGreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanIIIGreIpV6TaggedPacket import \
    EthernetSnapErspanIIIGreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapErspanIIIGreIpV6VlanStackPacket import \
    EthernetSnapErspanIIIGreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapGreIpV6Packet import EthernetSnapGreIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapGreIpV6TaggedPacket import \
    EthernetSnapGreIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapGreIpV6VlanStackPacket import \
    EthernetSnapGreIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapIpEncapsulatedIpV6Packet import \
    EthernetSnapIpEncapsulatedIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapIpEncapsulatedIpV6TaggedPacket import \
    EthernetSnapIpEncapsulatedIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Encapsulated.IpV6.EthernetSnapIpEncapsulatedIpV6VlanStackPacket import \
    EthernetSnapIpEncapsulatedIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2BootpUdpIpV4Packet import Ethernet2BootpUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2BootpUdpIpV4TaggedPacket import \
    Ethernet2BootpUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2BootpUdpIpV4VlanStackPacket import \
    Ethernet2BootpUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DBDescriptionOspfIpV4Packet import \
    Ethernet2DBDescriptionOspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DBDescriptionOspfIpV4TaggedPacket import \
    Ethernet2DBDescriptionOspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DBDescriptionOspfIpV4VlanStackPacket import \
    Ethernet2DBDescriptionOspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsTcpIpV4Packet import Ethernet2DnsTcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsTcpIpV4TaggedPacket import Ethernet2DnsTcpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsTcpIpV4VlanStackPacket import \
    Ethernet2DnsTcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsUdpIpV4Packet import Ethernet2DnsUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsUdpIpV4TaggedPacket import Ethernet2DnsUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2DnsUdpIpV4VlanStackPacket import \
    Ethernet2DnsUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2HelloOspfIpV4Packet import Ethernet2HelloOspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2HelloOspfIpV4TaggedPacket import \
    Ethernet2HelloOspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2HelloOspfIpV4VlanStackPacket import \
    Ethernet2HelloOspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4MplsPacket import Ethernet2IcmpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4MplsTaggedPacket import \
    Ethernet2IcmpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4MplsVlanStackPacket import \
    Ethernet2IcmpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4Packet import Ethernet2IcmpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4TaggedPacket import Ethernet2IcmpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IcmpIpV4VlanStackPacket import Ethernet2IcmpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4MplsPacket import Ethernet2IgmpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4MplsTaggedPacket import \
    Ethernet2IgmpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4MplsVlanStackPacket import \
    Ethernet2IgmpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4Packet import Ethernet2IgmpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4TaggedPacket import Ethernet2IgmpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IgmpIpV4VlanStackPacket import Ethernet2IgmpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4MplsPacket import Ethernet2IpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4MplsTaggedPacket import Ethernet2IpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4MplsVlanStackPacket import Ethernet2IpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4Packet import Ethernet2IpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4TaggedPacket import Ethernet2IpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2IpV4VlanStackPacket import Ethernet2IpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateAcknowledgeOspfIpV4Packet import \
    Ethernet2LinkStateAcknowledgeOspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateAcknowledgeOspfIpV4TaggedPacket import \
    Ethernet2LinkStateAcknowledgeOspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateAcknowledgeOspfIpV4VlanStackPacket import \
    Ethernet2LinkStateAcknowledgeOspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateRequestOspfIpV4Packet import \
    Ethernet2LinkStateRequestOspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateRequestOspfIpV4TaggedPacket import \
    Ethernet2LinkStateRequestOspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateRequestOspfIpV4VlanStackPacket import \
    Ethernet2LinkStateRequestOspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateUpdateOspfIpV4Packet import \
    Ethernet2LinkStateUpdateOspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateUpdateOspfIpV4TaggedPacket import \
    Ethernet2LinkStateUpdateOspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2LinkStateUpdateOspfIpV4VlanStackPacket import \
    Ethernet2LinkStateUpdateOspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4Packet import Ethernet2OspfIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4TaggedPacket import Ethernet2OspfIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2OspfIpV4VlanStackPacket import Ethernet2OspfIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2PimIpV4Packet import Ethernet2PimIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2PimIpV4TaggedPacket import Ethernet2PimIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2PimIpV4VlanStackPacket import Ethernet2PimIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RadiusUdpIpV4Packet import Ethernet2RadiusUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RadiusUdpIpV4TaggedPacket import \
    Ethernet2RadiusUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RadiusUdpIpV4VlanStackPacket import \
    Ethernet2RadiusUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4MplsPacket import Ethernet2RipUdpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4MplsTaggedPacket import \
    Ethernet2RipUdpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4MplsVlanStackPacket import \
    Ethernet2RipUdpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4Packet import Ethernet2RipUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4TaggedPacket import Ethernet2RipUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2RipUdpIpV4VlanStackPacket import \
    Ethernet2RipUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2SyslogUdpIpV4Packet import Ethernet2SyslogUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2SyslogUdpIpV4TaggedPacket import \
    Ethernet2SyslogUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2SyslogUdpIpV4VlanStackPacket import \
    Ethernet2SyslogUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4MplsPacket import Ethernet2TcpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4MplsTaggedPacket import Ethernet2TcpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4MplsVlanStackPacket import \
    Ethernet2TcpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4Packet import Ethernet2TcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4TaggedPacket import Ethernet2TcpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2TcpIpV4VlanStackPacket import Ethernet2TcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4MplsPacket import Ethernet2UdpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4MplsTaggedPacket import Ethernet2UdpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4MplsVlanStackPacket import \
    Ethernet2UdpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4Packet import Ethernet2UdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4TaggedPacket import Ethernet2UdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2UdpIpV4VlanStackPacket import Ethernet2UdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4MplsPacket import Ethernet2VrrpIpV4MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4MplsTaggedPacket import \
    Ethernet2VrrpIpV4MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4MplsVlanStackPacket import \
    Ethernet2VrrpIpV4MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4Packet import Ethernet2VrrpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4TaggedPacket import Ethernet2VrrpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Ethernet2VrrpIpV4VlanStackPacket import Ethernet2VrrpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Bgp.Ethernet2BgpTcpIpV4Packet import Ethernet2BgpTcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.IpV4.Bgp.Ethernet2BgpTcpIpV4TaggedPacket import \
    Ethernet2BgpTcpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV4.Bgp.Ethernet2BgpTcpIpV4VlanStackPacket import \
    Ethernet2BgpTcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsTcpIpV6Packet import Ethernet2DnsTcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsTcpIpV6TaggedPacket import Ethernet2DnsTcpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsTcpIpV6VlanStackPacket import \
    Ethernet2DnsTcpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsUdpIpV6Packet import Ethernet2DnsUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsUdpIpV6TaggedPacket import Ethernet2DnsUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2DnsUdpIpV6VlanStackPacket import \
    Ethernet2DnsUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6MplsPacket import Ethernet2IcmpV6IpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6MplsTaggedPacket import \
    Ethernet2IcmpV6IpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6MplsVlanStackPacket import \
    Ethernet2IcmpV6IpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6Packet import Ethernet2IcmpV6IpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6TaggedPacket import Ethernet2IcmpV6IpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IcmpV6IpV6VlanStackPacket import \
    Ethernet2IcmpV6IpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6MplsPacket import Ethernet2IpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6MplsTaggedPacket import Ethernet2IpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6MplsVlanStackPacket import Ethernet2IpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6Packet import Ethernet2IpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6TaggedPacket import Ethernet2IpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2IpV6VlanStackPacket import Ethernet2IpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2PimIpV6Packet import Ethernet2PimIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2PimIpV6TaggedPacket import Ethernet2PimIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2PimIpV6VlanStackPacket import Ethernet2PimIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RadiusUdpIpV6Packet import Ethernet2RadiusUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RadiusUdpIpV6TaggedPacket import \
    Ethernet2RadiusUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RadiusUdpIpV6VlanStackPacket import \
    Ethernet2RadiusUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6MplsPacket import Ethernet2RipNgUdpIpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6MplsTaggedPacket import \
    Ethernet2RipNgUdpIpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6MplsVlanStackPacket import \
    Ethernet2RipNgUdpIpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6Packet import Ethernet2RipNgUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6TaggedPacket import \
    Ethernet2RipNgUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2RipNgUdpIpV6VlanStackPacket import \
    Ethernet2RipNgUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2SyslogUdpIpV6Packet import Ethernet2SyslogUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2SyslogUdpIpV6TaggedPacket import \
    Ethernet2SyslogUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2SyslogUdpIpV6VlanStackPacket import \
    Ethernet2SyslogUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6MplsPacket import Ethernet2TcpIpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6MplsTaggedPacket import Ethernet2TcpIpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6MplsVlanStackPacket import \
    Ethernet2TcpIpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6Packet import Ethernet2TcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6TaggedPacket import Ethernet2TcpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2TcpIpV6VlanStackPacket import Ethernet2TcpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6MplsPacket import Ethernet2UdpIpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6MplsTaggedPacket import Ethernet2UdpIpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6MplsVlanStackPacket import \
    Ethernet2UdpIpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6Packet import Ethernet2UdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6TaggedPacket import Ethernet2UdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2UdpIpV6VlanStackPacket import Ethernet2UdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6MplsPacket import Ethernet2VrrpIpV6MplsPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6MplsTaggedPacket import \
    Ethernet2VrrpIpV6MplsTaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6MplsVlanStackPacket import \
    Ethernet2VrrpIpV6MplsVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6Packet import Ethernet2VrrpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6TaggedPacket import Ethernet2VrrpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Ethernet2VrrpIpV6VlanStackPacket import Ethernet2VrrpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Bgp.Ethernet2BgpTcpIpV6Packet import Ethernet2BgpTcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.IpV6.Bgp.Ethernet2BgpTcpIpV6TaggedPacket import \
    Ethernet2BgpTcpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.IpV6.Bgp.Ethernet2BgpTcpIpV6VlanStackPacket import \
    Ethernet2BgpTcpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Ipx.Ieee802_2IpxPacket import Ieee802_2IpxPacket
from ExtremeAutomation.Library.Net.Packet.Ipx.Ieee802_2IpxTaggedPacket import Ieee802_2IpxTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Ipx.Ieee802_2IpxVlanStackPacket import Ieee802_2IpxVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2CsnpDbsyncDvrPacket import Ethernet2CsnpDbsyncDvrPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2CsnpDbsyncDvrTaggedPacket import \
    Ethernet2CsnpDbsyncDvrTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2CsnpDbsyncDvrVlanStackPacket import \
    Ethernet2CsnpDbsyncDvrVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbpDbsyncDvrPacket import Ethernet2DbpDbsyncDvrPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbpDbsyncDvrTaggedPacket import \
    Ethernet2DbpDbsyncDvrTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbpDbsyncDvrVlanStackPacket import \
    Ethernet2DbpDbsyncDvrVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrPacket import Ethernet2DbsyncDvrPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrTaggedPacket import Ethernet2DbsyncDvrTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2DbsyncDvrVlanStackPacket import \
    Ethernet2DbsyncDvrVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2LldpPacket import Ethernet2LldpPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2LldpTaggedPacket import Ethernet2LldpTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Other.Ethernet2LldpVlanStackPacket import Ethernet2LldpVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduPacket import SapBpduPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduTaggedPacket import SapBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapBpduVlanStackPacket import SapBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapMstpSpanningTreeBpduPacket import SapMstpSpanningTreeBpduPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapMstpSpanningTreeBpduTaggedPacket import \
    SapMstpSpanningTreeBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapMstpSpanningTreeBpduVlanStackPacket import \
    SapMstpSpanningTreeBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapRstpBpduPacket import SapRstpBpduPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapRstpBpduTaggedPacket import SapRstpBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapRstpBpduVlanStackPacket import SapRstpBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapSpanningTreeBpduPacket import SapSpanningTreeBpduPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapSpanningTreeBpduTaggedPacket import SapSpanningTreeBpduTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.SapSpanningTreeBpduVlanStackPacket import \
    SapSpanningTreeBpduVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapCSNPIsisPacket import SapCSNPIsisPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapCSNPIsisTaggedPacket import SapCSNPIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapCSNPIsisVlanStackPacket import SapCSNPIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapHelloPduIsisPacket import SapHelloPduIsisPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapHelloPduIsisTaggedPacket import SapHelloPduIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapHelloPduIsisVlanStackPacket import SapHelloPduIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisPacket import SapIsisPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisTaggedPacket import SapIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapIsisVlanStackPacket import SapIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapLSPIsisPacket import SapLSPIsisPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapLSPIsisTaggedPacket import SapLSPIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapLSPIsisVlanStackPacket import SapLSPIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapPSNPIsisPacket import SapPSNPIsisPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapPSNPIsisTaggedPacket import SapPSNPIsisTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Sap.Isis.SapPSNPIsisVlanStackPacket import SapPSNPIsisVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapPacket import EthernetSnapPacket
from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapTaggedPacket import EthernetSnapTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.EthernetSnapVlanStackPacket import EthernetSnapVlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapIpV4Packet import EthernetSnapIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapIpV4TaggedPacket import EthernetSnapIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapIpV4VlanStackPacket import \
    EthernetSnapIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapTcpIpV4Packet import EthernetSnapTcpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapTcpIpV4TaggedPacket import \
    EthernetSnapTcpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapTcpIpV4VlanStackPacket import \
    EthernetSnapTcpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapUdpIpV4Packet import EthernetSnapUdpIpV4Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapUdpIpV4TaggedPacket import \
    EthernetSnapUdpIpV4TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV4.EthernetSnapUdpIpV4VlanStackPacket import \
    EthernetSnapUdpIpV4VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6Packet import EthernetSnapIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6TaggedPacket import EthernetSnapIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapIpV6VlanStackPacket import \
    EthernetSnapIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapTcpIpV6Packet import EthernetSnapTcpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapTcpIpV6TaggedPacket import \
    EthernetSnapTcpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapTcpIpV6VlanStackPacket import \
    EthernetSnapTcpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapUdpIpV6Packet import EthernetSnapUdpIpV6Packet
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapUdpIpV6TaggedPacket import \
    EthernetSnapUdpIpV6TaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.IpV6.EthernetSnapUdpIpV6VlanStackPacket import \
    EthernetSnapUdpIpV6VlanStackPacket
from ExtremeAutomation.Library.Net.Packet.Snap.Other.EthernetSnapLldpPacket import EthernetSnapLldpPacket
from ExtremeAutomation.Library.Net.Packet.Snap.Other.EthernetSnapLldpTaggedPacket import EthernetSnapLldpTaggedPacket
from ExtremeAutomation.Library.Net.Packet.Snap.Other.EthernetSnapLldpVlanStackPacket import \
    EthernetSnapLldpVlanStackPacket
# ### End Packets Auto-generated ####

# ### Start Packet Headers Auto-generated ####
from ExtremeAutomation.Library.Net.Packet.Ethernet2PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.EthernetPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.Ieee802LlcPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.SapPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.TaggedPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.VlanStackPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.IpV4.IpV4PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.IpV6.IpV6PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.Ipx.IpxPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ArpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BgpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BootpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.BpduPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrCsnpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrDbpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DbsyncDvrPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.DnsPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanIIIPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ErspanPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.GrePacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IcmpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IgmpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.InnerPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IpEncapsulatedPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisCSNPPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisHelloPduPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisLSPPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.IsisPSNPPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LldpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MplsEncapsulatedPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MplsPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.MstpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfDBDescriptionPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfHelloPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfLinkStateAcknowledgePacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfLinkStateRequestPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfLinkStateUpdatePacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.OspfPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.PimPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.ProviderBackboneBridgePacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RadiusPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RipNgPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RipPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.RstpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SnapPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SpanningTreePacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.SyslogPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.TcpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.UdpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VrrpPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.VxlanPacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer1PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer2PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer3PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer4PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer5PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer6PacketHeader import *
from ExtremeAutomation.Library.Net.Packet.PacketHeaders.LayerPacketHeaders.Layer7PacketHeader import *
########################################################################################################################
# ### End Packet Headers Auto-generated ####
########################################################################################################################

from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.FileUtils import FileUtils
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketTagConstants
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Logger import Logger
import sys
import traceback


class PacketClassifier(object):

    @staticmethod
    def classify_packet_bytes(packet_bytes):
        packet_bytes = packet_bytes.replace(" ", "")
        return PacketClassifier.classify_packet(
            packet_bytes[0:12], packet_bytes[12:24], packet_bytes[24:28], packet_bytes[28:])

    @staticmethod
    def classify_packet(da, sa, pkt_type, packet_bytes):
        # save off the original bytes to use later
        original_bytes = da + sa + pkt_type + packet_bytes
        # strip of the type field to classify the packet
        pkt_type = pkt_type.replace(" ", "").upper()
        all_bytes = original_bytes
        packet_bytes = packet_bytes.replace(" ", "")
        if pkt_type == "0800":
            packet = PacketClassifier.processIpv4Packet(all_bytes, "")
        elif pkt_type == PacketClassifierConstants.ETHER_TYPE_IPV6:
            packet = PacketClassifier.processIpv6Packet(all_bytes, "")
        elif pkt_type == "0806":
            packet = PacketClassifier.processArpPacket(all_bytes, "")
        elif pkt_type == "8847":
            packet = PacketClassifier.processMplsPacket(all_bytes, "")
        elif pkt_type == "88CC":
            packet = Ethernet2LldpPacket()
        elif pkt_type == "88E7":
            packet = Ethernet2ProviderBackboneBridgePacket()
        elif pkt_type == PacketClassifierConstants.ETHER_TYPE_DVR:
            packet = PacketClassifier.processDvrPacket(all_bytes, "")
        elif pkt_type in ["8100", "88A8", "9100", "9200", "9300"]:
            # this is a tagged packet, count out the headers and find if it's stacked or just tagged.
            # strip off the first tag
            packet_bytes = packet_bytes[4:]
            temp_type = packet_bytes[:4].upper()
            if temp_type in ["8100", "88A8", "9100", "9200", "9300"]:
                # the inner header is another stack so this is a stacked
                num_tags = 1
                while temp_type in ["8100", "88A8", "9100", "9200", "9300"]:
                    # attempt to strip off more taggs
                    num_tags += 1
                    packet_bytes = packet_bytes[8:]
                    temp_type = packet_bytes[:4].upper()
                packet = EthernetVlanStackPacket(num_tags)
                packet.set_payload(all_bytes)
                if temp_type == "0800":
                    packet = PacketClassifier.processIpv4Packet(all_bytes, str(num_tags))
                elif temp_type == "86DD":
                    packet = PacketClassifier.processIpv6Packet(all_bytes, str(num_tags))
                elif temp_type == "0806":
                    packet = PacketClassifier.processArpPacket(all_bytes, str(num_tags))
                elif temp_type == "8847":
                    packet = PacketClassifier.processMplsPacket(all_bytes, str(num_tags))
                elif temp_type == "88CC":
                    packet = Ethernet2LldpVlanStackPacket(num_tags)
                elif temp_type == "888E":
                    packet = Ethernet2RadiusUdpIpV4VlanStackPacket(num_tags)
                elif temp_type == "88E7":
                    packet = Ethernet2ProviderBackboneBridgeVlanStackPacket(num_tags)
                elif temp_type == PacketClassifierConstants.ETHER_TYPE_DVR:
                    packet = PacketClassifier.processDvrPacket(all_bytes, str(num_tags))
                elif int(temp_type, 16) < 1500:
                    packet = PacketClassifier.process802Packet(all_bytes, str(num_tags))
                else:
                    packet = Ethernet2VlanStackPacket(num_tags)
            else:
                # there is only one tag, this is a tagged packet.
                if temp_type == "0800":
                    packet = PacketClassifier.processIpv4Packet(all_bytes, "Tagged")
                elif temp_type == "86DD":
                    packet = PacketClassifier.processIpv6Packet(all_bytes, "Tagged")
                elif temp_type == "0806":
                    packet = PacketClassifier.processArpPacket(all_bytes, "Tagged")
                elif temp_type == "88CC":
                    packet = Ethernet2LldpTaggedPacket()
                elif temp_type == "88E7":
                    packet = Ethernet2ProviderBackboneBridgeTaggedPacket()
                elif temp_type == PacketClassifierConstants.ETHER_TYPE_DVR:
                    packet = PacketClassifier.processDvrPacket(all_bytes, "Tagged")
                elif int(temp_type, 16) < 1500:
                    packet = PacketClassifier.process802Packet(all_bytes, "Tagged")
                else:
                    packet = Ethernet2TaggedPacket()
        elif int(pkt_type, 16) <= 1500:
            packet = PacketClassifier.process802Packet(all_bytes, "")
        else:
            packet = Ethernet2Packet()
        # finally set the original bytes back into the packet.
        packet_bytes = original_bytes
        try:
            packet.set_payload(packet_bytes)
            if isinstance(packet, GrePacketHeader):
                try:
                    packet.set_gre_inner_packet(
                        PacketClassifier.classify_packet_bytes(packet.get_gre_inner_packet().get_bytes()))
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                    Logger().log_info("Something wrong with the inner encapsulated packet")
            elif isinstance(packet, VxlanPacketHeader):
                try:
                    packet.set_vxlan_inner_packet(
                        PacketClassifier.classify_packet_bytes(packet.get_vxlan_inner_packet().get_bytes()))
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                    Logger().log_info("Something wrong with the inner encapsulated packet")
            elif isinstance(packet, IpEncapsulatedPacketHeader):
                try:
                    packet.set_inner_packet(
                        PacketClassifier.classify_packet_bytes(packet.get_inner_packet().get_bytes()))
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                    Logger().log_info("Something wrong with the inner encapsulated packet")
            elif isinstance(packet, MplsEncapsulatedPacketHeader):
                try:
                    packet.set_inner_packet(
                        PacketClassifier.classify_packet_bytes(packet.get_inner_packet().get_bytes()))
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                    Logger().log_info("Something wrong with the inner encapsulated packet")
            elif isinstance(packet, ProviderBackboneBridgePacketHeader):
                try:
                    packet.set_inner_packet(
                        PacketClassifier.classify_packet_bytes(packet.get_inner_packet().get_bytes()))
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                    Logger().log_info("Something wrong with the inner encapsulated packet")

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            Logger().log_info("Packet is too short.")
            packet.set_status("Bad Packet")
            Logger().log_info("Captured Bytes:" + packet_bytes)
            Logger().log_info("*** format_exception:")
            Logger().log_info(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)).replace("\\n", "\n"))
            # Logger().log_info("*** extract_tb:")
            # Logger().log_info(repr(traceback.extract_tb(exc_traceback)).replace("\\n","\n"))
            # Logger().log_info("*** format_tb:")
            # Logger().log_info(repr(traceback.format_tb(exc_traceback)).replace("\\n","\n"))
            # Logger().log_info("*** tb_lineno:", exc_traceback.tb_lineno)
        packet.set_captured_bytes(packet_bytes)
        packet.set_length(len(packet_bytes.replace(" ", "")) // 2)
        return packet

    @staticmethod
    def processArpPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2ArpTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2ArpVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2ArpPacket()
        # packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processDvrPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2DbsyncDvrTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2DbsyncDvrVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2DbsyncDvrPacket()
        packet.set_payload(all_bytes)
        try:
            pl = packet.get_payload()
            pkt_type = pl[8:10]
            if pkt_type == "12":
                if tagged_type == 'Tagged':
                    packet = Ethernet2DbpDbsyncDvrTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2DbpDbsyncDvrVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2DbpDbsyncDvrPacket()
            if pkt_type == "18":
                if tagged_type == 'Tagged':
                    packet = Ethernet2CsnpDbsyncDvrTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2CsnpDbsyncDvrVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2CsnpDbsyncDvrPacket()
        except Exception as e:
            Logger().log_debug(e)
        return packet

    @staticmethod
    def processMplsPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2MplsTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2MplsVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2MplsPacket()
        packet.set_payload(all_bytes)
        if packet.get_payload().startswith("45"):
            if tagged_type == 'Tagged':
                packet = Ethernet2IpV4MplsTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IpV4MplsVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IpV4MplsPacket()
            packet.set_payload(all_bytes)
            if packet.get_ip_protocol() == 6:
                packet = PacketClassifier.processTcpIpv4MplsPacket(all_bytes, tagged_type)
            elif packet.get_ip_protocol() == 17:
                packet = PacketClassifier.processUdpIpv4MplsPacket(all_bytes, tagged_type)
            elif packet.get_ip_protocol() == 1:
                if tagged_type == 'Tagged':
                    packet = Ethernet2IcmpIpV4MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2IcmpIpV4MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2IcmpIpV4MplsPacket()
            elif packet.get_ip_protocol() == 2:
                if tagged_type == 'Tagged':
                    packet = Ethernet2IgmpIpV4MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2IgmpIpV4MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2IgmpIpV4MplsPacket()
            elif packet.get_ip_protocol() == 88:
                if tagged_type == 'Tagged':
                    packet = Ethernet2IgmpIpV4MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2IgmpIpV4MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2IgmpIpV4MplsPacket()
            elif packet.get_ip_protocol() == 112:
                if tagged_type == 'Tagged':
                    packet = Ethernet2VrrpIpV4MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2VrrpIpV4MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2VrrpIpV4MplsPacket()
        elif packet.get_payload().startswith("6"):
            if tagged_type == 'Tagged':
                packet = Ethernet2IpV6MplsTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IpV6MplsVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IpV6MplsPacket()
            packet.set_payload(all_bytes)
            if packet.get_ipv6_next_header() == 6 or packet.get_ipv6_last_next_header() == 6:
                packet = PacketClassifier.processTcpIpv6MplsPacket(all_bytes, tagged_type)
            elif packet.get_ipv6_next_header() == 17 or packet.get_ipv6_last_next_header() == 17:
                packet = PacketClassifier.processUdpIpv6MplsPacket(all_bytes, tagged_type)
            if packet.get_ipv6_next_header() == 58 or packet.get_ipv6_last_next_header() == 58:
                if tagged_type == 'Tagged':
                    packet = Ethernet2IcmpV6IpV6MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2IcmpV6IpV6MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2IcmpV6IpV6MplsPacket()
            elif packet.get_ipv6_next_header() == 112 or packet.get_ipv6_last_next_header() == 112:
                if tagged_type == 'Tagged':
                    packet = Ethernet2VrrpIpV6MplsTaggedPacket()
                elif tagged_type.isdigit():
                    packet = Ethernet2VrrpIpV6MplsVlanStackPacket(int(tagged_type))
                else:
                    packet = Ethernet2VrrpIpV6MplsPacket()
        # see if it a control word and room for an encapsulated packet
        elif packet.get_payload().startswith("00000000") and len(all_bytes) >= (4 * 2) + (64 * 2) + (60 * 2):
            if tagged_type == 'Tagged':
                packet = Ethernet2MplsEncapsulatedTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2MplsEncapsulatedVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2MplsEncapsulatedPacket()
        return packet

    @staticmethod
    def process802Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ieee802LlcTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ieee802LlcVlanStackPacket(int(tagged_type))
        else:
            packet = Ieee802LlcPacket()
        packet.set_payload(all_bytes)
        if packet.get_llc_dsap() == 0xE0 and packet.get_llc_ssap() == 0xE0:
            if tagged_type == 'Tagged':
                packet = Ieee802_2IpxTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ieee802_2IpxVlanStackPacket(int(tagged_type))
            else:
                packet = Ieee802_2IpxPacket()
        elif packet.get_llc_dsap() == 0xFE and packet.get_llc_ssap() == 0xFE:
            packet = PacketClassifier.process802IsisPacket(all_bytes, str(tagged_type))
        elif packet.get_llc_dsap() == 0xAA and packet.get_llc_ssap() == 0xAA:
            if tagged_type == 'Tagged':
                packet = EthernetSnapTaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapVlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapPacket()
            packet.set_payload(all_bytes)
            if packet.get_snap_ether_type() == 0x800:
                packet = PacketClassifier.processIpv4SnapPacket(all_bytes, tagged_type)
            elif packet.get_snap_ether_type() == 0x86DD:
                packet = PacketClassifier.processIpv6SnapPacket(all_bytes, tagged_type)
            # elif type == "88CC":
            #     packet = Ethernet2LldpTaggedPacket()
            # else:
            #     packet = EthernetSnapTaggedPacket()
        elif packet.get_llc_dsap() == 0x42 and packet.get_llc_ssap() == 0x42:
            packet = PacketClassifier.processSnapBpdu(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processSnapBpdu(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = SapBpduTaggedPacket()
        elif tagged_type.isdigit():
            packet = SapBpduVlanStackPacket(int(tagged_type))
        else:
            packet = SapBpduPacket()
        packet.set_payload(all_bytes)
        if packet.get_bpdu_version() == 3:
            if tagged_type == 'Tagged':
                packet = SapMstpSpanningTreeBpduTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapMstpSpanningTreeBpduVlanStackPacket(int(tagged_type))
            else:
                packet = SapMstpSpanningTreeBpduPacket()
            packet.set_payload(all_bytes)
        if packet.get_bpdu_version() == 2:
            if tagged_type == 'Tagged':
                packet = SapRstpBpduTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapRstpBpduVlanStackPacket(int(tagged_type))
            else:
                packet = SapRstpBpduPacket()
            packet.set_payload(all_bytes)
        if packet.get_bpdu_version() == 1:
            if tagged_type == 'Tagged':
                packet = SapSpanningTreeBpduTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapSpanningTreeBpduVlanStackPacket(int(tagged_type))
            else:
                packet = SapSpanningTreeBpduPacket()
            packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processIpv4Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2IpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2IpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2IpV4Packet()
        packet.set_payload(all_bytes)
        if packet.get_ip_protocol() == 6:
            packet = PacketClassifier.processTcpIpv4Packet(all_bytes, tagged_type)
        elif packet.get_ip_protocol() == 17:
            packet = PacketClassifier.processUdpIpv4Packet(all_bytes, tagged_type)
        elif packet.get_ip_protocol() == 1:
            if tagged_type == 'Tagged':
                packet = Ethernet2IcmpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IcmpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IcmpIpV4Packet()
        elif packet.get_ip_protocol() == 2:
            if tagged_type == 'Tagged':
                packet = Ethernet2IgmpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IgmpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IgmpIpV4Packet()
        elif packet.get_ip_protocol() == 47:
            packet = PacketClassifier.processEnet2GreIpv4Packet(all_bytes, tagged_type)
        elif packet.get_ip_protocol() == 4:
            if tagged_type == 'Tagged':
                packet = Ethernet2IpEncapsulatedIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IpEncapsulatedIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IpEncapsulatedIpV4Packet()
        elif packet.get_ip_protocol() == 88:
            if tagged_type == 'Tagged':
                packet = Ethernet2IgmpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IgmpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IgmpIpV4Packet()
        elif packet.get_ip_protocol() == 112:
            if tagged_type == 'Tagged':
                packet = Ethernet2VrrpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2VrrpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2VrrpIpV4Packet()
        elif packet.get_ip_protocol() == 0x67:
            if tagged_type == 'Tagged':
                packet = Ethernet2PimIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2PimIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2PimIpV4Packet()
        elif packet.get_ip_protocol() == 89:
            packet = PacketClassifier.processOspfPacket(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processOspfPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2OspfIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2OspfIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2OspfIpV4Packet()
        packet.set_payload(all_bytes)
        if packet.get_ospf_message_type() == 1:
            if tagged_type == 'Tagged':
                packet = Ethernet2HelloOspfIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2HelloOspfIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2HelloOspfIpV4Packet()
        elif packet.get_ospf_message_type() == 2:
            if tagged_type == 'Tagged':
                packet = Ethernet2DBDescriptionOspfIpV4TaggedPacket
            elif tagged_type.isdigit():
                packet = Ethernet2DBDescriptionOspfIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2DBDescriptionOspfIpV4Packet()
        elif packet.get_ospf_message_type() == 3:
            if tagged_type == 'Tagged':
                packet = Ethernet2LinkStateRequestOspfIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2LinkStateRequestOspfIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2LinkStateRequestOspfIpV4Packet()
        elif packet.get_ospf_message_type() == 4:
            if tagged_type == 'Tagged':
                packet = Ethernet2LinkStateUpdateOspfIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2LinkStateUpdateOspfIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2LinkStateUpdateOspfIpV4Packet()
        elif packet.get_ospf_message_type() == 5:
            if tagged_type == 'Tagged':
                packet = Ethernet2LinkStateAcknowledgeOspfIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2LinkStateAcknowledgeOspfIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2LinkStateAcknowledgeOspfIpV4Packet()
        return packet

    @staticmethod
    def processEnet2GreIpv4Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2GreIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2GreIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2GreIpV4Packet()
        packet.set_payload(all_bytes)
        if packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_II:
            if tagged_type == 'Tagged':
                packet = Ethernet2ErspanGreIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2ErspanGreIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2ErspanGreIpV4Packet()
        elif packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_III:
            if tagged_type == 'Tagged':
                packet = Ethernet2ErspanIIIGreIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2ErspanIIIGreIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2ErspanIIIGreIpV4Packet()
        return packet

    @staticmethod
    def processEnet2GreIpv6Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2GreIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2GreIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2GreIpV6Packet()
        packet.set_payload(all_bytes)
        if packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_II:
            if tagged_type == 'Tagged':
                packet = Ethernet2ErspanGreIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2ErspanGreIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2ErspanGreIpV6Packet()
        elif packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_III:
            if tagged_type == 'Tagged':
                packet = Ethernet2ErspanIIIGreIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2ErspanIIIGreIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2ErspanIIIGreIpV6Packet()
        return packet

    @staticmethod
    def processEnetSnapGreIpv4Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = EthernetSnapGreIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = EthernetSnapGreIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = EthernetSnapGreIpV4Packet()
        packet.set_payload(all_bytes)
        if packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_II:
            if tagged_type == 'Tagged':
                packet = EthernetSnapErspanGreIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapErspanGreIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapErspanGreIpV4Packet()
        elif packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_III:
            if tagged_type == 'Tagged':
                packet = EthernetSnapErspanIIIGreIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapErspanIIIGreIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapErspanIIIGreIpV4Packet()
        return packet

    @staticmethod
    def processEnetSnapGreIpv6Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = EthernetSnapGreIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = EthernetSnapGreIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = EthernetSnapGreIpV6Packet()
        packet.set_payload(all_bytes)
        if packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_II:
            if tagged_type == 'Tagged':
                packet = EthernetSnapErspanGreIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapErspanGreIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapErspanGreIpV6Packet()
        elif packet.get_gre_protocol_type() == GrePacketConstants.GRE_PROTOCOL_ESPAN_III:
            if tagged_type == 'Tagged':
                packet = EthernetSnapErspanIIIGreIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapErspanIIIGreIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapErspanIIIGreIpV6Packet()
        return packet

    @staticmethod
    def process802IsisPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = SapIsisTaggedPacket()
        elif tagged_type.isdigit():
            packet = SapIsisVlanStackPacket(int(tagged_type))
        else:
            packet = SapIsisPacket()
        packet.set_payload(all_bytes)
        pdu_type = packet.get_isis_pdu_type()
        if pdu_type == 0x0F or pdu_type == 0x10 or pdu_type == 0x11:
            if tagged_type == 'Tagged':
                packet = SapHelloPduIsisTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapHelloPduIsisVlanStackPacket(int(tagged_type))
            else:
                packet = SapHelloPduIsisPacket()
        elif pdu_type == 0x12 or pdu_type == 0x14:
            if tagged_type == 'Tagged':
                packet = SapLSPIsisTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapLSPIsisVlanStackPacket(int(tagged_type))
            else:
                packet = SapLSPIsisPacket()
        elif pdu_type == 0x18 or pdu_type == 0x19:
            if tagged_type == 'Tagged':
                packet = SapCSNPIsisTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapCSNPIsisVlanStackPacket(int(tagged_type))
            else:
                packet = SapCSNPIsisPacket()
        elif pdu_type == 0x1A or pdu_type == 0x1B:
            if tagged_type == 'Tagged':
                packet = SapPSNPIsisTaggedPacket()
            elif tagged_type.isdigit():
                packet = SapPSNPIsisVlanStackPacket(int(tagged_type))
            else:
                packet = SapPSNPIsisPacket()
        return packet

    @staticmethod
    def processTcpIpv4Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2TcpIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2TcpIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2TcpIpV4Packet()
        packet.set_payload(all_bytes)
        packet_payload = packet.get_payload()
        p = re.compile("[0]+")
        if p.match(packet_payload):
            return packet
        bgp_ports = [179]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        if sport in bgp_ports or dport in bgp_ports:
            packet = PacketClassifier.processBgpIpv4Packets(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processTcpIpv4MplsPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2TcpIpV4MplsTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2TcpIpV4MplsVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2TcpIpV4MplsPacket()
        packet.set_payload(all_bytes)
        packet_payload = packet.get_payload()
        p = re.compile("[0]+")
        if p.match(packet_payload):
            return packet
        bgp_ports = [179]
        syslog_ports = [514]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        # if sport in bgp_ports or dport in bgp_ports:
        #     packet = PacketClassifier.processBgpIpv4Packets(all_bytes, tagged_type)
        # if sport in syslog_ports or dport in syslog_ports:
        #     packet = PacketClassifier.processSyslogIpv4Packets(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processTcpIpv6Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2TcpIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2TcpIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2TcpIpV6Packet()
        packet.set_payload(all_bytes)
        packet_payload = packet.get_payload()
        p = re.compile("[0]+")
        if p.match(packet_payload):
            return packet
        bgp_ports = [179]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        if sport in bgp_ports or dport in bgp_ports:
            packet = PacketClassifier.processBgpIpv6Packets(all_bytes, tagged_type)
        # elif dport in vxlan_ports:
        #     if tagged_type == 'Tagged':
        #         packet = Ethernet2VxlanUdpIpV4TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = Ethernet2VxlanUdpIpV4VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = Ethernet2VxlanUdpIpV4Packet()
        return packet

    @staticmethod
    def processTcpIpv6MplsPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2TcpIpV6MplsTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2TcpIpV6MplsVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2TcpIpV6MplsPacket()
        packet.set_payload(all_bytes)
        packet_payload = packet.get_payload()
        p = re.compile("[0]+")
        if p.match(packet_payload):
            return packet
        bgp_ports = [179]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        # if sport in bgp_ports or dport in bgp_ports:
        #     packet = PacketClassifier.processBgpIpv6Packets(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processBgpIpv4Packets(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2BgpTcpIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2BgpTcpIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2BgpTcpIpV4Packet()
        packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processBgpIpv6Packets(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2BgpTcpIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2BgpTcpIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2BgpTcpIpV6Packet()
        packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processSyslogIpv4Packets(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2SyslogUdpIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2SyslogUdpIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2SyslogUdpIpV4Packet()
        packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processSyslogIpv6Packets(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2SyslogUdpIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2SyslogUdpIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2SyslogUdpIpV6Packet()
        packet.set_payload(all_bytes)
        return packet

    @staticmethod
    def processUdpIpv4Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2UdpIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2UdpIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2UdpIpV4Packet()
        packet.set_payload(all_bytes)
        radius_ports = [1812, 1813]
        vxlan_ports = [4789, 8472]
        rip_ports = [520, 521]
        bootp_ports = [67, 68]
        syslog_ports = [514]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        if sport in radius_ports or dport in radius_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RadiusUdpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RadiusUdpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RadiusUdpIpV4Packet()
        elif dport in vxlan_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2VxlanUdpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2VxlanUdpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2VxlanUdpIpV4Packet()
        elif sport in rip_ports or dport in rip_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RipUdpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RipUdpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RipUdpIpV4Packet()
        elif sport in bootp_ports or dport in bootp_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2BootpUdpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2BootpUdpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2BootpUdpIpV4Packet()
        elif sport in syslog_ports or dport in syslog_ports:
            packet = PacketClassifier.processSyslogIpv4Packets(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processUdpIpv4MplsPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2UdpIpV4MplsTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2UdpIpV4MplsVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2UdpIpV4MplsPacket()
        packet.set_payload(all_bytes)
        radius_ports = [1812, 1813]
        vxlan_ports = [4789, 8472]
        rip_ports = [520, 521]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        # if sport in radius_ports or dport in radius_ports:
        #     if tagged_type == 'Tagged':
        #         packet = Ethernet2RadiusUdpIpV4TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = Ethernet2RadiusUdpIpV4VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = Ethernet2RadiusUdpIpV4Packet()
        # elif dport in vxlan_ports:
        #     if tagged_type == 'Tagged':
        #         packet = Ethernet2VxlanUdpIpV4TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = Ethernet2VxlanUdpIpV4VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = Ethernet2VxlanUdpIpV4Packet()
        if dport in rip_ports or sport in rip_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RipUdpIpV4MplsTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RipUdpIpV4MplsVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RipUdpIpV4MplsPacket()
        return packet

    @staticmethod
    def processIpv6Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2IpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2IpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2IpV6Packet()
        packet.set_payload(all_bytes)
        if packet.get_ipv6_next_header() == 6 or packet.get_ipv6_last_next_header() == 6:
            packet = PacketClassifier.processTcpIpv6Packet(all_bytes, tagged_type)
        elif packet.get_ipv6_next_header() == 17 or packet.get_ipv6_last_next_header() == 17:
            packet = PacketClassifier.processUdpIpv6Packet(all_bytes, tagged_type)
        if packet.get_ipv6_next_header() == 58 or packet.get_ipv6_last_next_header() == 58:
            if tagged_type == 'Tagged':
                packet = Ethernet2IcmpV6IpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IcmpV6IpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IcmpV6IpV6Packet()
        elif packet.get_ipv6_next_header() == 47:
            packet = PacketClassifier.processEnet2GreIpv6Packet(all_bytes, tagged_type)
        elif packet.get_ipv6_next_header() == 4:
            if tagged_type == 'Tagged':
                packet = Ethernet2IpEncapsulatedIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2IpEncapsulatedIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2IpEncapsulatedIpV6Packet()
        elif packet.get_ipv6_next_header() == 112 or packet.get_ipv6_last_next_header() == 112:
            if tagged_type == 'Tagged':
                packet = Ethernet2VrrpIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2VrrpIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2VrrpIpV6Packet()
        elif packet.get_ipv6_next_header() == 0x67:
            if tagged_type == 'Tagged':
                packet = Ethernet2PimIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2PimIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2PimIpV6Packet()
        return packet

    @staticmethod
    def processUdpIpv6Packet(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2UdpIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2UdpIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2UdpIpV6Packet()
        packet.set_payload(all_bytes)
        radius_ports = [1812, 1813]
        vxlan_ports = [4789, 8472]
        rip_ports = [520, 521]
        syslog_ports = [514]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        if sport in radius_ports or dport in radius_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RadiusUdpIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RadiusUdpIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RadiusUdpIpV6Packet()
        elif dport in vxlan_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2VxlanUdpIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2VxlanUdpIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2VxlanUdpIpV6Packet()
        elif dport in rip_ports or sport in rip_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RipNgUdpIpV6MplsTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RipNgUdpIpV6MplsVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RipNgUdpIpV6MplsPacket()
        elif sport in syslog_ports or dport in syslog_ports:
            packet = PacketClassifier.processSyslogIpv6Packets(all_bytes, tagged_type)
        return packet

    @staticmethod
    def processUdpIpv6MplsPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = Ethernet2UdpIpV6MplsTaggedPacket()
        elif tagged_type.isdigit():
            packet = Ethernet2UdpIpV6MplsVlanStackPacket(int(tagged_type))
        else:
            packet = Ethernet2UdpIpV6MplsPacket()
        packet.set_payload(all_bytes)
        radius_ports = [1812, 1813]
        vxlan_ports = [4789, 8472]
        rip_ports = [520, 521]
        sport = packet.get_source_port()
        dport = packet.get_destination_port()
        if dport in rip_ports or sport in rip_ports:
            if tagged_type == 'Tagged':
                packet = Ethernet2RipNgUdpIpV6MplsTaggedPacket()
            elif tagged_type.isdigit():
                packet = Ethernet2RipNgUdpIpV6MplsVlanStackPacket(int(tagged_type))
            else:
                packet = Ethernet2RipNgUdpIpV6MplsPacket()
        # if sport in radius_ports or dport in radius_ports:
        #     if tagged_type == 'Tagged':
        #         packet = Ethernet2RadiusUdpIpV6TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = Ethernet2RadiusUdpIpV6VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = Ethernet2RadiusUdpIpV6Packet()
        # elif dport in vxlan_ports:
        #     if tagged_type == 'Tagged':
        #         packet = Ethernet2VxlanUdpIpV6TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = Ethernet2VxlanUdpIpV6VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = Ethernet2VxlanUdpIpV6Packet()
        return packet

    @staticmethod
    def processIpv4SnapPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = EthernetSnapIpV4TaggedPacket()
        elif tagged_type.isdigit():
            packet = EthernetSnapIpV4VlanStackPacket(int(tagged_type))
        else:
            packet = EthernetSnapIpV4Packet()
        packet.set_payload(all_bytes)
        if packet.get_ip_protocol() == 6:
            if tagged_type == 'Tagged':
                packet = EthernetSnapTcpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapTcpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapTcpIpV4Packet()
        elif packet.get_ip_protocol() == 17:
            if tagged_type == 'Tagged':
                packet = EthernetSnapUdpIpV4TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapUdpIpV4VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapUdpIpV4Packet()
        # elif packet.get_ip_protocol() == 1:
        #     if tagged_type == 'Tagged':
        #         packet = EthernetSnapIcmpIpV4TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = EthernetSnapIcmpIpV4VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = EthernetSnapIcmpIpV4Packet()
        # elif packet.get_ip_protocol() == 88:
        #     if tagged_type == 'Tagged':
        #         packet = EthernetSnapIgmpIpV4TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = EthernetSnapIgmpIpV4VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = EthernetSnapIgmpIpV4Packet()
        return packet

    @staticmethod
    def processIpv6SnapPacket(all_bytes, tagged_type):
        if tagged_type == 'Tagged':
            packet = EthernetSnapIpV6TaggedPacket()
        elif tagged_type.isdigit():
            packet = EthernetSnapIpV6VlanStackPacket(int(tagged_type))
        else:
            packet = EthernetSnapIpV6Packet()
        packet.set_payload(all_bytes)
        if packet.get_ipv6_next_header() == 6 or packet.get_ipv6_last_next_header() == 6:
            if tagged_type == 'Tagged':
                packet = EthernetSnapTcpIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapTcpIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapTcpIpV6Packet()
        elif packet.get_ipv6_next_header() == 17 or packet.get_ipv6_last_next_header() == 17:
            if tagged_type == 'Tagged':
                packet = EthernetSnapUdpIpV6TaggedPacket()
            elif tagged_type.isdigit():
                packet = EthernetSnapUdpIpV6VlanStackPacket(int(tagged_type))
            else:
                packet = EthernetSnapUdpIpV6Packet()
        # elif packet.get_ipv6_next_header() == 47 or packet.get_ipv6_last_next_header() == 47:
        #     if tagged_type == 'Tagged':
        #         packet = EthernetSnapIcmpV6IpV6TaggedPacket()
        #     elif tagged_type.isdigit():
        #         packet = EthernetSnapIcmpV6IpV6VlanStackPacket(int(tagged_type))
        #     else:
        #         packet = EthernetSnapIcmpV6IpV6Packet()
        return packet

    @staticmethod
    def copy_to_tag_packet(source_packet):
        if isinstance(source_packet, TaggedPacketHeader):
            return source_packet
        assert isinstance(source_packet, EthernetPacket)
        tags = source_packet.get_packet_tags()
        tags.append(PacketTagConstants.TAG_QTAGGED)
        if PacketTagConstants.TAG_VLAN_STACK in tags:
            tags.remove(PacketTagConstants.TAG_VLAN_STACK)
        packets = PacketClassifier.get_all_packets_from_tags(tags)
        if len(packets) > 0:
            packets.sort(key=lambda x: len(x.get_name()))
            packet = packets[0]
        else:
            packet = Ethernet2TaggedPacket()
        packet.clone(source_packet)
        return packet

    @staticmethod
    def copy_to_untag_packet(source_packet):
        if not isinstance(source_packet, TaggedPacketHeader) and not isinstance(source_packet, VlanStackPacketHeader):
            return source_packet
        assert isinstance(source_packet, EthernetPacket)
        tags = source_packet.get_packet_tags()
        if PacketTagConstants.TAG_VLAN_STACK in tags:
            tags.remove(PacketTagConstants.TAG_VLAN_STACK)
        if PacketTagConstants.TAG_QTAGGED in tags:
            tags.remove(PacketTagConstants.TAG_QTAGGED)
        packets = PacketClassifier.get_all_packets_from_tags(tags)
        if len(packets) > 0:
            packets.sort(key=lambda x: len(x.get_name()))
            packet = packets[0]
        else:
            packet = Ethernet2Packet()
        packet.clone(source_packet)
        return packet

    @staticmethod
    def copy_to_vlanstack_packet(source_packet):
        if isinstance(source_packet, VlanStackPacketHeader):
            return source_packet
        assert isinstance(source_packet, EthernetPacket)
        tags = source_packet.get_packet_tags()
        tags.append(PacketTagConstants.TAG_VLAN_STACK)
        if PacketTagConstants.TAG_QTAGGED in tags:
            tags.remove(PacketTagConstants.TAG_QTAGGED)
        packets = PacketClassifier.get_all_packets_from_tags(tags)
        if len(packets) > 0:
            packets.sort(key=lambda x: len(x.get_name()))
            packet = packets[0]
        else:
            packet = Ethernet2Packet()
        packet.clone(source_packet)
        return packet

    @staticmethod
    def copy_to_mpls_packet(source_packet):
        if isinstance(source_packet, MplsPacketHeader):
            return source_packet
        assert isinstance(source_packet, EthernetPacket)
        tags = source_packet.get_packet_tags()
        tags.append(PacketTagConstants.TAG_MPLS)
        packets = PacketClassifier.get_all_packets_from_tags(tags)
        if len(packets) > 0:
            packets.sort(key=lambda x: len(x.get_name()))
            packet = packets[0]
        else:
            if isinstance(source_packet, TaggedPacketHeader):
                packet = Ethernet2MplsTaggedPacket()
            elif isinstance(source_packet, VlanStackPacketHeader):
                packet = Ethernet2MplsVlanStackPacket(source_packet.get_num_vlans())
            else:
                packet = Ethernet2MplsPacket()
        packet.clone(source_packet)
        return packet

    @staticmethod
    def copy_to_nonmpls_packet(source_packet):
        if not isinstance(source_packet, MplsPacketHeader):
            return source_packet
        assert isinstance(source_packet, EthernetPacket)
        tags = source_packet.get_packet_tags()
        if PacketTagConstants.TAG_MPLS in tags:
            tags.remove(PacketTagConstants.TAG_MPLS)
        packets = PacketClassifier.get_all_packets_from_tags(tags)
        if len(packets) > 0:
            packets.sort(key=lambda x: len(x.get_name()))
            packet = packets[0]
        else:
            packet = Ethernet2Packet()
        packet.clone(source_packet)
        return packet

    @staticmethod
    def clone_packet(source_packet):
        return copy.deepcopy(source_packet)

    @staticmethod
    def get_one_of_every_snap():
        return PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_SNAP])

    @staticmethod
    def get_one_of_every_sap():
        return PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_SAP])

    @staticmethod
    def get_one_of_every_ethernet2():
        return PacketClassifier.get_all_packets_from_tags(PacketClassifierConstants.TAG_ENET2)

    @staticmethod
    def get_one_of_every_llc_ipx():
        return PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_IPX,
                                                           PacketClassifierConstants.TAG_BPDU,
                                                           PacketClassifierConstants.TAG_SPANNING_TREE])

    @staticmethod
    def get_one_of_every_llc_stp():
        return PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_BPDU,
                                                           PacketClassifierConstants.TAG_SPANNING_TREE])

    @staticmethod
    def get_one_of_every_untagged():
        return PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_UNTAGGED])

    @staticmethod
    def get_one_of_every_packet(pkt_filter=None):
        liste = PacketClassifier.get_all_packets_from_tags()
        if pkt_filter:
            new_list = []
            for p in liste:
                if pkt_filter.upper() in p.get_name().upper():
                    new_list.append(p)
            liste = new_list
        return liste

    @staticmethod
    def get_one_of_every_vlan_stacked_packet():
        return PacketClassifier.get_all_packets_from_tags(PacketClassifierConstants.TAG_VLAN_STACK)

    @staticmethod
    def get_one_of_every_lldp_packet():
        return PacketClassifier.get_all_packets_from_tags(PacketClassifierConstants.TAG_LLDP)

    # regenerate with Utils/PacketTypeSet.py
    # also call ExtremeAutomation\Keywords\TrafficKeywords\Utils\Constants\GenerateRobotVariables.py
    # after the info below is updated.
    @staticmethod
    def get_packet(name):
        # ### Start Pack Auto-generated ####
        name = name.upper()
        if name == "ABSTRACTPACKET":
            return AbstractPacket()
        if name == "ETHERNET2ARPPACKET":
            return Ethernet2ArpPacket()
        if name == "ETHERNET2ARPTAGGEDPACKET":
            return Ethernet2ArpTaggedPacket()
        if name == "ETHERNET2ARPVLANSTACKPACKET":
            return Ethernet2ArpVlanStackPacket(0)
        if name == "ETHERNET2MPLSPACKET":
            return Ethernet2MplsPacket()
        if name == "ETHERNET2MPLSTAGGEDPACKET":
            return Ethernet2MplsTaggedPacket()
        if name == "ETHERNET2MPLSVLANSTACKPACKET":
            return Ethernet2MplsVlanStackPacket(0)
        if name == "ETHERNET2PACKET":
            return Ethernet2Packet()
        if name == "ETHERNET2TAGGEDPACKET":
            return Ethernet2TaggedPacket()
        if name == "ETHERNET2VLANSTACKPACKET":
            return Ethernet2VlanStackPacket(0)
        if name == "ETHERNETPACKET":
            return EthernetPacket()
        if name == "ETHERNETTAGGEDPACKET":
            return EthernetTaggedPacket()
        if name == "ETHERNETVLANSTACKPACKET":
            return EthernetVlanStackPacket(0)
        if name == "IEEE802LLCPACKET":
            return Ieee802LlcPacket()
        if name == "IEEE802LLCTAGGEDPACKET":
            return Ieee802LlcTaggedPacket()
        if name == "IEEE802LLCVLANSTACKPACKET":
            return Ieee802LlcVlanStackPacket(0)
        if name == "SAPPACKET":
            return SapPacket()
        if name == "SAPTAGGEDPACKET":
            return SapTaggedPacket()
        if name == "SAPVLANSTACKPACKET":
            return SapVlanStackPacket(0)
        if name == "ETHERNET2MPLSENCAPSULATEDPACKET":
            return Ethernet2MplsEncapsulatedPacket()
        if name == "ETHERNET2MPLSENCAPSULATEDTAGGEDPACKET":
            return Ethernet2MplsEncapsulatedTaggedPacket()
        if name == "ETHERNET2MPLSENCAPSULATEDVLANSTACKPACKET":
            return Ethernet2MplsEncapsulatedVlanStackPacket(0)
        if name == "ETHERNET2PROVIDERBACKBONEBRIDGEPACKET":
            return Ethernet2ProviderBackboneBridgePacket()
        if name == "ETHERNET2PROVIDERBACKBONEBRIDGETAGGEDPACKET":
            return Ethernet2ProviderBackboneBridgeTaggedPacket()
        if name == "ETHERNET2PROVIDERBACKBONEBRIDGEVLANSTACKPACKET":
            return Ethernet2ProviderBackboneBridgeVlanStackPacket(0)
        if name == "ETHERNET2ERSPANGREIPV4PACKET":
            return Ethernet2ErspanGreIpV4Packet()
        if name == "ETHERNET2ERSPANGREIPV4TAGGEDPACKET":
            return Ethernet2ErspanGreIpV4TaggedPacket()
        if name == "ETHERNET2ERSPANGREIPV4VLANSTACKPACKET":
            return Ethernet2ErspanGreIpV4VlanStackPacket(0)
        if name == "ETHERNET2ERSPANIIIGREIPV4PACKET":
            return Ethernet2ErspanIIIGreIpV4Packet()
        if name == "ETHERNET2ERSPANIIIGREIPV4TAGGEDPACKET":
            return Ethernet2ErspanIIIGreIpV4TaggedPacket()
        if name == "ETHERNET2ERSPANIIIGREIPV4VLANSTACKPACKET":
            return Ethernet2ErspanIIIGreIpV4VlanStackPacket(0)
        if name == "ETHERNET2GREIPV4PACKET":
            return Ethernet2GreIpV4Packet()
        if name == "ETHERNET2GREIPV4TAGGEDPACKET":
            return Ethernet2GreIpV4TaggedPacket()
        if name == "ETHERNET2GREIPV4VLANSTACKPACKET":
            return Ethernet2GreIpV4VlanStackPacket(0)
        if name == "ETHERNET2IPENCAPSULATEDIPV4PACKET":
            return Ethernet2IpEncapsulatedIpV4Packet()
        if name == "ETHERNET2IPENCAPSULATEDIPV4TAGGEDPACKET":
            return Ethernet2IpEncapsulatedIpV4TaggedPacket()
        if name == "ETHERNET2IPENCAPSULATEDIPV4VLANSTACKPACKET":
            return Ethernet2IpEncapsulatedIpV4VlanStackPacket(0)
        if name == "ETHERNET2VXLANUDPIPV4PACKET":
            return Ethernet2VxlanUdpIpV4Packet()
        if name == "ETHERNET2VXLANUDPIPV4TAGGEDPACKET":
            return Ethernet2VxlanUdpIpV4TaggedPacket()
        if name == "ETHERNET2VXLANUDPIPV4VLANSTACKPACKET":
            return Ethernet2VxlanUdpIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPERSPANGREIPV4PACKET":
            return EthernetSnapErspanGreIpV4Packet()
        if name == "ETHERNETSNAPERSPANGREIPV4TAGGEDPACKET":
            return EthernetSnapErspanGreIpV4TaggedPacket()
        if name == "ETHERNETSNAPERSPANGREIPV4VLANSTACKPACKET":
            return EthernetSnapErspanGreIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPERSPANIIIGREIPV4PACKET":
            return EthernetSnapErspanIIIGreIpV4Packet()
        if name == "ETHERNETSNAPERSPANIIIGREIPV4TAGGEDPACKET":
            return EthernetSnapErspanIIIGreIpV4TaggedPacket()
        if name == "ETHERNETSNAPERSPANIIIGREIPV4VLANSTACKPACKET":
            return EthernetSnapErspanIIIGreIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPGREIPV4PACKET":
            return EthernetSnapGreIpV4Packet()
        if name == "ETHERNETSNAPGREIPV4TAGGEDPACKET":
            return EthernetSnapGreIpV4TaggedPacket()
        if name == "ETHERNETSNAPGREIPV4VLANSTACKPACKET":
            return EthernetSnapGreIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV4PACKET":
            return EthernetSnapIpEncapsulatedIpV4Packet()
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV4TAGGEDPACKET":
            return EthernetSnapIpEncapsulatedIpV4TaggedPacket()
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV4VLANSTACKPACKET":
            return EthernetSnapIpEncapsulatedIpV4VlanStackPacket(0)
        if name == "ETHERNET2ERSPANGREIPV6PACKET":
            return Ethernet2ErspanGreIpV6Packet()
        if name == "ETHERNET2ERSPANGREIPV6TAGGEDPACKET":
            return Ethernet2ErspanGreIpV6TaggedPacket()
        if name == "ETHERNET2ERSPANGREIPV6VLANSTACKPACKET":
            return Ethernet2ErspanGreIpV6VlanStackPacket(0)
        if name == "ETHERNET2ERSPANIIIGREIPV6PACKET":
            return Ethernet2ErspanIIIGreIpV6Packet()
        if name == "ETHERNET2ERSPANIIIGREIPV6TAGGEDPACKET":
            return Ethernet2ErspanIIIGreIpV6TaggedPacket()
        if name == "ETHERNET2ERSPANIIIGREIPV6VLANSTACKPACKET":
            return Ethernet2ErspanIIIGreIpV6VlanStackPacket(0)
        if name == "ETHERNET2GREIPV6PACKET":
            return Ethernet2GreIpV6Packet()
        if name == "ETHERNET2GREIPV6TAGGEDPACKET":
            return Ethernet2GreIpV6TaggedPacket()
        if name == "ETHERNET2GREIPV6VLANSTACKPACKET":
            return Ethernet2GreIpV6VlanStackPacket(0)
        if name == "ETHERNET2IPENCAPSULATEDIPV6PACKET":
            return Ethernet2IpEncapsulatedIpV6Packet()
        if name == "ETHERNET2IPENCAPSULATEDIPV6TAGGEDPACKET":
            return Ethernet2IpEncapsulatedIpV6TaggedPacket()
        if name == "ETHERNET2IPENCAPSULATEDIPV6VLANSTACKPACKET":
            return Ethernet2IpEncapsulatedIpV6VlanStackPacket(0)
        if name == "ETHERNET2VXLANUDPIPV6PACKET":
            return Ethernet2VxlanUdpIpV6Packet()
        if name == "ETHERNET2VXLANUDPIPV6TAGGEDPACKET":
            return Ethernet2VxlanUdpIpV6TaggedPacket()
        if name == "ETHERNET2VXLANUDPIPV6VLANSTACKPACKET":
            return Ethernet2VxlanUdpIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPERSPANGREIPV6PACKET":
            return EthernetSnapErspanGreIpV6Packet()
        if name == "ETHERNETSNAPERSPANGREIPV6TAGGEDPACKET":
            return EthernetSnapErspanGreIpV6TaggedPacket()
        if name == "ETHERNETSNAPERSPANGREIPV6VLANSTACKPACKET":
            return EthernetSnapErspanGreIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPERSPANIIIGREIPV6PACKET":
            return EthernetSnapErspanIIIGreIpV6Packet()
        if name == "ETHERNETSNAPERSPANIIIGREIPV6TAGGEDPACKET":
            return EthernetSnapErspanIIIGreIpV6TaggedPacket()
        if name == "ETHERNETSNAPERSPANIIIGREIPV6VLANSTACKPACKET":
            return EthernetSnapErspanIIIGreIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPGREIPV6PACKET":
            return EthernetSnapGreIpV6Packet()
        if name == "ETHERNETSNAPGREIPV6TAGGEDPACKET":
            return EthernetSnapGreIpV6TaggedPacket()
        if name == "ETHERNETSNAPGREIPV6VLANSTACKPACKET":
            return EthernetSnapGreIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV6PACKET":
            return EthernetSnapIpEncapsulatedIpV6Packet()
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV6TAGGEDPACKET":
            return EthernetSnapIpEncapsulatedIpV6TaggedPacket()
        if name == "ETHERNETSNAPIPENCAPSULATEDIPV6VLANSTACKPACKET":
            return EthernetSnapIpEncapsulatedIpV6VlanStackPacket(0)
        if name == "ETHERNET2BOOTPUDPIPV4PACKET":
            return Ethernet2BootpUdpIpV4Packet()
        if name == "ETHERNET2BOOTPUDPIPV4TAGGEDPACKET":
            return Ethernet2BootpUdpIpV4TaggedPacket()
        if name == "ETHERNET2BOOTPUDPIPV4VLANSTACKPACKET":
            return Ethernet2BootpUdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2DBDESCRIPTIONOSPFIPV4PACKET":
            return Ethernet2DBDescriptionOspfIpV4Packet()
        if name == "ETHERNET2DBDESCRIPTIONOSPFIPV4TAGGEDPACKET":
            return Ethernet2DBDescriptionOspfIpV4TaggedPacket()
        if name == "ETHERNET2DBDESCRIPTIONOSPFIPV4VLANSTACKPACKET":
            return Ethernet2DBDescriptionOspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2DNSTCPIPV4PACKET":
            return Ethernet2DnsTcpIpV4Packet()
        if name == "ETHERNET2DNSTCPIPV4TAGGEDPACKET":
            return Ethernet2DnsTcpIpV4TaggedPacket()
        if name == "ETHERNET2DNSTCPIPV4VLANSTACKPACKET":
            return Ethernet2DnsTcpIpV4VlanStackPacket(0)
        if name == "ETHERNET2DNSUDPIPV4PACKET":
            return Ethernet2DnsUdpIpV4Packet()
        if name == "ETHERNET2DNSUDPIPV4TAGGEDPACKET":
            return Ethernet2DnsUdpIpV4TaggedPacket()
        if name == "ETHERNET2DNSUDPIPV4VLANSTACKPACKET":
            return Ethernet2DnsUdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2HELLOOSPFIPV4PACKET":
            return Ethernet2HelloOspfIpV4Packet()
        if name == "ETHERNET2HELLOOSPFIPV4TAGGEDPACKET":
            return Ethernet2HelloOspfIpV4TaggedPacket()
        if name == "ETHERNET2HELLOOSPFIPV4VLANSTACKPACKET":
            return Ethernet2HelloOspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2ICMPIPV4MPLSPACKET":
            return Ethernet2IcmpIpV4MplsPacket()
        if name == "ETHERNET2ICMPIPV4MPLSTAGGEDPACKET":
            return Ethernet2IcmpIpV4MplsTaggedPacket()
        if name == "ETHERNET2ICMPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2IcmpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2ICMPIPV4PACKET":
            return Ethernet2IcmpIpV4Packet()
        if name == "ETHERNET2ICMPIPV4TAGGEDPACKET":
            return Ethernet2IcmpIpV4TaggedPacket()
        if name == "ETHERNET2ICMPIPV4VLANSTACKPACKET":
            return Ethernet2IcmpIpV4VlanStackPacket(0)
        if name == "ETHERNET2IGMPIPV4MPLSPACKET":
            return Ethernet2IgmpIpV4MplsPacket()
        if name == "ETHERNET2IGMPIPV4MPLSTAGGEDPACKET":
            return Ethernet2IgmpIpV4MplsTaggedPacket()
        if name == "ETHERNET2IGMPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2IgmpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2IGMPIPV4PACKET":
            return Ethernet2IgmpIpV4Packet()
        if name == "ETHERNET2IGMPIPV4TAGGEDPACKET":
            return Ethernet2IgmpIpV4TaggedPacket()
        if name == "ETHERNET2IGMPIPV4VLANSTACKPACKET":
            return Ethernet2IgmpIpV4VlanStackPacket(0)
        if name == "ETHERNET2IPV4MPLSPACKET":
            return Ethernet2IpV4MplsPacket()
        if name == "ETHERNET2IPV4MPLSTAGGEDPACKET":
            return Ethernet2IpV4MplsTaggedPacket()
        if name == "ETHERNET2IPV4MPLSVLANSTACKPACKET":
            return Ethernet2IpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2IPV4PACKET":
            return Ethernet2IpV4Packet()
        if name == "ETHERNET2IPV4TAGGEDPACKET":
            return Ethernet2IpV4TaggedPacket()
        if name == "ETHERNET2IPV4VLANSTACKPACKET":
            return Ethernet2IpV4VlanStackPacket(0)
        if name == "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4PACKET":
            return Ethernet2LinkStateAcknowledgeOspfIpV4Packet()
        if name == "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4TAGGEDPACKET":
            return Ethernet2LinkStateAcknowledgeOspfIpV4TaggedPacket()
        if name == "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4VLANSTACKPACKET":
            return Ethernet2LinkStateAcknowledgeOspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2LINKSTATEREQUESTOSPFIPV4PACKET":
            return Ethernet2LinkStateRequestOspfIpV4Packet()
        if name == "ETHERNET2LINKSTATEREQUESTOSPFIPV4TAGGEDPACKET":
            return Ethernet2LinkStateRequestOspfIpV4TaggedPacket()
        if name == "ETHERNET2LINKSTATEREQUESTOSPFIPV4VLANSTACKPACKET":
            return Ethernet2LinkStateRequestOspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2LINKSTATEUPDATEOSPFIPV4PACKET":
            return Ethernet2LinkStateUpdateOspfIpV4Packet()
        if name == "ETHERNET2LINKSTATEUPDATEOSPFIPV4TAGGEDPACKET":
            return Ethernet2LinkStateUpdateOspfIpV4TaggedPacket()
        if name == "ETHERNET2LINKSTATEUPDATEOSPFIPV4VLANSTACKPACKET":
            return Ethernet2LinkStateUpdateOspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2OSPFIPV4PACKET":
            return Ethernet2OspfIpV4Packet()
        if name == "ETHERNET2OSPFIPV4TAGGEDPACKET":
            return Ethernet2OspfIpV4TaggedPacket()
        if name == "ETHERNET2OSPFIPV4VLANSTACKPACKET":
            return Ethernet2OspfIpV4VlanStackPacket(0)
        if name == "ETHERNET2PIMIPV4PACKET":
            return Ethernet2PimIpV4Packet()
        if name == "ETHERNET2PIMIPV4TAGGEDPACKET":
            return Ethernet2PimIpV4TaggedPacket()
        if name == "ETHERNET2PIMIPV4VLANSTACKPACKET":
            return Ethernet2PimIpV4VlanStackPacket(0)
        if name == "ETHERNET2RADIUSUDPIPV4PACKET":
            return Ethernet2RadiusUdpIpV4Packet()
        if name == "ETHERNET2RADIUSUDPIPV4TAGGEDPACKET":
            return Ethernet2RadiusUdpIpV4TaggedPacket()
        if name == "ETHERNET2RADIUSUDPIPV4VLANSTACKPACKET":
            return Ethernet2RadiusUdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2RIPUDPIPV4MPLSPACKET":
            return Ethernet2RipUdpIpV4MplsPacket()
        if name == "ETHERNET2RIPUDPIPV4MPLSTAGGEDPACKET":
            return Ethernet2RipUdpIpV4MplsTaggedPacket()
        if name == "ETHERNET2RIPUDPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2RipUdpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2RIPUDPIPV4PACKET":
            return Ethernet2RipUdpIpV4Packet()
        if name == "ETHERNET2RIPUDPIPV4TAGGEDPACKET":
            return Ethernet2RipUdpIpV4TaggedPacket()
        if name == "ETHERNET2RIPUDPIPV4VLANSTACKPACKET":
            return Ethernet2RipUdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2SYSLOGUDPIPV4PACKET":
            return Ethernet2SyslogUdpIpV4Packet()
        if name == "ETHERNET2SYSLOGUDPIPV4TAGGEDPACKET":
            return Ethernet2SyslogUdpIpV4TaggedPacket()
        if name == "ETHERNET2SYSLOGUDPIPV4VLANSTACKPACKET":
            return Ethernet2SyslogUdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2TCPIPV4MPLSPACKET":
            return Ethernet2TcpIpV4MplsPacket()
        if name == "ETHERNET2TCPIPV4MPLSTAGGEDPACKET":
            return Ethernet2TcpIpV4MplsTaggedPacket()
        if name == "ETHERNET2TCPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2TcpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2TCPIPV4PACKET":
            return Ethernet2TcpIpV4Packet()
        if name == "ETHERNET2TCPIPV4TAGGEDPACKET":
            return Ethernet2TcpIpV4TaggedPacket()
        if name == "ETHERNET2TCPIPV4VLANSTACKPACKET":
            return Ethernet2TcpIpV4VlanStackPacket(0)
        if name == "ETHERNET2UDPIPV4MPLSPACKET":
            return Ethernet2UdpIpV4MplsPacket()
        if name == "ETHERNET2UDPIPV4MPLSTAGGEDPACKET":
            return Ethernet2UdpIpV4MplsTaggedPacket()
        if name == "ETHERNET2UDPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2UdpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2UDPIPV4PACKET":
            return Ethernet2UdpIpV4Packet()
        if name == "ETHERNET2UDPIPV4TAGGEDPACKET":
            return Ethernet2UdpIpV4TaggedPacket()
        if name == "ETHERNET2UDPIPV4VLANSTACKPACKET":
            return Ethernet2UdpIpV4VlanStackPacket(0)
        if name == "ETHERNET2VRRPIPV4MPLSPACKET":
            return Ethernet2VrrpIpV4MplsPacket()
        if name == "ETHERNET2VRRPIPV4MPLSTAGGEDPACKET":
            return Ethernet2VrrpIpV4MplsTaggedPacket()
        if name == "ETHERNET2VRRPIPV4MPLSVLANSTACKPACKET":
            return Ethernet2VrrpIpV4MplsVlanStackPacket(0)
        if name == "ETHERNET2VRRPIPV4PACKET":
            return Ethernet2VrrpIpV4Packet()
        if name == "ETHERNET2VRRPIPV4TAGGEDPACKET":
            return Ethernet2VrrpIpV4TaggedPacket()
        if name == "ETHERNET2VRRPIPV4VLANSTACKPACKET":
            return Ethernet2VrrpIpV4VlanStackPacket(0)
        if name == "ETHERNET2BGPTCPIPV4PACKET":
            return Ethernet2BgpTcpIpV4Packet()
        if name == "ETHERNET2BGPTCPIPV4TAGGEDPACKET":
            return Ethernet2BgpTcpIpV4TaggedPacket()
        if name == "ETHERNET2BGPTCPIPV4VLANSTACKPACKET":
            return Ethernet2BgpTcpIpV4VlanStackPacket(0)
        if name == "ETHERNET2DNSTCPIPV6PACKET":
            return Ethernet2DnsTcpIpV6Packet()
        if name == "ETHERNET2DNSTCPIPV6TAGGEDPACKET":
            return Ethernet2DnsTcpIpV6TaggedPacket()
        if name == "ETHERNET2DNSTCPIPV6VLANSTACKPACKET":
            return Ethernet2DnsTcpIpV6VlanStackPacket(0)
        if name == "ETHERNET2DNSUDPIPV6PACKET":
            return Ethernet2DnsUdpIpV6Packet()
        if name == "ETHERNET2DNSUDPIPV6TAGGEDPACKET":
            return Ethernet2DnsUdpIpV6TaggedPacket()
        if name == "ETHERNET2DNSUDPIPV6VLANSTACKPACKET":
            return Ethernet2DnsUdpIpV6VlanStackPacket(0)
        if name == "ETHERNET2ICMPV6IPV6MPLSPACKET":
            return Ethernet2IcmpV6IpV6MplsPacket()
        if name == "ETHERNET2ICMPV6IPV6MPLSTAGGEDPACKET":
            return Ethernet2IcmpV6IpV6MplsTaggedPacket()
        if name == "ETHERNET2ICMPV6IPV6MPLSVLANSTACKPACKET":
            return Ethernet2IcmpV6IpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2ICMPV6IPV6PACKET":
            return Ethernet2IcmpV6IpV6Packet()
        if name == "ETHERNET2ICMPV6IPV6TAGGEDPACKET":
            return Ethernet2IcmpV6IpV6TaggedPacket()
        if name == "ETHERNET2ICMPV6IPV6VLANSTACKPACKET":
            return Ethernet2IcmpV6IpV6VlanStackPacket(0)
        if name == "ETHERNET2IPV6MPLSPACKET":
            return Ethernet2IpV6MplsPacket()
        if name == "ETHERNET2IPV6MPLSTAGGEDPACKET":
            return Ethernet2IpV6MplsTaggedPacket()
        if name == "ETHERNET2IPV6MPLSVLANSTACKPACKET":
            return Ethernet2IpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2IPV6PACKET":
            return Ethernet2IpV6Packet()
        if name == "ETHERNET2IPV6TAGGEDPACKET":
            return Ethernet2IpV6TaggedPacket()
        if name == "ETHERNET2IPV6VLANSTACKPACKET":
            return Ethernet2IpV6VlanStackPacket(0)
        if name == "ETHERNET2PIMIPV6PACKET":
            return Ethernet2PimIpV6Packet()
        if name == "ETHERNET2PIMIPV6TAGGEDPACKET":
            return Ethernet2PimIpV6TaggedPacket()
        if name == "ETHERNET2PIMIPV6VLANSTACKPACKET":
            return Ethernet2PimIpV6VlanStackPacket(0)
        if name == "ETHERNET2RADIUSUDPIPV6PACKET":
            return Ethernet2RadiusUdpIpV6Packet()
        if name == "ETHERNET2RADIUSUDPIPV6TAGGEDPACKET":
            return Ethernet2RadiusUdpIpV6TaggedPacket()
        if name == "ETHERNET2RADIUSUDPIPV6VLANSTACKPACKET":
            return Ethernet2RadiusUdpIpV6VlanStackPacket(0)
        if name == "ETHERNET2RIPNGUDPIPV6MPLSPACKET":
            return Ethernet2RipNgUdpIpV6MplsPacket()
        if name == "ETHERNET2RIPNGUDPIPV6MPLSTAGGEDPACKET":
            return Ethernet2RipNgUdpIpV6MplsTaggedPacket()
        if name == "ETHERNET2RIPNGUDPIPV6MPLSVLANSTACKPACKET":
            return Ethernet2RipNgUdpIpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2RIPNGUDPIPV6PACKET":
            return Ethernet2RipNgUdpIpV6Packet()
        if name == "ETHERNET2RIPNGUDPIPV6TAGGEDPACKET":
            return Ethernet2RipNgUdpIpV6TaggedPacket()
        if name == "ETHERNET2RIPNGUDPIPV6VLANSTACKPACKET":
            return Ethernet2RipNgUdpIpV6VlanStackPacket(0)
        if name == "ETHERNET2SYSLOGUDPIPV6PACKET":
            return Ethernet2SyslogUdpIpV6Packet()
        if name == "ETHERNET2SYSLOGUDPIPV6TAGGEDPACKET":
            return Ethernet2SyslogUdpIpV6TaggedPacket()
        if name == "ETHERNET2SYSLOGUDPIPV6VLANSTACKPACKET":
            return Ethernet2SyslogUdpIpV6VlanStackPacket(0)
        if name == "ETHERNET2TCPIPV6MPLSPACKET":
            return Ethernet2TcpIpV6MplsPacket()
        if name == "ETHERNET2TCPIPV6MPLSTAGGEDPACKET":
            return Ethernet2TcpIpV6MplsTaggedPacket()
        if name == "ETHERNET2TCPIPV6MPLSVLANSTACKPACKET":
            return Ethernet2TcpIpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2TCPIPV6PACKET":
            return Ethernet2TcpIpV6Packet()
        if name == "ETHERNET2TCPIPV6TAGGEDPACKET":
            return Ethernet2TcpIpV6TaggedPacket()
        if name == "ETHERNET2TCPIPV6VLANSTACKPACKET":
            return Ethernet2TcpIpV6VlanStackPacket(0)
        if name == "ETHERNET2UDPIPV6MPLSPACKET":
            return Ethernet2UdpIpV6MplsPacket()
        if name == "ETHERNET2UDPIPV6MPLSTAGGEDPACKET":
            return Ethernet2UdpIpV6MplsTaggedPacket()
        if name == "ETHERNET2UDPIPV6MPLSVLANSTACKPACKET":
            return Ethernet2UdpIpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2UDPIPV6PACKET":
            return Ethernet2UdpIpV6Packet()
        if name == "ETHERNET2UDPIPV6TAGGEDPACKET":
            return Ethernet2UdpIpV6TaggedPacket()
        if name == "ETHERNET2UDPIPV6VLANSTACKPACKET":
            return Ethernet2UdpIpV6VlanStackPacket(0)
        if name == "ETHERNET2VRRPIPV6MPLSPACKET":
            return Ethernet2VrrpIpV6MplsPacket()
        if name == "ETHERNET2VRRPIPV6MPLSTAGGEDPACKET":
            return Ethernet2VrrpIpV6MplsTaggedPacket()
        if name == "ETHERNET2VRRPIPV6MPLSVLANSTACKPACKET":
            return Ethernet2VrrpIpV6MplsVlanStackPacket(0)
        if name == "ETHERNET2VRRPIPV6PACKET":
            return Ethernet2VrrpIpV6Packet()
        if name == "ETHERNET2VRRPIPV6TAGGEDPACKET":
            return Ethernet2VrrpIpV6TaggedPacket()
        if name == "ETHERNET2VRRPIPV6VLANSTACKPACKET":
            return Ethernet2VrrpIpV6VlanStackPacket(0)
        if name == "ETHERNET2BGPTCPIPV6PACKET":
            return Ethernet2BgpTcpIpV6Packet()
        if name == "ETHERNET2BGPTCPIPV6TAGGEDPACKET":
            return Ethernet2BgpTcpIpV6TaggedPacket()
        if name == "ETHERNET2BGPTCPIPV6VLANSTACKPACKET":
            return Ethernet2BgpTcpIpV6VlanStackPacket(0)
        if name == "IEEE802_2IPXPACKET":
            return Ieee802_2IpxPacket()
        if name == "IEEE802_2IPXTAGGEDPACKET":
            return Ieee802_2IpxTaggedPacket()
        if name == "IEEE802_2IPXVLANSTACKPACKET":
            return Ieee802_2IpxVlanStackPacket(0)
        if name == "ETHERNET2CSNPDBSYNCDVRPACKET":
            return Ethernet2CsnpDbsyncDvrPacket()
        if name == "ETHERNET2CSNPDBSYNCDVRTAGGEDPACKET":
            return Ethernet2CsnpDbsyncDvrTaggedPacket()
        if name == "ETHERNET2CSNPDBSYNCDVRVLANSTACKPACKET":
            return Ethernet2CsnpDbsyncDvrVlanStackPacket(0)
        if name == "ETHERNET2DBPDBSYNCDVRPACKET":
            return Ethernet2DbpDbsyncDvrPacket()
        if name == "ETHERNET2DBPDBSYNCDVRTAGGEDPACKET":
            return Ethernet2DbpDbsyncDvrTaggedPacket()
        if name == "ETHERNET2DBPDBSYNCDVRVLANSTACKPACKET":
            return Ethernet2DbpDbsyncDvrVlanStackPacket(0)
        if name == "ETHERNET2DBSYNCDVRPACKET":
            return Ethernet2DbsyncDvrPacket()
        if name == "ETHERNET2DBSYNCDVRTAGGEDPACKET":
            return Ethernet2DbsyncDvrTaggedPacket()
        if name == "ETHERNET2DBSYNCDVRVLANSTACKPACKET":
            return Ethernet2DbsyncDvrVlanStackPacket(0)
        if name == "ETHERNET2LLDPPACKET":
            return Ethernet2LldpPacket()
        if name == "ETHERNET2LLDPTAGGEDPACKET":
            return Ethernet2LldpTaggedPacket()
        if name == "ETHERNET2LLDPVLANSTACKPACKET":
            return Ethernet2LldpVlanStackPacket(0)
        if name == "SAPBPDUPACKET":
            return SapBpduPacket()
        if name == "SAPBPDUTAGGEDPACKET":
            return SapBpduTaggedPacket()
        if name == "SAPBPDUVLANSTACKPACKET":
            return SapBpduVlanStackPacket(0)
        if name == "SAPMSTPSPANNINGTREEBPDUPACKET":
            return SapMstpSpanningTreeBpduPacket()
        if name == "SAPMSTPSPANNINGTREEBPDUTAGGEDPACKET":
            return SapMstpSpanningTreeBpduTaggedPacket()
        if name == "SAPMSTPSPANNINGTREEBPDUVLANSTACKPACKET":
            return SapMstpSpanningTreeBpduVlanStackPacket(0)
        if name == "SAPRSTPBPDUPACKET":
            return SapRstpBpduPacket()
        if name == "SAPRSTPBPDUTAGGEDPACKET":
            return SapRstpBpduTaggedPacket()
        if name == "SAPRSTPBPDUVLANSTACKPACKET":
            return SapRstpBpduVlanStackPacket(0)
        if name == "SAPSPANNINGTREEBPDUPACKET":
            return SapSpanningTreeBpduPacket()
        if name == "SAPSPANNINGTREEBPDUTAGGEDPACKET":
            return SapSpanningTreeBpduTaggedPacket()
        if name == "SAPSPANNINGTREEBPDUVLANSTACKPACKET":
            return SapSpanningTreeBpduVlanStackPacket(0)
        if name == "SAPCSNPISISPACKET":
            return SapCSNPIsisPacket()
        if name == "SAPCSNPISISTAGGEDPACKET":
            return SapCSNPIsisTaggedPacket()
        if name == "SAPCSNPISISVLANSTACKPACKET":
            return SapCSNPIsisVlanStackPacket(0)
        if name == "SAPHELLOPDUISISPACKET":
            return SapHelloPduIsisPacket()
        if name == "SAPHELLOPDUISISTAGGEDPACKET":
            return SapHelloPduIsisTaggedPacket()
        if name == "SAPHELLOPDUISISVLANSTACKPACKET":
            return SapHelloPduIsisVlanStackPacket(0)
        if name == "SAPISISPACKET":
            return SapIsisPacket()
        if name == "SAPISISTAGGEDPACKET":
            return SapIsisTaggedPacket()
        if name == "SAPISISVLANSTACKPACKET":
            return SapIsisVlanStackPacket(0)
        if name == "SAPLSPISISPACKET":
            return SapLSPIsisPacket()
        if name == "SAPLSPISISTAGGEDPACKET":
            return SapLSPIsisTaggedPacket()
        if name == "SAPLSPISISVLANSTACKPACKET":
            return SapLSPIsisVlanStackPacket(0)
        if name == "SAPPSNPISISPACKET":
            return SapPSNPIsisPacket()
        if name == "SAPPSNPISISTAGGEDPACKET":
            return SapPSNPIsisTaggedPacket()
        if name == "SAPPSNPISISVLANSTACKPACKET":
            return SapPSNPIsisVlanStackPacket(0)
        if name == "ETHERNETSNAPPACKET":
            return EthernetSnapPacket()
        if name == "ETHERNETSNAPTAGGEDPACKET":
            return EthernetSnapTaggedPacket()
        if name == "ETHERNETSNAPVLANSTACKPACKET":
            return EthernetSnapVlanStackPacket(0)
        if name == "ETHERNETSNAPIPV4PACKET":
            return EthernetSnapIpV4Packet()
        if name == "ETHERNETSNAPIPV4TAGGEDPACKET":
            return EthernetSnapIpV4TaggedPacket()
        if name == "ETHERNETSNAPIPV4VLANSTACKPACKET":
            return EthernetSnapIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPTCPIPV4PACKET":
            return EthernetSnapTcpIpV4Packet()
        if name == "ETHERNETSNAPTCPIPV4TAGGEDPACKET":
            return EthernetSnapTcpIpV4TaggedPacket()
        if name == "ETHERNETSNAPTCPIPV4VLANSTACKPACKET":
            return EthernetSnapTcpIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPUDPIPV4PACKET":
            return EthernetSnapUdpIpV4Packet()
        if name == "ETHERNETSNAPUDPIPV4TAGGEDPACKET":
            return EthernetSnapUdpIpV4TaggedPacket()
        if name == "ETHERNETSNAPUDPIPV4VLANSTACKPACKET":
            return EthernetSnapUdpIpV4VlanStackPacket(0)
        if name == "ETHERNETSNAPIPV6PACKET":
            return EthernetSnapIpV6Packet()
        if name == "ETHERNETSNAPIPV6TAGGEDPACKET":
            return EthernetSnapIpV6TaggedPacket()
        if name == "ETHERNETSNAPIPV6VLANSTACKPACKET":
            return EthernetSnapIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPTCPIPV6PACKET":
            return EthernetSnapTcpIpV6Packet()
        if name == "ETHERNETSNAPTCPIPV6TAGGEDPACKET":
            return EthernetSnapTcpIpV6TaggedPacket()
        if name == "ETHERNETSNAPTCPIPV6VLANSTACKPACKET":
            return EthernetSnapTcpIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPUDPIPV6PACKET":
            return EthernetSnapUdpIpV6Packet()
        if name == "ETHERNETSNAPUDPIPV6TAGGEDPACKET":
            return EthernetSnapUdpIpV6TaggedPacket()
        if name == "ETHERNETSNAPUDPIPV6VLANSTACKPACKET":
            return EthernetSnapUdpIpV6VlanStackPacket(0)
        if name == "ETHERNETSNAPLLDPPACKET":
            return EthernetSnapLldpPacket()
        if name == "ETHERNETSNAPLLDPTAGGEDPACKET":
            return EthernetSnapLldpTaggedPacket()
        if name == "ETHERNETSNAPLLDPVLANSTACKPACKET":
            return EthernetSnapLldpVlanStackPacket(0)
        pass

    # EXAMPLE: PacketClassifier.get_packet_from_tags(PacketClassifierConstants.TAG_IPV4)
    # EXAMPLE: PacketClassifier.get_packet_from_tags([PacketClassifierConstants.TAG_IPV4,
    #                                                 PacketClassifierConstants.TAG_TCP])
    @staticmethod
    def get_packet_from_tags(tags):
        # loop through PacketClassifierConstants.ALL_PACKETS
        packets = PacketClassifier.get_all_packet_names_from_tags(tags)
        packet = sorted(packets, key=len)[0]
        return PacketClassifier.get_packet(packet)

    # EXAMPLE: PacketClassifier.get_all_packets_from_tags(PacketClassifierConstants.TAG_IPV4)
    # EXAMPLE: PacketClassifier.get_all_packets_from_tags([PacketClassifierConstants.TAG_IPV4,
    #                                                      PacketClassifierConstants.TAG_TCP])
    @staticmethod
    def get_all_packets_from_tags(tags=None):
        packets = PacketClassifier.get_all_packet_names_from_tags(tags)
        index = 0
        while index < len(packets):
            packets[index] = PacketClassifier.get_packet(packets[index])
            index += 1
        return packets

    @staticmethod
    def get_all_packet_names_from_tags(tags=None):
        if isinstance(tags, str):
            tags = [tags]
        # loop through PacketClassifierConstants.ALL_PACKETS*
        all_packets_to_return = []
        for p in PacketClassifierConstants.ALL_PACKETS:
            if not tags:
                all_packets_to_return.append(p)
            elif PacketClassifier.check_packet_tags(p, tags):
                all_packets_to_return.append(p)
        return all_packets_to_return

    @staticmethod
    def check_packet_tags(packet_name, tags):
        packet_name = packet_name.upper()
        if "LLC" in tags and "SNAP" in tags:
            tags.remove("LLC")
        if isinstance(tags, deque):
            tags = list(tags)
        if isinstance(tags, list):
            for tag in tags:
                if tag.upper() == PacketClassifierConstants.TAG_UNTAGGED:
                    if PacketClassifierConstants.TAG_QTAGGED in packet_name or \
                            PacketClassifierConstants.TAG_VLAN_STACK in packet_name:
                        return False
                elif not tag.upper() in packet_name:
                    return False
        return True

    # EXAMPLE: PacketClassifier.translate_packet(packet, PacketClassifierConstants.ETHERNETSNAPUDPIPV4PACKET)
    @staticmethod
    def translate_packet(source_packet, new_packet_tag):
        new_packet = PacketClassifier.get_packet(new_packet_tag)
        new_packet.clone(source_packet)
        # packet.remove_packet_composite(PacketConstants.PACKET_HEADER_L2_ETHERNET_TAGGED)
        return new_packet

    @staticmethod
    def process_pcap_file(pcap_file):
        with open(pcap_file, mode='rb') as open_file:
            fileContent = open_file.read()
        return PacketClassifier.process_pcap_file_contents(fileContent)

    @staticmethod
    def process_pcap_file_contents(buff, return_list=None):
        # http://www.kroosec.com/2012/10/a-look-at-pcap-file-format.html
        hex_string = ''.join((hex(ord(x))[2:]).zfill(2) for x in buff)
        # starts with d4 c3 b2 a1

        magic_number = AbstractPacket.get_bytes_from_string(4, hex_string)  # a1b2c3d4
        hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
        # the next 4 bytes 02 00 04 00 are the Major version (2 bytes) and Minor Version (2 bytes)
        version = AbstractPacket.get_bytes_from_string(4, hex_string)
        hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
        # next 4 bytes are timezone
        time_zone = AbstractPacket.get_bytes_from_string(8, hex_string)
        hex_string = AbstractPacket.remove_bytes_from_string(8, hex_string)
        # next 4 bytes are the max length
        max_packet_length = AbstractPacket.get_bytes_from_string(4, hex_string)
        hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
        max_packet_length = NumberUtils.little_endian_hex_string_to_int(max_packet_length)
        # The last 4 bytes in the global header specify the Link-Layer Header Type.
        packet_capture_type = AbstractPacket.get_bytes_from_string(4, hex_string)
        hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
        packets = []
        packet_number = 0
        while len(hex_string) > 0:
            packet_number += 1
            # after that there are
            # 4 bytes time captured
            captured_time = AbstractPacket.get_bytes_from_string(4, hex_string)
            hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
            captured_time_micro = AbstractPacket.get_bytes_from_string(4, hex_string)
            hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
            # 4 bytes length in little endian (captured)
            packet_length_captured = AbstractPacket.get_bytes_from_string(4, hex_string)
            hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
            packet_length_captured = NumberUtils.little_endian_hex_string_to_int(packet_length_captured)
            # 4 bytes length in little endian (saved)
            packet_length_saved = AbstractPacket.get_bytes_from_string(4, hex_string)
            hex_string = AbstractPacket.remove_bytes_from_string(4, hex_string)
            packet_length_saved = NumberUtils.little_endian_hex_string_to_int(packet_length_saved)
            packet_data = AbstractPacket.get_bytes_from_string(packet_length_saved, hex_string)
            hex_string = AbstractPacket.remove_bytes_from_string(packet_length_saved, hex_string)
            packet = PacketClassifier.classify_packet_bytes(packet_data)
            if (return_list and packet_number in return_list) or return_list is None:
                packets.append(packet)
            # Logger().log_debug(str(packet_number) + ") " + packet_data)
        return packets

    @staticmethod
    def save_to_pcap_file_contents(packets, pcap_file):
        # http://www.kroosec.com/2012/10/a-look-at-pcap-file-format.html
        hex_string = "d4c3b2a1"  # magic number
        hex_string += "02000400"  # 4 bytes 02 00 04 00 are the Major version (2 bytes) and Minor Version (2 bytes)
        hex_string += "00000000"  # timezone
        hex_string += "00000000"  # timezone micro
        hex_string += "ffff0000"  # max_packet_length (might be 65535)
        hex_string += "01000000"  # link layer type = 1

        packet_number = 0
        while packet_number < len(packets):
            packet = packets[packet_number]
            packet_string = ""
            packet_string += "9549fe57"  # captured time 95 49 fe 57
            packet_string += "cc880320"  # captured time micro cc 88 03 20
            packet_bytes = packet.get_bytes()
            packet_length = int(packet.get_length())
            while (len(packet_bytes) // 2) < packet_length:
                packet_bytes += "00"
            packet_length = NumberUtils.int_to_little_endian_hex_string(packet_length, 4)
            packet_string += packet_length  # packet_length_captured length in little endian (captured)
            packet_string += packet_length  # packet_length_captured length in little endian (saved)
            packet_string += packet_bytes
            hex_string += packet_string
            packet_number += 1
        ret_string = StringUtils.hex_string_to_bytes(hex_string)
        FileUtils.write_str_to_file(pcap_file, ret_string, True)
        # packets = PacketClassifier.process_pcap_file(pcap_file)
        return

    @staticmethod
    def set_default_test_packet_values(packet):
        packet.set_destination_mac("00:33:22:33:44:55")
        packet.set_source_mac("00:33:22:33:44:66")
        tags = packet.get_packet_tags()
        length = 124
        if PacketTagConstants.TAG_QTAGGED in tags or isinstance(packet, TaggedPacketHeader):
            # packet.set_vlan_protocol_id(0x9100)
            packet.set_vlan_id(44)
            packet.set_vlan_tci(3)
        if PacketTagConstants.TAG_ENET2 in tags or isinstance(packet, Ethernet2PacketHeader):
            pass
        if PacketTagConstants.TAG_SNAP in tags or isinstance(packet, SnapPacketHeader):
            assert isinstance(packet, SnapPacketHeader)
            packet.set_snap_ether_type(0x0811)
            packet.set_snap_organization_code(0x02)
            assert isinstance(packet, Ieee802LlcPacketHeader)
            packet.set_llc_control(1)
            packet.set_llc_length(54)
        if isinstance(packet, ArpPacketHeader):
            assert isinstance(packet, ArpPacketHeader)
            packet.set_arp_target_hardware_address("00:55:44:33:22")
            packet.set_arp_target_protocol_address("2.2.12.12")
            packet.set_arp_sender_hardware_address("00:44:33:66:22")
            packet.set_arp_source_protocol_address("1.1.12.12")
            packet.set_arp_operation(2)
        if PacketTagConstants.TAG_IPV4 in tags or isinstance(packet, IpV4PacketHeader):
            packet.set_destination_ip("1.1.1.1")
            packet.set_source_ip("2.2.2.2")
            # packet.set_ip_tos(3)
            packet.set_ip_ttl(250)
            packet.set_ip_protocol(0x44)
            # packet.set_ip_fragment_offset("2")
            # packet.set_ip_flags_dont_frag()
            # packet.set_ip_flags_more_frag()
            # packet.set_ip_options_and_auto_pad("24 34 22")
        if PacketTagConstants.TAG_IPV6 in tags or isinstance(packet, IpV6PacketHeader):
            packet.set_ipv6_destination_address("FF00::dddd")
            packet.set_ipv6_source_address("FF00::eeee")
            # packet.add_ipv6_extension_headers_fragment()
        if PacketTagConstants.TAG_TCP in tags or isinstance(packet, TcpPacketHeader):
            packet.set_destination_port("44")
            packet.set_source_port("33")
            packet.set_data_offset(8)
            packet.set_options_and_auto_pad("24 34 22")
        if PacketTagConstants.TAG_UDP in tags or isinstance(packet, UdpPacketHeader):
            if not isinstance(packet, RadiusPacketHeader) and not isinstance(packet, VxlanPacketHeader):
                packet.set_destination_port("0x66")
                packet.set_source_port("55")
        if PacketTagConstants.TAG_GRE in tags or isinstance(packet, GrePacketHeader):
            assert isinstance(packet, GrePacketHeader)
            if "erspan" not in packet.get_name().lower():
                packet.set_gre_protocol_type(0x6558)
        if isinstance(packet, RadiusPacketHeader):
            assert isinstance(packet, RadiusPacketHeader)
            packet.set_radius_code(0x0b)
            packet.set_radius_id(0x05)
            packet.set_radius_length(109)
            packet.set_radius_authenticator("f050649184625d36f14c9075b7a48b83")
            packet.add_radius_attribute_value_pair_framed_ip_address("FF FF FF FE")
            packet.add_radius_attribute_value_pair_framed_mtu(575)
            packet.add_radius_attribute_value_nas_ip_address("10.0.0.1")
            packet.add_radius_attribute_value_pair_username("John.McGiurk")
            packet.add_radius_attribute_value_pair_reply_message("Hello, John.McGiurk")
            packet.add_radius_attribute_value_pair_eap_message("03010004")
            packet.add_radius_attribute_value_pair_message_authenticator("c6d195032fdc3024077313b231ef1d77")
        if PacketTagConstants.TAG_IPX in tags or isinstance(packet, IpxPacketHeader):
            packet.set_ipx_destination_network("FF FF EE DD")
            packet.set_ipx_destination_node("FF FF EE DD EE DD")
            packet.set_ipx_destination_socket("0xEE ED")
            packet.set_ipx_source_network("FF FF EE FF")
            packet.set_ipx_source_node("FF FF EE DD EE FF")
            packet.set_ipx_source_socket("0xEE EF")
        if isinstance(packet, IcmpPacketHeader):
            assert isinstance(packet, IcmpPacketHeader)
            if isinstance(packet, IpV6PacketHeader):
                packet.set_icmp_type(22)
                packet.set_icmp_code(73)
            else:
                packet.set_icmp_type(0)
                packet.set_icmp_code(0)
            packet.set_icmp_id(4)
            packet.set_icmp_seq(6)
        if isinstance(packet, BpduPacketHeader):
            assert isinstance(packet, BpduPacketHeader)
            packet.set_destination_mac("01:80:C2:00:00:00")
            packet.set_bpdu_protocol_id(0)
            packet.set_bpdu_message_type(0x02)
            packet.set_bpdu_flags(0x7c)
            packet.set_bpdu_root_priority(0)
            packet.set_bpdu_root_mac("00:1f:27:b4:7d:80")
            packet.set_bpdu_cost(0x00030d40)
            packet.set_bpdu_bridge_priority(0x8000)
            packet.set_bpdu_bridge_mac("00:16:46:b5:8c:80")
            packet.set_bpdu_port_id(0x800f)
            packet.set_bpdu_age(1)
            packet.set_bpdu_max_age(20)
            packet.set_bpdu_hello_timer(2)
            packet.set_bpdu_forward_delay(15)
        if isinstance(packet, IgmpPacketHeader):
            assert isinstance(packet, IgmpPacketHeader)
            packet.set_igmp_type(IgmpPacketConstants.IGMP_TYPE_MEMBERSHIP_QUERY)
            packet.set_igmp_groupaddress("224.1.1.1")
        if isinstance(packet, MstpPacketHeader):
            assert isinstance(packet, MstpPacketHeader)
            packet.set_destination_mac("01:00:0C:CC:CC:CD")
            # packet.set_mstp_version_3_length(96)
            packet.set_mstp_version_3_name("Brewery")
            packet.set_mstp_version_3_digest("9357ebb7a8d74dd5fef4f2bab50531aa")
            packet.set_mstp_version_3_cist_bridge_internal_priority(32768)
            packet.set_mstp_version_3_cist_bridge_internal_system_id("00:16:46:b5:8c:80")
            packet.set_mstp_version_3_cist_internal_root_path_cost(0)
            packet.set_mstp_version_3_cist_remaining_hops(20)
            packet.add_mstid_entry()
            packet.set_mstp_version_3_mstid_flags(0x0fc, 1)
            packet.set_mstp_version_3_mstid_priority(0x06, 1)
            packet.set_mstp_version_3_mstid_mstid(0x01, 1)
            packet.set_mstp_version_3_mstid_regional_root("00:1e:f7:05:a8:80", 1)
            packet.set_mstp_version_3_mstid_internal_root_path_cost(0x0, 1)
            packet.set_mstp_version_3_mstid_bridge_identifier_priority(0x06, 1)
            packet.set_mstp_version_3_mstid_port_identifier_priority(0x08, 1)
            packet.set_mstp_version_3_mstid_remaining_hops(20, 1)
            packet.add_mstid_entry()
            packet.set_mstp_version_3_mstid_flags(0x0f8, 2)
            packet.set_mstp_version_3_mstid_priority(0x08, 2)
            packet.set_mstp_version_3_mstid_mstid(0x01, 2)
            packet.set_mstp_version_3_mstid_regional_root("00:16:46:b5:8c:80", 2)
            packet.set_mstp_version_3_mstid_internal_root_path_cost(200000, 2)
            packet.set_mstp_version_3_mstid_bridge_identifier_priority(0x08, 2)
            packet.set_mstp_version_3_mstid_port_identifier_priority(0x08, 2)
            packet.set_mstp_version_3_mstid_remaining_hops(20, 2)
            length += 500
        if isinstance(packet, LldpPacketHeader):
            packet.add_lldp_tlv_chassis_subtype("00:18:ba:98:68:Bf")
            packet.add_lldp_tlv_port_subtype("Fa0/13")
            packet.add_lldp_tlv_time_to_live(120)
            packet.add_lldp_tlv_system_name("S1.cisco.com")
            packet.add_lldp_tlv_system_description("436973636f20494f5320536f6674776172652c20433335363020536f66747761726"
                                                   "5202843333536302d414456495053455256494345534b392d4d292c205665727369"
                                                   "6f6e2031322e322834342953452c2052454c4541534520534f46545741524520286"
                                                   "66331290a436f707972696768742028632920313938362d32303038206279204369"
                                                   "73636f2053797374656d732c20496e632e0a436f6d70696c6564205361742030352"
                                                   "d4a616e2d30382030303a3135206279207765696c6975".decode('hex'))
            packet.add_lldp_tlv_port_description("FastEthernet0/13")
            packet.add_lldp_tlv_capabilities([0x00, 0x14, 0x00, 0x04])
            packet.add_lldp_tlv_ieee_802_1_portvlan("0x0080c2010001")
            packet.add_lldp_tlv_ieee_802_3_mc_phy_config("00120f010300360010")
            packet.add_lldp_tlv_end()
        if isinstance(packet, VlanStackPacketHeader):
            num = packet.get_vlan_num()
            if num == 0:
                # packet.set_vlan_num(random.randint(2,5))
                packet.set_vlan_num(2)
                num = packet.get_vlan_num()
            index = 1
            for index in range(1, num + 1):
                packet.set_vlan_protocol_id(index, "0x9100")
                packet.set_vlan_id(index, 10 + index)
                packet.set_vlan_tci(index, index)
                index += 1
            index += 1
            length += 100

        if isinstance(packet, MplsPacketHeader):
            packet.set_label_num(2)
            packet.set_mpls_bottom_of_label_stack(1, 2)
        if isinstance(packet, VxlanPacketHeader):
            inner_packet = Ethernet2IpV4Packet()
            inner_packet.set_destination_mac("00:11:22:33:44:55")
            inner_packet.set_source_mac("00:11:22:33:44:66")
            inner_packet.set_source_ip("4.5.4.5")
            packet.set_vxlan_inner_packet(inner_packet)
        # packet.configure_packet()
        packet.auto_set_minimum_length()
        length = packet.get_length()
        packet.configure_packet_length_fields(length)
        # packet.set_length(500)


class PacketClassifierConstants(object, metaclass=Singleton):
    def __init__(self):
        super(PacketClassifierConstants, self).__init__()

    # Don't allow values to be updated.
    def __setattr__(self, *_):
        pass

    TAG_TCP = "TCP"
    TAG_UDP = "UDP"
    TAG_VRRP = "VRRP"
    TAG_OSPF = "OSPF"
    TAG_RIP = "RIP"
    TAG_IPV4 = "IPV4"
    TAG_IPV6 = "IPV6"
    TAG_MPLS = "MPLS"
    TAG_MLD = "MLD"
    TAG_MLD_V2 = "MLDV2"
    TAG_DVMRP = "DVMRP"
    TAG_BOOTP = "BOOTP"
    TAG_DHCP = "DHCP"
    TAG_PIM_JOIN_PRUNE = "PIMJOINPRUNE"
    TAG_PIM_BOOTSTRAP = "PIMBOOTSTRAP"
    TAG_PIM_ASSERT = "PIMASSERT"
    TAG_PIM_CANIDATE = "PIMCANIDATE"
    TAG_PIM_GRAFT_ACK_MESSAGE = "PIMGRAFTACKMESSAGE"
    TAG_PIM_GRAFT_MESSAGE = "PIMGRAFTMESSAGE"
    TAG_PIM_REGISTER_STOP_MESSAGE = "PIMREGISTERSTOP"
    TAG_PIM_REGISTER_MESSAGE = "PIMREGISTER"
    TAG_PIM_HELLO = "PIMHELLO"
    TAG_PIM_V2 = "PIMV2"
    TAG_DNS = "DNS"
    TAG_IPX = "IPX"
    TAG_UNTAGGED = "UNTAGGED"
    TAG_QTAGGED = "TAGGED"
    TAG_VLAN_STACK = "VLANSTACK"
    TAG_VXLAN = "VXLAN"
    TAG_ARP = "ARP"
    TAG_RARP = "RARP"
    TAG_ICMP = "ICMP"
    TAG_ICMP_V6 = "ICMPV6"
    TAG_IGMP = "IGMP"
    TAG_SAP = "SAP"
    TAG_SNAP = "SNAP"
    TAG_ENET2 = "Ethernet2"
    TAG_BPDU = "BPDU"
    TAG_SPANNING_TREE = "SPANNINGTREE"
    TAG_RAW = "RAW"
    TAG_ETHER_ENCAP = "ENCAPSULATED"
    TAG_IPV4_IPV4_ENCAP = "IPV4IPV4ENCAPSULATED"
    TAG_IPV4_IPV6_ENCAP = "IPV4IPV6ENCAPSULATED"
    TAG_IPV6_ENCAP = "IPV6ENCAPSULATED"
    TAG_PAUSE_CONTROL = "PAUSECONTROL"
    TAG_NEIGHBOR_DISCOVERY = "NEIGHBORDISCOVERY"
    TAG_LLDP = "LLDP"

    # ## constants ###
    ETHER_TYPE_DVR = "8101"
    ETHER_TYPE_IPV6 = "86DD"
    ETHER_TYPE_IPV4 = "0800"

    # regenerate with Utils/PacketTypeSet.py
    ETHERNET2ARPPACKET = "ETHERNET2ARPPACKET"
    ETHERNET2ARPTAGGEDPACKET = "ETHERNET2ARPTAGGEDPACKET"
    ETHERNET2ARPVLANSTACKPACKET = "ETHERNET2ARPVLANSTACKPACKET"
    ETHERNET2MPLSPACKET = "ETHERNET2MPLSPACKET"
    ETHERNET2MPLSTAGGEDPACKET = "ETHERNET2MPLSTAGGEDPACKET"
    ETHERNET2MPLSVLANSTACKPACKET = "ETHERNET2MPLSVLANSTACKPACKET"
    ETHERNET2PACKET = "ETHERNET2PACKET"
    ETHERNET2TAGGEDPACKET = "ETHERNET2TAGGEDPACKET"
    ETHERNET2VLANSTACKPACKET = "ETHERNET2VLANSTACKPACKET"
    ETHERNETPACKET = "ETHERNETPACKET"
    ETHERNETTAGGEDPACKET = "ETHERNETTAGGEDPACKET"
    ETHERNETVLANSTACKPACKET = "ETHERNETVLANSTACKPACKET"
    IEEE802LLCPACKET = "IEEE802LLCPACKET"
    IEEE802LLCTAGGEDPACKET = "IEEE802LLCTAGGEDPACKET"
    IEEE802LLCVLANSTACKPACKET = "IEEE802LLCVLANSTACKPACKET"
    SAPPACKET = "SAPPACKET"
    SAPTAGGEDPACKET = "SAPTAGGEDPACKET"
    SAPVLANSTACKPACKET = "SAPVLANSTACKPACKET"
    ETHERNET2MPLSENCAPSULATEDPACKET = "ETHERNET2MPLSENCAPSULATEDPACKET"
    ETHERNET2MPLSENCAPSULATEDTAGGEDPACKET = "ETHERNET2MPLSENCAPSULATEDTAGGEDPACKET"
    ETHERNET2MPLSENCAPSULATEDVLANSTACKPACKET = "ETHERNET2MPLSENCAPSULATEDVLANSTACKPACKET"
    ETHERNET2PROVIDERBACKBONEBRIDGEPACKET = "ETHERNET2PROVIDERBACKBONEBRIDGEPACKET"
    ETHERNET2PROVIDERBACKBONEBRIDGETAGGEDPACKET = "ETHERNET2PROVIDERBACKBONEBRIDGETAGGEDPACKET"
    ETHERNET2PROVIDERBACKBONEBRIDGEVLANSTACKPACKET = "ETHERNET2PROVIDERBACKBONEBRIDGEVLANSTACKPACKET"
    ETHERNET2ERSPANGREIPV4PACKET = "ETHERNET2ERSPANGREIPV4PACKET"
    ETHERNET2ERSPANGREIPV4TAGGEDPACKET = "ETHERNET2ERSPANGREIPV4TAGGEDPACKET"
    ETHERNET2ERSPANGREIPV4VLANSTACKPACKET = "ETHERNET2ERSPANGREIPV4VLANSTACKPACKET"
    ETHERNET2ERSPANIIIGREIPV4PACKET = "ETHERNET2ERSPANIIIGREIPV4PACKET"
    ETHERNET2ERSPANIIIGREIPV4TAGGEDPACKET = "ETHERNET2ERSPANIIIGREIPV4TAGGEDPACKET"
    ETHERNET2ERSPANIIIGREIPV4VLANSTACKPACKET = "ETHERNET2ERSPANIIIGREIPV4VLANSTACKPACKET"
    ETHERNET2GREIPV4PACKET = "ETHERNET2GREIPV4PACKET"
    ETHERNET2GREIPV4TAGGEDPACKET = "ETHERNET2GREIPV4TAGGEDPACKET"
    ETHERNET2GREIPV4VLANSTACKPACKET = "ETHERNET2GREIPV4VLANSTACKPACKET"
    ETHERNET2IPENCAPSULATEDIPV4PACKET = "ETHERNET2IPENCAPSULATEDIPV4PACKET"
    ETHERNET2IPENCAPSULATEDIPV4TAGGEDPACKET = "ETHERNET2IPENCAPSULATEDIPV4TAGGEDPACKET"
    ETHERNET2IPENCAPSULATEDIPV4VLANSTACKPACKET = "ETHERNET2IPENCAPSULATEDIPV4VLANSTACKPACKET"
    ETHERNET2VXLANUDPIPV4PACKET = "ETHERNET2VXLANUDPIPV4PACKET"
    ETHERNET2VXLANUDPIPV4TAGGEDPACKET = "ETHERNET2VXLANUDPIPV4TAGGEDPACKET"
    ETHERNET2VXLANUDPIPV4VLANSTACKPACKET = "ETHERNET2VXLANUDPIPV4VLANSTACKPACKET"
    ETHERNETSNAPERSPANGREIPV4PACKET = "ETHERNETSNAPERSPANGREIPV4PACKET"
    ETHERNETSNAPERSPANGREIPV4TAGGEDPACKET = "ETHERNETSNAPERSPANGREIPV4TAGGEDPACKET"
    ETHERNETSNAPERSPANGREIPV4VLANSTACKPACKET = "ETHERNETSNAPERSPANGREIPV4VLANSTACKPACKET"
    ETHERNETSNAPERSPANIIIGREIPV4PACKET = "ETHERNETSNAPERSPANIIIGREIPV4PACKET"
    ETHERNETSNAPERSPANIIIGREIPV4TAGGEDPACKET = "ETHERNETSNAPERSPANIIIGREIPV4TAGGEDPACKET"
    ETHERNETSNAPERSPANIIIGREIPV4VLANSTACKPACKET = "ETHERNETSNAPERSPANIIIGREIPV4VLANSTACKPACKET"
    ETHERNETSNAPGREIPV4PACKET = "ETHERNETSNAPGREIPV4PACKET"
    ETHERNETSNAPGREIPV4TAGGEDPACKET = "ETHERNETSNAPGREIPV4TAGGEDPACKET"
    ETHERNETSNAPGREIPV4VLANSTACKPACKET = "ETHERNETSNAPGREIPV4VLANSTACKPACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV4PACKET = "ETHERNETSNAPIPENCAPSULATEDIPV4PACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV4TAGGEDPACKET = "ETHERNETSNAPIPENCAPSULATEDIPV4TAGGEDPACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV4VLANSTACKPACKET = "ETHERNETSNAPIPENCAPSULATEDIPV4VLANSTACKPACKET"
    ETHERNET2ERSPANGREIPV6PACKET = "ETHERNET2ERSPANGREIPV6PACKET"
    ETHERNET2ERSPANGREIPV6TAGGEDPACKET = "ETHERNET2ERSPANGREIPV6TAGGEDPACKET"
    ETHERNET2ERSPANGREIPV6VLANSTACKPACKET = "ETHERNET2ERSPANGREIPV6VLANSTACKPACKET"
    ETHERNET2ERSPANIIIGREIPV6PACKET = "ETHERNET2ERSPANIIIGREIPV6PACKET"
    ETHERNET2ERSPANIIIGREIPV6TAGGEDPACKET = "ETHERNET2ERSPANIIIGREIPV6TAGGEDPACKET"
    ETHERNET2ERSPANIIIGREIPV6VLANSTACKPACKET = "ETHERNET2ERSPANIIIGREIPV6VLANSTACKPACKET"
    ETHERNET2GREIPV6PACKET = "ETHERNET2GREIPV6PACKET"
    ETHERNET2GREIPV6TAGGEDPACKET = "ETHERNET2GREIPV6TAGGEDPACKET"
    ETHERNET2GREIPV6VLANSTACKPACKET = "ETHERNET2GREIPV6VLANSTACKPACKET"
    ETHERNET2IPENCAPSULATEDIPV6PACKET = "ETHERNET2IPENCAPSULATEDIPV6PACKET"
    ETHERNET2IPENCAPSULATEDIPV6TAGGEDPACKET = "ETHERNET2IPENCAPSULATEDIPV6TAGGEDPACKET"
    ETHERNET2IPENCAPSULATEDIPV6VLANSTACKPACKET = "ETHERNET2IPENCAPSULATEDIPV6VLANSTACKPACKET"
    ETHERNET2VXLANUDPIPV6PACKET = "ETHERNET2VXLANUDPIPV6PACKET"
    ETHERNET2VXLANUDPIPV6TAGGEDPACKET = "ETHERNET2VXLANUDPIPV6TAGGEDPACKET"
    ETHERNET2VXLANUDPIPV6VLANSTACKPACKET = "ETHERNET2VXLANUDPIPV6VLANSTACKPACKET"
    ETHERNETSNAPERSPANGREIPV6PACKET = "ETHERNETSNAPERSPANGREIPV6PACKET"
    ETHERNETSNAPERSPANGREIPV6TAGGEDPACKET = "ETHERNETSNAPERSPANGREIPV6TAGGEDPACKET"
    ETHERNETSNAPERSPANGREIPV6VLANSTACKPACKET = "ETHERNETSNAPERSPANGREIPV6VLANSTACKPACKET"
    ETHERNETSNAPERSPANIIIGREIPV6PACKET = "ETHERNETSNAPERSPANIIIGREIPV6PACKET"
    ETHERNETSNAPERSPANIIIGREIPV6TAGGEDPACKET = "ETHERNETSNAPERSPANIIIGREIPV6TAGGEDPACKET"
    ETHERNETSNAPERSPANIIIGREIPV6VLANSTACKPACKET = "ETHERNETSNAPERSPANIIIGREIPV6VLANSTACKPACKET"
    ETHERNETSNAPGREIPV6PACKET = "ETHERNETSNAPGREIPV6PACKET"
    ETHERNETSNAPGREIPV6TAGGEDPACKET = "ETHERNETSNAPGREIPV6TAGGEDPACKET"
    ETHERNETSNAPGREIPV6VLANSTACKPACKET = "ETHERNETSNAPGREIPV6VLANSTACKPACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV6PACKET = "ETHERNETSNAPIPENCAPSULATEDIPV6PACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV6TAGGEDPACKET = "ETHERNETSNAPIPENCAPSULATEDIPV6TAGGEDPACKET"
    ETHERNETSNAPIPENCAPSULATEDIPV6VLANSTACKPACKET = "ETHERNETSNAPIPENCAPSULATEDIPV6VLANSTACKPACKET"
    ETHERNET2BOOTPUDPIPV4PACKET = "ETHERNET2BOOTPUDPIPV4PACKET"
    ETHERNET2BOOTPUDPIPV4TAGGEDPACKET = "ETHERNET2BOOTPUDPIPV4TAGGEDPACKET"
    ETHERNET2BOOTPUDPIPV4VLANSTACKPACKET = "ETHERNET2BOOTPUDPIPV4VLANSTACKPACKET"
    ETHERNET2DBDESCRIPTIONOSPFIPV4PACKET = "ETHERNET2DBDESCRIPTIONOSPFIPV4PACKET"
    ETHERNET2DBDESCRIPTIONOSPFIPV4TAGGEDPACKET = "ETHERNET2DBDESCRIPTIONOSPFIPV4TAGGEDPACKET"
    ETHERNET2DBDESCRIPTIONOSPFIPV4VLANSTACKPACKET = "ETHERNET2DBDESCRIPTIONOSPFIPV4VLANSTACKPACKET"
    ETHERNET2DNSTCPIPV4PACKET = "ETHERNET2DNSTCPIPV4PACKET"
    ETHERNET2DNSTCPIPV4TAGGEDPACKET = "ETHERNET2DNSTCPIPV4TAGGEDPACKET"
    ETHERNET2DNSTCPIPV4VLANSTACKPACKET = "ETHERNET2DNSTCPIPV4VLANSTACKPACKET"
    ETHERNET2DNSUDPIPV4PACKET = "ETHERNET2DNSUDPIPV4PACKET"
    ETHERNET2DNSUDPIPV4TAGGEDPACKET = "ETHERNET2DNSUDPIPV4TAGGEDPACKET"
    ETHERNET2DNSUDPIPV4VLANSTACKPACKET = "ETHERNET2DNSUDPIPV4VLANSTACKPACKET"
    ETHERNET2HELLOOSPFIPV4PACKET = "ETHERNET2HELLOOSPFIPV4PACKET"
    ETHERNET2HELLOOSPFIPV4TAGGEDPACKET = "ETHERNET2HELLOOSPFIPV4TAGGEDPACKET"
    ETHERNET2HELLOOSPFIPV4VLANSTACKPACKET = "ETHERNET2HELLOOSPFIPV4VLANSTACKPACKET"
    ETHERNET2ICMPIPV4MPLSPACKET = "ETHERNET2ICMPIPV4MPLSPACKET"
    ETHERNET2ICMPIPV4MPLSTAGGEDPACKET = "ETHERNET2ICMPIPV4MPLSTAGGEDPACKET"
    ETHERNET2ICMPIPV4MPLSVLANSTACKPACKET = "ETHERNET2ICMPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2ICMPIPV4PACKET = "ETHERNET2ICMPIPV4PACKET"
    ETHERNET2ICMPIPV4TAGGEDPACKET = "ETHERNET2ICMPIPV4TAGGEDPACKET"
    ETHERNET2ICMPIPV4VLANSTACKPACKET = "ETHERNET2ICMPIPV4VLANSTACKPACKET"
    ETHERNET2IGMPIPV4MPLSPACKET = "ETHERNET2IGMPIPV4MPLSPACKET"
    ETHERNET2IGMPIPV4MPLSTAGGEDPACKET = "ETHERNET2IGMPIPV4MPLSTAGGEDPACKET"
    ETHERNET2IGMPIPV4MPLSVLANSTACKPACKET = "ETHERNET2IGMPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2IGMPIPV4PACKET = "ETHERNET2IGMPIPV4PACKET"
    ETHERNET2IGMPIPV4TAGGEDPACKET = "ETHERNET2IGMPIPV4TAGGEDPACKET"
    ETHERNET2IGMPIPV4VLANSTACKPACKET = "ETHERNET2IGMPIPV4VLANSTACKPACKET"
    ETHERNET2IPV4MPLSPACKET = "ETHERNET2IPV4MPLSPACKET"
    ETHERNET2IPV4MPLSTAGGEDPACKET = "ETHERNET2IPV4MPLSTAGGEDPACKET"
    ETHERNET2IPV4MPLSVLANSTACKPACKET = "ETHERNET2IPV4MPLSVLANSTACKPACKET"
    ETHERNET2IPV4PACKET = "ETHERNET2IPV4PACKET"
    ETHERNET2IPV4TAGGEDPACKET = "ETHERNET2IPV4TAGGEDPACKET"
    ETHERNET2IPV4VLANSTACKPACKET = "ETHERNET2IPV4VLANSTACKPACKET"
    ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4PACKET = "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4PACKET"
    ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4TAGGEDPACKET = "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4TAGGEDPACKET"
    ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4VLANSTACKPACKET = "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4VLANSTACKPACKET"
    ETHERNET2LINKSTATEREQUESTOSPFIPV4PACKET = "ETHERNET2LINKSTATEREQUESTOSPFIPV4PACKET"
    ETHERNET2LINKSTATEREQUESTOSPFIPV4TAGGEDPACKET = "ETHERNET2LINKSTATEREQUESTOSPFIPV4TAGGEDPACKET"
    ETHERNET2LINKSTATEREQUESTOSPFIPV4VLANSTACKPACKET = "ETHERNET2LINKSTATEREQUESTOSPFIPV4VLANSTACKPACKET"
    ETHERNET2LINKSTATEUPDATEOSPFIPV4PACKET = "ETHERNET2LINKSTATEUPDATEOSPFIPV4PACKET"
    ETHERNET2LINKSTATEUPDATEOSPFIPV4TAGGEDPACKET = "ETHERNET2LINKSTATEUPDATEOSPFIPV4TAGGEDPACKET"
    ETHERNET2LINKSTATEUPDATEOSPFIPV4VLANSTACKPACKET = "ETHERNET2LINKSTATEUPDATEOSPFIPV4VLANSTACKPACKET"
    ETHERNET2OSPFIPV4PACKET = "ETHERNET2OSPFIPV4PACKET"
    ETHERNET2OSPFIPV4TAGGEDPACKET = "ETHERNET2OSPFIPV4TAGGEDPACKET"
    ETHERNET2OSPFIPV4VLANSTACKPACKET = "ETHERNET2OSPFIPV4VLANSTACKPACKET"
    ETHERNET2PIMIPV4PACKET = "ETHERNET2PIMIPV4PACKET"
    ETHERNET2PIMIPV4TAGGEDPACKET = "ETHERNET2PIMIPV4TAGGEDPACKET"
    ETHERNET2PIMIPV4VLANSTACKPACKET = "ETHERNET2PIMIPV4VLANSTACKPACKET"
    ETHERNET2RADIUSUDPIPV4PACKET = "ETHERNET2RADIUSUDPIPV4PACKET"
    ETHERNET2RADIUSUDPIPV4TAGGEDPACKET = "ETHERNET2RADIUSUDPIPV4TAGGEDPACKET"
    ETHERNET2RADIUSUDPIPV4VLANSTACKPACKET = "ETHERNET2RADIUSUDPIPV4VLANSTACKPACKET"
    ETHERNET2RIPUDPIPV4MPLSPACKET = "ETHERNET2RIPUDPIPV4MPLSPACKET"
    ETHERNET2RIPUDPIPV4MPLSTAGGEDPACKET = "ETHERNET2RIPUDPIPV4MPLSTAGGEDPACKET"
    ETHERNET2RIPUDPIPV4MPLSVLANSTACKPACKET = "ETHERNET2RIPUDPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2RIPUDPIPV4PACKET = "ETHERNET2RIPUDPIPV4PACKET"
    ETHERNET2RIPUDPIPV4TAGGEDPACKET = "ETHERNET2RIPUDPIPV4TAGGEDPACKET"
    ETHERNET2RIPUDPIPV4VLANSTACKPACKET = "ETHERNET2RIPUDPIPV4VLANSTACKPACKET"
    ETHERNET2SYSLOGUDPIPV4PACKET = "ETHERNET2SYSLOGUDPIPV4PACKET"
    ETHERNET2SYSLOGUDPIPV4TAGGEDPACKET = "ETHERNET2SYSLOGUDPIPV4TAGGEDPACKET"
    ETHERNET2SYSLOGUDPIPV4VLANSTACKPACKET = "ETHERNET2SYSLOGUDPIPV4VLANSTACKPACKET"
    ETHERNET2TCPIPV4MPLSPACKET = "ETHERNET2TCPIPV4MPLSPACKET"
    ETHERNET2TCPIPV4MPLSTAGGEDPACKET = "ETHERNET2TCPIPV4MPLSTAGGEDPACKET"
    ETHERNET2TCPIPV4MPLSVLANSTACKPACKET = "ETHERNET2TCPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2TCPIPV4PACKET = "ETHERNET2TCPIPV4PACKET"
    ETHERNET2TCPIPV4TAGGEDPACKET = "ETHERNET2TCPIPV4TAGGEDPACKET"
    ETHERNET2TCPIPV4VLANSTACKPACKET = "ETHERNET2TCPIPV4VLANSTACKPACKET"
    ETHERNET2UDPIPV4MPLSPACKET = "ETHERNET2UDPIPV4MPLSPACKET"
    ETHERNET2UDPIPV4MPLSTAGGEDPACKET = "ETHERNET2UDPIPV4MPLSTAGGEDPACKET"
    ETHERNET2UDPIPV4MPLSVLANSTACKPACKET = "ETHERNET2UDPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2UDPIPV4PACKET = "ETHERNET2UDPIPV4PACKET"
    ETHERNET2UDPIPV4TAGGEDPACKET = "ETHERNET2UDPIPV4TAGGEDPACKET"
    ETHERNET2UDPIPV4VLANSTACKPACKET = "ETHERNET2UDPIPV4VLANSTACKPACKET"
    ETHERNET2VRRPIPV4MPLSPACKET = "ETHERNET2VRRPIPV4MPLSPACKET"
    ETHERNET2VRRPIPV4MPLSTAGGEDPACKET = "ETHERNET2VRRPIPV4MPLSTAGGEDPACKET"
    ETHERNET2VRRPIPV4MPLSVLANSTACKPACKET = "ETHERNET2VRRPIPV4MPLSVLANSTACKPACKET"
    ETHERNET2VRRPIPV4PACKET = "ETHERNET2VRRPIPV4PACKET"
    ETHERNET2VRRPIPV4TAGGEDPACKET = "ETHERNET2VRRPIPV4TAGGEDPACKET"
    ETHERNET2VRRPIPV4VLANSTACKPACKET = "ETHERNET2VRRPIPV4VLANSTACKPACKET"
    ETHERNET2BGPTCPIPV4PACKET = "ETHERNET2BGPTCPIPV4PACKET"
    ETHERNET2BGPTCPIPV4TAGGEDPACKET = "ETHERNET2BGPTCPIPV4TAGGEDPACKET"
    ETHERNET2BGPTCPIPV4VLANSTACKPACKET = "ETHERNET2BGPTCPIPV4VLANSTACKPACKET"
    ETHERNET2DNSTCPIPV6PACKET = "ETHERNET2DNSTCPIPV6PACKET"
    ETHERNET2DNSTCPIPV6TAGGEDPACKET = "ETHERNET2DNSTCPIPV6TAGGEDPACKET"
    ETHERNET2DNSTCPIPV6VLANSTACKPACKET = "ETHERNET2DNSTCPIPV6VLANSTACKPACKET"
    ETHERNET2DNSUDPIPV6PACKET = "ETHERNET2DNSUDPIPV6PACKET"
    ETHERNET2DNSUDPIPV6TAGGEDPACKET = "ETHERNET2DNSUDPIPV6TAGGEDPACKET"
    ETHERNET2DNSUDPIPV6VLANSTACKPACKET = "ETHERNET2DNSUDPIPV6VLANSTACKPACKET"
    ETHERNET2ICMPV6IPV6MPLSPACKET = "ETHERNET2ICMPV6IPV6MPLSPACKET"
    ETHERNET2ICMPV6IPV6MPLSTAGGEDPACKET = "ETHERNET2ICMPV6IPV6MPLSTAGGEDPACKET"
    ETHERNET2ICMPV6IPV6MPLSVLANSTACKPACKET = "ETHERNET2ICMPV6IPV6MPLSVLANSTACKPACKET"
    ETHERNET2ICMPV6IPV6PACKET = "ETHERNET2ICMPV6IPV6PACKET"
    ETHERNET2ICMPV6IPV6TAGGEDPACKET = "ETHERNET2ICMPV6IPV6TAGGEDPACKET"
    ETHERNET2ICMPV6IPV6VLANSTACKPACKET = "ETHERNET2ICMPV6IPV6VLANSTACKPACKET"
    ETHERNET2IPV6MPLSPACKET = "ETHERNET2IPV6MPLSPACKET"
    ETHERNET2IPV6MPLSTAGGEDPACKET = "ETHERNET2IPV6MPLSTAGGEDPACKET"
    ETHERNET2IPV6MPLSVLANSTACKPACKET = "ETHERNET2IPV6MPLSVLANSTACKPACKET"
    ETHERNET2IPV6PACKET = "ETHERNET2IPV6PACKET"
    ETHERNET2IPV6TAGGEDPACKET = "ETHERNET2IPV6TAGGEDPACKET"
    ETHERNET2IPV6VLANSTACKPACKET = "ETHERNET2IPV6VLANSTACKPACKET"
    ETHERNET2PIMIPV6PACKET = "ETHERNET2PIMIPV6PACKET"
    ETHERNET2PIMIPV6TAGGEDPACKET = "ETHERNET2PIMIPV6TAGGEDPACKET"
    ETHERNET2PIMIPV6VLANSTACKPACKET = "ETHERNET2PIMIPV6VLANSTACKPACKET"
    ETHERNET2RADIUSUDPIPV6PACKET = "ETHERNET2RADIUSUDPIPV6PACKET"
    ETHERNET2RADIUSUDPIPV6TAGGEDPACKET = "ETHERNET2RADIUSUDPIPV6TAGGEDPACKET"
    ETHERNET2RADIUSUDPIPV6VLANSTACKPACKET = "ETHERNET2RADIUSUDPIPV6VLANSTACKPACKET"
    ETHERNET2RIPNGUDPIPV6MPLSPACKET = "ETHERNET2RIPNGUDPIPV6MPLSPACKET"
    ETHERNET2RIPNGUDPIPV6MPLSTAGGEDPACKET = "ETHERNET2RIPNGUDPIPV6MPLSTAGGEDPACKET"
    ETHERNET2RIPNGUDPIPV6MPLSVLANSTACKPACKET = "ETHERNET2RIPNGUDPIPV6MPLSVLANSTACKPACKET"
    ETHERNET2RIPNGUDPIPV6PACKET = "ETHERNET2RIPNGUDPIPV6PACKET"
    ETHERNET2RIPNGUDPIPV6TAGGEDPACKET = "ETHERNET2RIPNGUDPIPV6TAGGEDPACKET"
    ETHERNET2RIPNGUDPIPV6VLANSTACKPACKET = "ETHERNET2RIPNGUDPIPV6VLANSTACKPACKET"
    ETHERNET2SYSLOGUDPIPV6PACKET = "ETHERNET2SYSLOGUDPIPV6PACKET"
    ETHERNET2SYSLOGUDPIPV6TAGGEDPACKET = "ETHERNET2SYSLOGUDPIPV6TAGGEDPACKET"
    ETHERNET2SYSLOGUDPIPV6VLANSTACKPACKET = "ETHERNET2SYSLOGUDPIPV6VLANSTACKPACKET"
    ETHERNET2TCPIPV6MPLSPACKET = "ETHERNET2TCPIPV6MPLSPACKET"
    ETHERNET2TCPIPV6MPLSTAGGEDPACKET = "ETHERNET2TCPIPV6MPLSTAGGEDPACKET"
    ETHERNET2TCPIPV6MPLSVLANSTACKPACKET = "ETHERNET2TCPIPV6MPLSVLANSTACKPACKET"
    ETHERNET2TCPIPV6PACKET = "ETHERNET2TCPIPV6PACKET"
    ETHERNET2TCPIPV6TAGGEDPACKET = "ETHERNET2TCPIPV6TAGGEDPACKET"
    ETHERNET2TCPIPV6VLANSTACKPACKET = "ETHERNET2TCPIPV6VLANSTACKPACKET"
    ETHERNET2UDPIPV6MPLSPACKET = "ETHERNET2UDPIPV6MPLSPACKET"
    ETHERNET2UDPIPV6MPLSTAGGEDPACKET = "ETHERNET2UDPIPV6MPLSTAGGEDPACKET"
    ETHERNET2UDPIPV6MPLSVLANSTACKPACKET = "ETHERNET2UDPIPV6MPLSVLANSTACKPACKET"
    ETHERNET2UDPIPV6PACKET = "ETHERNET2UDPIPV6PACKET"
    ETHERNET2UDPIPV6TAGGEDPACKET = "ETHERNET2UDPIPV6TAGGEDPACKET"
    ETHERNET2UDPIPV6VLANSTACKPACKET = "ETHERNET2UDPIPV6VLANSTACKPACKET"
    ETHERNET2VRRPIPV6MPLSPACKET = "ETHERNET2VRRPIPV6MPLSPACKET"
    ETHERNET2VRRPIPV6MPLSTAGGEDPACKET = "ETHERNET2VRRPIPV6MPLSTAGGEDPACKET"
    ETHERNET2VRRPIPV6MPLSVLANSTACKPACKET = "ETHERNET2VRRPIPV6MPLSVLANSTACKPACKET"
    ETHERNET2VRRPIPV6PACKET = "ETHERNET2VRRPIPV6PACKET"
    ETHERNET2VRRPIPV6TAGGEDPACKET = "ETHERNET2VRRPIPV6TAGGEDPACKET"
    ETHERNET2VRRPIPV6VLANSTACKPACKET = "ETHERNET2VRRPIPV6VLANSTACKPACKET"
    ETHERNET2BGPTCPIPV6PACKET = "ETHERNET2BGPTCPIPV6PACKET"
    ETHERNET2BGPTCPIPV6TAGGEDPACKET = "ETHERNET2BGPTCPIPV6TAGGEDPACKET"
    ETHERNET2BGPTCPIPV6VLANSTACKPACKET = "ETHERNET2BGPTCPIPV6VLANSTACKPACKET"
    IEEE802_2IPXPACKET = "IEEE802_2IPXPACKET"
    IEEE802_2IPXTAGGEDPACKET = "IEEE802_2IPXTAGGEDPACKET"
    IEEE802_2IPXVLANSTACKPACKET = "IEEE802_2IPXVLANSTACKPACKET"
    ETHERNET2CSNPDBSYNCDVRPACKET = "ETHERNET2CSNPDBSYNCDVRPACKET"
    ETHERNET2CSNPDBSYNCDVRTAGGEDPACKET = "ETHERNET2CSNPDBSYNCDVRTAGGEDPACKET"
    ETHERNET2CSNPDBSYNCDVRVLANSTACKPACKET = "ETHERNET2CSNPDBSYNCDVRVLANSTACKPACKET"
    ETHERNET2DBPDBSYNCDVRPACKET = "ETHERNET2DBPDBSYNCDVRPACKET"
    ETHERNET2DBPDBSYNCDVRTAGGEDPACKET = "ETHERNET2DBPDBSYNCDVRTAGGEDPACKET"
    ETHERNET2DBPDBSYNCDVRVLANSTACKPACKET = "ETHERNET2DBPDBSYNCDVRVLANSTACKPACKET"
    ETHERNET2DBSYNCDVRPACKET = "ETHERNET2DBSYNCDVRPACKET"
    ETHERNET2DBSYNCDVRTAGGEDPACKET = "ETHERNET2DBSYNCDVRTAGGEDPACKET"
    ETHERNET2DBSYNCDVRVLANSTACKPACKET = "ETHERNET2DBSYNCDVRVLANSTACKPACKET"
    ETHERNET2LLDPPACKET = "ETHERNET2LLDPPACKET"
    ETHERNET2LLDPTAGGEDPACKET = "ETHERNET2LLDPTAGGEDPACKET"
    ETHERNET2LLDPVLANSTACKPACKET = "ETHERNET2LLDPVLANSTACKPACKET"
    SAPBPDUPACKET = "SAPBPDUPACKET"
    SAPBPDUTAGGEDPACKET = "SAPBPDUTAGGEDPACKET"
    SAPBPDUVLANSTACKPACKET = "SAPBPDUVLANSTACKPACKET"
    SAPMSTPSPANNINGTREEBPDUPACKET = "SAPMSTPSPANNINGTREEBPDUPACKET"
    SAPMSTPSPANNINGTREEBPDUTAGGEDPACKET = "SAPMSTPSPANNINGTREEBPDUTAGGEDPACKET"
    SAPMSTPSPANNINGTREEBPDUVLANSTACKPACKET = "SAPMSTPSPANNINGTREEBPDUVLANSTACKPACKET"
    SAPRSTPBPDUPACKET = "SAPRSTPBPDUPACKET"
    SAPRSTPBPDUTAGGEDPACKET = "SAPRSTPBPDUTAGGEDPACKET"
    SAPRSTPBPDUVLANSTACKPACKET = "SAPRSTPBPDUVLANSTACKPACKET"
    SAPSPANNINGTREEBPDUPACKET = "SAPSPANNINGTREEBPDUPACKET"
    SAPSPANNINGTREEBPDUTAGGEDPACKET = "SAPSPANNINGTREEBPDUTAGGEDPACKET"
    SAPSPANNINGTREEBPDUVLANSTACKPACKET = "SAPSPANNINGTREEBPDUVLANSTACKPACKET"
    SAPCSNPISISPACKET = "SAPCSNPISISPACKET"
    SAPCSNPISISTAGGEDPACKET = "SAPCSNPISISTAGGEDPACKET"
    SAPCSNPISISVLANSTACKPACKET = "SAPCSNPISISVLANSTACKPACKET"
    SAPHELLOPDUISISPACKET = "SAPHELLOPDUISISPACKET"
    SAPHELLOPDUISISTAGGEDPACKET = "SAPHELLOPDUISISTAGGEDPACKET"
    SAPHELLOPDUISISVLANSTACKPACKET = "SAPHELLOPDUISISVLANSTACKPACKET"
    SAPISISPACKET = "SAPISISPACKET"
    SAPISISTAGGEDPACKET = "SAPISISTAGGEDPACKET"
    SAPISISVLANSTACKPACKET = "SAPISISVLANSTACKPACKET"
    SAPLSPISISPACKET = "SAPLSPISISPACKET"
    SAPLSPISISTAGGEDPACKET = "SAPLSPISISTAGGEDPACKET"
    SAPLSPISISVLANSTACKPACKET = "SAPLSPISISVLANSTACKPACKET"
    SAPPSNPISISPACKET = "SAPPSNPISISPACKET"
    SAPPSNPISISTAGGEDPACKET = "SAPPSNPISISTAGGEDPACKET"
    SAPPSNPISISVLANSTACKPACKET = "SAPPSNPISISVLANSTACKPACKET"
    ETHERNETSNAPPACKET = "ETHERNETSNAPPACKET"
    ETHERNETSNAPTAGGEDPACKET = "ETHERNETSNAPTAGGEDPACKET"
    ETHERNETSNAPVLANSTACKPACKET = "ETHERNETSNAPVLANSTACKPACKET"
    ETHERNETSNAPIPV4PACKET = "ETHERNETSNAPIPV4PACKET"
    ETHERNETSNAPIPV4TAGGEDPACKET = "ETHERNETSNAPIPV4TAGGEDPACKET"
    ETHERNETSNAPIPV4VLANSTACKPACKET = "ETHERNETSNAPIPV4VLANSTACKPACKET"
    ETHERNETSNAPTCPIPV4PACKET = "ETHERNETSNAPTCPIPV4PACKET"
    ETHERNETSNAPTCPIPV4TAGGEDPACKET = "ETHERNETSNAPTCPIPV4TAGGEDPACKET"
    ETHERNETSNAPTCPIPV4VLANSTACKPACKET = "ETHERNETSNAPTCPIPV4VLANSTACKPACKET"
    ETHERNETSNAPUDPIPV4PACKET = "ETHERNETSNAPUDPIPV4PACKET"
    ETHERNETSNAPUDPIPV4TAGGEDPACKET = "ETHERNETSNAPUDPIPV4TAGGEDPACKET"
    ETHERNETSNAPUDPIPV4VLANSTACKPACKET = "ETHERNETSNAPUDPIPV4VLANSTACKPACKET"
    ETHERNETSNAPIPV6PACKET = "ETHERNETSNAPIPV6PACKET"
    ETHERNETSNAPIPV6TAGGEDPACKET = "ETHERNETSNAPIPV6TAGGEDPACKET"
    ETHERNETSNAPIPV6VLANSTACKPACKET = "ETHERNETSNAPIPV6VLANSTACKPACKET"
    ETHERNETSNAPTCPIPV6PACKET = "ETHERNETSNAPTCPIPV6PACKET"
    ETHERNETSNAPTCPIPV6TAGGEDPACKET = "ETHERNETSNAPTCPIPV6TAGGEDPACKET"
    ETHERNETSNAPTCPIPV6VLANSTACKPACKET = "ETHERNETSNAPTCPIPV6VLANSTACKPACKET"
    ETHERNETSNAPUDPIPV6PACKET = "ETHERNETSNAPUDPIPV6PACKET"
    ETHERNETSNAPUDPIPV6TAGGEDPACKET = "ETHERNETSNAPUDPIPV6TAGGEDPACKET"
    ETHERNETSNAPUDPIPV6VLANSTACKPACKET = "ETHERNETSNAPUDPIPV6VLANSTACKPACKET"
    ETHERNETSNAPLLDPPACKET = "ETHERNETSNAPLLDPPACKET"
    ETHERNETSNAPLLDPTAGGEDPACKET = "ETHERNETSNAPLLDPTAGGEDPACKET"
    ETHERNETSNAPLLDPVLANSTACKPACKET = "ETHERNETSNAPLLDPVLANSTACKPACKET"
    ALL_PACKETS = [
        "ETHERNET2ARPPACKET",
        "ETHERNET2ARPTAGGEDPACKET",
        "ETHERNET2ARPVLANSTACKPACKET",
        "ETHERNET2MPLSPACKET",
        "ETHERNET2MPLSTAGGEDPACKET",
        "ETHERNET2MPLSVLANSTACKPACKET",
        "ETHERNET2PACKET",
        "ETHERNET2TAGGEDPACKET",
        "ETHERNET2VLANSTACKPACKET",
        "ETHERNETPACKET",
        "ETHERNETTAGGEDPACKET",
        "ETHERNETVLANSTACKPACKET",
        "IEEE802LLCPACKET",
        "IEEE802LLCTAGGEDPACKET",
        "IEEE802LLCVLANSTACKPACKET",
        "SAPPACKET",
        "SAPTAGGEDPACKET",
        "SAPVLANSTACKPACKET",
        "ETHERNET2MPLSENCAPSULATEDPACKET",
        "ETHERNET2MPLSENCAPSULATEDTAGGEDPACKET",
        "ETHERNET2MPLSENCAPSULATEDVLANSTACKPACKET",
        "ETHERNET2PROVIDERBACKBONEBRIDGEPACKET",
        "ETHERNET2PROVIDERBACKBONEBRIDGETAGGEDPACKET",
        "ETHERNET2PROVIDERBACKBONEBRIDGEVLANSTACKPACKET",
        "ETHERNET2ERSPANGREIPV4PACKET",
        "ETHERNET2ERSPANGREIPV4TAGGEDPACKET",
        "ETHERNET2ERSPANGREIPV4VLANSTACKPACKET",
        "ETHERNET2ERSPANIIIGREIPV4PACKET",
        "ETHERNET2ERSPANIIIGREIPV4TAGGEDPACKET",
        "ETHERNET2ERSPANIIIGREIPV4VLANSTACKPACKET",
        "ETHERNET2GREIPV4PACKET",
        "ETHERNET2GREIPV4TAGGEDPACKET",
        "ETHERNET2GREIPV4VLANSTACKPACKET",
        "ETHERNET2IPENCAPSULATEDIPV4PACKET",
        "ETHERNET2IPENCAPSULATEDIPV4TAGGEDPACKET",
        "ETHERNET2IPENCAPSULATEDIPV4VLANSTACKPACKET",
        "ETHERNET2VXLANUDPIPV4PACKET",
        "ETHERNET2VXLANUDPIPV4TAGGEDPACKET",
        "ETHERNET2VXLANUDPIPV4VLANSTACKPACKET",
        "ETHERNETSNAPERSPANGREIPV4PACKET",
        "ETHERNETSNAPERSPANGREIPV4TAGGEDPACKET",
        "ETHERNETSNAPERSPANGREIPV4VLANSTACKPACKET",
        "ETHERNETSNAPERSPANIIIGREIPV4PACKET",
        "ETHERNETSNAPERSPANIIIGREIPV4TAGGEDPACKET",
        "ETHERNETSNAPERSPANIIIGREIPV4VLANSTACKPACKET",
        "ETHERNETSNAPGREIPV4PACKET",
        "ETHERNETSNAPGREIPV4TAGGEDPACKET",
        "ETHERNETSNAPGREIPV4VLANSTACKPACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV4PACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV4TAGGEDPACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV4VLANSTACKPACKET",
        "ETHERNET2ERSPANGREIPV6PACKET",
        "ETHERNET2ERSPANGREIPV6TAGGEDPACKET",
        "ETHERNET2ERSPANGREIPV6VLANSTACKPACKET",
        "ETHERNET2ERSPANIIIGREIPV6PACKET",
        "ETHERNET2ERSPANIIIGREIPV6TAGGEDPACKET",
        "ETHERNET2ERSPANIIIGREIPV6VLANSTACKPACKET",
        "ETHERNET2GREIPV6PACKET",
        "ETHERNET2GREIPV6TAGGEDPACKET",
        "ETHERNET2GREIPV6VLANSTACKPACKET",
        "ETHERNET2IPENCAPSULATEDIPV6PACKET",
        "ETHERNET2IPENCAPSULATEDIPV6TAGGEDPACKET",
        "ETHERNET2IPENCAPSULATEDIPV6VLANSTACKPACKET",
        "ETHERNET2VXLANUDPIPV6PACKET",
        "ETHERNET2VXLANUDPIPV6TAGGEDPACKET",
        "ETHERNET2VXLANUDPIPV6VLANSTACKPACKET",
        "ETHERNETSNAPERSPANGREIPV6PACKET",
        "ETHERNETSNAPERSPANGREIPV6TAGGEDPACKET",
        "ETHERNETSNAPERSPANGREIPV6VLANSTACKPACKET",
        "ETHERNETSNAPERSPANIIIGREIPV6PACKET",
        "ETHERNETSNAPERSPANIIIGREIPV6TAGGEDPACKET",
        "ETHERNETSNAPERSPANIIIGREIPV6VLANSTACKPACKET",
        "ETHERNETSNAPGREIPV6PACKET",
        "ETHERNETSNAPGREIPV6TAGGEDPACKET",
        "ETHERNETSNAPGREIPV6VLANSTACKPACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV6PACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV6TAGGEDPACKET",
        "ETHERNETSNAPIPENCAPSULATEDIPV6VLANSTACKPACKET",
        "ETHERNET2BOOTPUDPIPV4PACKET",
        "ETHERNET2BOOTPUDPIPV4TAGGEDPACKET",
        "ETHERNET2BOOTPUDPIPV4VLANSTACKPACKET",
        "ETHERNET2DBDESCRIPTIONOSPFIPV4PACKET",
        "ETHERNET2DBDESCRIPTIONOSPFIPV4TAGGEDPACKET",
        "ETHERNET2DBDESCRIPTIONOSPFIPV4VLANSTACKPACKET",
        "ETHERNET2DNSTCPIPV4PACKET",
        "ETHERNET2DNSTCPIPV4TAGGEDPACKET",
        "ETHERNET2DNSTCPIPV4VLANSTACKPACKET",
        "ETHERNET2DNSUDPIPV4PACKET",
        "ETHERNET2DNSUDPIPV4TAGGEDPACKET",
        "ETHERNET2DNSUDPIPV4VLANSTACKPACKET",
        "ETHERNET2HELLOOSPFIPV4PACKET",
        "ETHERNET2HELLOOSPFIPV4TAGGEDPACKET",
        "ETHERNET2HELLOOSPFIPV4VLANSTACKPACKET",
        "ETHERNET2ICMPIPV4MPLSPACKET",
        "ETHERNET2ICMPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2ICMPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2ICMPIPV4PACKET",
        "ETHERNET2ICMPIPV4TAGGEDPACKET",
        "ETHERNET2ICMPIPV4VLANSTACKPACKET",
        "ETHERNET2IGMPIPV4MPLSPACKET",
        "ETHERNET2IGMPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2IGMPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2IGMPIPV4PACKET",
        "ETHERNET2IGMPIPV4TAGGEDPACKET",
        "ETHERNET2IGMPIPV4VLANSTACKPACKET",
        "ETHERNET2IPV4MPLSPACKET",
        "ETHERNET2IPV4MPLSTAGGEDPACKET",
        "ETHERNET2IPV4MPLSVLANSTACKPACKET",
        "ETHERNET2IPV4PACKET",
        "ETHERNET2IPV4TAGGEDPACKET",
        "ETHERNET2IPV4VLANSTACKPACKET",
        "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4PACKET",
        "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4TAGGEDPACKET",
        "ETHERNET2LINKSTATEACKNOWLEDGEOSPFIPV4VLANSTACKPACKET",
        "ETHERNET2LINKSTATEREQUESTOSPFIPV4PACKET",
        "ETHERNET2LINKSTATEREQUESTOSPFIPV4TAGGEDPACKET",
        "ETHERNET2LINKSTATEREQUESTOSPFIPV4VLANSTACKPACKET",
        "ETHERNET2LINKSTATEUPDATEOSPFIPV4PACKET",
        "ETHERNET2LINKSTATEUPDATEOSPFIPV4TAGGEDPACKET",
        "ETHERNET2LINKSTATEUPDATEOSPFIPV4VLANSTACKPACKET",
        "ETHERNET2OSPFIPV4PACKET",
        "ETHERNET2OSPFIPV4TAGGEDPACKET",
        "ETHERNET2OSPFIPV4VLANSTACKPACKET",
        "ETHERNET2PIMIPV4PACKET",
        "ETHERNET2PIMIPV4TAGGEDPACKET",
        "ETHERNET2PIMIPV4VLANSTACKPACKET",
        "ETHERNET2RADIUSUDPIPV4PACKET",
        "ETHERNET2RADIUSUDPIPV4TAGGEDPACKET",
        "ETHERNET2RADIUSUDPIPV4VLANSTACKPACKET",
        "ETHERNET2RIPUDPIPV4MPLSPACKET",
        "ETHERNET2RIPUDPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2RIPUDPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2RIPUDPIPV4PACKET",
        "ETHERNET2RIPUDPIPV4TAGGEDPACKET",
        "ETHERNET2RIPUDPIPV4VLANSTACKPACKET",
        "ETHERNET2SYSLOGUDPIPV4PACKET",
        "ETHERNET2SYSLOGUDPIPV4TAGGEDPACKET",
        "ETHERNET2SYSLOGUDPIPV4VLANSTACKPACKET",
        "ETHERNET2TCPIPV4MPLSPACKET",
        "ETHERNET2TCPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2TCPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2TCPIPV4PACKET",
        "ETHERNET2TCPIPV4TAGGEDPACKET",
        "ETHERNET2TCPIPV4VLANSTACKPACKET",
        "ETHERNET2UDPIPV4MPLSPACKET",
        "ETHERNET2UDPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2UDPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2UDPIPV4PACKET",
        "ETHERNET2UDPIPV4TAGGEDPACKET",
        "ETHERNET2UDPIPV4VLANSTACKPACKET",
        "ETHERNET2VRRPIPV4MPLSPACKET",
        "ETHERNET2VRRPIPV4MPLSTAGGEDPACKET",
        "ETHERNET2VRRPIPV4MPLSVLANSTACKPACKET",
        "ETHERNET2VRRPIPV4PACKET",
        "ETHERNET2VRRPIPV4TAGGEDPACKET",
        "ETHERNET2VRRPIPV4VLANSTACKPACKET",
        "ETHERNET2BGPTCPIPV4PACKET",
        "ETHERNET2BGPTCPIPV4TAGGEDPACKET",
        "ETHERNET2BGPTCPIPV4VLANSTACKPACKET",
        "ETHERNET2DNSTCPIPV6PACKET",
        "ETHERNET2DNSTCPIPV6TAGGEDPACKET",
        "ETHERNET2DNSTCPIPV6VLANSTACKPACKET",
        "ETHERNET2DNSUDPIPV6PACKET",
        "ETHERNET2DNSUDPIPV6TAGGEDPACKET",
        "ETHERNET2DNSUDPIPV6VLANSTACKPACKET",
        "ETHERNET2ICMPV6IPV6MPLSPACKET",
        "ETHERNET2ICMPV6IPV6MPLSTAGGEDPACKET",
        "ETHERNET2ICMPV6IPV6MPLSVLANSTACKPACKET",
        "ETHERNET2ICMPV6IPV6PACKET",
        "ETHERNET2ICMPV6IPV6TAGGEDPACKET",
        "ETHERNET2ICMPV6IPV6VLANSTACKPACKET",
        "ETHERNET2IPV6MPLSPACKET",
        "ETHERNET2IPV6MPLSTAGGEDPACKET",
        "ETHERNET2IPV6MPLSVLANSTACKPACKET",
        "ETHERNET2IPV6PACKET",
        "ETHERNET2IPV6TAGGEDPACKET",
        "ETHERNET2IPV6VLANSTACKPACKET",
        "ETHERNET2PIMIPV6PACKET",
        "ETHERNET2PIMIPV6TAGGEDPACKET",
        "ETHERNET2PIMIPV6VLANSTACKPACKET",
        "ETHERNET2RADIUSUDPIPV6PACKET",
        "ETHERNET2RADIUSUDPIPV6TAGGEDPACKET",
        "ETHERNET2RADIUSUDPIPV6VLANSTACKPACKET",
        "ETHERNET2RIPNGUDPIPV6MPLSPACKET",
        "ETHERNET2RIPNGUDPIPV6MPLSTAGGEDPACKET",
        "ETHERNET2RIPNGUDPIPV6MPLSVLANSTACKPACKET",
        "ETHERNET2RIPNGUDPIPV6PACKET",
        "ETHERNET2RIPNGUDPIPV6TAGGEDPACKET",
        "ETHERNET2RIPNGUDPIPV6VLANSTACKPACKET",
        "ETHERNET2SYSLOGUDPIPV6PACKET",
        "ETHERNET2SYSLOGUDPIPV6TAGGEDPACKET",
        "ETHERNET2SYSLOGUDPIPV6VLANSTACKPACKET",
        "ETHERNET2TCPIPV6MPLSPACKET",
        "ETHERNET2TCPIPV6MPLSTAGGEDPACKET",
        "ETHERNET2TCPIPV6MPLSVLANSTACKPACKET",
        "ETHERNET2TCPIPV6PACKET",
        "ETHERNET2TCPIPV6TAGGEDPACKET",
        "ETHERNET2TCPIPV6VLANSTACKPACKET",
        "ETHERNET2UDPIPV6MPLSPACKET",
        "ETHERNET2UDPIPV6MPLSTAGGEDPACKET",
        "ETHERNET2UDPIPV6MPLSVLANSTACKPACKET",
        "ETHERNET2UDPIPV6PACKET",
        "ETHERNET2UDPIPV6TAGGEDPACKET",
        "ETHERNET2UDPIPV6VLANSTACKPACKET",
        "ETHERNET2VRRPIPV6MPLSPACKET",
        "ETHERNET2VRRPIPV6MPLSTAGGEDPACKET",
        "ETHERNET2VRRPIPV6MPLSVLANSTACKPACKET",
        "ETHERNET2VRRPIPV6PACKET",
        "ETHERNET2VRRPIPV6TAGGEDPACKET",
        "ETHERNET2VRRPIPV6VLANSTACKPACKET",
        "ETHERNET2BGPTCPIPV6PACKET",
        "ETHERNET2BGPTCPIPV6TAGGEDPACKET",
        "ETHERNET2BGPTCPIPV6VLANSTACKPACKET",
        "IEEE802_2IPXPACKET",
        "IEEE802_2IPXTAGGEDPACKET",
        "IEEE802_2IPXVLANSTACKPACKET",
        "ETHERNET2CSNPDBSYNCDVRPACKET",
        "ETHERNET2CSNPDBSYNCDVRTAGGEDPACKET",
        "ETHERNET2CSNPDBSYNCDVRVLANSTACKPACKET",
        "ETHERNET2DBPDBSYNCDVRPACKET",
        "ETHERNET2DBPDBSYNCDVRTAGGEDPACKET",
        "ETHERNET2DBPDBSYNCDVRVLANSTACKPACKET",
        "ETHERNET2DBSYNCDVRPACKET",
        "ETHERNET2DBSYNCDVRTAGGEDPACKET",
        "ETHERNET2DBSYNCDVRVLANSTACKPACKET",
        "ETHERNET2LLDPPACKET",
        "ETHERNET2LLDPTAGGEDPACKET",
        "ETHERNET2LLDPVLANSTACKPACKET",
        "SAPBPDUPACKET",
        "SAPBPDUTAGGEDPACKET",
        "SAPBPDUVLANSTACKPACKET",
        "SAPMSTPSPANNINGTREEBPDUPACKET",
        "SAPMSTPSPANNINGTREEBPDUTAGGEDPACKET",
        "SAPMSTPSPANNINGTREEBPDUVLANSTACKPACKET",
        "SAPRSTPBPDUPACKET",
        "SAPRSTPBPDUTAGGEDPACKET",
        "SAPRSTPBPDUVLANSTACKPACKET",
        "SAPSPANNINGTREEBPDUPACKET",
        "SAPSPANNINGTREEBPDUTAGGEDPACKET",
        "SAPSPANNINGTREEBPDUVLANSTACKPACKET",
        "SAPCSNPISISPACKET",
        "SAPCSNPISISTAGGEDPACKET",
        "SAPCSNPISISVLANSTACKPACKET",
        "SAPHELLOPDUISISPACKET",
        "SAPHELLOPDUISISTAGGEDPACKET",
        "SAPHELLOPDUISISVLANSTACKPACKET",
        "SAPISISPACKET",
        "SAPISISTAGGEDPACKET",
        "SAPISISVLANSTACKPACKET",
        "SAPLSPISISPACKET",
        "SAPLSPISISTAGGEDPACKET",
        "SAPLSPISISVLANSTACKPACKET",
        "SAPPSNPISISPACKET",
        "SAPPSNPISISTAGGEDPACKET",
        "SAPPSNPISISVLANSTACKPACKET",
        "ETHERNETSNAPPACKET",
        "ETHERNETSNAPTAGGEDPACKET",
        "ETHERNETSNAPVLANSTACKPACKET",
        "ETHERNETSNAPIPV4PACKET",
        "ETHERNETSNAPIPV4TAGGEDPACKET",
        "ETHERNETSNAPIPV4VLANSTACKPACKET",
        "ETHERNETSNAPTCPIPV4PACKET",
        "ETHERNETSNAPTCPIPV4TAGGEDPACKET",
        "ETHERNETSNAPTCPIPV4VLANSTACKPACKET",
        "ETHERNETSNAPUDPIPV4PACKET",
        "ETHERNETSNAPUDPIPV4TAGGEDPACKET",
        "ETHERNETSNAPUDPIPV4VLANSTACKPACKET",
        "ETHERNETSNAPIPV6PACKET",
        "ETHERNETSNAPIPV6TAGGEDPACKET",
        "ETHERNETSNAPIPV6VLANSTACKPACKET",
        "ETHERNETSNAPTCPIPV6PACKET",
        "ETHERNETSNAPTCPIPV6TAGGEDPACKET",
        "ETHERNETSNAPTCPIPV6VLANSTACKPACKET",
        "ETHERNETSNAPUDPIPV6PACKET",
        "ETHERNETSNAPUDPIPV6TAGGEDPACKET",
        "ETHERNETSNAPUDPIPV6VLANSTACKPACKET",
        "ETHERNETSNAPLLDPPACKET",
        "ETHERNETSNAPLLDPTAGGEDPACKET",
        "ETHERNETSNAPLLDPVLANSTACKPACKET",
    ]
