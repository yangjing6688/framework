import os
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariableConstants \
    import PlatformVariableConstants


class PlatformVariableFactory(BaseApiFactory):
    def __init__(self):
        super(PlatformVariableFactory, self).__init__()
        self.element_type = None

    def get_api(self, device, *args):
        """
        This function overrides the parent class get_api function. It first attempst to
        set the element_type. Then it calls the parent class get_api function.
        """
        try:
            self.element_type = args[0].upper()
        except IndexError:
            raise IndexError("An element type must be provided.")

        return super(PlatformVariableFactory, self).get_api(device, None, None)

    def set_base_path(self, device):
        """
        This function sets the api_name, base_path, and base_file_name based on the device type.
        """
        self.api_name = "PlatformVariables"
        self.base_path = os.path.join(PathUtils.get_api_root(), device.get_device_type(), "GeneratedApis",
                                      "PlatformVariables")

        if self.element_type in [PlatformVariableConstants.TYPE_NETWORK_ELEMENT.upper(),
                                 PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT.upper()]:
            self.base_file_name = os.path.join(device.oper_sys, "baseplatvars", device.oper_sys.capitalize() +
                                               "PlatformVariables.py")
        else:
            self.base_file_name = os.path.join(device.application, "baseplatvars", device.application.capitalize() +
                                               "PlatformVariables.py")

    def set_factory_folders(self, device):
        """
        This function sets and return the factory folders based on the device type.
        """
        if self.element_type in [PlatformVariableConstants.TYPE_NETWORK_ELEMENT.upper(),
                                 PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT.upper()]:
            factory_folders = [device.platform,
                               device.version,
                               device.unit
                               ]

            return factory_folders
        elif self.element_type == PlatformVariableConstants.TYPE_UI_ELEMENT.upper():
            factory_folders = [device.app_version]

            return factory_folders
