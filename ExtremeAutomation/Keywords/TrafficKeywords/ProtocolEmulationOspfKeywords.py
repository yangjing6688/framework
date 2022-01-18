from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationOspfKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationOspfKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_ospf_interface(self, port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, link_type="standard", area_type="extcapable", passive=False, prio="1",
                              cost="1", trans_delay="40", hello_int="10", dead_int="40", retrans_int="5",
                              wait_time="40", **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [area_id] -
        [source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -  (default: None)
        [link_type] -  (default: "standard")
        [area_type] -  (default: "extcapable")
        [passive] -  (default: False)
        [prio] -  (default: "1")
        [cost] -  (default: "1")
        [trans_delay] -  (default: "40")
        [hello_int] -  (default: "10")
        [dead_int] -  (default: "40")
        [retrans_int] -  (default: "5")
        [wait_time] -  (default: "40")

        create_ospf_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.create_ospf_interface(self.current_port, router_id, area_id, source_ip, netmask,
                                                 gateway_address, mac_address, vlan_id, link_type, area_type, passive,
                                                 prio, cost, trans_delay, hello_int, dead_int, retrans_int, wait_time)
        self._keyword_cleanup()

    def add_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step, age, ls_type="AS_EXTERNAL",
                       adv_rtr="0.0.0.0", forward_address="0.0.0.0", cost=1, costype="type1_external", ex_route_tag=1,
                       **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -
        [num_routes] -
        [step] -
        [age] -
        [ls_type] -  (default: "AS_EXTERNAL")
        [adv_rtr] -  (default: "0.0.0.0")
        [forward_address] -  (default: "0.0.0.0")
        [cost] -  (default: 1)
        [costype] -  (default: "type1_external")
        [ex_route_tag] -  (default: 1)

        add_ospf_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.add_ospf_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                          step, age, ls_type, adv_rtr, forward_address, cost, costype, ex_route_tag)
        self._keyword_cleanup()

    def delete_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -
        [num_routes] -
        [step] -  (default:  1)

        delete_ospf_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.delete_ospf_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                             step)
        self._keyword_cleanup()

    def remove_ospf_router(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        remove_ospf_router
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.remove_ospf_router(self.current_port, router_id)
        self._keyword_cleanup()

    def set_ospf_router_enabled(self, port_string, router_id, enable=True, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [enable] -  (default: True)

        set_ospf_router_enabled
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.set_ospf_router_enabled(self.current_port, router_id, enable)
        self._keyword_cleanup()

    def get_ospf_state(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_ospf_state
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.get_ospf_state(self.current_port, router_id, )
        self._keyword_cleanup()

    def add_ospf_lsas(self, port_string, router_id, lsa, receive_router, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [lsa] -
        [receive_router] -

        add_ospf_lsas
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.add_ospf_lsas(self.current_port, router_id, lsa, receive_router)
        self._keyword_cleanup()

    def get_ospf_stats(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_ospf_stats
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.get_ospf_stats(self.current_port, router_id, )
        self._keyword_cleanup()

    def add_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id,
                    attached_router_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [ip_address] -
        [designated_router_address] -
        [netmask] -
        [attached_router_id] -
        [attached_router_ip] -

        add_network
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.add_network(self.current_port, router_id, ip_address, designated_router_address,
                                       netmask, attached_router_id, attached_router_ip)
        self._keyword_cleanup()

    def remove_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id,
                       attached_router_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [ip_address] -
        [designated_router_address] -
        [netmask] -
        [attached_router_id] -
        [attached_router_ip] -

        remove_network
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.remove_network(self.current_port, router_id, ip_address,
                                          designated_router_address, netmask, attached_router_id, attached_router_ip, )
        self._keyword_cleanup()

    def add_stub_network(self, port_string, router_id, ip_address, netmask, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [ip_address] -
        [netmask] -

        add_stub_network
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.add_stub_network(self.current_port, router_id, ip_address, netmask)
        self._keyword_cleanup()

    def remove_stub_network(self, port_string, router_id, ip_address, netmask, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [ip_address] -
        [netmask] -

        remove_stub_network
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.remove_stub_network(self.current_port, router_id, ip_address, netmask)
        self._keyword_cleanup()

    def generate_ospf_routes(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        generate_ospf_routes
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.OSPF_API, **kwargs)

        self.emulation_api.generate_ospf_routes(self.current_port, router_id)
        self._keyword_cleanup()
