from ExtremeAutomation.Library.Utils.FileUtils import FileUtils
from ExtremeAutomation.Library.Net.Packet.Utils.GenScript import *


base_path = "C:\\Users\\apepelis\\PycharmProject\\SQA_ROBOT_AUTOMATION\\"
types = ["Ixia", "Jets" ] #,"Spirent",  "Ostinato"]
base_classes={"TrafficGenerating": "TrafficGenerationApi",
              "NetworkEmulating": "TrafficGenerationApi"}
# generate_traffic_apis("NetworkEmulating", "Spbm", [])
# generate_traffic_apis("TrafficGenerating", "Spbm", {})
def generate_traffic_apis(base_type, protocol, methods):
    space = "    "
    s = S()
    base_class = base_classes[base_type]
    s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Apis."+base_class+" import "+base_class+"")
    s.a("import abc")
    #s.a("from ExtremeAutomation.Library.Utils.StringUtils import StringUtils")
    print("generate:" + base_type + protocol + "Api")
    s.a("")
    s.a("")
    s.a("class " + base_type + protocol + "Api(" + base_class + "):")

    s.a("\t\"\"\"")
    s.a("\tinit function")
    s.a("\t\"\"\"")
    s.a("\tdef __init__(self, device):")
    s.a("\t\tsuper(" + base_type + protocol + "Api, self).__init__(device)")
    for m in methods:
        s.a("")
        s.a("\t@abc.abstractmethod")
        s.a("\tdef "+m+":")
        s.a("\t\treturn self.log_unimplemented_method()")
    #write this to base_path + "ExtremeAutomation.Library.Device.TrafficGeneration.Apis."+base_type + protocol + "Api.py"
    print(str(s).replace("\t", space))

    for t in types:
        s = S()
        s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Apis."+base_type + protocol + "Api import "+base_type + protocol + "Api")
        s.a("from ExtremeAutomation.Library.Utils.StringUtils import StringUtils")
        print("generate:" + t + protocol + "Api extending " + base_type + protocol + "Api")
        s.a("")
        s.a("")
        s.a("class "+ t + protocol + "Api(" + base_type + protocol + "Api):")

        s.a("\t\"\"\"")
        s.a("\tinit function")
        s.a("\t\"\"\"")
        s.a("\tdef __init__(self, device):")
        s.a("\t\tsuper("+t + protocol + "Api, self).__init__(device)")
        for m in methods:
            s.a("")
            s.a("\tdef "+m+":")
            s.a("\t\treturn self.log_unimplemented_method()")
        print(str(s).replace("\t", space))
        #write this to base_path + "ExtremeAutomation.Library.Device.TrafficGeneration."+t+"Apis."+ t + protocol + "Api.py"


# generate_traffic_apis("TrafficGenerating", "Spbm", ["set_isis_globals(self, hello_interval=9, isi_multiplier=3, retrans_lsp_interval=5)",
#                                                     "create_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id, pnode_id, spb_instance, cost, enable=True)"])

# generate_traffic_apis("NetworkEmulating", "Spbm", ["set_isis_globals(self, hello_interval=9, isi_multiplier=3, retrans_lsp_interval=5)",
#                                                     "create_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id, pnode_id, spb_instance, cost, enable=True)"])


# generate_traffic_apis("NetworkEmulating", "Bgp", ["configure_network_generator_bgp_peer(self, port_string, handle_name, local_ip_addr, remote_ip_addr, vlan_id, source_mac, neighbor_type, local_as, ip_version, options=None)",
# "configure_network_generator_bgp_routes_on_bgp_peer(self, bgp_interface_handle, prefix, netmask, num_routes, origin_route_enable, origin, ip_version, options=None)",
# "start_network_generator_bgp_emulation(self, port_string, options=None)",
# "stop_network_generator_bgp_emulation(self, port_string, options=None)",
# "restart_network_generator_bgp_emulation(self, port_string, options=None)"])


# tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01 -state enable
# router create simOspfRtr ospf -device 1 -routerID 3.3.3.3 -areaID 0.0.0.0 -helloInterval 10 -deadInterval 40 -retransmittal 47 -cost 1 -priority 1 -intftype standard -learn true -areatype extcapable
# simOspfRtr log start update

# <name like simOspfRtrLink1 > add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1 -type AS_EXTERNAL -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0 -forwardAddr 0.0.0.0}}
# <name like simOspfRtrLink1 > remove -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1}}

# <name like simOspfRtrLink1 > getlist

# generate_traffic_apis("NetworkEmulating", "Ospf",
#                       ["create_ospf_interface(self, port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address, vlan_id, link_type=\"broadcast\", area_type=\"extcapable\", passive=False, prio=\"1\", cost=\"1\", trans_delay=\"40\", hello_int=\"10\", dead_int=\"40\", retrans_int=\"5\", wait_time=\"40\")",
#                        "add_ospf_route(self, port_string, router_id, first_ip, netmask,  num_routes, step=1, ls_type=\"AS_EXTERNAL\", adv_rtr=\"0.0.0.0\",forward_address=\"0.0.0.0\", age, cost=1, costype=\"type1_external\", ex_route_tag=1)",
#                        "delete_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1)",
#                        "remove_ospf_router(self, port_string, router_id)",
#                        "set_ospf_router_enabled(self, port_string, router_id, enable=True)",
#                        "get_ospf_state(self, port_string, router_id)",
#                        "add_ospf_lsas(self, port_string, router_id, lsa, receive_router)",
#                        "get_ospf_stats(self, port_string, router_id)",
#                        "add_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id, attached_router_ip )",
#                        "remove_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id, attached_router_ip )",
#                        "add_stub_network(self, port_string, router_id, ip_address, netmask)",
#                        "remove_stub_network(self, port_string, router_id, ip_address, netmask)"])

# router create simVrrpRtr vrrp -device 1 -ipaddr 16.1.1.1 -advIntInMsecs 1000 -version 33
# tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01 -state enable
# simVrrpRtr addVrf -vrfId 1 -bkupAddr 16.1.1.106 -priority 150
# simVrrpRtr enableVrf -vrfId 1
# simVrrpRtr disableVrf -vrfId 1
# simVrrpRtr removeVrf -vrfId 1
# simVrrpRtr deleteRouter  -device 1 -ipaddr 16.1.1.1

# generate_traffic_apis("NetworkEmulating", "Vrrp",
#                       ["create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id=None, advertise_interval_msecs=1000, version=2)",
#                        "remove_vrrp_router(self, port_string, router_id)",
#                        "add_vrf(self, port_string, router_id, vrf_id, backup_address, priority=150)",
#                        "enable_vrf(self, port_string, router_id, vrf_id)",
#                        "remove_vrf(self, port_string, router_id, vrf_id)"])

# http://avaya-svn.extremenetworks.com/svn/nes/Jets/trunk/src/com/nortel/jets/jetsTcl/lldp/
# lldp create lldpSim1 -device 1 -mac 00:00:fa:fa:16:01 -chassisMac 00:fa:fa:16:01:00 -ttl 120
# lldpSim1 enable
# lldpSim1 disable -sendPduWithZeroTtl true
# lldpSim1 enable
# lldpSim1 addLclMgmtAddr -lclMgmtAddr 192.168.1.1 -lclMgmtPort 1/1 -lclMgmtOid 1.3.1.4.1.2272.1.8.2.1.2.64
# lldpSim1 txTlv -tlv local-mgmt-addr
# lldpSim1 stopTxTlv -tlv local-mgmt-addr
# lldpSim1 disable -sendPduWithZeroTtl true
# lldpSim1 enable
# lldpSim1 setAttributes -capSupported 128 -capEnabled 128
# lldpSim1 txTlv -tlv sys-cap
# lldpSim1 stopTxTlv -tlv sys-cap
# lldpSim1 disable -sendPduWithZeroTtl true
# lldpSim1 enable
# lldpSim1 setAttributes -sysDesc "JETS-SIMULATOR"
# lldpSim1 txTlv -tlv sys-desc
# lldpSim1 stopTxTlv -tlv sys-desc
# lldpSim1 disable -sendPduWithZeroTtl true


