from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingBgpApi import NetworkEmulatingBgpApi


class JetsBgpApi(NetworkEmulatingBgpApi):
    def __init__(self, device):
        super(JetsBgpApi, self).__init__(device)

    # def create_bgp_interface(self, port_string, router_id, area_id, source_ip, netmask, gateway_address, mac_address,
    #                           vlan_id=None, link_type="standard", area_type="extcapable", passive=False, prio="1",
    #                           cost="1", trans_delay="40", hello_int="10", dead_int="40", retrans_int="5",
    #                           wait_time="40"):

    def create_bgp_interface(self, port_string, router_id, local_as, source_ip, netmask, gateway_address, mac_address,
                             vlan_id=None, neighbor_type=None, ip_version="IPv4", options=None):
        # bgp config -device 1 -updateinterval 1000 -maxattributes 10000 -notifylogsize 256
        # tcpip config -device 1 -ipAddr 31.1.2.3 -netmask 255.255.255.0 -rtrStackIp 31.1.2.1
        # -macAddress 00:33:44:55:66:77
        # router create simBgpRtr bgp -device 1 -ipAddr 31.1.2.3 -IPversion IPv4 -ASN 4
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)
            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + source_ip + \
                " -netmask " + netmask + " -gateway " + gateway_address + \
                " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)
            self.configure_bgp_options(port_string)

            conf_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                     " -ipAddr " + str(source_ip) + \
                                     " -IPversion " + str(ip_version) + \
                                     " -ASN " + str(local_as)
            self.send_command("router create " + routername + " bgp " + conf_isis_ext_ip_reach)
            self.send_command(routername + " log start update ")
        except Exception as e:
            self.logger.log_debug(e)

    def configure_bgp_options(self, port_string, updateinterval=1000, maxattributes=1000, notifylogsize=256):
        # bgp config -device 1 -updateinterval 1000 -maxattributes 10000 -notifylogsize 256
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            self.send_command("bgp config -device " + str(prt_id) +
                              " -updateinterval " + str(updateinterval) +
                              " -maxattributes " + str(maxattributes) +
                              " -notifylogsize " + str(notifylogsize))
        except Exception as e:
            self.logger.log_debug(e)

    def add_bgp_neighbor(self, port_string, router_id, ip_address, netmask, local_as):
        # simBgpRtr neighbor create -ipAddr 66.1.0.6 -ASN 10
        # simBgpRtr neighbor create -ipAddr 67.1.0.6 -ASN 10 -netmask 255.255.255.0
        # simBgp_eth1_3_3_3_3  neighbor link -ipAddr 152.1.1.1 -state UP

        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)
            conf_isis_ext_ip_reach = " -ipAddr " + str(ip_address) + \
                                     " -ASN " + str(local_as) + \
                                     " -netmask " + str(netmask)
            self.send_command(routername + " neighbor create " + conf_isis_ext_ip_reach)
            self.send_command(routername + " neighbor link -ipAddr  " + str(ip_address) + " -state UP")
        except Exception as e:
            self.logger.log_debug(e)

    def configure_network_generator_bgp_routes_on_bgp_peer(self, bgp_interface_handle, prefix, netmask, num_routes,
                                                           origin_route_enable, origin, ip_version, options=None):
        return self.logger.log_unimplemented_method()

    def start_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def stop_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def restart_network_generator_bgp_emulation(self, port_string, options=None):
        return self.logger.log_unimplemented_method()

    def add_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1, origin="IGP", med=0,
                      localpref=0):
        """
        simBgpRtrLink1 add -routes {{  -ipAddr 188.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1 -origin IGP -med 0
                                       -localpref 0 }}
        :param port_string:
        :param router_id:
        :param first_ip:
        :param netmask:
        :param num_routes:
        :param step:
        :param origin: "IGP"
        :param med:
        :param localpref:

        :return:
        """
        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)

            # simbgpRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1
            # -type AS_EXTERNAL-cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0
            # -forwardAddr 0.0.0.0}}

            conf_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                     " -netmask " + str(netmask) + \
                                     " -numAddr " + str(num_routes) + \
                                     " -step " + str(step) + \
                                     " -origin " + str(origin) + \
                                     " -med " + str(med) + \
                                     " -localpref " + str(localpref)
            self.send_command(routername + " add -routes {{" + conf_isis_ext_ip_reach + "}}")
        except Exception as e:
            self.logger.log_debug(e)

    def delete_bgp_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        """
        simbgpRtrLink1 remove -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1}}
        :param port_string:
        :param router_id:
        :param first_ip:
        :param netmask:
        :param num_routes:
        :param step:
        :return:
        """
        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)

            # simbgpRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1
            # -type AS_EXTERNAL -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0
            # -forwardAddr 0.0.0.0}}

            conf_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                     " -netmask " + str(netmask) + \
                                     " -numAddr " + str(num_routes) + \
                                     " -step " + str(step)
            self.send_command(routername + " remove -routes {{" + conf_isis_ext_ip_reach + "}}")
        except Exception as e:
            self.logger.log_debug(e)

    def remove_bgp_router(self, port_string, router_id):
        """
        simbgpRtrLink1 destroy
        also, delete the tcp stacks
        :param port_string:
        :param router_id:
        :return:
        """
        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)
            # config_str = dev.get_tcp_config_string(prt_id)
            # tcpip = config_str + " -device " + str(prt_id) +" -ipAddr " + source_ip +\
            #         " -netmask "+netmask+" -rtrStackIp " + gateway_address +\
            #         " -macAddress " + mac_address
            # if vlan_id:
            #     tcpip += " -vlanId " + str(vlan_id)
            # tcpip += "  -state enable "
            # self.send_command("tcpip " + tcpip )

            self.send_command(routername + " destroy ")
        except Exception as e:
            self.logger.log_debug(e)

    def set_bgp_router_enabled(self, port_string, router_id, enable=True):
        """
        simbgpRtrLink1 enable/disable
        :param port_string:
        :param router_id:
        :param enable:
        :return:
        """
        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)
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
        except Exception as e:
            self.logger.log_debug(e)

    def delete_bpg_route(self, port_string, router_id, first_ip, netmask, num_routes, step=1):
        """
        simbgpRtrLink1 remove -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1}}
        :param port_string:
        :param router_id:
        :param first_ip:
        :param netmask:
        :param num_routes:
        :param step:
        :return:
        """
        try:
            # dev = self.get_device()
            # prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_bgp_router_name(port_string, router_id)

            # simbgpRtrLink1 add -routes {{-ipAddr 177.0.10.0 -netmask 255.255.255.0 -numAddr 5 -step 1
            # -type AS_EXTERNAL -cost 1 -costtype type1_external -exroutetag 1 -flooddelay 100 -advrtr 0.0.0.0
            # -forwardAddr 0.0.0.0}}

            conf_isis_ext_ip_reach = " -ipAddr " + str(first_ip) + \
                                     " -netmask " + str(netmask) + \
                                     " -numAddr " + str(num_routes) + \
                                     " -step " + str(step)
            self.send_command(routername + " remove -routes {{" + conf_isis_ext_ip_reach + "}}")
        except Exception as e:
            self.logger.log_debug(e)

    def get_bgp_state(self, port_string, router_id):
        """
        simBgpRtr getlist
        :param port_string:
        :param router_id:
        :return:
        """
        # dev = self.get_device()
        # prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_bgp_router_name(port_string, router_id)
        self.send_command(routername + " getlist ")

    def get_bgp_stats(self, port_string, router_id):
        """
        simbgpRtr stats
        :param port_string:
        :param router_id:
        :return:
        """
        # dev = self.get_device()
        # prt_id = dev.get_port_index_from_group_string(port_string)
        routername = self.__get_bgp_router_name(port_string, router_id)
        self.send_command(routername + " stats ")

    @staticmethod
    def __get_bgp_router_name(port_string, router_id):
        return ("simBgp_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
