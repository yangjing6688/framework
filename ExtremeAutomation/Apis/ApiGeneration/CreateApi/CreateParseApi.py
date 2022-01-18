from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateCliApi import CreateApi


class CreateParseApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        Creates a single API file for a give data bean list.
        """
        functions = list()
        api_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        if "existing_api_file" in kwargs:
            if kwargs["existing_api_file"] is not None:
                api_list, functions = self.get_functions_from_existing_file(kwargs["existing_api_file"])
                api_list = self.__update_file_imports(api_list, data_bean_list[0], feature)
                if api_list[-1] != "":
                    api_list.append("")

        if len(api_list) == 0:
            api_list = self.__create_file_header(data_bean_list[0], feature) + api_list

        for data_bean in data_bean_list:
            if data_bean.agent == self.agent:
                if data_bean.interface_method != "":
                    if data_bean.interface_method not in functions:
                        api_list += self.__create_function(data_bean)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        Creates a single base API file for a given feature.
        """
        base_api_list = list()

        if len(function_list) == 0:
            raise Exception("Function list is empty.")

        base_api_list += self.__create_base_api_header(feature)

        for _function in function_list:
            base_api_list += self.__create_base_function(_function)

        base_api_list += self.__create_base_api_footer()

        return base_api_list

    def __update_file_imports(self, existing_list, data_bean, feature):
        """
        This function takes an existing file as a list and updates the imports present based on the
        passed data_bean and feature.
        """
        new_list = None
        import_list = []

        if data_bean.previous_version is not None:
            import_str_1 = "from ExtremeAutomation.Apis." + self.device_type_import() + ".GeneratedApis.ParseApis."
            import_str_2 = ".".join([self.agent, feature, data_bean.operating_system, data_bean.platform,
                                     data_bean.previous_version[-1], data_bean.unit, feature.capitalize() +
                                     "CustomShowTools"])
            import_str_3 = " import " + feature.capitalize() + "CustomShowTools as " + feature.capitalize() + \
                           "BaseCustomShowTools"
            import_list.append(self.fix_import_line_length(import_str_1 + import_str_2 + import_str_3))
        else:
            import_list.append(self.fix_import_line_length("from ExtremeAutomation.Apis." + self.device_type_import() +
                                                           ".GeneratedApis.ParseApis." + self.agent + "." + feature +
                                                           ".base." + feature.capitalize() +
                                                           "BaseCustomShowTools import " + feature.capitalize() +
                                                           "BaseCustomShowTools"))
        import_list.append("# All imports above this line will be removed after generation.")
        import_list.append("# User imports must be added below.")

        if len([i for i in existing_list
                if "# All imports above this line will be removed after generation." in i]) != 0:
            new_list = "|||".join(existing_list).split("# User imports must be added below.")[1].split("|||")
            if new_list[0] == "":
                new_list = new_list[1:]

        return import_list + new_list if new_list is not None else import_list + existing_list

    def __create_file_header(self, data_bean, feature):
        """
        This function creates the header for a parse API. Its format is as follows.

        from ExtremeAutomation.Apis.<device_type>.GeneratedApis.ParseApis.<agent>.<feature>.
        <feature>BaseCustomShowTools import <feature>BaseCustomShowTools
        # All imports above this line will be removed after generation.
        # User imports must be added below.


        class <feature>CustomShowTools(<feature>BaseCustomShowTools):
            def __init__(self, device):
                super(<feature>CustomShowTools, self).__init__()
        """
        file_header = list()

        if data_bean.previous_version is not None:
            import_str_1 = "from ExtremeAutomation.Apis." + self.device_type_import() + ".GeneratedApis.ParseApis."
            import_str_2 = ".".join([self.agent, feature, data_bean.operating_system, data_bean.platform,
                                     data_bean.previous_version[-1], data_bean.unit, feature.capitalize() +
                                     "CustomShowTools"])
            import_str_3 = " import " + feature.capitalize() + "CustomShowTools as " + feature.capitalize() + \
                           "BaseCustomShowTools"
            file_header.append(self.fix_import_line_length(import_str_1 + import_str_2 + import_str_3))
        else:
            file_header.append(self.fix_import_line_length("from ExtremeAutomation.Apis." + self.device_type_import() +
                                                           ".GeneratedApis.ParseApis." + self.agent + "." +
                                                           feature + ".base." + feature.capitalize() +
                                                           "BaseCustomShowTools import " + feature.capitalize() +
                                                           "BaseCustomShowTools"))
        file_header.append("# All imports above this line will be removed after generation.")
        file_header.append("# User imports must be added below.")
        file_header.append("")
        file_header.append("")
        file_header.append("class " + feature.capitalize() + "CustomShowTools(" + feature.capitalize() +
                           "BaseCustomShowTools):")
        file_header.append(self.create_indent(1) + "def __init__(self, device):")
        file_header.append(self.create_indent(2) + "super(" + feature.capitalize() +
                           "CustomShowTools, self).__init__(device)")
        file_header.append("")

        return file_header

    def __create_base_api_header(self, feature):
        """
        This function creates the header for a base parse API. The format is as follows.

        from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
        from ExtremeAutomation.Library.Common.CommandObjects.<command_object_type> import <command_object_type>


        class <feature>BaseCustomShowTools(BaseShowApi):
            def __init__(self, device):
                super(<feature>BaseCustomShowTools, self).__init__()
                self.device = device
                self.it = self.device.inspection_toolkit

        """
        file_header = list()

        file_header.append("from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi")

        if self.agent.upper() == "CLI":
            cmd_obj = ("from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject "
                       "import CliCommandObject")
        elif self.agent.upper() == "REST":
            cmd_obj = ("from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject "
                       "import RestCommandObject")
        elif self.agent.upper() == "SNMP":
            cmd_obj = ("from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject "
                       "import SnmpCommandObject")
        else:
            raise ValueError("Invalid agent type provided.")

        if cmd_obj is not None:
            file_header.append(cmd_obj)

        file_header.append("")
        file_header.append("")
        file_header.append("class " + feature.capitalize() + "BaseCustomShowTools(BaseShowApi):")
        file_header.append(self.create_indent(1) + "def __init__(self, device):")
        file_header.append(self.create_indent(2) + "super(" + feature.capitalize() +
                           "BaseCustomShowTools, self).__init__()")
        file_header.append(self.create_indent(2) + "self.device = device")
        file_header.append(self.create_indent(2) + "self.it = self.device.inspection_toolkit")
        file_header.append("")

        return file_header

    def __create_function(self, data_bean):
        """
        This creates a function from the given data bean. The format is as follows.

        def <function>(self, *args):
            return self.cmd_obj_constants.METHOD_NOT_SUPPORTED
        """
        function_list = list()

        function_list.append(self.create_indent(1) + "def " + data_bean.interface_method + "(self, output, args, "
                                                                                           "**kwargs):")
        function_list.append(self.create_indent(2) + "return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None")
        function_list.append("")

        return function_list

    def __create_base_function(self, function_name):
        """
        This creates a function from the given data bean. The format is as follows.

        def <function>(self, *args):
            return self.cmd_obj_constants.METHOD_NOT_SUPPORTED
        """
        function_list = list()

        function_list.append(self.create_indent(1) + "def " + function_name + "(self, *func_args, **kwargs):")
        function_list.append(self.create_indent(2) + "return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None")
        function_list.append("")

        return function_list

    def __create_base_api_footer(self):
        """
        This function creates the footer for a base API.
        """
        base_api_footer = list()

        base_api_footer.append(self.create_indent(1) + "def base_function(self, *args, **kwargs):")
        base_api_footer.append(self.create_indent(2) + "return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None")

        base_api_footer.append("")
        base_api_footer.append(self.create_indent(1) + "def __getattr__(self, item):")
        base_api_footer.append(self.create_indent(2) + "# Return the base_function if the called "
                                                       "function does not exist.")
        base_api_footer.append(self.create_indent(2) + "return self.base_function")
        base_api_footer.append("")

        return base_api_footer
