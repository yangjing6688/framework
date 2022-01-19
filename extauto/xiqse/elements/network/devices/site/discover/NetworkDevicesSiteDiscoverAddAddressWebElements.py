from extauto.common.WebElementHandler import *
from xiqse.defs.network.devices.site.discover.NetworkDevicesSiteDiscoverAddAddressWebElementsDefinitions import *
import re


class NetworkDevicesSiteDiscoverAddAddressWebElements(NetworkDevicesSiteDiscoverAddAddressWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_add_address_discover_type_dropdown(self):
        """
        :return: 'Discover Type' dropdown in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_discover_type_dropdown)

    def get_add_address_subnet_mask_field(self):
        """
        :return: 'Subnet/Mask' text field in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_subnet_mask_field)

    def get_add_address_seed_address_field(self):
        """
        :return: 'Seed Address' text field in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_seed_address_field)

    def get_add_address_start_address_field(self):
        """
        :return: 'Start Address' text field in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_start_address_field)

    def get_add_address_end_address_field(self):
        """
        :return: 'End Address' text field in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_end_address_field)

    def get_add_address_dialog_ok_button(self):
        """
        :return: 'OK' button in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_ok_button)

    def get_add_address_dialog_cancel_button(self):
        """
        :return: 'Cancel' button in the Add Address dialog
        """
        return self.weh.get_element(self.add_address_dialog_cancel_button)
