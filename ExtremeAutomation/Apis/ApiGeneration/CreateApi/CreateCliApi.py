from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateApi import CreateApi
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants


class CreateCliApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single API file for a given data bean list.
        """
        api_list = list()
        valid_methods = ["set", "clear", "enable", "disable", "create", "delete", "show", "reset", "login", 'bypass', 'run']
        manual_methods = ["dutlearning", "unittest", "filemanagement", "hostutils", "firmware", "unit"]

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        api_list += self.__create_file_header(data_bean_list[0], feature)

        for data_bean in data_bean_list:
            if data_bean.agent == GenerationConstants.AGENT_TYPE_CLI:
                if self.device_type == "network_element":
                    if data_bean.interface_method.split("_")[0] in valid_methods:
                        api_list += self.__create_function(data_bean)
                    else:
                        if feature not in manual_methods:
                            self.log.error("Invalid API method name in {0}.csv: {1}".
                                           format(feature, str(data_bean.interface_method)))
                            raise Exception
                        else:
                            api_list += self.__create_function(data_bean)
                else:
                    api_list += self.__create_function(data_bean)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        This function creates a single base API file for a given feature.
        """
        base_api_list = list()

        if len(function_list) == 0:
            raise Exception("Function list is empty.")

        base_api_list += self.__create_base_api_header(feature)

        for _function in function_list:
            base_api_list += self.__create_base_function(_function)

        return base_api_list

    def __create_file_header(self, data_bean, feature):
        r"""
        This function creates the header for a command API. The header format is as follows.

        \"\"\"
        All <feature> supported commands
        \"\"\"
        from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
        from ExtremeAutomation.Apis.<device_type>.GeneratedApis.CommandApis.<agent>.<feature>.base.
        <feature>base import <feature>Base


        class <feature>(DeviceApi, <feature>Base):
            def __init__(self, device_input):
                super(<feature>, self).__init__(device_input)

        """
        file_header = list()
        file_header.append('"""')
        file_header.append("All " + feature + " supported commands")
        file_header.append('"""')
        if data_bean.previous_version is None:
            file_header.append("from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi")
        if data_bean.previous_version is not None:
            import_str_1 = "from ExtremeAutomation.Apis." + self.device_type_import() + ".GeneratedApis.CommandApis."
            import_str_2 = ".".join([self.agent, feature, data_bean.operating_system, data_bean.platform,
                                     data_bean.previous_version[-1], data_bean.unit, feature])
            import_str_3 = " import " + feature.capitalize() + " as " + feature.capitalize() + "Base"
            file_header.append(self.fix_import_line_length(import_str_1 + import_str_2 + import_str_3))
        else:
            file_header.append(self.fix_import_line_length("from ExtremeAutomation.Apis." + self.device_type_import() +
                                                           ".GeneratedApis.CommandApis." + self.agent + "." + feature +
                                                           ".base." + feature + "base import " + feature.capitalize() +
                                                           "Base"))
        file_header.append("")
        file_header.append("")
        if data_bean.previous_version is not None:
            file_header.append("class " + feature.capitalize() + "(" + feature.capitalize() + "Base):")
        else:
            file_header.append("class " + feature.capitalize() + "(DeviceApi, " + feature.capitalize() + "Base):")
        file_header.append(self.create_indent(1) + "def __init__(self, device_input):")
        file_header.append(self.create_indent(2) + "super(" + feature.capitalize() + ", self).__init__(device_input)")
        file_header.append("")

        return file_header

    def __create_base_api_header(self, feature):
        r"""
        This method creates the header for a command base API. The header format is as follows.

        \"""
        Base class for all <feature> commands.
        \"""
        from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi


        class <feature>Base(CliBaseApi):
        """
        base_api_header = list()

        base_api_header.append('"""')
        base_api_header.append("Base class for all " + feature + " commands.")
        base_api_header.append('"""')
        base_api_header.append("from ExtremeAutomation.Library.Device.Common.Apis.CliBaseApi import CliBaseApi")
        base_api_header.append("")
        base_api_header.append("")
        base_api_header.append("class " + feature.capitalize() + "Base(CliBaseApi):")
        base_api_header.append(self.create_indent(1) + "def __init__(self, device):")
        base_api_header.append(self.create_indent(2) + "super(" + feature.capitalize() + "Base, self).__init__()")
        base_api_header.append(self.create_indent(2) + "self.device = device")
        base_api_header.append("")

        return base_api_header

    def __create_function(self, data_bean):
        r"""
        This method creates the function body text for a given data_bean. Function format is as follows.

        def method_1(self, arg_dictionary):
            uuid = <uuid>
            cmd = <command>
            prompt = <prompt> (if present)
            prompt_args = <prompt_args> (if present)
            conf = <confirmation_phrases> (if present)
            conf_args = <confirmation_args> (if present)

            self.device.add_error_to_ignore_list(*errs)
            self.device.add_error_to_temp_list(*errs)

            return self.create_cmd_obj(*args)

        """
        _function = list()
        _function.append(self.create_indent(1) + "def " + data_bean.interface_method.lower() +
                         "(self, arg_dictionary, **kwargs):")
        
        uuid_indent_str = "{0}uuid = ".format(self.create_indent(2))
        uuid_str = self.format_string_with_args(data_bean.uuid, line_indent_len=len(uuid_indent_str))
        _function.append("{0}{1}".format(uuid_indent_str, uuid_str))
        cmd_obj_args = ["uuid"]
        
        cmd_indent_str = "{0}cmd = ".format(self.create_indent(2))
        cmd_str = self.format_string_with_args(data_bean.command, line_indent_len=len(cmd_indent_str))
        _function.append("{0}{1}".format(cmd_indent_str, cmd_str))
        cmd_obj_args.append("cmd")

        if data_bean.prompt:
            _function.append("{0}prompt = \"{1}\"".format(self.create_indent(2), data_bean.prompt))
            cmd_obj_args.append("prompt=prompt")

        if data_bean.prompt_arguments and data_bean.prompt_arguments != "None":
            prompt_arg_string = self.format_string_with_args(data_bean.prompt_arguments)
            _function.append("{0}prompt_args = {1}".format(self.create_indent(2), prompt_arg_string))
            cmd_obj_args.append("prompt_args=prompt_args")

        if data_bean.confirmation_phrase and data_bean.confirmation_phrase != "None":
            _function.append("{0}conf = \"{1}\"".format(self.create_indent(2), data_bean.confirmation_phrase))
            cmd_obj_args.append("conf=conf")

        if data_bean.confirmation_argument and data_bean.confirmation_argument != "None":
            conf_arg_string = self.format_string_with_args(data_bean.confirmation_argument, line_indent_len=20)
            _function.append("{0}conf_args = {1}".format(self.create_indent(2), conf_arg_string))
            cmd_obj_args.append("conf_args=conf_args")

        _function.append("")

        if len(data_bean.ignore_errors) != 0:
            _function.append(self.create_indent(2) + "self.device.error_checker.add_error_to_ignore_list(*[" +
                             ", ".join(['"' + i + '"' for i in data_bean.ignore_errors]) + "])")
        if len(data_bean.add_errors) != 0:
            _function.append(self.create_indent(2) + "self.device.error_checker.add_error_to_temp_list(*[" +
                             ", ".join(['"' + i + '"' for i in data_bean.add_errors]) + "])")
        if len(data_bean.ignore_errors) != 0 or len(data_bean.add_errors) != 0:
            _function.append("")

        cmd_args_str = ", ".join(cmd_obj_args)
        _function.append("{0}return self.create_cmd_obj({1})".format(self.create_indent(2), cmd_args_str))
        _function.append("")

        return _function

    def __create_base_function(self, function_name):
        """
        This method creates the function body text for a base api function. The format is as follows.

        def <function_name>(self, arg_dictionary):
            command = CliCommandObject()
            command.not_supported = True

            return command

        """
        base_function = list()

        base_function.append(self.create_indent(1) + "def " + function_name.lower() + "(self, *args, **kwargs):")
        base_function.append(self.create_indent(2) + "return self.base_function()")
        base_function.append("")

        return base_function

    def create_constant(self, constant, tag=None):
        """
        This function sets the tag type for a CLI API, then it calls its parent class's create_constant function.
        """
        tag = "COMMAND_CLI" if tag is None else tag
        return super(CreateCliApi, self).create_constant(constant, tag)
