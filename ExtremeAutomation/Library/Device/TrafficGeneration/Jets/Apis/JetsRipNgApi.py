from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingRipNgApi import NetworkEmulatingRipNgApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsRipNgApi(NetworkEmulatingRipNgApi):
    def __init__(self, device):
        super(JetsRipNgApi, self).__init__(device)

    def create_ripng_interface(self, port_string, router_id_and_source_ip, prefix_length, mac_address, vlan_id=None,
                               mode="R1", refresh_time=30):
        # JETS_SIM>tcpip config -device 1 -ipAddr 1016::1 -prefixLen 64 -macAddress 0.0.10.16.00.01 -state enable
        # JETS_SIM>router create simRipRtr1 rip -device 1 -ipaddr 1016::1 -mode R1 -refreshtime 30
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id_and_source_ip)
            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + router_id_and_source_ip + \
                " -prefixLen " + str(prefix_length) + " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)
            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -ipaddr " + str(router_id_and_source_ip) + \
                                       " -mode " + str(mode) + \
                                       " -refreshtime " + str(refresh_time)
            self.send_command("router create " + routername + " rip " + config_isis_ext_ip_reach)
            # self.send_command(routername + " log start update ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def add_ripng_route(self, port_string, router_id, first_ip, next_hop=None, prefix_length=64, metric=1, num_routes=1,
                        step=1):

        # JETS_SIM>simRipRtr1 add -routes {{-ipAddr 0:0:0:0:0:0:0:0 -prefixLen 0 -numAddr 1 -step 1 -metric 1
        #   -nexthop 0:0:0:0:0:0:0:0 }}
        # JETS_SIM>simRipRtr1 add -routes {{-ipAddr 3010:1::0 -prefixLen 64 -numAddr 1 -step 1 -metric 1 }}

        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id)
            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -nexthop " + str(next_hop) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -prefixLen " + str(prefix_length) + \
                                       " -step " + str(step) + \
                                       " -metric " + str(metric)
            if next_hop:
                " -nexthop " + str(next_hop)
            self.send_command(routername + " add -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def delete_ripng_route(self, port_string, router_id, first_ip, next_hop="0:0:0:0:0:0:0:0", prefix_length=64,
                           num_routes=1, step=1):
        # JETS_SIM>simRipRtr1 remove -routes {{-ipAddr 0:0:0:0:0:0:0:0 -prefixLen 0 -numAddr 1 -step 1 }}
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id)
            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -step " + str(step)
            self.send_command(routername + " remove -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def remove_ripng_router(self, port_string, router_id_and_source_ip):
        # JETS_SIM>simRipRtr destroy
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_rip_router_name(port_string, router_id_and_source_ip)
            self.send_command(routername + " deleteRouter  -device " + str(prt_id) + " -ipaddr " +
                              str(router_id_and_source_ip))
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def ripng_config(self, port_string, tx_delay):
        # JETS_SIM>rip config -device 1 -txdelay 100
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)

            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -txdelay " + str(tx_delay)
            self.send_command("rip config " + config_isis_ext_ip_reach)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def get_ripng_stats(self, port_string, router_id):
        # JETS_SIM>simRipRtr stats
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_rip_router_name(port_string, router_id)
        self.send_command(routername + " stats ")

    def __get_rip_router_name(self, port_string, router_id):
        return ("simRip_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
