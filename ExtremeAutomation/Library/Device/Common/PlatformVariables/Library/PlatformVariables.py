from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.Common.Factories.PlatformVariableFactory import PlatformVariableFactory
from io import IOBase

class PlatformVariables(object):
    def __init__(self):
        self.logger = Logger()
        self.factory = PlatformVariableFactory()
        self.robot_built_in = RobotUtils()

    def get_variables(self, device_name):
        """
        This function attempts to generate platform variables for the given device. If it is not
        able to a message will be written to the log.
        """
        elem_type, elem_prefix = RobotUtils.get_device_prefix(device_name)
        device = DeviceCollectionManager().get_device(device_name, init=False)
        plat_var_obj = self.factory.get_api(device, elem_type)

        if plat_var_obj is not None:
            self.__add_plat_vars_to_suite_vars(elem_prefix, plat_var_obj.vars)
            return plat_var_obj.vars
        else:
            self.logger.log_info("Unable to generate platform variables for " + device.name + ".")

    def __add_plat_vars_to_suite_vars(self, elem_prefix, plat_vars):
        if elem_prefix is not None:
            try:
                suite_vars = self.robot_built_in.get_variables(no_decoration=True)[elem_prefix]
                self.set_to_dictionary(suite_vars, "plat_vars", plat_vars)
                self.robot_built_in.set_global_variable("${" + elem_prefix + "}", suite_vars)
                self.logger.log_trace("Adding platform variables...")
                self.logger.log_trace(plat_vars)
            except Exception:
                self.logger.log_trace("Unable to access robot process, platform variables not added.")
        else:
            self.logger.log_trace("Unable to determine element prefix, platform variables not added.")
            
    def set_to_dictionary(self, dictionary, *key_value_pairs, **items):
        """Adds the given ``key_value_pairs`` and ``items`` to the ``dictionary``.
        Giving items as ``key_value_pairs`` means giving keys and values
        as separate arguments:
        | Set To Dictionary | ${D1} | key | value | second | ${2} |
        =>
        | ${D1} = {'a': 1, 'key': 'value', 'second': 2}
        | Set To Dictionary | ${D1} | key=value | second=${2} |
        The latter syntax is typically more convenient to use, but it has
        a limitation that keys must be strings.
        If given keys already exist in the dictionary, their values are updated.
        """
        self._validate_dictionary(dictionary)
        if len(key_value_pairs) % 2 != 0:
            raise ValueError("Adding data to a dictionary failed. There "
                             "should be even number of key-value-pairs.")
        for i in range(0, len(key_value_pairs), 2):
            dictionary[key_value_pairs[i]] = key_value_pairs[i+1]
        dictionary.update(items)
        return dictionary
    
    def _validate_dictionary(self, dictionary, position=1):
        if self.is_string(dictionary) or self.is_number(dictionary):
            raise TypeError("Expected argument %d to be a dictionary or dictionary-like, "
                            "got %s instead." % (position, self.type_name(dictionary)))
            
    def is_number(self, item):
        return isinstance(item, (int, float))
    
    
    def is_string(self, item):
        return isinstance(item, str)
    
    def type_name(self, item, capitalize=False):
        if isinstance(item, IOBase):
            name = 'file'
        else:
            typ = type(item) if not isinstance(item, type) else item
            named_types = {str: 'string', bool: 'boolean', int: 'integer',
                           type(None): 'None', dict: 'dictionary'}
            name = named_types.get(typ, typ.__name__)
        return name.capitalize() if capitalize and name.islower() else name

