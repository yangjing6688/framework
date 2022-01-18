from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationRipNgKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationRipNgKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_ripng_interface(self, port_string, router_id_and_source_ip, prefix_length, mac_address, vlan_id=None,
                               mode="R1", refresh_time=30, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id_and_source_ip] -
        [prefix_length] -
        [mac_address] -
        [vlan_id] -  (default: None)
        [mode] -  (default: "R1")
        [refresh_time] -  (default: 30)

        create_ripng_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.create_ripng_interface(self.current_port, router_id_and_source_ip,
                                                  prefix_length, mac_address, vlan_id, mode, refresh_time)
        self._keyword_cleanup()

    def add_ripng_route(self, port_string, router_id, first_ip, next_hop=None, prefix_length=64, metric=1, num_routes=1,
                        step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [next_hop] -  (default: None)
        [prefix_length] -  (default: 64)
        [metric] -  (default: 1)
        [num_routes] -  (default: 1)
        [step] -  (default: 1)

        add_ripng_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.add_ripng_route(self.current_port, router_id, first_ip, next_hop, prefix_length,
                                           metric, num_routes, step)
        self._keyword_cleanup()

    def delete_ripng_route(self, port_string, router_id, first_ip, next_hop="0:0:0:0:0:0:0:0", prefix_length=64,
                           num_routes=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [first_ip] -
        [next_hop] -  (default: "0:0:0:0:0:0:0:0")
        [prefix_length] -  (default: 64)
        [num_routes] -  (default: 1)
        [step] -  (default: 1)

        delete_ripng_route
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.delete_ripng_route(self.current_port, router_id, first_ip, next_hop,
                                              prefix_length, num_routes, step)
        self._keyword_cleanup()

    def remove_ripng_router(self, port_string, router_id_and_source_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id_and_source_ip] -

        remove_ripng_router
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.remove_ripng_router(self.current_port, router_id_and_source_ip)
        self._keyword_cleanup()

    def ripng_config(self, port_string, tx_delay, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [tx_delay] -

        ripng_config
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.ripng_config(self.current_port, tx_delay)
        self._keyword_cleanup()

    def get_ripng_stats(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        get_ripng_stats
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.RIPNG_API, **kwargs)

        self.emulation_api.get_ripng_stats(self.current_port, router_id)
        self._keyword_cleanup()
