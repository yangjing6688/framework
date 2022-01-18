from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import IxRouteIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceArpHelper import \
    TrafficGeneratingDeviceArpHelper


class SpirentArpHelper(TrafficGeneratingDeviceArpHelper):

    def configure_arp(self, port_string, start_ip, start_mac, num_addresses, gateway_address,
                      mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                      arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                      netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        # port_string = self.convert_port_to_port_handle(port_handle)
        port_handle = self.convert_port_to_port_handle(port_string)
        self.send_command("set hProject [stc::create project]")
        self.send_command("set hHostTx [stc::create Host -under $hProject -EnablePingResponse TRUE]")
        # Create an Ethernet/Ipv4 protocol stack.
        self.send_command("set txIpAddr \"" + str(start_ip) + "\"")
        self.send_command("set rxIpAddr \"" + str(gateway_address) + "\"")
        self.send_command("set txMacAddr \"" + str(start_mac) + "\"")

        self.send_command("set hEthTxIf [stc::create \"EthIIIf\" \\\n" +
                          "-under $hHostTx \\\n" +
                          "-sourceMac $txMacAddr ]")

        self.send_command("set hIPv4TxIf [stc::create \"Ipv4If\" \\\n" +
                          "-under $hHostTx \\\n" +
                          "-address $txIpAddr \\\n" +
                          "-PrefixLength \"" + str(netmask) + "\" \\\n" +
                          "-gateway $rxIpAddr ] ")

        if vlan_enable:
            self.send_command("set hVlanTxIf [stc::create \"VlanIf\" \\\n" +
                              "-under $hHostTx \\\n" +
                              "-VlanID \"" + str(vlan_id) + "\" ] ")

        # -under $host(2) \
        #         -Address "30.1.0.3" \
        #         -PrefixLength "24" \
        #         -UsePortDefaultIpv4Gateway "FALSE" \
        #         -Gateway "30.1.0.1" \
        #         -ResolveGatewayMac "TRUE" \
        #        -Name "Ipv4If 2"]

        # Specify the top of the stack.
        self.send_command("stc::config $hHostTx -TopLevelIf-targets $hIPv4TxIf")

        # Order the remaining stack items.
        if vlan_enable:
            self.send_command("stc::config $hIPv4TxIf -stackedOnEndpoint-targets $hVlanTxIf")
            self.send_command("stc::config $hVlanTxIf -stackedOnEndpoint-targets $hEthTxIf")
        else:
            self.send_command("stc::config $hIPv4TxIf -stackedOnEndpoint-targets $hEthTxIf")

        # Specify the top level interface facing the DUT.
        self.send_command("stc::config $hHostTx -PrimaryIf-targets $hIPv4TxIf")

        # Affiliate the host with a port.
        self.send_command("stc::config $hHostTx -AffiliationPort-targets " + port_handle)

        self.send_command("stc::apply")

        # ---------------------------
        # Start ArpNd
        # ---------------------------
        self.send_command("stc::perform ArpNdStart -HandleList [list " + port_handle + "] -WaitForArpToFinish TRUE")
        pass

    def configure_neighbor_discovery(self, port_string, start_ipv6, start_mac, num_addresses, gateway_address,
                                     mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                                     arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                                     netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        return self.logger.log_unimplemented_method()

    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3):
        return self.logger.log_unimplemented_method()
