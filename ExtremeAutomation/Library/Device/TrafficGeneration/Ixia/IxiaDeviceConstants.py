from ExtremeAutomation.Library.Utils.Singleton import Singleton


class IxiaDeviceConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    TRAFFIC_TAG_CONFIG_API = "TRAFFIC_TAG_CONFIG_API"
    IXIA_STREAM_CONFIG_IX_TCL_HAL_API = "IXIA_STREAM_CONFIG_IX_TCL_HAL_API"
    IXIA_CAPTURE_IX_TCL_HAL_API = "IXIA_CAPTURE_IX_TCL_HAL_API"
    IXIA_STATISTIC_IX_TCL_HAL_API = "IXIA_STATISTIC_IX_TCL_HAL_API"
    IXIA_PORT_CONFIG_IX_TCL_HAL_API = "IXIA_PORT_CONFIG_IX_TCL_HAL_API"

    IXIA_FILER_PALLETTE_IX_TCL_HAL_API = "IXIA_FILER_PALLETTE_IX_TCL_HAL_API"
    IXIA_FILER_IX_TCL_HAL_API = "IXIA_FILER_IX_TCL_HAL_API"

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

    # FCS stream modes from A-149 version 3.40.
    FCS_GOOD = 0
    FCS_GOOD_STRING = "streamErrorGood"
    FCS_ALIGN_ERROR = 1
    FCS_ALIGN_ERROR_STRING = "streamErrorAlignment"
    FCS_DRIBBLE_ERROR = 2
    FCS_DRIBBLE_ERROR_STRING = "streamErrorDribble"
    FCS_BAD = 3
    FCS_BAD_STRING = "streamErrorBadCRC"
    FCS_NONE = 4
    FCS_NONE_STRING = "streamErrorNoCRC"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass
