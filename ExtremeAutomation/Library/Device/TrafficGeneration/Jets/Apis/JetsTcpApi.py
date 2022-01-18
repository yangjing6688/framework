from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpApi
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from collections import OrderedDict


class JetsTcpApi(NetworkEmulatingTcpApi):
    def __init__(self, device):
        super(JetsTcpApi, self).__init__(device)

    def create_tcp_stack(self, port_string, source_ip, netmask=None, gateway_address=None, mac_address=None,
                         vlan_id=None):
        # tcpip config -device 1 -ipAddr 31.1.2.3 -netmask 255.255.255.0 -rtrStackIp 31.1.2.1
        #   -macAddress 00:33:44:55:66:77
        try:
            dev = self.get_device()
            order_dict = OrderedDict()
            prt_id = dev.get_port_index_from_group_string(port_string)
            config_str = dev.get_tcp_config_string(prt_id)
            order_dict["device"] = str(prt_id)
            order_dict["ipAddr"] = str(source_ip)
            if netmask:
                order_dict["netmask"] = str(netmask)
            # else:
            #     order_dict["netmask"] = str("255.255.255.0")
            if gateway_address:
                order_dict["gateway"] = str(gateway_address)
            # else:
            #     parts = source_ip.split(".")
            #     parts[-1] = "1"
            #     order_dict["gateway"] = ".".join(parts)
            if mac_address:
                order_dict["macAddress"] = str(mac_address)
            else:
                addr = Ipv4Address.to_long(source_ip)
                addr = EnetAddress(addr).to_string()
                order_dict["macAddress"] = addr
            if vlan_id:
                order_dict["vlanId"] = str(vlan_id)
            tcpip = config_str + " "
            tcpip += " ".join('-{} {}'.format(key, value) for key, value in order_dict.items())
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def delete_tcp_stack(self, port_string, source_ip):
        # tcpip terminateOneStack -device 1 -ipAddr 1.2.3.4
        try:
            dev = self.get_device()
            order_dict = OrderedDict()
            prt_id = dev.get_port_index_from_group_string(port_string)
            reply = self.send_command("tcpip terminateOneStack -device " + str(prt_id) + " -ipAddr " + source_ip)
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())
