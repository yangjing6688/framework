from extauto.common.WebElementHandler import *
from xiqse.defs.network.archives.NetworkArchivesWebElementsDefinitions import *


class NetworkArchivesWebElements(NetworkArchivesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_button(self):
        """
        :return: Create button on the Network> Archives page
        """
        return self.weh.get_element(self.create_button)

    def get_refresh_button(self):
        """
        :return: Refresh button on the Network> Archives page
        """
        return self.weh.get_element(self.refresh_button)

    def get_archive_tree_node(self, name):
        """
        :param name:  Name of tree node to return
        :return:      tree node with specified name
        """
        return self.weh.get_template_element(self.archive_tree_node, element_name=name)

    def get_archive_stamp_new_version_menu(self):
        """
        :return: Stamp New Version menu item from the context menu of an archive in the Archives tree
        """
        return self.weh.get_element(self.archive_stamp_menu)

    def get_archive_delete_menu(self):
        """
        :return: Delete menu item from the context menu of an archive in the Archives tree
        """
        return self.weh.get_element(self.archive_delete_menu)
