import os
import re
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils

r"""
Example:
def show_accesscontrol_nacversion(self, **kwargs):
    \"\"\"
    baseVersion args:
    ip
    v1 args:

    \"\"\"
    return self.execute_verify_keywords()
"""


class CreateNorthboundKeywords(object):
    def __init__(self):
        self.keyword_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Keywords",
                                         "EndsystemKeywords", "NorthBound")

    def create_keywords(self, data_beans):
        """
        This function creates a single keyword file from a list of data beans.
        """
        for feature in data_beans:
            with open(os.path.join(self.keyword_path,
                                   "Endsystem" + feature.capitalize() + "Keywords.py"), "w") as kw_file:
                kw_file.write("\n".join(self.__create_keyword_header(feature)))
                for data_bean in data_beans[feature]["EMC"]["base"]["baseversion"]["baseunit"]:
                    kw_file.write("\n".join(self.__create_keyword(data_bean)))

    def __create_keyword_header(self, feature):
        r"""
        Example:
        from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
        from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.<feature>Constants \
            import <feature>Constants as ParseConstants
        from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.<feature>Constants \
            import <feature>Constants as CommandConstants


        class Endsystem<feature>Keywords(EndsystemKeywordBaseClass):
            def __init__(self):
                super(Endsystem<feature>Keywords, self).__init__()
                self.cmd_const = CommandConstants()
                self.parse_const = ParseConstants()
        """
        header_list = list()

        header_list.append('"""')
        header_list.append("Keyword class for all " + feature + " northbound commands.")
        header_list.append('"""')
        header_list.append("from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import "
                           "EndsystemKeywordBaseClass")
        header_list.append("from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants."
                           "{0}Constants import \\\n".format(feature.capitalize()) + self.create_indent(1) +
                           "{0}Constants as ParseConstants".format(feature.capitalize()))
        header_list.append("from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants."
                           "{0}Constants import \\\n".format(feature.capitalize()) + self.create_indent(1) +
                           "{0}Constants as CommandConstants".format(feature.capitalize()))
        header_list.append("")
        header_list.append("")
        header_list.append("class Endsystem{0}Keywords(EndsystemKeywordBaseClass):".format(feature.capitalize()))
        header_list.append(self.create_indent(1) + "def __init__(self):")
        header_list.append(self.create_indent(2) +
                           "super(Endsystem{0}Keywords, self).__init__()".format(feature.capitalize()))
        header_list.append(self.create_indent(2) + "self.cmd_const = CommandConstants()")
        header_list.append(self.create_indent(2) + "self.parse_const = ParseConstants()")
        header_list.append(self.create_indent(2) + "self.api_const = \"" + feature + "\"")
        header_list.append("")

        return header_list

    def __create_keyword(self, data_bean):
        """
        Example:
        def verify_device_assettag(self, device_name, ip, assettag, **kwargs):

            Keyword Arguments:
            [device_name] - The device the keyword will be run against.
            [ip]          - The IP of the device you want to verify.
            [assettag]    - The assettag you are verifying.
            Verifies that the specified device has the expected assettag.

            Dictionary Arguments:
            [ip] - The IP of the device you want to verify.
            [assettag] - The assettag you are verifying.

            args = {"ip": ip,
                    "assettag": assettag}

            return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DEVICE_ASSETTAG,
                                               self.parse_const.VERIFY_DEVICE_ASSETTAG, True,
                                               "Assettag returned matched provided value of: '{assettag}'.",
                                               "Assettag returned did not match provided value of: '{assettag}'.",
                                               **kwargs)
        """
        function_list = list()

        function_list.append("")
        function_list.append(self.create_indent(1) + "def verify_" + data_bean.interface_method +
                             "(self, device_name, **kwargs):")
        function_list.append(self.create_indent(2) + "\"\"\"Verifies the output from " + data_bean.interface_method +
                             ".\"\"\"")
        function_list.append(self.create_indent(2) + "return self.execute_verify_keyword(device_name, kwargs,\n" +
                             self.create_indent(10) + "   self.cmd_const." + data_bean.interface_method.upper() +
                             ",\n" + self.create_indent(10) + "   self.parse_const." +
                             data_bean.interface_method.upper() + ",\n" + self.create_indent(10) +
                             "   True, \"PASSED\", \"FAILED\", **kwargs)")
        function_list.append("")

        return function_list

    # +----------------+
    # | Helper Methods |
    # +----------------+
    @staticmethod
    def parse_nbi_query(query):
        """
        This function returns all variables within an NBI query.
        """
        return re.findall(r'\(.*?:"{(.*?)}"\)', query)

    @staticmethod
    def create_indent(number):
        """
        This function creates a string of whitespace that is 4 * <number> characters long.
        """
        return (" " * 4) * number
