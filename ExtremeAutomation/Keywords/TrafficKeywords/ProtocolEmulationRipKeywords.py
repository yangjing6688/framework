from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationRipKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationRipKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_rip_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address, vlan_id,
                             mode="R1", refresh_time=30, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id_and_source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -
        [mode] -  (default: "R1")
        [refresh_time] -  (default: 30)

        create_rip_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.create_rip_interface(self.current_port, router_id_and_source_ip, netmask,
                                                gateway_address, mac_address, vlan_id, mode, refresh_time)
        self._keyword_cleanup()

    def add_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", next_hop="0.0.0.0", metric=1,
                      num_routes=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -  (default: "0.0.0.0")
        [next_hop] -  (default: "0.0.0.0")
        [metric] -  (default: 1)
        [num_routes] -  (default: 1)
        [step] -  (default: 1)

        add_rip_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.add_rip_route(self.current_port, router_id, first_ip, netmask, next_hop, metric,
                                         num_routes, step)
        self._keyword_cleanup()

    def delete_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", num_routes=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [netmask] -  (default: "0.0.0.0")
        [num_routes] -  (default: 1)
        [step] -  (default: 1)

        delete_rip_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.delete_rip_route(self.current_port, router_id, first_ip, netmask, num_routes,
                                            step)
        self._keyword_cleanup()

    def remove_rip_router(self, port_string, router_id_and_source_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id_and_source_ip] -

        remove_rip_router
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.remove_rip_router(self.current_port, router_id_and_source_ip)
        self._keyword_cleanup()

    def rip_config(self, port_string, tx_delay, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [tx_delay] -

        rip_config
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.rip_config(self.current_port, tx_delay)
        self._keyword_cleanup()

    def get_rip_stats(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_rip_stats
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIP_API, **kwargs)

        self.emulation_api.get_rip_stats(self.current_port, router_id)
        self._keyword_cleanup()
