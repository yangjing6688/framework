import sys

from robot.libraries.BuiltIn import BuiltIn
from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.UpdateEnvironment import UpdateEnvironment
from ExtremeAutomation.Keywords.TrafficKeywords.Utils.Constants.GenerateRobotVariables import logger
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariableConstants import PlatformVariableConstants
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
import re

p1 = '^\$\{'   # regex check to see if the var is already in robot format

class RobotUtils():
    
    @staticmethod
    def get_variables(no_decoration=True):
        return BuiltIn().get_variables(no_decoration=no_decoration)
   
    @staticmethod
    def get_variable_value(varname, default=None):
        return BuiltIn().get_variable_value(varname, default)
    
    @staticmethod
    def set_global_variable(key, value):
        BuiltIn().set_global_variable(key, value)
    
    
    @staticmethod
    def update_variables(device_name, learned_system):
        """Updates the environment dictionary with the learn_system variables."""
        try:
            elem_prefix = RobotUtils.get_device_prefix(device_name)[1]
            if elem_prefix is not None:
                suite_vars = BuiltIn().get_variables(no_decoration=True)[elem_prefix]
                updated_dict = UpdateEnvironment().update_environment(device_name, learned_system, suite_vars)
                BuiltIn().set_global_variable(elem_prefix, updated_dict)
            else:
                logger().log_trace("Unable to find prefix for device " + device_name +
                                   ", cannot update its variables.")
        except Exception:
            pass

    @staticmethod
    def add_value_to_variables(device_name, *key_value_pairs):
        """Adds the new key:value pairs to the Environment dictionary."""
        if len(key_value_pairs) % 2 != 0:
            raise ValueError("Each key must have a matching value.")

        elem_prefix = RobotUtils.get_device_prefix(device_name)[1]

        try:
            suite_vars = BuiltIn().get_variables(no_decoration=True)[elem_prefix]

            i = 0
            while i < len(key_value_pairs):
                suite_vars[key_value_pairs[i]] = key_value_pairs[i + 1]
                i += 2
            BuiltIn().set_global_variable(elem_prefix, suite_vars)
        except Exception:
            pass
    
    @staticmethod
    def get_ports_from_test_environment(var_dict, port_list=None):
        """Return a dictionary of all port ifnames in the environment."""
        if port_list is None:
            port_list = {}

        for key in var_dict:
            if isinstance(var_dict[key], dict):
                if "ifname" in var_dict[key]:
                    port_list[key] = var_dict[key]["ifname"]
                else:
                    RobotUtils.get_ports_from_test_environment(var_dict[key], port_list)
        return port_list
    
    @staticmethod
    def get_device_prefix(device_name):
        """Returns the device's type and prefix."""
        device = DeviceCollectionManager().get_device(device_name, init=False)

        element_type = None
        element_prefix = None

        if PlatformVariableConstants.TYPE_NETWORK_ELEMENT in str(type(device)):
            element_type = PlatformVariableConstants.TYPE_NETWORK_ELEMENT
            element_prefix = PlatformVariableConstants.YAML_NETWORK_ELEM_PREFIX
        elif PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT in str(type(device)):
            element_type = PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT
            element_prefix = PlatformVariableConstants.YAML_END_SYSTEM_ELEM_PREFIX
        elif PlatformVariableConstants.TYPE_UI_ELEMENT in str(type(device)):
            element_type = PlatformVariableConstants.TYPE_UI_ELEMENT
            element_prefix = PlatformVariableConstants.YAML_UI_ELEM_PREFIX

        element_number = RobotUtils().get_device_number(element_prefix, device_name)

        return element_type, element_prefix + element_number if element_number is not None else None
    
    @staticmethod
    def get_device_number(device_prefix, device_name):
        """Returns the device's index number in the environment."""
        try:
            variables = BuiltIn().get_variables(no_decoration=True)
            regex = "^" + device_prefix + r"\d+$"
            device_number = [k for k in variables if len(re.findall(regex, k)) != 0 and
                             variables[k]["name"] == device_name]

            if len(device_number) == 1:
                # Gets the numbers within the string netelem<#>_name.
                # Splits the string into two parts [netleme<#>, name]
                # Iterates over "netelem<#>" and creates a list of digit characters.
                # Joins the list into a string and returns it.
                return "".join([i for i in device_number[0] if i.isdigit()])
            elif len(device_number) >= 2:
                logger().log_debug(variables)
                raise Exception("Each netelem name must be unique within the test environment file.")
        except Exception:
            return None
        return None
