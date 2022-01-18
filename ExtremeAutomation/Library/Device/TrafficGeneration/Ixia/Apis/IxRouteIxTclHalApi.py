from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxiaIxTclHalApi import IxiaIxTclHalApi
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxRouteIxTclHalConstants(object, metaclass=Singleton):
    # api reference constant for this api to get it from the device
    IXROUTE_TCL_HAL_API = "IXROUTE_TCL_HAL_API"

    ARP_MODE_RESOLVE_ARP = "arpGatewayOnly"
    ARP_MODE_LEARN_ARP = "arpLearnOnly"
    ARP_MODE_RESOLVE_AND_LEARN_ARP = "arpGatewayAndLearn"

    IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC = "oneIpToOneMAC"
    IP_TABLE_MAPPING_OPTIONS_MANY_IPS_TO_ONE_MAC = "manyIpToOneMAC"

    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_IPV4_ROUTED = "atmEncapsulationVccMuxIPV4Routed"
    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_BRIDGED_ETHERNET_FCS = "atmEncapsulationVccMuxBridgedEthernetFCS"
    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_BRIDGED_ETHERNET_NOFCS = "atmEncapsulationVccMuxBridgedEthernetNoFCS"
    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_IPV6_ROUTED = "atmEncapsulationVccMuxIPV6Routed"
    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_MPLS_ROUTED = "atmEncapsulationVccMuxMPLSRouted"
    IP_TABLE_ATM_ENCAPSULATION_LLC_ROUTED_CLIP = "atmEncapsulationLLCRoutedCLIP"
    IP_TABLE_ATM_ENCAPSULATION_LLC_BRIDGED_ETHERNET_FCS = "atmEncapsulationLLCBridgedEthernetFCS"
    IP_TABLE_ATM_ENCAPSULATION_LLC_BRIDGED_ETHERNET_NOFCS = "atmEncapsulationLLCBridgedEthernetNoFCS"
    IP_TABLE_ATM_ENCAPSULATION_LLC_PPP_OA = "atmEncapsulationLLCPPPoA"
    IP_TABLE_ATM_ENCAPSULATION_VCC_MUX_PPP_OZ = "atmEncapsulationVccMuxPPPoA"

    # Don't allow values to be updated.
    def __setattr__(self, *_):
        pass


class IxRouteIxTclHalApi(IxiaIxTclHalApi):
    def __init__(self, device):
        super(IxRouteIxTclHalApi, self).__init__(device)

