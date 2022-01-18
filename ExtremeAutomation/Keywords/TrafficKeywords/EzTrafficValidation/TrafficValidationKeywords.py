from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketCreationKeywords import TrafficPacketCreationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficCaptureKeywords import TrafficCaptureKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStreamConfigurationKeywords import \
    TrafficStreamConfigurationKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficTransmitKeywords import TrafficTransmitKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficStatisticsKeywords import TrafficStatisticsKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPacketInspectionKeywords import TrafficPacketInspectionKeywords


class TrafficValidationKeywords(TrafficKeywordBaseClass):

    ######################################################################################
    # Auto generated start (do not edit code here)
    ######################################################################################

    def transmit_ethernet2_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, ether_type=None, length=None,
                                                               prime=False, skip_config=False, filter_list=True,
                                                               threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Ethernet2 Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ethernet2_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, ether_type=None, length=None,
                                                                   prime=False, skip_config=False, filter_list=True,
                                                                   threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Ethernet2 Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ethernet2_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac,
                                                                               ether_type=None, length=None,
                                                                               prime=False, skip_config=False,
                                                                               filter_list=True, threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Ethernet2 Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ethernet2_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   ether_type=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Ethernet2 Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ethernet2_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                             dst_mac, ether_type=None, vlan_id=None, vlan_priority=None,
                                                             vlan_tpid=None, length=None, prime=False,
                                                             skip_config=False, filter_list=True, threshold=0,
                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Ethernet2 Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ethernet2_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, ether_type=None, vlan_id=None,
                                                                 vlan_priority=None, vlan_tpid=None, length=None,
                                                                 prime=False, skip_config=False, filter_list=True,
                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Ethernet2 Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ethernet2_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                             packet_rate, src_mac, dst_mac,
                                                                             ether_type=None, vlan_id=None,
                                                                             vlan_priority=None, vlan_tpid=None,
                                                                             length=None, prime=False,
                                                                             skip_config=False, filter_list=True,
                                                                             threshold=0,
                                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Ethernet2 Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ethernet2_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 ether_type=None, vlan_id=None,
                                                                                 vlan_priority=None, vlan_tpid=None,
                                                                                 length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Ethernet2 Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ethernet2_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                           dst_mac, ether_type=None, vlan_id_list=None,
                                                           vlan_prio_list=None, vlan_tpid_list=None, length=None,
                                                           prime=False, skip_config=False, filter_list=True,
                                                           threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ Ethernet2 Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ethernet2_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, ether_type=None, vlan_id_list=None,
                                                               vlan_prio_list=None, vlan_tpid_list=None, length=None,
                                                               prime=False, skip_config=False, filter_list=True,
                                                               threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ Ethernet2 Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ethernet2_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                           packet_rate, src_mac, dst_mac,
                                                                           ether_type=None, vlan_id_list=None,
                                                                           vlan_prio_list=None, vlan_tpid_list=None,
                                                                           length=None, prime=False, skip_config=False,
                                                                           filter_list=True, threshold=0,
                                                                           packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ Ethernet2 Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ethernet2_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac,
                                                                               ether_type=None, vlan_id_list=None,
                                                                               vlan_prio_list=None, vlan_tpid_list=None,
                                                                               length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [ether_type]        - packet ether type (Ex: 0xFFFF)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ Ethernet2 Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipx_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                         dst_mac, length=None, prime=False, skip_config=False,
                                                         filter_list=True, threshold=0,
                                                         packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPX Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipx_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                             dst_mac, length=None, prime=False, skip_config=False,
                                                             filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPX Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipx_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                         packet_rate, src_mac, dst_mac, length=None,
                                                                         prime=False, skip_config=False,
                                                                         filter_list=True, threshold=0,
                                                                         packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPX Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipx_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                             packet_rate, src_mac, dst_mac, length=None,
                                                                             prime=False, skip_config=False,
                                                                             filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPX Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipx_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                       dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                       length=None, prime=False, skip_config=False, filter_list=True,
                                                       threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPX Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipx_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                           dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                           length=None, prime=False, skip_config=False,
                                                           filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPX Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipx_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                       src_mac, dst_mac, vlan_id=None,
                                                                       vlan_priority=None, vlan_tpid=None, length=None,
                                                                       prime=False, skip_config=False, filter_list=True,
                                                                       threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPX Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipx_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                           packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                           vlan_priority=None, vlan_tpid=None,
                                                                           length=None, prime=False, skip_config=False,
                                                                           filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPX Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, sip=None, dip=None, length=None, prime=False,
                                                          skip_config=False, filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac, sip=None,
                                                                          dip=None, length=None, prime=False,
                                                                          skip_config=False, filter_list=True,
                                                                          threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                        dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                        sip=None, dip=None, length=None, prime=False, skip_config=False,
                                                        filter_list=True, threshold=0,
                                                        packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, length=None, prime=False,
                                                            skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                        vlan_priority=None, vlan_tpid=None, sip=None,
                                                                        dip=None, length=None, prime=False,
                                                                        skip_config=False, filter_list=True,
                                                                        threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, length=None,
                                                                            prime=False, skip_config=False,
                                                                            filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, sip=None, dip=None, length=None, prime=False,
                                                          skip_config=False, filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac, sip=None,
                                                                          dip=None, length=None, prime=False,
                                                                          skip_config=False, filter_list=True,
                                                                          threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                        dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                        sip=None, dip=None, length=None, prime=False, skip_config=False,
                                                        filter_list=True, threshold=0,
                                                        packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, length=None, prime=False,
                                                            skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                        vlan_priority=None, vlan_tpid=None, sip=None,
                                                                        dip=None, length=None, prime=False,
                                                                        skip_config=False, filter_list=True,
                                                                        threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, length=None,
                                                                            prime=False, skip_config=False,
                                                                            filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_tcp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, src_port=None, dst_port=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0,
                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 TCP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tcp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, src_port=None,
                                                                  dst_port=None, length=None, prime=False,
                                                                  skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 TCP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_tcp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, src_port=None, dst_port=None,
                                                                              length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 TCP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tcp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, src_port=None,
                                                                                  dst_port=None, length=None,
                                                                                  prime=False, skip_config=False,
                                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 TCP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_tcp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, src_port=None, dst_port=None,
                                                            length=None, prime=False, skip_config=False,
                                                            filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 TCP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tcp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, src_port=None,
                                                                dst_port=None, length=None, prime=False,
                                                                skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 TCP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_tcp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, src_port=None,
                                                                            dst_port=None, length=None, prime=False,
                                                                            skip_config=False, filter_list=True,
                                                                            threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 TCP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tcp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                src_port=None, dst_port=None,
                                                                                length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 TCP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_udp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, src_port=None, dst_port=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0,
                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 UDP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_udp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, src_port=None,
                                                                  dst_port=None, length=None, prime=False,
                                                                  skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 UDP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_udp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, src_port=None, dst_port=None,
                                                                              length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 UDP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_udp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, src_port=None,
                                                                                  dst_port=None, length=None,
                                                                                  prime=False, skip_config=False,
                                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 UDP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_udp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, src_port=None, dst_port=None,
                                                            length=None, prime=False, skip_config=False,
                                                            filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 UDP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_udp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, src_port=None,
                                                                dst_port=None, length=None, prime=False,
                                                                skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 UDP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_udp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, src_port=None,
                                                                            dst_port=None, length=None, prime=False,
                                                                            skip_config=False, filter_list=True,
                                                                            threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 UDP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_udp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                src_port=None, dst_port=None,
                                                                                length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 UDP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_icmp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, sip=None, dip=None, length=None,
                                                               prime=False, skip_config=False, filter_list=True,
                                                               threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ICMP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_icmp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, sip=None, dip=None, length=None,
                                                                   prime=False, skip_config=False, filter_list=True,
                                                                   threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ICMP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_icmp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac, sip=None,
                                                                               dip=None, length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ICMP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_icmp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   sip=None, dip=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ICMP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_icmp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                             dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                             sip=None, dip=None, length=None, prime=False,
                                                             skip_config=False, filter_list=True, threshold=0,
                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ICMP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_icmp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                 vlan_tpid=None, sip=None, dip=None, length=None,
                                                                 prime=False, skip_config=False, filter_list=True,
                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ICMP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_icmp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                             packet_rate, src_mac, dst_mac,
                                                                             vlan_id=None, vlan_priority=None,
                                                                             vlan_tpid=None, sip=None, dip=None,
                                                                             length=None, prime=False,
                                                                             skip_config=False, filter_list=True,
                                                                             threshold=0,
                                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ICMP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_icmp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 vlan_id=None, vlan_priority=None,
                                                                                 vlan_tpid=None, sip=None, dip=None,
                                                                                 length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ICMP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=1)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpIpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=1)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_fragment_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, sip=None, dip=None, frag=None,
                                                                   length=None, prime=False, skip_config=False,
                                                                   filter_list=True, threshold=0,
                                                                   packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Fragment Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_fragment_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                       src_mac, dst_mac, sip=None, dip=None, frag=None,
                                                                       length=None, prime=False, skip_config=False,
                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Fragment Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_fragment_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   sip=None, dip=None, frag=None,
                                                                                   length=None, prime=False,
                                                                                   skip_config=False, filter_list=True,
                                                                                   threshold=0,
                                                                                   packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Fragment Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_fragment_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                       num_packets, packet_rate,
                                                                                       src_mac, dst_mac, sip=None,
                                                                                       dip=None, frag=None, length=None,
                                                                                       prime=False, skip_config=False,
                                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Fragment Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_fragment_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                 vlan_tpid=None, sip=None, dip=None, frag=None,
                                                                 length=None, prime=False, skip_config=False,
                                                                 filter_list=True, threshold=0,
                                                                 packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Fragment Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_fragment_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                     src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                     vlan_tpid=None, sip=None, dip=None, frag=None,
                                                                     length=None, prime=False, skip_config=False,
                                                                     filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Fragment Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_fragment_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 vlan_id=None, vlan_priority=None,
                                                                                 vlan_tpid=None, sip=None, dip=None,
                                                                                 frag=None, length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0,
                                                                                 packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Fragment Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_fragment_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                     num_packets, packet_rate, src_mac,
                                                                                     dst_mac, vlan_id=None,
                                                                                     vlan_priority=None, vlan_tpid=None,
                                                                                     sip=None, dip=None, frag=None,
                                                                                     length=None, prime=False,
                                                                                     skip_config=False,
                                                                                     filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Fragment Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_untagged_ipv4_ttl_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, ttl=None, length=None,
                                                              prime=False, skip_config=False, filter_list=True,
                                                              threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Untagged IPv4 TTL Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_untagged_ipv4_ttl_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, ttl=None,
                                                                  length=None, prime=False, skip_config=False,
                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Untagged IPv4 TTL Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_untagged_ipv4_ttl_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, ttl=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Untagged IPv4 TTL Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_untagged_ipv4_ttl_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, ttl=None,
                                                                                  length=None, prime=False,
                                                                                  skip_config=False, filter_list=True,
                                                                                  threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Untagged IPv4 TTL Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_tagged_ipv4_ttl_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, ttl=None, length=None, prime=False,
                                                            skip_config=False, filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Tagged IPv4 TTL Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_tagged_ipv4_ttl_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, ttl=None,
                                                                length=None, prime=False, skip_config=False,
                                                                filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Tagged IPv4 TTL Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_tagged_ipv4_ttl_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, ttl=None, length=None,
                                                                            prime=False, skip_config=False,
                                                                            filter_list=True, threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit Tagged IPv4 TTL Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_tagged_ipv4_ttl_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                ttl=None, length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit Tagged IPv4 TTL Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_tos_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, tos=None, length=None,
                                                              prime=False, skip_config=False, filter_list=True,
                                                              threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ToS Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tos_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, tos=None,
                                                                  length=None, prime=False, skip_config=False,
                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ToS Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_tos_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, tos=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ToS Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tos_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, tos=None,
                                                                                  length=None, prime=False,
                                                                                  skip_config=False, filter_list=True,
                                                                                  threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ToS Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_tos_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, tos=None, length=None, prime=False,
                                                            skip_config=False, filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ToS Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tos_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, tos=None,
                                                                length=None, prime=False, skip_config=False,
                                                                filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ToS Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_tos_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, tos=None, length=None,
                                                                            prime=False, skip_config=False,
                                                                            filter_list=True, threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 ToS Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_tos_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                tos=None, length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 ToS Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_protocol_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, sip=None, dip=None, proto=None,
                                                                   length=None, prime=False, skip_config=False,
                                                                   filter_list=True, threshold=0,
                                                                   packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Protocol Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_protocol_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                       src_mac, dst_mac, sip=None, dip=None, proto=None,
                                                                       length=None, prime=False, skip_config=False,
                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Protocol Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_protocol_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   sip=None, dip=None, proto=None,
                                                                                   length=None, prime=False,
                                                                                   skip_config=False, filter_list=True,
                                                                                   threshold=0,
                                                                                   packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Protocol Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_protocol_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                       num_packets, packet_rate,
                                                                                       src_mac, dst_mac, sip=None,
                                                                                       dip=None, proto=None,
                                                                                       length=None, prime=False,
                                                                                       skip_config=False,
                                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Protocol Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv4_protocol_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                 vlan_tpid=None, sip=None, dip=None, proto=None,
                                                                 length=None, prime=False, skip_config=False,
                                                                 filter_list=True, threshold=0,
                                                                 packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Protocol Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_protocol_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                     src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                     vlan_tpid=None, sip=None, dip=None, proto=None,
                                                                     length=None, prime=False, skip_config=False,
                                                                     filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Protocol Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv4_protocol_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 vlan_id=None, vlan_priority=None,
                                                                                 vlan_tpid=None, sip=None, dip=None,
                                                                                 proto=None, length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0,
                                                                                 packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv4 Protocol Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv4_protocol_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                     num_packets, packet_rate, src_mac,
                                                                                     dst_mac, vlan_id=None,
                                                                                     vlan_priority=None, vlan_tpid=None,
                                                                                     sip=None, dip=None, proto=None,
                                                                                     length=None, prime=False,
                                                                                     skip_config=False,
                                                                                     filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv4 Protocol Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_tcp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, src_port=None, dst_port=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0,
                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 TCP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tcp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, src_port=None,
                                                                  dst_port=None, length=None, prime=False,
                                                                  skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 TCP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_tcp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, src_port=None, dst_port=None,
                                                                              length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 TCP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tcp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, src_port=None,
                                                                                  dst_port=None, length=None,
                                                                                  prime=False, skip_config=False,
                                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 TCP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_tcp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, src_port=None, dst_port=None,
                                                            length=None, prime=False, skip_config=False,
                                                            filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 TCP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tcp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, src_port=None,
                                                                dst_port=None, length=None, prime=False,
                                                                skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 TCP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_tcp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, src_port=None,
                                                                            dst_port=None, length=None, prime=False,
                                                                            skip_config=False, filter_list=True,
                                                                            threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 TCP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_tcp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                src_port=None, dst_port=None,
                                                                                length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 TCP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_udp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, sip=None, dip=None, src_port=None, dst_port=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0,
                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 UDP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_udp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, sip=None, dip=None, src_port=None,
                                                                  dst_port=None, length=None, prime=False,
                                                                  skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 UDP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_udp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac, sip=None,
                                                                              dip=None, src_port=None, dst_port=None,
                                                                              length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0,
                                                                              packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 UDP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_udp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  sip=None, dip=None, src_port=None,
                                                                                  dst_port=None, length=None,
                                                                                  prime=False, skip_config=False,
                                                                                  filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 UDP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_udp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                            dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                            sip=None, dip=None, src_port=None, dst_port=None,
                                                            length=None, prime=False, skip_config=False,
                                                            filter_list=True, threshold=0,
                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 UDP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_udp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                vlan_tpid=None, sip=None, dip=None, src_port=None,
                                                                dst_port=None, length=None, prime=False,
                                                                skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 UDP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_udp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                            vlan_priority=None, vlan_tpid=None,
                                                                            sip=None, dip=None, src_port=None,
                                                                            dst_port=None, length=None, prime=False,
                                                                            skip_config=False, filter_list=True,
                                                                            threshold=0,
                                                                            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 UDP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_udp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id=None, vlan_priority=None,
                                                                                vlan_tpid=None, sip=None, dip=None,
                                                                                src_port=None, dst_port=None,
                                                                                length=None, prime=False,
                                                                                skip_config=False, filter_list=True,
                                                                                threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 UDP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_icmp_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, sip=None, dip=None, length=None,
                                                               prime=False, skip_config=False, filter_list=True,
                                                               threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 ICMP Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_icmp_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, sip=None, dip=None, length=None,
                                                                   prime=False, skip_config=False, filter_list=True,
                                                                   threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 ICMP Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_icmp_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac, sip=None,
                                                                               dip=None, length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 ICMP Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_icmp_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   sip=None, dip=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 ICMP Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_icmp_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                             dst_mac, vlan_id=None, vlan_priority=None, vlan_tpid=None,
                                                             sip=None, dip=None, length=None, prime=False,
                                                             skip_config=False, filter_list=True, threshold=0,
                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 ICMP Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_icmp_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                 vlan_tpid=None, sip=None, dip=None, length=None,
                                                                 prime=False, skip_config=False, filter_list=True,
                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 ICMP Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_icmp_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                             packet_rate, src_mac, dst_mac,
                                                                             vlan_id=None, vlan_priority=None,
                                                                             vlan_tpid=None, sip=None, dip=None,
                                                                             length=None, prime=False,
                                                                             skip_config=False, filter_list=True,
                                                                             threshold=0,
                                                                             packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 ICMP Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_icmp_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 vlan_id=None, vlan_priority=None,
                                                                                 vlan_tpid=None, sip=None, dip=None,
                                                                                 length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 ICMP Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IcmpV6IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                              length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=58)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_fragment_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, sip=None, dip=None, length=None,
                                                                   prime=False, skip_config=False, filter_list=True,
                                                                   threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Fragment Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_fragment_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                       src_mac, dst_mac, sip=None, dip=None,
                                                                       length=None, prime=False, skip_config=False,
                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Fragment Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_fragment_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   sip=None, dip=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0,
                                                                                   packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Fragment Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_fragment_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                       num_packets, packet_rate,
                                                                                       src_mac, dst_mac, sip=None,
                                                                                       dip=None, length=None,
                                                                                       prime=False, skip_config=False,
                                                                                       filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Fragment Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_fragment_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                 src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                 vlan_tpid=None, sip=None, dip=None, length=None,
                                                                 prime=False, skip_config=False, filter_list=True,
                                                                 threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Fragment Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_fragment_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                     src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                     vlan_tpid=None, sip=None, dip=None, length=None,
                                                                     prime=False, skip_config=False, filter_list=True,
                                                                     threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Fragment Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_fragment_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                 packet_rate, src_mac, dst_mac,
                                                                                 vlan_id=None, vlan_priority=None,
                                                                                 vlan_tpid=None, sip=None, dip=None,
                                                                                 length=None, prime=False,
                                                                                 skip_config=False, filter_list=True,
                                                                                 threshold=0,
                                                                                 packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Fragment Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_fragment_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                     num_packets, packet_rate, src_mac,
                                                                                     dst_mac, vlan_id=None,
                                                                                     vlan_priority=None, vlan_tpid=None,
                                                                                     sip=None, dip=None, length=None,
                                                                                     prime=False, skip_config=False,
                                                                                     filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Fragment Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_hop_limit_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                    src_mac, dst_mac, sip=None, dip=None,
                                                                    hop_limit=None, length=None, prime=False,
                                                                    skip_config=False, filter_list=True, threshold=0,
                                                                    packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Hop Limit Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_hop_limit_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac, sip=None,
                                                                        dip=None, hop_limit=None, length=None,
                                                                        prime=False, skip_config=False,
                                                                        filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Hop Limit Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_hop_limit_untagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                    packet_rate, src_mac, dst_mac,
                                                                                    sip=None, dip=None, hop_limit=None,
                                                                                    length=None, prime=False,
                                                                                    skip_config=False, filter_list=True,
                                                                                    threshold=0,
                                                                                    packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Hop Limit Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_hop_limit_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                        num_packets, packet_rate,
                                                                                        src_mac, dst_mac, sip=None,
                                                                                        dip=None, hop_limit=None,
                                                                                        length=None, prime=False,
                                                                                        skip_config=False,
                                                                                        filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Hop Limit Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_hop_limit_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                  vlan_tpid=None, sip=None, dip=None, hop_limit=None,
                                                                  length=None, prime=False, skip_config=False,
                                                                  filter_list=True, threshold=0,
                                                                  packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Hop Limit Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_hop_limit_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, vlan_id=None,
                                                                      vlan_priority=None, vlan_tpid=None, sip=None,
                                                                      dip=None, hop_limit=None, length=None,
                                                                      prime=False, skip_config=False, filter_list=True,
                                                                      threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Hop Limit Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_hop_limit_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  vlan_id=None, vlan_priority=None,
                                                                                  vlan_tpid=None, sip=None, dip=None,
                                                                                  hop_limit=None, length=None,
                                                                                  prime=False, skip_config=False,
                                                                                  filter_list=True, threshold=0,
                                                                                  packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Hop Limit Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_hop_limit_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                      num_packets, packet_rate, src_mac,
                                                                                      dst_mac, vlan_id=None,
                                                                                      vlan_priority=None,
                                                                                      vlan_tpid=None, sip=None,
                                                                                      dip=None, hop_limit=None,
                                                                                      length=None, prime=False,
                                                                                      skip_config=False,
                                                                                      filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Hop Limit Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_traffic_class_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac, sip=None,
                                                                        dip=None, traffic_class=None, length=None,
                                                                        prime=False, skip_config=False,
                                                                        filter_list=True, threshold=0,
                                                                        packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Traffic Class Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_traffic_class_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                            packet_rate, src_mac, dst_mac, sip=None,
                                                                            dip=None, traffic_class=None, length=None,
                                                                            prime=False, skip_config=False,
                                                                            filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Traffic Class Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_traffic_class_untagged_frames_bidirectionally_and_verify_received(
            self, tx_port, rx_port,
            num_packets, packet_rate,
            src_mac, dst_mac, sip=None,
            dip=None, traffic_class=None,
            length=None, prime=False,
            skip_config=False,
            filter_list=True, threshold=0,
            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Traffic Class Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_traffic_class_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                            num_packets, packet_rate,
                                                                                            src_mac, dst_mac, sip=None,
                                                                                            dip=None,
                                                                                            traffic_class=None,
                                                                                            length=None, prime=False,
                                                                                            skip_config=False,
                                                                                            filter_list=True,
                                                                                            threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Traffic Class Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_traffic_class_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, vlan_id=None,
                                                                      vlan_priority=None, vlan_tpid=None, sip=None,
                                                                      dip=None, traffic_class=None, length=None,
                                                                      prime=False, skip_config=False, filter_list=True,
                                                                      threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Traffic Class Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_traffic_class_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                          vlan_priority=None, vlan_tpid=None, sip=None,
                                                                          dip=None, traffic_class=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Traffic Class Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_traffic_class_tagged_frames_bidirectionally_and_verify_received(
            self, tx_port, rx_port,
            num_packets, packet_rate, src_mac,
            dst_mac, vlan_id=None,
            vlan_priority=None,
            vlan_tpid=None, sip=None,
            dip=None, traffic_class=None,
            length=None, prime=False,
            skip_config=False,
            filter_list=True, threshold=0,
            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Traffic Class Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_traffic_class_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                          num_packets, packet_rate,
                                                                                          src_mac, dst_mac,
                                                                                          vlan_id=None,
                                                                                          vlan_priority=None,
                                                                                          vlan_tpid=None, sip=None,
                                                                                          dip=None, traffic_class=None,
                                                                                          length=None, prime=False,
                                                                                          skip_config=False,
                                                                                          filter_list=True,
                                                                                          threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Traffic Class Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_next_header_untagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, sip=None, dip=None,
                                                                      next_header=None, length=None, prime=False,
                                                                      skip_config=False, filter_list=True, threshold=0,
                                                                      packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Next Header Untagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_next_header_untagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac, sip=None,
                                                                          dip=None, next_header=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Next Header Untagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_next_header_untagged_frames_bidirectionally_and_verify_received(
            self, tx_port, rx_port,
            num_packets, packet_rate, src_mac,
            dst_mac, sip=None, dip=None,
            next_header=None, length=None,
            prime=False, skip_config=False,
            filter_list=True, threshold=0,
            packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Next Header Untagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_next_header_untagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                          num_packets, packet_rate,
                                                                                          src_mac, dst_mac, sip=None,
                                                                                          dip=None, next_header=None,
                                                                                          length=None, prime=False,
                                                                                          skip_config=False,
                                                                                          filter_list=True,
                                                                                          threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Next Header Untagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_ipv6_next_header_tagged_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                    src_mac, dst_mac, vlan_id=None, vlan_priority=None,
                                                                    vlan_tpid=None, sip=None, dip=None,
                                                                    next_header=None, length=None, prime=False,
                                                                    skip_config=False, filter_list=True, threshold=0,
                                                                    packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Next Header Tagged Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_next_header_tagged_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac, vlan_id=None,
                                                                        vlan_priority=None, vlan_tpid=None, sip=None,
                                                                        dip=None, next_header=None, length=None,
                                                                        prime=False, skip_config=False,
                                                                        filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Next Header Tagged Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid,
                                  length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_ipv6_next_header_tagged_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                    packet_rate, src_mac, dst_mac,
                                                                                    vlan_id=None, vlan_priority=None,
                                                                                    vlan_tpid=None, sip=None, dip=None,
                                                                                    next_header=None, length=None,
                                                                                    prime=False, skip_config=False,
                                                                                    filter_list=True, threshold=0,
                                                                                    packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit IPv6 Next Header Tagged Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_ipv6_next_header_tagged_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                        num_packets, packet_rate,
                                                                                        src_mac, dst_mac, vlan_id=None,
                                                                                        vlan_priority=None,
                                                                                        vlan_tpid=None, sip=None,
                                                                                        dip=None, next_header=None,
                                                                                        length=None, prime=False,
                                                                                        skip_config=False,
                                                                                        filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id]           - packet vlan ID (Ex: 1000)
        [vlan_priority]     - packet priority (Ex: 5)
        [vlan_tpid]         - packet vlan protocol id  (Ex: 0x8100)
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit IPv6 Next Header Tagged Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6Packet", vlan_id, vlan_priority, vlan_tpid, length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipx_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac, dst_mac,
                                                     vlan_id_list=None, vlan_prio_list=None, vlan_tpid_list=None,
                                                     length=None, prime=False, skip_config=False, filter_list=True,
                                                     threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPX Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipx_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                         dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                         vlan_tpid_list=None, length=None, prime=False,
                                                         skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPX Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipx_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                     src_mac, dst_mac, vlan_id_list=None,
                                                                     vlan_prio_list=None, vlan_tpid_list=None,
                                                                     length=None, prime=False, skip_config=False,
                                                                     filter_list=True, threshold=0,
                                                                     packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPX Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipx_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                         packet_rate, src_mac, dst_mac,
                                                                         vlan_id_list=None, vlan_prio_list=None,
                                                                         vlan_tpid_list=None, length=None, prime=False,
                                                                         skip_config=False, filter_list=True,
                                                                         threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPX Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac, ether_type=0x8137)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                      dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                      vlan_tpid_list=None, sip=None, dip=None, length=None, prime=False,
                                                      skip_config=False, filter_list=True, threshold=0,
                                                      packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, length=None,
                                                          prime=False, skip_config=False, filter_list=True,
                                                          threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, vlan_id_list=None,
                                                                      vlan_prio_list=None, vlan_tpid_list=None,
                                                                      sip=None, dip=None, length=None, prime=False,
                                                                      skip_config=False, filter_list=True, threshold=0,
                                                                      packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          length=None, prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                      dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                      vlan_tpid_list=None, sip=None, dip=None, length=None, prime=False,
                                                      skip_config=False, filter_list=True, threshold=0,
                                                      packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, length=None,
                                                          prime=False, skip_config=False, filter_list=True,
                                                          threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, vlan_id_list=None,
                                                                      vlan_prio_list=None, vlan_tpid_list=None,
                                                                      sip=None, dip=None, length=None, prime=False,
                                                                      skip_config=False, filter_list=True, threshold=0,
                                                                      packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          length=None, prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_tcp_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                          dst_port=None, length=None, prime=False, skip_config=False,
                                                          filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 TCP Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_tcp_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                              dst_port=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 TCP Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_tcp_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          src_port=None, dst_port=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 TCP Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_tcp_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              src_port=None, dst_port=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 TCP Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_udp_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                          dst_port=None, length=None, prime=False, skip_config=False,
                                                          filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 UDP Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_udp_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                              dst_port=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 UDP Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_udp_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          src_port=None, dst_port=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 UDP Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_udp_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              src_port=None, dst_port=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 UDP Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_tcp_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                          dst_port=None, length=None, prime=False, skip_config=False,
                                                          filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 TCP Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_tcp_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                              dst_port=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 TCP Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_tcp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_tcp_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          src_port=None, dst_port=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 TCP Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_tcp_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              src_port=None, dst_port=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port (Ex: 66)
        [dst_port]          - packet Destination UDP Port (Ex: 66)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 TCP Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_tcp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2TcpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_tcp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_udp_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                          dst_port=None, length=None, prime=False, skip_config=False,
                                                          filter_list=True, threshold=0,
                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 UDP Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_udp_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, src_port=None,
                                                              dst_port=None, length=None, prime=False,
                                                              skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 UDP Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_udp(rx_packet_name, dst_port, src_port)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_udp_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          src_port=None, dst_port=None, length=None,
                                                                          prime=False, skip_config=False,
                                                                          filter_list=True, threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 UDP Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_udp_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              src_port=None, dst_port=None, length=None,
                                                                              prime=False, skip_config=False,
                                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [src_port]          - packet Source UDP Port  (Ex: 66)
        [dst_port]          - packet Destination UDP Port  (Ex: 6)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 UDP Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_udp(tx_packet_name, src_port, dst_port)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2UdpIpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_udp(rx_packet_name, dst_port, src_port)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_fragment_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                               vlan_tpid_list=None, sip=None, dip=None, frag=None,
                                                               length=None, prime=False, skip_config=False,
                                                               filter_list=True, threshold=0,
                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Fragment Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_fragment_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, vlan_id_list=None,
                                                                   vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                   dip=None, frag=None, length=None, prime=False,
                                                                   skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Fragment Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_fragment_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac,
                                                                               vlan_id_list=None, vlan_prio_list=None,
                                                                               vlan_tpid_list=None, sip=None, dip=None,
                                                                               frag=None, length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Fragment Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_fragment_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   vlan_id_list=None,
                                                                                   vlan_prio_list=None,
                                                                                   vlan_tpid_list=None, sip=None,
                                                                                   dip=None, frag=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [frag]             - packet Fragment Offset
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Fragment Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_frag_offset=frag)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_fragment_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                               vlan_tpid_list=None, sip=None, dip=None, length=None,
                                                               prime=False, skip_config=False, filter_list=True,
                                                               threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Fragment Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_fragment_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, vlan_id_list=None,
                                                                   vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                   dip=None, length=None, prime=False,
                                                                   skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Fragment Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip)
                tpk.set_ipv6_fragment(rx_packet_name)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_fragment_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac,
                                                                               vlan_id_list=None, vlan_prio_list=None,
                                                                               vlan_tpid_list=None, sip=None, dip=None,
                                                                               length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Fragment Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_fragment_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   vlan_id_list=None,
                                                                                   vlan_prio_list=None,
                                                                                   vlan_tpid_list=None, sip=None,
                                                                                   dip=None, length=None, prime=False,
                                                                                   skip_config=False, filter_list=True,
                                                                                   threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Fragment Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip)
            tpk.set_ipv6_fragment(tx_packet_name)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip)
            tpk.set_ipv6_fragment(rx_packet_name)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_ttl_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, ttl=None,
                                                          length=None, prime=False, skip_config=False, filter_list=True,
                                                          threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 TTL Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_ttl_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, ttl=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 TTL Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_ttl_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          ttl=None, length=None, prime=False,
                                                                          skip_config=False, filter_list=True,
                                                                          threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 TTL Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_ttl_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              ttl=None, length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [ttl]             - packet TTL
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 TTL Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_ttl=ttl)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_hop_limit_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                src_mac, dst_mac, vlan_id_list=None,
                                                                vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                dip=None, hop_limit=None, length=None, prime=False,
                                                                skip_config=False, filter_list=True, threshold=0,
                                                                packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Hop Limit Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_hop_limit_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                    src_mac, dst_mac, vlan_id_list=None,
                                                                    vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                    dip=None, hop_limit=None, length=None, prime=False,
                                                                    skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Hop Limit Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_hop_limit_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                packet_rate, src_mac, dst_mac,
                                                                                vlan_id_list=None, vlan_prio_list=None,
                                                                                vlan_tpid_list=None, sip=None, dip=None,
                                                                                hop_limit=None, length=None,
                                                                                prime=False, skip_config=False,
                                                                                filter_list=True, threshold=0,
                                                                                packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Hop Limit Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_hop_limit_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                    packet_rate, src_mac, dst_mac,
                                                                                    vlan_id_list=None,
                                                                                    vlan_prio_list=None,
                                                                                    vlan_tpid_list=None, sip=None,
                                                                                    dip=None, hop_limit=None,
                                                                                    length=None, prime=False,
                                                                                    skip_config=False, filter_list=True,
                                                                                    threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [hop_limit]             - packet Hop Limit
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Hop Limit Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_hop_limit=hop_limit)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_tos_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                          dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                          vlan_tpid_list=None, sip=None, dip=None, tos=None,
                                                          length=None, prime=False, skip_config=False, filter_list=True,
                                                          threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 ToS Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_tos_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate, src_mac,
                                                              dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                              vlan_tpid_list=None, sip=None, dip=None, tos=None,
                                                              length=None, prime=False, skip_config=False,
                                                              filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 ToS Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_tos_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                          packet_rate, src_mac, dst_mac,
                                                                          vlan_id_list=None, vlan_prio_list=None,
                                                                          vlan_tpid_list=None, sip=None, dip=None,
                                                                          tos=None, length=None, prime=False,
                                                                          skip_config=False, filter_list=True,
                                                                          threshold=0,
                                                                          packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 ToS Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_tos_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                              packet_rate, src_mac, dst_mac,
                                                                              vlan_id_list=None, vlan_prio_list=None,
                                                                              vlan_tpid_list=None, sip=None, dip=None,
                                                                              tos=None, length=None, prime=False,
                                                                              skip_config=False, filter_list=True,
                                                                              threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [tos]             - packet TOS
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 ToS Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_tos=tos)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_traffic_class_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                    src_mac, dst_mac, vlan_id_list=None,
                                                                    vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                    dip=None, traffic_class=None, length=None,
                                                                    prime=False, skip_config=False, filter_list=True,
                                                                    threshold=0, packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Traffic Class Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_traffic_class_frames_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                        packet_rate, src_mac, dst_mac,
                                                                        vlan_id_list=None, vlan_prio_list=None,
                                                                        vlan_tpid_list=None, sip=None, dip=None,
                                                                        traffic_class=None, length=None, prime=False,
                                                                        skip_config=False, filter_list=True,
                                                                        threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Traffic Class Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_traffic_class_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                    packet_rate, src_mac, dst_mac,
                                                                                    vlan_id_list=None,
                                                                                    vlan_prio_list=None,
                                                                                    vlan_tpid_list=None, sip=None,
                                                                                    dip=None, traffic_class=None,
                                                                                    length=None, prime=False,
                                                                                    skip_config=False, filter_list=True,
                                                                                    threshold=0,
                                                                                    packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Traffic Class Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_traffic_class_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                        num_packets, packet_rate,
                                                                                        src_mac, dst_mac,
                                                                                        vlan_id_list=None,
                                                                                        vlan_prio_list=None,
                                                                                        vlan_tpid_list=None, sip=None,
                                                                                        dip=None, traffic_class=None,
                                                                                        length=None, prime=False,
                                                                                        skip_config=False,
                                                                                        filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [traffic_class]             - packet Traffic Class
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Traffic Class Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_traffic_class=traffic_class)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv4_protocol_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                               src_mac, dst_mac, vlan_id_list=None, vlan_prio_list=None,
                                                               vlan_tpid_list=None, sip=None, dip=None, proto=None,
                                                               length=None, prime=False, skip_config=False,
                                                               filter_list=True, threshold=0,
                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Protocol Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_protocol_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                   src_mac, dst_mac, vlan_id_list=None,
                                                                   vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                   dip=None, proto=None, length=None, prime=False,
                                                                   skip_config=False, filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Protocol Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv4_protocol_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                               packet_rate, src_mac, dst_mac,
                                                                               vlan_id_list=None, vlan_prio_list=None,
                                                                               vlan_tpid_list=None, sip=None, dip=None,
                                                                               proto=None, length=None, prime=False,
                                                                               skip_config=False, filter_list=True,
                                                                               threshold=0,
                                                                               packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv4 Protocol Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv4_protocol_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port, num_packets,
                                                                                   packet_rate, src_mac, dst_mac,
                                                                                   vlan_id_list=None,
                                                                                   vlan_prio_list=None,
                                                                                   vlan_tpid_list=None, sip=None,
                                                                                   dip=None, proto=None, length=None,
                                                                                   prime=False, skip_config=False,
                                                                                   filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv4 Address (Ex: 1.2.3.4)
        [dip]               - packet Destination IPv4 Address (Ex: 1.2.3.4)
        [proto]             - packet Protocol (Ex: 45)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv4 Protocol Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(tx_packet_name, dip, sip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV4VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv4(rx_packet_name, sip, dip, ip_proto=proto)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

    def transmit_qinq_ipv6_next_header_frames_and_verify_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                  src_mac, dst_mac, vlan_id_list=None,
                                                                  vlan_prio_list=None, vlan_tpid_list=None, sip=None,
                                                                  dip=None, next_header=None, length=None, prime=False,
                                                                  skip_config=False, filter_list=True, threshold=0,
                                                                  packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Next Header Frames and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_next_header_frames_and_verify_not_received(self, tx_port, rx_port, num_packets, packet_rate,
                                                                      src_mac, dst_mac, vlan_id_list=None,
                                                                      vlan_prio_list=None, vlan_tpid_list=None,
                                                                      sip=None, dip=None, next_header=None, length=None,
                                                                      prime=False, skip_config=False, filter_list=True,
                                                                      threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Next Header Frames and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port if prime is selected
            if prime:
                tsck.remove_all_streams_from_port(rx_port)
                tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
                tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
                tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
                tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
                self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                            rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)

    def transmit_qinq_ipv6_next_header_frames_bidirectionally_and_verify_received(self, tx_port, rx_port, num_packets,
                                                                                  packet_rate, src_mac, dst_mac,
                                                                                  vlan_id_list=None,
                                                                                  vlan_prio_list=None,
                                                                                  vlan_tpid_list=None, sip=None,
                                                                                  dip=None, next_header=None,
                                                                                  length=None, prime=False,
                                                                                  skip_config=False, filter_list=True,
                                                                                  threshold=0,
                                                                                  packet_inspection_type="random 5"):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification
        [packet_inspection_type] - which packets to inspect [random 5, all]

        Transmit QinQ IPv6 Next Header Frames Bidirectionally and Verify Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_received(tx_port, rx_port, tx_packet_name, num_packets, threshold, packet_inspection_type)
        self._verify_packets_received(rx_port, tx_port, rx_packet_name, num_packets, threshold, packet_inspection_type)

    def transmit_qinq_ipv6_next_header_frames_bidirectionally_and_verify_not_received(self, tx_port, rx_port,
                                                                                      num_packets, packet_rate, src_mac,
                                                                                      dst_mac, vlan_id_list=None,
                                                                                      vlan_prio_list=None,
                                                                                      vlan_tpid_list=None, sip=None,
                                                                                      dip=None, next_header=None,
                                                                                      length=None, prime=False,
                                                                                      skip_config=False,
                                                                                      filter_list=True, threshold=0):
        """
        Keyword Arguments:
        [tx_port]           - the device port to transfer on
        [rx_port]           - the device port to receive on
        [num_packets]       - the number of packets to send
        [packet_rate]       - the rate at which to send packets
        [src_mac]           - packet source mac address (Ex: 00:00:33:44:55:66)
        [dst_mac]           - packet destination mac address (Ex: 00:00:33:44:55:66)
        [vlan_id_list]      - packet vlan ID list (Ex: "${vlan_id_list}=  Create List  1000  2000")
        [vlan_prio_list]    - packet priority list (Ex: "${vlan_prio_list}=  Create List  1  5")
        [vlan_tpid_list]    - packet vlan protocol id list (Ex: "${vlan_tpid_list}=  Create List  0x88a8  0x8100")
        [sip]               - packet Source IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [dip]               - packet Destination IPv6 Address (Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
        [next_header]             - packet Next Header (Ex: 10)
        [length]            - packet length
        [prime]             - prime the connection with a few packets from both ports
        [skip_config]       - skip configuring the stream
        [filter_list]       - filters to use on the capture port [True = DA/SA filter]
        [threshold]         - threshold value for the verification

        Transmit QinQ IPv6 Next Header Frames Bidirectionally and Verify NOT Received
        """
        tx_packet_name = "tx_packet"
        rx_packet_name = "rx_packet"
        if not skip_config:
            # create the packet on tx_port
            tsck = TrafficStreamConfigurationKeywords()
            tsck.remove_all_streams_from_port(tx_port)
            tpk = TrafficPacketCreationKeywords()
            tpk.create_packet(tx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(tx_packet_name, dst_mac, src_mac)
            tpk.set_vlan_stack_tag(tx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(tx_packet_name, dip, sip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(tx_port, tx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)

            # create the packet on rx_port
            tsck.remove_all_streams_from_port(rx_port)
            tpk.create_packet(rx_packet_name, "Ethernet2IpV6VlanStackPacket", length=length)
            tpk.set_ethernet2(rx_packet_name, src_mac, dst_mac)
            tpk.set_vlan_stack_tag(rx_packet_name, vlan_id_list, vlan_prio_list, vlan_tpid_list)
            tpk.set_ipv6(rx_packet_name, sip, dip, ipv6_next_header=next_header)
            self._configure_packet_on_port_single_burst(rx_port, rx_packet_name, skip_config, count=num_packets,
                                                        rate=packet_rate)
        if prime:
            self._prime(tx_port, rx_port)
        rx_filter_list = self._normalize_filter(filter_list, dst_mac, src_mac)
        self._start_capture(tx_port, rx_port, rx_filter_list)
        tx_filter_list = self._normalize_filter(filter_list, src_mac, dst_mac)
        self._start_capture(rx_port, tx_port, tx_filter_list)
        self._transmit_packet_on_port_single_burst(tx_port)
        self._transmit_packet_on_port_single_burst(rx_port)
        self._stop_capture(tx_port, rx_port)
        self._verify_packets_not_received(tx_port, rx_port, num_packets, threshold)
        self._verify_packets_not_received(rx_port, tx_port, num_packets, threshold)

        ######################################################################################
        # Auto generated end
        ######################################################################################

    @staticmethod
    def _prime(tx_port, rx_port):
        ttk = TrafficTransmitKeywords()
        ttk.start_transmit_on_port(tx_port)
        ttk.start_transmit_on_port(rx_port)
        ttk.start_transmit_on_port(tx_port)
        ttk.stop_transmit_on_port(tx_port)
        ttk.stop_transmit_on_port(rx_port)

    @staticmethod
    def _start_capture(tx_port, rx_port, filter_list):
        tck = TrafficCaptureKeywords()
        if filter_list:
            if "da" in filter_list:
                tck.configure_capture_da1(rx_port, filter_list["da"])
            if "sa" in filter_list:
                tck.configure_capture_sa1(rx_port, filter_list["sa"])
        # start capture on rx_port
        tck.start_capture_on_port(rx_port)
        # clear statistics on rx_port
        tck.clear_port_statistics(rx_port)
        # clear statistics on tx_port
        tck.clear_port_statistics(tx_port)

    @staticmethod
    def _stop_capture(tx_port, rx_port):
        tck = TrafficCaptureKeywords()
        tck.stop_capture_on_port(rx_port)
        tck.stop_capture_on_port(tx_port)

    @staticmethod
    def _configure_packet_on_port_single_burst(tx_port, packet_name, skip_config=False,
                                               stream_number=1, count=100, rate=100, unit="pps"):
        #     Remove All Streams from Port        ${tgen_port}
        #     Configure Stream Packet             ${tgen_port}  ${stream_number}  ${packet_name}
        #     Configure Stream Rate               ${tgen_port}  ${stream_number}  ${rate}
        #     Configure Stream Unit               ${tgen_port}  ${stream_number}  ${unit}
        #     Configure Stream Count              ${tgen_port}  ${stream_number}  ${count}
        #     Configure Stream Mode Single Burst  ${tgen_port}  ${stream_number}
        #     Add Stream to Port                  ${tgen_port}  ${stream_number}
        if not skip_config:
            tsck = TrafficStreamConfigurationKeywords()
            tsck.configure_stream_packet(tx_port, stream_number, packet_name)
            tsck.configure_stream_rate(tx_port, stream_number, rate)
            tsck.configure_stream_unit(tx_port, stream_number, unit)
            tsck.configure_stream_count(tx_port, stream_number, count)
            tsck.configure_stream_mode_single_burst(tx_port, stream_number)
            tsck.add_stream_to_port(tx_port, stream_number)

    @staticmethod
    def _transmit_packet_on_port_single_burst(tx_port, max_wait=60):
        #     Start Transmit on Port and Wait     ${tgen_port}  ${max_wait}
        ttk = TrafficTransmitKeywords()
        ttk.start_transmit_on_port_and_wait(tx_port, max_wait)

    @staticmethod
    def _verify_packets_received(tx_port, rx_port, packet_name, num_packets, threshold,
                                 packet_inspection_type="random 5"):
        # Get Captured Count                      ${rx_port}
        # Stat Value Should be Plus or Minus      ${rx_port}  100  5
        # Get Tx Count                            ${tx_port}
        # Stat Value Should be Equal              ${tx_port}  100
        # Capture Inspection Random List          ${rx_port}  rx_packet  5
        tsk = TrafficStatisticsKeywords()
        tpik = TrafficPacketInspectionKeywords()

        tsk.get_captured_count(rx_port)
        tsk.stat_value_should_be_plus_or_minus(rx_port, num_packets, threshold)
        tsk.get_tx_count(tx_port)
        tsk.stat_value_should_be_equal(tx_port, num_packets)
        inspection = packet_inspection_type.split(" ")
        if inspection[0] == "random":
            tpik.capture_inspection_random_list(rx_port, packet_name, inspection[1])
        elif inspection[0] == "all":
            tpik.capture_inspection_all(rx_port, packet_name)
        else:
            tpik.capture_inspection_random_list(rx_port, packet_name, 5)

    @staticmethod
    def _verify_packets_not_received(tx_port, rx_port, num_packets, threshold):
        # Get Captured Count                      ${rx_port}
        # Stat Value Should be Plus or Minus      ${rx_port}  0  5
        # Get Tx Count                            ${tx_port}
        # Stat Value Should be Equal              ${tx_port}  0
        tsk = TrafficStatisticsKeywords()

        tsk.get_captured_count(rx_port)
        tsk.stat_value_should_be_plus_or_minus(rx_port, 0, threshold)
        tsk.get_tx_count(tx_port)
        tsk.stat_value_should_be_equal(tx_port, num_packets)

    @staticmethod
    def _normalize_filter(filter_list, dst_mac, src_mac, swap_values=False):
        update_da_sa = False
        if filter_list is True and not isinstance(filter_list, dict):
            filter_list = {}
            update_da_sa = True
        if filter_list is not None and isinstance(filter_list, dict):
            if "dst" in filter_list:
                filter_list["da"] = filter_list.pop("dst")
            if "src" in filter_list:
                filter_list["sa"] = filter_list.pop("src")
            if swap_values:
                da = filter_list.pop("da") if "da" in filter_list else False
                sa = filter_list.pop("sa") if "sa" in filter_list else False
                if da:
                    filter_list["sa"] = da
                if sa:
                    filter_list["da"] = sa
                dip = filter_list.pop("dip") if "dip" in filter_list else False
                sip = filter_list.pop("sip") if "sip" in filter_list else False
                if dip:
                    filter_list["sip"] = dip
                if sip:
                    filter_list["dip"] = sip
                dport = filter_list.pop("dport") if "dport" in filter_list else False
                sport = filter_list.pop("sport") if "sport" in filter_list else False
                if dport:
                    filter_list["sport"] = dport
                if sport:
                    filter_list["dport"] = sport
            if update_da_sa:
                filter_list["da"] = dst_mac
                filter_list["sa"] = src_mac
        return filter_list
