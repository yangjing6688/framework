from common.WebElementHandler import *
from xiqse.defs.network.devices.tree_panel.NetworkDevicesTreePanelWebElementsDefinitions import *


class NetworkDevicesTreePanelWebElements(NetworkDevicesTreePanelWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_context_dropdown(self):
        """
        :return: Context dropdown for the tree panel on the Network> Devices page
        """
        return self.weh.get_element(self.context_dropdown)

    def get_site_tree_node(self, site="World"):
        """
        :param site: optional name of the site tree node;  default is "World"
        :return: Site Tree Node on the Network> Devices page
        """
        return self.weh.get_template_element(self.site_tree_node, element_name=site)

    def get_tree_action_menu(self):
        """
        :return: Action Menu for the tree panel on the Network> Devices page
        """
        return self.weh.get_element(self.tree_action_menu)

    def get_maps_sites_menu(self):
        """
        :return: 'Maps/Sites' Menu in the tree action menu on the Network> Devices page
        """
        elements = self.weh.get_elements(self.maps_sites_menu)
        return self.weh.get_displayed_element(elements)

    def get_create_site_menu(self):
        """
        :return: 'Create Site...' Menu in the tree action menu on the Network> Devices page
        """
        elements = self.weh.get_elements(self.create_site_menu)
        return self.weh.get_displayed_element(elements)

    def get_delete_site_menu(self):
        """
        :return: 'Delete Site' Menu in the tree action menu on the Network> Devices page
        """
        elements = self.weh.get_elements(self.delete_site_menu)
        return self.weh.get_displayed_element(elements)
