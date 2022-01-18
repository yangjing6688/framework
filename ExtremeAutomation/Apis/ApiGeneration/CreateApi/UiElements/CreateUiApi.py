from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateCliApi import CreateApi


class CreateUiApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single UI API for a given data bean list.
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
            if data_bean.interface_method != "":
                if data_bean.interface_method not in functions:
                    api_list += self.__create_function(data_bean, feature)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        There are no base APIs for UI APIs, so this function is not needed.
        """
        pass

    def __update_file_imports(self, existing_list, data_bean, feature):
        new_list = None
        import_list = []

        if data_bean.previous_version is not None:
            import_str_1 = "from ExtremeAutomation.Apis." + self.device_type_import() + ".GeneratedApis."
            import_str_2 = ".".join([self.agent, data_bean.application, feature, data_bean.previous_version[-1],
                                     feature])
            import_str_3 = " import " + feature.capitalize() + " as " + feature.capitalize() + "Base"
            import_list.append(self.fix_import_line_length(import_str_1 + import_str_2 + import_str_3))
        else:
            import_list.append(self.fix_import_line_length("from ExtremeAutomation.Library.Device.Common.Apis."
                                                           "UiBaseApi import UiBaseApi as " + feature.capitalize() +
                                                           "Base"))
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
        <feature>Base import <feature>Base
        # All imports above this line will be removed after generation.
        # User imports must be added below.


        class <feature>CustomShowTools(<feature>Base):
        """
        file_header = list()

        if data_bean.previous_version is not None:
            import_str_1 = "from ExtremeAutomation.Apis." + self.device_type_import() + ".GeneratedApis."
            import_str_2 = ".".join([self.agent, data_bean.application, feature, data_bean.previous_version[-1],
                                     feature])
            import_str_3 = " import " + feature.capitalize() + " as " + feature.capitalize() + "Base"
            file_header.append(self.fix_import_line_length(import_str_1 + import_str_2 + import_str_3))
        else:
            file_header.append(self.fix_import_line_length("from ExtremeAutomation.Library.Device.Common.Apis."
                                                           "UiBaseApi import UiBaseApi as " + feature.capitalize() +
                                                           "Base"))
        file_header.append("# All imports above this line will be removed after generation.")
        file_header.append("# User imports must be added below.")
        file_header.append("")
        file_header.append("")
        file_header.append("class " + feature.capitalize() + "(" + feature.capitalize() + "Base):")

        return file_header

    def __create_function(self, data_bean, feature):
        """
        This creates a function from the given data bean. The format is as follows.

        def <function>(self, arg_dict, **kwargs):
            # This try/except is here to protect any inheritance that might be used.
            # If a super class is specified the super class's function will be called.
            # If no super class is specified the ui_cmd_obj is returned.
            # This can all be removed if a user implements the function.
            try:
                return super(<feature>, self).<function>(arg_dict, **kwargs)
            except AttributeError:
                return ui_cmd_obj
        """
        function_list = list()

        function_list.append(self.create_indent(1) + "def " + data_bean.interface_method +
                             "(self, ui_cmd_obj, arg_dict):")
        function_list.append(self.create_indent(2) + "# This try/except is here to protect any inheritance that might "
                                                     "be used.")
        function_list.append(self.create_indent(2) + "# If a super class is specified the super class's function will "
                                                     "be called.")
        function_list.append(self.create_indent(2) + "# If no super class is specified the ui_cmd_obj is returned.")
        function_list.append(self.create_indent(2) + "# This can all be removed if a user implements the function.")
        function_list.append(self.create_indent(2) + "try:")
        function_list.append(self.create_indent(3) + "return super(" + feature.capitalize() + ", self)." +
                             data_bean.interface_method + "(ui_cmd_obj, arg_dict)")
        function_list.append(self.create_indent(2) + "except AttributeError:")
        function_list.append(self.create_indent(3) + "return self.base_function()")
        function_list.append("")

        return function_list
