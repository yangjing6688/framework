from common.WebElementHandler import *
from xiqse.defs.network.devices.tree_panel.NetworkDevicesTreePanelCreateSiteWebElementsDefinitions import *


class NetworkDevicesTreePanelCreateSiteWebElements(NetworkDevicesTreePanelCreateSiteWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_name_field(self):
        """
        :return: 'Name' field in the Create Site dialog
        """
        return self.weh.get_element(self.name_field)

    def get_ok_button(self):
        """
        :return: 'OK' button in the Create Site dialog
        """
        return self.weh.get_element(self.ok_button)

    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Create Site dialog
        """
        return self.weh.get_element(self.cancel_button)
