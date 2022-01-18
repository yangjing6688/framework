from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpApi
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils


class IxiaTcpApi(NetworkEmulatingTcpApi):
    def __init__(self, device):
        super(IxiaTcpApi, self).__init__(device)

    def create_tcp_stack(self, port_string, source_ip, netmask=None, gateway_address=None, mac_address=None,
                         vlan_id=None):
        try:
            og_port_string = port_string
            port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
            port_handle = TrafficGenerationUtils.convert_port_string_to_port_handle(og_port_string)
            temp_parts = port_handle.split("/")
            temp_parts = temp_parts[1::]
            port_description = ":0".join(temp_parts)
            # Enable ARP Protocol
            self.send_command("protocolServer setDefault")
            self.send_command("protocolServer config -enableArpResponse true")
            self.send_command("protocolServer set " + port_string)

            self.send_command("interfaceTable   select            " + port_string)
            self.send_command("interfaceTable   clearAllInterfaces ")
            self.send_command("interfaceEntry   clearAllItems     addressTypeIpV6")
            self.send_command("interfaceEntry   clearAllItems     addressTypeIpV4")

            self.send_command("interfaceIpV4    setDefault        ")
            if gateway_address:
                self.send_command("interfaceIpV4    config         -gatewayIpAddress   " + str(gateway_address))
            else:
                ip = source_ip.split(".")[:-1]
                gateway_address = ".".join(ip) + ".1"
                self.send_command("interfaceIpV4    config         -gatewayIpAddress   " + str(gateway_address))
            if netmask:
                if netmask == "255.255.255.0":
                    netmask = "24"
                elif netmask == "255.255.0.0":
                    netmask = "16"
                elif netmask == "255.0.0.0":
                    netmask = "8"
                else:
                    netmask = "32"
            else:
                netmask = "24"
            self.send_command("interfaceIpV4    config         -maskWidth       " + str(netmask))
            self.send_command("interfaceIpV4    config         -ipAddress       " + str(source_ip))
            self.send_command("interfaceEntry addItem addressTypeIpV4")

            self.send_command("interfaceEntry   setDefault        ")
            self.send_command("interfaceEntry   config         -enable          true")
            self.send_command("interfaceEntry   config         -description     \"" + port_description + "\"")
            if not mac_address:
                addr = Ipv4Address.to_long(source_ip)
                addr = EnetAddress(addr).to_string()
                mac_address = addr
            self.send_command("interfaceEntry   config         -macAddress      {" +
                              mac_address.replace(":", " ") + "}")
            self.send_command("interfaceTable   addInterface  interfaceTypeConnected")
            self.send_command("set portList [list [list " + port_string + "]]")
            self.send_command("ixWriteConfigToHardware portList ")
        except Exception:
            self.logger.log_debug(StringUtils.exception_to_string())

    def delete_tcp_stack(self, port_string, source_ip):
        return self.logger.log_unimplemented_method()
