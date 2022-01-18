from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.macsec.base.MacsecBaseCustomShowTools import \
    MacsecBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class MacsecCustomShowTools(MacsecBaseCustomShowTools):
    def __init__(self, device):
        super(MacsecCustomShowTools, self).__init__(device)

    def verify_macsec_ca(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        ca_name_found = self.pw.get_exact_value_by_offset(output, args["ca_name"], 0)
        result = True if ca_name_found == args["ca_name"] else False
        return result, {"ret_ca_name": ca_name_found}

    def verify_macsec_cipher_suite(self, output, args, **kwargs):
        cipher_string = "gcm-aes-" + args["cipher_value"]
        full_line = self.pw.get_value_range(output, args["port"] + "  ", "\n")
        self.logger.log_info(full_line)
        full_line = full_line.split()
        line_length = len(full_line)
        cipher_found = self.pw.get_value_by_offset(output, args["port"] + "  ", line_length - 3)
        result = True if cipher_string == cipher_found else False
        return result, {"ret_cipher": cipher_found}

    def verify_macsec_confidentiality_offset(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_macsec_include_sci(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_macsec_mka_actor_priority(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_macsec_replay_protect(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_macsec_on_port(self, output, args, **kwargs):
        state_found = self.pw.get_value_by_offset(output, args["port"] + "  ", 1)
        result = True if state_found == "Yes" else False
        return result, {"ret_state": state_found}

    def verify_macsec_ca_port(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        ca_name_found = self.pw.get_exact_value_by_offset(output, args["ca_name"], 0)
        ca_port_found = self.pw.get_exact_value_by_offset(output, args["ca_name"], 1)
        result = self.it.compare_port_values(ca_port_found, args["port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_ca_name": ca_name_found,
                        "ret_ca_port": ca_port_found}

    def verify_macsec_ca_ckn(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        ca_name_found = self.pw.get_exact_value_by_offset(output, args["ca_name"], 0)
        ckn_name_found = self.pw.get_exact_value_by_offset(output, args["ca_name"], 2)
        result = True if ca_name_found == args["ca_name"] and ckn_name_found == args["ckn_name"] else False
        return result, {"ret_ca_ckn": ckn_name_found}

    def verify_macsec_port_connection_status(self, output, args, **kwargs):
        status_found = self.pw.get_value_by_offset(output, "Connect", 2)
        result = True if status_found == args["status"] else False
        return result, {"ret_status_found": status_found}

    def verify_macsec_port_confidentiality_offset_admin(self, output, args, **kwargs):
        admin_conf_offset_found = self.pw.get_value_from_string_to_eol(output, "Local MACsec Capability")
        result = True if str('0' or '30' or '50') in admin_conf_offset_found else False
        return result, {"ret_admin_conf_offset_found": admin_conf_offset_found}

    def verify_macsec_port_cipher_suite_admin(self, output, args, **kwargs):
        cipher_suite_admin_found = self.pw.get_value_by_offset(output, "MACsec Cipher Suite Admin", 5)
        result = True if cipher_suite_admin_found == args["suite"] else False
        return result, {"ret_cipher_suite_admin_found": cipher_suite_admin_found}

    def verify_macsec_port_cipher_suite_oper(self, output, args, **kwargs):
        cipher_suite_oper_found = self.pw.get_value_by_offset(output, "MACsec Cipher Suite Oper", 5)
        result = True if cipher_suite_oper_found == args["suite"] else False

        return result, {"ret_cipher_suite_oper_found": cipher_suite_oper_found}

    def verify_macsec_tx_port_key_number(self, output, args, **kwargs):
        tx_key_number_found = self.pw.get_value_by_offset(output, "MKA Tx Key Number", 5)
        result = True if tx_key_number_found == args["tx_key_num"] else False
        return result, {"ret_tx_key_found": tx_key_number_found}

    def verify_macsec_rx_port_key_number(self, output, args, **kwargs):
        rx_key_number_found = self.pw.get_value_by_offset(output, "MKA Rx Key Number", 5)
        result = True if rx_key_number_found == args["rx_key_num"] else False
        return result, {"ret_rx_key_found": rx_key_number_found}

    def verify_macsec_tx_port_association_number(self, output, args, **kwargs):
        tx_association_number_found = self.pw.get_value_by_offset(output, "MKA Tx Association Number", 5)
        result = True if tx_association_number_found == args["tx_assoc_num"] else False
        return result, {"ret_tx_association_number_found": tx_association_number_found}

    def verify_macsec_rx_port_association_number(self, output, args, **kwargs):
        rx_association_number_found = self.pw.get_value_by_offset(output, "MKA Rx Association Number", 5)
        result = True if rx_association_number_found == args["rx_assoc_num"] else False
        return result, {"ret_rx_association_number_found": rx_association_number_found}

    def verify_macsec_port_confidentiality_offset_oper(self, output, args, **kwargs):
        oper_conf_offset_found = self.pw.get_value_from_string_to_eol(output, "Negotiated Protection")
        result = True if str('0' or '30' or '50') in oper_conf_offset_found else False
        return result, {"ret_conf_offset_found": oper_conf_offset_found}

    def verify_macsec_self_elected_key_server(self, output, args, **kwargs):
        key_server = self.pw.get_value_by_offset(output, args["port"] + "  ", 6)
        result = True if key_server == "Local" else False
        return result, {"ret_keyserver": key_server}

    def verify_macsec_peer_elected_key_server(self, output, args, **kwargs):
        key_server = self.pw.get_value_by_offset(output, args["port"] + "  ", 6)
        result = True if key_server == "Peer" else False
        return result, {"ret_keyserver": key_server}

    def verify_macsec_tx_sc_octets_encrypted(self, output, args, **kwargs):
        """
        Return True if MACsec Tx SC Octets Encrypted matches expected count, false otherwise.
        """
        return self._check_count(output, args, "Octets Encrypted", **kwargs);

    def verify_macsec_tx_sc_encrypted_packets(self, output, args, **kwargs):
        """
        Return True if MACsec Tx SC Encrypted Packets matches expected count, false otherwise.
        Note: First occurance of "Encrypted Pkts" is for Tx SC
        """
        return self._check_count(output, args, "Encrypted Pkts", index=1, **kwargs);

    def verify_macsec_tx_sa_encrypted_packets(self, output, args, **kwargs):
        """
        Return True if MACsec Tx SA Encrypted Packets matches expected count, false otherwise.
        Note: Second occurance of "Encrypted Pkts" is for Tx SA
        """
        return self._check_count(output, args, "Encrypted Pkts", index=2, **kwargs);

    def verify_macsec_rx_sc_octets_decrypted(self, output, args, **kwargs):
        """
        Return True if MACsec Rx SC Octets Decrypted matches expected count, false otherwise.
        """
        return self._check_count(output, args, "Octets Decrypted", **kwargs);

    def verify_macsec_rx_sc_ok_packets(self, output, args, **kwargs):
        """
        Return True if MACsec Rx SC OK Packets matches expected count, false otherwise.
        Note: First occurance of "OK Pkts" is for Rx SC
        """
        return self._check_count(output, args, "OK Pkts", index=1, **kwargs);

    def verify_macsec_rx_sa_ok_packets(self, output, args, **kwargs):
        """
        Return True if MACsec Rx SA OK Packets matches expected count, false otherwise.
        Note: Second occurance of "OK Pkts" is for Rx SA
        """
        return self._check_count(output, args, "OK Pkts", index=2, **kwargs);

    def _check_count(self, output, args, counter_name, index=1, **kwargs):
        actual_count = self._counter_value(output, counter_name, index)
        count_max_str = args["count_max"]
        # print(">>> count_max_str '{0}' type:{1}".format(count_max_str, type(count_max_str)))
        if count_max_str:
            count_min = int(args["count"])
            count_max = int(count_max_str)
            # print(">>> count_min:{0} count_max{1}".format(count_min, count_max))
            return self._check_count_range(counter_name, count_min, count_max, actual_count);
        else:
            expected_count = int(args["count"])
            # print(">>> expected_count:{0}".format(expected_count))
            return self._check_count_exact(counter_name, expected_count, actual_count);

    def _check_count_exact(self, counter_name, expected_count, actual_count):
        result = True if actual_count == expected_count else False
        print("  Verify MACsec counter '{0}' expect:{1} actual:{2} result:{3}".format(counter_name, expected_count, actual_count, result))
        return result, {"count": actual_count}

    def _check_count_range(self, counter_name, count_min, count_max, actual_count):
        result = True if count_min <= actual_count <= count_max else False
        print("  Verify MACsec counter '{0}' expect:{1}..{2} actual:{3} result:{4}".format(counter_name, count_min, count_max, actual_count, result))
        return result, {"count": actual_count}

    def _counter_value(self, output, counter_name, index):
        """
        Return the value of one countersspecified in 'counter_name'. If a
        counter is not found in 'output' then its value will default to -1.
        :param output: output of the "show macsec port <port> detail" command,
                       which should contain the counter names and values.
        :param counter_name: Text to search for within 'output'
        :param index:  'counter_name' may show up multiple times in output,
                       A 1-based index, so first occurance is index 1
        :return: value of counter, if found
                 -1 otherwise
        """
        position = len(counter_name.split()) + 1
        values = self.pw.get_value_by_offset(output, counter_name, position).split(" ")
        # print(">>> counter:{0} index:{1} values:{2}".format(counter_name, index, values))
        try:
            value = values[index-1]
        except IndexError:
            return -1
        else:
            if value != "valueNotPresent":
                return int(value)
        return -1

    def verify_macsec_tx_port_no_errors(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_macsec_rx_port_no_errors(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