# generate_traffic_apis("NetworkEmulating", "Lldp",
#                       ["create_lldp_interface(self, port_string, router_id, mac_address, chassic_mac, ttl)", # lldp create lldpSim1 -device 1 -mac 00:00:fa:fa:16:01 -chassisMac 00:fa:fa:16:01:00 -ttl 120
#                        "remove_lldp_interface(self, port_string, router_id)", # lldpSim1 delete
#                        "enable_lldp(self, port_string, router_id, enabled=True)", # lldpSim1 enable   lldpSim1 disable -sendPduWithZeroTtl true
#                        #"set_lldp_attribute(self, port_string, router_id, sysdesc=None, portdesc=None, capsupported=None, capenabled=None, interface_name=None, send_mac_as_port_id=None)", # lldpSim1 setAttributes -capSupported 128 -capEnabled 128
#                        # lldpSim1 setAttributes -sysDesc "JETS-SIMULATOR"
#                        #"set_lldp_attribute_localmanagement(self, port_string, router_id, localmanagement_address, localmanagement_port, localmanagement_oid)", # lldpSim1 addLclMgmtAddr -lclMgmtAddr 192.168.1.1 -lclMgmtPort 1/1 -lclMgmtOid 1.3.1.4.1.2272.1.8.2.1.2.64
#                        #"set_lldp_attribute_dot1_port_protocol_vlan(self, port_string, router_id, vlanId, supported, enabled)", # lldpSim1 addDot1PortProtocol -vlanId <> -supported <> -enbaled <>
#                        "start_transmit_tlv(self, port_string, router_id, tlv_name)", # lldpSim1 txTlv -tlv sys-cap
#                        "stop_transmit_tlv(self, port_string, router_id, tlv_name)"]) # lldpSim1 stopTxTlv -tlv sys-desc

# "sys-name""sys-desc""sys-cap""port-desc""local-mgmt-addr"
# "dot1-port-vlan-id""dot1-protocol-identity""dot1-port-protocol-vlan-id"
# "dot1-vlan-name""dot3-mac-phy-config-status""dot3-power-mdi""dot3-link-aggregation"
# "dot3-maximum-frame-size""fa-elem""fa-isid-vlan-assignment""med-capabilites"
# "med-network-policy""med-location-id""med-power-via-mdi""med-hw-revision""med-firmware-revision"
# "med-software-revision""med-serial-number""med-mfg-name""med-model-name""med-asset-id"

# create_vxlan_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id)
# meshost create mltRtrEndpt1 -type MLT -macAddr 00:00:13:01:01:02 -ipAddr 13.1.1.2 -vlanId 133 -defGateway 13.1.1.1 -mask 255.255.255.0 -group testCtrl-IpStacks
# INFO: Created MLT host mltRtrEndpt1
# multilink trunk
# DEBUG: Host mltRtrEndpt1 defaultRoute was set to 13.1.1.1
# mltRtrEndpt1 addCircuits -intfs " 3"
# mltRtrEndpt1 enable -ignoreDhcpGwOption false
# mltRtrEndpt1 setOutCircuit -intf 3

