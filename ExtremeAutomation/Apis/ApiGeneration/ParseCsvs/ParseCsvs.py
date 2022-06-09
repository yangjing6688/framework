import os
import csv
import abc
import yaml
import json
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
import shutil
from ExtremeAutomation.Apis.ApiGeneration.addUuid import AddUuid


class ParseCsvs(object):
    def __init__(self, csv_dir, agent):
        """
        [csv_dir] - The top level folder where the CSVs are located.

        self.all_parsed_csvs is a nested dictionary in the following format.

        {<folder_1>:
            {<folder_2>:
                {<folder_3>:
                    {<folder_4>:
                        {<folder_N>: [<data_beans>]
                        }
                    }
                }
            }
        }

        """
        self.csv_dir = csv_dir
        self.all_parsed_csvs = {}
        self.current_csv_dir = None
        self.__data_bean_list = {}
        self.keyword_info = {"descriptions": {},
                             "uuid": {},
                             "rest_data_args": {},
                             "arg_order": {}}
        self.agent = agent
        self.logger = Logger()
        self.keyword_document_generated = os.path.join(PathUtils.get_project_root(), "ExtremeAutomation", "Documentation",
                                                       "Generated")       

    @abc.abstractmethod
    def _create_data_bean(self, csv_row, feature, uuid=None):
        """
        This function must be overridden by any child classes.

        This function describes how to create a data bean based on a given CSV row and feature.
        """
        pass

    def parse_all_csvs(self):
        """
        Parses all CSVs present in the <csv_dir>.

        Opens each CSV and creates a data bean for each row, ignoring the first header lines.

        Adds the data bean to the correct dictionary.
        """
        
       
        # Add the UUID
        self.logger.log_debug("Generating missing UUIDs")
        uuidGenerator = AddUuid()
        uuidGenerator.generateUUid()
        self.logger.log_debug("Completed generating missing UUIDs")
        
        delete_old_docs = True
        parse_api_processing = False;
        for csv_file_dir in self._get_csvs():
            self.current_csv_dir = csv_file_dir
            if delete_old_docs and "ParseApiDefinition" in self.current_csv_dir:
                parse_api_processing = True
                delete_old_docs = False
            if delete_old_docs and "ParseApiDefinition" not in self.current_csv_dir:
                if os.path.exists(self.keyword_document_generated):
                    shutil.rmtree(self.keyword_document_generated)
                self.__create_directory(self.keyword_document_generated)
                delete_old_docs = False
            
            if self.current_csv_dir.endswith(".csv"):
                self.__parse_csv()
            elif self.current_csv_dir.endswith(".yaml"):
                self.__parse_yaml(parse_api_processing)
            elif self.current_csv_dir.endswith(".json"):
                self.__parse_json()

        self.set_previous_version()

    def __parse_yaml(self, parse_api_processing):
        
        interface_method_information = {} 
        
        """Parses a YAML API definition file and creates data_beans with the standard format."""
        with open(self.current_csv_dir, "r") as yaml_file:
            yaml_file_parsed = self.current_csv_dir.split(os.sep)[-1].lower()
            self.logger.log_info("Parsing YAML: " + yaml_file_parsed)
            api_dict = yaml.safe_load(yaml_file)
            dict_keys = list(api_dict.keys())

            if len(dict_keys) > 1:
                self.logger.log_error("Too many feature keys in YAML file!\n" + str(dict_keys))
                raise KeyError
            else:
                feature = dict_keys[0]

            try:
                if not parse_api_processing:
                    # moved this here...
                    # Write Header for Doc
                    mappingfilename = self.keyword_document_generated
                    header_text =   "# Keyword Library Documentation for " + \
                                    feature.capitalize() + "\nThis feature is located in this file: `" + yaml_file_parsed + "` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition)" +\
                                    ". If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: " + \
                                    "/extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory " + \
                                    "(/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` "
                    
                    self.__create_index_file(mappingfilename, header_text, feature.capitalize())
                    self.__create_mapping_file_methods_commands(mappingfilename, header_text, feature.capitalize())
                
                for api_method in list(api_dict[feature].keys()):
                    if api_method.split("_")[0] != "show":
                        if "description" in api_dict[feature][api_method]:
                            self.keyword_info["descriptions"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["description"]
                        else:
                            self.keyword_info["descriptions"].setdefault(feature, {})[api_method] = ""
                        if "restData" in api_dict[feature][api_method].setdefault("arguments", {}):
                            self.keyword_info["rest_data_args"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["arguments"]["restData"]
                        else:
                            self.keyword_info["rest_data_args"].setdefault(feature, {})[api_method] = None
                        if "order" in api_dict[feature][api_method].setdefault("arguments", {}):
                            self.keyword_info["arg_order"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["arguments"]["order"]
                        else:
                            self.keyword_info["arg_order"].setdefault(feature, {})[api_method] = None
                            
                    uuid = 'none'
                    if "uuid" in api_dict[feature][api_method]:
                        uuid = api_dict[feature][api_method]["uuid"]
                            
                    if isinstance(api_dict[feature][api_method]["apis"], list):
                        self.__parse_api_items(api_dict[feature][api_method]["apis"], api_method, feature, self.agent, uuid=uuid)
                    else:
                        for agent in api_dict[feature][api_method]["apis"]:
                            self.__parse_api_items(api_dict[feature][api_method]["apis"][agent], api_method, feature,
                                                   agent, uuid=uuid)
                    
                    if not parse_api_processing:
                        argument_order = ""
                        try:
                            if api_method.split("_")[0] != "show":
                                argument_order = self.keyword_info["arg_order"][feature][api_method]
                                if argument_order == None:
                                    argument_order = ""
                        except Exception:
                            pass

                        if feature not in interface_method_information:
                            interface_method_information[feature] = {}

                        if api_method.split("_")[0] != "show" and api_method not in interface_method_information[feature]:
                            interface_method_information[feature][api_method] = {}
                            if 'description' in api_dict[feature][api_method]:
                                interface_method_information[feature][api_method]['description'] = api_dict[feature][api_method]["description"]
                            else:
                                interface_method_information[feature][api_method]['description'] = ""

                            commaAfterDevice = ""
                            if argument_order != "":
                                commaAfterDevice = ","
                            interface_method_information[feature][api_method]['pytest_command'] =   "\n\n\t\tself.defaultLibrary.apiLowLevelApis."+ feature + "." + feature + "_" + api_method + "(device_name" + commaAfterDevice + " " + "".join(argument_order).replace(",",", ") + ")\n"

                            interface_method_information[feature][api_method]['robot_command'] =    "\n\n\t\t" + feature + "_" + api_method + "  device_name  " + "".join(argument_order).replace(",","  ") + "\n"

                            interface_method_information[feature][api_method]['uuid'] = uuid
                            interface_method_information[feature][api_method]['api_method'] = api_method
                            interface_method_information[feature][api_method]['command_info'] = {}
                            interface_method_information[feature][api_method]['command_info']['CLI'] = []
                            interface_method_information[feature][api_method]['command_info']['REST'] = []
                            interface_method_information[feature][api_method]['command_info']['SNMP'] = []

                            end_of_command = "\n\n----------------------------------------------\n\n"

                            for agentType in api_dict[feature][api_method]['apis']:
                                if api_method.split("_")[0] != "show":
                                    if agentType == 'CLI':
                                        cli = api_dict[feature][api_method]['apis'][agentType]
                                        for cli_index in cli:
                                            file_str = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: {0}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: {1}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: {2}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: {3}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:\n\n\t\t{4}{5}".format(  str(cli_index[0]),
                                                                                                                                    str(agentType),
                                                                                                                                    str(cli_index[5]),
                                                                                                                                    str(cli_index[6]),
                                                                                                                                    str(cli_index[4]),
                                                                                                                                    end_of_command)
                                            interface_method_information[feature][api_method]['command_info']['CLI'].append(file_str)

                                    elif agentType == 'REST':
                                        rest = api_dict[feature][api_method]['apis'][agentType]
                                        for rest_index in rest:
                                            file_str = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: {0}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: {1}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: {2}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`URL`: {3}{4}".format( str(rest_index[0]),
                                                                                                                        str(agentType),
                                                                                                                        str(rest_index[4]),
                                                                                                                        str(rest_index[5]),
                                                                                                                        end_of_command)
                                            interface_method_information[feature][api_method]['command_info']['REST'].append(file_str)

                                    elif agentType == 'SNMP':
                                        snmp = api_dict[feature][api_method]['apis'][agentType]
                                        for snmp_index in snmp:
                                            file_str = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: {0}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: {1}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: {2}\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: {3}{4}".format( str(snmp_index[0]),
                                                                                                                        str(agentType),
                                                                                                                        str(snmp_index[4]),
                                                                                                                        str(snmp_index[5]),
                                                                                                                        end_of_command)
                                            interface_method_information[feature][api_method]['command_info']['SNMP'].append(file_str)
                if not parse_api_processing:
                    # Write out the documentation
                    for feature in interface_method_information.keys():
                        command_header = interface_method_information[feature]
                        for function in command_header:
                            command_data = command_header[function]
                            function_header =   "# API Function: " + function + "\n\tPytest API Call: " + command_data['pytest_command'] + "\n\tRobot API Call: " + command_data['robot_command'] + "\nUUID: " + str(command_data['uuid'])
                            self.__add_to_mapping_file_methods_commands(self.keyword_document_generated, function_header, feature.capitalize())
                            for command_group in command_data['command_info']:
                                file_str = ("## " + str(command_group))
                                self.__add_to_mapping_file_methods_commands(self.keyword_document_generated, file_str, feature.capitalize())
                                command_agent_data = command_data['command_info'][command_group]
                                for command in command_agent_data:
                                    self.__add_to_mapping_file_methods_commands(self.keyword_document_generated, command, feature.capitalize())
                        self.logger.log_info("Created documentation for " + feature.capitalize() + ".md")
            except AttributeError as error:
                self.logger.log_info("YAML API file for feature '" + feature.capitalize() + "' is empty!")
                raise error

    def __parse_csv(self):
        """Parses a CSV API definition file and creates data_beans with the standard format."""
        with open(self.current_csv_dir, "r") as csv_file:
            self.logger.log_info("Parsing CSV: " + self.current_csv_dir.split(os.sep)[-1].lower())
            csv_reader = csv.reader(csv_file)
            feature = None
            def_end = True
            for i, row in enumerate(csv_reader):
                if i == 0:
                    feature = row[1].lower()
                elif i > 1:
                    if len(row) > 0:
                        if row[0] == "Keyword Definitions:":
                            def_end = False
                            continue
                        elif row[0] == "End Keyword Definitions":
                            def_end = True
                            continue
                        if not def_end and not row[0].startswith("#"):
                            try:
                                self.keyword_info["descriptions"].setdefault(feature, {})[row[0]] = row[1]
                            except IndexError:
                                self.keyword_info["descriptions"].setdefault(feature, {})[row[0]] = ""
                            try:
                                self.keyword_info["arg_order"].setdefault(feature, {})[row[0]] = row[2]
                            except IndexError:
                                self.keyword_info["arg_order"].setdefault(feature, {})[row[0]] = None
                        elif not row[0].startswith("#"):
                            data_bean = self._create_data_bean(row, feature)
                            data_bean = [data_bean] if not isinstance(data_bean, list) else data_bean
                            for bean in data_bean:
                                bean.agent = self.agent
                                self.add_data_bean_to_dict(feature, bean)

    def __parse_json(self):
        """Parses a JSON API definition file and creates data_beans with the standard format."""
        with open(self.current_csv_dir, "r") as json_file:
            self.logger.log_info("Parsing YAML: " + self.current_csv_dir.split(os.sep)[-1].lower())
            api_dict = json.load(json_file)
            dict_keys = list(api_dict.keys())

            if len(dict_keys) > 1:
                self.logger.log_error("Too many feature keys in YAML file!\n" + str(dict_keys))
                raise KeyError
            else:
                feature = dict_keys[0]

            try:
                for api_method in list(api_dict[feature].keys()):
                    if api_method.split("_")[0] != "show":
                        if "description" in api_dict[feature][api_method]:
                            self.keyword_info["descriptions"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["description"]
                        else:
                            self.keyword_info["descriptions"].setdefault(feature, {})[api_method] = ""
                        if "restData" in api_dict[feature][api_method].setdefault("arguments", {}):
                            self.keyword_info["rest_data_args"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["arguments"]["restData"]
                        else:
                            self.keyword_info["rest_data_args"].setdefault(feature, {})[api_method] = None
                        if "order" in api_dict[feature][api_method].setdefault("arguments", {}):
                            self.keyword_info["arg_order"].setdefault(feature, {})[api_method] = \
                                api_dict[feature][api_method]["arguments"]["order"]
                        else:
                            self.keyword_info["arg_order"].setdefault(feature, {})[api_method] = None

                    if isinstance(api_dict[feature][api_method]["apis"], list):
                        self.__parse_api_items(api_dict[feature][api_method]["apis"], api_method, feature, self.agent)
                    else:
                        for agent in api_dict[feature][api_method]["apis"]:
                            self.__parse_api_items(api_dict[feature][api_method]["apis"][agent], api_method, feature,
                                                   agent)
            except AttributeError as error:
                self.logger.log_info("YAML API file for feature '" + feature + "' is empty!")
                raise error

    def set_previous_version(self):
        """
        This function looks at each data bean and attempts to figure out it's previous version.
        If no previous version can be determined, base is used.
        """
        version_dict = self.__create_version_dictionary()
        self.__update_data_bean_previous_version(version_dict)

    def __create_version_dictionary(self):
        version_dict = {}

        for feature in self.__data_bean_list:
            version_dict[feature] = {}
            for data_bean in self.__data_bean_list[feature]:
                current_bean_path = ", ".join([i[0] for i in data_bean.get_folders() if not i[1]])
                current_bean_version = "".join([i[0] for i in data_bean.get_folders() if i[1]])

                if current_bean_path not in version_dict[feature]:
                    version_dict[feature][current_bean_path] = []
                if current_bean_version not in version_dict[feature][current_bean_path]:
                    version_dict[feature][current_bean_path].append(current_bean_version)

        for feature in version_dict:
            for key in version_dict[feature]:
                version_dict[feature][key].sort()
                if NetworkElementConstants.VERSION_BASE in version_dict[feature][key]:
                    base_index = version_dict[feature][key].index(NetworkElementConstants.VERSION_BASE)
                    version_dict[feature][key].insert(0, version_dict[feature][key].pop(base_index))

        return version_dict

    def __update_data_bean_previous_version(self, version_dict):
        for feature in self.__data_bean_list:
            for data_bean in self.__data_bean_list[feature]:
                current_bean_path = ", ".join([i[0] for i in data_bean.get_folders() if not i[1]])
                current_bean_version = "".join([i[0] for i in data_bean.get_folders() if i[1]])
                version_index = version_dict[feature][current_bean_path].index(current_bean_version)
                if version_index > 0:
                    data_bean.previous_version = version_dict[feature][current_bean_path][0:version_index]

    def __parse_api_items(self, api_list, api_method, feature, agent, uuid=None):
        for api in api_list:
            api_list = [api_method]
            api_list.extend(api)
            api_list.append(agent)
            data_bean = self._create_data_bean(api_list, feature, uuid=uuid)
            data_bean = [data_bean] if not isinstance(data_bean, list) else data_bean
            for bean in data_bean:
                bean.agent = agent
                self.add_data_bean_to_dict(feature, bean)

    def _get_csvs(self):
        """
        Scans <csv_dir> and any sub-folders for files with the extension ".csv".

        The path for each file that is found is appended to a list.

        Then the created list is returned.
        """
        all_csv_paths = []

        for dir_path, dir_names, file_names in os.walk(self.csv_dir):
            for file_name in file_names:
                extension = os.path.splitext(file_name)[1]
                if extension == ".csv" or extension == ".yaml":
                    all_csv_paths.append(dir_path + os.sep + file_name)

        return all_csv_paths

    def add_data_bean_to_dict(self, feature, data_bean):
        """
        Takes a data bean and adds to the correct list within the nested dictionary.
        """
        # Get the list of folders for the current data bean.
        # get_folders() returns a tuple, we only need the first item.
        folders = [i[0] for i in data_bean.get_folders()]
        current_folder = self.all_parsed_csvs

        # Iterate over each folder in the folders list.
        # For every folder except the last, check if it's in the
        # current_folder dictionary. If it's not add a dictionary
        # Then set current_folder to the newly added dictionary.
        # When we get to the last item in the list check if it's
        # in the dictionary, if it's not add a list. Then add the
        # data bean to the list.
        for i, folder in enumerate(folders):
            if i == len(folders) - 1:
                if folder not in current_folder:
                    current_folder[folder] = []
                current_folder[folder].append(data_bean)
            else:
                if folder not in current_folder:
                    current_folder[folder] = {}
                current_folder[folder].setdefault('contains_agents', set()).add(data_bean.agent)
                current_folder = current_folder[folder]

        # Check if the feature is in the __data_bean_list. If it's
        # not add a list. Then append the data bean to the list.
        if feature not in self.__data_bean_list:
            self.__data_bean_list[feature] = []
        self.__data_bean_list[feature].append(data_bean)
        
    
    
    def __create_mapping_file_methods_commands(self, mappingdir, header_text, feature):
        os.makedirs(mappingdir, exist_ok=True)
        mappingfilename = os.path.join(mappingdir, feature + '.md')               
        with open(mappingfilename, "w") as file_object:           
            file_object.write(header_text + "\n\n")
            
    def __create_index_file(self, mappingdir, header_text, feature):
        os.makedirs(mappingdir, exist_ok=True)
        mappingfilename = os.path.join(mappingdir, 'index.md')               
        with open(mappingfilename, "a") as file_object:
            feature_link = str(feature) + '.md'
            index_feature = "# [" + str(feature) + "](" + feature_link + ") \n\nThis is the " + feature + " documentation page for all of the generated low level libraries\n\n"
            file_object.write(index_feature + "\n\n")
            
    def __add_to_mapping_file_methods_commands(self, mappingdir, method_command, feature):
        mappingfilename = os.path.join(mappingdir, feature + '.md')               
        with open(mappingfilename, "a") as file_object:
            file_object.write(method_command+"\n")    
    
    
    def __create_directory(self, path):
        """
        This function creates the given directory and adds an __init__.py file to it.
        """
        try:
            os.makedirs(path)
        except OSError:
            pass
