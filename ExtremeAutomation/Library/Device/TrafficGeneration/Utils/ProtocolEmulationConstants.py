class ProtocolEmulationConstants:
    def __init__(self):
        pass

    # Don't allow values to be updated.
    def __setattr__(self, *_):
        pass

    # Constants
    BGP_API = "BGP_API"
    DHCP_API = "DHCP_API"
    DVR_API = "DVR_API"
    END_STATION_API = "END_STATION_API"
    LLDP_API = "LLDP_API"
    IGMP_API = "IGMP_API"
    OSPF_API = "OSPF_API"
    RIP_API = "RIP_API"
    RIPNG_API = "RIPNG_API"
    ROUTE_API = "ROUTE_API"
    SPB_API = "SBP_API"
    TCP_API = "TCP_API"
    VRRP_API = "VRRP_API"
    VXLAN_API = "VXLAN_API"
