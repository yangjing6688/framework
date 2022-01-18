import abc


class BaseErrorChecker(object):
    def __init__(self):
        self.temp_error_msgs = []
        self.ignore_error_msgs = []
        self.error_msgs = []
        self.gen_errors = []
        self.json_errors = []
        self.protocol_specific_errors = {}
        self.init_gen_errors()
        self.init_protocol_specific_errors()
        self.init_json_errors()

    @abc.abstractmethod
    def init_gen_errors(self):
        """
        This method must be overridden by any child class. It defines which errors to check for in
        a given output.
        """
        pass

    @abc.abstractmethod
    def init_protocol_specific_errors(self):
        """
        This method should be overridden by any child classes. If defines errors on a protocol specific
        level. It is possible for this to be empty.
        """
        pass

    @abc.abstractmethod
    def init_json_errors(self):
        """
        This method should be overridden by any child classes. If defines error keys for a JSON output.
        It is possible for this to be empty.
        """
        pass

    def add_error_to_temp_list(self, *errors):
        """
        This function appends all the <errors> passed to this function to the temp_error_msgs list.
        """
        for error in errors:
            self.temp_error_msgs.append(error)

    def remove_error_from_temp_list(self, *errors):
        """
        This function checks each of the passed <errors> and removes it if it is present in the
        temp_error_msgs list.
        """
        for error in errors:
            if error in self.temp_error_msgs:
                self.temp_error_msgs.remove(error)

    def clear_temp_error_list(self):
        """
        This function resets the temp_error_msgs list back to an empty list.
        """
        self.temp_error_msgs = []

    def add_error_to_ignore_list(self, *errors):
        """
        This function appends all the <errors> passed to this function to the ignore_error_msgs list.
        """
        for error in errors:
            self.ignore_error_msgs.append(error)

    def remove_error_from_ignore_list(self, *errors):
        """
        This function checks each of the passed <errors> and removes it if it is present in the
        ignore_error_msgs list.
        """
        for error in errors:
            if error in self.ignore_error_msgs:
                self.ignore_error_msgs.remove(error)

    def clear_ignore_error_list(self):
        """
        This function resets the ignore_error_msgs list back to any empty list.
        """
        self.ignore_error_msgs = []

    def check_for_errors(self, output):
        """
        This functions accepts an output as a string. It then iterates over each of the error lists
        and adds the error for each error encountered. With the exception of the ignore_error_msgs list.
        For each match in that list the string is replaced so it doesn't trip the later error checks.

        A formatted error message is returned if any errors are found, otherwise an empty string is returned.
        """
        pruned_output = output
        for error in self.ignore_error_msgs:
            if isinstance(error, str) and error in pruned_output:
                pruned_output = pruned_output.replace(error, "")
        for key in self.protocol_specific_errors.keys():
            for err in self.protocol_specific_errors[key]:
                if err in pruned_output:
                    self.error_msgs.append(err)
        for err in self.gen_errors:
            if err in pruned_output:
                self.error_msgs.append(err)
        for err in self.temp_error_msgs:
            if err in pruned_output:
                self.error_msgs.append(err)
        ferr = self.format_error_messages()
        self.error_msgs = []  # reset the list
        return ferr

    def check_for_errors_json(self, json_dict, error_item=0):
        """
        This functions accepts a JSON dictionary. It then iterates over each of the key/values
        and adds the error for each error encountered. With the exception of the ignore_error_msgs list.
        For each match in that list the string is replaced so it doesn't trip the later error checks.

        A formatted error message is returned if any errors are found, otherwise an empty string is returned.
        """
        json_output = json_dict
        error_messages = []
        error_list = error_item

        if error_list == 0:
            for error in self.ignore_error_msgs:
                if isinstance(json_output, dict):
                    for key in json_output:
                        if isinstance(json_output[key], str):
                            if error in json_output[key]:
                                json_output.pop(key)
                        else:
                            self.check_for_errors_json(json_output[key], 0)
                elif isinstance(json_output, str):
                    json_output = json_output.replace(error, "")
                else:
                    for i, list_item in enumerate(json_output):
                        if isinstance(list_item, str):
                            if error in list_item:
                                json_output = json_output.pop(i)
                        else:
                            self.check_for_errors_json(list_item, 0)
            error_list = 1

        if error_list == 1:
            for key in self.protocol_specific_errors.keys():
                err_list = self.protocol_specific_errors[key]
                for error in err_list:
                    error_messages.extend(self.recursive_json_search(error, json_output))
            error_list = 2

        if error_list == 2:
            for error in self.gen_errors:
                error_messages.extend(self.recursive_json_search(error, json_output))
            error_list = 3

        if error_list == 3:
            for error in self.temp_error_msgs:
                error_messages.extend(self.recursive_json_search(error, json_output))
            error_list = 4

        if error_list == 4:
            for error in self.json_errors:
                error_messages.extend(self.recursive_json_search(error, json_output))

        self.error_msgs = error_messages
        ferr = self.format_error_messages()
        self.error_msgs = []  # reset the list
        return ferr

    def format_error_messages(self):
        """
        This function returns a formatted string for each error observed in the output.
        If no errors were found an empty string is returned.
        """
        formatted_msg = ''
        for err in self.error_msgs:
            formatted_msg += 'Error -> ' + err + '\n'
        return formatted_msg

    def recursive_json_search(self, error, json_output):
        """
        This function reads into all levels of a JSON dictionary and returns a list of errors found in the JSON
        dictionary that match or contain the supplied error.
        """
        error_messages = []
        if isinstance(json_output, dict):
            for json_key in json_output:
                if error in json_key:
                    error_messages.append(json_output[json_key])
                if isinstance(json_output[json_key], str):
                    if error in json_output[json_key]:
                        error_messages.append(error)
                else:
                    err = self.recursive_json_search(error, json_output[json_key])
                    if err:
                        error_messages.extend(err)
        elif isinstance(json_output, list):
            for list_item in json_output:
                if isinstance(list_item, str):
                    if error in list_item:
                        error_messages.append(list_item)
                else:
                    err = self.recursive_json_search(error, list_item)
                    if err:
                        error_messages.extend(err)
        else:
            if error in str(json_output):
                error_messages.append(json_output)
        return error_messages
