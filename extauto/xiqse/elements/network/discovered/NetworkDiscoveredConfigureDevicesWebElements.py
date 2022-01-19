from common.WebElementHandler import *
from xiqse.defs.network.discovered.NetworkDiscoveredConfigureDevicesWebElementsDefinitions import *


class NetworkDiscoveredConfigureDevicesWebElements(NetworkDiscoveredConfigureDevicesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Action Buttons
    def get_save_button(self):
        """
        :return: 'Save' button in the Configure Device dialog
        """
        return self.weh.get_element(self.save_button)

    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Configure Device dialog
        """
        return self.weh.get_element(self.cancel_button)

