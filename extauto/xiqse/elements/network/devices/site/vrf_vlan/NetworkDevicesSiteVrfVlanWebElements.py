from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.site.vrf_vlan.NetworkDevicesSiteVrfVlanWebElementsDefinitions import NetworkDevicesSiteVrfVlanWebElementsDefinitions


class NetworkDevicesSiteVrfVlanWebElements(NetworkDevicesSiteVrfVlanWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_vlan_add_button(self):
        """
        :return: "Add..." button element on VLAN grid toolbar
        """
        return self.weh.get_element(self.vlan_add_button)

    def get_vlan_add_name_field(self):
        """
        :return: 'VLAN Name' field in the Add VLAN dialog
        """
        return self.weh.get_element(self.vlan_add_name_field)

    def get_vlan_add_vid_field(self):
        """
        :return: 'VID' field in the Add VLAN dialog
        """
        return self.weh.get_element(self.vlan_add_vid_field)

    def get_vlan_update_button(self):
        """
        :return: 'Update' button in the VLAN row editor
        """
        return self.weh.get_element(self.vlan_update_button)

    def get_vlan_cancel_button(self):
        """
        :return: 'Cancel' button in the VLAN row editor
        """
        return self.weh.get_element(self.vlan_cancel_button)
