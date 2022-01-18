import importlib
import os

from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Device.VirtualEnvironment.Constants.VirtualConstants import VirtualConstants


class VirtualMachineFactory:
    def __init__(self):
        self.loaded_api_dict = dict()
        self.logger = Logger()

    def get_api(self, vm_device, _type):
        """
        Gets the API for the given device and type.
        """
        # if the dict is empty, just add in the API
        path = vm_device.get_path(_type)
        if not bool(self.loaded_api_dict):
            loaded_api = self.__create_new_virtual_machine_object(_type, path, vm_device)
            self.loaded_api_dict[path] = loaded_api
        else:
            # check if the API is already loaded
            if path in self.loaded_api_dict.values():
                loaded_api = self.loaded_api_dict[path]
            else:
                loaded_api = self.__create_new_virtual_machine_object(_type, path, vm_device)
                self.loaded_api_dict[path] = loaded_api
        if self.loaded_api_dict is None:
            if vm_device.version is not VirtualConstants.VERSION_BASE or \
                    vm_device.unit is not VirtualConstants.UNIT_BASE:
                vm_device.unit = vm_device.unit
                vm_device.version = VirtualConstants.VERSION_BASE
                path = vm_device.get_api_path(_type)
                loaded_api = self.__create_new_virtual_machine_object(_type, path, vm_device)
                self.loaded_api_dict[path] = loaded_api
                self.logger.log_error('WARNING: base version, base unit Virtual Machine was loaded')

        return loaded_api

    def __create_new_virtual_machine_object(self, vm_name, path, vm_device):
        # print 'Loading API for ' + path
        path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + path
        path = PathUtils.get_import_path(path)
        try:
            loaded_source = importlib.import_module(path, "VirtualBaseApi")
            loaded_api = loaded_source.create_instance(vm_device)
            return loaded_api
        except Exception as e:
            self.logger.log_debug(e)
            # let's ignore the API which are not valid
            if "No such file or directory" not in str(e):
                self.logger.log_error('FAILED to LOAD: ' + path + " -> " + str(e))
            return None
