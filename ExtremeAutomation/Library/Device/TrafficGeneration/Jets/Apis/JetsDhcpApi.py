from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingDhcpApi import NetworkEmulatingDhcpApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from collections import OrderedDict
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress


class JetsDhcpApi(NetworkEmulatingDhcpApi):
    # These need to be implemented.
    # addDhcpOption
    # {
    # return \[eval \"jmeshost addDhcpOption -hostName $name \[lrange \$args 1 end\]\"\]
    # }
    # deleteDhcpOption
    # {
    # return \[eval \"jmeshost deleteDhcpOption -hostName $name \[lrange \$args 1 end\]\"\]
    # }
    # setDhcpHWAddress
    # {
    # return \[eval \"jmeshost setDhcpHWAddress -hostName $name \[lrange \$args 1 end\]\"\]
    # }

    def __init__(self, device):
        super(JetsDhcpApi, self).__init__(device)

    def create_dhcp_client(self, port_string, mac_address, network_mask, vlan=-1, count=1, step=1):
        self.logger.log_debug("create_dhcp_client(" + port_string + ")")
        # meshost create dhcp_hostL3_GblRtr -type DHCP -macAddr 00:01:02:03:04:05 -intf 3 -mask 255.0.0.0
        # dhcp_hostL3_GblRtr enable -ignoreDhcpGwOption false
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            # mac = mac_address

            index = 0
            while index < count:
                mac = EnetAddress.add_to_address(EnetAddress(mac_address), index * step)
                name = self.__get_dhcp_client_name(port_string, mac)
                order_dict = OrderedDict()
                # bridge createCorePlsbInterface -bridgeName edgeA -intf 1 -macAddr 00:00:00:0c:0a:01 -vlan 4051
                # -svlan 4052 -area c02000000000 -sysId 00:00:00:0e:0a:0f -pnodeId 3 -plsbInstance 1 -cost 10
                # -mode 802.1aq -dvrMode NONE
                order_dict["type"] = "DHCP"
                order_dict["intf"] = str(prt_id)
                order_dict["macAddr"] = str(mac)
                order_dict["mask"] = str(network_mask)
                if vlan >= 0:
                    order_dict["vlan"] = str(vlan)

                create_core_plsb_interface = " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())

                self.send_command("meshost create " + str(name) + " " + create_core_plsb_interface)
                self.send_command(str(name) + "  enable -ignoreDhcpGwOption false")
                index += 1
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def remove_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1):
        try:
            index = 0
            while index < count:
                mac = EnetAddress.add_to_address(EnetAddress(mac_address), index * step)
                name = self.__get_dhcp_client_name(port_string, mac)
                self.send_command(str(name) + " disable")
                index += 1
        except Exception as e:
            self.logger.log_debug(StringUtils.exception_to_string())

    def start_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1):
        try:
            index = 0
            while index < count:
                mac = EnetAddress.add_to_address(EnetAddress(mac_address), index * step)
                name = self.__get_dhcp_client_name(port_string, mac)
                self.send_command(str(name) + " getIpAddress")
                index += 1
        except Exception as e:
            self.logger.log_debug(StringUtils.exception_to_string())

    def get_dhcp_client_address(self, port_string, mac_address):
        try:
            mac = mac_address
            name = self.__get_dhcp_client_name(port_string, mac)
            obj = self.send_command_no_parse(str(name) + " getIpAddress")
            return (obj.return_text.split("has IP ADDRESS")[1].strip())[:-1].strip()
        except Exception as e:
            self.logger.log_debug(StringUtils.exception_to_string())
        return "No IP"

    def ping_dhcp_client(self, port_string, mac_address, network_mask, destination_ip):
        try:
            mac = mac_address
            name = self.__get_dhcp_client_name(port_string, mac)
            obj = self.send_command_no_parse(str(name) + " ping -ipAddr " + str(destination_ip))
        #     check obj.return_text
        except Exception as e:
            self.logger.log_debug(StringUtils.exception_to_string())

    def __get_dhcp_client_name(self, port_string, router_id):
        router_id = str(router_id).lower()
        return ("simDhcp_" + str(port_string) + "_" +
                str(router_id)).replace(" ", "_").replace(".", "_").replace(":", "_")
