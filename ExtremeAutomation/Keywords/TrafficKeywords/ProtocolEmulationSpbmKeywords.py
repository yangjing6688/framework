from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationSpbmKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationSpbmKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                              pnode_id, spb_instance, cost="10", options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]  - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]  - The name for the emulated bridge.
        [mac_addr]     - The source MAC address for the interface.
        [vlan_id]      - The VLAN ID of the interface.
        [svlan_id]     - The Service VLAN ID.
        [area]         - The ISIS Area ID.
        [sys_id]       - The system ID.
        [pnode_id]     - The partner node ID.
        [spb_instance] - The SPB instance ID.
        [cost]         - The ISIS interface path cost.
        [options]      - A dictionary of available options to include on the interface.

        Creates an emulated ISIS interface.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.SPB_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_isis_interface(self.current_port, bridge_name, mac_addr, vlan_id, svlan_id, area,
                                                 sys_id, pnode_id, spb_instance, cost, options)

        self._keyword_cleanup()

    def set_isis_globals(self, tgen_name, hello_interval=9, isi_multiplier=3, retrans_lsp_interval=5, options=None,
                         **kwargs):
        """
        Keyword Arguments:
        [tgen_name]            - The name of the Traffic Generator to configure.
        [hello_interval]       - The ISIS hello interval.
        [isi_multiplier]       - The ISIS hello multiplier value.
        [retrans_lsp_interval] - The LSP retransmit interval.
        [options]              - A dictionary of available options.

        Configured the global ISIS parameters.
        """
        self._init_keyword(tgen_name, self.emulation_constants.SPB_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.set_isis_globals(hello_interval, isi_multiplier, retrans_lsp_interval,
                                            options)

        self._keyword_cleanup()

    def set_bridge_enabled(self, tgen_name, enable=True, **kwargs):
        """
        Keyword Arguments:
        [tgen_name] - The name of the Traffic Generator to configure.
        [enable]    - The ISIS hello interval.

        Enables the emulated bridge.
        """
        self._init_keyword(tgen_name, self.emulation_constants.SPB_API, **kwargs)

        self.emulation_api.set_bridge_enabled(enable)

        self._keyword_cleanup()

    def create_and_go_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                                     pnode_id, spb_instance, cost="10", enable=True, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]  - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]  - The name for the emulated bridge.
        [mac_addr]     - The source MAC address for the interface.
        [vlan_id]      - The VLAN ID of the interface.
        [svlan_id]     - The Service VLAN ID.
        [area]         - The ISIS Area ID.
        [sys_id]       - The system ID.
        [pnode_id]     - The partner node ID.
        [spb_instance] - The SPB instance ID.
        [cost]         - The ISIS interface path cost.
        [options]      - A dictionary of available options to include on the interface.

        Creates and enables an emulated ISIS interface.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.SPB_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_and_go_isis_interface(self.current_port, bridge_name, mac_addr, vlan_id, svlan_id,
                                                        area, sys_id, pnode_id, spb_instance, cost, enable, options)

        self._keyword_cleanup()

    def create_isis_ipv4_route_stack(self, port_string, bridge_name, create_stack, starting_ip, netmask, gateway_ip,
                                     num_routes, cost, step, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]  - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]  - The name for the emulated bridge.
        [create_stack] - The source MAC address for the interface.
        [starting_ip]  - The first IP address of the route stack.
        [netmask]      - The IP address netmask for all routes in the stack.
        [gateway_ip]   - The gateway IP for the route stack.
        [num_routes]   - The total number of routes to create.
        [cost]         - The route cost for the stack.
        [step]         - The step increment between routes in the stack.
        [options]      - A dictionary of available options to include on the interface.

        Creates the defined number of IPv4 routes for ISIS.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.SPB_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_isis_ipv4_route_stack(self.current_port, bridge_name, create_stack, starting_ip,
                                                        netmask, gateway_ip, num_routes, cost, step, options)

        self._keyword_cleanup()

    def create_isis_ipv6_route_stack(self, port_string, bridge_name, create_stack, shortcut_ip, starting_ip,
                                     prefix_length, num_routes, cost, step, l3isid, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]   - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]   - The name for the emulated bridge.
        [create_stack]  - The source MAC address for the interface.
        [shortcut_ip]   - The IPv6 shortcut for the route stack.
        [starting_ip]   - The first IP address of the route stack.
        [prefix_length] - The IPv6 prefix-length for all routes in the stack.
        [num_routes]    - The total number of routes to create.
        [cost]          - The route cost for the stack.
        [step]          - The step increment between routes in the stack.
        [l3isid]        - The L3 ISIS ID.
        [options]       - A dictionary of available options to include on the interface.

        Creates the defined number of IPv6 routes for ISIS.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.SPB_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_isis_ipv6_route_stack(self.current_port, bridge_name, create_stack, shortcut_ip,
                                                        starting_ip, prefix_length, num_routes, cost, step, l3isid,
                                                        options)

        self._keyword_cleanup()

    def create_l2vsn_ipv4_endpoint(self, tgen_name, bridge_name, base_name, isis_id, endpoint_ip, endpoint_mask,
                                   endpoint_mac, num_eps=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]     - The name of the Traffic Generator to configure.
        [bridge_name]   - The name of the emulated bridge.
        [base_name]     - The base name of the endpoint.
        [isis_id]       - The ISIS ID of the endpoint.
        [endpoint_ip]   - The IP Address of the endpoint.
        [endpoint_mask] - The Network Mask for the endpoint IP Address.
        [endpoint_mac]  - The MAC address of the endpoint.
        [num_eps]       - The total number of endpoints to create.
        [options]       - A dictionary of available options to include on the interface.

        Creates the given L2 virtual service network IPv4 endpoint.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_l2vsn_ipv4_endpoint(bridge_name, base_name, isis_id, endpoint_ip, endpoint_mask,
                                                      endpoint_mac, num_eps, options)

        self._keyword_cleanup()

    def create_routed_l2vsn_ipv4_endpoint(self, tgen_name, bridge_name, base_name, isis_id, endpoint_ip, endpoint_mask,
                                          endpoint_gateway, endpoint_mac, num_eps=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]        - The name of the Traffic Generator to configure.
        [bridge_name]      - The name for the emulated bridge.
        [base_name]        - The base name of the endpoint.
        [isis_id]          - The ISIS ID of the endpoint.
        [endpoint_ip]      - The IP Address of the endpoint.
        [endpoint_mask]    - The Network Mask for the endpoint IP Address.
        [endpoint_gateway] - The route gateway for the endpoint.
        [endpoint_mac]     - The MAC address of the endpoint.
        [num_eps]          - The total number of endpoints to create.
        [options]          - A dictionary of available options to include on the interface.

        Creates the given L2 virtual service network IPv4 endpoint via routed gateway.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_routed_l2vsn_ipv4_endpoint(bridge_name, base_name, isis_id, endpoint_ip,
                                                             endpoint_mask, endpoint_gateway, endpoint_mac, num_eps,
                                                             options)

        self._keyword_cleanup()

    def create_routed_l2vsn_ipv6_endpoint(self, tgen_name, bridge_name, base_name, isis_id, endpoint_ip,
                                          endpoint_prefix_length, endpoint_mac, num_eps=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]              - The name of the Traffic Generator to configure.
        [bridge_name]            - The name for the emulated bridge.
        [base_name]              - The base name of the endpoint.
        [isis_id]                - The ISIS ID of the endpoint.
        [endpoint_ip]            - The IP Address of the endpoint.
        [endpoint_prefix_length] - The Network Mask for the endpoint IP Address.
        [endpoint_mac]           - The MAC address of the endpoint.
        [num_eps]                - The total number of endpoints to create.
        [options]                - A dictionary of available options to include on the interface.

        Creates the given L2 virtual service network IPv6 endpoint via routed gateway.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_routed_l2vsn_ipv6_endpoint(bridge_name, base_name, isis_id, endpoint_ip,
                                                             endpoint_prefix_length, endpoint_mac, num_eps,
                                                             options)

        self._keyword_cleanup()

    def create_l2vsn_ipv6_endpoint(self, tgen_name, bridge_name, base_name, isis_id, endpoint_ip,
                                   endpoint_prefix_length, endpoint_mac, num_eps=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]              - The name of the Traffic Generator to configure.
        [bridge_name]            - The name for the emulated bridge.
        [base_name]              - The base name of the endpoint.
        [isis_id]                - The ISIS ID of the endpoint.
        [endpoint_ip]            - The IP Address of the endpoint.
        [endpoint_prefix_length] - The Network Mask for the endpoint IP Address.
        [endpoint_mac]           - The MAC address of the endpoint.
        [num_eps]                - The total number of endpoints to create.
        [options]                - A dictionary of available options to include on the interface.

        Creates the given L2 virtual service network IPv6 endpoint.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_l2vsn_ipv6_endpoint(bridge_name, base_name, isis_id, endpoint_ip,
                                                      endpoint_prefix_length, endpoint_mac, num_eps, options)

        self._keyword_cleanup()

    def create_l3vsn_ipv4_endpoint(self, tgen_name, bridge_name, base_name, isis_id, starting_ip, endpoint_ip,
                                   endpoint_mask, num_eps=1, num_routes=1, cost=1, step=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]        - The name of the Traffic Generator to configure.
        [bridge_name]      - The name for the emulated bridge.
        [base_name]        - The base name of the endpoint.
        [isis_id]          - The ISIS ID of the endpoint.
        [starting_ip]      - The first IP address in the VSN.
        [endpoint_ip]      - The IP Address of the endpoint.
        [endpoint_mask]    - The Network Mask for the endpoint IP Address.
        [num_eps]          - The number of endpoints to create.
        [num_routes]       - The number of routes in the VSN.
        [cost]             - The route cost of the endpoint.
        [step]             - The step increment between endpoints.
        [options]          - A dictionary of available options to include on the interface.

        Creates the given L3 virtual service network IPv4 endpoint.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_l3vsn_ipv4_endpoint(bridge_name, base_name, isis_id, starting_ip, endpoint_ip,
                                                      endpoint_mask, num_eps, num_routes, cost, step, options)

        self._keyword_cleanup()

    def create_l3vsn_ipv6_endpoint(self, tgen_name, bridge_name, base_name, isis_id, starting_ip, endpoint_ip,
                                   prefix_length, num_eps=1, num_routes=1, cost=1, step=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [tgen_name]        - The name of the Traffic Generator to configure.
        [bridge_name]      - The name for the emulated bridge.
        [base_name]        - The base name of the endpoint.
        [isis_id]          - The ISIS ID of the endpoint.
        [starting_ip]      - The first IP address in the VSN.
        [endpoint_ip]      - The IP Address of the endpoint.
        [endpoint_mask]    - The Network Mask for the endpoint IP Address.
        [num_eps]          - The number of endpoints to create.
        [num_routes]       - The number of routes in the VSN.
        [cost]             - The route cost of the endpoint.
        [step]             - The step increment between endpoints.
        [options]          - A dictionary of available options to include on the interface.

        Creates the given L3 virtual service network IPv6 endpoint.
        """
        self._init_keyword(tgen_name, self.emulation_constants.END_STATION_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_l3vsn_ipv6_endpoint(bridge_name, base_name, isis_id, starting_ip, endpoint_ip,
                                                      prefix_length, num_eps, num_routes, cost, step, options)

        self._keyword_cleanup()

    def advetise_ipv4_routes(self, port_string, bridge_name, shortcut_ip, shortcut_netmask, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]      - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]      - The name for the emulated bridge.
        [shortcut_ip]      - The shortcut IP address.
        [shortcut_netmask] - The netmask of the shortcut IP.
        [options]          - A dictionary of available options to include on the interface.

        Advertises the configured IPv4 routes over ISIS SPBM.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.ROUTE_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.advetise_ipv4_routes(self.current_port, bridge_name, shortcut_ip, shortcut_netmask, options)

        self._keyword_cleanup()

    def enable_ipv4_shortcuts(self, port_string, bridge_name, shortcut_ip=None, shortcut_netmask='255.255.255.255',
                              **kwargs):
        """
        Keyword Arguments:
        [port_string]      - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]      - The name for the emulated bridge.
        [shortcut_ip]      - The shortcut IP address.
        [shortcut_netmask] - The netmask of the shortcut IP.

        Enables the IPv4 shortcut IP.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.ROUTE_API, **kwargs)

        self.emulation_api.enable_ipv4_shortcuts(self.current_port, bridge_name, shortcut_ip, shortcut_netmask)

        self._keyword_cleanup()

    def advetise_ipv6_routes(self, port_string, bridge_name, shortcut_ip, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]  - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]  - The name for the emulated bridge.
        [shortcut_ip]  - The shortcut IP address.
        [options]      - A dictionary of available options to include on the interface.

        Advertises the configured IPv6 routes over ISIS SPBM.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.ROUTE_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.advetise_ipv6_routes(self.current_port, bridge_name, shortcut_ip, options)

        self._keyword_cleanup()

    def enable_ipv6_shortcuts(self, port_string, bridge_name, shortcut_ip=None, **kwargs):
        """
        Keyword Arguments:
        [port_string]      - A dictionary of the tgen_port and tgen_name to configure.
        [bridge_name]      - The name for the emulated bridge.
        [shortcut_ip]      - The shortcut IP address.
        [shortcut_netmask] - The netmask of the shortcut IP.

        Enables the IPv6 shortcut IP.
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.ROUTE_API, **kwargs)

        self.emulation_api.enable_ipv6_shortcuts(self.current_port, bridge_name, shortcut_ip)

        self._keyword_cleanup()
