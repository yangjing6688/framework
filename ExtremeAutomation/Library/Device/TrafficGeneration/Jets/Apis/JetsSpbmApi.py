from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingSpbmApi import NetworkEmulatingSpbmApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from collections import OrderedDict


class JetsSpbmApi(NetworkEmulatingSpbmApi):
    """
    init function
    bridge create_core_plsb_interface -bridgeName edgeA -intf 1 -macAddr 00:00:00:0c:0a:01 -vlan 4051 -svlan 4052
        -area c02000000000 -sysId 00:00:00:0e:0a:0f -pnodeId 3 -plsbInstance 1 -cost 10 -mode 802.1aq -dvrMode NONE
    bridge setIsisGlobals -helloInterval 9 -isisMultiplier 3 -retransLspInterval 5
    bridge enableAll

    """

    def __init__(self, device):
        super(JetsSpbmApi, self).__init__(device)

    # eth2, 'edgeA', "00:00:00:0c:0a:01", 4051, 4502, "c02000000000", "00:00:00:0e:0a:0f", 10, 3, 1, 10
    def create_isis_interface(self, port_string, bridge_name, mac_addr, vlan_id, svlan_id, area, sys_id,
                              pnode_id, spb_instance, cost, options=None):
        self.logger.log_debug("create_isis_interface(" + port_string + ")")
        try:
            if not options:
                options = {}
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            order_dict = OrderedDict()
            # bridge create_core_plsb_interface -bridgeName edgeA -intf 1 -macAddr 00:00:00:0c:0a:01 -vlan 4051
            #   -svlan 4052 -area c02000000000 -sysId 00:00:00:0e:0a:0f -pnodeId 3 -plsbInstance 1 -cost 10
            #   -mode 802.1aq -dvrMode NONE
            order_dict["bridgeName"] = bridge_name
            order_dict["intf"] = str(prt_id)
            order_dict["macAddr"] = str(mac_addr)
            order_dict["vlan"] = str(vlan_id)
            order_dict["svlan"] = str(svlan_id)
            order_dict["area"] = str(area)
            order_dict["sysId"] = str(sys_id)
            order_dict["pnodeId"] = str(pnode_id)
            order_dict["plsbInstance"] = str(spb_instance)
            order_dict["cost"] = str(cost)
            order_dict["mode"] = "802.1aq"
            order_dict["dvrMode"] = "NONE"

            for key in options:
                order_dict[key] = options[key]

            if options and 'dvrMode' in options:
                order_dict["dvrMode"] = str(options['dvrMode'])
            create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())

            self.send_command("bridge createCorePlsbInterface " + create_core_plsb_interface)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def set_isis_globals(self, hello_interval=9, isi_multiplier=3, retrans_lsp_interval=5, options=None):
        self.logger.log_debug("create_isis_interface()")
        try:
            dev = self.get_device()
            set_isis_globals = " -helloInterval " + str(hello_interval) + \
                               " -isisMultiplier " + str(isi_multiplier) + \
                               " -retransLspInterval " + str(retrans_lsp_interval)
            self.send_command("bridge setIsisGlobals " + set_isis_globals)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def set_bridge_enabled(self, enable=True):
        self.logger.log_debug("enable_bridge()")
        try:
            dev = self.get_device()
            if enable:
                self.send_command("bridge enableAll ")
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def set_multicast_enabled(self, enable=True):
        self.logger.log_debug("enable_bridge()")
        try:
            dev = self.get_device()
            if enable:
                self.send_command("bridge setSpbmAttributes -spbMc " + str(enable).lower())
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def create_isis_ipv4_route_stack(self, port_string, bridge_name, create_stack, starting_ip, netmask, gateway_ip,
                                     num_routes, cost, step, options=None):
        """
        bridge configIsisExtIpReach -bridgeName edgeA -startingIp 10.10.10.1 -mask 255.255.255.0 -num_routes 1 -cost 1
            -step 1 -updown false
        Added 1 starting at network 10.10.10.0
        advetise_isis_ipv4_routes('eth1', 'edgeA', True, '1.1.1.13', '255.255.255.255', '10.10.10.1', '255.255.255.0',
            1, 1, 1)
        tcpip alias -device 1 -ipAddr 10.10.10.1 -netmask 255.255.255.0 -rtrStackIp 1.1.1.13
        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            if create_stack:
                config_str = dev.get_tcp_config_string(prt_id)
                tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + starting_ip + \
                    " -netmask " + netmask + " -rtrStackIp " + gateway_ip
                self.send_command("tcpip " + tcpip)

            config_isis_ext_ip_reach = " -bridgeName " + bridge_name + \
                                       " -startingIp " + starting_ip + \
                                       " -mask " + netmask + \
                                       " -num_routes " + str(num_routes) + \
                                       " -cost " + str(cost) + \
                                       " -step " + str(step) + \
                                       " -updown false"
            self.send_command("bridge configIsisExtIpReach " + config_isis_ext_ip_reach)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def create_isis_ipv6_route_stack(self, port_string, bridge_name, create_stack, shortcut_ip, starting_ip,
                                     prefix_length, num_routes, cost, step, l3isid, options=None):
        """
        bridge configIsisExtIpv6Reach -bridgeName edgeA -startingIp 1000:5309:: -preFixLen 64 -num_routes 2 -cost 1
            -step 1 -l3isid 0
        advetise_isis_ipv6_routes('eth1', 'edgeA', True, '::867:5309:867:5309', '1000:5309::', 64, 2, 1, 1, 0)

        :return:
        """
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            if create_stack:
                config_str = dev.get_tcp_config_string(prt_id)
                tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + starting_ip + \
                    " -prefixLen " + str(prefix_length) + " -rtrStackIp " + shortcut_ip
                self.send_command("tcpip " + tcpip)
            # this sets up a tcp stack
            config_isis_ext_ipv6_reach = " -bridgeName " + bridge_name + \
                                         " -startingIp " + starting_ip + \
                                         " -preFixLen " + str(prefix_length) + \
                                         " -num_routes " + str(num_routes) + \
                                         " -cost " + str(cost) + \
                                         " -step " + str(step) + \
                                         " -l3isid " + str(l3isid)
            self.send_command("bridge configIsisExtIpv6Reach " + config_isis_ext_ipv6_reach)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())
