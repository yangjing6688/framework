from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton

"""
    This is the API class for the command: connect

    Class is auto-generated. If you update anything here,
        it will be over written.
"""


class ConnectApi(TrafficGenerationApi):

    """
    init function
    """
    def __init__(self, device):
        super(ConnectApi, self).__init__(device)

    """
    This is the "One Large Method" for the command: connect
    use this by passing in a dict() of all the commands
        dummyDict = dict()
        dummyDict[ConnectConstants.AGGREGATION_MODE_CMD] = ConnectConstants.AGGREGATION_MODE_NORMAL # constant value
        dummyDict[ConnectConstants.AGGREGATION_RESOURCE_MODE_CMD] = ConnectConstants.AGGREGATION_RESOURCE_MODE_NORMAL # constant value
        dummyDict[ConnectConstants.BREAK_LOCKS_CMD] = "dummyValue3" # static value
        dummyDict[ConnectConstants.CHAIN_CABLES_LENGTH_CMD] = "dummyValue4" # static value
        dummyDict[ConnectConstants.CHAIN_SEQUENCE_CMD] = "dummyValue5" # static value
        dummyDict[ConnectConstants.CHAIN_TYPE_CMD] = ConnectConstants.CHAIN_TYPE_DAISY # constant value
        dummyDict[ConnectConstants.CLOSE_SERVER_ON_DISCONNECT_CMD] = "dummyValue7" # static value
        dummyDict[ConnectConstants.CONFIG_FILE_CMD] = "dummyValue8" # static value
        dummyDict[ConnectConstants.CONFIG_FILE_HLT_CMD] = "dummyValue9" # static value
        dummyDict[ConnectConstants.CONNECT_TIMEOUT_CMD] = "dummyValue10" # static value
        dummyDict[ConnectConstants.DEVICE_CMD] = "dummyValue11" # static value
        dummyDict[ConnectConstants.ENABLE_WIN_TCL_SERVER_CMD] = "dummyValue12" # static value
        dummyDict[ConnectConstants.EXECUTION_TIMEOUT_CMD] = "dummyValue13" # static value
        dummyDict[ConnectConstants.FORCELOAD_CMD] = "dummyValue14" # static value
        dummyDict[ConnectConstants.GUARD_RAIL_CMD] = ConnectConstants.GUARD_RAIL_NONE # constant value
        dummyDict[ConnectConstants.HELPER_CMD] = "dummyValue16" # static value
        dummyDict[ConnectConstants.INTERACTIVE_CMD] = "dummyValue17" # static value
        dummyDict[ConnectConstants.IXNETWORK_LICENSE_SERVERS_CMD] = "dummyValue18" # static value
        dummyDict[ConnectConstants.IXNETWORK_LICENSE_TYPE_CMD] = ConnectConstants.IXNETWORK_LICENSE_TYPE_MIXED # constant value
        dummyDict[ConnectConstants.IXNETWORK_TCL_PROXY_CMD] = "dummyValue20" # static value
        dummyDict[ConnectConstants.IXNETWORK_TCL_SERVER_CMD] = "dummyValue21" # static value
        dummyDict[ConnectConstants.LOG_PATH_CMD] = "dummyValue22" # static value
        dummyDict[ConnectConstants.LOGGING_CMD] = ConnectConstants.LOGGING_HLTAPI_CALLS # constant value
        dummyDict[ConnectConstants.MASTER_DEVICE_CMD] = "dummyValue24" # static value
        dummyDict[ConnectConstants.MODE_CMD] = ConnectConstants.MODE_CONNECT # constant value
        dummyDict[ConnectConstants.NOBIOS_CMD] = "dummyValue26" # static value
        dummyDict[ConnectConstants.PORT_LIST_CMD] = "dummyValue27" # static value
        dummyDict[ConnectConstants.PROTOCOL_STACKING_MODE_CMD] = ConnectConstants.PROTOCOL_STACKING_MODE_PARALLEL # constant value
        dummyDict[ConnectConstants.RESET_CMD] = "dummyValue29" # static value
        dummyDict[ConnectConstants.RETURN_DETAILED_HANDLES_CMD] = "dummyValue30" # static value
        dummyDict[ConnectConstants.SESSION_RESUME_INCLUDE_FILTER_CMD] = "dummyValue31" # static value
        dummyDict[ConnectConstants.SESSION_RESUME_KEYS_CMD] = "dummyValue32" # static value
        dummyDict[ConnectConstants.SYNC_CMD] = "dummyValue33" # static value
        dummyDict[ConnectConstants.TCL_PROXY_USERNAME_CMD] = "dummyValue34" # static value
        dummyDict[ConnectConstants.TCL_SERVER_CMD] = "dummyValue35" # static value
        dummyDict[ConnectConstants.TIMEOUT_CMD] = "dummyValue36" # static value
        dummyDict[ConnectConstants.USERNAME_CMD] = "dummyValue37" # static value
        dummyDict[ConnectConstants.VPORT_COUNT_CMD] = "dummyValue38" # static value
        dummyDict[ConnectConstants.VPORT_LIST_CMD] = "dummyValue39" # static value

        api = device.getApi(ConnectConstants.CONNECT_API)
        assert isinstance(api, ConnectApi)
        api.connect(dummyDict)
    """
    def connect(self, argdictionary, supported = None):
        self.process_supported_hltapi_commands(argdictionary, supported)
        return self.send_command_args(self._nameSpace +"::connect", argdictionary)

    def connect_helper(self, device, port_list, argdictionary):
        """
        Helper Method: connect
        Keyword arguments:
        device --
        port_list --
        argdictionary --
        """
        temp_dict = dict()
        temp_dict["device"] = device
        temp_dict["port_list"] = port_list
        if isinstance(argdictionary,dict):
            temp_dict.update(argdictionary)
        return self.connect(temp_dict)

    """
    Individual commands for each option. Typically, the "One Large Method"
    is the one that you want to be using so look at that example above
    """
    def connect_aggregation_mode(self, param_string):
        return self.logger.log_unimplemented_method()

    def connect_aggregation_resource_mode(self, param_string):
        return self.logger.log_unimplemented_method()

    def connect_break_locks(self, bool_opt):
        """
        This is the method the command: connect option break_locks
        Description:Valid choices are:
            0     Force option is not used.
            1     Force option is used when taking ownership.
            DEFAULT

            1
        Constants Available: BREAK_LOCKS_CMD
        Supported:IxNetwork-NGPF
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.BREAK_LOCKS_CMD : bool_opt})

    def connect_chain_cables_length(self, any):
        return self.logger.log_unimplemented_method()

    def connect_chain_sequence(self, any):
        return self.logger.log_unimplemented_method()

    def connect_chain_type(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_close_server_on_disconnect(self, bool_opt):
        """
        This is the method the command: connect option close_server_on_disconnect
        Description:When connecting to an IxNetwork Proxy Server this flag will be used to
            determine if the IxNetwork session will be closed (shutdown) after the
            user disconnects or it will remain Idle to allow future session resume.
            This parameter is ignored when not connecting to a IxNetwork Proxy
            Server using IxTclNetwork (new API).
            DEFAULT

            1
            IxNetwork-NGPF

            DESCRIPTION

            When connecting to an IxNetwork Proxy Server this flag will be used to
            determine if the IxNetwork session will be closed (shutdown) after the
            user disconnects or it will remain Idle to allow future session resume.
            This parameter is ignored when not connecting to a IxNetwork Proxy
            Server using IxTclNetwork (new API).
            DEFAULT

            1
        Constants Available: CLOSE_SERVER_ON_DISCONNECT_CMD
        Supported:IxNetwork
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CLOSE_SERVER_ON_DISCONNECT_CMD : bool_opt})

    def connect_config_file(self, any):
        return self.logger.log_unimplemented_method()

    def connect_config_file_hlt(self, any):
        """
        This is the method the command: connect option config_file_hlt
        Description:Name of a file containing HLT configuration information. Valid only with
            an IxNetwork HLTSET as part of the session resume capabilities.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Name of a file containing HLT configuration information. Valid only with
            an IxNetwork HLTSET as part of the session resume capabilities.
            DEFAULT
                None
        Constants Available: CONFIG_FILE_HLT_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.CONFIG_FILE_HLT_CMD : any})

    def connect_connect_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def connect_device(self, ip_address):
        """
        This is the method the command: connect option device
        Description:IP address or name of the chassis. May contain a list of devices. When IxNetwork Tcl API is used this parameter can have one of the following 4 meanings: 1. When 'vport_list' and 'vport_count' parameters are missing, a new chassis is added, virtual ports are created and connected to the real ports specified with 'port_list' parameter. 2. When 'vport_count' is specified this parameter is ignored and 'vport_count' virtual ports are created. They will not be connected. 3. When 'vport_list' exists and -mode is 'connect' a connection to the 'device' chassis will be established. The real ports specified with 'port_list' will be connected to the virtual ports specified with 'vport_list'. The length and structure of the parameters 'port_list' and 'vport_list' must be the same (e.g. -port_list {{2/3 2/4} {1/2 1/3 1/4}} -vport_list {{0/0/1 0/0/2} {0/0/3 0/0/4 0/0/5}}). 4. When 'vport_list' exists and -mode is 'disconnect' this parameter will be ignored and the virtual ports specified with 'vport_list' will be disconnected from the real ports they are currently connected to.
        Constants Available: DEVICE_CMD
        Supported:IxNetwork,, IxOS/IxNetwork-FT,IxNetwork-NGPF
        Keyword arguments:
        ip_address --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.DEVICE_CMD : ip_address})

    def connect_enable_win_tcl_server(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_execution_timeout(self, numeric):
        return self.logger.log_unimplemented_method()

    def connect_forceload(self):
        """
        This is the method the command: connect option forceload
        Description:Supported platforms     Details
                    RETURN VALUES
            Supported Platform     Details
            IxNetwork-NGPF and IxOS/IxNetwork-FT and IxNetwork

            status

            $::SUCCESS | $::FAILURE
            log

            On status of failure, gives detailed information.
            vport_list

            List of virtual port handles.
            traffic_config

            a list having as elements the names of the existing traffic items (the
            name of the traffic item is normally returned when traffic_config
            creates a new traffic item by the stream_id key)
            vport_protocols_handle

            keyed list containing the vport protocols handle
            connection.client_version

            The IxNetwork version found on client
            connection.chassis.$device.hostname

            The hostname of the chassis
            connection.chassis.$device.ip

            The ip address of the chassis
            connection.chassis.$device.chassis_protocols_version

            The IxNetwork Protocols version found on the chassis
            connection.chassis.$device.chassis_type

            The type of the chassis
            connection.chassis.$device.chassis_version

            The IxOS version found on the chassis
            IxNetwork-NGPF

            port_handle.$device.$port

            Port in the form of c/l/p.
            $port_handle.connect

            keyed list with the following keys 'vport_list'
            $port_handle.emulation_bfd_config

            keyed list with the following keys 'router_handles
            router_interface_handles.__parent interface_handles.__parent'
            $port_handle.emulation_bfd_session_config

            keyed list with the following keys 'session_handles'
            $port_handle.emulation_bgp_config

            keyed list with the following keys 'handles'
            $port_handle.emulation_bgp_route_config

            keyed list with the following keys 'bgp_routes bgp_sites.__parent
            bgp_sites.__parent'
            $port_handle.emulation_cfm_config

            keyed list with the following keys 'handle interface_handles'
            $port_handle.emulation_cfm_custom_tlv_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_cfm_links_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_cfm_md_meg_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_cfm_mip_mep_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_cfm_vlan_config

            keyed list with the following keys 'handle mac_range_handles.__parent'
            $port_handle.emulation_dhcp_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_dhcp_group_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_dhcp_server_config

            keyed list with the following keys 'handle handle.dhcp_handle'
            $port_handle.emulation_efm_config

            keyed list with the following keys 'information_oampdu_id
            event_notification_oampdu_id'
            $port_handle.emulation_efm_org_var_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_eigrp_config

            keyed list with the following keys 'router_handles interface_handles
            __parent.connected_interface_handles __parent.gre_interface_handles'
            $port_handle.emulation_eigrp_route_config

            keyed list with the following keys 'session_handles'
            $port_handle.emulation_igmp_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_igmp_group_config

            keyed list with the following keys 'handle source_handle'
            $port_handle.emulation_isis_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_isis_topology_route_config

            keyed list with the following keys 'elem_handle version route_range
            stub.num_networks external.num_networks
            grid.connected_session__parent.row grid.connected_session__parent.col
            grid.connected_session.__parent.row grid.connected_session.__parent.col'
            $port_handle.emulation_lacp_link_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_ldp_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_ldp_route_config

            keyed list with the following keys 'lsp_handle lsp_intf
            lsp_vc_range_handles lsp_vc_ip_range_handles lsp_vc_mac_range_handles'
            $port_handle.emulation_mld_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_mld_group_config

            keyed list with the following keys 'handle group_pool_handle
            source_pool_handles'
            $port_handle.emulation_oam_config_msg

            keyed list with the following keys 'handle'
            $port_handle.emulation_oam_config_topology

            keyed list with the following keys 'handle traffic_handles'
            $port_handle.emulation_ospf_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_ospf_topology_route_config

            keyed list with the following keys 'elem_handle'
            $port_handle.emulation_pbb_config

            keyed list with the following keys 'handle interface_handles'
            $port_handle.emulation_pbb_trunk_config

            keyed list with the following keys 'trunk_handle mr_handle'
            $port_handle.emulation_pim_config

            keyed list with the following keys 'handle interfaces'
            $port_handle.emulation_pim_group_config

            keyed list with the following keys 'handle group_pool_handle
            source_pool_handles'
            $port_handle.emulation_rip_config

            keyed list with the following keys 'handle handle'
            $port_handle.emulation_rip_route_config

            keyed list with the following keys 'route_handle'
            $port_handle.emulation_rsvp_config

            keyed list with the following keys 'handles
            router_interface_handle.__parent'
            $port_handle.emulation_rsvp_tunnel_config

            keyed list with the following keys 'tunnel_handle
            tunnel_leaves_handle.__parent/ingress routed_interfaces.__parent/ingress
            tunnel_leaves_handle.__parent'
            $port_handle.emulation_stp_bridge_config

            keyed list with the following keys 'bridge_handle
            bridge_interface_handles.__parent interface_handles.__parent'
            $port_handle.emulation_stp_msti_config

            keyed list with the following keys 'handle'
            $port_handle.interface_config

            keyed list with the following keys 'interface_handle
            routed_interface_handle gre_interface_handle'
            $port_handle.l2tp_config

            keyed list with the following keys 'handles'
            $port_handle.pppox_config

            keyed list with the following keys 'handles'
            $port_handle.emulation_twamp_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_twamp_control_range_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_twamp_test_range_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_twamp_server_range_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_ancp_config

            keyed list with the following keys 'handle'
            $port_handle.emulation_ancp_subscriber_lines_config

            keyed list with the following keys 'handle'
            $port_handle.fc_client_config

            keyed list with the following keys 'handle'
            $port_handle.fc_fport_config

            keyed list with the following keys 'handle'
            $port_handle.fc_fport_vnport_config

            keyed list with the following keys 'handle'
            $stream_id.traffic_config

            keyed list with all the keys that the traffic_config procedure would
            return when configuring the $stream_id traffic item
            IxOS/IxNetwork-FT and IxNetwork

            <port_handle>.connect

            keyed list with the following keys 'vport_list'
            <port_handle>.emulation_bfd_config

            keyed list with the following keys 'router_handles
            router_interface_handles.<parent> interface_handles.<parent>'. Where
            <parent> is an object of type /vport/protocols/bfd/router.
            <port_handle>.emulation_bfd_session_config

            keyed list with the following keys 'session_handles'
            <port_handle>.emulation_bgp_config

            keyed list with the following keys 'handles'
            <port_handle>.emulation_bgp_route_config

            keyed list with the following keys 'bgp_routes bgp_sites.<parent>'.
            Where <parent> is an object of type
            /vport/protocols/bgp/neighborRange/l2Site, or
            /vport/protocols/bgp/neighborRange/l3Site.
            <port_handle>.emulation_cfm_config

            keyed list with the following keys 'handle interface_handles'
            <port_handle>.emulation_cfm_custom_tlv_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_cfm_links_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_cfm_md_meg_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_cfm_mip_mep_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_cfm_vlan_config

            keyed list with the following keys 'handle mac_range_handles.<parent>'.
            Where <parent> is an object of type /vport/protocols/cfm/bridge/vlans.
            <port_handle>.emulation_dhcp_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_dhcp_group_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_dhcp_server_config

            keyed list with the following keys 'handle handle.dhcp_handle'
            <port_handle>.dhcp_client_extension_config

            keyed list with the following keys 'handle'
            <port_handle>.dhcp_server_extension_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_efm_config

            keyed list with the following keys 'information_oampdu_id
            event_notification_oampdu_id'
            <port_handle>.emulation_efm_org_var_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_eigrp_config

            keyed list with the following keys 'router_handles interface_handles'
            <port_handle>.emulation_elmi_config

            keyed list with the following keys 'uni_handles interface_handles
            uni_status_handles bw_profile_handles evc_handles ce_vlan_id_range_handles'
            <port_handle>.emulation_eigrp_route_config

            keyed list with the following keys 'session_handles'
            <port_handle>.emulation_igmp_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_igmp_group_config

            keyed list with the following keys 'handle source_handle'
            <port_handle>.emulation_isis_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_isis_topology_route_config

            keyed list with the following keys 'elem_handle version route_range
            stub.num_networks external.num_networks
            grid.connected_session<parent>.row grid.connected_session<parent>.col'.
            Where <parent> is an object of type /vport/protocols/isis/router.
            <port_handle>.emulation_lacp_link_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_ldp_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_ldp_route_config

            keyed list with the following keys 'lsp_handle lsp_intf
            lsp_vc_range_handles lsp_vc_ip_range_handles lsp_vc_mac_range_handles'
            <port_handle>.emulation_mld_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_mld_group_config

            keyed list with the following keys 'handle group_pool_handle
            source_pool_handles'
            <port_handle>.emulation_oam_config_msg

            keyed list with the following keys 'handle'
            <port_handle>.emulation_oam_config_topology

            keyed list with the following keys 'handle traffic_handles'
            <port_handle>.emulation_ospf_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_ospf_topology_route_config

            keyed list with the following keys 'elem_handle'
            <port_handle>.emulation_pbb_config

            keyed list with the following keys 'handle interface_handles'
            <port_handle>.emulation_pbb_trunk_config

            keyed list with the following keys 'trunk_handle mr_handle'
            <port_handle>.emulation_pim_config

            keyed list with the following keys 'handle interfaces'
            <port_handle>.emulation_pim_group_config

            keyed list with the following keys 'handle group_pool_handle
            source_pool_handles'
            <port_handle>.emulation_rip_config

            keyed list with the following keys 'handle handle'
            <port_handle>.emulation_rip_route_config

            keyed list with the following keys 'route_handle'
            <port_handle>.emulation_rsvp_config

            keyed list with the following keys 'handles'
            <port_handle>.emulation_rsvp_tunnel_config

            keyed list with the following keys 'tunnel_handle
            tunnel_leaves_handle.<parent>/ingress tunnel_leaves_handle.<parent>'.
            Where <parent> is an object of type
            /vport/protocols/rsvp/neighborPair/destinationRange.
            <port_handle>.emulation_stp_bridge_config

            keyed list with the following keys 'bridge_handle
            bridge_interface_handles.<parent> interface_handles.<parent>'. Where
            <parent> is an object of type /vport/protocols/stp/bridge.
            <port_handle>.emulation_stp_msti_config

            keyed list with the following keys 'handle'
            <port_handle>.interface_config

            keyed list with the following keys 'interface_handle
            routed_interface_handle gre_interface_handle'
            <port_handle>.l2tp_config

            keyed list with the following keys 'handles'
            <port_handle>.pppox_config

            keyed list with the following keys 'handles'
            <port_handle>.emulation_twamp_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_twamp_control_range_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_twamp_test_range_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_twamp_server_range_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_ancp_config

            keyed list with the following keys 'handle'
            <port_handle>.emulation_ancp_subscriber_lines_config

            keyed list with the following keys 'handle'. These profiles are used on
            <port_handle>
            globals.emulation_ancp_subscriber_lines_config

            keyed list with the following keys 'handle'. These profiles are present
            in the configuration
            <port_handle>.fc_client_config

            keyed list with the following keys 'handle'
            <port_handle>.fc_fport_config

            keyed list with the following keys 'handle'
            <port_handle>.fc_fport_vnport_config

            keyed list with the following keys 'handle'
            <stream_id>.traffic_config

            keyed list with all the keys that the traffic_config procedure would
            return when configuring the $stream_id traffic item
            emulation_multicast_group_config

            keyed list with the following keys 'num_groups ip_addr_start
            ip_addr_step ip_prefix_len'
            emulation_multicast_source_config

            keyed list with the following keys 'num_sources ip_addr_start
            ip_addr_step ip_prefix_len'
            connection.using_tcl_proxy

            Boolean value indicating if the IxNetwork process was started using tcl
            proxy feature of not
            connection.process_id

            this is the PID of the IxNetwork process
            connection.session_id

            id of the Tcl Proxy session [used for join/resume functionality]
            connection.tcl_proxy_username

            name of the user owning the IxNetwork instance
            connection.server_version

            The IxNetwork version found on server
            connection.port

            TCL server port of the IxNetwork instance
            connection.rdp

            Boolean value indicating if the IxN process was started using RDP
            feature of not
            connection.state

            ENUM, current state of the process
            connection.start_time

            IxNetwork proxy start time
            connection.hostname

            Hostname of the IxNetwork server
            connection.username

            Username of the IxNetwork server
            connection.close_server_on_disconnect

            Boolean value indicating if the 'ixNet disconnect' call will also
            shutdown IxNetwork process
            traffic_l47_config.traffic_l47_handle

            a list of traffic item handles of the existing L47 AppLib traffic items
            traffic_l47_config.<traffic_l47_handle>.applib_profile

            a list of all the applib profiles under the <traffic_l47_handle>. Where
            <traffic_l47_handle> is an object of type /traffic/trafficItem.
            traffic_l47_config.<traffic_l47_handle>.<applib_profile>.applib_flow

            a list of flows existing under the <applib_profile>. Where
            <applib_profile> is an object of type /traffic/trafficItem/appLibProfile.
            traffic_l47_config.<traffic_l47_handle>.<applib_profile>.<applib_flow>.parameter

            a list of parameters existing under the <applib_flow>. Where the
            <applib_flow> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow.
            traffic_l47_config.<traffic_l47_handle>.<applib_profile>.<applib_flow>.connection

            a list of connections existing under the <applib_flow>. Where the
            <applib_flow> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow.
            traffic_l47_config.<traffic_l47_handle>.<applib_profile>.<applib_flow>.<connection>.parameter

            a list of parameters existing under the <connection>. Where the
            <connection> is an object of type
            /traffic/trafficItem/appLibProfile/appLibFlow/connection.
        Constants Available: FORCELOAD_CMD
        Keyword arguments:
        return -- pass/fail
        """
        return self.connect({ConnectConstants.FORCELOAD_CMD : ""})

    def connect_guard_rail(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_interactive(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_license_servers(self, any):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_license_type(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_tcl_proxy(self, any):
        return self.logger.log_unimplemented_method()

    def connect_ixnetwork_tcl_server(self, any):
        return self.logger.log_unimplemented_method()

    def connect_log_path(self, any):
        return self.logger.log_unimplemented_method()

    def connect_logging(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_master_device(self, any):
        return self.logger.log_unimplemented_method()

    def connect_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_nobios(self, any):
        """
        This is the method the command: connect option nobios
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: NOBIOS_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.NOBIOS_CMD : any})

    def connect_port_list(self, interface_list):
        """
        This is the method the command: connect option port_list
        Description:List of Ixia ports of which to take ownership. If multiple devices are specified, then this is a list of lists. A single item is of the form card number // port number. So card 2, port 4 would look like 2/4. This parameter depends on 'vport_list' and 'vport_count' parameters. More details are available in the description for parameter 'device'.
        Constants Available: PORT_LIST_CMD
        Supported:IxNetwork [M] , IxOS/IxNetwork-FT [M], IxNetwork-NGPF
        Keyword arguments:
        interface_list --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.PORT_LIST_CMD : interface_list})

    def connect_protocol_stacking_mode(self, opt):
        return self.logger.log_unimplemented_method()

    def connect_reset(self):
        """
        This is the method the command: connect option reset
        Description:Resets the card to factory defaults.

            When IxTclNetwork is used, the presence of this flag will reset all previous connections to chassis and ports. If this flag is missing and this is the first connect call from the script, the configuration will be imported from the IxNetwork Tcl Server and will be returned as keyed list (see Return Values section).
        Constants Available: RESET_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT,IxNetwork-NGPF
        Keyword arguments:
        return -- pass/fail
        """
        return self.connect({ConnectConstants.RESET_CMD : ""})

    def connect_return_detailed_handles(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_session_resume_include_filter(self, any):
        return self.logger.log_unimplemented_method()

    def connect_session_resume_keys(self, bool_opt):
        return self.logger.log_unimplemented_method()

    def connect_sync(self, bool_opt):
        """
        This is the method the command: connect option sync
        Description:If enabled, the ixClearTimeStamps routine is called for the reserved
            port list.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            If enabled, the ixClearTimeStamps routine is called for the reserved
            port list.
            DEFAULT

            1
        Constants Available: SYNC_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        bool_opt --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.SYNC_CMD : bool_opt})

    def connect_tcl_proxy_username(self, any):
        """
        This is the method the command: connect option tcl_proxy_username
        Description:Username for logging in IxNetwork Tcl Proxy server.
            This parameter is ignored when IxNetwork Tcl Proxy server is not used
            for connecting to IxNetwork. In this case, the username will be
            configured automatically at ::<namespace>::interface_config and will
            have the value 'IxNetwork/$(COMPUTERNAME)/$(USERNAME)'.
            However, when connecting to an IxNetwork Tcl Proxy Server this parameter
            is used to determine the username of the IxNetwork instance to which the
            Proxy Server will connect to.
            DEFAULT
                None
            IxNetwork-NGPF

            DESCRIPTION

            Username for logging in IxNetwork Tcl Proxy server.
            This parameter is ignored when IxNetwork Tcl Proxy server is not used
            for connecting to IxNetwork. In this case, the username will be
            configured automatically at ::::interface_config and will have the value
            'IxNetwork/$(COMPUTERNAME)/$(USERNAME)'.
            However, when connecting to an IxNetwork Tcl Proxy Server this parameter
            is used to determine the username of the IxNetwork instance to which the
            Proxy Server will connect to.
            DEFAULT
                None
        Constants Available: TCL_PROXY_USERNAME_CMD
        Supported:IxNetwork
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.TCL_PROXY_USERNAME_CMD : any})

    def connect_tcl_server(self, any):
        return self.logger.log_unimplemented_method()

    def connect_timeout(self, any):
        """
        This is the method the command: connect option timeout
        Description:Not supported
            DEFAULT
                Not supported
        Constants Available: TIMEOUT_CMD
        Supported:IxNetwork, IxOS/IxNetwork-FT
        Keyword arguments:
        any --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.TIMEOUT_CMD : any})

    def connect_username(self, name):
        """
        This is the method the command: connect option username
        Description:Username for logging in on the chassis.

            This parameter is ignored when using IxTclNetwork (new API) for connecting to an IxNetwork TCL Server. In this case, the username will be configured automatically at ::<namespace>::interface_config and will have the value 'IxNetwork/$(COMPUTERNAME)/$(USERNAME)'.
        Constants Available: USERNAME_CMD
        Supported:IxNetwork, IxNetwork-NGPF
        Keyword arguments:
        name --
        return -- pass/fail
        """
        return self.connect({ConnectConstants.USERNAME_CMD : name})

    def connect_vport_count(self, range):
        return self.logger.log_unimplemented_method()

    def connect_vport_list(self, any):
        return self.logger.log_unimplemented_method()


"""
    This is the Constants class for the command: connect
    Commands end with _CMD and constants for a command start with the beginning
    with the command's constant name minus the _CMD
"""


class ConnectConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    CONNECT_API = "CONNECT_API"

    AGGREGATION_MODE_CMD = "aggregation_mode"
    # Constant values for AGGREGATION_MODE_CMD
    AGGREGATION_MODE_NORMAL = "normal"
    AGGREGATION_MODE_MIXED = "mixed"
    AGGREGATION_MODE_NOT_SUPPORTED = "not_supported"
    AGGREGATION_MODE_SINGLE_MODE_AGGREGATION = "single_mode_aggregation"
    AGGREGATION_MODE_DUAL_MODE_AGGREGATION = "dual_mode_aggregation"
    AGGREGATION_MODE_HUNDRED_GIG_NON_FAN_OUT = "hundred_gig_non_fan_out"
    AGGREGATION_MODE_FORTY_GIG_AGGREGATION = "forty_gig_aggregation"
    AGGREGATION_MODE_FORTY_GIG_FAN_OUT = "forty_gig_fan_out"
    AGGREGATION_MODE_FORTY_GIG_NORMAL_MODE = "forty_gig_normal_mode"
    AGGREGATION_MODE_FOUR_BY_TWENTY_FIVE_GIG_NON_FAN_OUT = "four_by_twenty_five_gig_non_fan_out"
    AGGREGATION_MODE_TEN_GIG_AGGREGATION = "ten_gig_aggregation"
    AGGREGATION_MODE_TEN_GIG_FAN_OUT = "ten_gig_fan_out"
    AGGREGATION_MODE_THREE_BY_TEN_GIG_FAN_OUT = "three_by_ten_gig_fan_out"
    AGGREGATION_MODE_FOUR_BY_TEN_GIG_FAN_OUT = "four_by_ten_gig_fan_out"
    AGGREGATION_MODE_EIGHT_BY_TEN_GIG_FAN_OUT = "eight_by_ten_gig_fan_out"

    AGGREGATION_RESOURCE_MODE_CMD = "aggregation_resource_mode"
    # Constant values for AGGREGATION_RESOURCE_MODE_CMD
    AGGREGATION_RESOURCE_MODE_NORMAL = "normal"
    AGGREGATION_RESOURCE_MODE_DUAL_MODE_AGGREGATION = "dual_mode_aggregation"
    AGGREGATION_RESOURCE_MODE_SINGLE_MODE_AGGREGATION = "single_mode_aggregation"
    AGGREGATION_RESOURCE_MODE_FORTY_GIG_AGGREGATION = "forty_gig_aggregation"
    AGGREGATION_RESOURCE_MODE_HUNDRED_GIG_NON_FAN_OUT = "hundred_gig_non_fan_out"
    AGGREGATION_RESOURCE_MODE_FORTY_GIG_FAN_OUT = "forty_gig_fan_out"
    AGGREGATION_RESOURCE_MODE_FORTY_GIG_NORMAL_MODE = "forty_gig_normal_mode"
    AGGREGATION_RESOURCE_MODE_FOUR_BY_TWENTY_FIVE_GIG_NON_FAN_OUT = "four_by_twenty_five_gig_non_fan_out"
    AGGREGATION_RESOURCE_MODE_TEN_GIG_AGGREGATION = "ten_gig_aggregation"
    AGGREGATION_RESOURCE_MODE_TEN_GIG_FAN_OUT = "ten_gig_fan_out"
    AGGREGATION_RESOURCE_MODE_EIGHT_BY_TEN_GIG_FAN_OUT = "eight_by_ten_gig_fan_out"
    AGGREGATION_RESOURCE_MODE_THREE_BY_TEN_GIG_FAN_OUT = "three_by_ten_gig_fan_out"
    AGGREGATION_RESOURCE_MODE_FOUR_BY_TEN_GIG_FAN_OUT = "four_by_ten_gig_fan_out"

    BREAK_LOCKS_CMD = "break_locks"

    CHAIN_CABLES_LENGTH_CMD = "chain_cables_length"

    CHAIN_SEQUENCE_CMD = "chain_sequence"

    CHAIN_TYPE_CMD = "chain_type"
    # Constant values for CHAIN_TYPE_CMD
    CHAIN_TYPE_DAISY = "daisy"
    CHAIN_TYPE_NONE = "none"
    CHAIN_TYPE_STAR = "star"

    CLOSE_SERVER_ON_DISCONNECT_CMD = "close_server_on_disconnect"

    CONFIG_FILE_CMD = "config_file"

    CONFIG_FILE_HLT_CMD = "config_file_hlt"

    CONNECT_TIMEOUT_CMD = "connect_timeout"

    DEVICE_CMD = "device"

    ENABLE_WIN_TCL_SERVER_CMD = "enable_win_tcl_server"

    EXECUTION_TIMEOUT_CMD = "execution_timeout"

    FORCELOAD_CMD = "forceload"

    GUARD_RAIL_CMD = "guard_rail"
    # Constant values for GUARD_RAIL_CMD
    GUARD_RAIL_NONE = "none"
    GUARD_RAIL_STATISTICS = "statistics"

    HELPER_CMD = "helper"

    INTERACTIVE_CMD = "interactive"

    IXNETWORK_LICENSE_SERVERS_CMD = "ixnetwork_license_servers"

    IXNETWORK_LICENSE_TYPE_CMD = "ixnetwork_license_type"
    # Constant values for IXNETWORK_LICENSE_TYPE_CMD
    IXNETWORK_LICENSE_TYPE_MIXED = "mixed"
    IXNETWORK_LICENSE_TYPE_PERPETUAL = "perpetual"
    IXNETWORK_LICENSE_TYPE_SUBSCRIPTION_TIER0 = "subscription_tier0"
    IXNETWORK_LICENSE_TYPE_SUBSCRIPTION_TIER1 = "subscription_tier1"
    IXNETWORK_LICENSE_TYPE_SUBSCRIPTION_TIER2 = "subscription_tier2"
    IXNETWORK_LICENSE_TYPE_SUBSCRIPTION_TIER3 = "subscription_tier3"

    IXNETWORK_TCL_PROXY_CMD = "ixnetwork_tcl_proxy"

    IXNETWORK_TCL_SERVER_CMD = "ixnetwork_tcl_server"

    LOG_PATH_CMD = "log_path"

    LOGGING_CMD = "logging"
    # Constant values for LOGGING_CMD
    LOGGING_HLTAPI_CALLS = "hltapi_calls"

    MASTER_DEVICE_CMD = "master_device"

    MODE_CMD = "mode"
    # Constant values for MODE_CMD
    MODE_CONNECT = "connect"
    MODE_DISCONNECT = "disconnect"
    MODE_RECONNECT_PORTS = "reconnect_ports"
    MODE_SAVE = "save"

    NOBIOS_CMD = "nobios"

    PORT_LIST_CMD = "port_list"

    PROTOCOL_STACKING_MODE_CMD = "protocol_stacking_mode"
    # Constant values for PROTOCOL_STACKING_MODE_CMD
    PROTOCOL_STACKING_MODE_PARALLEL = "parallel"
    PROTOCOL_STACKING_MODE_SEQUENTIAL = "sequential"

    RESET_CMD = "reset"

    RETURN_DETAILED_HANDLES_CMD = "return_detailed_handles"

    SESSION_RESUME_INCLUDE_FILTER_CMD = "session_resume_include_filter"

    SESSION_RESUME_KEYS_CMD = "session_resume_keys"

    SYNC_CMD = "sync"

    TCL_PROXY_USERNAME_CMD = "tcl_proxy_username"

    TCL_SERVER_CMD = "tcl_server"

    TIMEOUT_CMD = "timeout"

    USERNAME_CMD = "username"

    VPORT_COUNT_CMD = "vport_count"

    VPORT_LIST_CMD = "vport_list"

    # don't allow values to be updated
    def __setattr__(self, *_):
        pass

"""
Implemented Commands (Alphabetical)
    -aggregation_mode
    -aggregation_resource_mode
    -break_locks
    -chain_cables_length
    -chain_sequence
    -chain_type
    -close_server_on_disconnect
    -config_file
    -config_file_hlt
    -connect_timeout
    -device
    -enable_win_tcl_server
    -execution_timeout
    -forceload
    -guard_rail
    -helper
    -interactive
    -ixnetwork_license_servers
    -ixnetwork_license_type
    -ixnetwork_tcl_proxy
    -ixnetwork_tcl_server
    -log_path
    -logging
    -master_device
    -mode
    -nobios
    -port_list
    -protocol_stacking_mode
    -reset
    -return_detailed_handles
    -session_resume_include_filter
    -session_resume_keys
    -sync
    -tcl_proxy_username
    -tcl_server
    -timeout
    -username
    -vport_count
    -vport_list
If you want to update this file, look in the CSV
"""
