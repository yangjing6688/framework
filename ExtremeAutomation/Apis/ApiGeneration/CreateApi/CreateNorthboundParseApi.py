import re
import itertools
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateCliApi import CreateApi


class CreateNorthbounParseApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single API file for a given data bean list.
        """
        api_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        if len(api_list) == 0:
            api_list = self.__create_file_header(feature)

        for data_bean in data_bean_list:
            api_list += self.__create_function(data_bean)

        return api_list

    def create_base_api(self, feature, function_list):
        """
        This function creates a base API file for a given feature.
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
        from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
        from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants
        import EndsystemElementConstants


        class DevicesBaseCustomShowTools(BaseShowApi):
            def __init__(self, device):
                super(DevicesBaseCustomShowTools, self).__init__()
                self.device = device
                self.it = self.device.get_inspection_toolkit()

        """
        base_header_list = list()

        base_header_list.append("from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi")
        base_header_list.append("from ExtremeAutomation.Library.Device.EndsystemElement.Constants."
                                "EndsystemElementConstants import EndsystemElementConstants")
        base_header_list.append("")
        base_header_list.append("")
        base_header_list.append("class " + feature.capitalize() + "BaseCustomShowTools(BaseShowApi):")
        base_header_list.append(self.create_indent(1) + "def __init__(self, device):")
        base_header_list.append(self.create_indent(2) + "super(" + feature.capitalize() +
                                "BaseCustomShowTools, self).__init__()")
        base_header_list.append(self.create_indent(2) + "self.device = device")
        base_header_list.append("")

        return base_header_list

    def __create_base_function(self, function_name):
        """
        def <function_name>(self, *args):
            return EndsystemElementConstants.METHOD_NOT_SUPPORTED
        """
        base_function_list = list()

        base_function_list.append(self.create_indent(1) + "def " + function_name + "(self, *args):")
        base_function_list.append(self.create_indent(2) + "return EndsystemElementConstants.METHOD_NOT_SUPPORTED")
        base_function_list.append("")

        return base_function_list

    def __create_file_header(self, feature):
        """
        from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.<feature>.base.\
            <feature>BaseCustomShowTools import <feature>BaseCustomShowTools


        class DevicesCustomShowTools(DevicesBaseCustomShowTools):
        """
        api_header_list = list()

        api_header_list.append("from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults")
        api_header_list.append(self.fix_import_line_length("from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis."
                                                           "ParseApis.NORTHBOUND." + feature + ".base." +
                                                           feature.capitalize() + "BaseCustomShowTools import " +
                                                           feature.capitalize() + "BaseCustomShowTools"))
        api_header_list.append("")
        api_header_list.append("")
        api_header_list.append("class " + feature.capitalize() + "CustomShowTools(" + feature.capitalize() +
                               "BaseCustomShowTools):")

        return api_header_list

    def __create_function(self, data_bean):
        """
        def <data_bean.interface_method>(self, output, args, **kwargs):
            try:
                result = output["data"]["network"]["device"]["assetTag"] == args["assettag"]
                result &= output["data"]["network"]["device"]["mac"] == args["mac"]
                return result
            except KeyError:
                return False
        """
        function_list = list()

        function_list.append(self.create_indent(1) + "def " + data_bean.interface_method +
                             "(self, output, args, **kwargs):")
        function_list.append(self.create_indent(2) + "try:")
        function_list.append(self.create_indent(3) + "result = NorthboundResults()")

        for index, validation in enumerate(self.parse_nbi_query(data_bean.query)):
            function_list.append(self.create_indent(3) + "result.add_result(output['" + "']['".join(validation) +
                                 "'], args['" + validation[-1].lower() + "'])")

        function_list.append(self.create_indent(3) + "return result.return_result()")
        function_list.append(self.create_indent(2) + "except KeyError:")
        function_list.append(self.create_indent(3) + "self.logger.log_info(\"KEY ERROR\")")
        function_list.append(self.create_indent(3) + "return False")
        function_list.append("")

        return function_list

    # +----------------+
    # | Helper Methods |
    # +----------------+
    @staticmethod
    def parse_nbi_query(query):
        """
        This function returns each unique combination of keys for a given nbi query.

        For example {test{query{one two}}

        Would return
        [test][query][one]
        [test][query][two]
        """
        query = "{data" + query + "}"
        for var in re.findall(r"\(.*?\)", query):
            query = query.replace(var, "")
        query_split = [i.replace("}", "").split() for i in query.split("{") if i != ""]
        return list([list(i) for i in itertools.product(*query_split)])
