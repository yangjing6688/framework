from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingIgmpApi import NetworkEmulatingIgmpApi
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class JetsIgmpApi(NetworkEmulatingIgmpApi):
    def __init__(self, device):
        super(JetsIgmpApi, self).__init__(device)

    def create_igmp_host(self, port_string, source_ip, netmask, gateway_address, mac_address, igmp_version=2,
                         vlan_id=None, options=None):
        # config one host:
        # tcpip config -device 1 -ipAddr 16.1.1.1 -netmask 255.255.255.0 -gateway 16.1.1.6 -macAddress 0.0.11.11.16.01
        #   -state enable
        # igmp hostconfig -device 1 -ipAddr 16.1.1.1 -version 2 -step 0.0.0.1 -count 1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)

            config_str = dev.get_tcp_config_string(prt_id)
            tcpip = config_str + " -device " + str(prt_id) + " -ipAddr " + source_ip + \
                " -netmask " + netmask + " -gateway " + gateway_address + \
                " -macAddress " + mac_address
            if vlan_id:
                tcpip += " -vlanId " + str(vlan_id)
            tcpip += "  -state enable "
            self.send_command("tcpip " + tcpip)
            config_igmp_host = " -device " + str(prt_id) + \
                               " -ipAddr " + str(source_ip) + \
                               " -version " + str(igmp_version) + " -step 0.0.0.1 -count 1 "
            self.send_command("igmp hostconfig " + config_igmp_host)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def generate_igmp_leave(self, port_string, source_ip, multicast_address):
        # igmp leave -device 1 -ipAddr 16.1.1.1 -step 0.0.0.1 -count 1 -multiAddr 225.1.1.1 -multistep 0.0.0.1
        #   -multicount 1 -ssmGroupRange true -leaveAndSendWaitTime 1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            config_igmp_host = " -device " + str(prt_id) + \
                               " -ipAddr " + str(source_ip) + \
                               " -step 0.0.0.1 -count 1 " + \
                               " -multiAddr " + str(multicast_address) + \
                               " -multistep 0.0.0.1 -multicount 1 " + \
                               "-ssmGroupRange true -leaveAndSendWaitTime 1"

            self.send_command("igmp leave " + config_igmp_host)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def generate_igmp_join(self, port_string, source_ip, multicast_address):
        # igmp join -device 1 -ipAddr 16.1.1.1 -step 0.0.0.1 -count 1 -multiAddr 225.1.1.1 -multistep 0.0.0.1
        #   -multicount 1
        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)
            config_igmp_host = " -device " + str(prt_id) + \
                               " -ipAddr " + str(source_ip) + \
                               " -step 0.0.0.1 -count 1 " + \
                               " -multiAddr " + str(multicast_address) + \
                               " -multistep 0.0.0.1 -multicount 1 "

            self.send_command("igmp join " + config_igmp_host)
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())

    def remove_igmp_host(self, port_string):
        """
        igmp  teminiate <port>
        tcpip  teminiate <port>
        also, delete the tcp stacks
        :param port_string:
        :return:
        """
        # igmp terminate -device 1
        # tcpip terminate -device 1

        try:
            dev = self.get_device()
            prt_id = dev.get_port_index_from_group_string(port_string)

            self.send_command("igmp  teminiate " + str(prt_id))
            self.send_command("tcpip  teminiate " + str(prt_id))
        except Exception:
            self.logger.log_info(StringUtils.exception_to_string())
