from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateApi import CreateApi
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants


class CreateRestApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single API based on a list of data beans.
        """
        api_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        api_list += self.__create_file_header(data_bean_list[0], feature)

        for data_bean in data_bean_list:
            if data_bean.agent == GenerationConstants.AGENT_TYPE_REST or \
                    data_bean.agent == GenerationConstants.AGENT_TYPE_XMC_REST:
                api_list += self.__create_function(data_bean)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        This function creates a single base API based on a given feature.
        """
        base_api_list = list()

        if len(function_list) == 0:
            raise Exception("Function list is empty.")

        base_api_list += self.__create_base_api_header(feature)

        for _function in function_list:
            base_api_list += self.__create_base_function(_function)

        return base_api_list

    def create_data_file(self, data_bean_list, existing_data_file):
        """
        This function creates a data file for a given data bean list.
        """
        data_file_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        if existing_data_file is not None:
            data_file_list, functions = self.get_functions_from_existing_file(existing_data_file)
            if data_file_list[-1] != "":
                data_file_list.append("")
        else:
            data_file_list += self.__create_data_file_header(feature)
            functions = []

        for data_bean in data_bean_list:
            if data_bean.agent == GenerationConstants.AGENT_TYPE_REST:
                if data_bean.data_function != "":
                    if data_bean.data_function not in functions:
                        data_file_list += self.__create_data_file_function(data_bean)

        return data_file_list

    def __create_file_header(self, data_bean, feature):
        """
        \"""
        All interface supported rest commands.
        \"""
        from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
        from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.<feature>.base.<feature>base import \
            <feature>Base
        from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.REST.<feature>.<os>.<platform>.<version>.\
            <unit>.<feature>Data import <feature>Data


        class Interface(DeviceApi, <feature>Base):
            def __init__(self, device):
                super(<feature>, self).__init__(device)
                self.data_file = <feature>Data()

        """
        file_header = list()

        file_header.append('"""')
        file_header.append("All " + feature + " supported rest commands.")
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
        file_header.append(self.fix_import_line_length("from ExtremeAutomation.Apis." + self.device_type_import() +
                                                       ".GeneratedApis.CommandApis." + self.agent + "." +
                                                       ".".join([i[0] for i in data_bean.get_folders()]) + "." +
                                                       feature + "Data import " + feature.capitalize() + "Data"))
        file_header.append("")
        file_header.append("")
        if data_bean.previous_version is not None:
            file_header.append("class " + feature.capitalize() + "(" + feature.capitalize() + "Base):")
        else:
            file_header.append("class " + feature.capitalize() + "(DeviceApi, " + feature.capitalize() + "Base):")
        file_header.append(self.create_indent(1) + "def __init__(self, device):")
        file_header.append(self.create_indent(2) + "super(" + feature.capitalize() + ", self).__init__(device)")
        file_header.append(self.create_indent(2) + "self.data_file = " + feature.capitalize() + "Data()")
        file_header.append("")

        return file_header

    def __create_base_api_header(self, feature):
        r"""
        This function creates the base API header. The format is as follows.

        \"\"\"
        Base class for all <feature> rest commands.
        \"\"\"
        from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi
        from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


        class <feature>Base(object):
            def __init__(self, device):
                self.device = device

        """
        base_api_header = list()

        base_api_header.append('"""')
        base_api_header.append("Base class for all " + feature + " rest commands.")
        base_api_header.append('"""')
        base_api_header.append("from ExtremeAutomation.Library.Device.Common.Apis.RestBaseApi import RestBaseApi")
        base_api_header.append("from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject "
                               "import RestCommandObject")
        base_api_header.append("")
        base_api_header.append("")
        base_api_header.append("class " + feature.capitalize() + "Base(RestBaseApi):")
        base_api_header.append(self.create_indent(1) + "def __init__(self, device):")
        base_api_header.append(self.create_indent(2) + "super(" + feature.capitalize() + "Base, self).__init__()")
        base_api_header.append(self.create_indent(2) + "self.device = device")
        base_api_header.append("")

        return base_api_header

    @staticmethod
    def __create_data_file_header(feature):
        """
        This function creates the header for a data file. The format is as follows.

        class <feature>Data(object):
        """
        data_file_header = list()

        data_file_header.append("class " + feature.capitalize() + "Data(object):")

        return data_file_header

    def __create_function(self, data_bean):
        """
        This method creates the function body text for a given data_bean. Function format is as follows.

            def show_bgp_global(self, data_dict, **kwargs):
                rest_request = RestCommandObject()
                rest_request.uri = "/public/v1/state/Vlans"
                rest_request.data = None
                rest_request.request_type = "get"

                return self.device.send_command_object(rest_request, **kwargs)
        """
        _function = list()

        _function.append(self.create_indent(1) + "def " + data_bean.interface_method + "(self, arg_dict, **kwargs):")
        _function += self.__create_main_function(data_bean)

        return _function

    def __create_base_function(self, function_name):
        """
        This method creates the function body text for a base api function. The format is as follows.

            def show_bgp_global(self, data_dict):
                rest_request = RestCommandObject()
                rest_request.not_supported = True

                return rest_request

        """
        base_function = list()

        base_function.append(self.create_indent(1) + "def " + function_name + "(self, *args, **kwargs):")
        base_function.append(self.create_indent(2) + "rest_request = RestCommandObject()")
        base_function.append(self.create_indent(2) + "rest_request.not_supported = True")
        base_function.append("")
        base_function.append(self.create_indent(2) + "return rest_request")
        base_function.append("")

        return base_function

    def __create_data_file_function(self, data_bean):
        """
        This function creates a data file function. The format is as follows.

            @staticmethod
            def <data_function>(arg_dict):
                pass

        """
        data_file_function_list = list()

        data_file_function_list.append(self.create_indent(1) + "@staticmethod")
        data_file_function_list.append(self.create_indent(1) + "def " + data_bean.data_function + "(arg_dict):")
        data_file_function_list.append(self.create_indent(2) + "pass")
        data_file_function_list.append("")

        return data_file_function_list

    def __create_main_function(self, data_bean):
        """
        This function creates the function body. The function format is as follows.

            rest_request = RestCommandObject()
            rest_request.uri = "/public/v1/state/Vlans"
            rest_request.data = None
            rest_request.request_type = "get"

            return self.device.send_command_object(rest_request, **kwargs)
        """
        _function = list()

        uri_indent_str = "{0}uri = ".format(self.create_indent(2))
        uri_str = self.format_string_with_args(data_bean.uri, "arg_dict", line_indent_len=len(uri_indent_str))
        _function.append("{0}{1}".format(uri_indent_str, uri_str))
        _function.append("{0}request_type = \"{1}\"".format(self.create_indent(2), data_bean.request_type))

        cmd_obj_args = ["uri", "request_type"]

        if data_bean.data_function:
            _function.append("{0}data = self.data_file.{1}".format(self.create_indent(2), data_bean.data_function))
            cmd_obj_args.append("data")
            cmd_obj_args.append("arg_dict")

        # If there are headers present, add them in following format.
        #
        # If len(headers) == 1 add: rest_request.headers = {"key": "val"}
        #
        # If len(headers) > 1 add rest_request.headers = {"key1": "val1",
        #                                                 "key2": "val2",
        #                                                 "keyN": "valN"}
        if data_bean.headers:
            header_str = "{0}header = ".format(self.create_indent(2))
            header_split = data_bean.headers.split(",")
            cmd_obj_args.append("header")

            for index, header in enumerate(header_split):
                k, v = [i.strip() for i in header.split("=")]
                # If there is only one entry in the headers dict add rest_request = {"key": "val"}
                if len(header_split) == 1:
                    header_str = "{0}{{\"{1}\": \"{2}\"}}".format(header_str, k, v)
                # If there is more than one entry and this is the first add rest_request = {"key": "val",
                elif index == 0:
                    header_str = "{0}{{\"{1}\": \"{2}\",".format(header_str, k, v)
                # If there is more than one entry and this is the last entry add  "key": "val"}
                elif index == len(header_split) - 1:
                    header_str = "{0}                        \"{1}\": \"{2}\" }}".format(header_str, k, v)
                # If there is more than one entry and this is neither the first or last add "key": "val"}
                else:
                    header_str = "{0}                        \"{1}\": \"{2}\",".format(header_str, k, v)
            _function.append(header_str)

        _function.append("")

        if len(data_bean.ignore_errors) != 0:
            _function.append(self.create_indent(2) + "for ignore_string in [" +
                             ", ".join(['"' + i + '"' for i in data_bean.ignore_errors]) + "]:")
            _function.append(self.create_indent(3) + "self.device.error_checker.add_error_to_ignore_list"
                             "(ignore_string)")
        if len(data_bean.add_errors) != 0:
            _function.append(self.create_indent(2) + "for add_error in [" +
                             ", ".join(['"' + i + '"' for i in data_bean.add_errors]) + "]:")
            _function.append(self.create_indent(3) + "self.device.error_checker.add_error_to_temp_list"
                             "(add_error)")

        if len(data_bean.ignore_errors) != 0 or len(data_bean.add_errors) != 0:
            _function.append("")

        _function.append("{0}return self.create_cmd_obj({1})".format(self.create_indent(2), ", ".join(cmd_obj_args)))
        _function.append("")

        return _function

    def create_constant(self, constant, tag=None):
        """
        This function sets the tag type for a REST API, then it calls its parent class's create_constant function.
        """
        tag = "COMMAND_REST" if tag is None else tag
        return super(CreateRestApi, self).create_constant(constant, tag)
