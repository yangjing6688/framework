from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationBgpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationBgpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_bgp_interface(self, port_string, router_id, local_as, source_ip, netmask, gateway_address, mac_address,
                             vlan_id=None, neighbor_type=None, ip_version="IPv4", options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [local_as] -
        [source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -  (default: None)
        [neighbor_type] -  (default: None)
        [ip_version] -  (default: "IPv4")
        [options] -  (default: None)

        create_bgp_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.create_bgp_interface(self.current_port, router_id, local_as, source_ip,
                                                netmask, gateway_address, mac_address, vlan_id, neighbor_type,
                                                ip_version, options)
        self._keyword_cleanup()

    def configure_bgp_options(self, port_string, updateinterval=1000, maxattributes=1000, notifylogsize=256, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [updateinterval] -  (default: 1000)
        [maxattributes] -  (default: 1000)
        [notifylogsize] -  (default: 256)

        configure_bgp_options
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.configure_bgp_options(self.current_port, updateinterval, maxattributes,
                                                 notifylogsize)
        self._keyword_cleanup()

    def add_bgp_neighbor(self, port_string, router_id, ip_address, netmask, local_as, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [ip_address] -
        [netmask] -
        [local_as] -

        add_bgp_neighbor
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.add_bgp_neighbor(self.current_port, router_id, ip_address, netmask, local_as)
        self._keyword_cleanup()

    def start_network_generator_bgp_emulation(self, port_string, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [options] -  (default: None)

        start_network_generator_bgp_emulation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.start_network_generator_bgp_emulation(self.current_port, options)
        self._keyword_cleanup()

    def stop_network_generator_bgp_emulation(self, port_string, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [options] -  (default: None)

        stop_network_generator_bgp_emulation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.stop_network_generator_bgp_emulation(self.current_port, options)
        self._keyword_cleanup()

    def restart_network_generator_bgp_emulation(self, port_string, options=None, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [options] -  (default: None)

        restart_network_generator_bgp_emulation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.restart_network_generator_bgp_emulation(self.current_port, options)
        self._keyword_cleanup()

    def add_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, origin="IGP", med=0,
                      localpref=0, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -
        [num_routes] -
        [step] -  (default: 1)
        [origin] -  (default: "IGP")
        [med] -  (default: 0)
        [localpref] -  (default: 0)

        add_bgp_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.add_bgp_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                         step, origin, med, localpref)
        self._keyword_cleanup()

    def delete_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -
        [num_routes] -
        [step] -  (default: 1)

        delete_bgp_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.delete_bgp_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                            step)
        self._keyword_cleanup()

    def remove_bgp_router(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        remove_bgp_router
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.remove_bgp_router(self.current_port, router_id)
        self._keyword_cleanup()

    def set_bgp_router_enabled(self, port_string, router_id, enable=True, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [enable] -  (default: True)

        set_bgp_router_enabled
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.set_bgp_router_enabled(self.current_port, router_id, enable)
        self._keyword_cleanup()

    def delete_bpg_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -
        [num_routes] -
        [step] -  (default: 1)

        delete_bpg_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.delete_bpg_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                            step)
        self._keyword_cleanup()

    def get_bgp_state(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_bgp_state
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.get_bgp_state(self.current_port, router_id)
        self._keyword_cleanup()

    def get_bgp_stats(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_bgp_stats
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.BGP_API, **kwargs)

        self.emulation_api.get_bgp_stats(self.current_port, router_id)
        self._keyword_cleanup()
