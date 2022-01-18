import re
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateApi import CreateApi
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants


class CreateSnmpApi(CreateApi):
    def create_api(self, data_bean_list, **kwargs):
        """
        This function creates a single API based on a given data bean list.
        """
        api_list = list()

        if len(data_bean_list) == 0:
            raise Exception("Data bean list is empty.")
        else:
            feature = data_bean_list[0].feature

        api_list += self.__create_file_header(data_bean_list[0], feature)

        for data_bean in data_bean_list:
            if data_bean.agent == GenerationConstants.AGENT_TYPE_SNMP:
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

    def __create_file_header(self, data_bean, feature):
        r"""
        This function creates the file header for an SNMP command API. The format is as follows.

        \"\"\"
        All system supported snmp commands.
        \"\"\"
        from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
        from ExtremeAutomation.Library.Device.Common.CommandObjects.SnmpCommandObject import SnmpCommandObject
        from ExtremeAutomation.Apis.<device_type>.GeneratedApis.CommandApis.SNMP.<feature>.base.
            <feature> import <feature>Base


        class <feature>(DeviceApi, <feature>Base):
            def __init__(self, device):
                super(<feature>, self).__init__(device)
                self.device = device

        """
        file_header = list()

        file_header.append('"""')
        file_header.append("All " + feature + " supported " + self.agent.upper() + " commands.")
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
            file_header.append(self.fix_import_line_length("from ExtremeAutomation.Apis.NetworkElement.GeneratedApis."
                                                           "CommandApis." + self.agent.upper() + "." + feature +
                                                           ".base." + feature + "base import " + feature.capitalize() +
                                                           "Base"))
        file_header.append("")
        file_header.append("")
        if data_bean.previous_version is not None:
            file_header.append("class " + feature.capitalize() + "(" + feature.capitalize() + "Base):")
        else:
            file_header.append("class " + feature.capitalize() + "(DeviceApi, " + feature.capitalize() + "Base):")
        file_header.append(self.create_indent(1) + "def __init__(self, device):")
        file_header.append(self.create_indent(2) + "super(" + feature.capitalize() + ", self).__init__(device)")
        file_header.append(self.create_indent(2) + "self.device = device")
        file_header.append("")

        return file_header

    def __create_base_api_header(self, feature):
        r"""
        This function creates the header for an SNMP base API. The format is as follows.

        \"\"\"
        Base class for all system snmp commands.
        \"\"\"
        from ExtremeAutomation.Apis.Apis.SnmpBaseApi import SnmpBaseApi


        class <feature>Base(SnmpBaseApi):
            def __init__(self, device):
                super(<feature>Base, self).__init__()
                self.device = device

        """
        base_api_header = list()

        base_api_header.append('"""')
        base_api_header.append("Base class for all " + feature + " SNMP commands.")
        base_api_header.append('"""')
        base_api_header.append("from ExtremeAutomation.Library.Device.Common.Apis.SnmpBaseApi import SnmpBaseApi")
        base_api_header.append("")
        base_api_header.append("")
        base_api_header.append("class " + feature.capitalize() + "Base(SnmpBaseApi):")
        base_api_header.append(self.create_indent(1) + "def __init__(self, device):")
        base_api_header.append(self.create_indent(2) + "super(" + feature.capitalize() + "Base, self).__init__()")
        base_api_header.append(self.create_indent(2) + "self.device = device")
        base_api_header.append("")

        return base_api_header

    def __create_function(self, data_bean):
        """
        This function creates an SNMP command API function. The format is as follows.

        def get_host_location(self, arg_dict):
            snmp_request = SnmpCommandObject()
            snmp_request.command_type = <cmd_type>
            snmp_request.oid = <oid>
            snmp_request.data_type = <data_type>
            snmp_request.value = arg_dict[<value>]

            return self.device.send_command_object(snmp_request)

        """
        _function = list()

        _function.append(self.create_indent(1) + "def " + data_bean.interface_method + "(self, arg_dict, **kwargs):")

        oid_indent_str = "{0}oid = ".format(self.create_indent(2))
        oid_string = self.format_oid_string(data_bean.oid, len(oid_indent_str))
        cmd_obj_args = ["command_type", "oid"]
        _function.append("{0}command_type = \"{1}\"".format(self.create_indent(2), data_bean.command_type))
        _function.append("{0}{1}".format(oid_indent_str, oid_string))

        if data_bean.command_type == "snmpset":
            value_indent = "{0}value = ".format(self.create_indent(2))
            value_string = self.format_string_with_args(data_bean.value, "arg_dict", line_indent_len=len(value_indent))
            _function.append("{0}data_type = \"{1}\"".format(self.create_indent(2), data_bean.data_type))
            _function.append("{0}value = {1}".format(self.create_indent(2), value_string))
            cmd_obj_args.append("data_type")
            cmd_obj_args.append("value")

        _function.append("")
        _function.append("{0}return self.create_cmd_obj({1})".format(self.create_indent(2), ", ".join(cmd_obj_args)))
        _function.append("")

        return _function

    def __create_base_function(self, _function):
        """
        This function creates an SNMP base API function. The format is as follows.

        def <function_name>(self, arg_dict):
            snmp_request = SnmpCommandObject()
            snmp_request.not_supported = True

            return snmp_request
        """
        base_function = list()

        base_function.append(self.create_indent(1) + "def " + _function + "(self, *args, **kwargs):")
        base_function.append(self.create_indent(2) + "return self.base_function()")
        base_function.append("")

        return base_function

    def create_constant(self, constant, tag=None):
        """
        This function sets the tag type for an SNMP API, then it calls its parent class's create_constant function.
        """
        tag = "COMMAND_SNMP" if tag is None else tag
        return super(CreateSnmpApi, self).create_constant(constant, tag)

    def format_oid_string(self, oid, indent):
        """Returns the OID formatted into a valid string for SNMP."""
        if "||" not in oid:
            oid_str = "\"{0}\"".format(oid)
            return self.format_oid_args(oid_str)

        oid_split = oid.split("||")

        index = 0

        while index < len(oid_split):
            if index == 0:
                oid_split[index] = "\"{0}||\" \\".format(oid_split[index])
            elif index == len(oid_split) - 1:
                oid_split[index] = "{0}\"{1}\"".format(" " * indent, oid_split[index])
            else:
                oid_split[index] = "{0}\"{1}||\" \\".format(" " * indent, oid_split[index])
            index += 1

        formatted_oid_str = self.format_oid_args("\n".join(oid_split))
        return formatted_oid_str

    def format_oid_args(self, oid_str):
        """Returns the OID and args combined into a valid SNMP string."""
        oid_args = set(re.findall("{.*?}", oid_str))

        for index, arg in enumerate(oid_args):
            oid_str = oid_str.replace(arg, "{" + str(index) + "}")

        # Create a Dictionary of arg/value pairs, argument function calls will be filled out here.
        arg_values = []
        for val in oid_args:
            if "<" in val:
                func, args = self._get_arg_functions(val)
                if len(args) == 1:
                    arg_values.append("self.{0}(arg_dict['{1}'])".format(func, args[0].strip("{}")))
                else:
                    arg_value = "self.{0}(".format(func)
                    for arg in args:
                        arg_value += "arg_dict['{0}'], ".format(arg.strip("{}"))
                    arg_values.append(arg_value[:-2] + ")")
            else:
                arg_values.append("arg_dict['{0}']".format(val.strip("{}")))

        if oid_args:
            if len(oid_args) > 1:
                indent = " " * (len(oid_str) - oid_str.rfind("\n") + len(".format(") - 1)
                oid_str += ".format("
                for index, arg in enumerate(arg_values):
                    if index == 0:
                        oid_str += arg + ",\n"
                    elif index == len(oid_args) - 1:
                        oid_str += indent + arg + ")"
                    else:
                        oid_str += indent + arg + ",\n"
            else:
                oid_str += ".format({0})".format(", ".join(arg_values))

        return oid_str
