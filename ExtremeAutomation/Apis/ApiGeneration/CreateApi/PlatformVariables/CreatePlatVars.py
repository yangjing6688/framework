from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateApi import CreateApi


class CreatePlatVars(CreateApi):
    def create_api(self, data_bean_list, *args, **kwargs):
        """
        This function creates a single API file based on the provided data bean list.
        """
        plat_var_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            os_or_app = data_bean_list[0].operating_system
            if os_or_app is None:
                os_or_app = data_bean_list[0].application

        plat_var_list += self.__create_file_header(os_or_app)

        plat_var_list += self.__create_variables(data_bean_list)

        return plat_var_list

    def create_base_api(self, feature, data_bean_list):
        """
        This function creates a base API for a given feature.
        """
        base_plat_var_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            os_or_app = data_bean_list[0].operating_system
            if os_or_app is None:
                os_or_app = data_bean_list[0].application

        base_plat_var_list += self.__create_base_file_header(os_or_app)

        base_plat_var_list += self.__create_base_variables(data_bean_list)

        return base_plat_var_list

    def __create_file_header(self, os_or_app):
        """
        This function creates the header for a platform variable class. The format is as follows.

        from ExtremeAutomation.Library.Utils.DotDict import DotDict
        from ExtremeAutomation.Apis.<elem_type>.GeneratedApis.PlatformVariables.<os_or_app>.baseplatvars.
        <os_or_app>PlatformVariables import <os_or_app>PlatformVariables


        def create_instance():
            return PlatformVariables()


        class PlatformVariables(<os_or_app>PlatformVariables):
            def __init__(self):
                super(PlatformVariables, <os_or_app>PlatformVariables).__init__()

        """
        header = list()

        elem_folders = {"NETWORKELEMENT": "NetworkElement",
                        "ENDSYSTEMELEMENT": "EndSystemElement",
                        "UIELEMENT": "UiElement"
                        }

        header.append("from ExtremeAutomation.Library.Utils.DotDict import DotDict")
        header.append(self.fix_import_line_length("from ExtremeAutomation.Apis." +
                                                  elem_folders[self.device_type_import().upper()] +
                                                  ".GeneratedApis.PlatformVariables." + os_or_app.upper() +
                                                  ".baseplatvars." + os_or_app.capitalize() +
                                                  "PlatformVariables import " + os_or_app.capitalize() +
                                                  "PlatformVariables"))
        header.append("")
        header.append("")
        header.append("def create_instance():")
        header.append(self.create_indent(1) + "return PlatformVariables()")
        header.append("")
        header.append("")
        header.append("class PlatformVariables(" + os_or_app.capitalize() + "PlatformVariables):")
        header.append(self.create_indent(1) + "def __init__(self):")
        header.append(self.create_indent(2) + "super(PlatformVariables, self).__init__()")
        header.append("")

        return header

    def __create_base_file_header(self, os_or_app):
        """
        This function creates the header for a platform variable class. The format is as follows.

        from ExtremeAutomation.Library.Utils.DotDict import DotDict
        from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.BasePlatformVariables
        import BasePlatformVariables


        def create_instance():
            return PlatformVariables()


        class <os_or_app>PlatformVariables(BasePlatformVariables):
            def __init__(self):
                super(<os_or_app>PlatformVariables, self).__init__()

        """
        base_header = list()

        base_header.append("from ExtremeAutomation.Library.Utils.DotDict import DotDict")
        base_header.append("from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library."
                           "BasePlatformVariables \\")
        base_header.append(self.create_indent(1) + "import BasePlatformVariables")
        base_header.append("")
        base_header.append("")
        base_header.append("def create_instance():")
        base_header.append(self.create_indent(1) + "return " + os_or_app.capitalize() + "PlatformVariables()")
        base_header.append("")
        base_header.append("")
        base_header.append("class " + os_or_app.capitalize() + "PlatformVariables(BasePlatformVariables):")
        base_header.append(self.create_indent(1) + "def __init__(self):")
        base_header.append(self.create_indent(2) + "super(" + os_or_app.capitalize() +
                           "PlatformVariables, self).__init__()")
        base_header.append("")

        return base_header

    def __create_variables(self, data_bean_list):
        """
        This function creates each platform variable. The format is as follows.

        # <feature_1> Platform Variables
        self.vars["<feature_1>"] = DotDict()
        self.vars["<feature_1>"]["<var_name>"] = "<var_value">

        # <feature_N> Platform Variables
        self.vars["<feature_N>"] = DotDict()
        self.vars["<feature_N>"]["<var_name>"] = "<var_value">

        """
        variable_list = list()
        current_feature = data_bean_list[0].feature

        variable_list.append(self.create_indent(2) + "if \"" + current_feature + "\" not in self.vars:")
        variable_list.append(self.create_indent(3) + "self.vars[\"" + current_feature + "\"] = DotDict()")

        for data_bean in data_bean_list:
            if data_bean.feature != current_feature:
                current_feature = data_bean.feature

                variable_list.append("")
                variable_list.append(self.create_indent(2) + "# " + current_feature + " Platform Variables")
                variable_list.append(self.create_indent(2) + "if \"" + current_feature + "\" not in self.vars:")
                variable_list.append(self.create_indent(3) + "self.vars[\"" + current_feature + "\"] = DotDict()")

            if len(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                   data_bean.variable_name + "\"] = \"" + data_bean.variable_value + "\"") > 120:
                variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                                     data_bean.variable_name + "\"] = \\\n" + self.create_indent(3) + "\"" +
                                     data_bean.variable_value + "\"")
            else:
                variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                                     data_bean.variable_name + "\"] = \"" + data_bean.variable_value + "\"")
        variable_list.append("")

        return variable_list

    def __create_base_variables(self, data_bean_list):
        """
        This function creates each platform variable. The format is as follows.

        # <feature_1> Platform Variables
        self.vars["<feature_1>"] = DotDict()
        self.vars["<feature_1>"]["<var_name>"] = "<var_value">

        # <feature_N> Platform Variables
        self.vars["<feature_N>"] = DotDict()
        self.vars["<feature_N>"]["<var_name>"] = "<var_value">

        """
        base_variable_list = list()
        current_feature = data_bean_list[0].feature

        base_variable_list.append(self.create_indent(2) + "# " + current_feature + " Platform Variables")
        base_variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"] = DotDict()")

        for data_bean in data_bean_list:
            if data_bean.feature != current_feature:
                current_feature = data_bean.feature

                base_variable_list.append("")
                base_variable_list.append(self.create_indent(2) + "# " + current_feature + " Platform Variables")
                base_variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"] = DotDict()")

            if len(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                   data_bean.variable_name + "\"] = \"" + data_bean.variable_value + "\"") > 120:
                base_variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                                          data_bean.variable_name + "\"] = \\\n" + self.create_indent(3) + "\"" +
                                          data_bean.variable_value + "\"")
            else:
                base_variable_list.append(self.create_indent(2) + "self.vars[\"" + current_feature + "\"][\"" +
                                          data_bean.variable_name + "\"] = \"" + data_bean.variable_value + "\"")
        base_variable_list.append("")

        return base_variable_list
