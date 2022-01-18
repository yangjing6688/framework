from ExtremeAutomation.Library.Device.TrafficGeneration.Utils.ProtocolEmulationConstants import \
    ProtocolEmulationConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import \
    TrafficStreamConfigurationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficTransmitKeywords import TrafficTransmitKeywords


class ProtocolEmulationDhcpKeywords(TrafficKeywordBaseClass):
    def __init__(self):
        super(ProtocolEmulationDhcpKeywords, self).__init__()
        self.emulation_constants = ProtocolEmulationConstants()

    def create_dhcp_client(self, port_string, mac_address, network_mask, vlan=-1, count=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [network_mask] -
        [vlan] -  (default: -1)
        [count] -  (default: 1)
        [step] -  (default: 1)

        create_dhcp_client
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        self.emulation_api.create_dhcp_client(self.current_port, mac_address, network_mask, vlan, count,
                                              step)
        self._keyword_cleanup()

    def remove_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [network_mask] -
        [count] -  (default: 1)
        [step] -  (default: 1)

        remove_dhcp_client
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        self.emulation_api.remove_dhcp_client(self.current_port, mac_address, network_mask, count, step)
        self._keyword_cleanup()

    def start_dhcp_client(self, port_string, mac_address, network_mask, count=1, step=1, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [network_mask] -
        [count] -  (default: 1)
        [step] -  (default: 1)

        start_dhcp_client
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        self.emulation_api.start_dhcp_client(self.current_port, mac_address, network_mask, count, step)
        self._keyword_cleanup()

    def get_dhcp_client_address(self, port_string, mac_address, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -

        get_dhcp_client_address
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        self.emulation_api.get_dhcp_client_address(self.current_port, mac_address)
        self._keyword_cleanup()

    def wait_dhcp_client_address(self, port_string, mac_address, max_wait_in_sec=60, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -

        get_dhcp_client_address
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        address = self.emulation_api.wait_for_dhcp_client_address(self.current_port, mac_address,
                                                                  max_wait_in_sec * 1000)
        self._determine_result(address != "0.0.0.0", True, **kwargs)
        self._keyword_cleanup()

    def ping_dhcp_client(self, port_string, mac_address, network_mask, destination_ip, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [network_mask] -
        [destination_ip] -

        ping_dhcp_client
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)

        self.emulation_api.ping_dhcp_client(self.current_port, mac_address, network_mask, destination_ip)
        self._keyword_cleanup()

    def transmit_ipv4_frames_from_dhcp_address(self, port_string, src_mac, dst_mac, dip, vlan_id=None, num_packets=10,
                                               packet_rate=100, length=None, **kwargs):
        """
        Keyword Arguments:
        [port_string] -
        [mac_address] -
        [num_packets] -
        [packet_rate] -
        [src_mac] -
        [dst_mac] -
        [dip] -
        [length] -
        [kwargs] -

        transmit_ipv4_untagged_frames_from_dhcp_address
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(emulation_api_const=self.emulation_constants.DHCP_API, **kwargs)
        sip = self.emulation_api.wait_for_dhcp_client_address(self.current_port, src_mac, 60000)
        stream_number = 1
        tx_packet_name = "dhcp_packet"
        tx_port = port_string
        rate = packet_rate
        unit = "pps"
        count = num_packets

        tsck = TrafficStreamConfigurationKeywords()
        tpk = TrafficPacketCreationKeywords()
        ttk = TrafficTransmitKeywords()

        tsck.remove_all_streams_from_port(tx_port)
        tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, length=length)
        tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
        tpk.set_ipv4(tx_packet_name, dip, sip)
        tsck.configure_stream_packet(tx_port, stream_number, tx_packet_name)
        tsck.configure_stream_rate(tx_port, stream_number, rate)
        tsck.configure_stream_unit(tx_port, stream_number, unit)
        tsck.configure_stream_count(tx_port, stream_number, count)
        tsck.configure_stream_mode_single_burst(tx_port, stream_number)
        tsck.add_stream_to_port(tx_port, stream_number)
        ttk.start_transmit_on_port_and_wait(tx_port)
        ttk.stop_transmit_on_port(tx_port)
        self._keyword_cleanup()
