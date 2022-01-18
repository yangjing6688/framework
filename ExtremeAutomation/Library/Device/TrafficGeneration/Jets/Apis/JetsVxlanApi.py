from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingVxlanApi import NetworkEmulatingVxlanApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsVxlanApi(NetworkEmulatingVxlanApi):
    def __init__(self, device):
        super(JetsVxlanApi, self).__init__(device)

    # set vlan_id to 0 or None for untagged
    def create_vxlan_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address,
                               vlan_id):
        # vxlan_api.create_vxlan_interface(bridge_a_port, router_handle, "255.255.255.255", "10.59.4.1",
        #   "00:00:fa:fa:16:01", 603)
        # meshost create mltRtrEndpt1 -type MLT -macAddr 00:00:13:01:01:02 -ipAddr 13.1.1.2 -vlanId 133
        #   -defGateway 13.1.1.1 -mask 255.255.255.0 -group testCtrl-IpStacks
        # INFO: Created MLT host mltRtrEndpt1
        # multilink trunk
        # DEBUG: Host mltRtrEndpt1 defaultRoute was set to 13.1.1.1
        # mltRtrEndpt1 addCircuits -intfs " 3"
        # mltRtrEndpt1 enable -ignoreDhcpGwOption false
        # mltRtrEndpt1 setOutCircuit -intf 3
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_vxlan_router_name(port_string, router_id_and_source_ip)
        try:
            config_isis_ext_ip_reach = " -macAddr " + str(mac_address) + \
                                       " -ipAddr " + str(router_id_and_source_ip) + \
                                       " -vlanId " + str(vlan_id) + \
                                       " -defGateway " + str(gateway_address) + \
                                       " -mask " + str(netmask) + \
                                       " -group testCtrl-" + str(routername)
            if vlan_id and int(vlan_id) > 0:
                config_isis_ext_ip_reach += " -vlanid " + str(vlan_id)
            self.send_command("meshost create " + str(routername) + "  -type MLT " + config_isis_ext_ip_reach)
            self.send_command(str(routername) + " addCircuits -intfs \" " + str(prt_id) + "\"")
            self.send_command(str(routername) + " enable -ignoreDhcpGwOption false")
            self.send_command(str(routername) + " setOutCircuit -intf " + str(prt_id))
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    # set vlan_id to 0 or None for untagged
    def add_vxlan_host(self, port_string, router_id, inner_source_ip, netmask, mac_address, vlan_id, vxlan_vlan_id,
                       vxlan_src_ip, vxlan_dest_ip):
        # 1
        # tcpip alias -device 3 -ipAddr 11.11.11.11 -netmask 255.255.255.255 -rtrStackIp 13.1.1.2
        # Created stack behind router mltRtrEndpt1-13.1.1.2:ETH1
        #
        # tcpip alias -device 3 -ipAddr 10.10.10.21 -netmask 255.255.255.0 -rtrStackIp 11.11.11.11 -vnid 100
        #   -vtepdest 9.9.9.9 -macAddress 00:00:10:10:10:21 -group testCtrl-IpStacks
        # Enet registered under VXLAN : CircuitEnet:VXLANTUNNEL:100_11.11.11.11_9.9.9.9 mtu=1522
        # Created stack behind router IpStack:CircuitEnet:ETH0 mtu=1950:Ip:11.11.11.11
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_vxlan_router_name(port_string, router_id)
        try:
            random_ip = (str(254 - int(prt_id)) + "." + str(254 - int(prt_id)) + "." + str(254 - int(prt_id)) + "." +
                         str(prt_id))
            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -ipAddr " + str(vxlan_src_ip) + \
                                       " -netmask " + str("255.255.255.255") + \
                                       " -rtrStackIp " + str(router_id)
            self.send_command("tcpip alias " + config_isis_ext_ip_reach)

            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -ipAddr " + str(inner_source_ip) + \
                                       " -netmask " + str(netmask) + \
                                       " -rtrStackIp " + str(vxlan_src_ip) + \
                                       " -vnid " + str(vxlan_vlan_id) + \
                                       " -vtepdest " + str(vxlan_dest_ip) + \
                                       " -macAddress " + str(mac_address) + \
                                       " -group testCtrl-" + str(routername)
            if vlan_id and int(vlan_id) > 0:
                config_isis_ext_ip_reach += " -vlanid " + str(vlan_id)
            self.send_command("tcpip alias " + config_isis_ext_ip_reach)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def __get_vxlan_router_name(self, port_string, router_id):
        return ("simVxlan_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
