import os
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Device.Common.Factories.BaseApiFactory import BaseApiFactory


class UiElementCommandApiFactory(BaseApiFactory):
    APPLICATION_EMC = "EMC"
    APPLICATION_XMC = "XMC"
    APPLICATION_XCA = "XCA"
    APPLICATION_GIM = "GIM"
    APPLICATION_EWC = "EWC"
    APPLICATION_ECIQ = "ECIQ"
    APPLICATION_DFNDR = "DFNDR"

    def __init__(self):
        super(UiElementCommandApiFactory, self).__init__()
        self.valid_applications = {self.APPLICATION_EWC,
                                   self.APPLICATION_GIM,
                                   self.APPLICATION_XMC,
                                   self.APPLICATION_XCA,
                                   self.APPLICATION_EMC,
                                   self.APPLICATION_ECIQ,
                                   self.APPLICATION_DFNDR}

    def set_base_path(self, device):
        """
        Overrides the parent class function. This sets the base path based information from
        the device object.
        """
        agent_type = self._get_agent_type(device)
        application = self._get_application_type(device)

        self.base_path = os.path.join(PathUtils.get_api_root(), "UiElement", "GeneratedApis")

        if agent_type is not None:
            self.base_path = os.path.join(self.base_path, agent_type, application)

    def set_factory_folders(self, device):
        """
        This function defines which attributes of the device should be used to generate
        an API path.
        """
        factory_folders = [device.app_version]

        return factory_folders

    @staticmethod
    def find_best_match(path, search_value, default_value):
        """
        Overrides the parent class find_best_match function. For UI elements we want to grab the latest
        version if we cannot find a match, instead of using the base.
        """
        folders = [i.lower() for i in os.listdir(path) if os.path.isdir(path + os.sep + i)]
        folders.sort()
        return search_value if search_value.lower() in folders else folders[-1]

    def _get_application_type(self, device):
        if device.application.upper() in self.valid_applications:
            return device.application.upper()
        else:
            return None
