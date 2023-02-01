from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.common.configure_device.NetworkCommonConfigureDeviceImportSiteConfigWebElementsDefinitions import NetworkCommonConfigureDeviceImportSiteConfigWebElementsDefinitions


class NetworkCommonConfigureDeviceImportSiteConfigWebElements(NetworkCommonConfigureDeviceImportSiteConfigWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_import_site_configuration_dialog(self):
        """
        :return: 'Import Site Configuration' dialog
        """
        return self.weh.get_element(self.import_site_config_dialog)

    def get_import_site_configuration_dialog_yes_button(self):
        """
        :return: 'Yes' button in the 'Import Site Configuration' dialog
        """
        return self.weh.get_element(self.yes_button)

    def get_import_site_configuration_dialog_no_button(self):
        """
        :return: 'No' button in the 'Import Site Configuration' dialog
        """
        return self.weh.get_element(self.no_button)
