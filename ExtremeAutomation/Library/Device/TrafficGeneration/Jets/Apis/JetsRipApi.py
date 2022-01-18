from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingRipApi import NetworkEmulatingRipApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsRipApi(NetworkEmulatingRipApi):
    def __init__(self, device):
        super(JetsRipApi, self).__init__(device)

    def create_rip_interface(self, port_string, router_id_and_source_ip, netmask, gateway_address, mac_address, vlan_id,
                             mode="R1", refresh_time=30):
        # JETS_SIM>tcpip config -device 1 -ipAddr 66.1.0.1 -netmask 255.255.255.0 -gateway 66.1.0.6
        #   -macAddress 0.0.11.66.00.01 -vlanId 2 -userPriority 0 -CFI 0 -state enable
        # JETS_SIM>router create simRipRtr rip -device 1 -ipaddr 66.1.0.1 -mode R1 -refreshtime 30
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id_and_source_ip)
            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + router_id_and_source_ip + \
                " -netmask " + netmask + " -gateway " + gateway_address + \
                " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)
            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -ipaddr " + str(router_id_and_source_ip) + \
                                       " -mode " + str(mode) + \
                                       " -refreshtime " + str(refresh_time)
            self.send_command("router create " + routername + " rip " + config_isis_ext_ip_reach)
            self.send_command(routername + " log start update ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def add_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", next_hop="0.0.0.0", metric=1,
                      num_routes=1, step=1):
        # JETS_SIM>simRipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 - 1 -nexthop 0.0.0.0 }}
        # JETS_SIM>simVrf1RipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1
        #   -nexthop 0.0.0.0 }}
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id)
            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -netmask " + str(netmask) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -step " + str(step) + \
                                       " -metric " + str(metric) + \
                                       " -nexthop " + str(num_routes)
            self.send_command(routername + " add -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def delete_rip_route(self, port_string, router_id, first_ip, netmask="0.0.0.0", num_routes=1, step=1):
        # JETS_SIM>simVrf1RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}
        # JETS_SIM>simVrf255RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id)
            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -netmask " + str(netmask) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -step " + str(step)
            self.send_command(routername + " remove -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def remove_rip_router(self, port_string, router_id_and_source_ip):
        # JETS_SIM>simRipRtr destroy
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id_and_source_ip)
            self.send_command(routername + " deleteRouter  -device " + str(prt_id) + " -ipaddr " +
                              str(router_id_and_source_ip))
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def rip_config(self, port_string, tx_delay):
        # JETS_SIM>rip config -device 1 -txdelay 100
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)

            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -txdelay " + str(tx_delay)
            self.send_command("rip config " + config_isis_ext_ip_reach)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def get_rip_stats(self, port_string, router_id):
        # JETS_SIM>simRipRtr stats
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_rip_router_name(port_string, router_id)
        self.send_command(routername + " stats ")

    # JETS_SIM>tcpip config -device 1 -ipAddr 66.1.0.1 -netmask 255.255.255.0 -gateway 66.1.0.6
    #   -macAddress 0.0.11.66.00.01 -vlanId 2 -userPriority 0 -CFI 0 -state enable
    # JETS_SIM>tcpip alias -device 1 -ipAddr 66.1.0.2 -netmask 255.255.255.0 -gateway 66.1.0.6
    #   -macAddress 0.0.11.66.00.02 -vlanId 2 -userPriority 0 -CFI 0 -state enable
    # Completed Alias for IpStack:CircuitEnet:ETH5 mtu=1514:IpRtr:66.1.0.2
    # JETS_SIM>rip config -device 1 -txdelay 100
    # JETS_SIM>rip config -device 1
    # JETS_SIM>router create simRipRtr rip -device 1 -ipaddr 66.1.0.1 -mode R1 -refreshtime 30
    # JETS_SIM>rip config -device 1
    # JETS_SIM>router create simVrf1RipRtr rip -device 1 -ipaddr 66.1.1.1 -mode R1 -refreshtime 30
    # JETS_SIM>rip config -device 1
    # JETS_SIM>router create simVrf255RipRtr rip -device 1 -ipaddr 66.1.255.1 -mode R1 -refreshtime 30
    # JETS_SIM>simRipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1 -nexthop 0.0.0.0 }}
    # JETS_SIM>simVrf1RipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1
    #   -nexthop 0.0.0.0 }}
    # JETS_SIM>simVrf255RipRtr add -routes {{-ipAddr 0.0.0.0 -netmask 0.0.0.0 -numAddr 1 -step 1 -metric 1
    #   -nexthop 0.0.0.0 }}
    # JETS_SIM>simVrf1RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}
    # JETS_SIM>simVrf255RipRtr remove -routes {{-ipAddr 30.10.1.0 -netmask 255.255.255.0 -numAddr 1 -step 1 }}

    def __get_rip_router_name(self, port_string, router_id):
        return ("simRip_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
