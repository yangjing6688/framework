import re
import os
import shutil
import traceback
from optparse import OptionParser
from collections import OrderedDict
from distutils.dir_util import copy_tree
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariableConstants \
    import PlatformVariableConstants
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateCliApi import CreateCliApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateParseApi import CreateParseApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateRestApi import CreateRestApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateSnmpApi import CreateSnmpApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.PlatformVariables.CreatePlatVars \
    import CreatePlatVars
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.UiElements.CreateUiApi import CreateUiApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateNorthboundApi import CreateNorthboundApi
from ExtremeAutomation.Apis.ApiGeneration.CreateApi.CreateNorthboundParseApi \
    import CreateNorthbounParseApi
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCommandCsvs import ParseCommandCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCliCommandCsvs import ParseCliCommandCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseRestCommandCsvs import ParseRestCommandCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseCliParseCsvs import ParseCliParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.UiElements.ParseUiElementCsvs \
    import ParseUiElementCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.PlatformVariables.ParseNetElemPlatVarCsvs \
    import ParseNetElemPlatVarCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.PlatformVariables.ParseEndSysPlatVarCsvs \
    import ParseEndSysPlatVarCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.PlatformVariables.ParseUiElemPlatVarCsvs \
    import ParseUiElemPlatVarCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseNorthboundCommandCsv \
    import ParseNorthboundCommandCsvs
from ExtremeAutomation.Apis.ApiGeneration.ParseCsvs.ParseNorthboundParseCsv \
    import ParseNorthboundParseCsvs
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.NetElemPlatformVariableDataBean \
    import NetElemPlatformVariableDataBean
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.EndSysPlatformVariableDataBean \
    import EndSysPlatformVariableDataBean
from ExtremeAutomation.Apis.ApiGeneration.Beans.PlatformVariableBeans.\
    UiElementPlatformVariableDataBean import UiElementPlatformVariableDataBean


