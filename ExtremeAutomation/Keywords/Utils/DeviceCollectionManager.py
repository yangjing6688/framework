from ExtremeAutomation.Library.Logger.Logger import Logger


class DeviceCollectionManager(object):

    device_dict = dict()

    def __init__(self):
        self.logger = Logger()

    def add_device(self, name, device):
        """
        Arguments:
        [name] - The name of the device
        [device] - Must be type (ManagedDeviceObject)
        """
        if name in self.device_dict:
            self.logger.log_info("ENTRY " + name + " ALREADY EXISTS OVERWRITING.")
        self.device_dict[name] = device

    def add_device_with_method(self, name, device, connection_method='None'):
        """
        Arguments:
        [name] - The name of the device
        [device] - Must be type (ManagedDeviceObject)
        [connection_method] - the connection method as defined in 
                              yaml, e.g., 'telnet'
        """

        if (name in self.device_dict and
            connection_method in self.device_dict and
            connection_method != 'None'):
            self.logger.log_info("ENTRY " + name + " ALREADY EXISTS OVERWRITING.")

        self.device_dict[name] = device
        self.device_dict[connection_method] = connection_method

    def get_device(self, name, init=True):
        """
        Arguments:
        [name] - The name of the device
        """
        try:
            device = self.device_dict[name]
            if init:
                try:
                    device.init_current_agent()
                except AttributeError:
                    pass  # Device type does not need/support initializing it's agent.
            return device
        except KeyError:
            pass

    def get_device_list(self):
        """Returns: All devices."""
        return self.device_dict.keys()

    def remove_device(self, name):
        """
        Args:
        [name] - The name of the device to remove.
        """
        try:
            self.device_dict.pop(name)
        except KeyError:
            self.logger.log_info("Device " + name + " not found, unable to remove.")
