from ExtremeAutomation.Library.Utils.DotDict import DotDict
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Utils.RobotUtils import RobotUtils


class DeviceValueStorage(object, metaclass=Singleton):
    storageDictionary = DotDict()

    def __init__(self):
        super(DeviceValueStorage, self).__init__()
        self.logger = Logger()

    def add_value(self, device_name, value_name, value):
        """
        Arguments:
        [name] - The name of the device
        [device] - Must be type (ManagedDeviceObject)
        """
        if device_name not in self.storageDictionary:
            self.storageDictionary[device_name] = DotDict()
        if value_name in self.storageDictionary[device_name]:
            self.logger.log_info("ENTRY " + value_name + " ALREADY EXISTS, UPDATING.")

        self.storageDictionary[device_name][value_name] = value

        self.__add_value_storage_to_suite_vars(device_name)

    def update_value(self, device_name, value_name, value):
        """
        Args:
        [name] - The name of the device.

        """
        if device_name not in self.storageDictionary:
            self.logger.log_info("Device storage for " + device_name + " was not found, creating.")
            self.storageDictionary[device_name] = DotDict()

        if value_name not in self.storageDictionary[device_name]:
            self.logger.log_info("ENTRY " + value_name + " DOES NOT EXIST, CREATING.")

        self.storageDictionary[device_name][value_name] = value

        self.__add_value_storage_to_suite_vars(device_name)

    def get_value(self, device_name, value_name):
        """
        Arguments:
        [name] - The name of the device
        """
        if device_name in self.storageDictionary:
            if value_name in self.storageDictionary[device_name]:
                return self.storageDictionary[device_name][value_name]
            else:
                self.logger.log_info("Device storage for value " + value_name + " was not found.")
        else:
            self.logger.log_info("Device storage for " + device_name + " was not found.")

    def __add_value_storage_to_suite_vars(self, device_name):
        RobotUtils.add_value_to_variables(device_name, "value_storage", self.storageDictionary[device_name])