# atmEncapsulation - For ATM type load modules, this is the type of ATM encapsulation that is used on the interface.
#     atmEncapsulationVccMuxIPV4Routed 101
#     atmEncapsulationVccMuxBridgedEthernetFCS 102
#     atmEncapsulationVccMuxBridgedEthernetNoFCS 103
#     atmEncapsulationVccMuxIPV6Routed 104
#     atmEncapsulationVccMuxMPLSRouted 105
#     atmEncapsulationLLCRoutedCLIP 106
#     atmEncapsulationLLCBridgedEthernetFCS 107 (default)
#     atmEncapsulationLLCBridgedEthernetNoFCS 108
#     atmEncapsulationLLCPPPoA 109
#     atmEncapsulationVccMuxPPPoA 110
# atmVci - The ATM VCI number, if this is an ATM port. (default = 0)
# atmVpi - The ATM VPI number, if this is an ATM port. (default = 0)
# enableExpandInterfaceTable - true | false
#     If true, then the range of IP addresses from fromIpAddress to toIpAddress are
#     expanded to individual IP addresses on the port. This only operates on ports with
#     individual CPUs and is for internal use only. (default = false)
# enableUseNetwork - true / false If set, the netMask field is used to set the network mask; otherwise, the network
#     mask is 0.0.0.0. (default = false)
# enableVlan - true / false Enables VLAN encapsulation of routing protocols. The VLAN ID is in the vlanId option.
#     (default = false)
# fromIpAddress - The first IP address for the IP address range. (default = 0.0.0.0)
# fromMacAddress - The first MAC address for the MAC address range. (default = {00 00 00 00 00
# 00})
# gatewayIpAddress - Default gateway IP address. (default = 0.0.0.0)
# mappingOption - Specifies the mapping option.
#     oneIpToOneMAC 0 (default)
#     manyIpToOneMAC 1
# netMask - If enableUseNetwork is set, this value is used to set the network mask. (default = 24).
# numAddresses - Number of consecutive addresses. (default = 1)
# overrideDefaultGateway - true/false Enable default gateway IP address. (default =false)
# toIpAddress - Read-Only. Last IP address in the IP address range. (default = 0.0.0.0)
# toMacAddress - Read-Only. Last MAC address in the MAC address range. (default = 00 00 00 00
# 00 00)
# vlanId - If enableVlan is true, the routing protocols are VLAN encapsulated with this ID.
#     Although a value of '0' is allowed, VLAN IDs normally start at 1. (default = 0)
# ipAddressTable setDefault
# ipAddressTable config -defaultGateway                     "0.0.0.0"
# ipAddressTableItem setDefault
# ipAddressTableItem config -fromIpAddress                      "151.1.1.1"
# ipAddressTableItem config -fromMacAddress                     "00 00 97 01 01 01"
# ipAddressTableItem config -numAddresses                       10
# ipAddressTableItem config -mappingOption                      0
# ipAddressTableItem config -overrideDefaultGateway             1
# ipAddressTableItem config -gatewayIpAddress                   "151.1.1.2"
# ipAddressTableItem config -enableUseNetwork                   true
# ipAddressTableItem config -netMask                            24
# ipAddressTableItem config -enableExpandInterfaceTable         false
# ipAddressTableItem config -enableVlan                         false
# ipAddressTableItem config -vlanId                             0
# ipAddressTableItem config -atmEncapsulation                   atmEncapsulationLLCBridgedEthernetFCS
# ipAddressTableItem config -atmVpi                             0
# ipAddressTableItem config -atmVci                             0
# if {[ipAddressTable addItem]} {
# 	errorMsg "Error calling ipAddressTable addItem"
# 	set retCode $::TCL_ERROR
# }
#
# if {[ipAddressTable set $chassis $card $port]} {
# 	errorMsg "Error calling ipAddressTable set $chassis $card $port"
# 	set retCode $::TCL_ERROR
# }

    def configure_ip_address_table(
            self, port_string, default_gateway="0.0.0.0", from_ip_address="151.1.1.1",
            from_mac_address="00 00 97 01 01 01", num_addresses=10, mapping_option=0,
            override_default_gateway=1, gateway_ip_address="151.1.1.2",
            enable_use_network="true", netmask=24, enable_expand_interface_table="false",
            enable_vlan="false", vlan_id=0,
            atm_encapsulation=IxRouteIxTclHalConstants.IP_TABLE_ATM_ENCAPSULATION_LLC_BRIDGED_ETHERNET_FCS,
            atm_vpi=0, atm_vci=0, clear_settings_first=False):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        if clear_settings_first:
            commands.append("ipAddressTable setDefault")
        else:
            commands.append("ipAddressTable get " + port_string)
        commands.append("ipAddressTable config -defaultGateway                  " + str(default_gateway))
        commands.append("ipAddressTableItem setDefault")
        commands.append("ipAddressTableItem config -fromIpAddress               " + str(from_ip_address))
        commands.append("ipAddressTableItem config -fromMacAddress              " + str(from_mac_address))
        commands.append("ipAddressTableItem config -numAddresses                " + str(num_addresses))
        commands.append("ipAddressTableItem config -mappingOption               " + str(mapping_option))
        commands.append("ipAddressTableItem config -overrideDefaultGateway      " + str(override_default_gateway))
        commands.append("ipAddressTableItem config -gatewayIpAddress            " + str(gateway_ip_address))
        commands.append("ipAddressTableItem config -enableUseNetwork            " + str(enable_use_network))
        commands.append("ipAddressTableItem config -netMask                     " + str(netmask))
        commands.append("ipAddressTableItem config -enableExpandInterfaceTable  " + str(enable_expand_interface_table))
        commands.append("ipAddressTableItem config -enableVlan                  " + str(enable_vlan))
        commands.append("ipAddressTableItem config -vlanId                      " + str(vlan_id))
        commands.append("ipAddressTableItem config -atmEncapsulation            " + str(atm_encapsulation))
        commands.append("ipAddressTableItem config -atmVpi                      " + str(atm_vpi))
        commands.append("ipAddressTableItem config -atmVci                      " + str(atm_vci))
        commands.append("ipAddressTable addItem")
        commands.append("ipAddressTable set " + port_string)
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)
        pass

