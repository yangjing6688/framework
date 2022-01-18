from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.port.base.PortBaseCustomShowTools import \
    PortBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class PortCustomShowTools(PortBaseCustomShowTools):
    def __init__(self, device):
        super(PortCustomShowTools, self).__init__(device)

    def create_interface_dictionaries(self, output, args, **kwargs):
        output = output.replace("SNMPv2-SMI::mib-2.31.1.1.1.1.", "").replace("=", "")

        if output.find("2:1") == -1:
            output = output.replace("1:", "")
        output = output.split()

        def dict_from_list(keys_and_values):
            return dict(zip(keys_and_values[::2], keys_and_values[1::2]))

        if_index_to_if_name = dict_from_list(output)
        if_name_to_if_index = dict((v, k) for k, v in if_index_to_if_name.items())

        self.value_storage.add_value(self.device.name, "port_name_index", if_name_to_if_index)
        self.value_storage.add_value(self.device.name, "port_index_name", if_index_to_if_name)

        result = True if len(if_name_to_if_index) and len(if_index_to_if_name) != 0 else False
        self.logger.log_debug("Arrays if_name_to_if_index and if_index_to_if_name created.")

        return result, None

    def verify_port_enabled(self, output, args, **kwargs):
        admin_state = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        return admin_state.lower() == "1", {"ret_state": admin_state}

    def verify_port_operational(self, output, args, **kwargs):
        operational_state = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        return operational_state.lower() == "1", {"ret_state": operational_state}

    def verify_port_mtu(self, output, args, **kwargs):
        port_mtu = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        return port_mtu.lower() == args["mtu"], {"ret_mtu": port_mtu}

    def verify_port_high_speed(self, output, args, **kwargs):
        port_speed = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        return port_speed.lower() == args["speed"], {"ret_high_speed": port_speed}

    def verify_port_mac_address(self, output, args, **kwargs):
        port_mac = self.pw.get_value_by_offset(output, args["oid_index"], 2)
        mac = args["mac"].lower()
        port_mac = port_mac[2:]
        if "." in mac:
            mac = mac.replace('.', '')
        elif ":" in mac:
            mac = mac.replace(':', '')
        elif "-" in mac:
            mac = mac.replace('-', '')

        return port_mac.lower() == mac, {"ret_mac": port_mac}

    def verify_port_alias(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        return port_count == args["alias"], {"ret_alias": port_count}

    def check_port_in_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_octets": port_count}

    def check_port_in_unicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_unicast": port_count}

    def check_port_in_discard_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_discard": port_count}

    def check_port_in_error_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_error": port_count}

    def check_port_in_unknown_protocol_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_unknown_protocol": port_count}

    def check_port_out_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_octets": port_count}

    def check_port_out_unicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_unicast": port_count}

    def check_port_out_discard_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_discard": port_count}

    def check_port_out_error_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_error": port_count}

    def check_port_in_multicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_multicast": port_count}

    def check_port_in_broadcast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_in_broadcast": port_count}

    def check_port_out_multicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_multicast": port_count}

    def check_port_64_bit_in_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_in_octets": port_count}

    def check_port_64_bit_out_octets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_out_octets": port_count}

    def check_port_out_broadcast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_out_broadcast": port_count}

    def check_port_64_bit_in_unicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_in_unicast": port_count}

    def check_port_64_bit_in_multicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_in_multicast": port_count}

    def check_port_64_bit_in_broadcast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_in_broadcast": port_count}

    def check_port_64_bit_out_unicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_out_unicast": port_count}

    def check_port_64_bit_out_multicast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_out_multicast": port_count}

    def check_port_64_bit_out_broadcast_packets(self, output, args, **kwargs):
        port_count = self.pw.get_value_by_offset(output, args["oid_index"], 2)

        result = NumberUtils().verify_expected_count(port_count, args["count_operator"], args["count"])
        return result, {"ret_64_out_broadcast": port_count}

    def create_dot1d_dictionaries(self, output, args, **kwargs):
        if output != "NO DATA":
            output = output.replace("SNMPv2-SMI::mib-2.17.1.4.1.2.", "").replace("=", "")
            output = output.split()

            def dict_from_list(keys_and_values):
                return dict(zip(keys_and_values[::2], keys_and_values[1::2]))

            dot1d_id_to_if_index = dict_from_list(output)
            if_index_to_dot1d_id = dict((v, k) for k, v in dot1d_id_to_if_index.items())

            self.value_storage.add_value(self.device.name, "dot1d_id_index", dot1d_id_to_if_index)
            self.value_storage.add_value(self.device.name, "port_index_dot1d_id", if_index_to_dot1d_id)

            result = len(dot1d_id_to_if_index) and len(if_index_to_dot1d_id) != 0
            self.logger.log_debug("Arrays dot1d_id_to_if_index and if_index_to_dot1d_id created.")

            return result, None
        return False, None
