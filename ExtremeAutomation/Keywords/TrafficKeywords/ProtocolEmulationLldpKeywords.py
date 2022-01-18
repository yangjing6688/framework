from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass


class ProtocolEmulationLldpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationLldpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_lldp_interface(self, port_string, router_id, mac_address, chassis_mac, ttl, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [mac_address] -
        [chassis_mac] -
        [ttl] -

        create_lldp_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.create_lldp_interface(self.current_port, router_id, mac_address, chassis_mac,
                                                 ttl)
        self._keyword_cleanup()

    def remove_lldp_interface(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        remove_lldp_interface
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_interface(self.current_port, router_id)
        self._keyword_cleanup()

    def enable_lldp(self, port_string, router_id, enabled=True, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [enabled] -  (default: True)

        enable_lldp
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.enable_lldp(self.current_port, router_id, enabled)
        self._keyword_cleanup()

    def start_transmit_tlv(self, port_string, router_id, tlv_name, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [tlv_name] -

        start_transmit_tlv
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_transmit_tlv(self.current_port, router_id, tlv_name)
        self._keyword_cleanup()

    def stop_transmit_tlv(self, port_string, router_id, tlv_name, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [tlv_name] -

        stop_transmit_tlv
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_transmit_tlv(self.current_port, router_id, tlv_name)
        self._keyword_cleanup()

    def add_lldp_tlv_sys_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_sys_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_sys_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_sys_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_sys_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_sys_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_sys_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_sys_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_sys_name(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_sys_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_sys_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_sys_name(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_sys_desc(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_sys_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_sys_desc(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_sys_desc(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_sys_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_sys_desc(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_sys_desc(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_sys_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_sys_desc(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_sys_desc(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_sys_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_sys_desc(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_sys_cap(self, port_string, router_id, cap_support, cap_enabled, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [cap_support] -
        [cap_enabled] -

        add_lldp_tlv_sys_cap
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_sys_cap(self.current_port, router_id, cap_support, cap_enabled)
        self._keyword_cleanup()

    def remove_lldp_tlv_sys_cap(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_sys_cap
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_sys_cap(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_sys_cap(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_sys_cap
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_sys_cap(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_sys_cap(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_sys_cap
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_sys_cap(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_port_desc(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_port_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_port_desc(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_port_desc(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_port_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_port_desc(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_port_desc(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_port_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_port_desc(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_port_desc(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_port_desc
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_port_desc(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port,
                                     local_management_oid, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [local_management_address] -
        [local_management_port] -
        [local_management_oid] -

        add_lldp_tlv_local_mgmt_addr
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_local_mgmt_addr(self.current_port, router_id,
                                                        local_management_address, local_management_port,
                                                        local_management_oid)
        self._keyword_cleanup()

    def remove_lldp_tlv_local_mgmt_addr(self, port_string, router_id, local_management_address, local_management_port,
                                        **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [local_management_address] -
        [local_management_port] -

        remove_lldp_tlv_local_mgmt_addr
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_local_mgmt_addr(self.current_port, router_id,
                                                           local_management_address, local_management_port)
        self._keyword_cleanup()

    def start_tlv_local_mgmt_addr(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_local_mgmt_addr
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_local_mgmt_addr(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_local_mgmt_addr(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_local_mgmt_addr
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_local_mgmt_addr(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_dot1_port_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot1_port_vlan_id(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot1_port_vlan_id(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot1_port_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot1_port_vlan_id(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot1_port_vlan_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot1_port_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot1_port_vlan_id(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot1_port_vlan_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot1_port_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot1_port_vlan_id(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_dot1_protocol_identity
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot1_protocol_identity(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot1_protocol_identity(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot1_protocol_identity
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot1_protocol_identity(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot1_protocol_identity(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot1_protocol_identity
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot1_protocol_identity(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot1_protocol_identity(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot1_protocol_identity
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot1_protocol_identity(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id, supported, enabled, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vlan_id] -
        [supported] -
        [enabled] -

        add_lldp_tlv_dot1_port_protocol_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot1_port_protocol_vlan_id(self.current_port, router_id, vlan_id,
                                                                   supported, enabled)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, vlan_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vlan_id] -

        remove_lldp_tlv_dot1_port_protocol_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot1_port_protocol_vlan_id(self.current_port, router_id,
                                                                      vlan_id)
        self._keyword_cleanup()

    def start_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot1_port_protocol_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot1_port_protocol_vlan_id(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot1_port_protocol_vlan_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot1_port_protocol_vlan_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot1_port_protocol_vlan_id(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot1_vlan_name(self, port_string, router_id, vlan_id, vlan_name, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vlan_id] -
        [vlan_name] -

        add_lldp_tlv_dot1_vlan_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot1_vlan_name(self.current_port, router_id, vlan_id, vlan_name)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot1_vlan_name(self, port_string, router_id, vlan_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [vlan_id] -

        remove_lldp_tlv_dot1_vlan_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot1_vlan_name(self.current_port, router_id, vlan_id)
        self._keyword_cleanup()

    def start_tlv_dot1_vlan_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot1_vlan_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot1_vlan_name(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot1_vlan_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot1_vlan_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot1_vlan_name(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, auto_neg_supported, auto_neg_enabled,
                                                auto_neg_ad_cap, op_mau_type, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [auto_neg_supported] -
        [auto_neg_enabled] -
        [auto_neg_ad_cap] -
        [op_mau_type] -

        add_lldp_tlv_dot3_mac_phy_config_status
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot3_mac_phy_config_status(self.current_port, router_id,
                                                                   auto_neg_supported, auto_neg_enabled,
                                                                   auto_neg_ad_cap, op_mau_type)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot3_mac_phy_config_status(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot3_mac_phy_config_status
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot3_mac_phy_config_status(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot3_mac_phy_config_status(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot3_mac_phy_config_status
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot3_mac_phy_config_status(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot3_mac_phy_config_status(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot3_mac_phy_config_status
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot3_mac_phy_config_status(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot3_power_mdi(self, port_string, router_id, mdi_power_support, pse_power_pair, power_class,
                                    **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [mdi_power_support] -
        [pse_power_pair] -
        [power_class] -

        add_lldp_tlv_dot3_power_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot3_power_mdi(self.current_port, router_id, mdi_power_support,
                                                       pse_power_pair, power_class)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot3_power_mdi(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot3_power_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot3_power_mdi(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot3_power_mdi(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot3_power_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot3_power_mdi(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot3_power_mdi(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot3_power_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot3_power_mdi(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, aggregation_supported, aggregation_enabled,
                                           aggregation_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [aggregation_supported] -
        [aggregation_enabled] -
        [aggregation_id] -

        add_lldp_tlv_dot3_link_aggregation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot3_link_aggregation(self.current_port, router_id,
                                                              aggregation_supported, aggregation_enabled,
                                                              aggregation_id)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot3_link_aggregation(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot3_link_aggregation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot3_link_aggregation(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot3_link_aggregation(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot3_link_aggregation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot3_link_aggregation(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot3_link_aggregation(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot3_link_aggregation
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot3_link_aggregation(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_dot3_maximum_frame_size
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_dot3_maximum_frame_size(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_dot3_maximum_frame_size(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_dot3_maximum_frame_size
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_dot3_maximum_frame_size(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_dot3_maximum_frame_size(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_dot3_maximum_frame_size
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_dot3_maximum_frame_size(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_dot3_maximum_frame_size(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_dot3_maximum_frame_size
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_dot3_maximum_frame_size(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_fa_elem(self, port_string, router_id, element_type, state, sys_id, conn_type, port_mlt_id,
                             mgmt_vlan, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [element_type] -
        [state] -
        [sys_id] -
        [conn_type] -
        [port_mlt_id] -
        [mgmt_vlan] -

        add_lldp_tlv_fa_elem
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_fa_elem(self.current_port, router_id, element_type, state, sys_id,
                                                conn_type, port_mlt_id, mgmt_vlan)
        self._keyword_cleanup()

    def remove_lldp_tlv_fa_elem(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_fa_elem
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_fa_elem(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_fa_elem(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_fa_elem
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_fa_elem(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_fa_elem(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_fa_elem
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_fa_elem(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, status, vlan, isid, n_mappings, vlan_step,
                                             isid_step, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [status] -
        [vlan] -
        [isid] -
        [n_mappings] -
        [vlan_step] -
        [isid_step] -

        add_lldp_tlv_fa_isid_vlan_assignment
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_fa_isid_vlan_assignment(self.current_port, router_id, status, vlan,
                                                                isid, n_mappings, vlan_step, isid_step)
        self._keyword_cleanup()

    def remove_lldp_tlv_fa_isid_vlan_assignment(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_fa_isid_vlan_assignment
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_fa_isid_vlan_assignment(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_fa_isid_vlan_assignment(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_fa_isid_vlan_assignment
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_fa_isid_vlan_assignment(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_fa_isid_vlan_assignment(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_fa_isid_vlan_assignment
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_fa_isid_vlan_assignment(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_capabilites(self, port_string, router_id, capabilty, network_policy, location_id,
                                     extended_power_pse, extended_power_pd, inventory, device_type, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [capabilty] -
        [network_policy] -
        [location_id] -
        [extended_power_pse] -
        [extended_power_pd] -
        [inventory] -
        [device_type] -

        add_lldp_tlv_med_capabilites
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_capabilites(self.current_port, router_id, capabilty,
                                                        network_policy, location_id, extended_power_pse,
                                                        extended_power_pd, inventory, device_type)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_capabilites(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_capabilites
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_capabilites(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_capabilites(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_capabilites
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_capabilites(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_capabilites(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_capabilites
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_capabilites(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_network_policy(self, port_string, router_id, network_policy_action,
                                        app_tlv_type, unknown, tagged, vlan_id, l2_priority, dscp, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [network_policy_action] -
        [app_tType] -
        [unknown] -
        [tagged] -
        [vlan_id] -
        [l2_priority] -
        [dscp] -

        add_lldp_tlv_med_network_policy
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_network_policy(self.current_port, router_id,
                                                           network_policy_action, app_tlv_type, unknown, tagged,
                                                           vlan_id, l2_priority, dscp)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_network_policy(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_network_policy
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_network_policy(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_network_policy(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_network_policy
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_network_policy(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_network_policy(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_network_policy
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_network_policy(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_location_id(self, port_string, router_id, coordinate_loc_action, civic_loc_action,
                                     ecs_elin_loc_action, coordinate_loc, civic_loc, ecs_elin_loc, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [coordinate_loc_action] -
        [civic_loc_action] -
        [ecs_elin_loc_action] -
        [coordinate_loc] -
        [civic_loc] -
        [ecs_elin_loc] -

        add_lldp_tlv_med_location_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_location_id(self.current_port, router_id,
                                                        coordinate_loc_action, civic_loc_action, ecs_elin_loc_action,
                                                        coordinate_loc, civic_loc, ecs_elin_loc)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_location_id(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_location_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_location_id(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_location_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_location_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_location_id(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_location_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_location_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_location_id(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_power_via_mdi(self, port_string, router_id, power_type, power_src, power_priority, power_value,
                                       **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [power_type] -
        [power_src] -
        [power_priority] -
        [power_value] -

        add_lldp_tlv_med_power_via_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_power_via_mdi(self.current_port, router_id, power_type,
                                                          power_src, power_priority, power_value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_power_via_mdi(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_power_via_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_power_via_mdi(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_power_via_mdi(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_power_via_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_power_via_mdi(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_power_via_mdi(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_power_via_mdi
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_power_via_mdi(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_hw_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_hw_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_hw_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_hw_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_hw_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_hw_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_hw_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_hw_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_hw_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_hw_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_hw_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_hw_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_firmware_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_firmware_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_firmware_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_firmware_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_firmware_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_firmware_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_firmware_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_firmware_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_firmware_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_firmware_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_firmware_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_firmware_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_software_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_software_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_software_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_software_revision(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_software_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_software_revision(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_software_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_software_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_software_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_software_revision(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_software_revision
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_software_revision(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_serial_number(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_serial_number
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_serial_number(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_serial_number(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_serial_number
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_serial_number(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_serial_number(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_serial_number
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_serial_number(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_serial_number(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_serial_number
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_serial_number(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_mfg_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_mfg_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_mfg_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_mfg_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_mfg_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_mfg_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_mfg_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_mfg_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_mfg_name(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_mfg_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_mfg_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_mfg_name(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_model_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_model_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_model_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_model_name(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_model_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_model_name(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_model_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_model_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_model_name(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_model_name(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_model_name
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_model_name(self.current_port, router_id)
        self._keyword_cleanup()

    def add_lldp_tlv_med_asset_id(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        add_lldp_tlv_med_asset_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.add_lldp_tlv_med_asset_id(self.current_port, router_id, value)
        self._keyword_cleanup()

    def remove_lldp_tlv_med_asset_id(self, port_string, router_id, value, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -
        [value] -

        remove_lldp_tlv_med_asset_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.remove_lldp_tlv_med_asset_id(self.current_port, router_id, value)
        self._keyword_cleanup()

    def start_tlv_med_asset_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        start_tlv_med_asset_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.start_tlv_med_asset_id(self.current_port, router_id)
        self._keyword_cleanup()

    def stop_tlv_med_asset_id(self, port_string, router_id, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [router_id] -

        stop_tlv_med_asset_id
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.LLDP_API, **kwargs)

        self.emulation_api.stop_tlv_med_asset_id(self.current_port, router_id)
        self._keyword_cleanup()
