import re
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateApi import CreateApi


class CreateNorthboundApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single API file from a list of data beans.
        """
        api_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        api_list += self.__create_file_header(feature)

        for data_bean in data_bean_list:
            api_list += self.__create_function(data_bean)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        This function creates a base API for a given feature.
        """
        base_api_list = list()

        if len(function_list) == 0:
            raise Exception("Function list is empty.")

        base_api_list += self.__create_base_api_header(feature)

        for _function in function_list:
            base_api_list += self.__create_base_function(_function)

        return base_api_list

    def __create_base_api_header(self, feature):
        """
        \"""
        Base class for all <feature> northbound commands.
        \"""
        from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
        from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


        class <feature>Base(BaseApi):
            def __init__(self, device):
                self.device = device
        """
        header_list = list()

        header_list.append('"""')
        header_list.append("Base class for all " + feature + " northbound commands.")
        header_list.append('"""')
        header_list.append("from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi")
        header_list.append("from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject "
                           "import RestCommandObject")
        header_list.append("")
        header_list.append("")
        header_list.append("class " + feature.capitalize() + "Base(BaseApi):")
        header_list.append(self.create_indent(1) + "def __init__(self, device):")
        header_list.append(self.create_indent(2) + "self.device = device")
        header_list.append("")

        return header_list

    def __create_base_function(self, function_name):
        """
        def <function_name>(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
        """
        base_function_list = list()

        base_function_list.append(self.create_indent(2) + "def " + function_name + "(self, data_dict):")
        base_function_list.append(self.create_indent(3) + "rest_request = RestCommandObject()")
        base_function_list.append(self.create_indent(3) + "rest_request.not_supported = True")
        base_function_list.append("")
        base_function_list.append(self.create_indent(3) + "return rest_request")
        base_function_list.append("")

        return base_function_list

    def __create_file_header(self, feature):
        """
        \"""
        All device supported northbound commands.
        \"""
        from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
        from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
        from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.devices.base.<feature>base \
            import <feature>Base


        class <feature>(DeviceApi, <feature>Base):
            def __init__(self, device):
                super(<feature>, self).__init__(device)

        """
        file_header_list = list()

        file_header_list.append('"""')
        file_header_list.append("All " + feature + " supported northbound commands.")
        file_header_list.append('"""')
        file_header_list.append("from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi")
        file_header_list.append("from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject "
                                "import RestCommandObject")
        file_header_list.append(self.fix_import_line_length("from ExtremeAutomation.Apis.EndsystemElement."
                                                            "GeneratedApis.CommandApis.NORTHBOUND." +
                                                            feature + ".base." + feature + "base import " +
                                                            feature.capitalize() + "Base"))
        file_header_list.append("")
        file_header_list.append("")
        file_header_list.append("class " + feature.capitalize() + "(DeviceApi, " + feature.capitalize() + "Base):")
        file_header_list.append(self.create_indent(1) + "def __init__(self, device):")
        file_header_list.append(self.create_indent(2) + "super(" + feature.capitalize() + ", self).__init__(device)")
        file_header_list.append("")

        return file_header_list

    def __create_function(self, data_bean):
        """
        def <data_bean.interface_method>(self, arg_dict):
            rest_request = RestCommandObject()
            rest_request.uri = "/nbi/graphql/"
            rest_request.query = "<data_bean.query>"
            rest_request.request_type = "post"

            return self.device.send_command_object(rest_request)
        """
        function_list = list()

        function_list.append(self.create_indent(1) + "def " + data_bean.interface_method + "(self, arg_dict):")
        function_list.append(self.create_indent(2) + "rest_request = RestCommandObject()")
        function_list.append(self.create_indent(2) + 'rest_request.uri = "/nbi/graphql/"')

        for var in re.findall("\".*?\"", data_bean.query):
            data_bean.query = data_bean.query.replace(var, "\"' + arg_dict[\"" + var.strip("\"{}") + "\"] + '\"")

        function_list.append(self.create_indent(2) + "rest_request.data = '" + data_bean.query + "'")
        function_list.append(self.create_indent(2) + 'rest_request.request_type = "post"')
        function_list.append("")
        function_list.append(self.create_indent(2) + "return self.device.send_command_object(rest_request)")
        function_list.append("")

        return function_list
