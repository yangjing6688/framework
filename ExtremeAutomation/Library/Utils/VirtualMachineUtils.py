import re


class VirtualMachineUtils(object):
    @staticmethod
    def get_device_names_from_variables(variables_dict, var_prefix):
        """Returns a list of all devices with the same var_prefix."""
        name_regex = "^" + var_prefix + "[0-9]+$"
        index_regex = "[0-9]+$"

        names = [key for key in variables_dict.keys() if len(re.findall(name_regex, key)) == 1]
        indexes = [re.search(index_regex, i).group() for i in names]

        return [var_prefix + i for i in sorted(indexes, key=int)]

    @staticmethod
    def get_vm_names_from_variables(variables_dict, var_prefix):
        """Returns a list of all devices with the same var_prefix."""
        name_regex = "^" + var_prefix + "[0-9]+$"
        index_regex = "[0-9]+$"

        names = [key for key in variables_dict["vms"].keys() if len(re.findall(name_regex, key)) == 1]
        indexes = [re.search(index_regex, i).group() for i in names]

        return [var_prefix + i for i in sorted(indexes, key=int)]

    @staticmethod
    def get_device_number(variables, search_name):
        """
        Returns the device number.
        Ex:
        For netelem2 the device number is "2"
        """
        for key in variables:
            if isinstance(variables[key], dict):
                try:
                    if variables[key]["name"] == search_name:
                        return key
                except KeyError:
                    pass

        raise ValueError("No device's with the name " + search_name + " found.")
