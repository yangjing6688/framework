from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationVrrpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationVrrpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, priority=200, advertise_interval_msecs=1000, version=2, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [source_ip] -
        [netmask] -
        [gateway_address] -
        [mac_address] -
        [vlan_id] -  (default: None)
        [priority] -  (default: 200)
        [advertise_interval_msecs] -  (default: 1000)
        [version] -  (default: 2)

        create_vrrp_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.create_vrrp_interface(self.current_port, router_id, source_ip, netmask,
                                                 gateway_address, mac_address, vlan_id, priority,
                                                 advertise_interval_msecs, version)
        self._keyword_cleanup()

    def remove_vrrp_router(self, port_string, router_id, route_address, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [route_address] -

        remove_vrrp_router
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.remove_vrrp_router(self.current_port, router_id, route_address)
        self._keyword_cleanup()

    def add_vrf(self, port_string, router_id, vrf_id, backup_address, priority=150, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vrf_id] -
        [backup_address] -
        [priority] -  (default: 150)

        add_vrf
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.add_vrf(self.current_port, router_id, vrf_id, backup_address, priority)
        self._keyword_cleanup()

    def enable_vrf(self, port_string, router_id, vrf_id, enabled=True, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vrf_id] -
        [enabled] -  (default: True)

        enable_vrf
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.enable_vrf(self.current_port, router_id, vrf_id, enabled)
        self._keyword_cleanup()

    def remove_vrf(self, port_string, router_id, vrf_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vrf_id] -

        remove_vrf
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.remove_vrf(self.current_port, router_id, vrf_id)
        self._keyword_cleanup()

    def rip_config(self, port_string, tx_delay, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [tx_delay] -

        rip_config
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

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
        self._init_keyword(emulation_api_const=self.emulation_constants.VRRP_API, **kwargs)

        self.emulation_api.get_rip_stats(self.current_port, router_id)
        self._keyword_cleanup()
