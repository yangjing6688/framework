from ExtremeAutomation.Library.Utils.Singleton import Singleton


class JetsDeviceConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device

    ARP_DST_HW_ADDR_CMD = "arp_dst_hw_addr"

    IPV6_DST_MODE_CMD = "ipv6_dst_mode"
    # Constant values for IPV6_DST_MODE_CMD
    IPV6_DST_MODE_FIXED_INCREMENT = "fixed increment"
    IPV6_DST_MODE_DECREMENT_LIST_RANDOM = "decrement list random"
    IPV6_DST_MODE_INCR_HOST_DECR_HOST = "incr_host decr_host"
    IPV6_DST_MODE_INCR_NETWORK = "incr_network"
    IPV6_DST_MODE_DECR_NETWORK = "decr_network"
    IPV6_DST_MODE_INCR_INTF_ID = "incr_intf_id"
    IPV6_DST_MODE_DECR_INTF_ID = "decr_intf_id"
    IPV6_DST_MODE_INCR_GLOBAL_TOP_LEVEL = "incr_global_top_level"
    IPV6_DST_MODE_DECR_GLOBAL_TOP_LEVEL = "decr_global_top_level"
    IPV6_DST_MODE_INCR_GLOBAL_NEXT_LEVEL = "incr_global_next_level"
    IPV6_DST_MODE_DECR_GLOBAL_NEXT_LEVEL = "decr_global_next_level"
    IPV6_DST_MODE_INCR_GLOBAL_SITE_LEVEL = "incr_global_site_level"
    IPV6_DST_MODE_DECR_GLOBAL_SITE_LEVEL = "decr_global_site_level"
    IPV6_DST_MODE_INCR_LOCAL_SITE_SUBNET = "incr_local_site_subnet"
    IPV6_DST_MODE_DECR_LOCAL_SITE_SUBNET = "decr_local_site_subnet"
    IPV6_DST_MODE_INCR_MCAST_GROUP = "incr_mcast_group"
    IPV6_DST_MODE_DECR_MCAST_GROUP = "decr_mcast_group"

    ENET_HDR = "ENET_HDR"
    LLC_HDR = "LLC"
    IEEE_8021Q_HDR = "IEEE_8021Q_HDR"
    QNQ_HDR = "QNQ_HDR"
    VXLAN_HDR = "VXLAN_HDR"
    SNAP_HDR = "SNAP_HDR"
    ARP_HDR = "ARP_HDR"
    IP_HDR = "IP_HDR"
    IPX_HDR = "IPX_HDR"
    IPv6_HDR = "IPv6_HDR"

    ICMP_HDR = "ICMP_HDR"
    UDP_HDR = "UDP_HDR"
    TCP_HDR = "TCP_HDR"
    IGMP_HDR = "IGMP_HDR"
    IGMP_V1V2_HDR = "IGMP_V1V2_HDR"
    IGMP_GROUP_ONLY = "IGMP_GROUP_ONLY"
    MEMBERSHIP_QUERY_MSG = "MEMBERSHIP_QUERY_MSG"

    RAW_DATA = "rawdata"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