# add_vxlan_host(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id)
# 1
# tcpip alias -device 3 -ipAddr 11.11.11.11 -netmask 255.255.255.255 -rtrStackIp 13.1.1.2
# Created stack behind router mltRtrEndpt1-13.1.1.2:ETH1
#
# tcpip alias -device 3 -ipAddr 10.10.10.21 -netmask 255.255.255.0 -rtrStackIp 11.11.11.11 -vnid 100 -vtepdest 9.9.9.9 -macAddress 00:00:10:10:10:21 -group testCtrl-IpStacks
# Enet registered under VXLAN : CircuitEnet:VXLANTUNNEL:100_11.11.11.11_9.9.9.9 mtu=1522
# Created stack behind router IpStack:CircuitEnet:ETH0 mtu=1950:Ip:11.11.11.11
#
# 2
# tcpip alias -device 3 -ipAddr 12.12.12.12 -netmask 255.255.255.255 -rtrStackIp 13.1.1.2
# Created stack behind router mltRtrEndpt1-13.1.1.2:ETH1
#
# tcpip alias -device 3 -ipAddr 10.10.10.22 -netmask 255.255.255.0 -rtrStackIp 12.12.12.12 -vnid 100 -vtepdest 9.9.9.9 -macAddress 00:00:10:10:10:22 -group testCtrl-IpStacks
# Enet registered under VXLAN : CircuitEnet:VXLANTUNNEL:100_12.12.12.12_9.9.9.9 mtu=1522
# Created stack behind router IpStack:CircuitEnet:ETH0 mtu=1950:Ip:12.12.12.12
#

#
# generate_traffic_apis("NetworkEmulating", "Vxlan",
#                       ["create_vxlan_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id)",
#                        "add_vxlan_host(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address, vlan_id)"])
#

# JETS_SIM>tcpip config -device 1 -ipAddr 66.1.0.1 -netmask 255.255.255.0 -gateway 66.1.0.6 -macAddress 0.0.11.66.00.01 -vlanId 2 -userPriority 0 -CFI 0 -state enable
# JETS_SIM>tcpip alias -device 1 -ipAddr 66.1.0.2 -netmask 255.255.255.0 -gateway 66.1.0.6 -macAddress 0.0.11.66.00.02 -vlanId 2 -userPriority 0 -CFI 0 -state enable
# Completed Alias for IpStack:CircuitEnet:ETH5 mtu=1514:IpRtr:66.1.0.2
# JETS_SIM>rip config -device 1 -txdelay 100
# JETS_SIM>rip config -device 1
# JETS_SIM>router create simRipRtr rip -device 1 -ipaddr 66.1.0.1 -mode R1 -refreshtime 30
# JETS_SIM>rip config -device 1
# JETS_SIM>router create simVrf1RipRtr rip -device 1 -ipaddr 66.1.1.1 -mode R1 -refreshtime 30
# JETS_SIM>rip config -device 1
# JETS_SIM>router create simVrf255RipRtr rip -device 1 -ipaddr 66.1.255.1 -mode R1 -refreshtime 30
# JETS_SIM>simRipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1 -nexthop 0.0.0.0 }}
# JETS_SIM>simVrf1RipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1 -nexthop 0.0.0.0 }}
# JETS_SIM>simVrf255RipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1 -nexthop 0.0.0.0 }}
# JETS_SIM>simVrf1RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}
# JETS_SIM>simVrf255RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}

#
# generate_traffic_apis("NetworkEmulating", "Rip",
#                       ["create_rip_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address, vlan_id, mode=\"R1\", refresh_time=30)",
#                        "add_rip_route(self, port_string, router_id, first_ip, netmask=\"0.0.0.0\", next_hop=\"0.0.0.0\", metric=1, num_routes=1, step=1)",
#                        "delete_rip_route(self, port_string, router_id, first_ip, netmask=\"0.0.0.0\", num_routes=1, step=1)",
#                        "remove_rip_router(self, port_string, router_id)",
#                        "rip_config(self, port_string, tx_delay)",
#                        "get_rip_state(self, port_string, router_id)",
#                        "get_rip_stats(self, port_string, router_id)",])


# JETS_SIM>tcpip config -device 1 -ipAddr 1016::1 -prefixLen 64 -macAddress 0.0.10.16.00.01 -state enable
# JETS_SIM>router create simRipRtr1 rip -device 1 -ipaddr 1016::1 -mode R1 -refreshtime 30