# arpServer setDefault
# arpServer config -retries                            3
# arpServer config -mode                               arpGatewayOnly|arpLearnOnly|arpGatewayAndLearn
# arpServer config -rate                               2083333
# arpServer config -requestRepeatCount                 3
# if {[arpServer set $chassis $card $port]} {
# 	errorMsg "Error calling arpServer set $chassis $card $port"
# 	set retCode $::TCL_ERROR
# }

    def configure_arp_server(self, port_string, retires=3, mode=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP,
                             rate=2083333, request_repeat_count=3, clear_settings_first=False):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        if clear_settings_first:
            commands.append("arpServer setDefault")
        else:
            commands.append("arpServer get " + port_string)
        commands.append("arpServer config -retries                         " + str(retires))
        commands.append("arpServer config -mode                            " + str(mode))
        commands.append("arpServer config -rate                            " + str(rate))
        commands.append("arpServer config -requestRepeatCount              " + str(request_repeat_count))
        commands.append("arpServer set " + port_string)
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

# protocolServer setDefault
# protocolServer config -enableArpResponse                  true
# protocolServer config -enablePingResponse                 true
# if {[protocolServer set $chassis $card $port]} {
# 	errorMsg "Error calling protocolServer set $chassis $card $port"
# 	set retCode $::TCL_ERROR
# }

    def configure_protocol_server(self, port_string, enable_arp_response=False, enable_ping_response=False,
                                  clear_settings_first=False):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        commands.append("protocolServer setDefault")
        commands.append("protocolServer config -enableArpResponse                         " +
                        str(enable_arp_response).lower())
        commands.append("protocolServer config -enablePingResponse                        " +
                        str(enable_ping_response).lower())
        commands.append("protocolServer set " + port_string)
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)

# interfaceTable configure options:
# dhcpV4RequestRate - The user-specified maximum number of Request messages that can be sent per
#   second from the client to the server, requesting an IPv4 address. A value of zero
#   (0) indicates that there is no rate control, that is, requests are sent as fast as
#   possible.
# dhcpV6RequestRate - The user-specified maximum number of Request messages that can be sent per
#   second from the client to the server, requesting an IPv6 address. A value of zero
#   (0) indicates that there is no rate control, that is, requests are sent as fast as
#   possible.
# dhcpV4MaximumOut-standingRequests -
#   The maximum number of DHCP V4 requests that can be pending, waiting replies
#   from the server. If this number is reached, no further requests can be sent until an
#   acknowledgment is received for a pending request.
# dhcpV6MaximumOut-standingRequests -
#   The maximum number of DHCP V6 requests that can be pending, waiting replies
#   from the server. If this number is reached, no further requests can be sent until an
#   acknowledgment is received for a pending request.
# enableFcfMac - Enables FCF MAC address.
# enablePMacInFpma - Enables PMAC.
# enableNameIdInVLANDiscovery - Enables Name ID parameter in Discovery VLAN.
# enableTargetLinkLayerAddrOption - Enables Target Link Layer Address option.
# enableAutoNeighborDiscovery - Enables Auto Neighbor Discovery parameter. If true and then MAC interface is
#   enabled, the Discovered Neighbors parameters are automatically available.
# enableAutoArp - Enables Auto ARP option. If true and then MAC interface is enabled, the
#   Learned IP Addresses and Learned MAC Addresses are automatically available.
# fcfMacCollectionTime - The FCF MAC collection time.
# fcoeNumRetries - FCoE number of retries before being marked as Failure. (default = 5)
# fcoeRetryInterval - FCoE interval between retries. (default = 2000)
# fcoeRequestRate - FCoE maximum rate (packets/second). (default = 500)
# fipVersion - FIP version. (default = 1)
#     fipVersion0 0 The version in incoming packets should
#     have the same value as the one
#     configured in IxExplorer, otherwise
#     packets is dropped.
#     fipVersion1 1 (default) See Usage for fipVersion0,
#     above.
#     fipVersionAuto 8888 The protocol sends packets matching
#     the fipversion of incoming packets. If
#     incoming packets are version 0, then
#     FIP sends version 0 packets; if
#     incoming packets are version 1 then
#     FIP sends version 1 packets.

