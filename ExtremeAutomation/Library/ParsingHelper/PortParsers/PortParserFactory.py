import os
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory


class PortParserFactory(BaseApiFactory):
    def set_base_path(self, device):
        """
        Sets the base_path, the absolute path to the PortParser folder for the current system.
        """
        self.base_path = os.path.join(os.path.dirname(__file__), "PortParser")
        self.api_name = "PortParser"

    def set_factory_folders(self, device):
        """
        Sets the folder names in the path for platform, version, and unit.
        """
        factory_folders = [device.platform,
                           device.version,
                           device.unit
                           ]

        return factory_folders
