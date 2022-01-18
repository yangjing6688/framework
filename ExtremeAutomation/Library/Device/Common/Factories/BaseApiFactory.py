import os
import re
import abc
import importlib
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants


class BaseApiFactory(object):
    API_TYPE_CLI = "CLI"
    API_TYPE_REST = "REST"
    API_TYPE_SIESTA = "SIESTA"
    API_TYPE_SELENIUM = "SELENIUM"
    API_TYPE_SNMP = "SNMP"
    API_TYPE_NORTHBOUND = "NORTHBOUND"
    API_TYPE_XMC_REST = "XMC_REST"

    def __init__(self):
        self.loaded_api_dict = {}
        self.logger = Logger()
        self.api_name = None
        self.base_file_name = None
        self.base_folder = "base"

        # Attributes with setter/getter methods.
        self._base_path = None

        # Get all attribute values in AgentConstants that start with TYPE_, create a list and upper case them.
        self.valid_agents = [getattr(AgentConstants, i).upper() for i in dir(AgentConstants) if i.startswith("TYPE_")]

        # Map of agent to folder for when the agent name is not the name of the folder.
        # For example a telnet agent would map to the CLI API folder, so it needs to be in the map.
        # Rest uses the REST folder, so it does not need to be mapped.
        self.agent_map = {AgentConstants.TYPE_TELNET: self.API_TYPE_CLI,
                          AgentConstants.TYPE_CONSOLE: self.API_TYPE_CLI,
                          AgentConstants.TYPE_SSH: self.API_TYPE_CLI,
                          AgentConstants.TYPE_JSON_RPC: self.API_TYPE_CLI,
                          AgentConstants.TYPE_REST: self.API_TYPE_REST,
                          AgentConstants.TYPE_JSON: self.API_TYPE_REST,
                          AgentConstants.TYPE_XMC_REST: self.API_TYPE_XMC_REST,
                          AgentConstants.TYPE_NORTHBOUND: self.API_TYPE_NORTHBOUND,
                          AgentConstants.TYPE_SNMP: self.API_TYPE_SNMP,
                          AgentConstants.TYPE_SELENIUM: self.API_TYPE_SELENIUM,
                          AgentConstants.TYPE_EXT_SELENIUM: self.API_TYPE_SELENIUM,
                          AgentConstants.TYPE_BASE_SELENIUM: self.API_TYPE_SELENIUM}
        self.ui_folder_path_agents = {AgentConstants.TYPE_EXT_SELENIUM,
                                      AgentConstants.TYPE_SELENIUM,
                                      AgentConstants.TYPE_BASE_SELENIUM}

    @property
    def base_path(self):
        """
        Property function for base_path, this function returns the private attribute _base_path.
        """
        return self._base_path

    @base_path.setter
    def base_path(self, path):
        """
        Setter function for base_path, this function returns the absolute path of the passed <path>.
        """
        self._base_path = os.path.abspath(path)

    @abc.abstractmethod
    def set_base_path(self, device):
        """
        This method must be implemented by any child class.

        The purpose of this method is to tell the factory where the top level folder
        for the given api structure is located.
        """
        pass

    @abc.abstractmethod
    def set_factory_folders(self, device):
        """
        This method must be implemented by any child class.

        The purpose of this method is to tell the factory how many layers deep the api folder structure is.

        The list should be in the following format

        Generic Example:        Network Element Example:
        [device.<folder_1>,     [device.platform,
         device.<folder_2>,      device.version,
         device.<folder_n>       device.unit
         ]                       ]

        Where <folder> is an attribute of the device.
        """
        return []

    def get_api(self, device, api_name=None, api_args=None):
        """
        Function Args:
        [device] - An instance of a device object.
        [api_name] - The name of the API to be retrieved.
        [api_args] - The arguments that should be passed when instantiating an API.

        This function attempts to retrieve the API based on the the passed <api_name>.
        It then attempts to instantiate it, if it is successful the created instance is
        returned, otherwise None is returned.
        """
        self.set_base_path(device)
        folders = self.set_factory_folders(device)
        base_attrs = device.get_base_attrs()

        path = self.get_api_path_with_wildcards(device, api_name, folders, base_attrs)
        loaded_api = self._create_new_api_object(path, device, api_args)

        if loaded_api is not None:
            self.loaded_api_dict[path] = loaded_api

        return loaded_api

    def get_api_path_with_wildcards(self, device, feature, folders, base_attrs):
        """
        Function Args:
        [device] - An instance of a device object.
        [feature] - The name of the API to be retrieved.
        [folders] - Folders based on the attributes of the device object.
        [base_attrs] - The folders that should be used if no match can be found for
                       a given folder.

        This function attempts to build a path with the best possible match based
        on the provided information. If no path can be created it will attempt to build
        a base path using the <base_attrs> information. If it still cannot create a bath
        it will use the device's base_file_name. If it still cannot find a match None
        is returned.
        """
        if feature is not None:
            if device.connection_method in self.ui_folder_path_agents:
                path = os.path.join(self.base_path, feature)
            else:
                path = os.path.join(self.base_path, feature, device.oper_sys)
        else:
            path = os.path.join(self.base_path, device.oper_sys)

        try:
            # Try to build the closest matching path according to the device's os, platform, version, and unit
            # information.
            if len(folders) != len(base_attrs):
                raise Exception("A base attribute must be provided for each folder specified.")

            for i, folder in enumerate(folders):
                if folder[0].isdigit():
                    folder = "v" + folder
                if "." in folder:
                    folder = folder.replace(".", "dot")

                path = os.path.join(path, self.find_best_match(path, folder, base_attrs[i]))

            api_file = [i for i in os.listdir(path)
                        if not i.startswith("__") and
                        i.endswith(".py") and not
                        i.endswith(".pyc") and not
                        i.lower().endswith("data.py")]

            if len(api_file) == 1:
                return os.path.join(path, api_file[0])
            elif len(api_file) > 1:
                raise Exception("Too many API files in folder " + path + ".")
            else:
                raise OSError("No API file found, using base.")
        except OSError:
            # If no path found, use the feature's base API.
            if feature is not None:
                try:
                    path = os.path.join(self.base_path, feature, self.base_folder)
                    api_file = [i for i in os.listdir(path) if not i.startswith("__") and i.endswith(".py")][0]
                    return os.path.join(path, api_file)
                except OSError:
                    return BaseApi().get_location()
            else:
                if self.base_file_name is not None:
                    return os.path.join(self.base_path, self.base_file_name)
                return None

    def _create_new_api_object(self, path, device, api_args):
        try:
            if path is not None:
                loaded_source = self.__import_class(path)
            else:
                return None

            try:
                loaded_api = loaded_source(device)
            except (TypeError, AttributeError) as e:
                if "abstract methods" in str(e):
                    raise e
                elif api_args is None:
                    loaded_api = loaded_source()
                else:
                    loaded_api = loaded_source(api_args)

            return loaded_api
        except (IOError, ImportError) as e:
            if "No such file or directory" not in str(e):
                self.logger.log_trace('FAILED to LOAD: ' + path + " -> " + str(e))
            return None

    def __import_class(self, path):
        import_path, import_class = self._get_module_info(path)
        import_mod = importlib.import_module(import_path, import_class)

        return getattr(import_mod, import_class)

    @staticmethod
    def find_best_match(path, search_value, default_value):
        """
        Function Args:
        [path] - The current search path.
        [search_value] - The folder to search for.
        [default_value] - The value to use if no match can be made.

        This function attempts to find the best match for a given folder. It attempts to build
        a list of matching folders and if one matches it is returns, otherwise return the
        default value.
        """
        folders = [i.lower() for i in os.listdir(path) if os.path.isdir(path + os.sep + i)]
        folder_regex = ["^" + i.replace(".", r"\.").replace("__", ".+") + "$" for i in folders]
        version_regex = r"v\d+(dot\d+)+"

        if search_value.lower() in folders:
            return search_value
        else:
            matches = []
            for i, folder in enumerate(folders):
                match = re.search(folder_regex[i].lower(), search_value.lower())
                if match is not None:
                    matches.append(folder)
            if len(matches) != 0:
                best_match = matches[0]
                for match in matches:
                    if match.count("__") < best_match.count("__"):
                        best_match = match
                    elif match.count("__") == best_match.count("__"):
                        if match.find("__") > best_match.find("__"):
                            best_match = match
                return best_match
            elif not matches and re.findall(version_regex, search_value):
                found_vers = []
                for i, folder in enumerate(folders):
                    match = re.findall(version_regex, folder)
                    if match:
                        search_ver_list = search_value[1:].split("dot")
                        folder_ver_list = folder[1:].split("dot")
                        if len(search_ver_list) == len(folder_ver_list):
                            for x, field in enumerate(folder_ver_list):
                                if field < search_ver_list[x]:
                                    found_vers.append(folder)
                                    break
                                elif field == search_ver_list[x]:
                                    continue
                                else:
                                    break
                if found_vers:
                    highest_version = max(found_vers)
                    if highest_version in folders:
                        return highest_version

            return default_value

    def _get_agent_type(self, device):
        if device.connection_method.upper() in self.valid_agents:
            if device.connection_method in self.agent_map:
                return self.agent_map[device.connection_method]
            else:
                return device.connection_method.upper()
        else:
            return None

    @staticmethod
    def _get_module_info(path):
        class_name = None

        with open(path, "r") as module_file:
            for line in module_file:
                if len(re.findall("^class .*:$", line.rstrip())):
                    class_name = line.split()[1][:line.split()[1].find("(")]
                    break

        module_path = PathUtils.get_import_path(path)

        if class_name is not None:
            return module_path, class_name
        else:
            raise ValueError("Unable to determine class name in file " + path)
