from extauto.common.WebElementHandler import *
from xiqse.defs.network.discovered.NetworkDiscoveredAddDevicesWebElementsDefinitions import *


class NetworkDiscoveredAddDevicesWebElements(NetworkDiscoveredAddDevicesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Action Buttons
    def get_add_button(self):
        """
        :return: 'Add' button in the Add Device dialog
        """
        return self.weh.get_element(self.add_button)

    def get_cancel_button(self):
        """
        :return: 'Cancel' button in the Add Device dialog
        """
        return self.weh.get_element(self.cancel_button)

    # Tabs
    def get_device_tab(self):
        """
        :return: 'Device' tab in the Add Device dialog
        """
        return self.weh.get_element(self.device_tab)

    def get_add_device_actions_tab(self):
        """
        :return: 'Add Device Actions' tab in the Add Device dialog
        """
        return self.weh.get_element(self.add_device_actions_tab)

    def get_device_annotation_tab(self):
        """
        :return: 'Device Annotation' tab in the Add Device dialog
        """
        return self.weh.get_element(self.device_annotation_tab)

    def get_ports_tab(self):
        """
        :return: 'Ports' tab in the Add Device dialog
        """
        return self.weh.get_element(self.ports_tab)

    # Device Annotation Tab Fields
    def get_nickname_field(self):
        """
        :return: 'Nickname' field in the Add Device dialog
        """
        return self.weh.get_element(self.nickname_field)

    def get_asset_tag_field(self):
        """
        :return: 'Asset Tag' field in the Add Device dialog
        """
        return self.weh.get_element(self.asset_tag_field)

    def get_user_data_1_field(self):
        """
        :return: 'User Data 1' field in the Add Device dialog
        """
        return self.weh.get_element(self.user_data_1_field)

    def get_user_data_2_field(self):
        """
        :return: 'User Data 2 field in the Add Device dialog
        """
        return self.weh.get_element(self.user_data_2_field)

    def get_user_data_3_field(self):
        """
        :return: 'User Data 3' field in the Add Device dialog
        """
        return self.weh.get_element(self.user_data_3_field)

    def get_user_data_4_field(self):
        """
        :return: 'User Data 4' field in the Add Device dialog
        """
        return self.weh.get_element(self.user_data_4_field)

    def get_note_field(self):
        """
        :return: 'Note' field in the Add Device dialog
        """
        return self.weh.get_element(self.note_field)
