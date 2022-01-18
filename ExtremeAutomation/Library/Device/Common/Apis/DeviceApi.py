from ExtremeAutomation.Library.Device.Common.ManagedObject import ManagedObject
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.ApiUtils import ApiUtils
import re


class DeviceApi(ManagedObject):
    def __init__(self, dev):
        ManagedObject.__init__(self)
        self.device = dev

        # API Function Utilities
        self.str_utils = StringUtils()
        self.api_utils = ApiUtils()

    def get_attributes_with_regexp(self, output, regexp, mapping_tbl, args, **kwargs):
        """
        Return the requested attributes, parsed from the output using regex.

        output      - The return text from the CLI command.
        regexp      - The regex string for matching and mapping all attributes.
        mapping_tbl - The attribute mapping table for regex matches.
        args        - The argument dictionary from the Robot Keyword.
        """
        result = self._parse_with_regexp(regexp, output, args)
        attr_dict = {}
        if result is None:
            # We did not match the regexp, can't get any attribute - fail.
            self.logger.log_warn("Device \"" + self.device.name + "\": regexp match failed to match with regexp '" +
                                 regexp + "'")
            fail_str = "Device \"" + self.device.name + "\": regexp match failed to match with regexp '" + \
                       regexp + "'"
            return False, attr_dict, fail_str

        # We matched the regular expression, traverse the attributes and add it to the attrDict
        for attr_to_validate in args["attrs_to_get"]:
            if attr_to_validate in mapping_tbl:
                grp_index = mapping_tbl[attr_to_validate]
                rx_value = str(result.group(grp_index)).strip()
                attr_dict[attr_to_validate] = rx_value
            else:
                return False, {}, "Device \"" + self.device.name + "\": attribute '" + \
                    attr_to_validate + "' is not supported for the version of code being run"
        return True, attr_dict, ""

    def verify_with_regexp(self, output, regexp, mapping_tbl, args, **kwargs):
        """
        Validate the requested attributes, parsed from the output using regex, match the expected values.

        output      - The return text from the CLI command.
        regexp      - The regex string for matching and mapping all attributes.
        mapping_tbl - The attribute mapping table for regex matches.
        args        - The argument dictionary from the Keyword.
        kwargs      - All attributes to validate, and values, from the Robot Keyword.
        """
        fail_str = ""
        result = self._parse_with_regexp(regexp, output, args)
        if result is None:
            if "should_not_be_present" in kwargs:
                if kwargs.get("should_not_be_present", False) is True:
                    self.logger.log_info("Device \"" + self.device.name + "\": is not present as expected")
                    return True
            else:
                self.logger.log_warn("Device \"" + self.device.name +
                                     "\": regexp match failed to match with regexp '" + regexp + "'")
                fail_str = "Device \"" + self.device.name + "\": regexp match failed to match with regexp '" + \
                           regexp + "'"
                return False, fail_str

        return_value = True

        for attr_to_validate in kwargs:
            if attr_to_validate in mapping_tbl:
                grp_index = mapping_tbl[attr_to_validate]
                rx_value = str(result.group(grp_index)).strip()
                exp_value = str(kwargs[attr_to_validate]).strip()
                if str(rx_value).lower() == exp_value.lower():
                    self.logger.log_info("Device \"" + self.device.name + "\": attribute '" +
                                         attr_to_validate + "' matches expected value '" + kwargs[attr_to_validate] +
                                         "'")
                else:
                    self.logger.log_warn("Device \"" + self.device.name + "\": attribute '" +
                                         attr_to_validate + "' has value '" + rx_value +
                                         "' which doesn't matches expected value '" + kwargs[attr_to_validate] + "'")
                    fail_str = (fail_str + "\n" + "Device \"" + self.device.name + "\": attribute '" +
                                attr_to_validate + "' has value '" + rx_value +
                                "' which doesn't matches expected value '" + kwargs[attr_to_validate] + "'")
                    return_value = False

        return return_value, fail_str

    @staticmethod
    def _parse_with_regexp(regexp, output, args):
        """
        Return match object for regex search of 'output'.

        regexp - The regular expression to use for searching the output.
        output - The return text from the CLI command.
        args   - the Argument dictionary from the Robot Keyword. (For replacing vars in the regex string)
        """
        # Replace all variables defined in regexp with value from args.
        # Use regex to find all instances of {<str>} within the <regexp>.
        string_vars = re.findall("{<.*?>}", regexp)

        # Iterate over each variables located by the above regex.
        for string_var in string_vars:
            # Format the current variable by removing its surrounding {} chars.
            # Then, if the formatted variable is in the <args> dictionary replace
            # all instances of it with with it's corresponding value.
            format_var = string_var.strip("{<>}")
            if format_var in args:
                regexp = regexp.replace(string_var, args[format_var])

        regexp_obj = re.compile(regexp, re.MULTILINE)
        result = regexp_obj.search(output)
        return result
