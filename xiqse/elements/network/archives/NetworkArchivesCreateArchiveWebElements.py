from common.WebElementHandler import *
from xiqse.defs.network.archives.NetworkArchivesCreateArchiveWebElementsDefinitions import *


class NetworkArchivesCreateArchiveWebElements(NetworkArchivesCreateArchiveWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_create_name_field(self):
        """
        :return: Name field in the Create Archive dialog
        """
        return self.weh.get_element(self.create_name_field)

    def get_create_frequency_dropdown(self):
        """
        :return: Frequency dropdown in the Create Archive dialog
        """
        return self.weh.get_element(self.create_frequency_dropdown)

    def get_create_next_button(self):
        """
        :return: Next button in the Create Archive dialog
        """
        return self.weh.get_element(self.create_next_button)

    def get_create_finish_button(self):
        """
        :return: Finish button in the Create Archive dialog
        """
        return self.weh.get_element(self.create_finish_button)

    def get_create_cancel_button(self):
        """
        :return: Cancel button in the Create Archive dialog
        """
        return self.weh.get_element(self.create_cancel_button)

    def get_create_select_device_expand_node(self, name):
        """
        :param name:  Name of tree node to expand
        :return:      Expander icon for the Select Devices tree node in the Create Archive dialog
        """
        return self.weh.get_template_element(self.create_select_device_expand_node, element_name=name)

    def get_create_select_device_node(self, name):
        """
        :param name:  Name of tree node to select
        :return:      Select Devices tree node in the Create Archive dialog
        """
        return self.weh.get_template_element(self.create_select_device_node, element_name=name)
