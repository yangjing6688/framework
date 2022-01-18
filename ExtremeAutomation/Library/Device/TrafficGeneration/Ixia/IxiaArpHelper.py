from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.Apis.IxRouteIxTclHalApi import IxRouteIxTclHalApi, \
    IxRouteIxTclHalConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingDeviceArpHelper import \
    TrafficGeneratingDeviceArpHelper
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.NetworkEmulatingTcpApi import NetworkEmulatingTcpConstants
from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.TrafficGenerationUtils import TrafficGenerationUtils
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiPacketConfigBuffersApi import \
    PacketConfigBuffersConstants
import time


class IxiaArpHelper(TrafficGeneratingDeviceArpHelper):
    def __init__(self, ixia_device):
        super(IxiaArpHelper, self).__init__(ixia_device)
        self.dev = ixia_device
        pass

    def configure_arp(self, port_string, start_ip, start_mac, num_addresses, gateway_address,
                      mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                      arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                      netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        port_string = self.convert_port_handle_to_port_string(port_string)
        api = self.dev.get_api(IxRouteIxTclHalConstants.IXROUTE_TCL_HAL_API)
        assert isinstance(api, IxRouteIxTclHalApi)
        # configure_ip_address_table(self, port_string, defaultGateway="0.0.0.0",fromIpAddress="151.1.1.1",
        #         fromMacAddress ="00 00 97 01 01 01",numAddresses =10,mappingOption=0,overrideDefaultGateway =1,
        #         gatewayIpAddress =c,enableUseNetwork ="true",netMask=24,enableExpandInterfaceTable ="false",
        #         enableVlan ="false",vlanId =0,
        #         atmEncapsulation =IxRouteIxTclHalConstants.IP_TABLE_ATM_ENCAPSULATION_LLC_BRIDGED_ETHERNET_FCS,
        #         atmVpi =0, atmVci =0, clear_settings_first=False)
        cmd_obj = api.configure_ip_address_table(port_string, from_ip_address=start_ip, from_mac_address=start_mac,
                                                 num_addresses=num_addresses, mapping_option=mapping_option,
                                                 gateway_ip_address=gateway_address, netmask=netmask,
                                                 enable_vlan=vlan_enable, vlan_id=vlan_id,
                                                 clear_settings_first=clear_settings_first)
        # configure_arp_server(self, port_string, retires=3, mode=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP,
        #                      rate=2083333, requestRepeatCount=3, clear_settings_first=False)
        cmd_obj = api.configure_arp_server(port_string, mode=arp_for, request_repeat_count=arp_retires,
                                           clear_settings_first=clear_settings_first)

    def configure_neighbor_discovery(self, port_string, start_ipv6, start_mac, num_addresses, gateway_address,
                                     mapping_option=IxRouteIxTclHalConstants.IP_TABLE_MAPPING_OPTIONS_ONE_IP_TO_ONE_MAC,
                                     arp_for=IxRouteIxTclHalConstants.ARP_MODE_RESOLVE_ARP, arp_retires=3,
                                     netmask=24, vlan_enable=False, vlan_id=None, clear_settings_first=False):
        return self.logger.log_unimplemented_method()

    def get_arp_table(self, port_string):
        return self.logger.log_unimplemented_method()

    def verify_arp_entry(self, port_string, expected_ip, expected_mac):
        return self.logger.log_unimplemented_method()

    def clear_arp_table(self, port_string, ip_address=None, vlan_id=None):
        return self.logger.log_unimplemented_method()

    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3):
        self.logger.log_info("Ixia ping timeout is simulated")
        og_port_string = port_string
        port_string = TrafficGenerationUtils.convert_port_string_to_ixtclhal_port(port_string)
        port_handle = TrafficGenerationUtils.convert_port_string_to_port_handle(og_port_string)

        api = self.get_api(NetworkEmulatingTcpConstants.TCP_API)
        pcb_api = self.get_api(PacketConfigBuffersConstants.PACKET_CONFIG_BUFFERS_API)
        pcb_api.packet_config_buffers(
            {PacketConfigBuffersConstants.PORT_HANDLE_CMD: port_handle,
             PacketConfigBuffersConstants.CONTROL_PLANE_CAPTURE_ENABLE_CMD: 1,
             PacketConfigBuffersConstants.CAPTURE_MODE_CMD: PacketConfigBuffersConstants.CAPTURE_MODE_TRIGGER,
             PacketConfigBuffersConstants.AFTER_TRIGGER_CMD: PacketConfigBuffersConstants.AFTER_TRIGGER_FILTER,
             PacketConfigBuffersConstants.CONTINUOUS_FILTER_CMD: PacketConfigBuffersConstants.CONTINUOUS_FILTER_ALL
             })

        api.create_tcp_stack(port_string, source_ip)

        self.send_command("stat get statAllStats " + str(port_string))
        self.send_command("stat cget  -txPingReply")
        self.send_command("stat cget  -txArpReply")
        self.send_command("stat cget  -txPingReply")
        self.send_command("stat cget  -rxArpRequest")
        self.send_command("stat cget  -rxPingRequest")
        try:
            tx_ping_request_before = int(self.send_command("stat cget  -txPingRequest").split("\n")[0].strip())
            rx_ping_reply_before = int(self.send_command("stat cget  -rxPingReply").split("\n")[0].strip())
            tx_arp_request_before = int(self.send_command("stat cget  -txArpRequest").split("\n")[0].strip())
            rx_arp_reply_before = int(self.send_command("stat cget  -rxArpReply").split("\n")[0].strip())
        except:
            tx_ping_request_before = 0
            rx_ping_reply_before = 0
            tx_arp_request_before = 0
            rx_arp_reply_before = 0
        self.send_command("interfaceTable select " + str(port_string))

        self.send_command("interfaceTable getFirstInterface")
        self.send_command("set description [interfaceEntry cget -description]")
        self.send_command("puts \"description=$description\"")
        index = 0
        time_out_index = 0
        while index < ping_count and time_out_index < timeout_secs:
            self.send_command("stat get statAllStats " + str(port_string))
            tx_count_before = int(self.send_command("stat cget  -txPingRequest").split("\n")[0].strip())
            res = self.send_command("set res [interfaceTable ping $description addressTypeIpV4 " + destination_ip + "]")
            index += 1
            self.send_command("stat get statAllStats " + str(port_string))
            tx_count_after = int(self.send_command("stat cget  -txPingRequest").split("\n")[0].strip())
            while time_out_index < timeout_secs and tx_count_before == tx_count_after:
                time.sleep(.8)
                self.send_command("stat get statAllStats " + str(port_string))
                tx_count_after = int(self.send_command("stat cget  -txPingRequest").split("\n")[0].strip())
                time_out_index += 1

        self.send_command("stat get statAllStats " + str(port_string))
        self.send_command("stat cget  -txPingReply")
        self.send_command("stat cget  -txArpReply")
        self.send_command("stat cget  -txPingReply")
        self.send_command("stat cget  -rxArpRequest")
        self.send_command("stat cget  -rxPingRequest")
        try:
            tx_ping_request_after = int(self.send_command("stat cget  -txPingRequest").split("\n")[0].strip())
            rx_ping_reply_after = int(self.send_command("stat cget  -rxPingReply").split("\n")[0].strip())
            tx_arp_request_after = int(self.send_command("stat cget  -txArpRequest").split("\n")[0].strip())
            rx_arp_reply_after = int(self.send_command("stat cget  -rxArpReply").split("\n")[0].strip())
        except:
            tx_ping_request_after = 0
            rx_ping_reply_after = 0
            tx_arp_request_after = 0
            rx_arp_reply_after = 0
        tx_passed = (tx_ping_request_before + ping_count) <= tx_ping_request_after
        rx_passed = (rx_ping_reply_before + ping_count) <= rx_ping_reply_after
        if not tx_passed:
            return self.logger.log_error("PING not sent.")
        if not rx_passed:
            return self.logger.log_error("PING not received.")
        if time_out_index == timeout_secs:
            return self.logger.log_error("PING timeout.")
        return tx_passed and rx_passed
