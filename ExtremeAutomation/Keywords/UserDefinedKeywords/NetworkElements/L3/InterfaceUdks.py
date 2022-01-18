from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementInterfaceGenKeywords import NetworkElementInterfaceGenKeywords


class InterfaceUdks():
    def __init__(self) -> None:
        self.networkElementInterfaceGenKeywords = NetworkElementInterfaceGenKeywords()

    def Configure_Primary_IPv4_Address_Enable_Interface_and_Validate(self, netelem_name, vlan, host_ip, host_ip_mask, **kwargs):
        self.networkElementInterfaceGenKeywords.interface_set_ipv4_primary_addr_netmask(netelem_name, vlan, host_ip, host_ip_mask, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_verify_ip_address(netelem_name, vlan, host_ip, host_ip_mask, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_enable_ip_forwarding(netelem_name, vlan, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_enable_interface(netelem_name, vlan, **kwargs)

    def Configure_IPv6_Address_Enable_Interface_and_Validate(self, netelem_name, vlan, ipv6, prefix, **kwargs):
        self.networkElementInterfaceGenKeywords.Interface_Set_IPv6_Address(netelem_name, vlan, ipv6, prefix, **kwargs)
        self.networkElementInterfaceGenKeywords.Interface_Verify_IPv6_Address(netelem_name, vlan, ipv6, prefix, **kwargs)
        self.networkElementInterfaceGenKeywords.Interface_Enable_IPv6_Forwarding(netelem_name, vlan, **kwargs)
        self.networkElementInterfaceGenKeywords.Interface_Enable_Interface(netelem_name, vlan, **kwargs)

    def Remove_Primary_IPv4_Address_Interface_and_Validate_Interface_Removed(self, netelem_name, vlan, **kwargs):
        self.networkElementInterfaceGenKeywords.Interface_Delete_Interface(netelem_name, vlan, **kwargs)
        self.networkElementInterfaceGenKeywords.Interface_Verify_Does_Not_Exist(netelem_name, vlan, **kwargs)

    def Configure_Loopback_IPv4_Address_Enable_and_Validate(self, netelem_name, loop_id, ipaddr, mask, **kwargs):
        self.networkElementInterfaceGenKeywords.interface_create_loopback(netelem_name, loop_id, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_set_ipv4_loopback_addr_netmask(netelem_name, loop_id, ipaddr, mask, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_enable_loopback(netelem_name, loop_id, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_verify_loopback_ipv4_address(netelem_name, loop_id, ipaddr, mask, **kwargs)

    def Remove_Loopback_and_Verify(self, netelem_name, loop_id, **kwargs):
        self.networkElementInterfaceGenKeywords.interface_delete_loopback(netelem_name, loop_id, **kwargs)
        self.networkElementInterfaceGenKeywords.interface_verify_loopback_does_not_exist(netelem_name, loop_id, **kwargs)
