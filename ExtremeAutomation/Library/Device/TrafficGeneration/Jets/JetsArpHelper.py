from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import IxRouteIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceArpHelper import \
    TrafficGeneratingDeviceArpHelper
from ExtremeAutomation.Library.Net.Address.EnetAddress import EnetAddress
from ExtremeAutomation.Library.Net.Address.Ipv4Address import Ipv4Address
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpConstants


class JetsArpHelper(TrafficGeneratingDeviceArpHelper):
    def __init__(self, ostinato_device):
        super(JetsArpHelper, self).__init__(ostinato_device)
        self._tcpip_stacks = {}  # {port_string:[JetsTcpipStackObject, JetsTcpipStackObject]}

    # trafficDevice.configure_arp(tx_port, "151.1.1.1", "00:33:44:55:66:77", 5, "0.0.0.0")
    # tcpip config -device $nicNumber -ipAddr $ip -netmask $mask -gateway $defRoute -macAddress $mac --vlanId =
    def configure_arp(self, port_string, start_ip, start_mac, num_addresses, gateway_address=None,
                      mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                      arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                      netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        prt_id = self.get_port_index_from_group_string(port_string)

        index = 0
        num_addresses = int(num_addresses)
        while index < num_addresses:
            mac = EnetAddress.add_to_address(EnetAddress(start_mac), index)
            ip = Ipv4Address.add_to_address(Ipv4Address(start_ip), index)
            options = "tcpip config -device " + str(prt_id) + " -ipAddr " + str(ip) + " "
            if gateway_address and not gateway_address == "0.0.0.0":
                options += "-gateway_address " + str(gateway_address) + " "
            if netmask:
                netmask = str(netmask)
                if netmask == "24":
                    options += "-netmask 255.255.255.0 "
                elif netmask == "16":
                    options += "-netmask 255.255.0.0 "
                elif netmask == "8":
                    options += "-netmask 255.0.0.0 "
                elif "." in netmask:
                    options += "-netmask " + netmask + " "
            options += "-macAddress " + str(mac) + " "
            if clear_settings_first:
                pass

            # set the vlan if needed
            if vlan_enable:
                options += "-vlanId " + str(vlan_id) + " "
            if index == 0:
                self.send_command("tcpip config " + options)
            else:
                self.send_command("tcpip alias " + options)
            index += 1

        # ##
        # ## Next maybe set up a stream with resolve macs or get it to reply to ICMP.
        # ##

    def configure_neighbor_discovery(self, port_string, start_ipv6, start_mac, num_addresses, gateway_address,
                                     mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                                     arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                                     netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        return self.logger.log_unimplemented_method()

    def get_arp_table(self, port_string):
        prt_id = self.get_port_index_from_group_string(port_string)
        return self.send_command("arp receive " + str(prt_id))

    def verify_arp_entry(self, port_string, expected_ip, expected_mac):
        value = self.get_arp_table(port_string)
        bool_res = False
        try:
            line = " ".join(value.split("\n")[1:-1])

            line = line.replace("\r", " ")
            line = line.replace("  ", " ")
            line = line.strip().lower().replace(":", ".").replace("-", ".")
            comp = (str(expected_ip) + " " + str(expected_mac))
            comp = comp.replace(":0", ":")
            comp = comp.replace("00", "0")
            comp = comp.replace(":", ".").replace("-", ".")
            comp = comp.lower()
            self.logger.log_info("comparing " + comp + " to " + line)
            bool_res = comp in line
        except:
            pass
        return bool_res

    def clear_arp_table(self, port_string, ip_address=None, vlan_id=None):
        prt_id = self.get_port_index_from_group_string(port_string)
        if ip_address and vlan_id:
            return self.send_command("tcpip clearArp -device " + str(prt_id) + " -ipAddr " + str(ip_address) +
                                     " -vlanId " + str(vlan_id))
        elif ip_address:
            return self.send_command("tcpip clearArp -device " + str(prt_id) + " -ipAddr " + str(ip_address))
        else:
            return self.send_command("tcpip clearArp -device " + str(prt_id))

    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3):
        prt_id = self.get_port_index_from_group_string(port_string)
        reply = self.send_command("axping config -device " + str(prt_id))
        options = " -t " + str(timeout_secs) + " -d 01 -n " + str(ping_count) + " -l 100 "
        ping_reply = self.send_command("axping " + destination_ip + " -device " + str(prt_id) +
                                       options + " -srcAddress " + source_ip)

        if "Can't perform ping on ip address" in ping_reply:
            api = self.get_api(NetworkEmulatingTcpConstants.TCP_API)
            api.create_tcp_stack(port_string, source_ip)
            ping_reply = self.send_command("axping " + destination_ip + " -device " + str(prt_id) +
                                           options + " -srcAddress " + source_ip)
            api.delete_tcp_stack(port_string, source_ip)
        self.send_command("global res1")
        self.send_command("axping results res1 -device " + str(prt_id) + "")
        ping_res = self.send_command("parray res1")
        return "did not get response" not in ping_reply and "isn't an array" not in ping_res

    # def _jets_add_stack(self, port_string, jets_stack_object):
    #     port_string = str(port_string)
    #     stream_id = str(stream_id)
    #     if port_string not in self._streams:
    #         self._streams[port_string] = {}
    #     port_streams = self._streams[port_string];
    #     port_streams[stream_id] = self.generate_jets_stream_name(port_string, stream_id)
    #     return port_streams[stream_id]
    #
    # def _jets_remove_stack(self, port_string, stack_id):


class JetsTcpipStackObject(object):
    def __init__(self, stream_name, port_string, port_id, stream_id, length, packet_mode, num_packets, rate_pps,
                 rate_burst):
        self.enabled = True
        self.port = port_string
        self.port_id = port_id
        self.stream_id = stream_id
        self.name = stream_name
        self.length = length
        self.packet_mode = packet_mode
        self.num_packets = num_packets
        self.rate_pps = rate_pps
        self.rate_burst = rate_burst
        self.state = None
        self.str = None

    def generate_pdl(self, pkt_string):
        self.str = "generator addPdlStream " + self.name + " " + str(self.port_id) + " -pdlStr \"" + pkt_string + \
                   "\"  " + "-totalLen " + str(self.length) + "  -mode " + self.packet_mode + " -rate " + \
                   str(max(self.rate_pps, self.num_packets)) + " -burstSize " + str(self.rate_burst)
