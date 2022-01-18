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
    s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Apis." +base_class +" import " +base_class +"")
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
        s.a("\tdef " +m +":")
        s.a("\t\treturn self.logger.log_unimplemented_method()")
    #write this to base_path + "ExtremeAutomation.Library.Device.TrafficGeneration.Apis."+base_type + protocol + "Api.py"
    print(str(s).replace("\t", space))

    for t in types:
        s = S()
        s.a("from ExtremeAutomation.Library.Device.TrafficGeneration.Apis." +base_type + protocol + "Api import " +base_type + protocol + "Api")
        s.a("from ExtremeAutomation.Library.Utils.StringUtils import StringUtils")
        print("generate:" + t + protocol + "Api extending " + base_type + protocol + "Api")
        s.a("")
        s.a("")
        s.a("class "+ t + protocol + "Api(" + base_type + protocol + "Api):")

        s.a("\t\"\"\"")
        s.a("\tinit function")
        s.a("\t\"\"\"")
        s.a("\tdef __init__(self, device):")
        s.a("\t\tsuper(" +t + protocol + "Api, self).__init__(device)")
        for m in methods:
            s.a("")
            s.a("\tdef " +m +":")
            s.a("\t\treturn self.logger.log_unimplemented_method()")
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

types = ["sys-name", "sys-desc", "sys-cap", "port-desc", "local-mgmt-addr",
         "dot1-port-vlan-id", "dot1-protocol-identity", "dot1-port-protocol-vlan-id",
         "dot1-vlan-name", "dot3-mac-phy-config-status", "dot3-power-mdi", "dot3-link-aggregation",
         "dot3-maximum-frame-size", "fa-elem", "fa-isid-vlan-assignment", "med-capabilites"
         "med-network-policy", "med-location-id", "med-power-via-mdi", "med-hw-revision", "med-firmware-revision",
         "med-software-revision", "med-serial-number", "med-mfg-name", "med-model-name", "med-asset-id"]

for t in types:
    fname = t.replace("-","_")
    print("####" * 10)
    print("######## " + str(t) + " ############")
    print("####" * 10)
    print("def add_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n	" +
          "type = \"" + t + "\"\n"
          "    routername = self.__get_lldp_router_name(port_string, router_id)\n"
          "	self.send_command(\"fix this\")\n\n"
          "def remove_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n"
          "	type = \"" + t + "\"\n"
          "    routername = self.__get_lldp_router_name(port_string, router_id)\n"
          "	self.send_command(\"fix this\")\n\n"
          "def start_tlv_" + fname + "(self, port_string, router_id):\n"
          "	type = \"" + t + "\"\n"
          "    routername = self.__get_lldp_router_name(port_string, router_id)\n"
          "	self.send_command(routername + \" txTlv -tlv \" + type)\n\n"
          "def stop_tlv_" + fname + "(self, port_string, router_id):\n"
          "	type = \"" + t + "\"\n"
          "    routername = self.__get_lldp_router_name(port_string, router_id)\n"
          "	self.send_command(routername + \" stopTxTlv -tlv \" + type)\n")

print("#####" * 35)
print("#####" * 35)
print("#####" * 35)
print("#####" * 35)
print("\n\n")
for t in types:
    fname = t.replace("-", "_")
    print("####" * 10)
    print("######## " + str(t) + " ############")
    print("####" * 10)
    print("@abc.abstractmethod\ndef add_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef remove_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef start_tlv_" + fname + "(self, port_string, router_id):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef stop_tlv_" + fname + "(self, port_string, router_id):\n"
          "	return self.logger.log_unimplemented_method()\n")
    print("def send_lldp_tlv_" + fname + "(self, port_string, router_id):\n"
          "    self.start_tlv_" + fname + "(port_string, router_id)\n"
          "    time.sleep(self.send_sleep_time)\n"
          "    self.stop_tlv_" + fname + "(port_string, router_id)\n")

print("#####" * 35)
print("#####" * 35)
print("#####" * 35)
print("#####" * 35)
print("\n\n")
for t in types:
    fname = t.replace("-", "_")
    print("####" * 10)
    print("######## " + str(t) + " ############")
    print("####" * 10)
    print("@abc.abstractmethod\ndef add_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef remove_lldp_tlv_" + fname + "(self, port_string, router_id, value):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef start_tlv_" + fname + "(self, port_string, router_id):\n"
          "	return self.logger.log_unimplemented_method()\n\n"
          "@abc.abstractmethod\ndef stop_tlv_" + fname + "(self, port_string, router_id):\n"
          "	return self.logger.log_unimplemented_method()\n")
