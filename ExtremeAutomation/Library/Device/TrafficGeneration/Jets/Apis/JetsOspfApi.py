from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingOspfApi import NetworkEmulatingOspfApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsOspfApi(NetworkEmulatingOspfApi):
    def __init__(self, device):
        super(JetsOspfApi, self).__init__(device)

    def create_ospf_interface(self, port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, link_type="standard", area_type="extcapable", passive=False, prio="1",
                              cost="1", trans_delay="40", hello_int="10", dead_int="40", retrans_int="5",
                              wait_time="40"):
        """
        tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01
            -state enable
        router create simOspfRtr ospf -device 1 -routerID 3.3.3.3 -areaID 0.0.0.0 -helloInterval 10 -deadInterval 40
            -retransmittal 47 -cost 1 -priority 1 -intftype standard -learn true -areatype extcapable
        simOspfRtr log start update
        :param port_string:
        :param router_id:
        :param area_id:
        :param source_ip:
        :param netmask:
        :param gateway_address:
        :param mac_address:
        :param vlan_id:
        :param link_type:
        :param area_type:
        :param passive:
        :param prio:
        :param cost:
        :param trans_delay:
        :param hello_int:
        :param dead_int:
        :param retrans_int:
        :param wait_time:
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)
            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + source_ip + \
                " -netmask " + netmask + " -rtrStackIp " + gateway_address +\
                " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)

            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -routerID " + str(router_id) + \
                                       " -areaID " + str(area_id) + \
                                       " -helloInterval " + str(hello_int) + \
                                       " -deadInterval " + str(dead_int) + \
                                       " -retransmittal " + str(retrans_int) + \
                                       " -cost " + str(cost) + \
                                       " -priority " + str(prio) + \
                                       " -intftype " + str(link_type) + \
                                       " -areatype " + str(area_type) + \
                                       " -learn true "
            self.send_command("router create " + routername + " ospf " + config_isis_ext_ip_reach)
            self.send_command(routername + " log start update ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def add_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step, age, ls_type="AS_EXTERNAL",
                       adv_rtr="0.0.0.0", forward_address="0.0.0.0", cost=1, costype="type1_external", ex_route_tag=1):
        """
        simOspfRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1 -type AS_EXTERNAL
            -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0 -forwardAddr 0.0.0.0}}
        :param port_string:
        :param router_id:
        :param first_ip:
        :param netmask:
        :param num_routes:
        :param step:
        :param age:
        :param ls_type:
        :param adv_rtr:
        :param forward_address:
        :param cost:
        :param costype:
        :param ex_route_tag:
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)

            # simOspfRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1
            #   -type AS_EXTERNAL -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0
            #   -forwardAddr 0.0.0.0}}

            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -netmask " + str(netmask) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -step " + str(step) + \
                                       " -type " + str(ls_type) + \
                                       " -cost " + str(cost) + \
                                       " -costtype " + str(ls_type) + \
                                       " -exroutetag " + str(ex_route_tag) + \
                                       " -flooddelay " + str(age) + \
                                       " -advrtr " + str(adv_rtr) + \
                                       " -forwardAddr " + str(forward_address)
            self.send_command(routername + " add -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def delete_ospf_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        """
        simOspfRtrLink1 remove -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1}}
        :param port_string:
        :param router_id:
        :param first_ip:
        :param netmask:
        :param num_routes:
        :param step:
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)

            # simOspfRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1
            #   -type AS_EXTERNAL -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0
            #   -forwardAddr 0.0.0.0}}

            config_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                       " -netmask " + str(netmask) + \
                                       " -numAddr " + str(num_routes) + \
                                       " -step " + str(step)
            self.send_command(routername + " remove -routes {{" + config_isis_ext_ip_reach + "}}")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def remove_ospf_router(self, port_string, router_id):
        """
        simOspfRtrLink1 destroy
        also, delete the tcp stacks
        :param port_string:
        :param router_id:
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)
            # config_str = dev.get_tcp_config_string(prt_id)
            # tcpip = config_str + " -device " + str(prt_id) +" -ipAddr " + source_ip +\
            #         " -netmask "+netmask+" -rtrStackIp " + gateway_address +\
            #         " -macAddress " + mac_address
            # if vlan_id:
            #     tcpip += " -vlanId " + str(vlan_id)
            # tcpip += "  -state enable "
            # self.send_command("tcpip " + tcpip )

            self.send_command(routername + " destroy ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def set_ospf_router_enabled(self, port_string, router_id, enable=True):
        """
        simOspfRtrLink1 enable/disable
        :param port_string:
        :param router_id:
        :param enable:
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)
            # config_str = dev.get_tcp_config_string(prt_id)
            # tcpip = config_str + " -device " + str(prt_id) +" -ipAddr " + source_ip +\
            #         " -netmask "+netmask+" -rtrStackIp " + gateway_address +\
            #         " -macAddress " + mac_address
            # if vlan_id:
            #     tcpip += " -vlanId " + str(vlan_id)
            # tcpip += "  -state enable "
            # self.send_command("tcpip " + tcpip )
            if not enable:
                self.send_command(routername + " disable ")
            else:
                self.send_command(routername + " enable ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def get_ospf_state(self, port_string, router_id):
        """
        simOspfRtr getlist
        :param port_string:
        :param router_id:
        :return:
        """
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_ospf_router_name(port_string, router_id)
        self.send_command(routername + " getlist ")

    def add_ospf_lsas(self, port_string, router_id, lsa, receive_router):
        """
        simOspfRtr addLsas
        ospf.createRouterLsa(NAME("simOspfRtr1"), LINK_STATE_ID("1.1.1.3"), ADV_ROUTER("0.0.0.66"),IP_VERSION("IPv6"),
            LINK(LINK_TYPE("virtuallink"),METRIC(3)), LINK(LINK_ID("1.1.1.2"),METRIC(5)))
        :param port_string:
        :param router_id:
        :param lsa:
        :param receive_router:
        :return:
        """
        pass

    def get_ospf_stats(self, port_string, router_id):
        """
        simOspfRtr stats
        :param port_string:
        :param router_id:
        :return:
        """
        dev = self.get_device()
        prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_ospf_router_name(port_string, router_id)
        self.send_command(routername + " stats ")

    def add_network(self, port_string, router_id, ip_address, designated_router_address, netmask, attached_router_id,
                    attached_router_ip):
        """
        ospf.addNetwork (NAME ("simOspfL3"), IP_ADDRESS ("12.1.1.2"), DR ("12.1.1.2"), NETMASK ("255.255.255.0"),
            ATTACHED_RTR_ID ("1.1.1.1"), ATTACHED_RTR_IP ("12.1.1.1"));
        :param port_string:
        :param router_id:
        :param ip_address:
        :param designated_router_address:
        :param netmask:
        :param attached_router_id:
        :param attached_router_ip:
        :return:
        """
        pass

    def remove_network(self, port_string, router_id, ip_address, designated_router_address, netmask,
                       attached_router_id, attached_router_ip):
        """
        ospf.removeNetwork (NAME ("simOspfL3"), IP_ADDRESS ("12.1.1.2"), DR ("12.1.1.2"), NETMASK ("255.255.255.0"),
            ATTACHED_RTR_ID ("1.1.1.1"), ATTACHED_RTR_IP ("12.1.1.1"))
        :param port_string:
        :param router_id:
        :param ip_address:
        :param designated_router_address:
        :param netmask:
        :param attached_router_id:
        :param attached_router_ip:
        :return:
        """
        pass

    def add_stub_network(self, port_string, router_id, ip_address, netmask):
        """
        ospf.addStubNetwork (NAME ("simOspfL3"), IP_ADDRESS ("12.1.1.2"), NETMASK ("255.255.255.0"));
        :param port_string:
        :param router_id:
        :param ip_address:
        :param netmask:
        :return:
        """
        pass

    def remove_stub_network(self, port_string, router_id, ip_address, netmask):
        """
        ospf.removeStubNetwork (NAME ("simOspfL3"), IP_ADDRESS ("12.1.1.2"), NETMASK ("255.255.255.0"));
        :param port_string:
        :param router_id:
        :param ip_address:
        :param netmask:
        :return:
        """
        pass

    def generate_ospf_routes(self, port_string, router_id):
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_ospf_router_name(port_string, router_id)
            self.send_command(str(routername) + " generateRoutes")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def __get_ospf_router_name(self, port_string, router_id):
        return ("simOspf_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
