import yaml
import platform
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class GlobalVariableCache(object, metaclass=Singleton):
    global_var_cache = {}

    def __init__(self):
        super(GlobalVariableCache, self).__init__()
        self.logger = Logger()
        self.__read_global_values()
        self.__loaded = True

    def add_global_value(self, value_name, value, log=True):
        """
        This function adds the given entry, 'value_name': value, to the global variable cache.
        """
        if value_name in self.global_var_cache:
            if log:
                self.logger.log_info("ENTRY " + value_name + " ALREADY EXISTS, UPDATING.")

        self.global_var_cache[value_name] = value

    def get_global_value(self, value_name, default_value=None):
        """
        This function returns the value for the given value_name in the variable cache.
        """
        if value_name in self.global_var_cache:
            return self.global_var_cache[value_name]
        else:
            return default_value

    def update_global_value(self, value_name, value, log=True):
        """
        This function updates the given value_name's value in the global variable cache
        """
        if value_name not in self.global_var_cache:
            if log:
                self.logger.log_info("ENTRY " + value_name + " DOES NOT EXIST, CREATING.")

        self.global_var_cache[value_name] = value

    def __read_global_values(self):
        try:
            # read in the values from global_cache_values.yaml
            # these are not added to __add_value_storage_to_suite_vars
            if platform.system() == 'Windows':
                req_yaml = "c:\\TRM_DATA\\"
            else:
                req_yaml = "/TRM_DATA/"
            req_yaml += "global_cache_values.yaml"
            with open(req_yaml, "r") as yaml_stream:
                parsed_yaml = yaml.safe_load(yaml_stream)
            for key, value in parsed_yaml.items():
                self.add_global_value(key, value)
        except FileNotFoundError:
            # the file doesn't exist.
            self.logger.log_trace("The Global Variable Cache does not exist.")


class GlobalVariableCacheConstants(object, metaclass=Singleton):
    DEBUG_VALUE_CLI_TIME_OUT = "DEBUG_VALUE_CLI_TIME_OUT"
    PREVIOUS_KW_RESULT = "previous_kw_result"

    # Don't allow values to be updated
    def __setattr__(self, *_):
        """Do NOT allow values to be updated."""
        pass
