import os
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory


class PromptFactory(BaseApiFactory):
    def __init__(self):
        super(PromptFactory, self).__init__()
        self.base_file_name = "BasePromptHandler.py"

    def set_base_path(self, device):
        """
        Overrides the parent class function. This sets the base path based information from
        the device object.
        """
        self.set_prompt_handler_base_path()
        self.api_name = "PromptHandler"

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

    def set_prompt_handler_base_path(self):
        """
        This function sets the base path for prompt handler APIs.
        """
        self.base_path = os.path.join(os.path.dirname(__file__), "..", "PromptHandler")
