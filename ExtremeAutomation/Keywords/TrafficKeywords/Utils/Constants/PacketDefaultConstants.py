class PacketDefaultConstants(object):

    SOURCE_MAC = "00:00:00:00:00:00"
    DESTINATION_MAC = "00:00:00:00:00:00"
    LLDP_DEST_MAC = "01:80:c2:00:00:0e"
    BPDU_DEST_MAC = "01:80:C2:00:00:00"
    VLAN_ID = "0"
    VLAN_PRIORITY = "0"
    VLAN_TPID = "0x8100"
    ETHER_TYPE = "0xFFFF"
    ETHER_TYPE_IP = "0x0800"
    ETHER_TYPE_IPV6 = "0x86DD"
    ETHER_TYPE_BPDU = "0x4242"
    TCN_BPDU_LENGTH = "43"
    LENGTH = "64"

    IP_TOS = "0x00"
    IP_ID = "0"
    IP_FLAGS = "0x00"
    IP_FRAG_OFFSET = "0"
    IP_TTL = "64"
    IP_PROTOCOL = "255"
    IP_PROTOCOL_UDP = "17"
    IP_PROTOCOL_TCP = "6"
    IP_PROTOCOL_PIM = "103"
    IP_PROTOCOL_ICMP = "1"
    IP_PROTOCOL_IGMP = "2"
    IP_SIP = "0.0.0.0"
    IP_DIP = "0.0.0.0"

    IPV6_TRAFFIC_CLASS = "0"
    IPV6_NEXT_HEADER = "59"
    IPV6_NEXT_HEADER_UDP = "17"
    IPV6_NEXT_HEADER_TCP = "6"
    IPv6_NEXT_HEADER_PIM = "103"
    IPV6_NEXT_HEADER_ICMP = "58"
    IPV6_NEXT_HEADER_IGMP = "2"
    IPV6_NEXT_HEADER_FRAGMENT = "44"
    IPV6_HOP_LIMIT = "255"
    IPV6_SIP = "0::0"
    IPV6_DIP = "0::0"

    UDP_SRC_PORT = "0"
    UDP_DST_PORT = "0"

    TCP_SRC_PORT = "0"
    TCP_DST_PORT = "0"
    TCP_SEQ_NUM = "0"
    TCP_ACK_NUM = "0"
    TCP_WINDOW = "0"
    TCP_FLAGS = "000000000"

    VXLAN_FLAGS = "0x0800"
    VXLAN_GROUP_ID = "0"
    VXLAN_VNI = "0"

    GRE_FLAGS = "0"
    GRE_VERSION = "0"
    GRE_PROTOCOL_TYPE = "0"
    GRE_CHECKSUM_BIT = False
    GRE_CHECKSUM = "0"
    GRE_ROUTING_BIT = False
    GRE_ROUTING = "0"
    GRE_OFFSET_BIT = False
    GRE_OFFSET = "0"
    GRE_KEY_BIT = False
    GRE_KEY = "0"
    GRE_SEQUENCE_BIT = False
    GRE_SEQUENCE = "0"
    GRE_SOURCE_ROUTE_BIT = False
    GRE_SOURCE_ROUTE = "0"
    GRE_RECURSION_CTRL = "0"

    # Arp Constants
    ARP_HARDWARE = "1"
    ARP_HARDWARE_TYPE = "0x0001"
    ARP_HARDWARE_SIZE = "6"
    ARP_ETHER_PROTO = "0x0806"
    ARP_IPV4_PROTO = "0x0800"
    ARP_PROTO_SIZE = "4"
    ARP_PROTO_TYPE = "0x0800"
    ARP_ID = "0"
    ARP_SEQ = "1"
    ARP_OPERATION = "1"
    ARP_SENDER_HARDWARE_ADDRESS = "FF:FF:FF:FF:FF:FF"
    ARP_SOURCE_PROTOCOL_ADDRESS = "0.0.0.0"
    ARP_TARGET_HARDWARE_ADDRESS = "00:00:00:00:00:00"
    ARP_TARGET_PROTOCOL_ADDRESS = "0.0.0.0"

    # STP Constants
    STP_PROTOCOL_ID = "0x0000"
    STP_VERSION = "0x00"
    STP_MESSAGE_TYPE = "0x00"
    STP_FLAGS = "0x00"
    STP_ROOT_PRIO = "0x8000"
    STP_ROOT_MAC = "00:00:00:00:00:00"
    STP_COST = "0"
    STP_BRIDGE_PRIO = "0x8000"
    STP_BRIDGE_MAC = "00:00:00:00:00:00"
    STP_PORT_ID = "0x8001"
    STP_AGE = "0"
    STP_MAX_AGE = "0x1400"
    STP_HELLO_TIME = "0x0200"
    STP_FORWARD_DELAY = "0x0f00"

    # MSTP Constants
    MSTP_FLAGS = "0x7C"
    MSTP_VERSION = "0x03"
    MSTP_MESSAGE_TYPE = "0x02"
    MSTI_ID = "7"
    MSTI_ROOT_PRIO = "8"
    MSTI_BRIDGE_PRIO = "0x80"
    VER1_LENGTH = "0"
    VER3_LENGTH = "64"
    MSTI_NAME = "default"
    MSTI_PATH_COST = "0"
    MSTI_DIGEST = "00000000000000000000000000000000"
    CIST_HOPS = "20"
    MSTI_HOPS = "20"
    MSTI_PORT_PRIO = "128"

    # RSTP Constants
    RSTP_FLAGS = "0x7C"
    RSTP_VERSION = "0x02"
    RSTP_MESSAGE_TYPE = "0x02"

    # ICMP Constants
    ICMP_TYPE = "1"
    ICMP_CODE = "1"
    ICMP_ID = "0"
    ICMP_SEQ = "0"

    # IGMP Constants
    IGMP_TYPE = "0x11"                  # Type 0x11 = IGMP Membership Query
    GROUP_ADDRESS = "224.0.0.1"
    MAX_RESP_TIME = "100"

    # PIM Constants
    PIM_VERSION = "2"
    PIM_TYPE = "0"

    # Don't allow values to be overwritten.
    def __setattr__(self, *_):
        """Do NOT allow values to be overwritten."""
        pass
