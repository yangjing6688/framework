from common.WebElementHandler import *
from xiqse.defs.network.devices.tree_panel.NetworkDevicesTreePanelDeleteSiteWebElementsDefinitions import *


class NetworkDevicesTreePanelDeleteSiteWebElements(NetworkDevicesTreePanelDeleteSiteWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_confirm_delete_site_dialog(self):
        """
        :return: 'Delete Site' confirmation dialog
        """
        return self.weh.get_element(self.confirm_delete_site_dialog)

    def get_yes_button(self):
        """
        :return: Yes button in the Delete Site confirmation dialog
        """
        return self.weh.get_element(self.yes_button)

    def get_no_button(self):
        """
        :return: No button in the Delete Site confirmation dialog
        """
        return self.weh.get_element(self.no_button)
