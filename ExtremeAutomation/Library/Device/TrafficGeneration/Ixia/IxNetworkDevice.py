from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigApi, InterfaceConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingCommandObject import \
    TrafficGeneratingCommandObject
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficControlApi import \
    TrafficControlApi, TrafficControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiTrafficConfigApi import \
    TrafficConfigConstants, TrafficConfigApi
#######
# BGP
#######
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpConfig import \
    EmulationBgpConfigApi, EmulationBgpConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpRouteConfigApi import \
    EmulationBgpRouteConfigApi, EmulationBgpRouteConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Bgp.HltApiEmulationBgpControlApi import \
    EmulationBgpControlApi, EmulationBgpControlConstants
#######
# OSPF
#######
# from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfConfigApi import \
#     EmulationOspfConfigApi, EmulationOspfConfigConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.Ospf.HltapiEmulationOspfControlApi import \
    EmulationOspfControlApi, EmulationOspfControlConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.TrafficGenerationApi import TrafficGenerationConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiConnectApi import ConnectApi, ConnectConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.NetworkEmulatingDevice import NetworkEmulatingDevice


class IxNetworkDevice(NetworkEmulatingDevice):
    def __init__(self):
        super(IxNetworkDevice, self).__init__()
        self.initialized_network_device = False
        self.ix_network_ip = None

    def connect_network_generator(self, host, ixnetwork_ip, port=5678):
        if self.connection is None:
            self.connection = self.agents[TrafficGenerationConstants.TELNET]
        if self.connection.is_connected():
            return
        self.ix_network_ip = ixnetwork_ip
        self.connection.connect()
        self.print_and_return(self.tgen_debug, self.connection.wait_until_quiet(1000))
        self.init_network_generator_device()

    def init_network_generator_device(self):
        if self.initialized_network_device:
            pass
        ret_string = self.send_command("package require Ixia")
        if "IxTclHal" in ret_string:
            try:
                output = ret_string.split("IxTclHal")
                self.version = output[-1].split("\r")[0]
            except:
                self.version = "unset"
        ret_string = self.connection.wait_until_quiet(2000)
        ret_string += self.send_command("package require IxTclHal")
        ret_string += self.send_command("package require IxTclNetwork")
        return self.print_and_return(self.tgen_debug, ret_string)
        self.initialized_network_device = True

    def take_network_generator_port_ownership(self, host, user, port_string, reset=False):
        """
        set connect_info [ixia::connect\
            -reset\
            -device 10.52.2.189\
            -port_list 1/1\
            -username ciscoUser
        ]
        """
        port_original = port_string
        port_string = self.convert_port_handle_to_port_string(port_string)
        capi = self.get_api(ConnectConstants.CONNECT_API)
        assert isinstance(capi, ConnectApi)
        options = {ConnectConstants.USERNAME_CMD: user,
                   ConnectConstants.IXNETWORK_TCL_SERVER_CMD: self.ix_network_ip}
        if reset:
            options[ConnectConstants.RESET_CMD] = ""
        temp = capi.connect_helper(host, port_string, options)
        if reset:
            self.set_capture_mode(port_original, "{" + InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                  InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP + "}")

    @staticmethod
    def add_default_values(values, options, overwrite=False):
        for key, value in values.items():
            if overwrite or key not in options:
                options[key] = value

    ###############
    # ## INTERFACE - START
    ###############
    # EXAMPLE:
    # ip_handle1 = add_interface("1/1", "interface1", "192.168.1.2", "192.168.1.1", "255.255.255.0")
    # ip_handle2 = add_interface("1/2", "interface2", "192.168.1.1", "192.168.1.2", "255.255.255.0")
    # clear_ixnetwork_stream("1/1")
    # clear_ixnetwork_stream("1/2")
    # configure_ixnetwork_one_to_one_traffic(self, ip_handle1, ip_handle2, "IPv4_Traffic",
    #   TrafficConfigConstants.CIRCUIT_ENDPOINT_TYPE_IPV4)
    #
    # if options is not set for make sure you set the transmit_mode, and then pkts
    # InterfaceConfigConstants.AUTONEGOTIATION_CMD
    # InterfaceConfigConstants.SPEED_CMD
    # InterfaceConfigConstants.DUPLEX_CMD
    # InterfaceConfigConstants.TRANSMIT_MODE_CMD
    # defaults will be used.
    def add_network_generator_interface(self, port_string, interface_name, interface_ip_address=None, gateway=None,
                                        netmask=None, src_mac_addr=None, options=None):
        port_string = self.convert_port_handle_to_port_string(port_string)
        if options is None:
            options = {}
        api = self.get_api(InterfaceConfigConstants.INTERFACE_CONFIG_API)
        assert isinstance(api, InterfaceConfigApi)
        default_keys = {InterfaceConfigConstants.AUTONEGOTIATION_CMD: 1,
                        InterfaceConfigConstants.SPEED_CMD: InterfaceConfigConstants.SPEED_AUTO,
                        InterfaceConfigConstants.DUPLEX_CMD: InterfaceConfigConstants.DUPLEX_AUTO,
                        InterfaceConfigConstants.TRANSMIT_MODE_CMD: InterfaceConfigConstants.TRANSMIT_MODE_ADVANCED,
                        InterfaceConfigConstants.INTF_MODE_CMD: InterfaceConfigConstants.INTF_MODE_ETHERNET
                        }
        self.add_default_values(default_keys, options)
        default_keys = {InterfaceConfigConstants.PORT_HANDLE_CMD: port_string,
                        InterfaceConfigConstants.INTF_IP_ADDR_CMD: interface_ip_address,
                        InterfaceConfigConstants.GATEWAY_CMD: gateway,
                        InterfaceConfigConstants.NETMASK_CMD: netmask,
                        InterfaceConfigConstants.SRC_MAC_ADDR_CMD: src_mac_addr
                        }
        self.add_default_values(default_keys, options, True)
        ret_value = api.interface_config(options)
        assert isinstance(ret_value, TrafficGeneratingCommandObject)
        # grab the interface handle and return it.
        ret = self.send_command("set " + interface_name +
                                " [keylget hltapiinterfaceconfigapi_interface_config interface_handle]")[:-1].strip()
        if "not found in keyed list" in ret:
            ret = False
        return ret

    def clear_network_generator_all_streams(self, options=None):
        if options is None:
            options = {}
        packet_dict = {}
        packet_dict[TrafficConfigConstants.TRAFFIC_GENERATOR_CMD] = TrafficConfigConstants.TRAFFIC_GENERATOR_IXNETWORK
        packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_RESET
        api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def clear_network_generator_stream(self, port_string, options=None):
        if options is None:
            options = {}
        packet_dict = {}
        packet_dict[TrafficConfigConstants.PORT_HANDLE_CMD] = port_string
        packet_dict[TrafficConfigConstants.TRAFFIC_GENERATOR_CMD] = TrafficConfigConstants.TRAFFIC_GENERATOR_IXNETWORK
        packet_dict[TrafficConfigConstants.MODE_CMD] = TrafficConfigConstants.MODE_RESET
        api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        ret_string = api.traffic_config(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def configure_network_generator_one_to_one_traffic(self, interface_handle1, interface_handle2, name, ip_type,
                                                       options=None):
        if not options:
            options = {}
        # set traffic_status [::ixia::traffic_config                                  \
        #         -mode                   create                                      \
        #         -traffic_generator      ixnetwork                                   \
        #         -transmit_mode          continuous                                  \
        #         -name                   "IPv4_Traffic"                              \
        #         -src_dest_mesh          fully                                       \
        #         -route_mesh             one_to_one                                  \
        #         -circuit_type           none                                        \
        #         -circuit_endpoint_type  ipv4                                        \
        #         -emulation_src_handle   [lindex $interface_handles 0]               \
        #         -emulation_dst_handle   [lindex $interface_handles 1]               \
        #         -track_by               endpoint_pair                               \
        #         -stream_packing         one_stream_per_endpoint_pair                \
        #         -pkts_per_burst         2                                           \
        #         -rate_percent           4.5                                         \
        #         -enforce_min_gap        9                                           \
        #         -tx_delay               10                                          \
        #         -inter_frame_gap        8                                           \
        #         -inter_burst_gap        11                                          \
        #         -inter_stream_gap       12                                          \
        #         -length_mode            increment                                   \
        #         -frame_size_max         512                                         \
        #         ]

        # if options is not set for make sure you set the transmit_mode, and then pkts
        #
        #
        # defaults will be used.
        # interface_handle1 and interface_handle2 are the return values from add_interface(...)
        api = self.get_api(TrafficConfigConstants.TRAFFIC_CONFIG_API)
        assert isinstance(api, TrafficConfigApi)
        default_keys = {
            TrafficConfigConstants.ROUTE_MESH_CMD: TrafficConfigConstants.ROUTE_MESH_ONE_TO_ONE,
            TrafficConfigConstants.SRC_DEST_MESH_CMD: TrafficConfigConstants.SRC_DEST_MESH_FULLY,
            TrafficConfigConstants.ROUTE_MESH_CMD: TrafficConfigConstants.ROUTE_MESH_ONE_TO_ONE,
            TrafficConfigConstants.TRACK_BY_CMD: TrafficConfigConstants.TRACK_BY_ENDPOINT_PAIR,
            TrafficConfigConstants.STREAM_PACKING_CMD:
            TrafficConfigConstants.STREAM_PACKING_ONE_STREAM_PER_ENDPOINT_PAIR
        }
        self.add_default_values(default_keys, options)
        default_keys = {
            TrafficConfigConstants.TRAFFIC_GENERATOR_CMD: TrafficConfigConstants.TRAFFIC_GENERATOR_IXNETWORK,
            TrafficConfigConstants.MODE_CMD: TrafficConfigConstants.MODE_CREATE,
            TrafficConfigConstants.EMULATION_SRC_HANDLE_CMD: interface_handle1,
            TrafficConfigConstants.EMULATION_DST_HANDLE_CMD: interface_handle2,
            TrafficConfigConstants.NAME_CMD: name,
            TrafficConfigConstants.CIRCUIT_ENDPOINT_TYPE_CMD: ip_type
        }
        self.add_default_values(default_keys, options, True)
        api.traffic_config(options)

    ###############
    # ## INTERFACE - END
    ###############

    ####################
    # ## BGP - START
    ###
    # ## Example:
    # ## route_handle = configure_ixnetwork_bgp_peer("1/1", "192.1.1.2", "192.1.1.1", 2,
    #                                            EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 200,
    #                                            EmulationBgpConfigConstants.IP_VERSION_4)
    # configure_ixnetwork_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 1, True,
    #    EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
    ###################
    def configure_network_generator_bgp_peer(self, port_string, handle_name, local_ip_addr, remote_ip_addr, vlan_id,
                                             source_mac, neighbor_type, local_as, ip_version, options=None):
        port_string = self.convert_port_handle_to_port_string(port_string)
        if options is None:
            options = {}
        ################################################################################
        # example call: configure_ixnetwork_bgp_peer("1/1", bgp_peer1,"192.1.1.2", "192.1.1.1", 2,
        #                                            EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 200,
        #                                            EmulationBgpConfigConstants.IP_VERSION_4)
        # TCL EXample:
        # set bgp_config_status [::ixia::emulation_bgp_config     \
        # -port_handle        $port_0                     \
        # -mode               reset                       \
        # -ip_version         4                           \
        # -local_ip_addr      192.1.1.2                   \
        # -remote_ip_addr     192.1.1.1                   \
        # -vlan_id            2                           \
        # -neighbor_type      internal                    \
        # -local_as           200                         \
        # ]
        api = self.get_api(EmulationBgpConfigConstants.EMULATION_BGP_CONFIG_API)
        assert isinstance(api, EmulationBgpConfigApi)

        default_keys = {EmulationBgpConfigConstants.MODE_CMD: EmulationBgpConfigConstants.MODE_RESET,
                        EmulationBgpConfigConstants.IP_VERSION_CMD: ip_version,
                        EmulationBgpConfigConstants.NEIGHBOR_TYPE_CMD: neighbor_type,
                        EmulationBgpConfigConstants.LOCAL_AS_CMD: local_as
                        }
        if vlan_id:
            default_keys[EmulationBgpConfigConstants.VLAN_ID_CMD] = vlan_id
        if ip_version == EmulationBgpConfigConstants.IP_VERSION_6:
            default_keys[EmulationBgpConfigConstants.LOCAL_IPV6_ADDR_CMD] = local_ip_addr
            default_keys[EmulationBgpConfigConstants.REMOTE_IPV6_ADDR_CMD] = remote_ip_addr
        else:
            default_keys[EmulationBgpConfigConstants.LOCAL_IP_ADDR_CMD] = local_ip_addr
            default_keys[EmulationBgpConfigConstants.REMOTE_IP_ADDR_CMD] = remote_ip_addr
        self.add_default_values(default_keys, options)
        default_keys = {EmulationBgpConfigConstants.PORT_HANDLE_CMD: port_string,
                        EmulationBgpConfigConstants.MAC_ADDRESS_START_CMD: source_mac
                        }
        self.add_default_values(default_keys, options, True)
        api.emulation_bgp_config(options)
        # grab the interface handle and return it.
        ret = self.send_command("set " + handle_name +
                                " [keylget hltapiemulationbgpconfigapi_emulation_bgp_config handles]")[:-1].strip()
        if "not found in keyed list" in ret:
            ret = False
        return ret

    def configure_network_generator_bgp_routes_on_bgp_peer(self, bgp_interface_handle, prefix, netmask, num_routes,
                                                           origin_route_enable, origin, ip_version, options=None):
        if options is None:
            options = {}
        # EXAMPLE: configure_ixnetwork_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 1, True,
        #    EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
        #
        # set ce_bgp_neighbor_handle_list [keylget bgp_config_status handles]
        # bgp_config_status is returned from the above code
        ############################################################################
        # Configure BGP routes on BGP peer
        ############################################################################
        # set bgp_route_config_status [::ixia::emulation_bgp_route_config \
        #         -mode                  add                     \
        #         -handle                $bgp_neighbor_handle    \
        #         -prefix                55.0.0.1             \
        #         -netmask               255.255.255.0           \
        #         -num_routes            1          \
        #         -ip_version            4                       \
        #         -origin_route_enable   1                       \
        #         -origin                igp                     \
        #         ]

        api = self.get_api(EmulationBgpRouteConfigConstants.EMULATION_BGP_ROUTE_CONFIG_API)
        assert isinstance(api, EmulationBgpRouteConfigApi)
        default_keys = {EmulationBgpRouteConfigConstants.MODE_CMD: EmulationBgpRouteConfigConstants.MODE_ADD,
                        EmulationBgpRouteConfigConstants.HANDLE_CMD: bgp_interface_handle,
                        EmulationBgpRouteConfigConstants.PREFIX_CMD: prefix,
                        EmulationBgpRouteConfigConstants.NETMASK_CMD: netmask,
                        EmulationBgpRouteConfigConstants.NUM_ROUTES_CMD: num_routes,
                        EmulationBgpRouteConfigConstants.IP_VERSION_CMD: ip_version,
                        EmulationBgpRouteConfigConstants.ORIGIN_ROUTE_ENABLE_CMD: origin_route_enable,
                        EmulationBgpRouteConfigConstants.ORIGIN_CMD: origin
                        }
        self.add_default_values(default_keys, options)
        api.emulation_bgp_route_config(options)

        # this is to have more than one peer added at one time.
        ################################################################################
        # set bgp_config_status [::ixia::emulation_bgp_config     \
        # -port_handle        $port_0                     \
        # -mode               reset                       \
        # -ip_version         4                           \
        # -local_ip_addr      192.1.1.2                   \
        # -remote_ip_addr     192.1.1.1                   \
        # -local_addr_step    0.0.1.0                     \
        # -remote_addr_step   0.0.1.0                     \
        # -vlan_id            2                           \
        # -vlan_id_step       1                           \
        # -count              $num_of_bgp_neighbors       \
        # -neighbor_type      internal                    \
        # -local_as           200                         \
        # -local_as_step      1                           \
        # -local_as_mode      increment                   \
        # ]
        # set ce_bgp_neighbor_handle_list [keylget bgp_config_status handles]
        #
        # foreach bgp_neighbor_handle $ce_bgp_neighbor_handle_list
        ############################################################################
        # Configure BGP routes on each BGP peer
        ############################################################################
        # set bgp_route_config_status [::ixia::emulation_bgp_route_config \
        #         -mode                  add                     \
        #         -handle                $bgp_neighbor_handle    \
        #         -prefix                $prefix_ce1             \
        #         -prefix_step           1                       \
        #         -netmask               255.255.255.0           \
        #         -num_routes            $num_of_prefix          \
        #         -ip_version            4                       \
        #         -origin_route_enable   1                       \
        #         -origin                igp                     \
        #         ]

    def start_network_generator_bgp_emulation(self, port_string, options=None):
        port_string = self.convert_port_handle_to_port_string(port_string)
        if options is None:
            options = {}
        api = self.get_api(EmulationBgpControlConstants.EMULATION_BGP_CONTROL_API)
        assert isinstance(api, EmulationBgpControlApi)
        packet_dict = {}
        packet_dict[EmulationBgpControlConstants.MODE_CMD] = EmulationBgpControlConstants.MODE_START
        packet_dict[EmulationBgpControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_bgp_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def stop_network_generator_bgp_emulation(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.get_api(EmulationBgpControlConstants.EMULATION_BGP_CONTROL_API)
        assert isinstance(api, EmulationBgpControlApi)
        packet_dict = {}
        packet_dict[EmulationBgpControlConstants.MODE_CMD] = EmulationBgpControlConstants.MODE_STOP
        packet_dict[EmulationBgpControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_bgp_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def restart_network_generator_bgp_emulation(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.get_api(EmulationBgpControlConstants.EMULATION_BGP_CONTROL_API)
        assert isinstance(api, EmulationBgpControlApi)
        packet_dict = {}
        packet_dict[EmulationBgpControlConstants.MODE_CMD] = EmulationBgpControlConstants.MODE_RESTART
        packet_dict[EmulationBgpControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_bgp_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    ####################
    # ## BGP - END
    ####################

    ####################
    # ## OSPF - START
    ###
    # ## Example:
    # ## route_handle = configure_ixnetwork_bgp_peer("1/1", "192.1.1.2", "192.1.1.1", 2,
    #                                            EmulationBgpConfigConstants.NEIGHBOR_TYPE_INTERNAL, 200,
    #                                            EmulationBgpConfigConstants.IP_VERSION_4)
    # configure_ixnetwork_bgp_routes_on_bgp_peer(route_handle, "55.0.0.1", "255.255.255.0", 1, True,
    #    EmulationBgpRouteConfigConstants.ORIGIN_IGP, EmulationBgpRouteConfigConstants.IP_VERSION_4)
    ###################

# TODO: The below function is broken.

#     def configure_network_generator_ospf_neighbor(self, port_string, handle_name, reset=True,
#                                                   session_type=EmulationOspfConfigConstants.SESSION_TYPE_OSPFV2,
#                                                   mode=EmulationOspfConfigConstants.MODE_CREATE,
#                                                   mac_address_init="1000.0000.0001",
#                                                   intf_ip_addr="100.1.1.1",
#                                                   router_id="1.1.1.1",
#                                                   neighbor_intf_ip_addr="100.1.1.2",
#                                                   area_id="0.0.0.1",
#                                                   area_type=EmulationOspfConfigConstants.AREA_TYPE_EXTERNALCAPABLE,
#                                                   authentication_mode="null",
#                                                   dead_interval=222,
#                                                   hello_interval=333,
#                                                   interface_cost=55,
#                                                   lsa_discard_mode=1,
#                                                   mtu=670,
#                                                   network_type=EmulationOspfConfigConstants.NETWORK_TYPE_PTOP,
#                                                   demand_circuit=1, options=None):
#         port_string = self.convert_port_handle_to_port_string(port_string)
#         if options is None:
#             options = {}
#         #################################################
#         #                                               #
#         #  Configure n OSPFv2 neighbors                 #
#         #                                               #
#         #################################################
#         # set ospf_neighbor_status [::ixia::emulation_ospf_config \
#         #         -port_handle                $port_tx         \
#         #         -reset                                       \
#         #         -session_type               ospfv2           \
#         #         -mode                       create           \
#         #         -count                      1               \
#         #         -mac_address_init           1000.0000.0001   \
#         #         -intf_ip_addr               100.1.1.1        \
#         #         -router_id                  1.1.1.1          \
#         #         -neighbor_intf_ip_addr      100.1.1.2        \
#         #         -area_id                    0.0.0.1          \
#         #         -area_type                  external-capable \
#         #         -authentication_mode        null             \
#         #         -dead_interval              222              \
#         #         -hello_interval             333              \
#         #         -interface_cost             55               \
#         #         -lsa_discard_mode           1                \
#         #         -mtu                        670              \
#         #         -network_type               ptop             \
#         #         -demand_circuit             1]
#         #
#         # if {[keylget ospf_neighbor_status status] != $::SUCCESS} {
#         #     return "FAIL - $test_name - [keylget ospf_neighbor_status log]"
#         # }
#         #
#         # set session_handle [keylget ospf_neighbor_status handle]
#         api = self.get_api(EmulationOspfConfigConstants.EMULATION_BGP_CONFIG_API)
#         assert isinstance(api, EmulationOspfConfigApi)
#
#         default_keys = {EmulationOspfConfigConstants.MODE_CMD: EmulationBgpConfigConstants.MODE_RESET,
#                         EmulationOspfConfigConstants.IP_VERSION_CMD: ip_version,
#                         EmulationOspfConfigConstants.NEIGHBOR_TYPE_CMD: neighbor_type,
#                         EmulationOspfConfigConstants.LOCAL_AS_CMD: local_as
#                         }
#         if vlan_id:
#             default_keys[EmulationOspfConfigConstants.VLAN_ID_CMD] = vlan_id
#         if ip_version == EmulationOspfConfigConstants.IP_VERSION_6:
#             default_keys[EmulationOspfConfigConstants.LOCAL_IPV6_ADDR_CMD] = local_ip_addr
#             default_keys[EmulationOspfConfigConstants.REMOTE_IPV6_ADDR_CMD] = remote_ip_addr
#         else:
#             default_keys[EmulationOspfConfigConstants.LOCAL_IP_ADDR_CMD] = local_ip_addr
#             default_keys[EmulationOspfConfigConstants.REMOTE_IP_ADDR_CMD] = remote_ip_addr
#         self.add_default_values(default_keys, options)
#         default_keys = {EmulationOspfConfigConstants.PORT_HANDLE_CMD: port_string,
#                         EmulationOspfConfigConstants.MAC_ADDRESS_START_CMD: source_mac
#                         }
#         self.add_default_values(default_keys, options, True)
#         api.emulation_bgp_config(options)
#         # grab the interface handle and return it.
#         ret = self.send_command("set " + handle_name +
#                                 " [keylget hltapiemulationbgpconfigapi_emulation_bgp_config handles]")[:-1].strip()
#         if "not found in keyed list" in ret:
#             ret = False
#         return ret

    ######################################################
    #                                                    #
    #  Configure a single router behind a session router #
    #                                                    #
    ######################################################
    # set route_config_status [::ixia::emulation_ospf_topology_route_config\
    #         -mode           create                  \
    #         -handle         $session_handle         \
    #         -type           router                  \
    #         -router_id      123.1.1.1               \
    #         -router_abr     1                       \
    #         -router_asbr    1                       \
    #         -router_te      1                       \
    #         -interface_ip_address   22.0.0.1        \
    #         -interface_ip_mask      255.255.0.0     \
    #         ]

    def start_network_generator_ospf_emulation(self, port_string, options=None):
        port_string = self.convert_port_handle_to_port_string(port_string)
        if options is None:
            options = {}
        api = self.get_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API)
        assert isinstance(api, EmulationOspfControlApi)
        packet_dict = {}
        packet_dict[EmulationOspfControlConstants.MODE_CMD] = EmulationOspfControlConstants.MODE_START
        packet_dict[EmulationOspfControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_ospf_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def stop_network_generator_ospf_emulation(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.get_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API)
        assert isinstance(api, EmulationOspfControlApi)
        packet_dict = {}
        packet_dict[EmulationOspfControlConstants.MODE_CMD] = EmulationOspfControlConstants.MODE_STOP
        packet_dict[EmulationOspfControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_ospf_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    def restart_network_generator_ospf_emulation(self, port_string, options=None):
        if options is None:
            options = {}
        port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.get_api(EmulationOspfControlConstants.EMULATION_OSPF_CONTROL_API)
        assert isinstance(api, EmulationOspfControlApi)
        packet_dict = {}
        packet_dict[EmulationOspfControlConstants.MODE_CMD] = EmulationOspfControlConstants.MODE_RESTART
        packet_dict[EmulationOspfControlConstants.PORT_HANDLE_CMD] = port_string
        ret_string = api.emulation_ospf_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))

    ####################
    # ## OSPF - END
    ####################

    def start_network_generator_traffic(self, options=None):
        if options is None:
            options = {}
        api = self.get_api(TrafficControlConstants.TRAFFIC_CONTROL_API)
        assert isinstance(api, TrafficControlApi)
        packet_dict = {}
        packet_dict[TrafficControlConstants.ACTION_CMD] = TrafficControlConstants.ACTION_RUN
        # packet_dict[TrafficControlConstants.TRAFFIC_GENERATOR_CMD] = \
        #     TrafficControlConstants.TRAFFIC_GENERATOR_IXNETWORK
        ret_string = api.traffic_control(TrafficGenerationUtils.merge_arrays(packet_dict, options))
