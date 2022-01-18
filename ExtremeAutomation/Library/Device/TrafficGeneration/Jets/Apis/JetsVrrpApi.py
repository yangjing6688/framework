from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingVrrpApi import NetworkEmulatingVrrpApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsVrrpApi(NetworkEmulatingVrrpApi):
    def __init__(self, device):
        super(JetsVrrpApi, self).__init__(device)

    def create_vrrp_interface(self, port_string, router_id, source_ip, netmask, gateway_address, mac_address,
                              vlan_id=None, priority=200, advertise_interval_msecs=1000, version=2):
        # router create simVrrpRtr vrrp -device 1 -ipaddr 16.1.1.1 -advIntInMsecs 1000 -version 33
        # tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01
        #   -state enable
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_vrrp_router_name(port_string, router_id)
            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + source_ip + \
                " -netmask " + netmask + " -gateway " + gateway_address + " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)

            if int(version) == 2:
                version = 0x21
            elif int(version) == 3:
                version = 0x31

            config_isis_ext_ip_reach = " -device " + str(prt_id) + \
                                       " -ipaddr " + str(source_ip) + \
                                       " -advIntInMsecs " + str(advertise_interval_msecs) + \
                                       " -version " + str(version) + \
                                       " -priority 255 "
            self.send_command("router create " + routername + " vrrp " + config_isis_ext_ip_reach)
            self.send_command(routername + " log start update ")
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def remove_vrrp_router(self, port_string, router_id, route_address):
        # simVrrpRtr deleteRouter  -device 1 -ipaddr 16.1.1.1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_vrrp_router_name(port_string, router_id)
            self.send_command(routername + " deleteRouter  -device " + str(prt_id) + " -ipaddr " + str(route_address))
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def add_vrf(self, port_string, router_id, vrf_id, backup_address, priority=150):
        # simVrrpRtr addVrf -vrfId 1 -bkupAddr 16.1.1.106 -priority 150

        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_vrrp_router_name(port_string, router_id)
            val = "-device " + str(prt_id) + \
                  " -vrfId " + str(vrf_id) + \
                  " -bkupAddr " + str(backup_address) + \
                  " -priority " + str(priority)
            self.send_command(routername + " addVrf " + val)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def enable_vrf(self, port_string, router_id, vrf_id, enabled=True):
        # simVrrpRtr enableVrf -vrfId 1
        # simVrrpRtr disableVrf -vrfId 1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_vrrp_router_name(port_string, router_id)
            val = "-device " + str(prt_id) + \
                  " -vrfId " + str(vrf_id)
            if enabled:
                self.send_command(routername + " enableVrf " + val)
            else:
                self.send_command(routername + " disableVrf " + val)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def remove_vrf(self, port_string, router_id, vrf_id):
        # simVrrpRtr removeVrf -vrfId 1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            routername = self.__get_vrrp_router_name(port_string, router_id)
            val = "-device " + str(prt_id) + \
                  " -vrfId " + str(vrf_id)
            self.send_command(routername + " removeVrf " + val)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def __get_vrrp_router_name(self, port_string, router_id):
        return ("simVrrp_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
