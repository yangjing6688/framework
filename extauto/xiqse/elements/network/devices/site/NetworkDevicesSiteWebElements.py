from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.site.NetworkDevicesSiteWebElementsDefinitions import NetworkDevicesSiteWebElementsDefinitions


class NetworkDevicesSiteWebElements(NetworkDevicesSiteWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_discover_tab(self):
        """
        :return: Discover Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.discover_tab)

    def get_actions_tab(self):
        """
        :return: Actions Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.actions_tab)

    def get_vrf_vlan_tab(self):
        """
        :return: VRF/VLAN Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.vrf_vlan_tab)

    def get_topologies_tab(self):
        """
        :return: Topologies Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.topologies_tab)

    def get_services_tab(self):
        """
        :return: Services Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.services_tab)

    def get_port_templates_tab(self):
        """
        :return: Port Templates Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.port_templates_tab)

    def get_ztp_device_defaults_tab(self):
        """
        :return: ZTP+ Device Defaults Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.ztp_device_defaults_tab)

    def get_endpoint_locations_tab(self):
        """
        :return: Endpoint Locations Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.endpoint_locations_tab)

    def get_analytics_tab(self):
        """
        :return: Analytics Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.analytics_tab)

    def get_custom_variables_tab(self):
        """
        :return: Custom Variables Sub Tab on the Network> Devices> Site page
        """
        return self.weh.get_element(self.custom_variables_tab)

    def get_discover_button(self):
        """
        :return: Discover button on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.discover_button)

    def get_save_button(self):
        """
        :return: Save button on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.save_button)

    def get_cancel_button(self):
        """
        :return: Cancel button on the Network> Devices> Site> Discover page
        """
        return self.weh.get_element(self.cancel_button)

    def get_site_unsaved_changes_dialog(self):
        """
        :return: 'Site - Unsaved Changes' dialog in the Network> Devices > Site page
        """
        return self.weh.get_element(self.site_unsaved_changes_dialog)

    def get_site_unsaved_changes_yes_button(self):
        """
        :return: Yes button in the 'Site - Unsaved Changes' dialog in the Network> Devices > Site page
        """
        return self.weh.get_element(self.site_unsaved_changes_yes_button)

    def get_site_unsaved_changes_no_button(self):
        """
        :return: No button in the 'Site - Unsaved Changes' dialog in the Network> Devices > Site page
        """
        return self.weh.get_element(self.site_unsaved_changes_no_button)

    def get_site_unsaved_changes_cancel_button(self):
        """
        :return: Cancel button in the 'Site - Unsaved Changes' dialog in the Network> Devices > Site page
        """
        return self.weh.get_element(self.site_unsaved_changes_cancel_button)
