import time
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Keywords.BaseClasses.KeywordResult import KeywordResult
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass \
    import NetworkElementKeywordBaseClass


class NetworkElementJsonRpc(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementJsonRpc, self).__init__()
        self.cmd_obj = {}

    def send_cmd_json_rpc(self, device_name, command, **kwargs):
        """
        Keyword Arguments:
            device_name - The name of the device the keyword should be run against.
            command - The command that should be sent to the device.

        Sends the given command to a device and saves returned json in a python dictionary.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)
        cmd_obj = self.__send_command(dev, command, **kwargs)
        self.cmd_obj[device_name] = cmd_obj
        kw_result = self._determine_result(dev, cmd_obj)
        return self._keyword_cleanup([kw_result])

    def verify_field(self, device_name, identifiers, **kwargs):
        """
        Keyword Arguments:
            [device_name] - The name of the device to run this keyword against.
            [identifiers] - Key/value pairs used to identify a block within the returned json.
                            The identifiers are formatted as follows.
                                key1: val1, key2 <> val2, keyN: valN

                            Leading and trailing whitespace will be stripped from all keys/values.
                            Valid operators:
                              :  Equal
                              <> Not Equal
                              >  Greater Than
                              >= Greater or Equal
                              <  Less Than
                              <= Less or Equal
                              ^  Range

                            Operator Examples
                              key: val
                              key <> val
                              key > val
                              key >= val
                              key < val
                              key <= val
                              key ^ valLo-valHigh -> key ^ 0-100

        This keyword will verify that the previous send_cmd contains all the provided
        key value pairs within a result dictionary. For example if the returned object had
        the following format.

        {"jsonrpc": "2.0",
         "id": 0,
         "result: [{"CLIOutput: <cli_output>},
                   {"resultDict1" <result_dict1>},
                   {"resultDict2" <result_dict2>}]

        It would verify that all the passed key value pairs were found within either "resultDict1"
        or "resultDict2". If some are found in each, the keyword will fail.
        """
        self._init_keyword(device_name, **kwargs)

        result, _ = self.__check_output(device_name, identifiers)

        kw_result = KeywordResult(device_name, result,
                                  "All key value pairs found",
                                  "Could not find all key value pairs.", None)
        return self._keyword_cleanup([kw_result])

    def get_field(self, device_name, return_field, identifiers, **kwargs):
        """
        Keyword Arguments:
            [device_name] - The name of the device to run this keyword against.
            [return_field] - The field's whose data should be returned if a match is found.
            [identifiers] - Key/value pairs used to identify a block within the returned json.
                            See verify_field's docstring for more information.

        This function returns a given field's value if a match for the provided identifiers is found.
        This function will return None if the return_field is not found.
        """
        self._init_keyword(device_name, **kwargs)

        _, return_dict = self.__check_output(device_name, identifiers)

        if return_dict and return_field in return_dict:
            return return_dict[return_field]
        return None

    def get_fields(self, device_name, return_fields, identifiers, **kwargs):
        """
        Keyword Arguments:
            [device_name] - The name of the device to run this keyword against.
            [return_fields] - All the fields whose data should be returned if a match is found.
                              Multiple fields and be provided with the either of the following formats.
                                [key1, key2, keyN]
                                key1, key2, keyN
            [identifiers] - Key/value pairs used to identify a block within the returned json.
                            See verify_field's docstring for more information.

        This function returns a given field's value if a match for the provided identifiers is found.
        If not object can be found using the provided identifiers an empty list will be returned.
        None will be appended to the list for any fields not found.
        """
        return_vals = []

        if not isinstance(return_fields, list):
            return_fields = [i.strip("] ") for i in return_fields.split(",")]

        self._init_keyword(device_name, **kwargs)

        _, return_dict = self.__check_output(device_name, identifiers)

        if return_dict:
            for return_field in return_fields:
                if return_field in return_dict:
                    return_vals.append(return_dict[return_field])
                else:
                    return_vals.append(None)
        return return_vals

    def wait_for_field(self, device_name, identifiers, initial_delay="0", interval="1", max_wait="10", **kwargs):
        """
        Keyword Args:
            [device_name] - The name of the device to run the keyword against.
            [identifiers] - Key/value pairs used to identify a block within the returned json.
                            See verify_field for more information.
            [initial_delay] - How long the wait for should delay until it's first check.
            [interval] - The delay between each check.
            [max_wait] - The maximum amount of time the wait for will wait before marking
                         the keyword as a failure.

        This function will wait for the supplied keyword to execute successfully or until
        <max_wait> seconds have passed. If a the keyword succeeds the wait for will pass
        otherwise it will fail.
        """
        dev, _, _ = self._init_keyword(device_name, **kwargs)

        result = False

        # Convert initial_delay, interval, and max_wait to ints. If the value passed
        # is not a digit and not an int use the default value.
        int_init_delay = int(initial_delay) if isinstance(initial_delay, int) or initial_delay.isdigit() else 0
        int_interval = int(interval) if isinstance(interval, int) or interval.isdigit() else 1
        int_max_wait = int(max_wait) if isinstance(max_wait, int) or max_wait.isdigit() else 10

        self.logger.log_info("Delaying " + str(int_init_delay) + " seconds before first check.")
        time.sleep(int_init_delay)
        start = time.time()  # Wait until after the initial delay to start the max_wait timer.

        cmd_obj = self.cmd_obj[device_name]
        self.logger.log_info("Starting wait for with max time of " + str(int_max_wait) + ".")
        while not result and time.time() - start < int_max_wait:
            result, _ = self.__check_output(device_name, identifiers)
            if not result:
                self.logger.log_info("Delaying " + str(int_interval) + " seconds before checking again.")
                self.cmd_obj[device_name] = self.__send_command(dev, cmd_obj.command, log=False)
                time.sleep(int_interval)

        kw_result = self._determine_result(dev, cmd_obj, result, True, "All key value pairs found",
                                           "Could not find all key value pairs within " + max_wait + " seconds.")
        return self._keyword_cleanup([kw_result])

    # +------------------------------+
    # | Non-Keyword Helper Functions |
    # +------------------------------+
    @staticmethod
    def __send_command(dev, command, **kwargs):
        """
        This functions creates a CLI command object and sends it to the given device.
        This function also supports a number of keyword arguments to set optional values
        within the command object.

        Optional Kwargs:
            prompt - This accepts a prompt constant (which can be found in NetworkElementConstants).
                     It tells the device which prompt it should sent the command from.
            prompt_args - This accepts either a string or list of strings which should contain
                          any arguments required by the prompt handler to change prompt.
            confirmation_phrases - This accepts either a string or list of strings which contain any
                                   outputs that require a response.
            confirmation_args - This accepts a string or list of strings to send in response to the
                                received confirmation phrase.
        """
        cmd_obj = CliCommandObject()
        cmd_obj.command = command
        cmd_obj.prompt = kwargs.get("prompt", "userPrompt")
        cmd_obj.prompt_args = kwargs.get("prompt_args", None)
        cmd_obj.confirmation_phrases = kwargs.get("confirmation_phrases", None)
        cmd_obj.confirmation_args = kwargs.get("confirmation_args", None)
        return dev.send_command_object(cmd_obj, **kwargs)

    def __check_output(self, device_name, required_data):
        """
        Function Args:
            [output_json] - The JSON data returned from a JSON-RPC command.
            [required_data] - This should be a string that follows the rules outlined
                              the <identifier> rules. See verify_field, get_field, or get_fields
                              for more info.

        This function checks each block in <output_json> looking for a block that contains
        all the info outlined in <required_data>. If a match is found True and the matching
        block are returned. Otherwise False and None are returned.
        """
        required_fields = self.__create_required_fields(required_data)
        results_dict = self.cmd_obj[device_name].return_text["result"]

        self.logger.log_info("Checking each block for the following:")
        for i, required_field in enumerate(required_fields):
            if i < len(required_fields) - 1:
                self.logger.log_info("    " + str(required_field))
            else:
                self.logger.log_info("    " + str(required_field) + "\n")

        for i, result in enumerate(results_dict):
            for key in result:
                if key.lower() not in ["clioutput", "status", "message"]:
                    formatted_result_dict = dict((k, str(v)) for (k, v) in result[key].items())
                    self.logger.log_info("Checking Block: \n" + StringUtils.pretty_print_dict(formatted_result_dict))

                    if self.__check_dict(formatted_result_dict, required_fields):
                        self.logger.log_info("Found a match!")
                        return True, formatted_result_dict
                    if i < len(results_dict) - 1:
                        self.logger.log_info("Block did not match, checking next block.")
        self.logger.log_info("No block matched provided identifiers.")
        return False, None

    @staticmethod
    def __check_dict(check_dict, required_fields):
        """
        This function checks an individual json block for the required fields. Returns
        True if a match is found and False otherwise.
        """
        for required_field in required_fields:
            if required_field.key not in check_dict:
                return False
            elif not required_field.compare(check_dict):
                return False
        return True

    def __create_required_fields(self, s):
        """
        This function creates a RequiredField block for a given key/value pair string.
        See RequiredField for more information.
        """
        # Splits the passed string on "," and removes any "{}" characters.
        key_pairs = [i.strip("{} ") for i in s.split(",")]
        required_fields = []

        # Iterates over the key_pairs list and splits them on their operator into key/value pairs.
        # Then it adds a RequiredField object for each key/value pair.
        # A ValueError is raised if no valid operator can be found.
        for key_pair in key_pairs:
            operator = self.__get_operator(key_pair)
            key, val = key_pair.split(operator)
            required_fields.append(RequiredField(key, val, operator))

        return required_fields

    @staticmethod
    def __get_operator(key_pair_string):
        """
        This function finds the operator for a given key/value pair string. If no valid
        operator can be found a ValueError is raised.
        """
        for op in RequiredField.VALID_OPERATORS:
            if op in key_pair_string:
                return op

        raise ValueError(key_pair_string + " does not contain a valid operator. "
                                           "See docstring for supported operators.")


class RequiredField(object):
    """
    A required field object contains the following.
        key
        val
        operator

    It also provides one method to compare a RequiredField object against a dictionary.
    It supports various operators which are outlined below.
    """

    EQUAL = ":"
    NOT_EQUAL = "<>"
    GREATER_THAN = ">"
    GREATER_OR_EQUAL = ">="
    LESS_THAN = "<"
    LESS_OR_EQUAL = "<="
    RANGE = "^"
    VALID_OPERATORS = [EQUAL, NOT_EQUAL,
                       GREATER_THAN, GREATER_OR_EQUAL,
                       LESS_THAN, LESS_OR_EQUAL,
                       RANGE]

    def __init__(self, key, val, operator):
        # Attribute with setter/getter.
        self._operator = None
        self._key = None
        self._val = None

        self.key = key
        self.val = val
        self.operator = operator
        self.logger = Logger()

    def __str__(self):
        return " ".join([self.key, self.operator, self.val])

    @property
    def operator(self):
        """
        Getter method for the operator attribute.
        """
        return self._operator

    @operator.setter
    def operator(self, op):
        """
        Setter method for the operator attribute. It sets the operator
        to the passed operator if it's within the valid operator list.
        Otherwise it sets it to EQUAL.
        """
        if op in self.VALID_OPERATORS:
            self._operator = op
        else:
            self._operator = self.EQUAL

    @property
    def key(self):
        """
        Getter method for the key attribute.
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Setter method for key attribute. Removes leading and trailing
        whitespace before setting.
        """
        self._key = key.strip()

    @property
    def val(self):
        """
        Getter method for the val attribute.
        """
        return self._val

    @val.setter
    def val(self, val):
        """
        Setter method for val attribute. Removes leading and trailing
        whitespace before setting.
        """
        self._val = val.strip()

    def compare(self, comp_field):
        """
        Compares a RequiredField object against a comp_field dictionary.

        This compare function assumes that the key in the RequiredField is
        present within the comp_field. If it's not there an exception will
        be raised.
        """
        self.logger.log_trace("Required: " + self.val +
                              " Received: " + comp_field[self.key] +
                              " Operator: " + self.operator)

        # To do >, >=, <, <=, and range comparisons we need to
        # ensure that both value and compare value can be casted
        # to floats. In the case of ranges we need to be able to split
        # the #-# string into two separate floats.
        if self.operator in [self.GREATER_THAN,
                             self.GREATER_OR_EQUAL,
                             self.LESS_THAN,
                             self.LESS_OR_EQUAL,
                             self.RANGE]:
            try:
                comp_num = float(comp_field[self.key])

                if self.operator != self.RANGE:
                    val_num = float(self.val)

                    if self.operator == self.GREATER_THAN:
                        return comp_num > val_num
                    elif self.operator == self.GREATER_OR_EQUAL:
                        return comp_num >= val_num
                    elif self.operator == self.LESS_THAN:
                        return comp_num < val_num
                    elif self.operator == self.LESS_OR_EQUAL:
                        return comp_num <= val_num
                else:
                    val_lo, val_high = [float(i) for i in self.val.split("-")]

                    if self.operator == self.RANGE:
                        return val_lo <= comp_num <= val_high
            except ValueError:
                # If we aren't able to convert any of the values to float, return False.
                return False

        # If we are doing a == or != comparison do the comparison normally
        # without casting anything.
        if self.operator == self.NOT_EQUAL:
            return self.val != comp_field[self.key]
        else:
            return self.val == comp_field[self.key]
