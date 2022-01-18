from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.BaseClasses.TrafficKeywordBaseClass import TrafficKeywordBaseClass
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.PacketUtils.PacketDictionary import PacketDictionary
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.ConfigurationManagement.StreamConfigManager\
    import StreamConfigManager


class TrafficStreamConfigurationKeywords(TrafficKeywordBaseClass):
    _stream_configs = StreamConfigManager()
    _pkt_dict = PacketDictionary()

    def configure_stream_packet(self, ports, stream_numbers, packet_name, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [packet_name] - The name of the packet to apply to the stream.

        Configures a packet to a given stream.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.packet = packet_name

        return self._keyword_cleanup()

    def configure_stream_packet_collection(self, ports, collection_name, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [collection_name] - The name of the packet collection to use.

        Configures a packet collection onto a port. When using a packet collection it is expected that only
        one stream is configured. When a packet collection is applied any value applied using the
        "configure_stream_packet" keyword will be lost.

        When a stream configured with a packet collection is applied to a port the remaining configuration
        will be applied using stream ID 1.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            stream_config = self._stream_configs.get_stream_config(name_port_list, "1")
            stream_config.packet_collection = collection_name
            stream_config.packet = None

        return self._keyword_cleanup()

    def configure_collection_on_ports(self, ports, stream_number, collection_name, **kwargs):
        """
        Keyword Arguments:
        [traffic_gen_name] - The name of the traffic generator the port exists on.
        [ports] - This is expected to be a list of ports. Each port will be configured with a different packet
                  from the collection (in order).
        [stream_number] - The stream number the configuration should be applied to.
        [collection_name] - The name of the packet collection to use.
        """
        ports = self._validate_tgen_name_port_list(ports)

        packet_collection = self._pkt_dict.get_collection(collection_name)

        self._init_keyword(**kwargs)

        if len(ports) <= len(packet_collection):
            for i in range(len(ports)):
                self.configure_stream_packet(ports[i], stream_number, packet_collection[i], log_keyword=False)
        else:
            self.logger.log_info("Can't apply " + str(len(packet_collection)) + " packets to " + str(len(ports)) +
                                 ".\n Number of packets must be greater than or equal to number of ports.")

        return self._keyword_cleanup()

    def configure_stream_rate(self, ports, stream_numbers, rate, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [rate] - The integer rate that should be applied to the stream.

        Configures the transmit rate of a given stream.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.rate = rate

        return self._keyword_cleanup()

    def configure_stream_count(self, ports, stream_numbers, count, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [count] - The number of packets that should be transmitted by the stream.

        Configures the number of packet a given stream should transmit.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.count = count

        return self._keyword_cleanup()

    def configure_stream_unit(self, ports, stream_numbers, unit, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [unit] - The unit that should be applied to the stream. Valid units are "pps", "bps", "kbps", "mbps",
                 "gbps", "percent", and "%".

        Configures the transmit unit for a given stream.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.unit = unit

        return self._keyword_cleanup()

    def configure_stream_mode_continuous(self, ports, stream_numbers, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.

        Configures the streams mode to continuous.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mode = self.config_constants.TRANSMIT_MODE_CONTINUOUS

        return self._keyword_cleanup()

    def configure_stream_mode_single_burst(self, ports, stream_numbers, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.

        Configures the streams mode to single burst.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mode = self.config_constants.TRANSMIT_MODE_SINGLE_BURST

        return self._keyword_cleanup()

    def configure_stream_mode_continuous_burst(self, ports, stream_numbers, inter_burst_gap=None,
                                               **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [inter_burst_gap] - Sets the delay in MS between each burst.

        Configures the streams mode to continuous burst.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mode = self.config_constants.TRANSMIT_MODE_CONTINUOUS_BURST
                stream_config.burst_gap = inter_burst_gap

        return self._keyword_cleanup()

    def configure_stream_mode_return_to_id(self, ports, stream_numbers, return_id, count=None,
                                           **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [return_id] - The stream ID to return to.
        [count] - Optional argument, sets how many times the stream should return to the configured Id.
                  if passed the mode will be set to return to id for count. If not set the mode will be
                  set to return to id (continuous).

        Configures the streams mode to either return to id or return to id for count if the count argument
        is provided.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)

                if count is None:
                    stream_config.mode = self.config_constants.TRANSMIT_MODE_RETURN_TO_ID
                else:
                    stream_config.mode = self.config_constants.TRANSMIT_MODE_RETURN_TO_ID_FOR_COUNT
                    stream_config.return_to_id_count = count

                stream_config.return_id = return_id

        return self._keyword_cleanup()

    def configure_stream_mode_advance(self, ports, stream_numbers, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.

        Configures the streams mode to advance.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mode = self.config_constants.TRANSMIT_MODE_NEXT

        return self._keyword_cleanup()

    def add_stream_to_port(self, ports, stream_number, clear_all_streams=False, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_number] - The stream configuration to load and apply to the port.
        [clear_all_streams] - If set to true all previously configured streams will be removed from the port
                              before configuring a new stream.

        Applies a stream configuration to a traffic generator port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            stream_dict = {}

            stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)

            if stream_config is None:
                self._determine_result(False, True, None,
                                       "No configuration found for port " + self.current_port + " stream number " +
                                       stream_number,**kwargs)
                return self._keyword_cleanup()

            if stream_config.count is not None:
                stream_dict[self.config_constants.PKTS_PER_BURST_CMD] = stream_config.count

            if stream_config.mode is not None:
                stream_dict[self.config_constants.TRANSMIT_MODE_CMD] = stream_config.mode

                if stream_config.mode == self.config_constants.TRANSMIT_MODE_CONTINUOUS_BURST:
                    if stream_config.burst_gap is not None:
                        stream_dict[self.config_constants.INTER_BURST_GAP_CMD] = stream_config.burst_gap
                elif (stream_config.mode == self.config_constants.TRANSMIT_MODE_RETURN_TO_ID or
                      stream_config.mode == self.config_constants.TRANSMIT_MODE_RETURN_TO_ID_FOR_COUNT):

                    stream_dict[self.config_constants.RETURN_TO_ID_CMD] = stream_config.return_id

                    if stream_config.mode == self.config_constants.TRANSMIT_MODE_RETURN_TO_ID_FOR_COUNT:
                        stream_dict[self.config_constants.LOOP_COUNT_CMD] = stream_config.return_to_id_count

            else:
                stream_dict[self.config_constants.TRANSMIT_MODE_CMD] = self.config_constants.TRANSMIT_MODE_CONTINUOUS

            if stream_config.unit is not None:
                if stream_config.rate is not None:
                    if stream_config.unit == "pps":
                        stream_dict[self.config_constants.RATE_PPS_CMD] = stream_config.rate
                    elif stream_config.unit == "bps":
                        stream_dict[self.config_constants.RATE_BPS_CMD] = stream_config.rate
                    elif stream_config.unit == "kbps":
                        stream_dict[self.config_constants.RATE_BPS_CMD] = stream_config.rate * 1000
                    elif stream_config.unit == "mbps":
                        stream_dict[self.config_constants.RATE_BPS_CMD] = stream_config.rate * 1000000
                    elif stream_config.unit == "gbps":
                        stream_dict[self.config_constants.RATE_BPS_CMD] = stream_config.rate * 1000000000
                    else:
                        stream_dict[self.config_constants.RATE_PERCENT_CMD] = stream_config.rate
            else:
                if stream_config.rate is not None:
                    stream_dict[self.config_constants.RATE_PPS_CMD] = stream_config.rate
                else:
                    stream_dict[self.config_constants.RATE_PPS_CMD] = 100

            if stream_config.packet is not None:
                if stream_config.mac_src_mode != self.config_constants.MAC_SRC_MODE_FIXED:
                    stream_dict[self.config_constants.MAC_SRC_MODE_CMD] = stream_config.mac_src_mode
                    if stream_config.mac_src_count is not None:
                        stream_dict[self.config_constants.MAC_SRC_COUNT_CMD] = stream_config.mac_src_count
                    if stream_config.mac_src_step is not None:
                        stream_dict[self.config_constants.MAC_SRC_STEP_CMD] = stream_config.mac_src_step
                    if stream_config.mac_src_mask is not None:
                        stream_dict[self.config_constants.MAC_SRC_MASK_CMD] = stream_config.mac_src_mask

                if stream_config.mac_dst_mode != self.config_constants.MAC_DST_MODE_FIXED:
                    stream_dict[self.config_constants.MAC_DST_MODE_CMD] = stream_config.mac_dst_mode
                    if stream_config.mac_dst_count is not None:
                        stream_dict[self.config_constants.MAC_DST_COUNT_CMD] = stream_config.mac_dst_count
                    if stream_config.mac_dst_step is not None:
                        stream_dict[self.config_constants.MAC_DST_STEP_CMD] = stream_config.mac_dst_step
                    if stream_config.mac_dst_mask is not None:
                        stream_dict[self.config_constants.MAC_DST_MASK_CMD] = stream_config.mac_dst_mask

                if stream_config.ip_src_mode != self.config_constants.IP_SRC_MODE_FIXED:
                    stream_dict[self.config_constants.IP_SRC_MODE_CMD] = stream_config.ip_src_mode
                    if stream_config.ip_src_count is not None:
                        stream_dict[self.config_constants.IP_SRC_COUNT_CMD] = stream_config.ip_src_count
                    if stream_config.ip_src_mask is not None:
                        stream_dict[self.config_constants.IP_SRC_STEP_CMD] = stream_config.ip_src_mask

                if stream_config.ip_dst_mode != self.config_constants.IP_DST_MODE_FIXED:
                    stream_dict[self.config_constants.IP_DST_MODE_CMD] = stream_config.ip_dst_mode
                    if stream_config.ip_dst_count is not None:
                        stream_dict[self.config_constants.IP_DST_COUNT_CMD] = stream_config.ip_dst_count
                    if stream_config.ip_dst_mask is not None:
                        stream_dict[self.config_constants.IP_DST_STEP_CMD] = stream_config.ip_dst_mask

                self.traffic_gen.configure_stream_using_packet(self.current_port, int(stream_number),
                                                               stream_config.packet, clear_all_streams,
                                                               options=stream_dict)
                self._stream_configs.clear_stream(name_port_list, stream_number)
            elif stream_config.packet_collection is not None:
                self.traffic_gen.configure_streams_using_packets(self.current_port, stream_config.packet_collection,
                                                                 options=stream_dict)
                self._stream_configs.clear_stream(name_port_list, stream_number)
            else:
                self._determine_result(False, True, None, "No packet configured, stream not applied.",**kwargs)
        return self._keyword_cleanup()

    def add_all_streams_to_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Applies all previously configured streams to a traffic generator port.

        Calling this function will clear the internal stream configuration, the configuration will still
        be applied to the port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            stream_configs = self._stream_configs.get_all_streams_for_port(name_port_list)

            for stream_config in stream_configs:
                self.add_stream_to_port(name_port_list, stream_config.stream_number, log_keyword=False, **kwargs)

            self._stream_configs.clear_port_streams(name_port_list)
        return self._keyword_cleanup()

    def remove_all_streams_from_port(self, ports, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.

        Removes all streams configured on a given traffic generator port also clears internal stream configurations.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            self.traffic_gen.clear_all_streams(self.current_port)
            self._stream_configs.clear_port_streams(name_port_list)

        return self._keyword_cleanup()

    def remove_stream_from_port(self, ports, stream_number, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_number] - the stream to remove Example: 1

        Removes a stream configured on a given traffic generator port.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.traffic_gen.clear_stream(self.current_port, stream_number)
        return self._keyword_cleanup()

    def configure_stream_mac_src_mode_increment(self, ports, stream_numbers, count, step="1", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [count] - How many times the source mac should be incremented.
        [step] - How much to increment each source mac.

        Configures the source mac to increment by <step>, <count> times.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mac_src_mode = self.config_constants.MAC_SRC_MODE_INCREMENT
                stream_config.mac_src_count = count
                stream_config.mac_src_step = step

        return self._keyword_cleanup()

    def configure_stream_mac_src_mode_random(self, ports, stream_numbers, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [mask] - Which part of the mac address should be masked. Only the unmasked portions will be randomized.
                 The mask value should be formatted as follows "XX XX XX XX 00 00" where X is masked an 0 is unmasked.

        Configures the source mac to be randomized for any unmasked portion of the address.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mac_src_mode = self.config_constants.MAC_SRC_MODE_RANDOM
                stream_config.mac_src_mask = mask

        return self._keyword_cleanup()

    def configure_stream_mac_dst_mode_increment(self, ports, stream_numbers, count, step="1", **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [count] - How many times the destination mac should be incremented.
        [step] - How much to increment each destination mac.

        Configures the destination mac to increment by <step>, <count> times.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mac_dst_mode = self.config_constants.MAC_DST_MODE_INCREMENT
                stream_config.mac_dst_count = count
                stream_config.mac_dst_step = step

        return self._keyword_cleanup()

    def configure_stream_mac_dst_mode_random(self, ports, stream_numbers, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [mask] - Which part of the mac address should be masked. Only the unmasked portions will be randomized.
                 The mask value should be formatted as follows "XX XX XX XX 00 00" where X is masked an 0 is unmasked.

        Configures the destination mac to be randomized for any unmasked portion of the address.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.mac_dst_mode = self.config_constants.MAC_DST_MODE_RANDOM
                stream_config.mac_dst_mask = mask

        return self._keyword_cleanup()

    def configure_stream_ip_src_mode_increment(self, ports, stream_numbers, count, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [count] - How many times the source IP should be incremented.

        Configures the source IP to increment <count> times.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.ip_src_mode = self.config_constants.IP_SRC_MODE_INCREMENT
                stream_config.ip_src_count = count
                stream_config.ip_src_mask = mask

        return self._keyword_cleanup()

    def configure_stream_ip_src_mode_random(self, ports, stream_numbers, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [mask] - Which part of the IP address should be masked. Only the unmasked portions will be randomized.
                 The mask value should be formatted as follows "255.255.0.0".

        Configures the source IP to be randomized for any unmasked portion of the address.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.ip_src_mode = self.config_constants.MAC_DST_MODE_RANDOM
                stream_config.ip_src_mask = mask

        return self._keyword_cleanup()

    def configure_stream_ip_dst_mode_increment(self, ports, stream_numbers, count, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [count] - How many times the destination IP should be incremented.

        Configures the destination IP to increment <count> times.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.ip_dst_mode = self.config_constants.IP_DST_MODE_INCREMENT
                stream_config.ip_dst_count = count
                stream_config.ip_dst_mask = mask

        return self._keyword_cleanup()

    def configure_stream_ip_dst_mode_random(self, ports, stream_numbers, mask=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [stream_numbers] - The stream number(s) the configuration should be applied to.
        [mask] - Which part of the IP address should be masked. Only the unmasked portions will be randomized.
                 The mask value should be formatted as follows "255.255.0.0".

        Configures the destination IP to be randomized for any unmasked portion of the address.
        """
        ports = self._validate_tgen_name_port_list(ports)
        stream_numbers = ListUtils.convert_to_list(stream_numbers)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)

            for stream_number in stream_numbers:
                stream_config = self._stream_configs.get_stream_config(name_port_list, stream_number)
                stream_config.ip_dst_mode = self.config_constants.MAC_DST_MODE_RANDOM
                stream_config.ip_dst_mask = mask

        return self._keyword_cleanup()
