import os
import re
import shutil
from distutils.dir_util import copy_tree
from collections import OrderedDict
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants

r"""
Example:
    def vlan_create_vlan_id(self, device_name, vlan, topology_name=None, mode=None, tag=None, **kwargs):
        \"\"\"
        Keyword Arguments:
        [device_name] - DESCRIPTION PLACEHOLDER
        [vlan] - DESCRIPTION PLACEHOLDER
        [topology_name] - DESCRIPTION PLACEHOLDER
        [mode] - DESCRIPTION PLACEHOLDER
        [tag] - DESCRIPTION PLACEHOLDER

        DESCRIPTION PLACEHOLDER
        \"\"\"
        args = {\"vlan\": vlan,
                \"topology_name\": vlan,
                \"mode\": mode,
                \"tag\": tag}

        return self.execute_keyword(device_name, args, self.cmd_const.CREATE_VLAN_ID, **kwargs)
"""


class CreateCliKeywords(object):
    def __init__(self):
        self.logger = Logger()
        self.keyword_import_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Imports")
        self.keyword_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Keywords",
                                         "NetworkElementKeywords", "GeneratedKeywords")
        self.keyword_path_static = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Keywords",
                                         "NetworkElementKeywords", "StaticKeywords")
        self.gen_temp_dir = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Keywords",
                                         "NetworkElementKeywords", "GeneratedKeywords", "GenerationTemp")
        self.kw_temp_dir = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Keywords",
                                        "NetworkElementKeywords", "GeneratedKeywords", "KeywordFileTemp")
        self.python_built_ins = ["type", "dir", "len", "str", "list", "dict", "id", "format"]
        self.command_methods = ["set", "clear", "enable", "disable", "create", "delete"]
        self.manual_keywords = ["dutlearning", "resetdevice", "unittest", "filemanagement", "hostutils", "firmware",
                                "sysinfo", "unit"]
        self.kw_files = None
        self.keyword_document_generated = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Documentation",
                                                       "Generated")
        self.allwired_file =  os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Imports","AllWired.robot")
        self.write_static_info_to_allwired_file(self.allwired_file)

    def append_dynamic_info_to_allwired_file(self, file_name, line):
        print('appending  to....' + file_name)
        with open(file_name, "a") as wired_robot:
            wired_robot.write('\n'+line)
        wired_robot.close()
    
    def write_static_info_to_allwired_file(self, file_name):
        print('writing to....' + file_name)
        list_of_hardcoded=[
            '*** Settings ***',
            'Library    ExtremeAutomation/Imports/DefaultLibrary.py',
            'Library    ExtremeAutomation/Library/Utils/NetworkElementUtils.py',
            'Library    ExtremeAutomation/Library/Utils/EndsystemElementUtils.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/NetworkElementConnectionManager.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementResetDeviceUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementFirmwareUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementHostServiceUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementHostUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementCosUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/StaticKeywords/NetworkElementFileManagementUtilsKeywords.py',
            'Library    ExtremeAutomation/Keywords/VirtualMachineKeywords/VirtualMachineManager.py',
            'Library    ExtremeAutomation/Keywords/VirtualMachineKeywords/Virtualization/VirtualMachineControl.py',
            'Library    ExtremeAutomation/Keywords/Utils/PingKeywords.py',
            'Library    ExtremeAutomation/Keywords/Utils/NetworkUtils.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/Utils/NetworkElementCliSend.py',
            'Library    ExtremeAutomation/Keywords/NetworkElementKeywords/Utils/NetworkElementRestCommandSend.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficCaptureKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficGeneratorConnectionManager.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketCreationKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficPacketInspectionKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficStatisticsKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficStreamConfigurationKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/EzTrafficValidation/TrafficValidationKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/TrafficTransmitKeywords.py',
            'Library    ExtremeAutomation/Keywords/TrafficKeywords/Utils/Constants/PacketTypeConstants.py',
            'Library    ExtremeAutomation/Keywords/UserDefinedKeywords/TrafficGeneration/TrafficGenerationUdks.py',
            'Library    ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/SetupTeardown/SetupTeardownUdks.py',
            'Library    ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L1/PortUdks.py',
            'Library    ExtremeAutomation/Keywords/UserDefinedKeywords/NetworkElements/L2/VlanUdks.py'
            '',
            ''
            ]
        
        with open(file_name, "w") as wired_robot:
            for line in list_of_hardcoded:
                wired_robot.write('\n'+line)
        wired_robot.close()
    
    def create_keywords(self, data_beans, keyword_info):
        """
        This function creates a single keyword file from a list of data beans.
        """
        self.__cleanup_temp_dirs()
        self.__create_directory(self.gen_temp_dir)
        self.__create_directory(self.kw_temp_dir)

        # Copy all keyword files to temp directory.
        self.kw_files = self.__copy_files_to_temp()
        self.keyword_document_generated = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation",
                                                       "Documentation",
                                                       "Generated")

        # try:
        for feature in data_beans:
            if feature not in self.manual_keywords:
                arg_dict, agent_dict = self.__generate_keyword_arg_dict(data_beans, feature)
              
                

                # Make sure keyword output path exists
                os.makedirs(self.keyword_path, exist_ok=True)
                filename = "NetworkElement" + feature.capitalize() + "GenKeywords.py"

                # Create a dictionary of existing 'verify' and helper keywords.
                verify_keywords = None
                helper_keywords = None
                import_lines = []
                for file in self.kw_files:
                    if file["file_name"] == filename:
                        orig_file = file
                        keyword_lines, verify_keywords = self.__get_verify_functions_from_existing_file(orig_file,
                                                                                                        feature)
                        helper_keywords = self.__get_helper_functions(keyword_lines)
                        import_lines = self.__get_user_import_lines(keyword_lines)

                # Generate and write all keyword lines to temp file.
                output_file = os.path.join(self.gen_temp_dir, filename)
                path_for_switch_file = "Library    ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords/"+filename
                self.append_dynamic_info_to_allwired_file(self.allwired_file, path_for_switch_file)
                #print(path_for_switch_file)
                
                with open(output_file, "w") as kw_file:
                    kw_file.write("\n".join(self.__create_keyword_header(feature, import_lines)))
                    for oper_sys in data_beans[feature].keys():
                        for platform in data_beans[feature][oper_sys].keys():
                            for version in data_beans[feature][oper_sys][platform].keys():
                                for unit in data_beans[feature][oper_sys][platform][version].keys():
                                    for bean in data_beans[feature][oper_sys][platform][version][unit]:
                                        if bean.interface_method.split("_")[0] in self.command_methods:
                                            if bean.interface_method in arg_dict.keys():
                                                kw_file.write("\n".join(
                                                    self.__create_keyword(feature, bean, arg_dict, agent_dict,
                                                                          keyword_info)))
                                              
                                                del arg_dict[bean.interface_method]
                                                
                                        else:
                                            if bean.interface_method.split("_")[0] != "show":
                                                self.logger.log_warn("Invalid method name in {0} API Definition: {1}".
                                                                     format(feature, str(bean.interface_method)))
                                                raise Exception

                    # Add existing 'verify' and 'get' keywords to the end of the file.
                    if verify_keywords:
                        kw_file.write("\n")
                        kw_file.write("\n".join(self.__create_verify_header()))
                        for verify_keyword in verify_keywords:
                            kw_file.write("\n")
                            kw_file.write("\n".join(verify_keywords[verify_keyword]))

                            arguments = re.findall('\[.*?\]',"\n".join(verify_keywords[verify_keyword]))
                            argument_pytest_string = ", ".join(arguments).replace("[","").replace("]","")
                            argument_robot_string = "  ".join(arguments).replace("[", "").replace("]", "")
                            pytest_command = "\n\n\t\tself.defaultLibrary.apiLowLevelApis." + feature + "." + verify_keyword + "(" + argument_pytest_string + ")\n"
                            robot_command = "\n\n\t\t" + verify_keyword + "  " + argument_robot_string + "\n"

                            function_header = "# API Function: " + verify_keyword + "\n\tPytest API Call: " + pytest_command + "\n\tRobot API Call: " + robot_command
                            self.__add_to_mapping_file_methods_commands(self.keyword_document_generated,
                                                                        function_header, feature.capitalize())

                    if helper_keywords:
                        kw_file.write("\n")
                        kw_file.write("\n".join(self.__create_helper_header()))
                        for helper_keyword in helper_keywords:
                            kw_file.write("\n")
                            kw_file.write("\n".join(helper_keywords[helper_keyword]))          

        # Move the generated Keywords from the temp directory in to the actual output directory.
        if os.path.exists(self.gen_temp_dir) and os.path.exists(self.keyword_path):
            copy_tree(self.gen_temp_dir, self.keyword_path)
            
            #generate the imports
            self.logger.log_debug("Creating the imports")
            self.generate_imports()
        # except Exception as e:
        #     self.logger.log_error("An exception was caught. Keyword generation aborted.")
        #     self.logger.log_error(e)
        self.__cleanup_temp_dirs()
        self.logger.log_debug("Completed")

    def __create_keyword_header(self, feature, user_imports):
        r"""
        from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import \
            NetworkElementKeywordBaseClass
        from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.VlanConstants \
            import VlanConstants as CommandConstants
        from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.VlanConstants \
            import VlanConstants as ParseConstants
        # All imports above this line will be removed after generation.
        # User imports must be added below.


        class NetworkElementVlanKeywords(NetworkElementKeywordBaseClass):
            def __init__(self):
                super(NetworkElementVlanKeywords, self).__init__()
                self.api_const = self.constants.API_VLAN
                self.cmd_const = CommandConstants()
                self.parse_const = ParseConstants()
                self.snmp_utils = NetworkElementSnmpUtils()
                        self.parse_const = ParseConstants()
        """
        header_list = list()
        has_parse_constants = False

        self.logger.log_info("Creating keyword file: NetworkElement{0}GenKeywords.py".format(feature.capitalize()))
        header_list.append('"""')
        header_list.append("Keyword class for all " + feature + " cli commands.")
        header_list.append('"""')
        header_list.append("from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import "
                           "NetworkElementKeywordBaseClass")

        # Check for ParseAPI before adding import
        parse_api_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Apis", "NetworkElement",
                                      "GeneratedApis", "ParseApis", "Constants",
                                      "{}Constants.py".format(feature.capitalize()))
        if os.path.exists(parse_api_path):
            has_parse_constants = True
            header_list.append("from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants."
                               "{0}Constants import \\\n".format(feature.capitalize()) + self.__create_indent(1) +
                               "{0}Constants as ParseConstants".format(feature.capitalize()))

        header_list.append("from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants."
                           "{0}Constants import \\\n".format(feature.capitalize()) + self.__create_indent(1) +
                           "{0}Constants as CommandConstants".format(feature.capitalize()))
        header_list.append("# All imports above this line will be removed after generation.")
        header_list.append("# User imports must be added below.")
        header_list.extend(user_imports)
        header_list.append("")
        header_list.append("")
        header_list.append("class NetworkElement{0}GenKeywords(NetworkElementKeywordBaseClass):".format(feature.
                                                                                                        capitalize()))
        header_list.append(self.__create_indent(1) + "def __init__(self):")
        header_list.append(self.__create_indent(2) +
                           "super(NetworkElement{0}GenKeywords, self).__init__()".format(feature.capitalize()))
        header_list.append(self.__create_indent(2) + "self.cmd_const = CommandConstants()")
        if has_parse_constants:
            header_list.append(self.__create_indent(2) + "self.parse_const = ParseConstants()")
        header_list.append(self.__create_indent(2) + "self.api_const = \"" + feature + "\"")
        header_list.append("")

        return header_list

    def __create_keyword(self, feature, data_bean, kw_arg_dict, os_agent_dict, keyword_info):
        """
        Example:
            def vlan_create_vlan_id(self, device_name, vlan='', topology_name='', mode='', tag='', **kwargs):
                /"/"/"
                Keyword Arguments:
                [device_name] - DESCRIPTION PLACEHOLDER
                [vlan] - DESCRIPTION PLACEHOLDER
                [topology_name] - DESCRIPTION PLACEHOLDER
                [mode] - DESCRIPTION PLACEHOLDER
                [tag] - DESCRIPTION PLACEHOLDER

                DESCRIPTION PLACEHOLDER
                /"/"/"
                args = {/"vlan/": vlan,
                        /"topology_name/": vlan,
                        /"mode/": mode,
                        /"tag/": tag}

                return self.execute_keyword(device_name, args, self.cmd_const.CREATE_VLAN_ID, **kwargs)
        """
        function_list = list()
        function_list.append("")

        # Create the function definition line and arg list
        def_line, args, list_value_in_args = self.__create_def_line(feature, data_bean.interface_method, kw_arg_dict,
                                                                    keyword_info["arg_order"][feature],
                                                                    keyword_info["rest_data_args"][feature])
        function_list.extend(self.__check_def_line_length(def_line))

        # Add keyword desciption to function list and supported platforms
        function_list.append(self.__create_indent(2) + "\"\"\"")
        try:
            description = keyword_info["descriptions"][feature][data_bean.interface_method]
            if description == "":
                description = "Not provided in CSV"
            desc_line = self.__create_indent(2) + "Description: " + description + "."
            function_list.extend(self.__check_desc_line_length(desc_line))
        except KeyError:
            desc_line = self.__create_indent(2) + "Description: Not provided in API definition file."
            function_list.extend(self.__check_desc_line_length(desc_line))
        function_list.append("")

        # Add list of supported agents/OSes
        function_list.append(self.__create_indent(2) + "Supported Agents and OS:")
        for agent in os_agent_dict[data_bean.interface_method]:
            function_list.append(self.__create_indent(3) + agent + ": " + ", ".join(
                os_agent_dict[data_bean.interface_method][agent]))

        function_list.append(self.__create_indent(2) + "\"\"\"")

        # create arg dictionary
        if len(args) == 0:
            function_list.append(self.__create_indent(2) + "args = {}\n")
        else:
            function_list.append(self.__create_indent(2) + "args = {")
            for arg in args:
                if arg in self.python_built_ins:
                    function_list.append(self.__create_indent(3) + '"{0}": _{0},'.format(arg))
                else:
                    function_list.append(self.__create_indent(3) + '"{0}": {0},'.format(arg))
            if function_list[-1].endswith(","):
                last_arg = function_list[-1][:-1]
                function_list = function_list[:-1]
                function_list.append(last_arg)
            function_list.append(self.__create_indent(2) + "}\n")
            
        if list_value_in_args:
            function_list.append(self.__create_indent(2) + "return self.execute_keyword(device_name, args,\n" +
                                 self.__create_indent(9) + "self.cmd_const." + data_bean.interface_method.upper() +
                                 ",\n" + self.__create_indent(9) + "list_value_arg=True,\n" +
                                 self.__create_indent(9) + "wait_for_prompt=False,\n" +
                                 self.__create_indent(9) + "**kwargs)")
        else:
            function_list.append(self.__create_indent(2) + "return self.execute_keyword(device_name, args,\n" +
                                 self.__create_indent(9) + "self.cmd_const." + data_bean.interface_method.upper() +
                                 ",\n" + self.__create_indent(9) + "**kwargs)")
        function_list.append("")

        return function_list

    def __generate_keyword_arg_dict(self, data_beans, feature):
        """
        This function get a dictionary of individual keyword names with corresponding supported os and returns it.
        """
        keyword_dict = {}
        os_agent_support = {}
        for oper_sys in data_beans[feature].keys():
            for platform in data_beans[feature][oper_sys].keys():
                for version in data_beans[feature][oper_sys][platform].keys():
                    for unit in data_beans[feature][oper_sys][platform][version].keys():
                        for bean in data_beans[feature][oper_sys][platform][version][unit]:

                            # Add agent type to supported OS dict
                            if bean.agent == GenerationConstants.AGENT_TYPE_CLI:
                                os_agent_support.setdefault(bean.interface_method, {}).\
                                    setdefault(GenerationConstants.AGENT_TYPE_CLI, []).append(bean.operating_system)
                            if bean.agent == GenerationConstants.AGENT_TYPE_SNMP:
                                os_agent_support.setdefault(bean.interface_method, {}).\
                                    setdefault(GenerationConstants.AGENT_TYPE_SNMP, []).append(bean.operating_system)
                            if bean.agent == GenerationConstants.AGENT_TYPE_REST:
                                os_agent_support.setdefault(bean.interface_method, {}).\
                                    setdefault(GenerationConstants.AGENT_TYPE_REST, []).append(bean.operating_system)

                            # get any args from the various command fields
                            if hasattr(bean, 'command'):
                                args = self.__parse_command_args(bean.command)
                                if args is not None:
                                    keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'uri'):
                                args = self.__parse_command_args(bean.uri)
                                if args is not None:
                                    keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'oid'):
                                args = self.__parse_command_args(bean.oid)
                                if args is not None:
                                    keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'prompt_arguments'):
                                if bean.prompt_arguments is not None:
                                    args = self.__parse_command_args(bean.prompt_arguments)
                                    if args is not None:
                                        keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'confirmation_argument'):
                                if bean.confirmation_argument is not None:
                                    args = self.__parse_command_args(bean.confirmation_argument)
                                    if args is not None:
                                        keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'headers'):
                                if bean.headers is not None:
                                    args = self.__parse_command_args(bean.headers)
                                    if args is not None:
                                        keyword_dict.setdefault(bean.interface_method, []).extend(args)
                            if hasattr(bean, 'value'):
                                if bean.value is not None:
                                    args = self.__parse_command_args(bean.value)
                                    if args is not None:
                                        keyword_dict.setdefault(bean.interface_method, []).extend(args)

        return keyword_dict, os_agent_support
          
    # +----------------+
    # | Helper Methods |
    # +----------------+
    @staticmethod
    def __parse_command_args(cmd):
        """
        This function returns all variables within an NBI query.
        """
        return re.findall("{(.*?)}", cmd)

    @staticmethod
    def __create_indent(number):
        """
        This function creates a string of whitespace that is 4 * <number> characters long.
        """
        return (" " * 4) * number

    @staticmethod
    def __create_verify_header():
        header_list = ["    # #########################################################################################"
                       "#########################",
                       "    #   Inspection Keywords   #################################################################"
                       "#########################",
                       "    # #########################################################################################"
                       "#########################\n"]
        return header_list

    @staticmethod
    def __create_helper_header():
        header_list = ["    # #########################################################################################"
                       "#########################",
                       "    #   Non-keyword helper functions   ########################################################"
                       "#########################",
                       "    # #########################################################################################"
                       "#########################"]
        return header_list

    def __create_def_line(self, feature, interface_method, kw_arg_dict, arg_order, rest_data_args):
        list_value_in_args = False
        def_line = "def {0}_".format(feature) + interface_method.lower() + "(self, device_name,"

        # get list of all required arguments for all platforms
        args = []
        for val in kw_arg_dict[interface_method]:
            # Check for list() arguments
            if re.findall(r"^\[.*?\]$", val):
                list_value_in_args = True
                val = re.findall(r"^\[(.*?)\]$", val)[0]

            # Check for API Utility function calls
            if "<" in val:
                func, arg_list = self.__get_arg_functions(val)
                for arg in arg_list:
                    args.append(arg)
            else:
                args.append(val)

        # remove any duplicates
        if interface_method in rest_data_args:
            if rest_data_args[interface_method] is not None:
                args.extend([a.strip() for a in rest_data_args[interface_method].split(",")])
        args = list(set(args))
        args.sort()

        # Check argument order from API definitions
        ordered_args = []
        if interface_method in arg_order:
            if arg_order[interface_method] is not None:
                if ">" in arg_order[interface_method].strip():
                    for arg in arg_order[interface_method].strip().split(">"):
                        if arg in args:
                            ordered_args.append(arg)
                elif "," in arg_order[interface_method].strip():
                    for arg in arg_order[interface_method].strip().split(","):
                        if arg in args:
                            ordered_args.append(arg)
                else:
                    if arg_order[interface_method].strip() in args:
                        ordered_args.append(arg_order[interface_method].strip())

        args_other = [arg for arg in args if arg not in ordered_args]

        for arg in ordered_args:
            if arg in self.python_built_ins:
                def_line += " _{0}='',".format(arg)
            else:
                def_line += " {0}='',".format(arg)
        for arg in args_other:
            if arg in self.python_built_ins:
                def_line += " _{0}='',".format(arg)
            else:
                def_line += " {0}='',".format(arg)

        def_line += " **kwargs):"
        def_line = self.__create_indent(1) + def_line

        return def_line, args, list_value_in_args

    def __check_def_line_length(self, line):
        """
        Return the line(s) with corrected length 120 (max).

        line - The line of code to check.
        """
        total_lines = []
        if "{" in line:
            len_open = len(line.split("{")[0]) + 1
        elif "(" in line:
            len_open = len(line.split("(")[0]) + 1
        else:
            len_open = len(line) - len(line.lstrip(" "))

        if len(line) > 120:
            first_line = line[:119]
            total_lines.append(",".join(first_line.split(",")[:-1]) + ",")

            next_line = ((" " * len_open) + (first_line.split(",")[-1].strip() + line[119:].lstrip()))
            if len(next_line) > 120:
                next_lines = self.__check_def_line_length(next_line)
                total_lines.extend(next_lines)
            else:
                total_lines.append(next_line)
        else:
            total_lines.append(line)

        return total_lines

    def __check_desc_line_length(self, line):
        """
        Return the line(s) with corrected length 120 (max).

        line - The line of code to check.
        """
        total_lines = []
        if len(line) > 120:
            first_line = line[:119]
            total_lines.append(" ".join(first_line.split(" ")[:-1]))

            next_line = ((" " * 21) + (first_line.split(" ")[-1].strip() + line[119:].lstrip()))
            if len(next_line) > 120:
                next_lines = self.__check_desc_line_length(next_line)
                total_lines.extend(next_lines)
            else:
                total_lines.append(next_line)
        else:
            total_lines.append(line)

        return total_lines

    def __copy_files_to_temp(self):
        file_list = []

        for dir_path, dir_names, file_names in os.walk(self.keyword_path):
            for file_name in file_names:
                if file_name.lower().endswith("keywords.py") and not file_name.startswith("__"):
                    file_dict = {"path": dir_path,
                                 "file_name": file_name,
                                 "temp_path": self.kw_temp_dir + dir_path.replace(self.keyword_path, ""),
                                 "rel_path": dir_path.replace(self.keyword_path, "")
                                 }

                    file_list.append(file_dict)

        for _file in file_list:
            if isinstance(_file, dict):
                try:
                    os.makedirs(_file["temp_path"])
                except OSError:
                    pass

                shutil.copy(os.path.join(_file["path"], _file["file_name"]),
                            os.path.join(_file["temp_path"], _file["file_name"]))

        return file_list

    def __get_verify_functions_from_existing_file(self, existing_file, feature):
        """
        This function returns all function lines from an existing file.
        """
        functions = OrderedDict()
        function_regex = r"^    def [a-zA-Z_0-9]*\("
        block_comment = "# " + ("#" * 110)

        try:
            with open(os.path.join(existing_file["temp_path"], existing_file["file_name"]), "r") as data_file:
                file_lines = data_file.read().splitlines()

            index = 0
            if file_lines is not None:
                while index < len(file_lines):
                    func = re.findall(function_regex, file_lines[index])
                    if len(func) > 0:
                        func_name = self.__get_function_name(func)
                        if func_name.split("_")[1] == "verify" and func_name.split("_")[0] == feature and '#' not in func_name:
                            func_lines = [file_lines[index]]
                            index += 1
                            while index < len(file_lines) and \
                                    len(re.findall(function_regex, file_lines[index])) == 0 and \
                                    block_comment not in file_lines[index] and \
                                    "@staticmethod" not in file_lines[index]:
                                if file_lines[index] != "":
                                    func_lines.append(file_lines[index])
                                elif file_lines[index] == "" and func_lines[-1] != "":
                                    func_lines.append(file_lines[index])
                                index += 1
                            if func_lines[-1] != "":
                                func_lines.append("")
                            functions[func_name] = func_lines
                        elif "verify" in func_name.split("_") and '#' not in func_name:
                            error_msg = "ERROR! Verify keyword has an invalid name and will be commented out: " + func_name
                            self.logger.log_error(error_msg + "\n")
                            comment = "# "
                            func_lines = []
                            func_lines.append(comment + " ERROR! Verify keyword has an invalid name and will be commented out. ") 
                            func_lines.append(comment + "The format must be <protocol>_verify_<name>. ")
                            func_lines.append(comment + "Please uncomment this code and rename the function to be in the ") 
                            func_lines.append(comment +  "correct format. Then you can run the generator again.")
                            func_lines.append(comment + file_lines[index])
                            index += 1
                            while index < len(file_lines) and \
                                    len(re.findall(function_regex, file_lines[index])) == 0 and \
                                    block_comment not in file_lines[index] and \
                                    "@staticmethod" not in file_lines[index]:
                                if file_lines[index] != "":
                                    func_lines.append(comment + file_lines[index])
                                elif file_lines[index] == "" and func_lines[-1] != "":
                                    func_lines.append(comment + file_lines[index])
                                index += 1
                            if func_lines[-1] != "":
                                func_lines.append("")
                            functions[func_name] = func_lines
                        else:
                            index += 1
                    else:
                        index += 1
            else:
                file_lines = []
        except IOError:
            file_lines = []

        return file_lines, functions

    def __get_helper_functions(self, file_lines):
        """
        This function returns all function lines from an existing file.
        """
        functions = OrderedDict()
        helper_function_regex = r"^    def [_]{2}[a-zA-Z_0-9]*[^_]\("
        any_function_regex = r"^    def [a-zA-Z_0-9]*\("
        block_comment = "# " + ("#" * 110)

        index = 0
        if file_lines is not None:
            while index < len(file_lines):
                func = re.findall(helper_function_regex, file_lines[index])
                if len(func) > 0:
                    func_name = self.__get_function_name(func)
                    func_lines = [file_lines[index]]
                    if "@staticmethod" in file_lines[index - 1]:
                        func_lines.insert(0, file_lines[index - 1])
                    index += 1
                    while index < len(file_lines) and \
                            len(re.findall(any_function_regex, file_lines[index])) == 0 and \
                            block_comment not in file_lines[index] and \
                            "@staticmethod" not in file_lines[index]:
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

        return functions

    @staticmethod
    def __get_function_name(re_findall_list):
        """
        This function gets the name of the function from a list of results from an re.findall()
        """
        if len(re_findall_list) != 1:
            raise Exception("Only one entry should be in the list.")
        return re_findall_list[0].lstrip().split(" ")[1].split("(")[0]

    @staticmethod
    def __get_user_import_lines(keyword_lines):
        import_lines = []

        default_imports = True
        index = 0
        if keyword_lines is not None:
            while index < len(keyword_lines):
                if "# User imports must be added below." in keyword_lines[index]:
                    default_imports = False
                    index += 1
                elif not default_imports:
                    if keyword_lines[index].startswith("import") or keyword_lines[index].startswith("from"):
                        import_lines.append(keyword_lines[index])
                        index += 1
                        while index < len(keyword_lines):
                            if keyword_lines[index].strip() == "" or keyword_lines[index].startswith("class"):
                                break
                            else:
                                import_lines.append(keyword_lines[index])
                            index += 1
                    elif keyword_lines[index].startswith("class"):
                        break
                    else:
                        index += 1
                else:
                    index += 1
        return import_lines

    def __create_directory(self, path):
        """
        This function creates the given directory and adds an __init__.py file to it.
        """
        try:
            os.makedirs(path)
            self.__create_python_init_file(path)
        except OSError:
            pass

    def __cleanup_temp_dirs(self):
        """
        This function removes any temporary directories that exist.
        """
        if os.path.exists(self.gen_temp_dir):
            shutil.rmtree(self.gen_temp_dir)
        if os.path.exists(self.kw_temp_dir):
            shutil.rmtree(self.kw_temp_dir)

    def __get_arg_functions(self, arg_string):
        func = re.findall(r"<(.*?)>", arg_string)
        if len(func) > 1:
            self.logger.log_info(str(func))
            self.logger.log_error("Invalid argument function. Too many matches found!")
            raise ValueError
        else:
            func = func[0]
            args = re.sub(r"<.*?>", "", arg_string)
            if "." in args:
                args = args.split(".")
            else:
                args = [args]
        return func, args

    @staticmethod
    def __create_python_init_file(path):
        """
        This function creates an __init__.py file within the given path.
        """
        file_name = "__init__.py"
        open(os.path.join(path, file_name), "w").close()
        
        
    def generate_imports(self):
        file_lines = []
    
        keyword_files, static_keyword_files = self.get_keyword_files()
        for name in keyword_files:
            feature_name = name.replace('.py', '')
            new_import_line = f"from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.{feature_name} import {feature_name}"
    
            file_lines.append(new_import_line)
        
        for name in static_keyword_files:
            feature_name = name.replace('.py', '')
            new_import_line = f"from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.{feature_name} import {feature_name}"
    
            file_lines.append(new_import_line)
    
        file_lines.append("")
        file_lines.append("")
        file_lines.append("class LowLevelApis:")
        file_lines.append("    def __init__(self):")
    
        for name in keyword_files:
            feature_name = name.replace('NetworkElement', '').replace('GenKeywords.py', '').lower()
            new_instance_line = f"        self.{feature_name} = {name.replace('.py', '')}()"
    
            file_lines.append(new_instance_line)
            
        for name in static_keyword_files:
            feature_name = name.replace('NetworkElement', '').replace('Keywords.py', '')
            feature_name = feature_name[0].lower() + feature_name[1:]
            new_instance_line = f"        self.{feature_name} = {name.replace('.py', '')}()"
    
            file_lines.append(new_instance_line)
    
        with open(os.path.join(self.keyword_import_path, "LowLevelApis.py"), "w") as file:
            file.write("\n".join(file_lines) + "\n")
    
    
    def get_keyword_files(self):
        keyword_files = set()
        static_keyword_files = set()
    
        for dirpath, dirnames, filenames in os.walk(self.keyword_path):
            for filename in filenames:
                if filename.startswith("NetworkElement") and filename.endswith(".py"):
                    keyword_files.add(filename)
    
    
        # Add in the static ones too
        for dirpath, dirnames, filenames in os.walk(self. keyword_path_static):
            for filename in filenames:
                if filename.startswith("NetworkElement") and filename.endswith("UtilsKeywords.py"):
                    static_keyword_files.add(filename)  
        return keyword_files, static_keyword_files

    def __add_to_mapping_file_methods_commands(self, mappingdir, method_command, feature):
        mappingfilename = os.path.join(mappingdir, feature + '.md')
        with open(mappingfilename, "a") as file_object:
            file_object.write(method_command + "\n")

