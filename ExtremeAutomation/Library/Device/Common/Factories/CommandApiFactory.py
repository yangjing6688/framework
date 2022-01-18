import os
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory


class CommandApiFactory(BaseApiFactory):
    def set_base_path(self, device):
        """
        Overrides the parent class function. This sets the base path based information from
        the device object.
        """
        agent_type = self._get_agent_type(device)

        self.base_path = os.path.join(PathUtils.get_api_root(), device.get_device_type(), "GeneratedApis",
                                      "CommandApis")

        if agent_type is not None:
            self.base_path = os.path.join(self.base_path, agent_type)

    def set_factory_folders(self, device):
        """
        This function defines which attributes of the device should be used to generate
        an API path.
        """
        factory_folders = [device.platform,
                           device.version,
                           device.unit
                           ]

        return factory_folders