class GenerateAllApis(object):
    def __init__(self, dev_type, csv_type, agent_type, app_type=None, input_dir=None, output_dir=None):
        _input_dir = None
        _output_dir = None

        self.logger = Logger()
        self.dev_type = dev_type
        self.csv_type = csv_type.upper()
        self.agent_type = agent_type.upper()
        self.app_type = None if app_type is None else app_type.upper()
        self.clean_output_dir = True
        self.functions_by_feature = {}
        self.plat_var_base_vars = {}
        self.has_data_file = False
        self.has_base_files = True
        self.has_constants_files = False
        self.update_api = False
        self.api_search_str = None
        self.api_files = []
        self.data_files = []
        self.gen_constants = GenerationConstants()
        self.app_type_list = [self.gen_constants.APPLICATION_TYPE_GIM,
                              self.gen_constants.APPLICATION_TYPE_XMC,
                              self.gen_constants.APPLICATION_TYPE_EMC,
                              self.gen_constants.APPLICATION_TYPE_XCA,
                              self.gen_constants.APPLICATION_TYPE_EWC,
                              self.gen_constants.APPLICATION_TYPE_ECIQ,
                              self.gen_constants.APPLICATION_TYPE_DFNDR]

        if input_dir is None or output_dir is None:
            _input_dir, _output_dir = PathUtils.get_csv_input_output_paths(self.dev_type, self.csv_type,
                                                                           self.agent_type)

        self.input_dir = _input_dir if input_dir is None else input_dir
        self.output_dir = _output_dir if output_dir is None else output_dir
        self.full_output_dir = os.path.join(self.output_dir, self.agent_type) if app_type is None \
            else os.path.join(self.output_dir, self.agent_type, app_type)
        self.constants_path = os.path.join(self.output_dir, "Constants") if app_type is None \
            else os.path.join(self.output_dir, "Constants", app_type)
        self.api_temp_dir = os.path.join(self.output_dir, "ApiTemp")
        self.data_temp_dir = os.path.join(self.output_dir, "DataTemp")
        self.generation_temp_dir = os.path.join(self.output_dir, "GenerationTemp") if app_type is None \
            else os.path.join(self.output_dir, "GenerationTemp", app_type)
        self.csv_parser, self.api_gen = self.__get_csv_parser_and_api_generator()

    def generate_all_apis(self):
        """
        This is the main function for generating APIs. It handles creating/removing temp folders. Creating
        new API folders, creating new APIs, creating base APIs, updating existing APIs, and moving
        generated APIs into the correct location.

        If an exception is encountered during generation, the exception is logged and the
        generation is stopped. If all files are generated without issue they are moved to
        their permanent location and all temporary files/folders are removed.
        """
        move_files = False

        # Remove any temp dirs.
        self.cleanup_temp_dirs()

        try:
            # Parse and create the CSV dictionary, needed later to create the actual API files.
            self.csv_parser.parse_all_csvs()

            # If data files are required first remove any existing data file temp directory.
            # Then move any existing files to a temp directory for use later.
            if self.has_data_file:
                if os.path.exists(self.data_temp_dir):
                    shutil.rmtree(self.data_temp_dir)
                self.data_files = self.__copy_files_to_temp("data.py", self.data_temp_dir)

            # If the existing API files need to be updated rather than completed regenerated first remove
            # any existing API file temp directory. Them move the existing API files to the API temp directory.
            if self.update_api:
                if os.path.exists(self.api_temp_dir):
                    shutil.rmtree(self.api_temp_dir)
                self.api_files = self.__copy_files_to_temp(self.api_search_str, self.api_temp_dir)

            # Create the generation temp directory.
            self.__create_directory(self.generation_temp_dir)

            # Use the CSV dictionary to create the needed API files. This function either creates
            # new API files or updates the existing API depending on the status of the update_api flag.
            # It will also create data files if they are needed.
            self.__create_apis_from_dict(self.generation_temp_dir, self.csv_parser.all_parsed_csvs)

            # If base APIs are needed they are generated here.
            if self.has_base_files:
                self.__create_base_apis_from_dict(self.generation_temp_dir)

            # This flag lets the generator know that the API files were generated successfully and can
            # later be moved from the their temp dir to the actual output dir.
            move_files = True
        except Exception as e:
            self.logger.log_info("\nAn error occurred during generation, no changes have been made.")
            self.logger.log_info("If you are unsure what caused this error please send "
                                 "the below information to Robot-Dev@extremenetworks.com")
            self.logger.log_info("\nException Information:")
            self.logger.log_info(e)
            self.logger.log_info(traceback.format_exc())  # This prints the entire exception.
            self.logger.log_info("\n")

        if move_files:
            # If all of the above was successful we check the clean_output_dir flag and remove the existing
            # output directory if needed.
            if self.clean_output_dir:
                if os.path.exists(self.full_output_dir):
                    shutil.rmtree(self.full_output_dir)

            # Create the output and full output folders.
            self.__create_directory(self.output_dir)
            self.__create_directory(self.full_output_dir)

            # Move the generated APIs from the temp directory in to the actual output directory.
            if os.path.exists(self.generation_temp_dir) and os.path.exists(self.full_output_dir):
                copy_tree(self.generation_temp_dir, self.full_output_dir)

            # If constants files are needed, generate them now.
            if self.has_constants_files:
                self.__create_directory(self.constants_path)
                self.__create_constants()

        # Cleanup any remaining temp directories.
        self.cleanup_temp_dirs()

    def cleanup_temp_dirs(self):
        """
        This function removes any temporary directories that exist.
        """
        if os.path.exists(self.generation_temp_dir):
            shutil.rmtree(self.generation_temp_dir)
        if os.path.exists(self.data_temp_dir):
            shutil.rmtree(self.data_temp_dir)
        if os.path.exists(self.api_temp_dir):
            shutil.rmtree(self.api_temp_dir)

    def __copy_files_to_temp(self, file_name_filter, temp_dir):
        file_list = []

        for dir_path, dir_names, file_names in os.walk(self.full_output_dir):
            for file_name in file_names:
                if file_name.lower().endswith(file_name_filter.lower()) and not file_name.startswith("__"):
                    file_dict = {"path": dir_path,
                                 "file_name": file_name,
                                 "temp_path": temp_dir + dir_path.replace(self.full_output_dir, ""),
                                 "rel_path": dir_path.replace(self.full_output_dir, "")
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

    def __create_apis_from_dict(self, path, current_dict):
        """
        This function scans through each level of the nested dictionary produced by the csv parser.
        It creates the needed folder for each of the features, os, platforms, units, and versions.
        It then creates the API file at the end of each /feature/os/platform/version/unit/ folder.
        It also creates a list of the functions present for each feature. These are used later
        to create the base api file for a given feature.
        """
        if not isinstance(current_dict, list):
            for directory in current_dict:
                new_path = os.path.join(path, directory)
                if isinstance(current_dict[directory], dict):
                    if self.agent_type in current_dict[directory]["contains_agents"]:
                        if not os.path.exists(os.path.join(path, directory)):
                            self.__create_directory(new_path)
                    current_dict[directory].pop("contains_agents")
                self.__create_apis_from_dict(new_path, current_dict[directory])
        elif isinstance(current_dict, list):
            # Check for current_agent APIs in the list
            has_agent_apis = False
            for data_bean in current_dict:
                if data_bean.agent == self.agent_type:
                    has_agent_apis = True

            # Generate API files if current agent is found
            if (self.clean_output_dir or
                (not self.clean_output_dir and not os.path.isfile(path + os.sep + current_dict[0].file_name))) and \
                    has_agent_apis:
                self.logger.log_info("Creating API file " + "/".join([i[0] for i in current_dict[0].get_folders()]) +
                                     "/" + current_dict[0].file_name)
                if not os.path.exists(path):
                    self.__create_directory(path)
                if not current_dict[0].is_base:
                    with open(os.path.join(path, current_dict[0].file_name), "w") as api_file:
                        if self.update_api:
                            temp_api_file = self.__get_existing_file(path, self.api_files)
                        else:
                            temp_api_file = None

                        api_file.writelines("\n".join(self.api_gen.create_api(current_dict,
                                                                              existing_api_file=temp_api_file)))

                    if self.has_data_file:
                        for x, api in enumerate(current_dict):
                            if api.agent == self.agent_type:
                                self.logger.log_info("Creating Data file " +
                                                     "/".join([i[0] for i in current_dict[x].get_folders()]) + "/" +
                                                     current_dict[x].data_file_name)
                                with open(os.path.join(path, current_dict[x].data_file_name), "w") as data_file:
                                    temp_data_file = self.__get_existing_file(path, self.data_files)
                                    data_file.writelines("\n".join(self.api_gen.create_data_file(current_dict,
                                                                                                 temp_data_file)))
            if self.csv_type != self.gen_constants.API_TYPE_PLATFORM_VARIABLE:
                self.__get_functions_from_data_bean_list(current_dict)
            else:
                self.__get_base_vars_from_data_bean_list(current_dict)

    def __get_existing_file(self, path, file_list):
        _file = [i for i in file_list if i["rel_path"] == path.replace(self.generation_temp_dir, "")]

        if len(_file) == 1:
            return _file[0]
        return None

    def __create_base_apis_from_dict(self, path):
        """
        This function iterates over the dictionary created by __get_functions_from_data_bean_list. For each of
        the features (keys) in the dictionary it creates a base API file for each function within the list.
        """
        if len(self.functions_by_feature) > 0:
            for feature in self.functions_by_feature:
                temp_path = path + os.sep + feature + os.sep + "base"
                self.__create_directory(temp_path)
                with open(temp_path + os.sep + self.functions_by_feature[feature]["file_name"], "w") as base_api_file:
                    self.logger.log_info("Creating base API file: " + self.functions_by_feature[feature]["file_name"])
                    base_api = self.api_gen.create_base_api(feature, self.functions_by_feature[feature]["methods"])
                    base_api_file.write("\n".join(base_api))
        elif len(self.plat_var_base_vars) > 0:
            for key in self.plat_var_base_vars:
                if isinstance(self.plat_var_base_vars[key][0], (NetElemPlatformVariableDataBean,
                                                                EndSysPlatformVariableDataBean)):
                    temp_path = os.path.join(path, self.plat_var_base_vars[key][0].operating_system, "baseplatvars")
                    top_folder = self.plat_var_base_vars[key][0].operating_system
                else:
                    temp_path = os.path.join(path, self.plat_var_base_vars[key][0].application, "baseplatvars")
                    top_folder = self.plat_var_base_vars[key][0].application

                self.__create_directory(temp_path)
                with open(os.path.join(temp_path, top_folder.capitalize() + "PlatformVariables.py"), "w") \
                        as base_plat_var_file:
                    self.logger.log_info("Creating base plat var file: PlatformVariables.py")
                    base_plat_vars = self.api_gen.create_base_api(top_folder, self.plat_var_base_vars[key])
                    base_plat_var_file.write("\n".join(base_plat_vars))
                self.__remove_unneeded_folders(top_folder)

    def __create_constants(self):
        """
        If the file does not exist create normally.

        if the file does exist get the constants from it.
        then for each function in function_by_feature check if it is present.
        if it is skip it otherwise add it.
        """
        methods = None
        existing_constants = None
        current_tag = self.csv_type + "_" + self.agent_type

        if len(self.functions_by_feature) > 0:
            for feature in self.functions_by_feature:
                file_name = feature.capitalize() + "Constants.py"
                file_path = os.path.join(self.constants_path, file_name)
                if os.path.isfile(os.path.join(self.constants_path, file_name)):
                    existing_constants = self.__get_constants_from_existing_file(file_path)

                    for _function in self.functions_by_feature[feature]["methods"]:
                        if _function not in existing_constants:
                            existing_constants[_function] = [current_tag]
                        elif _function in existing_constants:
                            if current_tag not in existing_constants[_function]:
                                existing_constants[_function].append(current_tag)
                    for _function in existing_constants:
                        if _function not in self.functions_by_feature[feature]["methods"]:
                            if current_tag in existing_constants[_function]:
                                existing_constants[_function].remove(current_tag)
                    existing_constants = dict((k, v) for (k, v) in existing_constants.items() if len(v) != 0)
                elif self.has_constants_files:
                    methods = self.functions_by_feature[feature]["methods"]
                    existing_constants = None
                with open(file_path, "w") as constants_file:
                    self.logger.log_info("Creating constants file: " + file_name)
                    constants_file.write("\n".join(self.api_gen.create_constants(feature, methods, current_tag,
                                                                                 existing_constants)))

    def __get_constants_from_existing_file(self, path):
        constants = OrderedDict()
        start_line = None

        with open(path, "r") as constants_file:
            file_lines = constants_file.readlines()

        for index, line in enumerate(file_lines):
            super_re = r"^super\(.*Constants, self\).__init__\(\)$"
            if len(re.findall(super_re, line.lstrip())) > 0:
                start_line = index + 1
                break

        if start_line is not None:
            constants_list = file_lines[start_line::]

            for index in range(0, len(constants_list), 3):
                constant = constants_list[index].split(":")[1].strip(" \"\n,")
                tags = self.__get_tags(constants_list[index + 1].split(":")[1])
                constants[constant] = tags

        return constants

    @staticmethod
    def __get_tags(tag_string):
        tags = tag_string.strip(", \n[]")

        if "," in tags:
            pass

        tags = [i.strip().replace('"', "") for i in tags.split(",")]

        return tags

    def __remove_unneeded_folders(self, top_folder):
        if self.agent_type in [PlatformVariableConstants.TYPE_NETWORK_ELEMENT.upper(),
                               PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT.upper()]:
            base_folders = ["base", "baseversion", "baseunit"]
        elif self.agent_type in [PlatformVariableConstants.TYPE_UI_ELEMENT.upper()]:
            base_folders = ["baseappver"]
        else:
            base_folders = []

        for i in range(len(base_folders))[::-1]:
            if i == len(base_folders) - 1:
                if os.path.exists(os.path.join(self.generation_temp_dir, top_folder, *base_folders[:i + 1])):
                    shutil.rmtree(os.path.join(self.generation_temp_dir, top_folder, *base_folders[:i + 1]))
            else:
                if os.path.exists(os.path.join(self.generation_temp_dir, top_folder, *base_folders[:i + 1])):
                    folder_contents = os.listdir(os.path.join(self.generation_temp_dir, top_folder,
                                                              *base_folders[:i + 1]))
                    if len([j for j in folder_contents if j.lower() not in["__init__.py", "__init__.pyc"]]) == 0:
                        shutil.rmtree(os.path.join(self.generation_temp_dir, top_folder, *base_folders[:i + 1]))

    def __get_functions_from_data_bean_list(self, data_bean_list):
        """
        This function creates a dictionary whose key is a feature name and whose value is a list. It iterates over
        the list of data_beans and grabs the feature it adds a key to the dictionary if the feature has not yet
        been added. Then it grabs the interface method and adds that to the list for the given feature. This
        dictionary/list is used later to create the base API files.
        """
        for data_bean in data_bean_list:
            if data_bean.agent == self.agent_type:
                if data_bean.feature not in self.functions_by_feature:
                    self.functions_by_feature[data_bean.feature] = {"file_name": data_bean.base_file_name,
                                                                    "methods": [],
                                                                    }

                if data_bean.interface_method not in self.functions_by_feature[data_bean.feature]["methods"]:
                    self.functions_by_feature[data_bean.feature]["methods"].append(data_bean.interface_method)

    def __get_base_vars_from_data_bean_list(self, data_bean_list):
        for data_bean in data_bean_list:
            if data_bean.is_base:
                if isinstance(data_bean, (NetElemPlatformVariableDataBean, EndSysPlatformVariableDataBean)):
                    if data_bean.operating_system not in self.plat_var_base_vars:
                        self.plat_var_base_vars[data_bean.operating_system] = []
                    self.plat_var_base_vars[data_bean.operating_system].append(data_bean)
                elif isinstance(data_bean, UiElementPlatformVariableDataBean):
                    if data_bean.application not in self.plat_var_base_vars:
                        self.plat_var_base_vars[data_bean.application] = []
                    self.plat_var_base_vars[data_bean.application].append(data_bean)

    def __create_directory(self, path):
        """
        This function creates the given directory and adds an __init__.py file to it.
        """
        try:
            os.makedirs(path)
            self.__create_python_init_file(path)
        except OSError:
            pass

    def __get_csv_parser_and_api_generator(self):
        if self.dev_type == self.gen_constants.DEVICE_TYPE_NET_ELEM:
            if self.csv_type == self.gen_constants.API_TYPE_COMMAND:
                self.has_constants_files = True
                csv_parser = ParseCommandCsvs(self.input_dir, self.agent_type)

                if self.agent_type == self.gen_constants.AGENT_TYPE_CLI:
                    api_gen = CreateCliApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_SNMP:
                    api_gen = CreateSnmpApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_REST:
                    self.has_data_file = True
                    api_gen = CreateRestApi(self.output_dir, self.dev_type, self.agent_type)
                else:
                    raise ValueError(self.agent_type + " is not a valid agent type for network element command CSVs.")
            elif self.csv_type == self.gen_constants.API_TYPE_PARSE:
                if self.agent_type in [self.gen_constants.AGENT_TYPE_CLI,
                                       self.gen_constants.AGENT_TYPE_SNMP,
                                       self.gen_constants.AGENT_TYPE_REST]:
                    self.update_api = True
                    self.api_search_str = "CustomShowTools.py"
                    self.has_constants_files = True
                    csv_parser = ParseCliParseCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateParseApi(self.output_dir, self.dev_type, self.agent_type)
                else:
                    raise ValueError(self.agent_type + " is not a valid agent type for network element parse CSVs.")
            elif self.csv_type == self.gen_constants.API_TYPE_PLATFORM_VARIABLE:
                self.full_output_dir = self.output_dir
                self.generation_temp_dir = os.path.join(self.output_dir, "..", "GenerationTemp")
                csv_parser = ParseNetElemPlatVarCsvs(self.input_dir, self.agent_type)
                api_gen = CreatePlatVars(self.output_dir, self.dev_type, self.agent_type)
            else:
                raise ValueError(self.csv_type + " is not a valid CSV type for Network Elements.")
        elif self.dev_type == self.gen_constants.DEVICE_TYPE_END_SYS_ELEM:
            if self.csv_type == self.gen_constants.API_TYPE_COMMAND:
                if self.agent_type == self.gen_constants.AGENT_TYPE_CLI:
                    self.has_constants_files = True
                    csv_parser = ParseCliCommandCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateCliApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_REST or self.gen_constants.AGENT_TYPE_XMC_REST:
                    self.has_data_file = True
                    self.has_constants_files = True
                    csv_parser = ParseRestCommandCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateRestApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_NORTHBOUND:
                    self.has_constants_files = True
                    csv_parser = ParseNorthboundCommandCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateNorthboundApi(self.output_dir, self.dev_type, self.agent_type)
                else:
                    raise ValueError(self.agent_type + " is not a valid agent type for end system command CSVs.")
            elif self.csv_type == self.gen_constants.API_TYPE_PARSE:
                if self.agent_type == self.gen_constants.AGENT_TYPE_CLI:
                    self.update_api = True
                    self.api_search_str = "CustomShowTools.py"
                    self.has_constants_files = True
                    csv_parser = ParseCliParseCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateParseApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_REST:
                    self.update_api = True
                    self.api_search_str = "CustomShowTools.py"
                    self.has_constants_files = True
                    csv_parser = ParseCliParseCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateParseApi(self.output_dir, self.dev_type, self.agent_type)
                elif self.agent_type == self.gen_constants.AGENT_TYPE_NORTHBOUND:
                    self.has_constants_files = True
                    csv_parser = ParseNorthboundParseCsvs(self.input_dir, self.agent_type)
                    api_gen = CreateNorthbounParseApi(self.output_dir, self.dev_type, self.agent_type)
                else:
                    raise ValueError(self.agent_type + " is not a valid agent type for end system parse CSVs.")
            elif self.csv_type == self.gen_constants.API_TYPE_PLATFORM_VARIABLE:
                self.full_output_dir = self.output_dir
                self.generation_temp_dir = os.path.join(self.output_dir, "..", "GenerationTemp")
                csv_parser = ParseEndSysPlatVarCsvs(self.input_dir, self.agent_type)
                api_gen = CreatePlatVars(self.output_dir, self.dev_type, self.agent_type)
            else:
                raise ValueError(self.csv_type + " is not a valid CSV type for End System Elements.")
        elif self.dev_type == self.gen_constants.DEVICE_TYPE_UI_ELEM:
            if self.csv_type == self.gen_constants.API_TYPE_COMMAND:
                if self.agent_type == self.gen_constants.AGENT_TYPE_SELENIUM:
                    if self.app_type in self.app_type_list:
                        self.input_dir = os.path.join(self.input_dir, self.app_type)
                        self.update_api = True
                        self.has_constants_files = True
                        self.api_search_str = ".py"
                        self.has_base_files = False
                        csv_parser = ParseUiElementCsvs(self.input_dir, self.agent_type)
                        api_gen = CreateUiApi(self.output_dir, self.dev_type, self.agent_type)
                    else:
                        raise ValueError(self.app_type + " is not a valid app type for ui element command CSVs.")
                else:
                    raise ValueError(self.agent_type + " is not a valid agent type for ui element command CSVs.")
            elif self.csv_type == self.gen_constants.API_TYPE_PLATFORM_VARIABLE:
                self.full_output_dir = self.output_dir
                self.generation_temp_dir = os.path.join(self.output_dir, "..", "GenerationTemp")
                csv_parser = ParseUiElemPlatVarCsvs(self.input_dir, self.agent_type)
                api_gen = CreatePlatVars(self.output_dir, self.dev_type, self.agent_type)
            else:
                raise ValueError(self.csv_type + " is not a valid CSV type for UI Elements.")
        else:
            raise ValueError(self.dev_type + " is not a supported device type.")

        return csv_parser, api_gen

    @staticmethod
    def __create_python_init_file(path):
        """
        This function creates an __init__.py file within the given path.
        """
        file_name = "__init__.py"
        open(os.path.join(path, file_name), "w").close()


def parse_args():
    """
    This function configures the option parser and parses the command line arguments.

    The supported args are as follows.

    -d --device_type - The type of device that is being parsed (netelem, endsys, uielem, etc)
    -t --csv_type - The type of CSV being parsed (command, parse)
    -a --agent_type - The agent intended to bse used when sending the command/parsing output (cli, rest, selenium, etc)
    -i --input_dir - The folder that contains the CSV files.
    -o --output_dir - The folder where the generated APIs should be placed.
    """
    opt_parser = OptionParser()
    opt_parser.add_option("-d", "--dev_type", help="The type of device being parsed.", dest="dev_type")
    opt_parser.add_option("-t", "--csv_type", help="The type of CSV being parsed.", dest="csv_type")
    opt_parser.add_option("-a", "--agent_type", help="The agent intended to be used when sending the command/"
                                                     "parsing the output.", dest="agent_type")
    opt_parser.add_option("-i", "--input_dir", help="The folder that contains the CSV files.", dest="input_dir")
    opt_parser.add_option("-o", "--output_dir", help="The folder where the generated APIs should be placed.",
                          dest="output_dir")
    parsed_options, _ = opt_parser.parse_args()

    return parsed_options


def check_args(args):
    """
    This function checks the passed command line arguments and verifies that all required values are present.
    It prints an error message which lists the missing arguments.
    """
    errors = []
    if not args.csv_type:
        errors.append("ERROR: Required argument missing, CSV type (-t <csv_type)")
    if not args.agent_type:
        errors.append("ERROR: Required argument missing, agent type (-a <agent_type)")

    Logger().log_info("\n" + "\n".join(errors))


if __name__ == '__main__':
    options = parse_args()

    try:
        main_input_dir = options.input_dir if options.input_dir else None
        main_output_dir = options.output_dir if options.output_dir else None
        gen_apis = GenerateAllApis(options.dev_type, options.csv_type, options.agent_type,
                                   main_input_dir, main_output_dir)
        gen_apis.generate_all_apis()
    except (AttributeError, TypeError):
        check_args(options)