#
# if {[interfaceTable select $chassis $card $port]} {
# 	errorMsg "Error calling interfaceTable select $chassis $card $port"
# 	set retCode $::TCL_ERROR
# }
#
# interfaceTable setDefault
# interfaceTable config -dhcpV4RequestRate                  0
# interfaceTable config -dhcpV6RequestRate                  0
# interfaceTable config -dhcpV4MaximumOutstandingRequests   100
# interfaceTable config -dhcpV6MaximumOutstandingRequests   100
# interfaceTable config -fcoeRequestRate                    500
# interfaceTable config -fcoeNumRetries                     5
# interfaceTable config -fcoeRetryInterval                  2000
# interfaceTable config -fipVersion                         fipVersion1
# interfaceTable config -enableFcfMac                       false
# interfaceTable config -fcfMacCollectionTime               1000
# interfaceTable config -enablePMacInFpma                   true
# interfaceTable config -enableNameIdInVLANDiscovery        false
# interfaceTable config -enableTargetLinkLayerAddrOption    false
# interfaceTable config -enableAutoNeighborDiscovery        false
# interfaceTable config -enableAutoArp                      false
# if {[interfaceTable set]} {
# 	errorMsg "Error calling interfaceTable set"
# 	set retCode $::TCL_ERROR
# }
#
# interfaceTable clearAllInterfaces
# if {[interfaceTable write]} {
# 	errorMsg "Error calling interfaceTable write"
# 	set retCode $::TCL_ERROR
# }

    def configure_interface_table(self, port_string, dhcp_v4_request_rate, dhcp_v6_request_rate,
                                  dhcp_v4_maximum_outstanding_requests, dhcp_v6_maximum_outstanding_requests,
                                  fcoe_request_rate, fcoe_num_retries, fcoe_retry_interval, fip_version,
                                  enable_fcf_mac, fcf_mac_collection_time, enable_pmac_in_fpma,
                                  enable_name_id_in_vlan_discovery, enable_target_link_layer_addr_option,
                                  enable_auto_neighbor_discovery, enable_auto_arp, clear_settings_first=False):
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        commands = list()
        commands.append("port get " + str(port_string))
        if clear_settings_first:
            commands.append("interfaceTable setDefault")
        else:
            commands.append("interfaceTable get " + port_string)
        commands.append("interfaceTable config -dhcpV4RequestRate                " + str(dhcp_v4_request_rate))
        commands.append("interfaceTable config -dhcpV6RequestRate                " + str(dhcp_v6_request_rate))
        commands.append("interfaceTable config -dhcpV4MaximumOutstandingRequests " +
                        str(dhcp_v4_maximum_outstanding_requests))
        commands.append("interfaceTable config -dhcpV6MaximumOutstandingRequests " +
                        str(dhcp_v6_maximum_outstanding_requests))
        commands.append("interfaceTable config -fcoeRequestRate                  " + str(fcoe_request_rate))
        commands.append("interfaceTable config -fcoeNumRetries                   " + str(fcoe_num_retries))
        commands.append("interfaceTable config -fcoeRetryInterval                " + str(fcoe_retry_interval))
        commands.append("interfaceTable config -fipVersion                       " + str(fip_version))
        commands.append("interfaceTable config -enableFcfMac                     " + str(enable_fcf_mac))
        commands.append("interfaceTable config -fcfMacCollectionTime             " + str(fcf_mac_collection_time))
        commands.append("interfaceTable config -enablePMacInFpma                 " + str(enable_pmac_in_fpma))
        commands.append("interfaceTable config -enableNameIdInVLANDiscovery      " +
                        str(enable_name_id_in_vlan_discovery))
        commands.append("interfaceTable config -enableTargetLinkLayerAddrOption  " +
                        str(enable_target_link_layer_addr_option))
        commands.append("interfaceTable config -enableAutoNeighborDiscovery      " +
                        str(enable_auto_neighbor_discovery))
        commands.append("interfaceTable config -enableAutoArp                    " + str(enable_auto_arp))
        commands.append("interfaceTable set ")
        commands.append("port set " + str(port_string))
        commands.append("port write " + str(port_string))
        commands.append("set portList [ list [ list " + port_string + "]]")
        commands.append("ixWriteConfigToHardware portList -noProtocolServer")
        self.send_commands(commands)
