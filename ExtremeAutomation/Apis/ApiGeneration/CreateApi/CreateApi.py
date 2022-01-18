import os
import re
import abc
import logging
from collections import OrderedDict


class CreateApi(object):
    def __init__(self, output_dir, device_type, agent):
        self.output_dir = output_dir
        self.device_type = device_type
        self.agent = agent
        self.log = logging.getLogger("Console")

    @abc.abstractmethod
    def create_api(self, device_type, agent, data_bean_list, **kwargs):
        """
        This function must be overridden by child classes with the code that generates a single API file.
        """
        pass

    @abc.abstractmethod
    def create_base_api(self, feature, function_list):
        """
        This function must be overridden by child classes with the code that generates a single base API file.
        """
        pass

    def create_data_file(self, *args):
        """
        This function should be overridden by child class with the code that generates a single data file.
        """
        pass

    @staticmethod
    def create_indent(number):
        """
        This function creates a string of whitespace that is 4 * <number> characters long.
        """
        return (" " * 4) * number

    def get_functions_from_existing_file(self, existing_file):
        """
        This function returns all function lines from an existing file.
        """
        functions = OrderedDict()
        function_regex = r"^    def [^_][a-zA-Z_0-9]*\("

        try:
            with open(os.path.join(existing_file["temp_path"], existing_file["file_name"]), "r") as data_file:
                file_lines = data_file.read().splitlines()

            index = 0
            if file_lines is not None:
                while index < len(file_lines):
                    func = re.findall(function_regex, file_lines[index])
                    if len(func) > 0:
                        func_name = self.__get_function_name(func)
                        func_lines = [file_lines[index]]
                        index += 1
                        while index < len(file_lines) and len(re.findall(function_regex, file_lines[index])) == 0:
                            if file_lines[index] != "":
                                func_lines.append(file_lines[index])
                            elif file_lines[index] == "" and func_lines[-1] != "":
                                func_lines.append(file_lines[index])
                            index += 1
                        if func_lines[-1] != "":
                            func_lines.append("")
                        functions[func_name] = func_lines
                    else:
                        index += 1
            else:
                file_lines = []
        except IOError:
            file_lines = []

        return file_lines, functions

    @staticmethod
    def __get_function_name(re_findall_list):
        """
        This function gets the name of the function from a list of results from an re.findall()
        """
        if len(re_findall_list) != 1:
            raise Exception("Only one entry should be in the list.")
        return re_findall_list[0].lstrip().split(" ")[1].split("(")[0]

    def create_constants(self, feature, functions, tag, existing_constants=None):
        """
        This function creates/updates a constants file based on the list of functions passed to it.
        """
        constants_file = self.create_constants_file_header(feature)

        constants = []

        if existing_constants is None:
            for _function in functions:
                constants.append(self.create_constant(_function, tag))
        else:
            for constant in existing_constants:
                constants.append(self.create_constant(constant, existing_constants[constant]))
        constants.sort(key=lambda x: x["constant"])
        constants_file += self.format_constants_dict(constants)
        constants_file.append("")

        return constants_file

    def create_constant(self, constant, tags):
        """
        This function creates a dictionary for a single constant with the needed tags.
        """
        constants_dict = OrderedDict()

        if isinstance(tags, str):
            tags = [tags]

        tags.sort()

        constants_dict["constant"] = constant.upper()
        constants_dict["constant_value"] = constant.lower()
        constants_dict["tags"] = tags
        constants_dict["link"] = "self.link." + constant.lower()

        return constants_dict

    def create_constants_file_header(self, feature):
        """
        This function creates the header for a constants file.
        """
        header = list()

        header.append('"""')
        header.append("This class outlines all the constants for the " + feature + " API.")
        header.append("")
        header.append("Although the constants are a dictionary you do not need to pass a key to retrieve a constant.")
        header.append("The super class handles that. Simply call <feature>Constants.<constant> and the string at ")
        header.append("key \"constant\" will be returned.")
        header.append("")
        header.append("The tags are for generation purposes and can be ignored.")
        header.append("The link key is useful in pycharm to navigate to the API referenced by the constant.")
        header.append("")
        header.append("Example...")
        header.append(">> print(" + feature.capitalize() + "Constants().<SOME_CONSTANT>)")
        header.append("some_constant")
        header.append('"""')
        header.append("from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants")
        header.append("")
        header.append("")
        header.append("class " + feature.capitalize() + "Constants(ApiConstants):")
        header.append(self.create_indent(1) + "def __init__(self):")
        header.append(self.create_indent(2) + "super(" + feature.capitalize() + "Constants, self).__init__()")

        return header

    def format_constants_dict(self, constants):
        """
        This function parses the constants dictionary and creates the next to add to the constants file.
        """
        constants_list = []

        for index, constants_dict in enumerate(constants):
            constants_list.append(self.create_indent(2) + "self." + constants_dict["constant"].upper() +
                                  ' = {"constant": "' + constants_dict["constant_value"] + '",')
            constants_list.append((" " * (len(constants_list[index * 3].split("=")[0]) + 3)) +
                                  '"tags": [' + ", ".join(['"' + i + '"' for i in constants_dict["tags"]]) + "],")
            constants_list.append((" " * (len(constants_list[index * 3].split("=")[0]) + 3)) +
                                  '"link": ' + constants_dict["link"] + "}")

        return constants_list

    # Utils
    @staticmethod
    def get_args_from_string(string):
        """
        This function searches a given string for instances of {some_text}, then returns a list of the
        values that match that format.
        """
        if string is not None:
            arg_regex = "{(.*?)}"
            args = re.findall(arg_regex, string)

            return args
        else:
            return []

    def format_string_with_args(self, string, arg_dict_name="arg_dictionary", line_indent_len=0):
        """
        This function creates the text for a python string format.

        For example the string "create vlan {vlan} tag {tag}" would be returned as

        "create vlan {0} tag {1}".format(arg_dictionary["vlan"], arg_dictionary["tag"])
        """
        if string is None:
            return "None"
        else:
            formatted_string = '"' + string.replace('\"', '\\"') + '"'

        str_args = self.get_args_from_string(string)

        # Replace each argument in the command, prompt, and confirmation field with "{#}".
        for i, arg in enumerate(str_args):
            formatted_string = formatted_string.replace("{" + arg + "}", "{" + str(i) + "}", 1)

        # Create a Dictionary of arg/value pairs, argument function calls will be filled out here.
        arg_values = []
        for val in str_args:
            if re.findall(r"^\[.*?\]$", val):
                val = re.findall(r"^\[(.*?)\]$", val)[0]
            if "<" in val:
                func, args = self._get_arg_functions(val)
                if len(args) == 1:
                    arg_values.append("self.{0}({1}['{2}'])".format(func, arg_dict_name, args[0]))
                else:
                    arg_value = "self.{0}(".format(func)
                    for arg in args:
                        arg_value += "{0}['{1}'], ".format(arg_dict_name, arg)
                    arg_values.append(arg_value[:-2] + ")")
            else:
                arg_values.append("{0}['{1}']".format(arg_dict_name, val))

        # Check if we have any args in the string.
        # If there is exactly 1 add string in the following format.
        # "cmd with {1} arg".format(<arg_dict_name>[<arg>])
        # Otherwise use the following format.
        # "cmd with {1} or more {2} args {3}".format(<arg_dict_name>[<arg>],
        #                                            <arg_dict_name>[<arg>],
        #                                            <arg_dict_name>[<arg>])
        if len(arg_values) == 1:
            formatted_string += ".format({0})".format(arg_values[0])
        else:
            indent = 0
            for index, arg in enumerate(arg_values):
                if index == 0:
                    indent_str = "{0}.format(".format(formatted_string)
                    full_str = "{0}{1},\n".format(indent_str, arg)
                    indent = len(indent_str) + line_indent_len
                    formatted_string = full_str
                elif index == len(str_args) - 1:
                    formatted_string += "{0}{1})".format(" " * indent, arg)
                else:
                    formatted_string += "{0}{1},\n".format(" " * indent, arg)

        return formatted_string

    def device_type_import(self):
        """
        This function returns the device type for use in an import statement.
        """
        return "".join([i.capitalize() for i in self.device_type.split("_")])

    def fix_import_line_length(self, import_str, max_len=120):
        """
        This function checks an import string's length and if it is longer than 120 characters it splits into
        multiple lines.
        """
        return_list = []

        # First check if the import string needs to be re-sized.
        if len(import_str) > max_len:
            # Set the while loop start index to the max length - 2. We subtract 2 because
            # any re-sized lines will have 2 characters, " \" appended.
            end_index = max_len - 2

            # Iterate over the import string starting with <end_index> and working backward.
            # Stop once either " " or "." is found. Ensure that any match is not preceded by
            # " ", this avoids false positives for indentation.
            while end_index > 0:
                if import_str[end_index] == ".":
                    break
                elif import_str[end_index] == " ":
                    if import_str[end_index - 1] != " ":
                        break
                end_index -= 1

            # If we found a non-zero end index append the first part of the string to the return
            # list. Then pass the second part of the string back into this function. Then
            # append each return string to the return list.
            if end_index != 0:
                return_list.append(import_str[0:end_index + 1] + "\\")
                return_val = self.fix_import_line_length(self.create_indent(1) + import_str[end_index + 1::])
                if isinstance(return_val, list):
                    return_list.append(i for i in return_val)
                else:
                    return_list.append(return_val)
            # If no end index could be found return the current import string as a list.
            else:
                return import_str
            return "\n".join(return_list)
        else:
            return import_str

    @staticmethod
    def _get_arg_functions(arg_string):
        func = re.findall(r"<(.*?)>", arg_string)
        if len(func) > 1:
            raise ValueError
        else:
            func = func[0]
            args = re.sub(r"<.*?>", "", arg_string)
            if "." in args:
                args = args.split(".")
            else:
                args = [args]
        return func, args
