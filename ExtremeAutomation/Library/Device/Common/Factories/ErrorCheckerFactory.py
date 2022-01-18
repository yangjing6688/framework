import os
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory


class ErrorCheckerFactory(BaseApiFactory):
    def set_base_path(self, device):
        """
        Overrides the parent class function. This sets the base path based information from
        the device object.
        """
        self.set_error_checker_base_path(device)
        self.api_name = "ErrorChecker"
        self.base_file_name = "BaseErrorChecker.py"

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

    def set_error_checker_base_path(self, device):
        """
        This function sets the base path for error checker APIs.
        """
        self.base_path = os.path.join(os.path.dirname(__file__), "..", "..",
                                      str(type(device)).split(".")[-1].strip("'>"), "ErrorChecker")
