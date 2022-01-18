from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass \
    import NetworkElementKeywordBaseClass


class NetworkElementSnmpSend(NetworkElementKeywordBaseClass):

    def send_snmp_get_command(self, device_names, oid, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the command should be sent to. This can be a single name
                         or a list of names.
        [oid]          - The object identifier in it's base numeric form.

        Sends an SNMP get command to a device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpget'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            kw_results.append(self._determine_result(dev, cmd_obj))

        return self._keyword_cleanup(kw_results)

    def send_snmp_set_command(self, device_names, oid, data_type, value, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the command should be sent to. This can be a single name
                         or a list of names.
        [oid]          - The object identifier in it's base numeric form.
        [data_type]    - The data used when setting the object.
        ('i':Integer, 'u':Unsigned32, 't':TimeTicks, 'a':IpAddress, 'b':Bits, 'o':ObjectIdentifier, 's':OctetString)
        [value]        - The value of the object used for setting.

        Sends an SNMP set command to a device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpset'
            cmd_obj.oid = oid
            cmd_obj.data_type = data_type
            cmd_obj.value = value

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            kw_results.append(self._determine_result(dev, cmd_obj))

        return self._keyword_cleanup(kw_results)

    def send_snmp_getnext_command(self, device_names, oid, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the command should be sent to. This can be a single name
                         or a list of names.
        [oid]          - The object identifier in it's base numeric form.

        Sends an SNMP get-next command to a device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpgetnext'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            kw_results.append(self._determine_result(dev, cmd_obj))

        return self._keyword_cleanup(kw_results)

    def send_snmp_walk_command(self, device_names, oid, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the command should be sent to. This can be a single name
                         or a list of names.
        [oid]          - The object identifier in it's base numeric form.

        Sends an SNMP walk command to a device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            kw_results.append(self._determine_result(dev, cmd_obj))

        return self._keyword_cleanup(kw_results)

    def send_snmp_bulkwalk_command(self, device_names, oid, **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the command should be sent to. This can be a single name
                         or a list of names.
        [oid]          - The object identifier in it's base numeric form.

        Sends an SNMP bulk walk command to a device.
        """
        device_names = ListUtils.convert_to_list(device_names)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpbulkwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            kw_results.append(self._determine_result(dev, cmd_obj))

        return self._keyword_cleanup(kw_results)

    def send_snmp_get_command_output_should_contain(self, device_names, oid, expected_outputs, ignore_whitespace=True,
                                                    ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]      -  The device(s) the command should be sent to. This can be a single name
                              or a list of names.
        [oid]               - The object identifier in it's base numeric form.
        [expected_outputs]  - The strings that should be present in the command's output. This can
                              be a single string or a list of strings.
        [ignore_whitespace] - Whether whitespace should be ignored in the command's output.
        [ignore_case]       - Whether capitalization should be ignored in the command's output.

        Sends an SNMP get command to a device and checks for the presence of the desired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(expected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpget'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(True, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_get_command_output_should_not_contain(self, device_names, oid, unexpected_outputs,
                                                        ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the command should be sent to. This can be a single name
                               or a list of names.
        [oid]                - The object identifier in it's base numeric form.
        [unexpected_outputs] - The strings that should be not present in the command's output. This can
                               be a single string or a list of strings.
        [ignore_whitespace]  - Whether whitespace should be ignored in the command's output.
        [ignore_case]        - Whether capitalization should be ignored in the command's output.

        Sends an SNMP get command to a device and checks for the presence of the undesired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(unexpected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpget'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(False, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_getnext_command_output_should_contain(self, device_names, oid, expected_outputs,
                                                        ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]      - The device(s) the command should be sent to. This can be a single name
                              or a list of names.
        [oid]               - The object identifier in it's base numeric form.
        [expected_outputs]  - The strings that should be present in the command's output. This can
                              be a single string or a list of strings.
        [ignore_whitespace] - Whether whitespace should be ignored in the command's output.
        [ignore_case]       - Whether capitalization should be ignored in the command's output.

        Sends an SNMP getnext command to a device and checks for the presence of the desired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(expected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpgetnext'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(True, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_getnext_command_output_should_not_contain(self, device_names, oid, unexpected_outputs,
                                                            ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the command should be sent to. This can be a single name
                               or a list of names.
        [oid]                - The object identifier in it's base numeric form.
        [unexpected_outputs] - The strings that should be not present in the command's output. This can
                               be a single string or a list of strings.
        [ignore_whitespace]  - Whether whitespace should be ignored in the command's output.
        [ignore_case]        - Whether capitalization should be ignored in the command's output.

        Sends an SNMP getnext command to a device and checks for the presence of the undesired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(unexpected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpgetnext'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(False, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_walk_command_output_should_contain(self, device_names, oid, expected_outputs, ignore_whitespace=True,
                                                     ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]      - The device(s) the command should be sent to. This can be a single name
                              or a list of names.
        [oid]               - The object identifier in it's base numeric form.
        [expected_outputs]  - The strings that should be present in the command's output. This can
                              be a single string or a list of strings.
        [ignore_whitespace] - Whether whitespace should be ignored in the command's output.
        [ignore_case]       - Whether capitalization should be ignored in the command's output.

        Sends an SNMP walk command to a device and checks for the presence of the desired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(expected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(True, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_walk_command_output_should_not_contain(self, device_names, oid, unexpected_outputs,
                                                         ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the command should be sent to. This can be a single name
                               or a list of names.
        [oid]                - The object identifier in it's base numeric form.
        [unexpected_outputs] - The strings that should be not present in the command's output. This can
                               be a single string or a list of strings.
        [ignore_whitespace]  - Whether whitespace should be ignored in the command's output.
        [ignore_case]        - Whether capitalization should be ignored in the command's output.

        Sends an SNMP walk command to a device and checks for the presence of the undesired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(unexpected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(False, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_bulkwalk_command_output_should_contain(self, device_names, oid, expected_outputs,
                                                         ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]      - The device(s) the command should be sent to. This can be a single name
                              or a list of names.
        [oid]               - The object identifier in it's base numeric form.
        [expected_outputs]  - The strings that should be present in the command's output. This can
                              be a single string or a list of strings.
        [ignore_whitespace] - Whether whitespace should be ignored in the command's output.
        [ignore_case]       - Whether capitalization should be ignored in the command's output.

        Sends an SNMP bulkwalk command to a device and checks for the presence of the desired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(expected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpbulkwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(True, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    def send_snmp_bulkwalk_command_output_should_not_contain(self, device_names, oid, unexpected_outputs,
                                                             ignore_whitespace=True, ignore_case=True, **kwargs):
        """
        Keyword Arguments:
        [device_names]       - The device(s) the command should be sent to. This can be a single name
                               or a list of names.
        [oid]                - The object identifier in it's base numeric form.
        [unexpected_outputs] - The strings that should be not present in the command's output. This can
                               be a single string or a list of strings.
        [ignore_whitespace]  - Whether whitespace should be ignored in the command's output.
        [ignore_case]        - Whether capitalization should be ignored in the command's output.

        Sends an SNMP bulkwalk command to a device and checks for the presence of the undesired output.
        """
        device_names = ListUtils.convert_to_list(device_names)
        expected_outputs = ListUtils.convert_to_list(unexpected_outputs)

        kw_results = []
        for device_name in device_names:
            dev, _, _ = self._init_keyword(device_name, **kwargs)

            cmd_obj = SnmpCommandObject()
            cmd_obj.command_type = 'snmpbulkwalk'
            cmd_obj.oid = oid

            dev.send_command_object(cmd_obj)
            output = cmd_obj.return_text
            self.logger.log_info(output)

            parse_result, parse_output = self.__output_verify(False, output, expected_outputs,
                                                              ignore_whitespace, ignore_case)

            for line in parse_output:
                self.logger.log_info(line)

            kw_results.append(self._determine_result(dev, cmd_obj, parse_result, True,
                                                     "SNMP Send passed.", "SNMP Send failed."))
        return self._keyword_cleanup(kw_results)

    @staticmethod
    def __output_verify(exists, output, search_list, ignore_whitespace, ignore_case):
        result = True
        result_output = list()

        if not isinstance(search_list, list):
            search_list = [search_list]

        original_search_list = list(search_list)

        ignore_whitespace = StringUtils.string_to_boolean(ignore_whitespace)
        ignore_case = StringUtils.string_to_boolean(ignore_case)

        if ignore_whitespace:
            output = output.replace(' ', '')
        if ignore_case:
            output = output.lower()

        if ignore_whitespace or ignore_case:
            for i in range(len(search_list)):
                if ignore_whitespace:
                    search_list[i] = search_list[i].replace(" ", "")
                if ignore_case:
                    search_list[i] = search_list[i].lower()

        output = output.split("\r\n")
        if exists:
            result_output.append("\nExpected Outputs:")
        if not exists:
            result_output.append("\nUnexpected Outputs:")

        for i, search in enumerate(search_list):
            for j, line in enumerate(output):
                if search in line:
                    result_output.append("Found: " + original_search_list[i])
                    if not exists:
                        result = False
                    break
                if j == len(output) - 1:
                    result_output.append("Not Found: " + original_search_list[i])
                    if exists:
                        result = False

        return result, result_output
