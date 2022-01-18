import os
import re
import abc
import csv
import sys
import glob
import yaml
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.ApiUtils import ApiUtils
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.Common.ManagedDeviceObject import ManagedDeviceObject
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils


class KeywordUnitTest(object, metaclass=abc.ABCMeta):
    CON_METHOD_CLI = "telnet"
    CON_METHOD_REST = "rest"
    CON_METHOD_SNMP = "snmp"

    def __init__(self, api_path, kw_path, agent):
        self.con_method = agent
        self.api_path = os.path.join(PathUtils.get_project_root(), api_path)
        self.api_dict = self.__get_api_path_list(self.api_path)
        self.methods_to_test = self.__build_api_method_lists()
        self.dev_collection = DeviceCollectionManager()
        self.logger = Logger()

        # Build Keyword method dictionary
        self.kw_path = os.path.join(PathUtils.get_project_root(), kw_path)
        self.kw_dict = self.__get_keyword_path_list(self.kw_path)
        self.kw_test_methods = self.__build_keyword_method_lists()

        self.logger.console_level = self.logger.ALL
        self.python_built_ins = ["type", "dir", "len", "str", "list", "dict", "id", "format"]

        modules = glob.glob(os.path.join(self.kw_path, "*.py"))
        test = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f) and not f.endswith('__init__.py')]
        from_line = "ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords"
        for py in test:
            mod = __import__(".".join([from_line, py]), fromlist=[py])
            classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
            for cls in classes:
                setattr(sys.modules[__name__], cls.__name__, cls)

    def generate_tests(self, _class):
        """
        This methods generates a unit test for each row in each CSV.

        It then adds the created test to the provided class.
        """
        test_count = 1

        for feature in self.kw_test_methods:
            feature_name = re.findall("NetworkElement(.*?)GenKeywords", feature)[0]
            for keyword in self.kw_test_methods[feature]:
                keyword_name = self.kw_test_methods[feature][keyword]
                for api_feat in self.methods_to_test:
                    if feature_name.lower() == api_feat[0]["feature"].lower():
                        for api_item in api_feat:
                            if api_item["function_name"] == keyword_name:
                                self.__create_device(api_item)
                                test_name = "test" + str(test_count) + "_" + "_".join(
                                    [api_item["feature"], api_item["function_name"], api_item["os"],
                                     api_item["platform"], api_item["version"], api_item["unit"]])
                                setattr(_class, test_name, self.generate_test(feature, keyword, api_item))
                                self.logger.log_info("Creating test #" + str(test_count) + " -> " + test_name)
                                test_count += 1

    @staticmethod
    def __get_api_path_list(api_path):
        """
        This method searches recursively through the given path for any file with the extension ".csv".

        It returns a dictionary with the following format.

        return_dict = {<file_name>.csv: <full_path_of_file>}
        """
        api_paths = {}

        for dir_path, _, file_names in os.walk(api_path):
            for file_name in file_names:
                if file_name.endswith(".csv") or file_name.endswith(".yaml"):
                    api_paths[file_name] = os.path.join(dir_path, file_name)
        return api_paths

    def __build_api_method_lists(self):
        """
        This builds a list of csv method lists. The CSV method lists contain a dictionary for each line inside
        the given CSV.
        """
        api_methods = []
        for api_file in self.api_dict:
            if api_file.endswith(".csv"):
                found_methods = self.__get_csv_methods(self.api_dict[api_file])
                if found_methods:
                    api_methods.append(found_methods)
            else:
                found_methods = self.__get_yaml_methods(self.api_dict[api_file])
                if found_methods:
                    api_methods.append(found_methods)

        return api_methods

    def __get_csv_methods(self, api_path):
        """
        This opens the given CSV file and creates a list of method dictionaries.

        For each row after row 2 a method dictionary is created. The format of this dictionary differs
        depending on the type of CSV being parsed.
        """
        method_info = []
        feature = None
        kw_desc = False

        with open(api_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, row in enumerate(csv_reader):
                if i == 0:
                    feature = row[1]
                elif i > 1:
                    if len(row) != 0:
                        if row[0] == "Keyword Definitions:":
                            kw_desc = True
                        elif row[0] == "End Keyword Definitions":
                            kw_desc = False
                        elif row[0] != "#" and not kw_desc:
                            method_info.append(self.create_method_dict(feature, row))
        return method_info

    def __get_yaml_methods(self, api_path):
        """
        This opens the given CSV file and creates a list of method dictionaries.

        For each row after row 2 a method dictionary is created. The format of this dictionary differs
        depending on the type of CSV being parsed.
        """
        method_info = []

        with open(api_path, "r") as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
            feature = list(yaml_dict.keys())[0]
            for api_method in list(yaml_dict[feature].keys()):
                if isinstance(yaml_dict[feature][api_method]["apis"], list):
                    for api in yaml_dict[feature][api_method]["apis"]:
                        api_list = [api_method]
                        api_list.extend(api)
                        method_info.append(self.create_method_dict(feature, api_list))
                elif isinstance(yaml_dict[feature][api_method]["apis"], dict):
                    if self.con_method in yaml_dict[feature][api_method]["apis"]:
                        for api in yaml_dict[feature][api_method]["apis"][self.con_method]:
                            api_list = [api_method]
                            api_list.extend(api)
                            method_info.append(self.create_method_dict(feature, api_list))

        return method_info

    def _get_args_from_command(self, command):
        """
        This function identifies all arguments within a given command string. It then builds a dictionary
        with the key being the variables value and a valid string as the key's value.
        """
        args = [i.strip("{}") for i in re.findall("{.*?}", command)]

        arg_list = []
        for arg in args:
            if re.findall(r"^\[.*?\]$", arg):
                arg = re.findall(r"^\[(.*?)\]$", arg)[0]
            if "<" in arg:
                arg = arg.split(">")[1]
                if "." in arg:
                    arg_list.extend(arg.split("."))
                else:
                    arg_list.append(arg)
            else:
                arg_list.append(arg)

        return self.__generate_arg_dict(arg_list)

    @staticmethod
    def __generate_arg_dict(command_args):
        """
        This function generates a dictionary from a list of command_args.

        The dictionary format is as follows.

        return_dict = {"arg1": "test_val_arg1",
                       "arg2": "test_val_arg2"}
        """
        return dict((i, "test_val_" + i) for i in command_args)

    @staticmethod
    def __get_keyword_path_list(kw_path):
        """
        This method searches recursively through the given path for any file with the extension "Keywords.py".

        It returns a dictionary with the following format.

        return_dict = {<file_name>.csv: <full_path_of_file>}
        """
        kw_paths = {}

        for dir_path, _, file_names in os.walk(kw_path):
            for file_name in file_names:
                if file_name.endswith("Keywords.py"):
                    kw_paths[file_name] = os.path.join(dir_path, file_name)
        return kw_paths

    def __build_keyword_method_lists(self):
        """
        This builds a list of csv method lists. The CSV method lists contain a dictionary for each line inside
        the given CSV.
        """
        kw_methods = {}
        for kw_file in self.kw_dict:
            method_info, feature = self.__get_keyword_methods(self.kw_dict[kw_file])
            kw_methods[feature] = method_info

        return kw_methods

    @staticmethod
    def __get_keyword_methods(kw_path):
        """
        This opens the given CSV file and creates a list of method dictionaries.

        For each row after row 2 a method dictionary is created. The format of this dictionary differs
        depending on the type of CSV being parsed.
        """
        method_info = {}
        feature = re.findall(r"(NetworkElement[a-zA-Z0-9]*Keywords).py", str(kw_path))[0]
        keyword_regex = r"^    def ([^_][a-zA-Z_0-9]*)\("
        block_comment = "# " + ("#" * 110)

        with open(kw_path, "r") as kw_file:
            file_lines = kw_file.readlines()
            index = 0
            while index < len(file_lines):
                keyword = re.findall(keyword_regex, file_lines[index])
                if len(keyword) > 0:
                    index += 1
                    while (index < len(file_lines) and
                           len(re.findall(keyword_regex, file_lines[index])) == 0 and
                           block_comment not in file_lines[index] and
                           "@staticmethod" not in file_lines[index]):
                        if "self.cmd_const" in file_lines[index]:
                            api_index = file_lines[index].split(".").index("cmd_const") + 1
                            method_info[keyword[0]] = file_lines[index].split(".")[api_index].split(",")[0].lower()
                        index += 1
                else:
                    index += 1

        return method_info, feature

    @staticmethod
    def _get_device_name(csv_row):
        """
        This function creates a device's string name from a given csv_row.
        The format is as follows.

        return_string = "<os>_<platform>_<version>_<unit>"
        """
        return "_".join([csv_row["os"], csv_row["platform"], csv_row["version"], csv_row["unit"]])

    def _generate_return_command(self, command, args):
        """
        This function substitutes in values from the generated arg dictionary into the command being sent.

        For example if the command was

        command = "Command with {arg1} and {arg2}"
        command = "Command with {arg1} and {<api_utils.some_func>arg2} and {<api_utils.some_func2>arg3.arg4}"

        The return command would be as follows.

        return_command = "Command with test_val_arg1 and test_val_arg2"
        return_command = "Command with test_val_arg1 and opt1 test_val_arg2 and opt2 test_val_arg3 opt3 test_val_arg4"
        """
        if args:
            return_command = command

            # Remove list wrappers in API arguments. All args will be strings for Unit Test.
            if re.findall(r"{\[.*?\]}", return_command):
                return_command = re.sub(r"{\[", "{", return_command)
                return_command = re.sub(r"\]}", "}", return_command)

            # Check for function calls in the API command
            if "<" in return_command:
                func_calls = re.findall("{<.*?>.*?}", return_command)
                for func_call in func_calls:
                    func_name = re.findall("<.*?>", func_call)[0].strip("<>")
                    func_args = re.sub("<.*?>", "", func_call).strip("{}").split(".")

                    # Replace the arg names with the test values
                    new_args = []
                    for func_arg in func_args:
                        if func_arg in args:
                            new_args.append(args[func_arg])
                        else:
                            new_args.append(func_arg)

                    # Pass test values to the appropriate util and replace the original API arg
                    func_class = ApiUtils()
                    if func_name.split(".")[0] == "str_utils":
                        func_class = StringUtils()
                    elif func_name.split(".")[0] == "snmp_utils":
                        func_class = SnmpUtils()
                    func_return = getattr(func_class, func_name.split(".")[1])(*new_args)
                    try:
                        return_command = return_command.replace(func_call, func_return)
                    except TypeError as error:
                        self.logger.log_error("API function " + func_name.split(".")[0] + "." +
                                              func_name.split(".")[1] + " returned 'None' for arg(s):" +
                                              str(func_args))
                        raise error

            # Replace the remaining non-function args
            for arg in args:
                return_command = return_command.replace("{" + arg + "}", args[arg])
            return return_command
        return command

    def generate_test(self, feature, keyword_name, method_dict):
        """
        This function generates a test function.

        The test function gets the necessary information from the passed method dictionary.

        It then verifies that the command send and the expected command are equal.
        """
        def generated_test(_self):
            """This is the test function that is created to be executed later."""
            dev_name = self._get_device_name(method_dict)
            args = method_dict["command_args"]
            for arg in args:
                if arg in self.python_built_ins:
                    args["_" + arg] = args[arg]
                    args.pop(arg)

            feat_class = eval(feature)()
            if "verify" in keyword_name:
                verify_args = getattr(feat_class, keyword_name).__code__.co_varnames
                for verify_arg in verify_args:
                    if verify_arg not in args and verify_arg not in ["self", "device_name", "kwargs", "args"]:
                        args[verify_arg] = "test_val_" + verify_arg
                result, _ = getattr(feat_class, keyword_name)(dev_name, **args, get_only=True)
            else:
                result = getattr(feat_class, keyword_name)(dev_name, **args)
            if isinstance(result, list):
                result = result[0]
            _self.assertEqual(result.command, method_dict["return_command"])
        return generated_test

    def __create_device(self, csv_row):
        """
        This function creates the needed dummy devices.

        First it generates the device name. If the device name does not yet exist in the device collection
        it is created and added to the collection.
        """
        device_name = self._get_device_name(csv_row)
        if device_name not in self.dev_collection.device_dict:
            device = DummyDeviceObject().create_dummy_device(csv_row["os"], csv_row["platform"], csv_row["version"],
                                                             csv_row["unit"], self.con_method)
            self.dev_collection.add_device(device_name, device)

    # ##################################################################################################################
    #    Abstract Methods    ###########################################################################################
    # ##################################################################################################################
    @abc.abstractmethod
    def create_method_dict(self, feature, csv_row):
        """
        This method MUST be overridden by any child classes. This methods describes how to created a
        method dictionary for a given CSV row.
        """
        pass


class DummyDeviceObject(ManagedDeviceObject):
    def __init__(self):
        super(DummyDeviceObject, self).__init__()

    @staticmethod
    def create_dummy_device(oper_sys, platform, version, unit, con_method):
        dev = NetworkElement(oper_sys, platform, unit, version)
        dev.connection_method = con_method
        dev.current_agent = dev.agent_dict[con_method](dev)
        dev.current_agent.connected = True
        dev.current_agent.logged_in = True
        dev.__class__ = DummyDeviceObject
        return dev

    def get_api(self, name):
        self.__class__ = NetworkElement
        if isinstance(self, NetworkElement):
            api = NetworkElement.get_api(self, name)
        else:
            api = None
        self.__class__ = DummyDeviceObject
        return api

    def get_parse_api(self, name):
        self.__class__ = NetworkElement
        if isinstance(self, NetworkElement):
            api = NetworkElement.get_parse_api(self, name)
        else:
            api = None
        self.__class__ = DummyDeviceObject
        return api

    def connect(self, *args):
        pass

    def disconnect(self, *args, **kwargs):
        pass

    def get_base_attrs(self):
        """
        This function creates the base_attrs list which is needed for the API factories. It first tries
        to find a matching PLATFORM_<OS>_BASE in the NetworkElementConstants. If it is unable
        to find a match PLATFORM_BASE is used instead.
        """
        try:
            base_attrs = [getattr(NetworkElementConstants, "PLATFORM_" + self.oper_sys + "_BASE"),
                          NetworkElementConstants.VERSION_BASE,
                          NetworkElementConstants.UNIT_BASE
                          ]
        except AttributeError:
            base_attrs = [NetworkElementConstants.PLATFORM_BASE,
                          NetworkElementConstants.VERSION_BASE,
                          NetworkElementConstants.UNIT_BASE
                          ]

        return base_attrs

    @staticmethod
    def send_command_object(cmd_obj):
        return cmd_obj
