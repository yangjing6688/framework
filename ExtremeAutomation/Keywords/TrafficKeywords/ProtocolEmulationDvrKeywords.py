from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationDvrKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationDvrKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def get_all_dvr_enties(self, tgen, bridge_name, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -

        get_all_dvr_enties
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.get_all_dvr_enties(self.current_port, bridge_name)
        self._keyword_cleanup()

    def add_dvr_gateway(self, tgen, bridge_name, l3_isid, l2_isid, cmac, mask_length, gateway, vlan_ip_interface,
                        **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [cmac] -
        [mask_length] -
        [gateway] -
        [vlan_ip_interface] -

        add_dvr_gateway
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.add_dvr_gateway(self.current_port, bridge_name, l3_isid, l2_isid, cmac, mask_length, gateway,
                                           vlan_ip_interface)
        self._keyword_cleanup()

    def delete_dvr_gateway(self, tgen, bridge_name, l3_isid, l2_isid, gateway, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [gateway] -

        delete_dvr_gateway
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.delete_dvr_gateway(self.current_port, bridge_name, l3_isid, l2_isid, gateway)
        self._keyword_cleanup()

    def verify_dvr_gateway(self, tgen, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, gateway, options=None,
                           **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [cmac] -
        [bmac] -
        [mask_length] -
        [gateway] -
        [options] -  (default: None)

        verify_dvr_gateway
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.verify_dvr_gateway(self.current_port, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length,
                                              gateway, options)
        self._keyword_cleanup()

    def add_dvr_route(self, tgen, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address, next_hop,
                      domain_id, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [cmac] -
        [mask_length] -
        [network_address] -
        [next_hop] -
        [domain_id] -

        add_dvr_route
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.add_dvr_route(self.current_port, bridge_name, l3_isid, l2_isid, cmac, mask_length,
                                         network_address, next_hop, domain_id)
        self._keyword_cleanup()

    def delete_dvr_route(self, tgen, bridge_name, l3_isid, l2_isid, cmac, mask_length, network_address, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [cmac] -
        [mask_length] -
        [network_address] -

        delete_dvr_route
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.delete_dvr_route(self.current_port, bridge_name, l3_isid, l2_isid, cmac, mask_length,
                                            network_address)
        self._keyword_cleanup()

    def verify_dvr_route(self, tgen, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length, network_address, domain_id,
                         ctrl=1, cost=1, options=None, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [cmac] -
        [bmac] -
        [mask_length] -
        [network_address] -
        [domain_id] -
        [ctrl] -  (default: 1)
        [cost] -  (default: 1)
        [options] -  (default: None)

        verify_dvr_route
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        options = options if options is not None else {}
        self.emulation_api.verify_dvr_route(self.current_port, bridge_name, l3_isid, l2_isid, cmac, bmac, mask_length,
                                            network_address, domain_id, ctrl, cost, options)
        self._keyword_cleanup()

    def add_dvr_multicast(self, tgen, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [multicast_config] -
        [igmp_version] -

        add_dvr_multicast
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.add_dvr_multicast(self.current_port, bridge_name, l3_isid, l2_isid, multicast_config,
                                             igmp_version)
        self._keyword_cleanup()

    def delete_dvr_multicast(self, tgen, bridge_name, l3_isid, l2_isid, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -

        delete_dvr_multicast
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.delete_dvr_multicast(self.current_port, bridge_name, l3_isid, l2_isid)
        self._keyword_cleanup()

    def verify_dvr_multicast(self, tgen, bridge_name, l3_isid, l2_isid, multicast_config, igmp_version=2,
                             igmp_query_interval=0, igmp_query_max_response=0, igmp_robust_value=0,
                             igmp_member_query_interval=0, igmp_ext_compatibility_mode_enable=16777215, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_isid] -
        [l2_isid] -
        [multicast_config] -
        [igmp_version] -  (default: 2)
        [igmp_query_interval] -  (default: 0)
        [igmp_query_max_response] -  (default: 0)
        [igmp_robust_value] -  (default: 0)
        [igmp_member_query_interval] -  (default: 0)
        [igmp_ext_compatibility_mode_enable] -  (default: 16777215)

        verify_dvr_multicast
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.verify_dvr_multicast(self.current_port, bridge_name, l3_isid, l2_isid, multicast_config,
                                                igmp_version, igmp_query_interval, igmp_query_max_response,
                                                igmp_robust_value, igmp_member_query_interval,
                                                igmp_ext_compatibility_mode_enable)
        self._keyword_cleanup()

    def create_dvr_gw_endpoint(self, tgen, bridge_name, l3_sid, starting_ip, mac_address, gateway, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [l3_sid] -
        [starting_ip] -
        [mac_address] -
        [gateway] -

        create_dvr_gw_endpoint
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.create_dvr_gw_endpoint(self.current_port, bridge_name, l3_sid, starting_ip, mac_address,
                                                  gateway)
        self._keyword_cleanup()

    def verify_dvr_member(self, tgen, bridge_name, bmac, domain_id, role, domain_isid, code, **kwargs):
        """
        Keyword Arguments:
        [bridge_name] -
        [bmac] -
        [domain_id] -
        [role] -
        [domain_isid] -
        [code] -

        verify_dvr_member
        """
        self._get_traffic_generator_info(tgen)
        self._init_keyword(emulation_api_const=self.emulation_constants.DVR_API, **kwargs)

        self.emulation_api.verify_dvr_member(self.current_port, bridge_name, bmac, domain_id, role, domain_isid, code)
        self._keyword_cleanup()
