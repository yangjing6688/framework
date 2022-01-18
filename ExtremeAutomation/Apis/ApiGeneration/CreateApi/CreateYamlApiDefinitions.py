import os
import re
import shutil
from distutils.dir_util import copy_tree
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Logger.Logger import Logger

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


class CreateYamlApiDefinitions(object):
    def __init__(self):
        self.logger = Logger()
        self.api_path = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Apis", "EndsystemElement",
                                     "YamlApiDefintion", "CommandApiDefinition", "CLI")
        self.gen_temp_dir = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Apis", "EndsystemElement",
                                         "YamlApiDefintion", "GenerationTemp")
        self.api_temp_dir = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Apis", "EndsystemElement",
                                         "YamlApiDefintion", "ApiTemp")
        self.api_files = None
        self.method_dict = {}

    def create_apis(self, data_beans, keyword_info):
        """
        This function creates a single keyword file from a list of data beans.
        """
        self.__create_directory(self.gen_temp_dir)
        self.__create_directory(self.api_temp_dir)

        try:
            for feature in data_beans:
                # Make sure keyword output path exists
                os.makedirs(self.api_path, exist_ok=True)
                filename = feature.lower() + ".yaml"
                method_dict = {}

                for version in data_beans[feature].keys():
                    for bean in data_beans[feature][version]:
                        method_dict.setdefault(bean.interface_method, {}).setdefault(version, []).append(bean)

                # Generate and write all keyword lines to temp file.
                output_file = os.path.join(self.gen_temp_dir, filename)
                with open(output_file, "w") as kw_file:
                    kw_file.write("\n".join(self.__create_api_definition(feature, method_dict, keyword_info)))

            # Move the generated Keywords from the temp directory in to the actual output directory.
            if os.path.exists(self.gen_temp_dir) and os.path.exists(self.api_path):
                copy_tree(self.gen_temp_dir, self.api_path)
        except Exception as e:
            self.logger.log_error(e)

        self.__cleanup_temp_dirs()

    def __create_api_definition(self, feature, method_dict, keyword_info):
        """
        Example:

        feature:
          interface_method:
            description: Some information describing the function of the keyword.
            apis:
              - [os,platform,version,unit,command,prompt,prompt_args,confirmation_prompt,confirmation_args,
                 ignore_errors,add_errors]
            arguments:
              order: arg2,arg3,arg1,arg4,arg5

        """
        api_lines = list()
        api_lines.extend(self.__create_file_header())
        api_lines.append(feature + ":")

        ordered_method_names = list()
        show_methods = list()

        for method in method_dict:
            if method.split("_")[0] != "show":
                ordered_method_names.append(method)
            else:
                show_methods.append(method)
        ordered_method_names.extend(show_methods)
        for method in ordered_method_names:
            api_lines.append(self.__create_indent(1) + method + ":")
            if feature in keyword_info["descriptions"] and method.split("_")[0] != "show":
                if method in keyword_info["descriptions"][feature]:
                    description = keyword_info["descriptions"][feature][method]
                    api_lines.append(self.__create_indent(2) + 'description: "{0}"'.format(description))

            if feature in keyword_info["arg_order"] and method.split("_")[0] != "show":
                if method in keyword_info["arg_order"][feature]:
                    api_lines.append(self.__create_indent(2) + "arguments:")
                    if keyword_info["arg_order"][feature][method] is not None:
                        order = ",".join(keyword_info["arg_order"][feature][method].split(">"))
                    else:
                        order = ""
                    api_lines.append(self.__create_indent(3) + "order: " + order)

            api_lines.append(self.__create_indent(2) + "apis:")
            for version in method_dict[method]:
                for bean in method_dict[method][version]:
                    # Application,Application Version
                    app_ver = bean.app_version.replace("v", "").replace("dot", ".")
                    api_line = (self.__create_indent(3) +
                                "- [{0},'{1}']".format(bean.application.lower(), app_ver))
                    api_lines.append(api_line)

        return api_lines

    # +----------------+
    # | Helper Methods |
    # +----------------+
    @staticmethod
    def __create_file_header():
        """Creates a documentation header for the API file."""
        api_lines = list()
        api_lines.append("# Documentation - Set and Show API formats.")
        api_lines.append("# feature_name:")
        api_lines.append("#     api_method_name:")
        api_lines.append("#         apis:")
        api_lines.append("#             - [OS1,Platform,Version,Unit,URI,Headers,IgnoreError,AddError]")
        api_lines.append("#             - [OS2,Platform,Version,Unit,URI,Headers,IgnoreError,AddError]")
        api_lines.append("")

        return api_lines

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

        for dir_path, dir_names, file_names in os.walk(self.api_path):
            for file_name in file_names:
                if file_name.lower().endswith("keywords.py") and not file_name.startswith("__"):
                    file_dict = {"path": dir_path,
                                 "file_name": file_name,
                                 "temp_path": self.api_temp_dir + dir_path.replace(self.api_path, ""),
                                 "rel_path": dir_path.replace(self.api_path, "")
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

    @staticmethod
    def __create_directory(path):
        """
        This function creates the given directory and adds an __init__.py file to it.
        """
        try:
            os.makedirs(path)
        except OSError:
            pass

    def __cleanup_temp_dirs(self):
        """
        This function removes any temporary directories that exist.
        """
        if os.path.exists(self.gen_temp_dir):
            shutil.rmtree(self.gen_temp_dir)
        if os.path.exists(self.api_temp_dir):
            shutil.rmtree(self.api_temp_dir)

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
