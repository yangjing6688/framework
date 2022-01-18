from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingRouteApi import NetworkEmulatingRouteApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsRouteApi(NetworkEmulatingRouteApi):
    """
    init function
    bridge createCorePlsbInterface -bridgeName edgeA -intf 1 -macAddr 00:00:00:0c:0a:01 -vlan 4051 -svlan 4052
        -area c02000000000 -sysId 00:00:00:0e:0a:0f -pnodeId 3 -plsbInstance 1 -cost 10 -mode 802.1aq -dvrMode NONE
    bridge setIsisGlobals -helloInterval 9 -isisMultiplier 3 -retransLspInterval 5
    bridge enableAll
    """

    def __init__(self, device):
        super(JetsRouteApi, self).__init__(device)

    def advetise_ipv4_routes(self, port_string, bridge_name, shortcut_ip, shortcut_netmask, options=None):
        """
        bridge enableIpShortcuts -intf 1 -bridgeName edgeA -ipAddr 1.1.1.13 -mask 255.255.255.255
        :return:
        """
        dev = self.get_device()
        if self.is_ipv4_shortcuts_enabled(port_string, bridge_name):
            self.logger.log_debug("Ipv4 Shortcut already enabled for " + str(port_string) + " sim " + str(bridge_name))
            return
        self.set_ipv4_shortcuts_enabled(port_string, bridge_name)
        try:
            prt_id = dev.get_port_index_from_group_string(port_string)

            enable_ip_shortcuts = " -intf " + str(prt_id) + \
                                  " -bridgeName " + bridge_name + \
                                  " -ipAddr " + shortcut_ip + \
                                  " -mask " + shortcut_netmask
            self.send_command("bridge enableIpShortcuts " + enable_ip_shortcuts)
            # this sets up a tcp stack
            dev.get_tcp_config_string(prt_id)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def enable_ipv4_shortcuts(self, port_string, bridge_name, shortcut_ip=None, shortcut_netmask='255.255.255.255'):
        if not shortcut_ip:
            prt_id = self.get_device().get_port_index_from_group_string(port_string)
            shortcut_ip = "1.1.1.1" + str(prt_id)
        self.advetise_ipv4_routes(port_string, bridge_name, shortcut_ip, shortcut_netmask)

    def advetise_ipv6_routes(self, port_string, bridge_name, shortcut_ip, options=None):
        """
        bridge enableIpv6Shortcuts -intf 1 -bridgeName edgeA -ipAddr ::867:5309:867:5309
        :return:
        """
        dev = self.get_device()
        if self.is_ipv6_shortcuts_enabled(port_string, bridge_name):
            self.logger.log_debug("Ipv6 Shortcut already enabled for " + str(port_string) + " sim " + str(bridge_name))
            return
        self.set_ipv6_shortcuts_enabled(port_string, bridge_name)
        try:
            prt_id = dev.get_port_index_from_group_string(port_string)
            enable_ipv6_shortcuts = " -intf  " + str(prt_id) + \
                                    " -bridgeName  " + bridge_name + \
                                    " -ipAddr  " + shortcut_ip
            self.send_command("bridge enableIpv6Shortcuts " + enable_ipv6_shortcuts)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def enable_ipv6_shortcuts(self, port_string, bridge_name, shortcut_ip=None):
        if not shortcut_ip:
            prt_id = self.get_device().get_port_index_from_group_string(port_string)
            shortcut_ip = "1000::" + str(prt_id)
        self.advetise_ipv6_routes(port_string, bridge_name, shortcut_ip)

    def get_routes(self, port_string, ip_address):

        dev = self.get_device()
        try:
            prt_id = dev.get_port_index_from_group_string(port_string)
            self.send_command("tcpip dumpRtm -device " + str(prt_id) + " -address " + str(ip_address))
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def get_all_routes_from_interface(self, port_string):
        dev = self.get_device()
        try:
            ip_address = dev.get_interface_base_address(port_string)
            prt_id = dev.get_port_index_from_group_string(port_string)
            self.send_command("tcpip dumpRtm -device " + str(prt_id) + " -address " + str(ip_address))
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())
