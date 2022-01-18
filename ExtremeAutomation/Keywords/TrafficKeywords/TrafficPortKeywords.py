from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Library.Device.TrafficGeneration.Apis.HltApi.HltapiInterfaceConfigApi import \
    InterfaceConfigConstants


class TrafficPortKeywords(TrafficKeywordBaseClass):

    def reset_port_to_factory_defaults(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Resets the given traffic device's port to factory defaults.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.take_port_ownership(name_port_list, reset=True, log_keyword=False)

    def take_port_ownership(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Takes ownership of the given traffic generator port(s).
        """
        # Create a list of keyword results
        kw_results = []
        if ports:
            ports = self._validate_tgen_name_port_list(ports)

            self._init_keyword(**kwargs)
            reset = kwargs.get("reset", True)
            autonegotiate = kwargs.get("autonegotiation", False)
            duplex = kwargs.get("duplex", False)
            speed = kwargs.get("speed", False)
            wait_for_link = kwargs.get("wait_for_link", False)

            for name_port_list in ports:
                self._get_traffic_generator_info(name_port_list)
                options = {}
                if autonegotiate:
                    if str(autonegotiate).lower() == "false" or str(autonegotiate).lower() == "0":
                        options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "0"
                    else:
                        options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "1"
                else:
                    options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "1"
                if duplex:
                    options[InterfaceConfigConstants.DUPLEX_CMD] = duplex
                else:
                    options[InterfaceConfigConstants.DUPLEX_CMD] = InterfaceConfigConstants.DUPLEX_AUTO
                if speed:
                    speed_parts = speed.split(" ")
                    speed_settings = []
                    for sp in speed_parts:
                        if sp == "10":
                            sp = InterfaceConfigConstants.SPEED_ETHER10
                        elif sp == "100":
                            sp = InterfaceConfigConstants.SPEED_ETHER100
                        elif sp == "1000":
                            sp = InterfaceConfigConstants.SPEED_ETHER1000
                        speed_settings.append(sp)
                    options[InterfaceConfigConstants.SPEED_CMD] = " ".join(speed_settings)
                else:
                    options[InterfaceConfigConstants.SPEED_CMD] = InterfaceConfigConstants.SPEED_AUTO
                kw_result = self.traffic_gen.take_port_ownership(self.traffic_gen.chassis_ip,
                                                                 self.traffic_gen.username, self.current_port,
                                                                 reset, options)
                if kw_result:
                    kw_results.extend(kw_result)

                # if phy_mode is None, the port speed/duplex advertisement is gone besides gig
                if self.phy_mode and \
                        self.traffic_gen.vendor.lower() != self.traffic_gen_constants.JETS_CHASSIS.lower():
                    self.traffic_gen.set_port_phy_mode(self.current_port, self.phy_mode)

                if wait_for_link:
                    self.traffic_gen.wait_for_has_link(self.current_port)

                # if self.traffic_gen.vendor.lower() == self.traffic_gen_constants.IXIA_CHASSIS.lower():
                #     kw_result = self.traffic_gen.enable_qos_stats(self.current_port, False)
                #     if kw_result:
                #         kw_results.extend(kw_result)

                # This was added for a card issue and not an Ixia version issue.
                # if phy_mode is set, IxTclHcl 6.70 wipes out
                # capture mode (captures packets)/wide packet group (give aggregate stats).
                if self.traffic_gen.vendor.lower() == self.traffic_gen_constants.IXIA_CHASSIS.lower():
                    if self.traffic_gen.get_version("IxTclHal").replace(" ", "") == "6.70":
                        self.traffic_gen.set_capture_mode(self.current_port,
                                                          "{" + InterfaceConfigConstants.PORT_RX_MODE_CAPTURE + " " +
                                                          InterfaceConfigConstants.PORT_RX_MODE_WIDE_PACKET_GROUP + "}")
        else:
            self.logger.log_info("Traffic Generator Portlist is empty. No ports reset.")
        self.kw_results.extend(kw_results)
        return self._keyword_cleanup()

    def clear_port_ownership(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Takes ownership of the given traffic generator port(s).
        """
        # Create a list of keyword results
        kw_results = []
        if ports:
            ports = self._validate_tgen_name_port_list(ports)

            self._init_keyword(**kwargs)
            reset = kwargs.get("reset", True)
            autonegotiate = kwargs.get("autonegotiation", False)
            duplex = kwargs.get("duplex", False)
            speed = kwargs.get("speed", False)

            for name_port_list in ports:
                self._get_traffic_generator_info(name_port_list)
                options = {}
                if autonegotiate:
                    if str(autonegotiate).lower() == "false" or str(autonegotiate).lower() == "0":
                        options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "0"
                    else:
                        options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "1"
                else:
                    options[InterfaceConfigConstants.AUTONEGOTIATION_CMD] = "1"
                if duplex:
                    options[InterfaceConfigConstants.DUPLEX_CMD] = duplex
                else:
                    options[InterfaceConfigConstants.DUPLEX_CMD] = InterfaceConfigConstants.DUPLEX_AUTO
                if speed:
                    speed_parts = speed.split(" ")
                    speed_settings = []
                    for sp in speed_parts:
                        if sp == "10":
                            sp = InterfaceConfigConstants.SPEED_ETHER10
                        elif sp == "100":
                            sp = InterfaceConfigConstants.SPEED_ETHER100
                        elif sp == "1000":
                            sp = InterfaceConfigConstants.SPEED_ETHER1000
                        speed_settings.append(sp)
                    options[InterfaceConfigConstants.SPEED_CMD] = " ".join(speed_settings)
                else:
                    options[InterfaceConfigConstants.SPEED_CMD] = InterfaceConfigConstants.SPEED_AUTO
                kw_result = self.traffic_gen.clear_port_ownership(self.traffic_gen.chassis_ip,
                                                                  self.current_port, reset, options)
                if kw_result:
                    kw_results.extend(kw_result)
        else:
            self.logger.log_info("Traffic Generator Portlist is empty. No ports reset.")
        self.kw_results.extend(kw_results)
        return self._keyword_cleanup()

    def set_port_duplex(self, ports, duplex, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [duplex]
        Set the duplex of the given traffic generator port(s).
        """
        # Create a list of keyword results
        if ports:
            ports = self._validate_tgen_name_port_list(ports)

            self._init_keyword(**kwargs)

            for name_port_list in ports:
                self._get_traffic_generator_info(name_port_list)
                self.traffic_gen.set_port_duplex(self.current_port, duplex)
        else:
            self.logger.log_info("Traffic Generator Portlist is empty. No ports reset.")
        # self.kw_results.extend(kw_results)
        return self._keyword_cleanup()

    def set_port_speed(self, ports, speed, disable_autonegotiation=False, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [speed]
        [disable_autonegotiation]
        Set the speed of the given traffic generator port(s).
        """
        # Create a list of keyword results
        if ports:
            ports = self._validate_tgen_name_port_list(ports)

            self._init_keyword(**kwargs)

            for name_port_list in ports:
                self._get_traffic_generator_info(name_port_list)
                self.traffic_gen.set_port_speed(self.current_port, speed, disable_autonegotiation)
        else:
            self.logger.log_info("Traffic Generator Portlist is empty. No ports reset.")
        # self.kw_results.extend(kw_results)
        return self._keyword_cleanup()

    def set_port_autonegotation(self, ports, autonegotiation, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [autonegotiation]
        Set the autonegotiation of the given traffic generator port(s).
        """
        # Create a list of keyword results
        if ports:
            ports = self._validate_tgen_name_port_list(ports)

            self._init_keyword(**kwargs)

            for name_port_list in ports:
                self._get_traffic_generator_info(name_port_list)
                self.traffic_gen.set_port_autonegotiation(self.current_port, autonegotiation)
        else:
            self.logger.log_info("Traffic Generator Portlist is empty. No ports reset.")
        # self.kw_results.extend(kw_results)
        return self._keyword_cleanup()

    def set_port_to_qos_mode(self, ports, mode="vlan", qos_byte_offset=None, pattern_match_offset=None,
                             pattern_match=None, pattern_match_mask=None, **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [mode] - The QOS mode that should be used. Valid options are "vlan", "iptos", "snaptos", and "custom".
                 Default and invalid options will be set to "vlan".
        [qos_byte_offset] - Byte offset where QOS information is located.
        [pattern_match_offset] - Byte offset of the pattern to match before checking for QOS info.
        [pattern_match] - The pattern that must be matched before checking for QOS info.
        [pattern_match_mask] - The mask that is applied to the pattern match.

        Sets a given ports statistic mode to QOS.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        if mode.lower() in ["iptos", "tos", "ip-tos", "ip_tos"]:
            mode = InterfaceConfigConstants.QOS_PACKET_TYPE_ETHERNET
        elif mode.lower() in ["snaptos", "snap-tos", "snap_tos"]:
            mode = InterfaceConfigConstants.QOS_PACKET_TYPE_IP_SNAP
        elif mode.lower() == "custom":
            mode = InterfaceConfigConstants.QOS_PACKET_TYPE_CUSTOM
        else:
            mode = InterfaceConfigConstants.QOS_PACKET_TYPE_VLAN

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            if mode != InterfaceConfigConstants.QOS_PACKET_TYPE_CUSTOM:
                self.traffic_gen.set_qos_mode(self.current_port, mode)
            else:
                self.traffic_gen.set_qos_mode(self.current_port, mode, qos_byte_offset, pattern_match_offset,
                                              pattern_match, pattern_match_mask)
            self.traffic_gen.wait_for_has_link(self.current_port)
        return self._keyword_cleanup()

    def set_port_to_normal_mode(self, ports, **kwargs):
        """
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Sets a given ports statistic mode to QOS.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.enable_qos_stats(self.current_port, False)

    def configure_arp_resolution(self, port, first_ip, start_mac, prefix_len, count, one_to_one=True,
                                 resolve_learn="both", retries="3", vlan=False, vlan_id=None, **kwargs):
        """
        [port]          - This must be a dictionary which contains the name of the traffic generator and the
                          traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [first_ip]      - The first IP address to resolve ARPs on.
        [start_mac]     - The first MAC address matched to the first IP address.
        [prefix_len]    - The prefix length of the IP subnet.
        [count]         - How many IPs, counted up from the first, to resolve ARP.
        [one-to-one]    - (Default=True) MAC to IP mapping, one IP per MAC or a single MAC for all IPs.
        [resolve_learn] - (Default=both) This argument sets the TGen port to learn, resolve, or both behaviors.
        [retries]       - (Default=3) Number of ARP retires when ARP times out.
        [vlan]          - (Default=False) Set True for VLAN tagged frames.
        [vlan_id]       - (Default=None) The VLAN ID if Tags are enabled.

        Configures the traffic generator port to reply to ARPs for the specified IP Address(s).
        """
        self._init_keyword(**kwargs)

        mapping = "oneIpToOneMAC" if one_to_one is True else "manyIpToOneMAC"
        start_ip = StringUtils.normalize_value(first_ip, PacketConstants.IPV4_ADDRESS)

        if resolve_learn.lower() == "learn":
            learning = "arpLearnOnly"
        elif resolve_learn.lower() == "resolve":
            learning = "arpGatewayOnly"
        else:
            learning = "arpGatewayAndLearn"

        self._get_traffic_generator_info(port)
        self.traffic_gen.configure_arp(self.current_port, start_ip, start_mac, count, "0.0.0.0", mapping_option=mapping,
                                       arp_for=learning, arp_retires=retries, netmask=prefix_len, vlan_enable=vlan,
                                       vlan_id=vlan_id, clear_settings_first=False)

    def ping(self, port_string, source_ip, destination_ip, timeout_secs=30, ping_count=3, **kwargs):
        """
        [port_string] This must be a dictionary which contains the name of the traffic generator and the
                      traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [source_ip]
        [destination_ip]
        [timeout_secs]
        [ping_count]
        [kwargs]
        :return:
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(**kwargs)
        inspection_result = self.traffic_gen.ping(self.current_port, source_ip, destination_ip, timeout_secs,
                                                  ping_count)
        self._determine_result(inspection_result, True, **kwargs)
        return self._keyword_cleanup()

    def verify_arp_entry(self, port_string, expected_ip, expected_mac, **kwargs):
        """
        [port_string] This must be a dictionary which contains the name of the traffic generator and the
                      traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_ip]
        [expected_mac]
        [kwargs]
        :return:
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(**kwargs)
        inspection_result = self.traffic_gen.verify_arp_entry(self.current_port, expected_ip, expected_mac)
        self._determine_result(inspection_result, True, **kwargs)
        return self._keyword_cleanup()

    def clear_arp_table(self, port_string, ip_address=None, vlan_id=None, **kwargs):
        """
        [port_string] This must be a dictionary which contains the name of the traffic generator and the
                      traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [ip_address] entry to clear. if None clears all.
        [vlan_id]
        [kwargs]
        :return:
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(**kwargs)
        self.traffic_gen.clear_arp_table(self.current_port, ip_address, vlan_id)
        return self._keyword_cleanup()

    def wait_for_ping(self, port_string, source_ip, destination_ip, max_wait_in_sec=60,
                      **kwargs):
        """
        [port_string] This must be a dictionary which contains the name of the traffic generator and the
                      traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [source_ip]
        [destination_ip]
        [timeout_secs]
        [ping_count]
        [max_wait_in_sec]
        [kwargs]
        :return:
        """
        self._get_traffic_generator_info(port_string)
        self._init_keyword(**kwargs)
        inspection_result = self.traffic_gen.wait_for_ping(self.current_port, source_ip, destination_ip,
                                                           max_wait_in_sec * 1000)
        self._determine_result(inspection_result, True, **kwargs)
        return self._keyword_cleanup()
