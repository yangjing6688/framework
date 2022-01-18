from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObjectConstants import CommandObjectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: session_info

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class SessionInfoApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(SessionInfoApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: session_info
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[SessionInfoConstants.MODE_CMD] = SessionInfoConstants.MODE_GET_SESSION_KEYS # constant value
        dummyDict[SessionInfoConstants.PORT_HANDLE_CMD] = "dummyValue2" # static value
        dummyDict[SessionInfoConstants.SESSION_KEYS_INCLUDE_FILTER_CMD] = SessionInfoConstants.SESSION_KEYS_INCLUDE_FILTER_CONNECT # constant value
        dummyDict[SessionInfoConstants.TRAFFIC_HANDLE_CMD] = "dummyValue4" # static value

        api = device.getApi(SessionInfoConstants.SESSION_INFO_API)
        api.session_info(dummyDict)
    """
    def session_info(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::session_info", argdictionary)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def session_info_mode(self):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_port_handle(self, port):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_session_keys_include_filter(self, any):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED

    def session_info_traffic_handle(self, any):
        return CommandObjectConstants.METHOD_NOT_SUPPORTED


"""
    This is the Constants class for the command: session_info
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class SessionInfoConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    SESSION_INFO_API = "SESSION_INFO_API"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_GET_SESSION_KEYS = "get_session_keys"
    MODE_GET_TRAFFIC_ITEMS = "get_traffic_items"
    MODE_GET_TRAFFIC_CE = "get_traffic_ce"
    MODE_GET_TRAFFIC_HLS = "get_traffic_hls"
    MODE_GET_TRAFFIC_HEADERS = "get_traffic_headers"
    MODE_GET_TRAFFIC_APPLICATION_PROFILES = "get_traffic_application_profiles"

    PORT_HANDLE_CMD = "port_handle"

    SESSION_KEYS_INCLUDE_FILTER_CMD = "session_keys_include_filter"
    # Constant values for SESSION_KEYS_INCLUDE_FILTER_CMD
    SESSION_KEYS_INCLUDE_FILTER_CONNECT = "connect"
    SESSION_KEYS_INCLUDE_FILTER_CONNECT_VPORT_LIST = "connect.vport_list"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG = "interface_config"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_INTERFACE_HANDLE = "interface_config.interface_handle"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_ROUTED_INTERFACE_HANDLE = "interface_config.routed_interface_handle"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_GRE_INTERFACE_HANDLE = "interface_config.gre_interface_handle"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_ATM_ENDPOINTS = "interface_config.atm_endpoints"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_FR_ENDPOINTS = "interface_config.fr_endpoints"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_IP_ENDPOINTS = "interface_config.ip_endpoints"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_LAN_ENDPOINTS = "interface_config.lan_endpoints"
    SESSION_KEYS_INCLUDE_FILTER_INTERFACE_CONFIG_IG_ENDPOINTS = "interface_config.ig_endpoints"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BFD_CONFIG = "emulation_bfd_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BFD_CONFIG_ROUTER_HANDLES = "emulation_bfd_config.router_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BFD_CONFIG_ROUTER_INTERFACE_HANDLES = "emulation_bfd_config.router_interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BFD_CONFIG_INTERFACE_HANDLES = "emulation_bfd_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BFD_SESSION_CONFIG_SESSION_HANDLES = "emulation_bfd_session_config.session_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BGP_CONFIG = "emulation_bgp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BGP_CONFIG_HANDLES = "emulation_bgp_config.handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BGP_ROUTE_CONFIG = "emulation_bgp_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BGP_ROUTE_CONFIG_BGP_ROUTES = "emulation_bgp_route_config.bgp_routes"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_BGP_ROUTE_CONFIG_BGP_SITES = "emulation_bgp_route_config.bgp_sites"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_CONFIG = "emulation_cfm_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_CONFIG_HANDLE = "emulation_cfm_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_CONFIG_INTERFACE_HANDLES = "emulation_cfm_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_CUSTOM_TLV_CONFIG = "emulation_cfm_custom_tlv_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_CUSTOM_TLV_CONFIG_HANDLE = "emulation_cfm_custom_tlv_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_LINKS_CONFIG = "emulation_cfm_links_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_LINKS_CONFIG_HANDLE = "emulation_cfm_links_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_MD_MEG_CONFIG = "emulation_cfm_md_meg_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_MD_MEG_CONFIG_HANDLE = "emulation_cfm_md_meg_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_MIP_MEP_CONFIG = "emulation_cfm_mip_mep_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_MIP_MEP_CONFIG_HANDLE = "emulation_cfm_mip_mep_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_VLAN_CONFIG = "emulation_cfm_vlan_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_VLAN_CONFIG_HANDLE = "emulation_cfm_vlan_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_CFM_VLAN_CONFIG_MAC_RANGE_HANDLES = "emulation_cfm_vlan_config.mac_range_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_CONFIG = "emulation_dhcp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_CONFIG_HANDLE = "emulation_dhcp_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_GROUP_CONFIG = "emulation_dhcp_group_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_GROUP_CONFIG_HANDLE = "emulation_dhcp_group_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_SERVER_CONFIG = "emulation_dhcp_server_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_DHCP_SERVER_CONFIG_HANDLE = "emulation_dhcp_server_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_DHCP_CLIENT_EXTENSION_CONFIG = "dhcp_client_extension_config"
    SESSION_KEYS_INCLUDE_FILTER_DHCP_CLIENT_EXTENSION_CONFIG_HANDLE = "dhcp_client_extension_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_DHCP_SERVER_EXTENSION_CONFIG = "dhcp_server_extension_config"
    SESSION_KEYS_INCLUDE_FILTER_DHCP_SERVER_EXTENSION_CONFIG_HANDLE = "dhcp_server_extension_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EFM_CONFIG = "emulation_efm_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EFM_CONFIG_INFORMATION_OAMPDU_ID = "emulation_efm_config.information_oampdu_id"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EFM_CONFIG_EVENT_NOTIFICATION_OAMPDU_ID = "emulation_efm_config.event_notification_oampdu_id"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EFM_ORG_VAR_CONFIG = "emulation_efm_org_var_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EFM_ORG_VAR_CONFIG_HANDLE = "emulation_efm_org_var_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EIGRP_CONFIG = "emulation_eigrp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EIGRP_CONFIG_ROUTER_HANDLES = "emulation_eigrp_config.router_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EIGRP_CONFIG_INTERFACE_HANDLES = "emulation_eigrp_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EIGRP_ROUTE_CONFIG = "emulation_eigrp_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_EIGRP_ROUTE_CONFIG_SESSION_HANDLES = "emulation_eigrp_route_config.session_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG = "emulation_elmi_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_INTERFACE_HANDLES = "emulation_elmi_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_UNI_HANDLES = "emulation_elmi_config.uni_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_UNI_STATUS_HANDLES = "emulation_elmi_config.uni_status_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_BW_PROFILE_HANDLES = "emulation_elmi_config.bw_profile_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_EVC_HANDLES = "emulation_elmi_config.evc_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ELMI_CONFIG_CE_VLAN_ID_RANGE_HANDLES = "emulation_elmi_config.ce_vlan_id_range_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_IGMP_CONFIG = "emulation_igmp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_IGMP_CONFIG_HANDLE = "emulation_igmp_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_IGMP_GROUP_CONFIG = "emulation_igmp_group_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_IGMP_GROUP_CONFIG_HANDLE = "emulation_igmp_group_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_IGMP_GROUP_CONFIG_SOURCE_HANDLE = "emulation_igmp_group_config.source_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_CONFIG = "emulation_isis_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_CONFIG_HANDLE = "emulation_isis_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_TOPOLOGY_ROUTE_CONFIG = "emulation_isis_topology_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_TOPOLOGY_ROUTE_CONFIG_ELEM_HANDLE = "emulation_isis_topology_route_config.elem_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_TOPOLOGY_ROUTE_CONFIG_STUB = "emulation_isis_topology_route_config.stub"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_TOPOLOGY_ROUTE_CONFIG_EXTERNAL = "emulation_isis_topology_route_config.external"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ISIS_TOPOLOGY_ROUTE_CONFIG_GRID = "emulation_isis_topology_route_config.grid"
    SESSION_KEYS_INCLUDE_FILTER_L2TP_CONFIG = "l2tp_config"
    SESSION_KEYS_INCLUDE_FILTER_L2TP_CONFIG_HANDLES = "l2tp_config.handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LACP_LINK_CONFIG = "emulation_lacp_link_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LACP_LINK_CONFIG_HANDLE = "emulation_lacp_link_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_CONFIG = "emulation_ldp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_CONFIG_HANDLE = "emulation_ldp_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG = "emulation_ldp_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG_LSP_HANDLE = "emulation_ldp_route_config.lsp_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG_LSP_INTF = "emulation_ldp_route_config.lsp_intf"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG_LSP_VC_RANGE_HANDLES = "emulation_ldp_route_config.lsp_vc_range_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG_LSP_VC_IP_RANGE_HANDLES = "emulation_ldp_route_config.lsp_vc_ip_range_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_LDP_ROUTE_CONFIG_LSP_VC_MAC_RANGE_HANDLES = "emulation_ldp_route_config.lsp_vc_mac_range_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MLD_CONFIG = "emulation_mld_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MLD_CONFIG_HANDLE = "emulation_mld_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MLD_GROUP_CONFIG = "emulation_mld_group_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MLD_GROUP_CONFIG_HANDLE = "emulation_mld_group_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_OSPF_CONFIG = "emulation_ospf_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_OSPF_CONFIG_HANDLE = "emulation_ospf_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG = "emulation_ospf_topology_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_OSPF_TOPOLOGY_ROUTE_CONFIG_ELEM_HANDLE = "emulation_ospf_topology_route_config.elem_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_CONFIG = "emulation_pbb_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_CONFIG_HANDLE = "emulation_pbb_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_CONFIG_INTERFACE_HANDLES = "emulation_pbb_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_TRUNK_CONFIG = "emulation_pbb_trunk_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_TRUNK_CONFIG_TRUNK_HANDLE = "emulation_pbb_trunk_config.trunk_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PBB_TRUNK_CONFIG_MR_HANDLE = "emulation_pbb_trunk_config.mr_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PIM_CONFIG = "emulation_pim_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PIM_CONFIG_HANDLE = "emulation_pim_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PIM_CONFIG_INTERFACES = "emulation_pim_config.interfaces"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PIM_GROUP_CONFIG = "emulation_pim_group_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_PIM_GROUP_CONFIG_HANDLE = "emulation_pim_group_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_PPPOX_CONFIG = "pppox_config"
    SESSION_KEYS_INCLUDE_FILTER_PPPOX_CONFIG_HANDLES = "pppox_config.handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RIP_CONFIG = "emulation_rip_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RIP_CONFIG_HANDLE = "emulation_rip_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RIP_ROUTE_CONFIG = "emulation_rip_route_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RIP_ROUTE_CONFIG_ROUTE_HANDLE = "emulation_rip_route_config.route_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_CONFIG = "emulation_rsvp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_CONFIG_HANDLES = "emulation_rsvp_config.handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_TUNNEL_CONFIG = "emulation_rsvp_tunnel_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_TUNNEL_CONFIG_TUNNEL_HANDLE = "emulation_rsvp_tunnel_config.tunnel_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_TUNNEL_CONFIG_TUNNEL_LEAVES_HANDLE = "emulation_rsvp_tunnel_config.tunnel_leaves_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_RSVP_TUNNEL_CONFIG_ROUTED_INTERFACES = "emulation_rsvp_tunnel_config.routed_interfaces"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_MSTI_CONFIG = "emulation_stp_msti_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_MSTI_CONFIG_HANDLE = "emulation_stp_msti_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_BRIDGE_CONFIG = "emulation_stp_bridge_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_BRIDGE_CONFIG_BRIDGE_HANDLE = "emulation_stp_bridge_config.bridge_handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_BRIDGE_CONFIG_BRIDGE_INTERFACE_HANDLES = "emulation_stp_bridge_config.bridge_interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_STP_BRIDGE_CONFIG_INTERFACE_HANDLES = "emulation_stp_bridge_config.interface_handles"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_CONFIG = "emulation_twamp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_CONFIG_HANDLE = "emulation_twamp_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_CONTROL_RANGE_CONFIG = "emulation_twamp_control_range_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_CONTROL_RANGE_CONFIG_HANDLE = "emulation_twamp_control_range_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_TEST_RANGE_CONFIG = "emulation_twamp_test_range_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_TEST_RANGE_CONFIG_HANDLE = "emulation_twamp_test_range_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_SERVER_RANGE_CONFIG = "emulation_twamp_server_range_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_TWAMP_SERVER_RANGE_CONFIG_HANDLE = "emulation_twamp_server_range_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ANCP_CONFIG = "emulation_ancp_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ANCP_CONFIG_HANDLE = "emulation_ancp_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ANCP_SUBSCRIBER_LINES_CONFIG = "emulation_ancp_subscriber_lines_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_ANCP_SUBSCRIBER_LINES_CONFIG_HANDLE = "emulation_ancp_subscriber_lines_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_FC_CLIENT_CONFIG = "fc_client_config"
    SESSION_KEYS_INCLUDE_FILTER_FC_CLIENT_CONFIG_HANDLE = "fc_client_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_FC_FPORT_CONFIG = "fc_fport_config"
    SESSION_KEYS_INCLUDE_FILTER_FC_FPORT_CONFIG_HANDLE = "fc_fport_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_FC_FPORT_VNPORT_CONFIG = "fc_fport_vnport_config"
    SESSION_KEYS_INCLUDE_FILTER_FC_FPORT_VNPORT_CONFIG_HANDLE = "fc_fport_vnport_config.handle"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_CONFIG = "traffic_config"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_CONFIG_STREAM_ID = "traffic_config.stream_id"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_CONFIG_TRAFFIC_ITEM = "traffic_config.traffic_item"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG = "traffic_l47_config"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG_TRAFFIC_L47_HANDLE_APPLIB_PROFILE = "traffic_l47_config.traffic_l47_handle.applib_profile"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG_TRAFFIC_L47_HANDLE_APPLIB_PROFILE_APPLIB_FLOW = "traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG_TRAFFIC_L47_HANDLE_APPLIB_PROFILE_APPLIB_FLOW_PARAMETER = "traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.parameter"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG_TRAFFIC_L47_HANDLE_APPLIB_PROFILE_APPLIB_FLOW_CONNECTION = "traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.connection"
    SESSION_KEYS_INCLUDE_FILTER_TRAFFIC_L47_CONFIG_TRAFFIC_L47_HANDLE_APPLIB_PROFILE_APPLIB_FLOW_CONNECTION_PARAMETER = "traffic_l47_config.traffic_l47_handle.applib_profile.applib_flow.connection.parameter"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MULTICAST_GROUP_CONFIG = "emulation_multicast_group_config"
    SESSION_KEYS_INCLUDE_FILTER_EMULATION_MULTICAST_SOURCE_CONFIG = "emulation_multicast_source_config"

    TRAFFIC_HANDLE_CMD = "traffic_handle"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -mode
    -port_handle
    -session_keys_include_filter
    -traffic_handle
If you want to update this file, look in the CSV
"""