# JETS_SIM>simRipRtr1 add -routes {{-ipAddr 0:0:0:0:0:0:0:0 -prefixLen 0 -numAddr 1 -step 1 -metric 1 -nexthop 0:0:0:0:0:0:0:0 }}
# JETS_SIM>simRipRtr1 add -routes {{-ipAddr 3010:1::0 -prefixLen 64 -numAddr 1 -step 1 -metric 1 }}
# JETS_SIM>simRipRtr1 remove -routes {{-ipAddr 0:0:0:0:0:0:0:0 -prefixLen 0 -numAddr 1 -step 1 }}
#
# generate_traffic_apis("NetworkEmulating", "RipNg",
#                       ["create_ripng_interface(self, port_string, router_id_and_source_ip, prefix_length, mac_address, vlan_id, mode=\"R1\", refresh_time=30)",
#                        "add_ripng_route(self, port_string, router_id, first_ip,  next_hop=\"0:0:0:0:0:0:0:0\", metric=1, num_routes=1, step=1)",
#                        "delete_ripng_route(self, port_string, router_id, first_ip, num_routes=1, step=1)",
#                        "remove_ripng_router(self, port_string, router_id)",
#                        "ripng_config(self, port_string, tx_delay)",
#                        "get_ripng_stats(self, port_string, router_id)",])


# JETS_SIM>bridge addDvrGw -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24 -gateway 10.10.10.1 -vrfId 0 -vlan_ip_interface 10.10.10.2
# Created DvrIpv4GatewayTlv:0:999:10.10.10.1:24:0:0:0:e:a:f:0:0:0:e:a:62:0:0:0:e:a:f and 10.10.10.1
#
# JETS_SIM>bridge addDvrRoute -bridgeName edgeA -l3isid 0 -l2isid 999 -cmac 0:0:0:0:0:0 -maskLen 24 -network 10.10.10.0 -nexthop 10.10.10.1 -vrfId 0 -domainId 3
# Created DvrIpv4RouteTlv:0:999:10.10.10.0:24:0:0:0:e:a:f:0:0:0:e:a:62:3
#
# JETS_SIM>bridge addDvrMcast -bridgeName edgeA -l3isid 0 -l2isid 999 -mcastCfg 1 -igmpVersion 2
# Created key=0:999 and tlv=DvrMulticastConfigTlv:0:999:1:2:125:100:2:10:1
#
# JETS_SIM>bridge addHostBehindDvrGw -bridgeName edgeA -l3isid 0 -ipAddr 10.10.10.53 -macAddr 00:00:00:aa:aa:01 -gwAddr 10.10.10.1
# Created DvrEp:10.10.10.53:Behind:10.10.10.1


# generate_traffic_apis("NetworkEmulating", "Dvr",
#                       ["add_dvr_gateway(self, port_string, router_id, l3_isid, l2_isid, cmac, mask_length, gateway, vlan_ip_interface)",
#                         "delete_dvr_gateway(self, port_string, router_id, l3_isid, l2_isid, gateway)",
#                         "add_dev_route(self, port_string, router_id, l3_isid, l2_isid, cmac, mask_length, network_address, next_hop, domain_id)",
#                         "delete_dev_route(self, port_string, router_id, l3_isid, l2_isid, cmac, mask_length, network_address)",
#                         "add_dev_multicast(self, port_string, router_id, l3_isid, l2_isid, multicast_config, igmp_version)",
#                         "delete_dev_multicast(self, port_string, router_id, l3_isid, l2_isid)",
#                         "create_dvr_gw_endpoint(self, bridgeName, basename, l3_sid, starting_ip, mac_address, gateway)",])


generate_traffic_apis("NetworkEmulating", "Dhcp",
                      ["create_dhcp_client(self, port_string, mac_address, network_mask, vlan=-1, count=1, step=1)",
                        "remove_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1)",
                        "start_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1)",
                        "get_dhcp_client_address(self, port_string, mac_address)",
                        "ping_dhcp_client(self, port_string, mac_address, network_mask, destination_ip)"])
