from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementTlvUtils import NetworkElementTlvUtils
from ExtremeAutomation.Keywords.Utils.DeviceValueStorage import DeviceValueStorage
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.PacketInspectionUtils.PacketInspectionUtils \
    import PacketInspectionUtils


class TrafficPacketInspectionKeywords(PacketInspectionUtils):
    def __init__(self):
        super(TrafficPacketInspectionKeywords, self).__init__()
        self.device_storage = DeviceValueStorage()

    def capture_inspection_random_list(self, ports, expected_packet_name, number_to_check="1",
                                       check_all_fields=False, ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [number_to_check] - The number of random packets that will be inspected.
        [ignore_list] - A list of fields within the packet that should be ignored.

        This keyword inspects <number_to_check> packets which are randomly selected from the capture.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        number_to_check = int(number_to_check)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            self.get_capture_length(self.current_port)

            packet_check_list = NumberUtils.get_random_list(number_to_check, self.capture_length)
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)

            self._determine_result(inspection_result, True)
        return self._keyword_cleanup()

    def capture_inspection_specific_packet(self, ports, expected_packet_name, packet_number_to_check="1",
                                           check_all_fields=False, ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [number_to_check] - The number of random packets that will be inspected.
        [ignore_list] - A list of fields within the packet that should be ignored.

        This keyword inspects a single packet within the capture.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        packet_check_list = [int(packet_number_to_check)]

        if int(packet_number_to_check) < 1:
            raise Exception("Packet number to check must be >= 1.")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)

            self._determine_result(inspection_result, True,**kwargs)
        return self._keyword_cleanup()

    def capture_inspection_range(self, ports, expected_packet_name, start_index="1", end_index="1",
                                 check_all_fields=False, ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [number_to_check] - The number of random packets that will be inspected.
        [ignore_list] - A list of fields within the packet that should be ignored.

        This keyword inspects all packets in the range <start_index> to <end_index>.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        start_index = int(start_index)
        end_index = int(end_index)

        if int(start_index) < 1 or int(end_index) < 1:
            raise Exception("Start and ending indexes must be >= 1.")

        packet_check_list = range(start_index, end_index + 1)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)

            self._determine_result(inspection_result, True,**kwargs)
        return self._keyword_cleanup()

    def capture_inspection_packet_list(self, ports, expected_packet_name, packet_index_list="[1]",
                                       check_all_fields=False, ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [number_to_check] - The list of packets that should be inspected.
                            For example, ["1", "2", "3"], "(1, 2, 3)", or "1, 2, 3" would all be accepted.
        [ignore_list] - A list of fields within the packet that should be ignored.

        This keyword inspects all packet indexes within a given list.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        packet_check_list = StringUtils.normalize_list(packet_index_list)

        for i in packet_index_list:
            if int(i) == 0:
                raise Exception("All indexes in packet index list must be >= 1.")

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)

            self._determine_result(inspection_result, True,**kwargs)
        return self._keyword_cleanup()

    def capture_inspection_first_and_last(self, ports, expected_packet_name, check_all_fields=False,
                                          ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [check_all_fields] - By default the only fields that are inspected are the fields the user has
                             configured. If you want to check all fields regardless of user configuration
                             set this argument to True.
        [ignore_list] - A list of fields within the packet that should be ignored.
        [include_list] - A list of fields within the packet that should be checked.

        This keyword checks the first and last packet within a capture against an expected packet.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            packet_check_list = [1, self.get_capture_length(self.current_port)]
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)

            self._determine_result(inspection_result, True)
        return self._keyword_cleanup()

    def capture_inspection_all(self, ports, expected_packet_name, check_all_fields=False,
                               ignore_list=None, include_list=None, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [expected_packet_name] - The name of the previously created packet that will be used for comparison.
                                 If a packet object is provided instead, that will be used.
        [check_all_fields] - By default the only fields that are inspected are the fields the user has
                             configured. If you want to check all fields regardless of user configuration
                             set this argument to True.
        [ignore_list] - A list of fields within the packet that should be ignored.
        [include_list] - A list of fields within the packet that should be checked.

        This keyword checks all the packets captured against an expected packet.
        """
        ports = self._validate_tgen_name_port_list(ports)

        self._init_keyword(**kwargs)

        for name_port_list in ports:
            self._get_traffic_generator_info(name_port_list)
            packet_check_list = range(self.get_capture_length(self.current_port) + 1)[1:]
            inspection_result = self._capture_inspection(self.current_port, expected_packet_name, packet_check_list,
                                                         check_all_fields, ignore_list, include_list)
            self._determine_result(inspection_result, True,**kwargs)
        return self._keyword_cleanup()

    def retrieve_tlv_list_from_random_packet(self, port, **kwargs):
        """
        Keyword Arguments:
        [ports] - This must be a dictionary which contains the name of the traffic generator and the
                  traffic generator port. Example {"tgen_name": "tgen_1", "ifname": "1/1/11"}.
        [device_name] - The device name the TLV was stored with.

        This keyword verifies that a given TLV is present inside a random packet within a capture.
        """
        # Initially only supports checking one packet.
        number_to_check = 1

        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._init_keyword(**kwargs)

        self._get_traffic_generator_info(port)
        self.get_capture_length(self.current_port)

        packet_check_list = NumberUtils.get_random_list(number_to_check, self.capture_length)
        packets_to_check = self._get_packets(packet_check_list, self.current_port)

        packet_tlvs = packets_to_check[packets_to_check.keys()[0]].get_all_lldp_tlv_entries_in_hex_string()
        packet_tlvs = [tlv.lower() for tlv in packet_tlvs]  # Lowercase all TLVs.
        self.device_storage.add_value(self.current_port, "all_tlvs", packet_tlvs)

        return packet_tlvs

    def lldp_tlv_type_should_be_equal(self, port, tlv_type, tlv_subtype=None, tlv_oui=None, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port] - The port on which LLDP packet transmission and reception should be DISABLED.

        Dictionary Arguments:
        [port] - This is the port on which LLDP packet transmission and reception should be DISABLED.

        Verifies that the specified port IS configured to transmit and receive LLDP packets.
        """
        tlv_utils = NetworkElementTlvUtils()
        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._get_traffic_generator_info(port)

        self._init_keyword(**kwargs)

        packet_tlv = tlv_utils.find_tlv_by_type(self.device_storage.get_value(self.current_port, "all_tlvs"), tlv_type,
                                                tlv_subtype, tlv_oui)
        result = tlv_utils.tlv_comparator(packet_tlv, "type", tlv_type)

        self._determine_result(result, True,
                               "LLDP TLV Type in received PDUs was equal to " + tlv_type + ".",
                               "LLDP TLV Type in received PDUs was NOT equal to " + tlv_type + ".",**kwargs)

        return self._keyword_cleanup()

    def lldp_tlv_length_should_be_equal(self, port, tlv_type, tlv_length, tlv_subtype=None, tlv_oui=None, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port] - The port on which LLDP packet transmission and reception should be DISABLED.

        Dictionary Arguments:
        [port] - This is the port on which LLDP packet transmission and reception should be DISABLED.

        Verifies that the specified port IS configured to transmit and receive LLDP packets.
        """
        tlv_utils = NetworkElementTlvUtils()
        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._get_traffic_generator_info(port)

        self._init_keyword(**kwargs)

        packet_tlv = tlv_utils.find_tlv_by_type(self.device_storage.get_value(self.current_port, "all_tlvs"), tlv_type,
                                                tlv_subtype, tlv_oui)
        result = tlv_utils.tlv_comparator(packet_tlv, "length", tlv_length)

        self._determine_result(result, True,
                               "LLDP TLV Length in received PDUs was equal to " + tlv_length + ".",
                               "LLDP TLV Length in received PDUs was NOT equal to " + tlv_length + ".",**kwargs)

        return self._keyword_cleanup()

    def lldp_tlv_subtype_should_be_equal(self, port, tlv_type, tlv_subtype, tlv_level="subtype", tlv_oui=None,
                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port] - The port on which LLDP packet transmission and reception should be DISABLED.

        Dictionary Arguments:
        [port] - This is the port on which LLDP packet transmission and reception should be DISABLED.

        Verifies that the specified port IS configured to transmit and receive LLDP packets.
        """
        tlv_utils = NetworkElementTlvUtils()
        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._get_traffic_generator_info(port)

        self._init_keyword(**kwargs)

        packet_tlv = tlv_utils.find_tlv_by_type(self.device_storage.get_value(self.current_port, "all_tlvs"), tlv_type,
                                                tlv_subtype, tlv_oui)
        result = tlv_utils.tlv_comparator(packet_tlv, "subtype", tlv_subtype, tlv_level)

        self._determine_result(result, True,
                               "LLDP TLV Subtype in received PDUs was equal to " + tlv_subtype + ".",
                               "LLDP TLV Subtype in received PDUs was NOT equal to " + tlv_subtype + ".",**kwargs)

        return self._keyword_cleanup()

    def lldp_tlv_oui_should_be_equal(self, port, tlv_type, tlv_oui, tlv_level="oui", tlv_subtype=None,
                                     **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port] - The port on which LLDP packet transmission and reception should be DISABLED.

        Dictionary Arguments:
        [port] - This is the port on which LLDP packet transmission and reception should be DISABLED.

        Verifies that the specified port IS configured to transmit and receive LLDP packets.
        """
        tlv_utils = NetworkElementTlvUtils()
        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._get_traffic_generator_info(port)

        self._init_keyword(**kwargs)

        packet_tlv = tlv_utils.find_tlv_by_type(self.device_storage.get_value(self.current_port, "all_tlvs"), tlv_type,
                                                tlv_subtype)
        result = tlv_utils.tlv_comparator(packet_tlv, "oui", tlv_oui, tlv_level)

        self._determine_result(result, True,
                               "LLDP TLV OUI in received PDUs was equal to " + tlv_oui + ".",
                               "LLDP TLV OUI in received PDUs was NOT equal to " + tlv_oui + ".",**kwargs)

        return self._keyword_cleanup()

    def lldp_tlv_message_should_be_equal(self, port, tlv_type, tlv_message, tlv_level="message", tlv_subtype=None,
                                         tlv_oui=None, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [port] - The port on which LLDP packet transmission and reception should be DISABLED.

        Dictionary Arguments:
        [port] - This is the port on which LLDP packet transmission and reception should be DISABLED.

        Verifies that the specified port IS configured to transmit and receive LLDP packets.
        """
        tlv_utils = NetworkElementTlvUtils()
        port = self._validate_tgen_name_port_list(port)

        if len(port) != 1:
            raise AttributeError("The function can only accept a single tgen port.")

        self._get_traffic_generator_info(port)

        self._init_keyword(**kwargs)

        packet_tlv = tlv_utils.find_tlv_by_type(self.device_storage.get_value(self.current_port, "all_tlvs"), tlv_type,
                                                tlv_subtype, tlv_oui)
        result = tlv_utils.tlv_comparator(packet_tlv, "message", tlv_message, tlv_level)

        self._determine_result(result, True,
                               "LLDP TLV Message in received PDUs was equal to " + tlv_message + ".",
                               "LLDP TLV Message in received PDUs was NOT equal to " + tlv_message + ".")

        return self._keyword_cleanup()
